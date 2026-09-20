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
  -d '{"q":"software earnings","granularity":"weekly"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: news_trends -->
```json
{
  "name": "news_trends",
  "arguments": {
    "request": {
      "q": "software earnings",
      "granularity": "weekly"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: news_trends -->
```json
{
  "ok": false,
  "feature": "news_trends",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:59:24.799854+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  },
  "error": {
    "kind": "service_unavailable",
    "message": "This data service is not connected to the private preview"
  }
}
```

This is the captured **complete response**, HTTP **503**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/news_trends.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

This live gateway capture returned HTTP 503 service_unavailable because the News connection was not configured. The response below is the actual output. No headlines, sentiment counts, funding amounts or event records are fabricated to make the example look successful.

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

Google/Bing search results used to research these documents are not Radar News API responses. A search-service result cannot be relabeled as this endpoint's successful output. After connecting the News services and an authorized key, rerun the capture to obtain a verified success example.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/financial-news-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
