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


## Email and phone permissions

The default wildcard data key does not reveal contacts. Select contact retrieval
when issuing a key, or add `contacts` to its explicit scope list. Email/phone
lookups use separate JSON POST requests and require paid linked Radar access.
See [contact requests and response shapes](../CONTACTS.md).

<!-- captured-workflow -->
## Walk from a signed-in account to a working integration key

Open the private `/developer` console on the operator-supplied trusted origin and
connect an existing verified Radar session. Read the effective plan and available
API policy, choose a descriptive key name and select only the data scopes your
application needs. Set an expiry within the supported one-to-ninety-day range.
The create-key response reveals the key once; store it directly in your application's
secret manager rather than in a browser bundle or a committed example file.

The captured response below was executed against a temporary account with synthetic
Radar identity verification. The credential is explicitly redacted, while the
returned public key ID and expiry retain their actual local values. Listing keys
later returns metadata and last-four characters, not the credential. The current
list response encodes scopes as a JSON string and uses Unix seconds for timestamps;
the dedicated endpoint reference preserves that actual wire format.

For rotation, create a replacement key, update the integration, verify a permitted
request, then revoke the previous key by ID. Revocation affects subsequent
authentication; an already admitted request may finish. Keys share account-wide
rate limits, concurrent-operation limits and credit usage. Reconnecting an expired
Radar session restores the linked session for that account without granting a new
monthly budget. A linked News key is a separate encrypted connection credential.

## Worked example: executed local account response with synthetic providers

The request captured for this example was **`POST /account/keys`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: account_create_key -->
```json
{
  "name": "Research notebook",
  "scopes": [
    "companies",
    "news"
  ],
  "expires_days": 30
}
```

<!-- response-example: account_create_key -->
```json
{
  "ok": true,
  "feature": "account",
  "data": {
    "id": "c2c62dac44ec6b9e53f49ff3",
    "name": "Research notebook",
    "api_key": "REDACTED_COPY_ONCE_API_KEY",
    "expires_at": 1792726844,
    "message": "Save this key now. It will not be shown again."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:40:44.541767+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T03:40:44.172223+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/account_create_key.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

Copy api_key into a secret store immediately; it is redacted in the published capture. The public id is used for later revocation. New keys share the account's existing rate limits and credit budget.

See the [complete account_create_key endpoint reference](../reference/account_create_key.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
