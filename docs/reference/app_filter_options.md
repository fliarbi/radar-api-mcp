# App category discovery API: available Google Play genre labels

[All endpoints](README.md) · [Workflow guide](../guides/apps-data-api.md)

Find observed category labels before constructing an app search. Labels come from stored app records rather than a hard-coded list of all possible store categories.

## Route, authentication and credits

**`POST /v1/apps/filter-options`** · MCP tool **`app_filter_options`** · key scope **`apps`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `q` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `limit` | default `20` | integer; minimum: `1`; maximum: `100` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/apps/filter-options" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q":"Food","limit":10}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: app_filter_options -->
```json
{
  "name": "app_filter_options",
  "arguments": {
    "request": {
      "q": "Food",
      "limit": 10
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: app_filter_options -->
```json
{
  "ok": true,
  "feature": "app_filter_options",
  "data": {
    "field": "category",
    "options": [
      "Food & Drink"
    ],
    "complete": true
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:59.240324+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:59.240490+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/app_filter_options.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Food query returns the stored Food & Drink category.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.field` | category. |
| `data.options` | Sorted matching observed category labels. |
| `data.complete` | False when the bounded response could have more results; not a claim that the store corpus is complete. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Select a returned label and pass it as category to search_apps. q is a case-insensitive substring; an empty request lists a bounded set of observed labels.

Coverage is observed Google Play / Android data. Apple App Store coverage is not connected. Capture time is not store freshness; observation timestamps are UTC. Zero ratings and unknown ratings remain distinct.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/apps-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
