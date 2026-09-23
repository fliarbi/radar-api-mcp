# Link a News API key to the Radar account

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

Stores an encrypted connection credential for the separately operated News service. It does not create a News subscription, activate an upstream server or change the News account's quota.

## Method and authentication

**`PUT /account/news-key`**

Use your existing Radar session in `Authorization: Bearer`. Every request verifies the live identity and current entitlements. Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `api_key` | required | string; min characters: `1`; max characters: `512` |

```bash
curl --fail-with-body -X PUT "$RADAR_API_URL/account/news-key" \
  -H "Authorization: Bearer $RADAR_SESSION_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"api_key":"REDACTED_NEWS_KEY"}'
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

<!-- response-example: account_link_news -->
```json
{
  "ok": true,
  "feature": "account",
  "data": {
    "linked": true
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:58:26.610592+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:58:26.016123+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/account_link_news.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

## What this response means

linked=true is a storage acknowledgment, not a live validation of the credential. A later news request can still fail because its service is unavailable or its key is not entitled. The demonstration key is an explicit placeholder.

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
