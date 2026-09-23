# Market pulse API: funding activity and trending business categories

[All endpoints](README.md) · [Workflow guide](../guides/startup-funding-data-api.md)

Retrieve Radar's existing market pulse: funding summaries, recent-funding candidates, investor references and trending categories. It can help an analyst decide which market or company to investigate next. The gateway returns source observations rather than calculating a fresh market census.

## Route, authentication and credits

**`POST /v1/markets/pulse`** · MCP tool **`market_pulse`** · key scope **`markets`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `days` | default `30` | integer; minimum: `1`; maximum: `365` |
| `limit` | default `5` | integer; minimum: `1`; maximum: `10` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/markets/pulse" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"days":30,"limit":2}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: market_pulse -->
```json
{
  "name": "market_pulse",
  "arguments": {
    "request": {
      "days": 30,
      "limit": 2
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: market_pulse -->
```json
{
  "ok": true,
  "feature": "market_pulse",
  "data": {
    "config": {
      "days": 30,
      "feed_limit": 2,
      "funding_limit": 2,
      "industry_limit": 2,
      "investor_limit": 2,
      "sector_limit": 2
    },
    "funding_pulse": {
      "hot_stage": "",
      "total_24h": 53,
      "total_7d": 53
    },
    "recent_fundings": [
      {
        "industries": [],
        "date": "2074-08-22",
        "domain": "one97.com",
        "headline": "The company raised as much as Rs 18,300 crore through its IPO.",
        "latest_deal_amount": -1,
        "latest_deal_type": "",
        "name": "one97.com",
        "stage": "Public",
        "total_funding": 0
      },
      {
        "industries": [],
        "date": "2072-08-22",
        "domain": "nsdl.co.in",
        "latest_deal_amount": -1,
        "latest_deal_type": "",
        "name": "nsdl.co.in",
        "stage": "Public",
        "total_funding": 0
      }
    ],
    "top_investors": [
      {
        "domain": "europa.eu",
        "name": "European Union",
        "short_description": "Provider of european union government services",
        "type": "Not An Institutional Investor"
      },
      {
        "domain": "ycombinator.com",
        "name": "Y Combinator",
        "short_description": "Startup accelerator and venture capital fund focused on early-stage companies",
        "type": "Accelerator and Incubator"
      }
    ],
    "trending_markets": [
      {
        "count": 173212,
        "market": "marketing services"
      },
      {
        "count": 167831,
        "market": "it services"
      }
    ],
    "trending_sectors": [],
    "winning_industries": []
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:55.527058+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:55.527254+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/market_pulse.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live output contained a recent_fundings row dated 2074-08-22 and latest_deal_amount=-1. Those are retained in the excerpt to expose the source issue. They must not be presented as a current funding event or a negative-dollar transaction. This capture demonstrates the response shape and a validation need, not validated recent-funding coverage.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.config` | The effective source request configuration. |
| `data.funding_pulse` | Source summary counters, whose coverage is not a complete capital-flow measure. |
| `data.recent_fundings` | Candidate funding records; check dates and sentinel values. |
| `data.trending_markets / top_investors` | Available category and entity references, not a comprehensive ranking universe. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Request a bounded day window and a small limit. Inspect the dates and amount fields of returned funding records before placing them on a timeline. Follow a company domain into its funding history and associated news, and review the original evidence before adding any market totals.

Reject or quarantine future-dated activity and documented unknown-value sentinels in your application view. Do not use the source's recent label alone to establish recency, or sum overlapping summaries as total invested capital.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/startup-funding-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
