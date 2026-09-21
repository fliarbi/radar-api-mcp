# Read Radar plans and API credit policy

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

Returns the catalog snapshot, configured per-credit rate, prepaid policy and checkout availability. Use this to explain pricing before asking a user to create a paid order.

## Method and authentication

**`GET /account/plans`**

Use your existing Radar session in `Authorization: Bearer`. Every request verifies the live identity and current entitlements. Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

This request has no JSON body.

```bash
curl --fail-with-body -X GET "$RADAR_API_URL/account/plans" \
  -H "Authorization: Bearer $RADAR_SESSION_TOKEN"
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

<!-- response-example: account_plans -->
```json
{
  "ok": true,
  "feature": "account",
  "data": {
    "plans": {
      "free": {
        "monthly_inr": 0,
        "monthly_usd": 0,
        "searches": 50,
        "following": 0,
        "api_access": false
      },
      "pro": {
        "monthly_inr": 1600,
        "monthly_usd": 19,
        "searches": 1000,
        "following": 100,
        "api_access": false
      },
      "business": {
        "monthly_inr": 5000,
        "monthly_usd": 60,
        "searches": 5000,
        "following": 1000,
        "api_access": true
      },
      "marketai_bundled": {
        "monthly_inr": 0,
        "monthly_usd": 0,
        "searches": 100,
        "following": 0,
        "api_access": false
      }
    },
    "catalog_verified_on": "2026-09-20",
    "currency": "INR",
    "credit_price_paise": 10,
    "checkout_enabled": true,
    "payg_all_verified_plans": true,
    "metering": "One credit per successful data operation; briefs reserve 6 or 7, comparisons reserve 3 per company. Failed sections refunded.",
    "note": "Private API allocation mirrors Business search allowance; dashboard search usage is separate. Upstream data access limits still apply. Market.ai bundled is a cross-grant, not a standalone free subscription."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T04:10:33.720499+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T04:10:33.455592+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/account_plans.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

## What this response means

The sample uses a synthetic ten-paise test rate so the checkout path can be exercised. The real default rate remains unset and checkout disabled. Catalog subscription prices and API credit budgets have separate meanings.

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
