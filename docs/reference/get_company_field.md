# Company field API: sectors, founders, technology, apps and LinkedIn data

[All endpoints](README.md) · [Workflow guide](../guides/company-data-api.md)

Request one named field from a company whose identity you have reviewed. The field selector is required and allowlisted; there is no all-fields option. The database projection selects only that field.

## Route, authentication and credits

**`POST /v1/companies/field`** · MCP tool **`get_company_field`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |
| `company_id` | default `null` | string or null; min characters: `1`; max characters: `100`; pattern: `^[A-Za-z0-9_-]+$` |
| `field` | required | string; one of `overview`, `classification`, `people`, `technology`, `web_presence`, `traffic`, `apps`, `products`, `geography`, `social`, `lifecycle`, `legal`, `assessments`, `hiring`, `innovation`, `activity`, `reputation`, `share_of_voice` |
| `item_limit` | default `50` | integer; minimum: `1`; maximum: `100` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/field" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"razorpay.com","field":"technology","item_limit":100}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_field -->
```json
{
  "name": "get_company_field",
  "arguments": {
    "request": {
      "domain": "razorpay.com",
      "field": "technology",
      "item_limit": 100
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_company_field -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "razorpay.com",
    "company_id": "2gowls1wmc",
    "field": "technology",
    "value": {
      "website_stack": [
        "amazon cloudfront",
        "amazon s3",
        "amazon web services",
        "angular",
        "animate.css",
        "antv g2",
        "apple icloud mail",
        "aws certificate manager",
        "bootstrap",
        "cart functionality",
        "cdnjs",
        "chakra ui",
        "chart.js",
        "cloudflare",
        "cloudflare bot management",
        "cloudflare browser insights",
        "core-js",
        "datadog",
        "emotion",
        "express",
        "facebook pixel",
        "font awesome",
        "framer sites",
        "google analytics",
        "google font api",
        "google sign-in",
        "google tag manager",
        "google workspace",
        "hotjar",
        "hsts",
        "http/3",
        "hubspot",
        "hubspot analytics",
        "hubspot chat",
        "jquery",
        "jquery cdn",
        "jsdelivr",
        "linkedin insight tag",
        "loadable-components",
        "lodash",
        "lottiefiles",
        "marked",
        "microsoft clarity",
        "next.js",
        "next.js app router",
        "nginx",
        "node.js",
        "open graph",
        "pdf.js",
        "preact",
        "priority hints",
        "pwa",
        "radix ui",
        "razorpay",
        "react",
        "react router",
        "recaptcha",
        "rss",
        "salesforce",
        "segment",
        "sentry",
        "shadcn/ui",
        "styled-components",
        "substack",
        "tailwind css",
        "typescript",
        "webpack",
        "yellow.ai",
        "zoho",
        "zone.js"
      ],
      "technographics": [],
      "observed_technologies": [
        "amazon cloudfront",
        "amazon s3",
        "amazon web services",
        "angular",
        "animate.css",
        "antv g2",
        "apple icloud mail",
        "bootstrap",
        "cart functionality",
        "cdnjs",
        "chakra ui",
        "chart.js",
        "cloudflare",
        "cloudflare bot management",
        "cloudflare browser insights",
        "core-js",
        "datadog",
        "emotion",
        "express",
        "facebook pixel",
        "font awesome",
        "framer sites",
        "google analytics",
        "google font api",
        "google sign-in",
        "google tag manager",
        "google workspace",
        "hotjar",
        "hsts",
        "http/3",
        "hubspot",
        "hubspot analytics",
        "hubspot chat",
        "jquery",
        "jquery cdn",
        "jsdelivr",
        "linkedin insight tag",
        "loadable-components",
        "lodash",
        "lottiefiles",
        "marked",
        "microsoft clarity",
        "next.js",
        "next.js app router",
        "nginx",
        "node.js",
        "open graph",
        "pdf.js",
        "preact",
        "priority hints",
        "pwa",
        "radix ui",
        "razorpay",
        "react",
        "react router",
        "recaptcha",
        "rss",
        "salesforce",
        "segment",
        "sentry",
        "shadcn/ui",
        "styled-components",
        "substack",
        "tailwind css",
        "typescript",
        "webpack",
        "yellow.ai",
        "zoho",
        "zone.js"
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
          "available": 70,
          "returned": 70,
          "truncated": false
        },
        "/value/technographics": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/observed_technologies": {
          "available": 69,
          "returned": 69,
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
    "retrieved_at": "2026-09-21T04:08:59.470819+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T04:08:59.471147+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_field.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The technology example preserves all seventy Razorpay stack entries with item_limit=100. Other company fields have separate real JSON captures.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.field / value` | Selected field and its source data only. |
| `data.status` | Stored observation status; missing is not zero. |
| `data.coverage.arrays` | Per-array available, returned and truncated counts. |
| `data.value.linkedin` | Social field only: latest observed company followers/headcount, bounded profile history and distinct stored posts. |
| `data.updated_at` | Source record update, distinct from gateway retrieval time. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Resolve the company and select one field. For field=social, read platform links alongside value.linkedin.profile, profile_history and recent_posts. These read underlying LinkedIn observations even when derived social enrichment is absent. Inspect observation dates, per-source coverage and array truncation.

A successful HTTP response does not independently establish current accuracy or complete coverage. Contact access checks and source plan limits remain authoritative.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
