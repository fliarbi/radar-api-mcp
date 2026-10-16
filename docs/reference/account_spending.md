# Set a monthly prepaid credit spending limit

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

Sets the maximum prepaid credits the account may spend in a UTC calendar month. The default zero disables prepaid consumption even when a wallet has credits. Included Business credits are used before prepaid funds.

## Method and authentication

**`PUT /account/spending`**

Use your existing Radar session in `Authorization: Bearer`. Every request verifies the live identity and current entitlements. Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `monthly_credit_limit` | default `0` | integer; minimum: `0.0`; maximum: `1000000.0` |

```bash
curl --fail-with-body -X PUT "$RADAR_API_URL/account/spending" \
  -H "Authorization: Bearer $RADAR_SESSION_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"monthly_credit_limit":100}'
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

<!-- response-example: account_spending -->
```json
{
  "ok": true,
  "feature": "account",
  "data": {
    "monthly_prepaid_limit": 100
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-10-16T04:29:41.674801+00:00",
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
The [downloadable JSON example](../examples/account_spending.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

## What this response means

monthly_prepaid_limit is credits, not rupees. Changing the limit does not charge money, buy credits or reset already-used monthly credit totals. In-flight reservations are already included in usage.

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
