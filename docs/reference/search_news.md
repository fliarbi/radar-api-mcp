# News search API: discover financial and business headlines

[All endpoints](README.md) · [Workflow guide](../guides/financial-news-api.md)

Search a topic or company for relevant news articles. Use this to discover source evidence, then retrieve selected articles rather than treating a headline alone as a complete report.

## Route, authentication and credits

**`POST /v1/news/search`** · MCP tool **`search_news`** · key scope **`news`**.
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
curl --fail-with-body -X POST "$RADAR_API_URL/v1/news/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q":"software earnings","limit":5,"date_from":"2026-04-01","date_to":"2026-04-30"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_news -->
```json
{
  "name": "search_news",
  "arguments": {
    "request": {
      "q": "software earnings",
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

**Current availability:** the 2026-09-23 probe returned HTTP 503 (`coverage_unavailable`). The successful response below is historical. See the [current output audit](../OUTPUT_DEPTH_AUDIT.md).

<!-- response-example: search_news -->
```json
{
  "ok": true,
  "feature": "search_news",
  "data": {
    "items": [
      {
        "id": "69e8d5e79baafc7356d34094",
        "headline": "A Look Back at Vertical Software Stocks’ Q4 Earnings: Toast (NYSE:TOST) Vs The Rest Of The Pack",
        "url": "https://www.theglobeandmail.com/investing/markets/stocks/TOST/pressreleases/1288588/a-look-back-at-vertical-software-stocks-q4-earnings-toast-nysetost-vs-the-rest-of-the-pack/",
        "publisher": "theglobeandmail.com",
        "published_at": "2026-04-13T22:37:00",
        "sentiment": {
          "label": "slight_pos",
          "score": 0.41,
          "group": "positive"
        },
        "priority": 7,
        "classes": [
          {
            "code": 0,
            "path": "/News/Business News/Company News",
            "score": 0.63
          }
        ],
        "country": "united states",
        "organizations": [
          "tost",
          "q4"
        ],
        "people": []
      }
    ],
    "returned": 1,
    "total_estimate": 1,
    "next_cursor": null,
    "unresolved": 0,
    "duplicates_dropped": 0,
    "limit": 5,
    "sort": "newest"
  },
  "window": {
    "since": "2026-04-01",
    "until": "2026-04-30",
    "days": 30,
    "data_through": "2026-08-24",
    "freshness": "volume thins after 2026-05; the last months are partial"
  },
  "meta": {
    "retrieved_at": "2026-09-20T10:58:50.084656+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI",
    "coverage": {
      "available": true
    }
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T10:58:50.084823+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_news.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

**Capture method:** Executed authenticated local Radar gateway and actual Prism News application code against live data; isolated test identity and quota dependencies, with the News Free plan's data limits retained. No deployed News URL, production News-key authentication or customer billing was verified.

The captured response was executed through the real gateway and News application against live data, with an isolated test identity and quota dependencies. It verifies data retrieval, not a deployed News URL, production key authentication or customer billing. The exact query software earnings matched one article in April 2026. Its headline, publisher, source URL, publication date, sentiment, priority, classifications, organizations and people are retained. The requested limit is a ceiling, not an instruction to manufacture five items.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data when connected` | data.items and next_cursor when supplied; window and coverage describe the accessible results |
| `window` | Effective source dates and data-through information, not an assurance of complete or current coverage. |
| `meta.coverage / plan / quota` | Relayed when the connected News service provides them. |
| `error.kind=service_unavailable` | The gateway has no configured connection for this operation. |
| `error.kind=access_required` | A linked News key is missing or the upstream account rejects access. |
| `data.items[].id / headline / url / publisher / published_at` | Article identity, short source title, attribution and reporting date; separate from retrieval time. |
| `data.items[].sentiment / priority / classes` | Derived labels and scores; classification paths and codes retain the source's taxonomy. |
| `data.items[].organizations / people / country` | Entities and location labels observed in the article; not proof of corporate ownership or residence. |
| `data.returned / total_estimate / limit` | Delivered page length, matching source count and requested page ceiling are distinct. |
| `data.next_cursor / unresolved / duplicates_dropped` | Continue with the opaque cursor and unchanged filters; missing article records and deduplicated URLs can shorten a page. |

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

Continue with the [workflow guide](../guides/financial-news-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
