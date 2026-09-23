# News trends API: daily, weekly and monthly volume

[All endpoints](README.md) · [Workflow guide](../guides/financial-news-api.md)

Measure observed news volume over time for a topic or company. This supports a trend chart whose denominator is the connected News service's accessible records, rather than every publication on the internet.

## Route, authentication and credits

**`POST /v1/news/trends`** · MCP tool **`news_trends`** · key scope **`news`**.
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
| `granularity` | default `"weekly"` | string; one of `daily`, `weekly`, `monthly` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/news/trends" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q":"software earnings","granularity":"weekly","date_from":"2026-04-01","date_to":"2026-04-30"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: news_trends -->
```json
{
  "name": "news_trends",
  "arguments": {
    "request": {
      "q": "software earnings",
      "granularity": "weekly",
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

<!-- response-example: news_trends -->
```json
{
  "ok": true,
  "feature": "news_trends",
  "data": {
    "granularity": "weekly",
    "points": [
      {
        "period": "2026-03-30",
        "articles": 0,
        "critical": 0,
        "critical_pct": null,
        "negative": 0,
        "positive": 0,
        "partial_period": true
      },
      {
        "period": "2026-04-06",
        "articles": 0,
        "critical": 0,
        "critical_pct": null,
        "negative": 0,
        "positive": 0,
        "partial_period": false
      },
      {
        "period": "2026-04-13",
        "articles": 1,
        "critical": 1,
        "critical_pct": 100.0,
        "negative": 0,
        "positive": 1,
        "partial_period": false
      },
      {
        "period": "2026-04-20",
        "articles": 0,
        "critical": 0,
        "critical_pct": null,
        "negative": 0,
        "positive": 0,
        "partial_period": false
      },
      {
        "period": "2026-04-27",
        "articles": 0,
        "critical": 0,
        "critical_pct": null,
        "negative": 0,
        "positive": 0,
        "partial_period": true
      }
    ],
    "total": 1,
    "critical_total": 1,
    "complete_periods": 3,
    "partial_periods": 2,
    "peak": "2026-04-13"
  },
  "window": {
    "since": "2026-04-01",
    "until": "2026-04-30",
    "days": 30,
    "data_through": "2026-08-24",
    "freshness": "volume thins after 2026-05; the last months are partial",
    "granularity": "weekly"
  },
  "meta": {
    "retrieved_at": "2026-09-20T10:58:50.564111+00:00",
    "partial": false,
    "notes": [
      "zero-count periods are included; partial_period marks buckets the window only partly covers"
    ],
    "provider": "Fliar BI",
    "coverage": {
      "available": true
    }
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-20T10:58:50.564298+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/news_trends.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

**Capture method:** Executed authenticated local Radar gateway and actual Prism News application code against live data; isolated test identity and quota dependencies, with the News Free plan's data limits retained. No deployed News URL, production News-key authentication or customer billing was verified.

The captured response was executed through the real gateway and News application against live data, with an isolated test identity and quota dependencies. It verifies data retrieval, not a deployed News URL, production key authentication or customer billing. The April software earnings series has five weekly buckets, one matched article, three complete periods and two partial boundary periods. The returned peak bucket is 2026-04-13; boundary buckets are not silently treated as complete weeks.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data when connected` | time buckets and coverage when supplied; granularity selects daily, weekly or monthly grouping |
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

Continue with the [workflow guide](../guides/financial-news-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
