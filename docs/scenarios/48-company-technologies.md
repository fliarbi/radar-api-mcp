# Retrieve Stripe’s observed technologies with their available source structure.

[All 50 scenarios](README.md) · [Workflow guide](../guides/technology-traffic-data-api.md) · [Endpoint reference](../reference/get_company_field.md)

**POST `/v1/companies/field`** · MCP tool **`get_company_field`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** Selected field technology contains data.

## Exact executed request

<!-- scenario-request: 48-company-technologies -->
```json
{
  "domain": "stripe.com",
  "field": "technology",
  "item_limit": 100
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.709136+00:00; HTTP **200**;
**observed**, 0.006 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

Only the requested detail field is returned. Preserve field_status, source update date, nested business structures and array coverage. Missing observations do not become zero or proof that the company lacks a technology, market or traffic source.

The baseline was HTTP 200, **observed**:
Response contract and declared scenario checks passed; source truth not independently certified. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 48-company-technologies -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "stripe.com",
    "company_id": "1x532zlgk5",
    "field": "technology",
    "value": {
      "website_stack": [
        "algolia",
        "amazon cloudfront",
        "amazon s3",
        "amazon web services",
        "apple icloud mail",
        "bootstrap",
        "cart functionality",
        "cloudflare",
        "cloudflare bot management",
        "contentful",
        "core-js",
        "digicert",
        "docusign",
        "envoy",
        "google analytics",
        "google workspace",
        "hcaptcha",
        "hsts",
        "jquery",
        "jquery migrate",
        "jquery ui",
        "lodash",
        "next.js",
        "nginx",
        "node.js",
        "open graph",
        "priority hints",
        "prism",
        "pwa",
        "react",
        "rss",
        "sentry",
        "stripe",
        "three.js",
        "webpack"
      ],
      "technographics": [],
      "observed_technologies": [
        "algolia",
        "amazon cloudfront",
        "amazon s3",
        "amazon web services",
        "apple icloud mail",
        "bootstrap",
        "cart functionality",
        "cloudflare",
        "cloudflare bot management",
        "core-js",
        "docusign",
        "google analytics",
        "google workspace",
        "hcaptcha",
        "hsts",
        "jquery",
        "jquery migrate",
        "jquery ui",
        "lodash",
        "next.js",
        "nginx",
        "node.js",
        "open graph",
        "priority hints",
        "prism",
        "pwa",
        "react",
        "rss",
        "sentry",
        "stripe",
        "three.js",
        "webpack"
      ],
      "observed_at": "2026-05-01"
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "technology": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/website_stack": {
          "available": 35,
          "returned": 35,
          "truncated": false
        },
        "/value/technographics": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/observed_technologies": {
          "available": 32,
          "returned": 32,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.709016+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/48-company-technologies.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
