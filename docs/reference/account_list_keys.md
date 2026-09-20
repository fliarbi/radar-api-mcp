# List API keys: names, expiry and revocation state

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

Lists the verified account's key metadata so users can manage integrations. It includes identifiers and last-four characters but never re-reveals the key or exposes a stored hash.

## Method and authentication

**`GET /account/keys`**

Use your existing Radar session in `Authorization: Bearer`. Every request verifies the live identity and current entitlements. Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

This request has no JSON body.

```bash
curl --fail-with-body -X GET "$RADAR_API_URL/account/keys" \
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

<!-- response-example: account_list_keys -->
```json
{
  "ok": true,
  "feature": "account",
  "data": [
    {
      "id": "8587d6feff542772062be456",
      "name": "Research notebook",
      "last4": "134f",
      "scopes": "[\"companies\", \"news\"]",
      "created": 1789886212,
      "expires": 1792478212,
      "revoked": 0
    }
  ],
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T06:36:52.974885+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-20T06:36:52.497809+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/account_list_keys.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

## What this response means

created and expires are Unix seconds; revoked is the persisted integer flag. scopes is currently a JSON-encoded string in this response, so parse it explicitly if your interface needs an array. That wire shape is preserved in the real local capture.

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
