# Create an API key: scopes, expiry and one-time reveal

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

Creates a random key owned by the verified account and returns it once. Set a recognizable application name, the smallest necessary data scopes and an explicit expiry. The server stores its hash rather than the plaintext key.

## Method and authentication

**`POST /account/keys`**

Use your existing Radar session in `Authorization: Bearer`. Every request verifies the live identity and current entitlements. Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `name` | required | string; min characters: `1`; max characters: `200` |
| `scopes` | optional; empty by default | array of string; min items: `1`; max items: `11` |
| `expires_days` | default `30` | integer; minimum: `1.0`; maximum: `90.0` |

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/account/keys" \
  -H "Authorization: Bearer $RADAR_SESSION_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"name":"Research notebook","scopes":["companies","news"],"expires_days":30}'
```

Set the private base URL without a trailing slash. Example IDs identify the
temporary documentation account; use your own returned identifiers when integrating.
Do not paste the redacted credential placeholders into a running application.

## Executed local output

**Provenance: real gateway code and a temporary SQLite account store, with a
synthetic verified Radar identity and synthetic Razorpay provider responses.**
No live user was created, payment collected or production account changed.
The synthetic Business plan and ten-paise credit price exercise the flow;
they do not announce an enabled checkout or an approved pay-per-use tariff.

<!-- response-example: account_create_key -->
```json
{
  "ok": true,
  "feature": "account",
  "data": {
    "id": "49a28e9b0f04e9d4b36c6251",
    "name": "Research notebook",
    "api_key": "REDACTED_COPY_ONCE_API_KEY",
    "expires_at": 1794716981,
    "message": "Save this key now. It will not be shown again."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-10-16T04:29:41.194208+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-10-16T04:29:40.723433+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/account_create_key.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

## What this response means

Copy api_key into a secret store immediately; it is redacted in the published capture. The public id is used for later revocation. New keys share the account's existing rate limits and credit budget.

The capture sequence connected a session, inspected plans, created and listed a
key, linked a placeholder News key, followed one domain, set a spending limit,
created a synthetic order, delivered its signed captured event, inspected usage,
then unfollowed the domain and revoked the key. Responses reflect that order.

Handle `401` by reconnecting an authorized session, `403` by checking plan/access,
and `429` with backoff and the supplied retry interval. Do not automate repeating
checkout requests after an ambiguous network failure: first inspect the provider
order and reconcile its captured status. Key creation reveals a credential once;
key listing is metadata-only. See the [account controls](../ACCOUNTS.md) for
creation caps, shared limits, spending reservations and payment reversal behavior.

Related: [API-key onboarding](../guides/api-keys-authentication.md),
[plans and pay-per-use](../guides/pricing-pay-per-use.md),
[full account schema](../account-openapi.json).
