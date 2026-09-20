# Capability discovery: tools, routes and input schemas

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

Lists the shared data-operation registry. Use it to discover the exact tool name, REST route and accepted input model instead of building arbitrary upstream calls.

## Method and authentication

**`GET /v1/capabilities`**

Use a data API key in `Authorization: Bearer`. Discovery does not reserve data-operation credits. Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

This request has no JSON body.

```bash
curl --fail-with-body -X GET "$RADAR_API_URL/v1/capabilities" \
  -H "Authorization: Bearer $RADAR_API_KEY"
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

<!-- response-example: capabilities -->
```json
{
  "ok": true,
  "feature": "capabilities",
  "data": {
    "features": [
      {
        "name": "search_companies",
        "method": "POST",
        "path": "/v1/companies/search",
        "read_only": true,
        "connection_configured": true
      },
      {
        "name": "semantic_company_search",
        "method": "POST",
        "path": "/v1/companies/semantic-search",
        "read_only": true,
        "connection_configured": true
      }
    ]
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T05:02:52.524142+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI",
    "coverage": null,
    "plan": null,
    "quota": null,
    "billing": null
  },
  "error": null
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T05:02:52.062535+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/capabilities.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

## What this response means

connection_configured means configuration is present for the caller, not that the service is healthy or that every query is entitled. The response excerpt shows a subset of thirty tools.

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
