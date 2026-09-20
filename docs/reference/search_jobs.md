# Jobs API: search company hiring by role, skills and location

[All endpoints](README.md) · [Workflow guide](../guides/hiring-signals-jobs-api.md)

Search observed job listings using company domain, role, geography, skills, remote status and freshness. The response can support a hiring-signals section in company research. It does not submit applications, upload resumes or guarantee that every listed role remains open.

## Route, authentication and credits

**`POST /v1/jobs/search`** · MCP tool **`search_jobs`** · key scope **`jobs`**.
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
| `q` | default `null` | string or null; min characters: `2`; max characters: `500` |
| `title` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `company` | default `null` | string or null |
| `city` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `country` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `skills` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `remote` | default `false` | boolean |
| `employment_type` | default `null` | string or null; one of `full_time`, `part_time`, `contract`, `temporary`, `internship` |
| `freshness_days` | default `null` | integer or null; minimum: `1`; maximum: `365` |
| `sort_by` | default `"recent"` | string; one of `recent`, `relevance` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/jobs/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q":"engineer","limit":2}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_jobs -->
```json
{
  "name": "search_jobs",
  "arguments": {
    "request": {
      "q": "engineer",
      "limit": 2
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: search_jobs -->
```json
{
  "ok": true,
  "feature": "search_jobs",
  "data": {
    "jobs": [],
    "total_estimate": 10000,
    "total_capped": true,
    "page": 0,
    "page_size": 2,
    "access": {
      "plan": "free",
      "results_per_query": 15,
      "searches_per_month": 50,
      "anonymous": true
    },
    "plan": "free",
    "partial_timeout": true
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:59:15.495397+00:00",
    "partial": true,
    "notes": [
      "The source timed out on part of this query; returned counts may be incomplete."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_jobs.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The engineer query returned jobs=[] together with total_estimate=10000, total_capped=true and partial_timeout=true. This is an incomplete response, not evidence of ten thousand accessible jobs or no matching jobs. No real job ID was available to feed the detail request in this run.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.jobs` | Returned listings; extract an actual ID for get_job. |
| `data.total_estimate / total_capped` | A capped estimate is not an exact vacancy count. |
| `data.partial_timeout / meta.partial` | Incomplete source work can be returned with HTTP 200. |
| `data.page / page_size / access` | Page and effective account result limits. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Start with a company or narrow role/geography combination, check whether the response is partial, and save stable job IDs before requesting detail. Preserve source dates. A posting is an observed vacancy signal, not evidence that a person was hired.

Never display the capped estimate as an exact market total or overwrite existing jobs with an empty partial page. Retain the failure/partial state and retry a narrower query with backoff.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/hiring-signals-jobs-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
