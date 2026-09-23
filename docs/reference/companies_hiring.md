# Hiring companies API: discover employers from recruitment signals

[All endpoints](README.md) · [Workflow guide](../guides/hiring-signals-jobs-api.md)

Use the same job filters to discover companies associated with observed hiring. This is useful when your unit of research is the employer rather than an individual vacancy. It is separate from firmographic company search and from a measured headcount-growth dataset.

## Route, authentication and credits

**`POST /v1/jobs/companies`** · MCP tool **`companies_hiring`** · key scope **`jobs`**.
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
| `company` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `city` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `country` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `skills` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `remote` | default `false` | boolean |
| `employment_type` | default `null` | string or null; one of `full_time`, `part_time`, `contract`, `temporary`, `internship`, `intern`, `freelance` |
| `salary_min` | default `null` | number or null; maximum: `1000000000` |
| `min_experience_months` | default `null` | integer or null; minimum: `1`; maximum: `960` |
| `max_experience_months` | default `null` | integer or null; minimum: `1`; maximum: `960` |
| `sources` | optional; empty by default | array of string; max items: `3`; one of `foundit`, `shine`, `talent` |
| `freshness_days` | default `null` | integer or null; minimum: `1`; maximum: `365` |
| `sort_by` | default `"recent"` | string; one of `recent`, `relevance`, `salary` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/jobs/companies" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"title":"machine learning engineer","country":"US","limit":3}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: companies_hiring -->
```json
{
  "name": "companies_hiring",
  "arguments": {
    "request": {
      "title": "machine learning engineer",
      "country": "US",
      "limit": 3
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: companies_hiring -->
```json
{
  "ok": true,
  "feature": "companies_hiring",
  "data": {
    "companies": [
      {
        "name": "AHU Technologies Inc",
        "domain": null,
        "open_roles": 3,
        "top_titles": [
          "Machine Learning Engineer - Recommendation Systems - Mandarin Required",
          "Machine Learning Engineer - United States - Remote",
          "Machine Learning Engineer Mandarin Required"
        ],
        "locations": [
          "Washington"
        ]
      },
      {
        "name": "Molex",
        "domain": null,
        "open_roles": 2,
        "top_titles": [
          "Machine Learning Engineer",
          "Machine Learning Engineer"
        ],
        "locations": [
          "Lisle"
        ]
      },
      {
        "name": "TekCommands Inc",
        "domain": null,
        "open_roles": 2,
        "top_titles": [
          "Machine Learning Engineer",
          "Machine Learning Engineer (Senior Level)"
        ],
        "locations": []
      }
    ],
    "total": 3,
    "total_capped": true,
    "access": {
      "plan": "free",
      "results_per_query": 15,
      "searches_per_month": 50,
      "anonymous": true
    },
    "plan": "free",
    "partial_timeout": false,
    "returned": 3,
    "rollup_note": "Ranked by matching roles in a bounded source scan; total describes returned groups, not all hiring companies. Page offsets are unsupported."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:58.896496+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:58.896665+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/companies_hiring.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The narrower US machine learning engineer query returns three employers with observed open-role counts, example titles and locations, without a partial timeout. total_capped=true remains visible: three is the delivered grouped result, not a complete count of every employer hiring for that role. Missing resolved domains are not inferred from employer names.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.companies` | Returned hiring-company records when available. |
| `data.total / total_capped` | Source count and any cap, subject to partial coverage. |
| `data.partial_timeout` | A partial empty result must not be treated as a complete negative result. |
| `data.access` | Linked plan and query-result restrictions. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Select a skill, role or geography, inspect returned company identity, and retrieve its company profile before enriching an account list. Keep the source query and partial status alongside the hiring observation so a later analyst can assess the evidence.

A vacancy signal is not a confirmed net-new employee or a company's total workforce. Do not rank business growth solely from a partial hiring feed.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/hiring-signals-jobs-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
