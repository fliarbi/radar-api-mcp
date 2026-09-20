# Get a Radar API key: account setup, authentication and key rotation

An API key connects your application to Radar company data, financial data and
news retrieval. The same key works with REST and the MCP server. In private
account mode, you create your own keys after signing in with a verified, active
Radar account; an operator does not need to send you a shared master key.

This workflow is implemented in the private package. Your operator must activate
account mode and provide its private URL. It is not yet a publicly deployed
developer service or a change to the existing Radar production dashboard.

## Create your first API key

1. Create or sign in to your Radar account and complete email verification.
2. Open the operator-supplied `/developer` console. When hosted on the same
   trusted origin as Radar, choose **Connect Radar session** to use the existing
   dashboard session. The local-development connection accepts a supplied session
   explicitly; signing in on the public Radar site does not transfer it to localhost.
3. Enter an application name, select its data scope and choose an expiry of up
   to 90 days. The default expiry is 30 days.
4. Choose **Create API key**, copy the key once and save it in your application's
   secret store. The console cannot reveal the key again later.

Keys begin with `rdr_`. The server stores their SHA-256 hashes. Linked Radar and
News credentials are encrypted separately. The console does not write keys or
new session tokens to browser storage.

## Authenticate a REST request

```bash
curl "$RADAR_API_URL/v1/companies/profile" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com"}'
```

`X-API-Key` is also accepted. If both headers are supplied, their values must
agree. Keep keys out of URLs and query strings. For MCP, use the same header on
the private `/mcp` endpoint; see [MCP setup](company-intelligence-mcp-server.md).

## Manage keys through the account API

Account routes require a Radar session in `X-Auth-Token`, rather than a data API key:

| Method and path | Purpose |
|---|---|
| `POST /account/keys` | Create a key with `name`, `scopes` and `expires_days` |
| `GET /account/keys` | List IDs, names, last four characters, expiry and revocation state |
| `DELETE /account/keys/{key_id}` | Revoke one of your keys |
| `POST /account/session` | Reconnect a current Radar session for existing keys |
| `PUT /account/news-key` | Link your separately issued News API key |

Supported scopes are `companies`, `investors`, `markets`, `locations`,
`industries`, `jobs`, `people`, `news`, or `*`. A company brief that includes news
requires both company and news access. Business supports up to ten active keys;
other plans support three. Creation is limited to ten keys per rolling 24 hours.

## Rotation, expired sessions and billing

Create a replacement, update your application, then revoke the old key. Creating
a new key does not reset account credits or request limits. A revoked key cannot
authenticate a subsequent request; requests already admitted may finish.

Radar validates the linked session on each authenticated call. If it expires or
is rejected after a password change, reconnect in the console. API-key expiry
and Radar-session expiry are separate. Dashboard logout behavior is controlled
by Radar; explicitly revoke API keys when you intend to stop API access.

A key does not grant unlimited data. Review [pricing and pay-per-use](pricing-pay-per-use.md)
and preserve the [data coverage limits](../USER_GUIDE.md) in your application.
