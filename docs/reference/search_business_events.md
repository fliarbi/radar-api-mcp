# Business news events API: structured events with article references

[All endpoints](README.md) · [Workflow guide](../guides/company-monitoring-api.md)

Discover structured business events associated with a company or topic through the News service. This differs from Radar's company event timeline: it uses the connected business-news contract and its own date window, quotas and article identifiers.

## Route, authentication and credits

**`POST /v1/news/events`** · MCP tool **`search_business_events`** · key scope **`news`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `q` | default `null` | string or null; min characters: `2`; max characters: `120` |
| `company` | default `null` | string or null |
| `country` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `date_from` | default `null` | string or null |
| `date_to` | default `null` | string or null |
| `sentiment` | default `null` | string or null; one of `positive`, `neutral`, `negative` |
| `priority_min` | default `null` | integer or null; minimum: `1`; maximum: `9` |
| `limit` | default `100` | integer; minimum: `1`; maximum: `100` |
| `cursor` | default `null` | string or null; max characters: `2048`; pattern: `^[A-Za-z0-9_=+-]+$` |
| `sort` | default `"newest"` | string; one of `newest`, `oldest`, `priority` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

`RADAR_API_URL` is `https://radar-api.fliarbi.com` (the [installer](../../README.md#install-in-one-line) sets it);
load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/news/events" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"company":"microsoft.com","limit":5,"date_from":"2026-04-01","date_to":"2026-04-30"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_business_events -->
```json
{
  "name": "search_business_events",
  "arguments": {
    "request": {
      "company": "microsoft.com",
      "limit": 5,
      "date_from": "2026-04-01",
      "date_to": "2026-04-30"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: search_business_events -->
```json
{
  "ok": true,
  "feature": "search_business_events",
  "data": {
    "items": [
      {
        "id": "69f880adbbf1d31455966a69",
        "event_type": "earnings",
        "role": "primary",
        "domain": "microsoft.com",
        "published_at": "2026-04-30T22:16:00"
      },
      {
        "id": "69f8804a43843dd771ce7099",
        "event_type": "earnings",
        "role": "primary",
        "domain": "microsoft.com",
        "published_at": "2026-04-30T21:20:25"
      },
      {
        "id": "69f8842343843dd771d08309",
        "event_type": "new_product",
        "role": "primary",
        "domain": "microsoft.com",
        "published_at": "2026-04-30T20:11:29"
      },
      {
        "id": "69f8a657bbf1d314559a2139",
        "event_type": "earnings",
        "role": "primary",
        "domain": "microsoft.com",
        "published_at": "2026-04-30T16:36:27"
      },
      {
        "id": "69f881798937ef12fc07b478",
        "headline": "Microsoft (MSFT 3.90%) just reported a quarter that beat on basically every number that matters.",
        "event_type": "earnings",
        "role": "primary",
        "domain": "microsoft.com",
        "published_at": "2026-04-30T13:41:49"
      }
    ],
    "returned": 5,
    "total_estimate": 68,
    "next_cursor": "eyJ2IjoxLCJ0IjoiZXYiLCJzIjoibmV3ZXN0IiwiZCI6IjIwMjYtMDQtMzAgMTM6NDE6NDkiLCJpIjoiNjlmODgxNzk4OTM3ZWYxMmZjMDdiNDc4IiwiZG0iOiJtaWNyb3NvZnQuY29tIiwiZXQiOiJlYXJuaW5ncyIsInJvIjoicHJpbWFyeSJ9",
    "by_type": {
      "key_people": 17,
      "earnings": 16,
      "contracts": 13,
      "company_announcement": 6,
      "lawsuit": 5,
      "layoffs": 5,
      "capital_infusion": 2,
      "ma": 2,
      "new_product": 1,
      "asset_acquisition": 1
    },
    "limit": 5,
    "sort": "newest",
    "resolved": false
  },
  "window": {
    "since": "2026-04-01",
    "until": "2026-04-30",
    "days": 30,
    "data_through": "2026-05-05",
    "freshness": "this business dataset is available through 2026-05-05; company events, funding and company-linked news may have different latest available dates"
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:51:49.795041+00:00",
    "partial": true,
    "notes": [],
    "provider": "Fliar BI",
    "coverage": {
      "available": false
    }
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:51:49.795172+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_business_events.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

**Capture method:** Executed authenticated local Radar gateway and actual Prism News application code against live data; isolated test identity and quota dependencies, with the News Free plan's data limits retained. No deployed News URL, production News-key authentication or customer billing was verified.

The captured response was executed through the real gateway and News application against live data, with an isolated test identity and quota dependencies. It verifies data retrieval, not a deployed News URL, production key authentication or customer billing. The Microsoft query returned five records from 68 April events with a by_type breakdown and article IDs. The event dataset's data_through is 2026-05-05. Longer extracted source sentences are omitted only from documentation, with paths listed; the API result remains unchanged.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data when connected` | business event records and article references when supplied; event and publication dates must remain distinct |
| `window` | Effective source dates and data-through information, not an assurance of complete or current coverage. |
| `meta.coverage / plan / quota` | Relayed when the connected News service provides them. |
| `error.kind=service_unavailable` | The gateway has no configured connection for this operation. |
| `error.kind=access_required` | A linked News key is missing or the upstream account rejects access. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Supply q or company, use explicit dates for a historical investigation, and check the returned coverage before interpreting results. For cursor-based searches, send the returned cursor unchanged with the same filters. Overview, trend and sentiment operations use their own analysis models rather than headline pagination.

The example is a historical query, not a current news feed. Read each dataset's data_through and freshness values. Configure both News service URLs and link an authorized News key for normal use; local integration identities never enter the deployed gateway. Search-engine results are not API responses.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-monitoring-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
