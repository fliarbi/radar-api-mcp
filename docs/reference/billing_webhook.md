# Payment webhook: verify captured payments and credit once

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

Receives provider payment events with an HMAC signature over the original raw request body. A matching captured payment credits its stored order once; duplicate delivery cannot create an additional grant.

## Method and authentication

**`POST /billing/webhook`**

Provider-only callback. Verify `X-Razorpay-Signature` against the original raw body with the configured webhook secret. This route does not accept a user API key as payment proof. Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

The body is a Razorpay event envelope. Its signature must match the exact bytes; reformatting signed JSON invalidates it. The stored order determines the expected account, credits, amount and currency.

```bash
curl --fail-with-body "$RADAR_API_URL/billing/webhook" \
  -H "X-Razorpay-Signature: $RAZORPAY_SIGNATURE" \
  -H 'Content-Type: application/json' \
  --data-binary @captured-event.json
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

<!-- response-example: billing_webhook -->
```json
{
  "ok": true,
  "feature": "account",
  "data": {
    "received": true
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-10-16T04:29:41.791592+00:00",
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
The [downloadable JSON example](../examples/billing_webhook.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

## What this response means

The example was generated using a synthetic provider event and the real local signature verifier. The secret and signature are redacted. Browser checkout success is not accepted as proof of payment. Refund/dispute events freeze the affected account for reconciliation.

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
