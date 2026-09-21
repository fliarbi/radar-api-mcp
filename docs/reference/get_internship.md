# Internship detail API: role description, requirements, stipend and application URL

[All endpoints](README.md) · [Workflow guide](../guides/internships-companies-api.md)

Retrieve a specific internship ID returned by search or employer grouping. Full API responses include the source role description alongside structured qualifications and compensation fields.

## Route, authentication and credits

**`POST /v1/jobs/internships/detail`** · MCP tool **`get_internship`** · key scope **`jobs`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `id` | required | string; min characters: `1`; max characters: `100`; pattern: `^[A-Za-z0-9_-]+$` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/jobs/internships/detail" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"id":"1783055647"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_internship -->
```json
{
  "name": "get_internship",
  "arguments": {
    "request": {
      "id": "1783055647"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_internship -->
```json
{
  "ok": true,
  "feature": "get_internship",
  "data": {
    "internship": {
      "id": "1783055647",
      "title": "Business Development (Sales) - Internship (WFH)",
      "company": "MITRA Consultancy",
      "company_domain": null,
      "url": "https://internshala.com/internship/detail/work-from-home-business-development-sales-internship-at-mitra-consultancy1783055647",
      "posted": "2026-07-03",
      "valid_through": "2026-08-02 23:59:59",
      "validity_status": "expired",
      "current_opening_verified": false,
      "employment_type": "INTERN, FULL_TIME",
      "locations": [
        {
          "locality": "Patna",
          "region": "Bihar",
          "country": "IN"
        }
      ],
      "skills": [
        "Social Media Marketing",
        "Email Marketing",
        "English Proficiency (Spoken)",
        "English Proficiency (Written)"
      ],
      "work_mode": "remote_indicated",
      "industry": "Computer Services",
      "experience_months": null,
      "stipend": {
        "value": 2200,
        "currency": "INR",
        "period": null
      },
      "salary": {
        "min": null,
        "max": null,
        "currency": "INR",
        "period": null
      },
      "scraped_at": 1783143472,
      "last_seen": 1783143472,
      "source": "internshala",
      "occupational_category": null
    },
    "note": "These are observed internship listings, not verified current vacancies. Posted and crawl dates are separate. Far-future source deadlines are not proof a listing remains open. Stipend periods are not supplied."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T10:48:29.956533+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-21T10:48:29.956706+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_internship.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The detail uses the actual MITRA Consultancy ID from the search response, preserving role requirements, locations, stipend and expired deadline. No placeholder ID or fabricated successful profile is used.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.internship.description` | Stored role description, available in the API; lengthy source prose is omitted explicitly from the documentation excerpt. |
| `data.internship.skills / experience_months` | Recorded requirements; null experience remains unknown. |
| `data.internship.stipend / salary` | Observed values and currency; period stays null when absent. |
| `data.internship.validity_status` | expired, future_deadline_unverified, not_expired_by_source_date or unknown. |
| `data.internship.url` | Original listing/application page; the API does not submit applications. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Request the returned ID, inspect source dates and follow the source URL manually if pursuing the role. IDs from normalized jobs belong to get_job, not this dedicated endpoint.

These records are historical observations, not verified open vacancies. Future or placeholder deadlines do not establish current availability. Stipend currency is supplied where recorded; payment period is unknown. Employer names are not automatically joined to company domains.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/internships-companies-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
