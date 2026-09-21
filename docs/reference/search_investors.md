# Investor search API: discover investors by business filters

[All endpoints](README.md) · [Workflow guide](../guides/investor-data-api.md)

Discover investor entities using supported headquarters and portfolio-related filters. This uses the same bounded company-search input model but selects investor entities internally. It is useful for the first stage of a venture-capital or investment research workflow.

## Route, authentication and credits

**`POST /v1/investors/search`** · MCP tool **`search_investors`** · key scope **`investors`**.
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
| `filters` | optional; empty by default | CompanyFilters |
| `sort_by` | default `"relevance"` | string; one of `relevance`, `valuation`, `funding`, `estimated_revenue`, `financing_rounds`, `latest_deal`, `employees`, `prominence`, `finance`, `scalability`, `momentum`, `innovation`, `maturity` |

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
curl --fail-with-body -X POST "$RADAR_API_URL/v1/investors/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"locations":["India"]},"limit":5}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_investors -->
```json
{
  "name": "search_investors",
  "arguments": {
    "request": {
      "filters": {
        "locations": [
          "India"
        ]
      },
      "limit": 5
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: search_investors -->
```json
{
  "ok": true,
  "feature": "search_investors",
  "data": {
    "companies": [
      {
        "flags": [],
        "founded": "2021",
        "hq": "kolkata",
        "has_phone": false,
        "domain": "linkedin.com",
        "company_id": "1d3ty0mvae",
        "has_email": false,
        "linkedin_slug": "anon-wellness-delivered",
        "name": "Anon",
        "slug": "anon",
        "tagline": "",
        "size": "",
        "location": {
          "c": "india",
          "rg": "west bengal",
          "l": "kolkata",
          "lc": "kolkata, west bengal, india",
          "hq": "kolkata",
          "cc": "",
          "coord": [
            88.36304,
            22.56263
          ],
          "g": "22.56263,88.36304"
        },
        "description": "",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=linkedin.com"
      },
      {
        "flags": [
          [
            "Medium Enterprise",
            "size"
          ]
        ],
        "founded": "2013",
        "hq": "bengaluru",
        "has_phone": false,
        "domain": "tracxnlabs.com",
        "company_id": "15f445yxls",
        "has_email": false,
        "linkedin_slug": "tracxnlabs",
        "name": "Tracxn Labs",
        "slug": "tracxn-labs",
        "tagline": "Seed capital and support for early-stage technology and tech-enabled companies",
        "size": "501-1000",
        "location": {
          "c": "india",
          "rg": "karnataka",
          "l": "bengaluru",
          "lc": "bengaluru, karnataka, india",
          "hq": "bengaluru",
          "cc": "",
          "coord": [
            77.59369,
            12.97194
          ],
          "g": "12.97194,77.59369"
        },
        "description": "Seed capital and support for early-stage technology and tech-enabled companies",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=tracxnlabs.com"
      },
      {
        "flags": [],
        "founded": "2015",
        "hq": "delhi",
        "has_phone": false,
        "domain": "advantedge.vc",
        "company_id": "3lueh5w5px",
        "has_email": false,
        "linkedin_slug": "advantedge-founders",
        "name": "AdvantEdge",
        "slug": "advantedge",
        "tagline": "Tech focused early stage incubator & VC firm investing primarily in India",
        "size": "",
        "location": {
          "c": "india",
          "rg": "delhi",
          "l": "delhi",
          "lc": "delhi, delhi, india",
          "hq": "delhi",
          "cc": "in",
          "coord": [
            77.23149,
            28.65195
          ],
          "g": "28.65195,77.23149"
        },
        "description": "Tech focused early stage incubator & VC firm investing primarily in India",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=advantedge.vc"
      },
      {
        "flags": [],
        "founded": "2016",
        "hq": "bengaluru",
        "has_phone": false,
        "domain": "rainmatter.com",
        "company_id": "1uk9jhb17j",
        "has_email": false,
        "linkedin_slug": "rainmatterin",
        "name": "rainmatters.org",
        "slug": "rainmatters-org",
        "tagline": "Platform providing online casino games accepting credit card payments in Mexico",
        "size": "",
        "location": {
          "c": "india",
          "rg": "karnataka",
          "l": "bengaluru",
          "lc": "bengaluru, karnataka, india",
          "hq": "bengaluru",
          "cc": "",
          "coord": [
            77.59369,
            12.97194
          ],
          "g": "12.97194,77.59369"
        },
        "description": "Platform providing online casino games accepting credit card payments in Mexico",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=rainmatter.com"
      },
      {
        "flags": [],
        "founded": "2014",
        "hq": "delhi",
        "has_phone": false,
        "domain": "investopad.com",
        "company_id": "23cxozg14u",
        "has_email": false,
        "linkedin_slug": "investopad",
        "name": "Investopad",
        "slug": "investopad",
        "tagline": "Venture capital fund and accelerator focused on startups",
        "size": "",
        "location": {
          "c": "india",
          "rg": "delhi",
          "l": "delhi",
          "lc": "delhi, delhi, india",
          "hq": "delhi",
          "cc": "in",
          "coord": [
            77.23149,
            28.65195
          ],
          "g": "28.65195,77.23149"
        },
        "description": "Venture capital fund and accelerator focused on startups",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=investopad.com"
      }
    ],
    "page": 0,
    "requested_limit": 5,
    "returned": 5,
    "total": null,
    "access": {
      "plan": "free",
      "results_capped": false,
      "searches_remaining": 50
    },
    "partial_timeout": false,
    "matching": {},
    "pagination": "Increment page; account caps can apply. No total is inferred from a page."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T04:02:31.099552+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T04:02:31.099780+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_investors.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The India investor query now returns HTTP 200 with five source cards, replacing the earlier timeout example. One source record is named Anon and uses linkedin.com as its domain, so successful retrieval does not establish a resolved investor identity. Review names and domains before using the result for a funding relationship; the published directory remains a separate navigation source.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.companies` | Investor company cards when the source query succeeds. |
| `data.access` | Effective plan, filter restrictions and result caps. |
| `data.total` | May be unknown; a page count is not a complete investor universe. |
| `error.kind` | A failed search is explicitly different from an empty successful page. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Begin with a narrow geography or portfolio category, inspect returned investor identity, then use the published investor directory or company funding history for supporting context. A discovered investor is not a verified current mandate or a promise of funding availability.

Do not retry a broad expensive search in a tight loop or convert a timeout into companies=[]. Narrow the query, use backoff and retain the failure status in your research workflow.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/investor-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
