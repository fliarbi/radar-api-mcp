# OAuth connector sign-in

Header-capable clients (Claude Code, Cursor, n8n) send `Authorization: Bearer rdr_…`
directly. ChatGPT and non-beta claude.ai custom connectors speak only OAuth with dynamic
client registration. This gateway is the OAuth 2.1 authorization server for them.

It does not introduce a new credential. **The access token it issues is a freshly-minted
`rdr_` API key** for the signed-in account, so every resource server that already accepts an
`rdr_` key — this gateway's own Companies Radar MCP, Prism, Prism News — accepts an OAuth-issued token
unchanged, and credit metering stays 1:1 with the key. One grant owns exactly one key; a
refresh re-mints the key and revokes the previous one.

## What a client does

0. **Find the sign-in server** — an unauthenticated `POST /mcp` returns `401` with
   `WWW-Authenticate: Bearer resource_metadata="…/.well-known/oauth-protected-resource/mcp"`
   (RFC 9728); that document names the issuer. Requires `RADAR_PUBLIC_URL`.
1. **Discover** — `GET {issuer}/.well-known/oauth-authorization-server` (RFC 8414). The same
   document is served with the issuer path appended and under `openid-configuration`.
2. **Register** — `POST {issuer}/oauth/register` (RFC 7591). Public clients get a `client_id`
   with no secret and use PKCE; confidential clients may request `client_secret_post`.
3. **Authorize** — browser visits `GET {issuer}/oauth/authorize?response_type=code&client_id=…
   &redirect_uri=…&code_challenge=…&code_challenge_method=S256&state=…`. The user approves on a
   consent screen, and the client receives `?code=…&state=…` at its redirect URI.
4. **Token** — `POST {issuer}/oauth/token` with `grant_type=authorization_code`, the `code`,
   the PKCE `code_verifier`, `redirect_uri` and `client_id`. The response is
   `{access_token: "rdr_…", token_type: "Bearer", expires_in, refresh_token, scope}`.
   Refresh with `grant_type=refresh_token`.

## Configuration

OAuth is **inert until an issuer is set**. Nothing changes on the gateway without it.

Gateway (authorization server) — requires account mode (`RADAR_ACCOUNTS_ENABLED=1`, encryption
key, Companies Radar upstream, Razorpay already configured for top-ups):

    RADAR_OAUTH_ISSUER=https://fliarbi.com/<gateway-mount>

> The issuer must be the **public origin that also hosts the Companies Radar dashboard**, because the
> consent page reads the signed-in session (`localStorage.radar_auth_token`) the same way the
> `/developer` console does. That is the fliarbi.com mount reached through the reverse proxy
> (with the matching `root_path`), **not** the `radar-api.fliarbi.com` subdomain — a different
> origin cannot read that session.

When the issuer is not on the dashboard's origin, keep it where it is and move only the consent
step, so tokens and registration stay on the API host:

    RADAR_PUBLIC_URL=https://<api host>                       # /mcp under it is the protected resource
    RADAR_OAUTH_AUTHORIZE_URL=https://fliarbi.com/<gateway-mount>/oauth/authorize
    RADAR_PUBLIC_DEVELOPER_URL=https://fliarbi.com/<gateway-mount>/developer
    RADAR_PUBLIC_PRIVACY_URL=https://fliarbi.com/privacy      # named in discovery documents and the landing page
    RADAR_PUBLIC_TERMS_URL=https://fliarbi.com/terms

The consent page sends signed-out visitors to the login page with a same-origin `?next=`, so
signing in or registering returns them to the approval step. Connector keys are shown the 25 core
tools (`CHAT_TOOLS` in `radar_api/server.py`); every tool remains callable.

Resource server (prism-mcp), so it advertises this gateway:

    PRISM_OAUTH_ISSUER=https://fliarbi.com/<gateway-mount>   # = RADAR_OAUTH_ISSUER
    PRISM_RESOURCE_URL=https://<prism-mcp public base>

## Reverse proxy / CDN

- Route `{issuer}/oauth/*` and `{issuer}/.well-known/oauth-authorization-server` to the gateway,
  preserving the path, and mount the gateway with the matching `root_path`.
- Those paths are public: no auth gate or bot rule in front of them.
- Do not let the CDN strip `Access-Control-*`, `WWW-Authenticate`, or `Cache-Control` headers;
  the app sets them.

## Revoking

A connector's key appears in the key console named `Connector <client_id>`. Revoking it ends
the grant immediately; the client must sign in again.

## Security

PKCE (S256) is required on every authorization. Authorization codes are single-use and
short-lived (5 min). `redirect_uri` is matched exactly against the DCR registration. The consent
step authenticates the human with the Companies Radar session header the dashboard holds — a header a
cross-origin page cannot read or forge, so no ambient cookie is trusted and the screen needs no
separate CSRF token (`frame-ancestors 'none'` blocks framing). DCR is open but rate-limited per
IP.
