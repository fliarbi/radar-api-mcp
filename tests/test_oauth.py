"""OAuth 2.1 connector flow: DCR, authorization-code + PKCE, token, refresh, and the
negative paths that keep it safe. Companies Radar identity is mocked exactly as in test_accounts.py:
session-a -> account "a". No live gateway or Companies Radar is contacted."""
from __future__ import annotations

import asyncio
import base64
import hashlib
import re
from urllib.parse import parse_qs, urlsplit

import httpx
import pytest
from cryptography.fernet import Fernet
from fastapi.testclient import TestClient

from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.accounts import Accounts
from radar_api.upstream import Upstream

from conftest import payload_for

ISSUER = "https://127.0.0.1"
REDIRECT = "https://client.example/callback"
VERIFIER = "abcdefghijklmnopqrstuvwxyz0123456789-._~ABCDEFG"  # 46 chars, PKCE-legal
CHALLENGE = base64.urlsafe_b64encode(hashlib.sha256(VERIFIER.encode()).digest()).rstrip(b"=").decode()


def _respond(request):
    if request.url.path == "/auth/me":
        token = request.headers.get("X-Auth-Token", "")
        if token not in {"session-a", "session-b"}:
            return httpx.Response(401)
        return httpx.Response(200, json={"user": {"_id": token[-1], "email_verified": True},
            "plan": "business", "plan_details": {"features": ["api_access"], "searches_per_month": 5000,
            "company_tracking": 1000}})
    return httpx.Response(200, json=payload_for(request.url.path))


def _make_app(issuer=ISSUER, tmp_path=None):
    settings = Settings(accounts_enabled=True, accounts_db=str(tmp_path / "accounts.db"),
        encryption_key=Fernet.generate_key().decode(), radar_url="http://radar.local",
        oauth_issuer=issuer, allowed_hosts=("testserver", "127.0.0.1", "localhost"),
        credit_price_cents=2, razorpay_key_id="rzp_test", razorpay_key_secret="s", razorpay_webhook_secret="h")
    transport = httpx.MockTransport(_respond)
    accounts = Accounts(settings, transport)
    app = create_app(settings, Upstream(settings, transport), accounts)
    return app, accounts


@pytest.fixture
def oauth(tmp_path):
    app, accounts = _make_app(tmp_path=tmp_path)
    with TestClient(app) as client:
        yield client, accounts


def register(client, redirect_uris=(REDIRECT,), name="Test Connector", method="none"):
    r = client.post("/oauth/register", json={"redirect_uris": list(redirect_uris),
                                             "client_name": name, "token_endpoint_auth_method": method})
    return r


def authorize_code(client, client_id, redirect=REDIRECT, challenge=CHALLENGE, method="S256",
                   state="xyz", session="session-a"):
    params = {"response_type": "code", "client_id": client_id, "redirect_uri": redirect,
              "code_challenge": challenge, "code_challenge_method": method, "scope": "mcp", "state": state}
    page = client.get("/oauth/authorize", params=params)
    assert page.status_code == 200 and "Authorize access" in page.text
    assert "frame-ancestors 'none'" in page.headers["content-security-policy"]
    approve = client.post("/oauth/authorize", data=params, headers={"X-Auth-Token": session})
    return page, approve


# -- Discovery -----------------------------------------------------------------------------
def test_metadata_is_public_and_cross_origin(oauth):
    client, _ = oauth
    r = client.get("/.well-known/oauth-authorization-server", headers={"Origin": "https://chatgpt.com"})
    assert r.status_code == 200
    meta = r.json()
    assert meta["issuer"] == ISSUER
    assert meta["authorization_endpoint"] == ISSUER + "/oauth/authorize"
    assert meta["token_endpoint"] == ISSUER + "/oauth/token"
    assert meta["registration_endpoint"] == ISSUER + "/oauth/register"
    assert meta["code_challenge_methods_supported"] == ["S256"]
    assert "authorization_code" in meta["grant_types_supported"] and "refresh_token" in meta["grant_types_supported"]
    assert r.headers["access-control-allow-origin"] == "*"


def test_token_preflight(oauth):
    client, _ = oauth
    r = client.options("/oauth/token", headers={"Origin": "https://chatgpt.com",
                        "Access-Control-Request-Method": "POST"})
    assert r.status_code == 204
    assert r.headers["access-control-allow-origin"] == "*"
    assert "POST" in r.headers["access-control-allow-methods"]


def test_disabled_without_issuer(tmp_path):
    app, _ = _make_app(issuer="", tmp_path=tmp_path)
    with TestClient(app) as client:
        assert client.get("/.well-known/oauth-authorization-server").status_code == 404
        assert client.post("/oauth/register", json={"redirect_uris": [REDIRECT]}).status_code == 404


# -- Dynamic client registration -----------------------------------------------------------
def test_dcr_public_client(oauth):
    client, _ = oauth
    r = register(client)
    assert r.status_code == 201
    body = r.json()
    assert re.fullmatch(r"rdrc_[a-f0-9]{32}", body["client_id"])
    assert body["token_endpoint_auth_method"] == "none"
    assert "client_secret" not in body
    assert body["redirect_uris"] == [REDIRECT]


def test_dcr_confidential_client_gets_secret(oauth):
    client, _ = oauth
    body = register(client, method="client_secret_post").json()
    assert body["token_endpoint_auth_method"] == "client_secret_post"
    assert len(body["client_secret"]) >= 20


def test_dcr_rejects_bad_redirect(oauth):
    client, _ = oauth
    for bad in ["http://evil.example/cb", "ftp://x/y", "https://ok.example/cb#frag", "not a url"]:
        r = client.post("/oauth/register", json={"redirect_uris": [bad]})
        assert r.status_code == 400 and r.json()["error"] == "invalid_redirect_uri"


# -- Full authorization-code flow ----------------------------------------------------------
def test_full_flow_issues_working_key(oauth):
    client, accounts = oauth
    cid = register(client).json()["client_id"]
    _, approve = authorize_code(client, cid)
    assert approve.status_code == 200
    location = approve.json()["redirect"]
    q = parse_qs(urlsplit(location).query)
    assert location.startswith(REDIRECT) and q["state"] == ["xyz"]
    code = q["code"][0]

    tok = client.post("/oauth/token", data={"grant_type": "authorization_code", "code": code,
                      "redirect_uri": REDIRECT, "client_id": cid, "code_verifier": VERIFIER})
    assert tok.status_code == 200
    data = tok.json()
    assert data["token_type"] == "Bearer" and data["expires_in"] > 0
    access, refresh = data["access_token"], data["refresh_token"]
    assert re.fullmatch(r"rdr_[a-f0-9]{64}", access)

    # The issued token is a real, usable key for the right account.
    info = asyncio.run(accounts.introspect(access))
    assert info["active"] is True and info["account_id"] == "a"

    # Refresh rotates the key and invalidates the old one.
    ref = client.post("/oauth/token", data={"grant_type": "refresh_token",
                      "refresh_token": refresh, "client_id": cid})
    assert ref.status_code == 200
    new_access = ref.json()["access_token"]
    assert new_access != access
    assert asyncio.run(accounts.introspect(new_access))["active"] is True
    assert asyncio.run(accounts.introspect(access))["active"] is False  # old key revoked on refresh


def test_reauthorize_replaces_prior_key(oauth):
    client, accounts = oauth
    cid = register(client).json()["client_id"]
    first = client.post("/oauth/token", data=_code_exchange(client, cid))
    second = client.post("/oauth/token", data=_code_exchange(client, cid))
    a1, a2 = first.json()["access_token"], second.json()["access_token"]
    assert a1 != a2
    assert asyncio.run(accounts.introspect(a1))["active"] is False  # superseded
    assert asyncio.run(accounts.introspect(a2))["active"] is True


def _code_exchange(client, cid):
    _, approve = authorize_code(client, cid)
    code = parse_qs(urlsplit(approve.json()["redirect"]).query)["code"][0]
    return {"grant_type": "authorization_code", "code": code, "redirect_uri": REDIRECT,
            "client_id": cid, "code_verifier": VERIFIER}


# -- Negative paths ------------------------------------------------------------------------
def test_code_is_single_use(oauth):
    client, _ = oauth
    cid = register(client).json()["client_id"]
    body = _code_exchange(client, cid)
    assert client.post("/oauth/token", data=body).status_code == 200
    again = client.post("/oauth/token", data=body)
    assert again.status_code == 400 and again.json()["error"] == "invalid_grant"


def test_wrong_pkce_verifier_rejected(oauth):
    client, _ = oauth
    cid = register(client).json()["client_id"]
    body = _code_exchange(client, cid)
    body["code_verifier"] = "x" * 46
    r = client.post("/oauth/token", data=body)
    assert r.status_code == 400 and r.json()["error"] == "invalid_grant"


def test_redirect_uri_must_match_at_token(oauth):
    client, _ = oauth
    cid = register(client, redirect_uris=[REDIRECT, "https://client.example/other"]).json()["client_id"]
    body = _code_exchange(client, cid)
    body["redirect_uri"] = "https://client.example/other"
    r = client.post("/oauth/token", data=body)
    assert r.status_code == 400 and r.json()["error"] == "invalid_grant"


def test_authorize_rejects_unknown_client(oauth):
    client, _ = oauth
    r = client.get("/oauth/authorize", params={"response_type": "code", "client_id": "rdrc_" + "0" * 32,
                   "redirect_uri": REDIRECT, "code_challenge": CHALLENGE, "code_challenge_method": "S256"})
    assert r.status_code == 400 and "not registered" in r.text


def test_authorize_rejects_unregistered_redirect(oauth):
    client, _ = oauth
    cid = register(client).json()["client_id"]
    r = client.get("/oauth/authorize", params={"response_type": "code", "client_id": cid,
                   "redirect_uri": "https://attacker.example/cb", "code_challenge": CHALLENGE,
                   "code_challenge_method": "S256"})
    assert r.status_code == 400 and "redirect address" in r.text


def test_authorize_requires_s256(oauth):
    client, _ = oauth
    cid = register(client).json()["client_id"]
    r = client.get("/oauth/authorize", params={"response_type": "code", "client_id": cid,
                   "redirect_uri": REDIRECT, "code_challenge": CHALLENGE, "code_challenge_method": "plain"})
    assert r.status_code == 400 and "PKCE" in r.text


def test_consent_requires_valid_session(oauth):
    client, _ = oauth
    cid = register(client).json()["client_id"]
    params = {"response_type": "code", "client_id": cid, "redirect_uri": REDIRECT,
              "code_challenge": CHALLENGE, "code_challenge_method": "S256", "scope": "mcp", "state": "xyz"}
    r = client.post("/oauth/authorize", data=params, headers={"X-Auth-Token": "not-a-session"})
    assert r.status_code == 401 and r.json()["error"] == "login_required"


def test_confidential_client_secret_enforced(oauth):
    client, _ = oauth
    reg = register(client, method="client_secret_post").json()
    cid, secret = reg["client_id"], reg["client_secret"]
    body = _code_exchange(client, cid)
    # Missing secret -> invalid_client.
    assert client.post("/oauth/token", data=body).status_code == 401
    # Correct secret -> works.
    body2 = _code_exchange(client, cid)
    body2["client_secret"] = secret
    assert client.post("/oauth/token", data=body2).status_code == 200
