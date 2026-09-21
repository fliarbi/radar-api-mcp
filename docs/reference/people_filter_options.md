# People filter options API: schools, skills and sectors

[All endpoints](README.md) · [Workflow guide](../guides/b2b-data-api.md)

Find canonical professional search values using Radar’s people suggestion handler.

## Route, authentication and credits

**`POST /v1/people/filter-options`** · MCP tool **`people_filter_options`** · key scope **`people`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `field` | required | string; one of `schools`, `skills`, `sectors` |
| `q` | required | string; min characters: `2`; max characters: `500` |
| `limit` | default `10` | integer; minimum: `1`; maximum: `10` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/people/filter-options" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"field":"skills","q":"machine learning","limit":5}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: people_filter_options -->
```json
{
  "name": "people_filter_options",
  "arguments": {
    "request": {
      "field": "skills",
      "q": "machine learning",
      "limit": 5
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: people_filter_options -->
```json
{
  "ok": true,
  "feature": "people_filter_options",
  "data": {
    "field": "skills",
    "query": "machine learning",
    "options": [
      "machine learning",
      "microsoft azure machine learning"
    ],
    "returned": 2,
    "complete": false
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T04:02:31.124847+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T04:02:31.124988+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/people_filter_options.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live machine-learning skill query returns source suggestions rather than guessed company-sector labels.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.field / options` | Chosen school, skill or sector vocabulary and matching suggestions. |
| `data.returned / complete` | Bounded suggestion count; not total records or complete vocabulary. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Inspect the request schema and returned coverage; use the related discovery response before selecting an identifier or field. Preserve access errors and unknown values in your application.

A successful HTTP response does not independently establish current accuracy or complete coverage. Contact access checks and source plan limits remain authoritative.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/b2b-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
