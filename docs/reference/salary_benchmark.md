# Salary benchmark API: role and geography statistics

[All endpoints](README.md) · [Workflow guide](../guides/hiring-signals-jobs-api.md)

Retrieve source salary statistics for a role, geography and optional currency. Use it to add sample-based compensation context to a research interface, while keeping the observation count and sparse-data indicator visible.

## Route, authentication and credits

**`POST /v1/jobs/salary-benchmark`** · MCP tool **`salary_benchmark`** · key scope **`jobs`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `title` | required | string; min characters: `1`; max characters: `200` |
| `city` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `country` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `currency` | default `null` | string or null; pattern: `^[A-Z]{3}$` |
| `skills` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/jobs/salary-benchmark" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"title":"software engineer","country":"US","currency":"USD"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: salary_benchmark -->
```json
{
  "name": "salary_benchmark",
  "arguments": {
    "request": {
      "title": "software engineer",
      "country": "US",
      "currency": "USD"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: salary_benchmark -->
```json
{
  "ok": true,
  "feature": "salary_benchmark",
  "data": {
    "count": 206,
    "currency": "USD",
    "filter_echo": {
      "city": null,
      "country": "US",
      "currency": "USD",
      "skills": null,
      "title": "software engineer"
    },
    "max": 226000,
    "median": 124000,
    "min": 20800,
    "p25": 99025,
    "p75": 150000,
    "sparse": false
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T02:35:05.455593+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T02:35:05.455723+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/salary_benchmark.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The US/software engineer/USD query returns 206 observations, sparse=false, p25=99025, median=124000 and p75=150000. These are source salary-midpoint statistics within one currency. A salary period is not supplied here, so the documentation does not invent annual or hourly units. This explicitly different query does not replace the earlier sparse India sample with a US salary.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.count` | The number of observed records in the source sample. |
| `data.currency` | The requested or returned currency context. |
| `data.sparse` | The sample is too sparse for a strong benchmark interpretation. |
| `data.filter_echo` | The source's effective filters, which may normalize country names to codes. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Choose a specific role and location, request the intended currency, and inspect sample count before displaying any summary. Compare like geography and currency. Do not convert a benchmark into a promise of an individual company's compensation offer.

An absent salary statistic is unknown, not a zero salary. A large salary figure from another region or currency is not a valid substitute for a sparse requested sample.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/hiring-signals-jobs-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
