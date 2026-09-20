# Company search API: filter B2B companies

[All endpoints](README.md) · [Workflow guide](../guides/company-search-api.md)

Use company search when you can describe a business segment with explicit criteria: industry, geography, company size, funding stage or a financial band. The response is a bounded page of company cards that can become the input to profile, enrichment, financial and news requests. It is a discovery step, not a complete database export.

## Route, authentication and credits

**`POST /v1/companies/search`** · MCP tool **`search_companies`** · key scope **`companies`**.
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

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"industries":["Software"],"locations":["India"]},"limit":2}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_companies -->
```json
{
  "name": "search_companies",
  "arguments": {
    "request": {
      "filters": {
        "industries": [
          "Software"
        ],
        "locations": [
          "India"
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

<!-- response-example: search_companies -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
    "companies": [
      {
        "slug": "e2e-networks",
        "linkedin_slug": "e2enetworks",
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
        "hq": "delhi",
        "size": "51-200",
        "founded": "2009",
        "tagline": "Provider of cloud infrastructure for artificial intelligence and machine learning",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "company_id": "3gf4ksfp7x",
        "name": "E2E Networks",
        "domain": "e2enetworks.com"
      },
      {
        "slug": "sun-telematics",
        "linkedin_slug": "sun-telematics-private-ltd",
        "location": {
          "c": "india",
          "rg": "karnataka",
          "l": "bengaluru",
          "lc": "bengaluru, karnataka, india",
          "hq": "bengaluru",
          "cc": "in",
          "coord": [
            77.59369,
            12.97194
          ],
          "g": "12.97194,77.59369"
        },
        "hq": "bengaluru",
        "size": "51-200",
        "founded": "2013",
        "tagline": "Saas-enabled fleet management solutions",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "company_id": "2olp0s0nzf",
        "name": "Sun Telematics",
        "domain": "suntelematics.com"
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
    "pagination": "Increment page; account caps can apply. No total is inferred from a page."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:42.797613+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_companies.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The live Software/India query returned two cards, including E2E Networks, with total=null and plan=free. A visible result does not establish complete segment coverage. The example preserves the real source fields and counts, while long descriptions and additional company attributes are omitted from the displayed excerpt.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.companies` | The company cards returned on this page. Use domain for the next lookup; company_id may be a string or number. |
| `data.page / requested_limit / returned` | Page zero is the first page. Requested and returned counts can differ. |
| `data.total` | May be null. Never use the page length as an inferred market total. |
| `data.access` | Effective plan, result caps, remaining search allowance and restricted filters when supplied. |
| `data.partial_timeout` | A partial upstream search may have completed even when HTTP status is 200. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Discover a vocabulary label, search a narrow segment, review candidate names and descriptions, and save each accepted domain with your own account identifier. Increase page only after processing the current page. If a filter is restricted by your plan, show that restriction instead of silently claiming the entire segment was searched.

A company's headquarters and the market where it sells are different attributes. Also distinguish a revenue-band filter from an exact revenue figure for a known fiscal year.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-search-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
