# Company potential data API: growth, investment and sales prospecting screens

[All endpoints](README.md) · [Workflow guide](../guides/potential-company-data-api.md)

Discover six explainable screens for scaling companies, profitable growth, seed-stage businesses, hiring demand, selected technologies and mobile-app scale. Every preset exposes its defining filters, sort, evidence columns and interpretation.

## Route, authentication and credits

**`POST /v1/companies/opportunities/presets`** · MCP tool **`opportunity_presets`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

This operation accepts an empty JSON object: `{}`.

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/opportunities/presets" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: opportunity_presets -->
```json
{
  "name": "opportunity_presets",
  "arguments": {
    "request": {}
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: opportunity_presets -->
```json
{
  "ok": true,
  "feature": "opportunity_presets",
  "data": {
    "presets": [
      {
        "id": "high_growth",
        "title": "Companies with recorded scaling signals",
        "filters": {
          "growth_stages": [
            "Scaling Super Fast",
            "Aggressively Scaling"
          ]
        },
        "sort_by": "momentum",
        "evidence_columns": [
          "employees",
          "total_funding",
          "latest_revenue"
        ],
        "interpretation": "Derived scaling labels; verify financial and hiring evidence separately."
      },
      {
        "id": "profitable_growth",
        "title": "Companies with recorded profits and revenue growth",
        "filters": {
          "profitability": [
            "profitable"
          ],
          "revenue_growth": [
            "growing"
          ]
        },
        "sort_by": "finance",
        "evidence_columns": [
          "latest_revenue",
          "growth_stage",
          "total_funding"
        ],
        "interpretation": "Recorded financial bands can be stale or source-plan restricted; use financial statements for exact periods."
      },
      {
        "id": "early_stage",
        "title": "Young companies with seed-stage records",
        "filters": {
          "ages": [
            "< 5y"
          ],
          "stages": [
            "Seed"
          ]
        },
        "sort_by": "funding",
        "evidence_columns": [
          "total_funding",
          "employees"
        ],
        "interpretation": "Historical age and funding classification; no claim of a current fundraising mandate."
      },
      {
        "id": "hiring_expansion",
        "title": "Companies with recorded hiring demand",
        "filters": {
          "hiring": {
            "is_hiring": true,
            "min_open_roles": 1,
            "recency_days": 90
          }
        },
        "sort_by": "employees",
        "evidence_columns": [
          "employees",
          "latest_revenue"
        ],
        "interpretation": "Hiring is an observed demand signal, not verified intent to buy a service."
      },
      {
        "id": "technology_modernization",
        "title": "Scaling companies using selected web technologies",
        "filters": {
          "technologies": [
            "PHP",
            "MySQL"
          ],
          "growth_stages": [
            "Aggressively Scaling"
          ]
        },
        "sort_by": "employees",
        "evidence_columns": [
          "web_presence",
          "employees"
        ],
        "interpretation": "A technology-and-growth screen. PHP or MySQL use does not prove poor technology or a modernization budget."
      },
      {
        "id": "mobile_scale",
        "title": "Companies with a substantial mobile-app footprint",
        "filters": {
          "mobile_downloads": [
            "1m+"
          ]
        },
        "sort_by": "employees",
        "evidence_columns": [
          "mobile_downloads",
          "mobile_growth",
          "employees"
        ],
        "interpretation": "Historical cumulative install bands; inspect individual apps and observation dates before estimating momentum."
      }
    ],
    "note": "Presets reproduce explicit Radar filters, not predicted investment returns, purchase intent or eligibility. Source gates and widened matches remain visible."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:27.597525+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:27.597658+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/opportunity_presets.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The capture exposes all six presets and their exact filter definitions for both investment research and B2B sales prospecting.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.presets[].filters` | Explicit Radar filters rather than hidden prediction weights. |
| `data.presets[].evidence_columns` | Observed company metrics requested for each matched page. |
| `data.presets[].interpretation` | What the signal can support and what it cannot establish. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Choose a preset, add geography or sector filters and call search_opportunities. Use company fields, financial statements, hiring, apps and news to validate the shortlist.

No screen estimates investment returns, purchase probability, budget or an active fundraising mandate. Technology use alone is not a deficiency or intent signal.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/potential-company-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
