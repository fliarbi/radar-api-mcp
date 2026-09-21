# Semantic company search API: natural-language business discovery

[All endpoints](README.md) · [Workflow guide](../guides/company-search-api.md)

Use semantic search when you know the business problem or product category but do not yet know Radar's classification labels. A natural-language query can be combined with supported company filters. Returned businesses are candidates for review, not a certified list of every company matching the sentence.

## Route, authentication and credits

**`POST /v1/companies/semantic-search`** · MCP tool **`semantic_company_search`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `page` | default `0` | integer; minimum: `0`; maximum: `200` |
| `limit` | default `20` | integer; minimum: `1`; maximum: `100` |
| `q` | required | string; min characters: `2`; max characters: `500` |
| `filters` | optional; empty by default | CompanyFilters |

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

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/semantic-search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q":"enterprise software companies in India","limit":2}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: semantic_company_search -->
```json
{
  "name": "semantic_company_search",
  "arguments": {
    "request": {
      "q": "enterprise software companies in India",
      "limit": 2
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: semantic_company_search -->
```json
{
  "ok": true,
  "feature": "semantic_company_search",
  "data": {
    "companies": [
      {
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "founded": "2018",
        "hq": "hyderabad",
        "has_phone": false,
        "domain": "karanam.in",
        "company_id": 11487170,
        "has_email": false,
        "linkedin_slug": "",
        "name": "Karanam",
        "slug": "karanam",
        "tagline": "",
        "size": "1-10",
        "location": {
          "c": "india",
          "cc": "IN",
          "coord": [
            78.491684,
            17.38714
          ],
          "l": "hyderabad",
          "lc": "hyderabad, telangana, india",
          "rg": "telangana"
        },
        "description": "ERP software for the management of enterprise",
        "classification": {
          "sectors": [
            "Enterprise Applications"
          ],
          "markets": [
            "Enterprise Resource Planning"
          ],
          "business_models": [
            "Multi-Industry",
            "Enterprise"
          ]
        },
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=karanam.in"
      }
    ],
    "page": 0,
    "requested_limit": 2,
    "returned": 1,
    "total": null,
    "access": {
      "plan": "free",
      "results_capped": false,
      "searches_remaining": 50
    },
    "partial_timeout": false,
    "matching": {
      "location_relaxed": false,
      "location_scope": "exact"
    },
    "pagination": "Increment page; account caps can apply. No total is inferred from a page."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T04:02:30.470154+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T04:02:30.470311+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/semantic_company_search.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The captured enterprise-software query returned one company, Karanam, although the request allowed two. The endpoint returned no public relevance score. That output is a useful discovery lead, but the preview has not measured precision or recall for this query.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.companies` | Candidate company cards; the source may return fewer than requested. |
| `data.total` | Unknown totals remain null. |
| `data.access` | Plan restrictions apply to semantic and structured searches alike. |
| `data.pagination` | Instructions for the bounded page model; no cursor is implied. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Describe a product or service in a short, specific query. Examine returned company descriptions and domains, then use structured company search if you need a repeatable segment. Save the original query with the results so another analyst understands why each candidate was retrieved.

Do not turn the ordering into a numerical relevance rating or promise that the first match is the best supplier. Product meaning, corporate identity and geography still need review.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-search-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
