# OpenAPI schema endpoint: REST and account contracts

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

Returns the machine-readable contract for the active gateway mode. Account mode includes session-authenticated management routes alongside key-authenticated data routes.

## Method and authentication

**`GET /v1/openapi.json`**

Use a data API key in `Authorization: Bearer`. Discovery does not reserve data-operation credits. Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

This request has no JSON body.

```bash
curl --fail-with-body -X GET "$RADAR_API_URL/v1/openapi.json" \
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

<!-- response-example: openapi -->
```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Radar API",
    "description": "Private B2B company data, financial statements, funding data, financial news and funding news. All data routes require an API key. Optional account routes use a verified Radar session.",
    "version": "0.1.0"
  },
  "paths": {
    "/healthz": {
      "get": {
        "summary": "Process liveness only; no data-service health claim",
        "operationId": "health_healthz_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    }
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T05:02:52.062535+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/openapi.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

## What this response means

Use the served schema from your deployment. The excerpt omits most schemas and paths; use the complete downloadable account-openapi.json for code generation. Account routes are absent when account mode is disabled.

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
