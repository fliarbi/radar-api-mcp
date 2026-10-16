# Company opportunity search API: prospects with measurable supporting evidence

[All endpoints](README.md) · [Workflow guide](../guides/potential-company-data-api.md)

Run one explicit company-potential preset plus additional company filters, then attach the preset’s measured display columns to the resulting domains. Preserve source access restrictions and partial evidence failures.

## Route, authentication and credits

**`POST /v1/companies/opportunities/search`** · MCP tool **`search_opportunities`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `page` | default `0` | integer; minimum: `0`; maximum: `200` |
| `limit` | default `10` | integer; minimum: `1`; maximum: `20` |
| `match_mode` | default `"strict"` | string; one of `strict`, `expanded` |
| `filters` | optional; empty by default | CompanyFilters |
| `sort_by` | default `"relevance"` | string; one of `relevance`, `valuation`, `funding`, `estimated_revenue`, `financing_rounds`, `latest_deal`, `employees`, `prominence`, `finance`, `scalability`, `momentum`, `innovation`, `maturity` |
| `preset` | required | string; one of `high_growth`, `profitable_growth`, `early_stage`, `hiring_expansion`, `technology_modernization`, `mobile_scale` |

### Fields inside `filters`

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `company_names` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `industries` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `sectors` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `markets` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `business_models` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `locations` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `sizes` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `stages` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `technologies` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `products` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `skills` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `event_types` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `financing_status` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `ownership_status` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `revenue_bands` | optional; empty by default | array of string; max items: `1`; one of `under1m`, `1m-10m`, `10m-100m`, `100m-1b`, `1b+` |
| `revenue_growth` | optional; empty by default | array of string; max items: `1`; one of `declining`, `flat`, `growing`, `high`, `hyper` |
| `profitability` | optional; empty by default | array of string; max items: `1`; one of `profitable`, `loss` |
| `entity_type` | default `"all"` | string; one of `all`, `investor`, `incubator` |
| `revenue_models` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `business_approaches` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `scalability` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `growth_stages` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `operating_status` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `organization_types` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `deal_sizes` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `ages` | optional; empty by default | array of string; max items: `1`; one of `Most Recent`, `< 5y`, `5-10y`, `10-25y`, `25+y` |
| `founded_year_from` | default `null` | integer or null; minimum: `1800`; maximum: `2100` |
| `founded_year_to` | default `null` | integer or null; minimum: `1800`; maximum: `2100` |
| `positions` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `verticals` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `industrial_applications` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `founders_background` | optional; empty by default | array of string; max items: `10`; one of `serial_entrepreneur`, `first_time_founder`, `founder_with_exit`, `top_ranked_founder`, `top_tier_university`, `elite_alumni`, `technical_founder`, `ex_notable_employer`, `c_level_exec`, `seasoned_15y` |
| `web_popularity` | optional; empty by default | array of string; max items: `3`; one of `high`, `medium`, `low` |
| `web_cwv` | optional; empty by default | array of string; max items: `3`; one of `pass`, `needs_improvement`, `poor` |
| `web_speed` | optional; empty by default | array of string; max items: `3`; one of `fast`, `average`, `slow` |
| `web_seo_maturity` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `web_sd_maturity` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `web_business_hints` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `web_score` | optional; empty by default | array of string; max items: `1`; one of `80+`, `60-80`, `40-60`, `<40` |
| `mobile_downloads` | optional; empty by default | array of string; max items: `1`; one of `1k+`, `100k+`, `1m+`, `10m+` |
| `mobile_growth` | optional; empty by default | array of string; max items: `1`; one of `declining`, `flat`, `growing`, `high`, `hyper` |
| `hiring` | default `null` | HiringFilter or null |
| `radius_km` | default `null` | integer or null; minimum: `21`; maximum: `250` |

### Fields inside `filters.hiring`

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `is_hiring` | default `true` | boolean |
| `min_open_roles` | default `1` | integer; minimum: `1`; maximum: `100000` |
| `roles` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `cities` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `recency_days` | default `30` | integer; minimum: `1`; maximum: `365` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

`RADAR_API_URL` is `https://radar-api.fliarbi.com` (the [installer](../../README.md#install-in-one-line) sets it);
load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/opportunities/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"preset":"mobile_scale","filters":{"locations":["India"],"markets":["Payments"]},"limit":2}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_opportunities -->
```json
{
  "name": "search_opportunities",
  "arguments": {
    "request": {
      "preset": "mobile_scale",
      "filters": {
        "locations": [
          "India"
        ],
        "markets": [
          "Payments"
        ]
      },
      "limit": 2
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: search_opportunities -->
```json
{
  "ok": true,
  "feature": "search_opportunities",
  "data": {
    "companies": [
      {
        "has_phone": false,
        "linkedin_slug": "paytm-mobile-solutions-pvt-ltd-",
        "founded": "2000",
        "flags": [],
        "company_id": "1lnxl8v10w",
        "description": "Digital payment platform offering financial services, recharges and more",
        "hq": "noida",
        "location": {
          "c": "india",
          "rg": "uttar pradesh",
          "l": "noida",
          "lc": "noida, uttar pradesh, india",
          "hq": "noida",
          "cc": "in",
          "coord": [
            77.33,
            28.58
          ],
          "g": "28.58,77.33"
        },
        "has_email": false,
        "tagline": "Digital payment platform offering financial services, recharges and more",
        "size": "10000+",
        "domain": "paytm.com",
        "slug": "paytm",
        "name": "Paytm",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=paytm.com",
        "match_tier": "strict"
      },
      {
        "has_phone": false,
        "linkedin_slug": "paisabazaar",
        "founded": "2014",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "company_id": "2inawol0hl",
        "description": "Online financial marketplace that offers a range of personal loan and credit card options to consumers",
        "hq": "gurugram",
        "location": {
          "c": "india",
          "rg": "haryana",
          "l": "gurugram",
          "lc": "gurugram, haryana, india",
          "hq": "gurugram",
          "cc": "in",
          "coord": [
            77.02635,
            28.4601
          ],
          "g": "28.4601,77.02635"
        },
        "has_email": false,
        "tagline": "Online financial marketplace that offers a range of personal loan and credit card options to consumers",
        "size": "5001-10000",
        "domain": "paisabazaar.com",
        "slug": "paisabazaar",
        "name": "Paisabazaar",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=paisabazaar.com",
        "match_tier": "strict"
      }
    ],
    "page": 0,
    "requested_limit": 2,
    "returned": 2,
    "total": null,
    "access": {
      "plan": "free",
      "results_capped": false,
      "searches_remaining": 50
    },
    "partial_timeout": false,
    "matching": {
      "mode": "strict",
      "tiers": [
        {
          "tier": "strict",
          "count": 71,
          "added": 2
        }
      ],
      "source_rows": 2,
      "excluded_candidates": 0,
      "strict_count_reported": 71,
      "candidate_pool_count_reported": 71,
      "count_capped": false,
      "filters_restricted": false,
      "note": "Strict means the source labelled the row strict and did not strip filters. Counts may describe an expanded candidate pool, not all matching companies. Missing tier metadata is unverified."
    },
    "next_page": 1,
    "pagination": "Increment source page even when strict filtering returns no rows; next_page is a continuation hint, not a guarantee of more matches. Account caps apply.",
    "preset": "mobile_scale",
    "effective_filters": {
      "markets": [
        "Payments"
      ],
      "locations": [
        "India"
      ],
      "mobile_downloads": [
        "1m+"
      ]
    },
    "sort_by": "employees",
    "evidence": [
      {
        "domain": "paytm.com",
        "columns": {
          "mobile_downloads": {
            "label": "App Downloads",
            "value": "825.0M"
          },
          "mobile_growth": {
            "label": "App Growth %",
            "value": "15"
          },
          "employees": null
        },
        "status": "available"
      },
      {
        "domain": "paisabazaar.com",
        "columns": {
          "mobile_downloads": {
            "label": "App Downloads",
            "value": "30.0M"
          },
          "mobile_growth": {
            "label": "App Growth %",
            "value": "24"
          },
          "employees": null
        },
        "status": "available"
      }
    ],
    "interpretation": "Historical cumulative install bands; inspect individual apps and observation dates before estimating momentum.",
    "coverage": {
      "partial": false,
      "evidence_available": true
    },
    "note": "These are source-filtered candidates, not verified opportunities. Inspect access/restricted_filters and matching metadata; display columns may suppress zero or negative values. Retrieve exact financials and detail fields separately."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:27.787095+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:27.787281+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_opportunities.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The India/Payments/mobile_scale capture returns Paytm and Paisabazaar. Recorded aggregate app-download values are 825.0M and 30.0M, with app growth display values 15 and 24. Employee values are null rather than invented.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.effective_filters / sort_by` | Filters submitted to Radar; source access restrictions or matching relaxation still govern what was applied. |
| `data.companies` | Bounded candidate cards, up to 20 per request. |
| `data.evidence` | Per-domain column values with labels and availability; not synthetic scores. |
| `data.access / matching` | Plan gates, restricted filters and source-relaxed matching when returned. |
| `data.coverage.partial` | True when search timed out partially or the evidence fetch failed. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Treat results as a shortlist. Request financials for exact periods, company field details for technology/hiring, individual apps for dated growth and news for a relevant event. Contacts remain a separate explicitly scoped request.

Additional filters cannot replace preset-defining criteria. Display columns can suppress zero or negative values; verify numeric claims with detailed source fields. One successful call costs one credit, including its bounded evidence lookup.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/potential-company-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
