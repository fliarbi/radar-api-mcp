# Create a prepaid API credit checkout order

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

Creates a Razorpay order in USD or INR (default INR) for a server-calculated amount. The minimum is US$5 worth of credits at the USD rate, applied as a credit count in either currency. The user must complete provider Checkout, and the gateway must receive a verified captured-payment event, before the wallet receives credits.

## Method and authentication

**`POST /account/topups`**

Use your existing Radar session in `Authorization: Bearer`. Every request verifies the live identity and current entitlements. Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `credits` | default `1000` | integer; minimum: `1.0`; maximum: `100000.0` |
| `currency` | default `"INR"` | string; one of `USD`, `INR` |

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/account/topups" \
  -H "Authorization: Bearer $RADAR_SESSION_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"credits":500}'
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

<!-- response-example: account_topup -->
```json
{
  "ok": true,
  "feature": "account",
  "data": {
    "order_id": "order_documentation",
    "key_id": "rzp_test_documentation",
    "amount": 5000,
    "currency": "INR",
    "credits": 500,
    "status": "awaiting_captured_payment"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-10-16T04:29:41.756751+00:00",
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
The [downloadable JSON example](../examples/account_topup.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

## What this response means

The synthetic example requests 500 credits at ten paise each, producing amount=5000 paise (₹50); its USD rate of one cent per credit makes 500 credits the minimum. This is an execution fixture, not the public tariff. The response is awaiting_captured_payment and does not itself grant balance.

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
