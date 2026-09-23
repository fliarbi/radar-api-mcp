# Companies offering internships API: employer lists and observed role counts

[All endpoints](README.md) · [Workflow guide](../guides/internships-companies-api.md)

Group matching internship records into an employer list, with counts, latest posting date, up to five sample titles and IDs for follow-up detail requests.

## Route, authentication and credits

**`POST /v1/jobs/internships/companies`** · MCP tool **`companies_offering_internships`** · key scope **`jobs`**.
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
| `title` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `company` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `location` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `skills` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `work_mode` | default `"any"` | string; one of `any`, `remote`, `onsite` |
| `part_time` | default `false` | boolean |
| `stipend_min` | default `null` | number or null; maximum: `10000000` |
| `posted_since` | default `null` | string or null |
| `posted_until` | default `null` | string or null |
| `validity` | default `"observed"` | string; one of `observed`, `not_expired` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/jobs/internships/companies" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"title":"Business Development","limit":3}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: companies_offering_internships -->
```json
{
  "name": "companies_offering_internships",
  "arguments": {
    "request": {
      "title": "Business Development",
      "limit": 3
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: companies_offering_internships -->
```json
{
  "ok": true,
  "feature": "companies_offering_internships",
  "data": {
    "companies": [
      {
        "name": "Across The Globe (ATG)",
        "company_domain": null,
        "observed_internships": 2,
        "latest_posted": "2026-06-19",
        "sample_titles": [
          "Business Development Executive - Internship (WFH & Part Time)",
          "Business Development & Client Relations - Internship (WFH)"
        ],
        "sample_internship_ids": [
          "1781859880",
          "1780995392"
        ],
        "current_openings_verified": false
      },
      {
        "name": "Estate Plus CRM",
        "company_domain": null,
        "observed_internships": 2,
        "latest_posted": "2026-07-03",
        "sample_titles": [
          "Business Development (Sales) - Internship (WFH & Part Time)",
          "Business Development (Sales) - Internship (WFH & Part Time)"
        ],
        "sample_internship_ids": [
          "1783075957",
          "1780743453"
        ],
        "current_openings_verified": false
      },
      {
        "name": "Fin Maverick",
        "company_domain": null,
        "observed_internships": 2,
        "latest_posted": "2026-06-22",
        "sample_titles": [
          "Business Development (NISM Mandatory) - Internship (WFH)",
          "Business Development (Sales) - Internship (WFH)"
        ],
        "sample_internship_ids": [
          "1782126972",
          "1781758426"
        ],
        "current_openings_verified": false
      }
    ],
    "page": 0,
    "limit": 3,
    "has_more": true,
    "grouping": "Exact source employer name, not a verified company identity or domain join",
    "note": "These are observed internship listings, not verified current vacancies. Posted and crawl dates are separate. Far-future source deadlines are not proof a listing remains open. Stipend periods are not supplied."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:58.828671+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:58.828822+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/companies_offering_internships.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Business Development example shows Across The Globe (ATG), Estate Plus CRM and Fin Maverick, with two matching observed internships each and real listing IDs.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.companies[].observed_internships` | Count of matching source records under this exact employer name, not verified current openings. |
| `data.companies[].sample_internship_ids` | Concrete IDs for get_internship; samples are bounded to five per employer. |
| `data.grouping` | Exact source name; name variants can remain separate and collisions are possible. |
| `data.has_more` | Continue zero-based pages to inspect more matching employer groups. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Apply the same filters as internship search, choose an employer, inspect sample details and resolve a company identity separately before joining financials or contacts.

These records are historical observations, not verified open vacancies. Future or placeholder deadlines do not establish current availability. Stipend currency is supplied where recorded; payment period is unknown. Employer names are not automatically joined to company domains.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/internships-companies-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
