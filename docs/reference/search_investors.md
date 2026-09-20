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
curl --fail-with-body -X POST "$RADAR_API_URL/v1/investors/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"locations":["India"]},"limit":2}'
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
      "limit": 2
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
  "ok": false,
  "feature": "search_investors",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:59:07.114970+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  },
  "error": {
    "kind": "upstream_timeout",
    "message": "The data service timed out; narrow the query or retry"
  }
}
```

This is the captured **complete response**, HTTP **504**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_investors.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The bounded India investor query exceeded the capture's twenty-second upstream timeout and returned HTTP 504 upstream_timeout. The response shown below is the actual failure. No investor list was fabricated as a substitute. investor_directory and get_investor_page did return live successful examples in the same run.

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
