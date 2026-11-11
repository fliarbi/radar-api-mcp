"""OAuth 2.1 authorization server for connector sign-in.

The gap this closes: header-capable clients (Claude Code, Cursor, n8n) can already send
`Authorization: Bearer rdr_…`, but ChatGPT and non-beta claude.ai custom connectors speak
only OAuth with dynamic client registration. This module is that OAuth front-end.

It does not invent a new credential. The access token it issues *is* a freshly-minted `rdr_`
key for the signed-in account, so every resource server that already accepts an rdr_ key
(this gateway's own Companies Radar MCP, Prism, Prism News) accepts an OAuth-issued token unchanged,
and metering stays 1:1 with the key. One grant owns exactly one key; a refresh re-mints the
key and revokes the previous one. Revoking the key (from the key console) ends the grant.

Design points that matter for security:
  * PKCE S256 is required on every authorization. Public clients carry no secret; the code
    verifier is the proof.
  * Authorization codes are single-use (deleted in the same transaction they are read) and
    short-lived; redirect_uri is matched exactly against the value registered at DCR.
  * The consent step authenticates the human with the Companies Radar session header the dashboard
    already holds (X-Auth-Token -> Companies Radar /auth/me). Because that is a header the page reads
    from same-origin storage, a cross-origin page cannot forge the approval (no ambient
    cookie is trusted), which is what keeps the consent screen free of a CSRF token.

Inert until RADAR_OAUTH_ISSUER is set; register_oauth_routes is a no-op without it.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import re
import secrets
import time
from pathlib import Path
from urllib.parse import urlencode, urlsplit

from fastapi import Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, Response

from .errors import RadarError

CODE_TTL = 300                 # authorization code lifetime (seconds)
ACCESS_TTL_DAYS = 30           # issued rdr_ key lifetime; expires_in reports this
CONNECTOR_KEY_SCOPES = ("*",)  # data groups the connector key carries (contacts still opt-in)
SCOPES_SUPPORTED = ("mcp",)    # coarse OAuth scope; granularity lives in the key's data groups
_STATIC = Path(__file__).parent / "static"

_CLIENT_ID = re.compile(r"rdrc_[a-f0-9]{32}")
_CHALLENGE = re.compile(r"[A-Za-z0-9._~-]{43,128}")
_VERIFIER = re.compile(r"[A-Za-z0-9._~-]{43,128}")
_SCOPE = re.compile(r"[A-Za-z0-9 :._/-]{0,200}")

CORS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "authorization, content-type, mcp-protocol-version",
    "Access-Control-Max-Age": "3600",
}


def _b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def _sha(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def _valid_redirect(uri) -> bool:
    """https anywhere, or http only on loopback. No fragment, no whitespace."""
    if not isinstance(uri, str) or not 1 <= len(uri) <= 2048 or any(c in uri for c in "\r\n \t"):
        return False
    u = urlsplit(uri)
    if u.fragment:
        return False
    if u.scheme == "https" and u.hostname:
        return True
    return u.scheme == "http" and u.hostname in {"127.0.0.1", "localhost", "::1"}


def _pkce_ok(verifier: str, challenge: str) -> bool:
    if not verifier or not _VERIFIER.fullmatch(verifier):
        return False
    computed = _b64url(hashlib.sha256(verifier.encode()).digest())
    return hmac.compare_digest(computed, challenge or "")


def _clean_state(value) -> str:
    if not isinstance(value, str):
        return ""
    return "".join(c for c in value if c.isprintable())[:512]


class OAuthError(Exception):
    """An OAuth error rendered per RFC 6749 §5.2 (token/registration JSON bodies)."""

    def __init__(self, error: str, description: str, status: int = 400):
        super().__init__(description)
        self.error, self.description, self.status = error, description, status


class OAuth:
    def __init__(self, accounts, settings):
        self.accounts = accounts
        self.settings = settings
        self.issuer = settings.oauth_issuer
        self._schema()

    def _schema(self):
        with self.accounts.db() as db:
            db.executescript("""
            CREATE TABLE IF NOT EXISTS oauth_clients (
              id TEXT PRIMARY KEY, secret_hash TEXT NOT NULL DEFAULT '', name TEXT NOT NULL,
              redirect_uris TEXT NOT NULL, auth_method TEXT NOT NULL DEFAULT 'none', created INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS oauth_codes (
              code_hash TEXT PRIMARY KEY, client_id TEXT NOT NULL, account TEXT NOT NULL,
              redirect_uri TEXT NOT NULL, challenge TEXT NOT NULL, scope TEXT NOT NULL,
              created INTEGER NOT NULL, expires INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS oauth_grants (
              id TEXT PRIMARY KEY, account TEXT NOT NULL, client_id TEXT NOT NULL, key_id TEXT NOT NULL,
              refresh_hash TEXT UNIQUE NOT NULL, scope TEXT NOT NULL, created INTEGER NOT NULL, updated INTEGER NOT NULL);
            CREATE INDEX IF NOT EXISTS oauth_grant_pair ON oauth_grants(account,client_id);
            """)

    # -- Dynamic client registration (RFC 7591) ---------------------------------------------
    def register_client(self, body: dict, peer: str) -> dict:
        self.accounts.rate("oauth-reg:" + self.accounts._peer_key(peer or ""), 20, 3600)
        if not isinstance(body, dict):
            raise OAuthError("invalid_client_metadata", "Send a JSON client metadata object")
        uris = body.get("redirect_uris")
        if not isinstance(uris, list) or not 1 <= len(uris) <= 5 or not all(_valid_redirect(u) for u in uris):
            raise OAuthError("invalid_redirect_uri",
                             "redirect_uris must be 1-5 https URLs (http only for loopback), no fragment")
        method = body.get("token_endpoint_auth_method", "none")
        if method not in {"none", "client_secret_post", "client_secret_basic"}:
            raise OAuthError("invalid_client_metadata", "Unsupported token_endpoint_auth_method")
        for grant in body.get("grant_types", ["authorization_code"]) or []:
            if grant not in {"authorization_code", "refresh_token"}:
                raise OAuthError("invalid_client_metadata", f"Unsupported grant_type: {grant}")
        name = str(body.get("client_name") or "MCP client")[:200]
        client_id = "rdrc_" + secrets.token_hex(16)
        secret, secret_hash = "", ""
        if method != "none":
            secret = secrets.token_urlsafe(32)
            secret_hash = _sha(secret)
        now = int(time.time())
        with self.accounts.db() as db:
            db.execute("INSERT INTO oauth_clients VALUES (?,?,?,?,?,?)",
                       (client_id, secret_hash, name, json.dumps(list(uris)), method, now))
        out = {"client_id": client_id, "client_id_issued_at": now, "redirect_uris": list(uris),
               "token_endpoint_auth_method": method, "grant_types": ["authorization_code", "refresh_token"],
               "response_types": ["code"], "client_name": name}
        if secret:
            out["client_secret"] = secret
            out["client_secret_expires_at"] = 0
        return out

    def client(self, client_id: str) -> dict | None:
        if not isinstance(client_id, str) or not _CLIENT_ID.fullmatch(client_id):
            return None
        with self.accounts.db() as db:
            row = db.execute("SELECT * FROM oauth_clients WHERE id=?", (client_id,)).fetchone()
        return dict(row) if row else None

    def _check_client_secret(self, client: dict, supplied: str) -> None:
        if client["auth_method"] == "none":
            return
        if not supplied or not hmac.compare_digest(_sha(supplied), client["secret_hash"]):
            raise OAuthError("invalid_client", "Client authentication failed", 401)

    # -- Authorization code -----------------------------------------------------------------
    def issue_code(self, client_id: str, account: str, redirect_uri: str, challenge: str, scope: str) -> str:
        code = secrets.token_urlsafe(32)
        now = int(time.time())
        with self.accounts.db() as db:
            db.execute("DELETE FROM oauth_codes WHERE expires<=?", (now,))
            db.execute("INSERT INTO oauth_codes VALUES (?,?,?,?,?,?,?,?)",
                       (_sha(code), client_id, account, redirect_uri, challenge, scope, now, now + CODE_TTL))
        return code

    def _redeem_code(self, code: str, client_id: str, redirect_uri: str, verifier: str) -> tuple[str, str]:
        if not code:
            raise OAuthError("invalid_grant", "Missing authorization code")
        now = int(time.time())
        with self.accounts.db() as db:
            row = db.execute("SELECT * FROM oauth_codes WHERE code_hash=?", (_sha(code),)).fetchone()
            if row:
                db.execute("DELETE FROM oauth_codes WHERE code_hash=?", (_sha(code),))  # single use
        if not row or row["expires"] <= now:
            raise OAuthError("invalid_grant", "Authorization code is invalid or expired")
        if not hmac.compare_digest(row["client_id"], client_id) or not hmac.compare_digest(row["redirect_uri"], redirect_uri):
            raise OAuthError("invalid_grant", "Authorization code does not match this client or redirect_uri")
        if not _pkce_ok(verifier, row["challenge"]):
            raise OAuthError("invalid_grant", "PKCE verification failed")
        return row["account"], row["scope"]

    # -- Token issuance ---------------------------------------------------------------------
    def _mint(self, account: str, client_id: str, scope: str, old_key_ids=()) -> dict:
        """Mint the connector key, record/rotate the grant, revoke superseded keys."""
        key, key_id, expires = self.accounts.issue_connector_key(
            account, f"Connector {client_id}", CONNECTOR_KEY_SCOPES, ACCESS_TTL_DAYS)
        refresh = secrets.token_urlsafe(32)
        return {"key": key, "key_id": key_id, "expires": expires, "refresh": refresh}

    def exchange_code(self, code: str, client_id: str, redirect_uri: str, verifier: str) -> dict:
        account, scope = self._redeem_code(code, client_id, redirect_uri, verifier)
        minted = self._mint(account, client_id, scope)
        now = int(time.time())
        gid = secrets.token_hex(16)
        with self.accounts.db() as db:
            superseded = [g["key_id"] for g in db.execute(
                "SELECT key_id FROM oauth_grants WHERE account=? AND client_id=?", (account, client_id)).fetchall()]
            db.execute("DELETE FROM oauth_grants WHERE account=? AND client_id=?", (account, client_id))
            db.execute("INSERT INTO oauth_grants VALUES (?,?,?,?,?,?,?,?)",
                       (gid, account, client_id, minted["key_id"], _sha(minted["refresh"]), scope, now, now))
            for kid in superseded:
                db.execute("UPDATE api_keys SET revoked=1 WHERE account=? AND id=?", (account, kid))
        return self._token_response(minted, scope)

    def refresh(self, refresh_token: str, client_id: str) -> dict:
        if not refresh_token:
            raise OAuthError("invalid_grant", "Missing refresh_token")
        with self.accounts.db() as db:
            row = db.execute("SELECT * FROM oauth_grants WHERE refresh_hash=?", (_sha(refresh_token),)).fetchone()
        if not row or not hmac.compare_digest(row["client_id"], client_id):
            raise OAuthError("invalid_grant", "Refresh token is invalid")
        minted = self._mint(row["account"], client_id, row["scope"])
        now = int(time.time())
        with self.accounts.db() as db:
            # Rotate only if the grant still exists (not revoked meanwhile), else drop the new key.
            still = db.execute("SELECT key_id FROM oauth_grants WHERE id=?", (row["id"],)).fetchone()
            if not still:
                db.execute("UPDATE api_keys SET revoked=1 WHERE account=? AND id=?", (row["account"], minted["key_id"]))
                raise OAuthError("invalid_grant", "Refresh token is invalid")
            db.execute("UPDATE oauth_grants SET key_id=?, refresh_hash=?, updated=? WHERE id=?",
                       (minted["key_id"], _sha(minted["refresh"]), now, row["id"]))
            db.execute("UPDATE api_keys SET revoked=1 WHERE account=? AND id=?", (row["account"], row["key_id"]))
        return self._token_response(minted, row["scope"])

    @staticmethod
    def _token_response(minted: dict, scope: str) -> dict:
        return {"access_token": minted["key"], "token_type": "Bearer",
                "expires_in": max(0, minted["expires"] - int(time.time())),
                "refresh_token": minted["refresh"], "scope": scope or "mcp"}

    def metadata(self) -> dict:
        i = self.issuer
        return {
            "issuer": i,
            "authorization_endpoint": self.settings.oauth_authorize_url or i + "/oauth/authorize",
            "token_endpoint": i + "/oauth/token",
            "registration_endpoint": i + "/oauth/register",
            "response_types_supported": ["code"],
            "grant_types_supported": ["authorization_code", "refresh_token"],
            "code_challenge_methods_supported": ["S256"],
            "token_endpoint_auth_methods_supported": ["none", "client_secret_post", "client_secret_basic"],
            "scopes_supported": list(SCOPES_SUPPORTED),
            "service_documentation": self.settings.public_url or self.settings.public_prism_url or i,
            **({"op_policy_uri": self.settings.public_privacy_url} if self.settings.public_privacy_url else {}),
            **({"op_tos_uri": self.settings.public_terms_url} if self.settings.public_terms_url else {}),
        }


    def resource_metadata(self) -> dict:
        """RFC 9728: tells a client holding only the MCP URL which server signs users in."""
        s = self.settings
        out = {"resource": s.public_url + "/mcp", "authorization_servers": [self.issuer],
               "bearer_methods_supported": ["header"], "scopes_supported": list(SCOPES_SUPPORTED),
               "resource_name": "Companies Radar"}
        if s.public_developer_url:
            out["resource_documentation"] = s.public_developer_url
        if s.public_privacy_url:
            out["resource_policy_uri"] = s.public_privacy_url
        if s.public_terms_url:
            out["resource_tos_uri"] = s.public_terms_url
        return out


def _consent_page(oauth: OAuth, client_name: str, params: dict) -> HTMLResponse:
    config = json.dumps({"client_name": client_name, "params": params}).replace("<", "\\u003c")
    html = (_STATIC / "oauth_consent.html").read_text()
    version = hashlib.sha256((_STATIC / "oauth.js").read_bytes()).hexdigest()[:12]
    html = html.replace("__OAUTH_CONFIG__", config).replace('"oauth.js"', f'"oauth.js?v={version}"')
    return HTMLResponse(html, headers={
        "Cache-Control": "no-store", "X-Robots-Tag": "noindex, nofollow", "Referrer-Policy": "no-referrer",
        "X-Content-Type-Options": "nosniff",
        "Content-Security-Policy": ("default-src 'none'; script-src 'self'; style-src 'self' 'unsafe-inline'; "
                                    "connect-src 'self'; img-src 'self' data:; base-uri 'none'; "
                                    "form-action 'none'; frame-ancestors 'none'")})


def _error_page(message: str, status: int = 400) -> HTMLResponse:
    body = ("<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'>"
            "<title>Sign-in error</title><body style='font:16px system-ui;margin:3rem auto;max-width:34rem;padding:0 1rem'>"
            f"<h1 style='font-size:1.3rem'>This connection can't be completed</h1><p>{message}</p>"
            "<p style='color:#666'>Nothing was authorized. You can close this window.</p>")
    return HTMLResponse(body, status_code=status, headers={"Cache-Control": "no-store", "X-Robots-Tag": "noindex"})


def register_oauth_routes(app, accounts, oauth: OAuth | None):
    """Mount the OAuth endpoints. A no-op when OAuth is not configured (no issuer)."""
    if not oauth or not oauth.issuer:
        return

    def _preflight():
        return Response(status_code=204, headers=CORS)

    @app.get("/oauth/oauth.js", include_in_schema=False)
    async def oauth_js():
        return FileResponse(_STATIC / "oauth.js", media_type="application/javascript",
                            headers={"Cache-Control": "public, max-age=3600", "X-Content-Type-Options": "nosniff"})

    async def as_metadata(request: Request):
        if request.method == "OPTIONS":
            return _preflight()
        return JSONResponse(oauth.metadata(), headers={**CORS, "Cache-Control": "public, max-age=3600"})

    # Clients look for the document at the plain well-known path, with the issuer's path
    # appended (RFC 8414) and under the OpenID name; serve the same document at each.
    issuer_path = urlsplit(oauth.issuer).path.rstrip("/")
    for base in ("/.well-known/oauth-authorization-server", "/.well-known/openid-configuration"):
        for path in dict.fromkeys((base, base + issuer_path)):
            app.add_api_route(path, as_metadata, methods=["GET", "OPTIONS"], include_in_schema=False)

    if oauth.settings.public_url:
        async def resource_metadata(request: Request):
            if request.method == "OPTIONS":
                return _preflight()
            return JSONResponse(oauth.resource_metadata(), headers={**CORS, "Cache-Control": "public, max-age=3600"})

        for path in ("/.well-known/oauth-protected-resource", "/.well-known/oauth-protected-resource/mcp"):
            app.add_api_route(path, resource_metadata, methods=["GET", "OPTIONS"], include_in_schema=False)

    @app.api_route("/oauth/register", methods=["POST", "OPTIONS"], include_in_schema=False)
    async def register(request: Request):
        if request.method == "OPTIONS":
            return _preflight()
        peer = (request.scope.get("client") or ("",))[0]
        try:
            body = await request.json()
        except ValueError:
            return JSONResponse({"error": "invalid_client_metadata", "error_description": "Body must be JSON"},
                                status_code=400, headers=CORS)
        try:
            return JSONResponse(oauth.register_client(body, peer), status_code=201, headers={**CORS, "Cache-Control": "no-store"})
        except OAuthError as e:
            return JSONResponse({"error": e.error, "error_description": e.description}, status_code=e.status, headers=CORS)
        except RadarError as e:
            return JSONResponse({"error": "temporarily_unavailable", "error_description": e.message},
                                status_code=e.status, headers=CORS)

    @app.api_route("/oauth/authorize", methods=["GET", "POST", "OPTIONS"], include_in_schema=False)
    async def authorize(request: Request):
        if request.method == "OPTIONS":
            return _preflight()
        src = request.query_params if request.method == "GET" else (await request.form())
        client_id = src.get("client_id", "")
        redirect_uri = src.get("redirect_uri", "")
        client = oauth.client(client_id)
        # Before consent, an unknown client or unregistered redirect can only be shown as an error:
        # never redirect to a URI the client did not register.
        if not client:
            return _error_page("The application is not registered for sign-in.")
        if redirect_uri not in json.loads(client["redirect_uris"]):
            return _error_page("The redirect address does not match this application's registration.")
        response_type = src.get("response_type", "")
        challenge = src.get("code_challenge", "")
        method = src.get("code_challenge_method", "")
        scope = src.get("scope", "") or "mcp"
        state = _clean_state(src.get("state", ""))
        invalid = (None if response_type == "code"
                   else "Only response_type=code is supported.") or (
                   None if method == "S256" else "PKCE with S256 is required.") or (
                   None if _CHALLENGE.fullmatch(challenge or "") else "A valid PKCE code_challenge is required.") or (
                   None if _SCOPE.fullmatch(scope) else "The requested scope is not allowed.")
        if invalid:
            return _error_page(invalid)
        params = {"client_id": client_id, "redirect_uri": redirect_uri, "response_type": "code",
                  "code_challenge": challenge, "code_challenge_method": "S256", "scope": scope, "state": state}
        if request.method == "GET":
            return _consent_page(oauth, client["name"], params)
        # POST = the consent form approving access; authenticate the human via the Companies Radar session.
        try:
            identity = await accounts.identity(request.headers.get("X-Auth-Token", ""),
                                               request.scope.get("radar.client_ip", ""))
        except RadarError as e:
            return JSONResponse({"error": "login_required", "error_description": e.message},
                                status_code=e.status, headers={**CORS, "Cache-Control": "no-store"})
        code = oauth.issue_code(client_id, identity.id, redirect_uri, challenge, scope)
        sep = "&" if urlsplit(redirect_uri).query else "?"
        location = f"{redirect_uri}{sep}{urlencode({'code': code, 'state': state} if state else {'code': code})}"
        return JSONResponse({"redirect": location}, headers={**CORS, "Cache-Control": "no-store"})

    @app.api_route("/oauth/token", methods=["POST", "OPTIONS"], include_in_schema=False)
    async def token(request: Request):
        if request.method == "OPTIONS":
            return _preflight()
        try:
            form = await request.form()
        except Exception:
            form = {}

        def field(name):
            value = form.get(name, "")
            return value if isinstance(value, str) else ""

        # Client authentication: Basic header or client_secret_post.
        auth = request.headers.get("authorization", "")
        basic_id = basic_secret = ""
        if auth.lower().startswith("basic "):
            try:
                basic_id, _, basic_secret = base64.b64decode(auth[6:].strip()).decode().partition(":")
            except Exception:
                return JSONResponse({"error": "invalid_client", "error_description": "Malformed Basic credentials"},
                                    status_code=401, headers={**CORS, "WWW-Authenticate": "Basic"})
        client_id = basic_id or field("client_id")
        client_secret = basic_secret or field("client_secret")
        try:
            client = oauth.client(client_id)
            if not client:
                raise OAuthError("invalid_client", "Unknown client", 401)
            oauth._check_client_secret(client, client_secret)
            grant_type = field("grant_type")
            if grant_type == "authorization_code":
                out = oauth.exchange_code(field("code"), client_id, field("redirect_uri"), field("code_verifier"))
            elif grant_type == "refresh_token":
                out = oauth.refresh(field("refresh_token"), client_id)
            else:
                raise OAuthError("unsupported_grant_type", "Use authorization_code or refresh_token")
        except OAuthError as e:
            headers = {**CORS, "Cache-Control": "no-store"}
            if e.error == "invalid_client":
                headers["WWW-Authenticate"] = "Basic"
            return JSONResponse({"error": e.error, "error_description": e.description}, status_code=e.status, headers=headers)
        except RadarError as e:
            return JSONResponse({"error": "temporarily_unavailable", "error_description": e.message},
                                status_code=e.status, headers={**CORS, "Cache-Control": "no-store"})
        return JSONResponse(out, headers={**CORS, "Cache-Control": "no-store", "Pragma": "no-cache"})
