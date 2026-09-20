# Job detail API: retrieve a listing by returned job ID

[All endpoints](README.md) · [Workflow guide](../guides/hiring-signals-jobs-api.md)

Retrieve one job listing after discovery. The accepted identifier should come from search_jobs. This separates a lightweight results page from a detail view and avoids inferring detail URLs from company names or job titles.

## Route, authentication and credits

**`POST /v1/jobs/detail`** · MCP tool **`get_job`** · key scope **`jobs`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `id` | required | string; min characters: `1`; max characters: `160`; pattern: `^[a-zA-Z0-9:_-]+$` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/jobs/detail" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"id":"unavailable-example"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_job -->
```json
{
  "name": "get_job",
  "arguments": {
    "request": {
      "id": "unavailable-example"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_job -->
```json
{
  "ok": false,
  "feature": "get_job",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:59:23.560869+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  },
  "error": {
    "kind": "no_data",
    "message": "No matching data was returned"
  }
}
```

This is the captured **complete response**, HTTP **404**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_job.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The live job search supplied no ID because it was partial. The detail capture therefore deliberately used the nonexistent ID unavailable-example and returned HTTP 404 no_data. This is a real negative-response example, not a successful listing with invented content.

## Read the response

| Field | Meaning and handling |
|---|---|
| `id` | A job identifier returned by search, using the allowed ID characters. |
| `data` | The source listing representation when available. |
| `error.kind=no_data` | No accessible listing was returned for that identifier. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Run a successful nonpartial search, retain its listing ID, then request detail. Keep any date and source link provided. If detail no longer exists, mark it unavailable without automatically removing unrelated job observations.

A 404 can reflect an unknown, removed or inaccessible listing; it does not establish that the employer has no vacancies. Do not turn the sample negative ID into a recommended production identifier.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/hiring-signals-jobs-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
