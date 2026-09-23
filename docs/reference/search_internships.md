# Internship data API: roles, skills, stipends, locations and posting dates

[All endpoints](README.md) · [Workflow guide](../guides/internships-companies-api.md)

Search Radar’s dedicated internship records, in addition to the normalized jobs index. Return structured internship cards with application URLs, employer names, skills, stipends, source dates and explicit validity qualifications.

## Route, authentication and credits

**`POST /v1/jobs/internships/search`** · MCP tool **`search_internships`** · key scope **`jobs`**.
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
curl --fail-with-body -X POST "$RADAR_API_URL/v1/jobs/internships/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"title":"Business Development","limit":3}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_internships -->
```json
{
  "name": "search_internships",
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

<!-- response-example: search_internships -->
```json
{
  "ok": true,
  "feature": "search_internships",
  "data": {
    "internships": [
      {
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
        "detail_request": {
          "method": "POST",
          "path": "/v1/jobs/internships/detail"
        }
      },
      {
        "id": "1783057160",
        "title": "Business Development (Sales) - Internship (WFH)",
        "company": "STEM-Xpert, Techgenius Innovations Pvt Ltd",
        "company_domain": null,
        "url": "https://internshala.com/internship/detail/work-from-home-business-development-sales-internship-at-stem-xpert-techgenius-innovations-pvt-ltd1783057160",
        "posted": "2026-07-03",
        "valid_through": "2026-08-02 23:59:59",
        "validity_status": "expired",
        "current_opening_verified": false,
        "employment_type": "INTERN, FULL_TIME",
        "locations": [
          {
            "locality": "Kozhikode",
            "region": "Kerala",
            "country": "IN"
          }
        ],
        "skills": [
          "Presentation skills",
          "Cold Calling",
          "Client Relationship Management (CRM)",
          "English Proficiency (Spoken)",
          "Hindi Proficiency (Spoken)",
          "Effective Communication",
          "Scheduling"
        ],
        "work_mode": "remote_indicated",
        "industry": "Education",
        "experience_months": null,
        "stipend": {
          "value": null,
          "currency": "INR",
          "period": null
        },
        "salary": {
          "min": 9000,
          "max": 21000,
          "currency": "INR",
          "period": null
        },
        "scraped_at": 1783143472,
        "last_seen": 1783143472,
        "source": "internshala",
        "detail_request": {
          "method": "POST",
          "path": "/v1/jobs/internships/detail"
        }
      },
      {
        "id": "1783059373",
        "title": "Business Development (Sales) - Internship (WFH)",
        "company": "BABY DINO",
        "company_domain": null,
        "url": "https://internshala.com/internship/detail/work-from-home-business-development-sales-internship-at-baby-dino1783059373",
        "posted": "2026-07-03",
        "valid_through": "2026-08-02 23:59:59",
        "validity_status": "expired",
        "current_opening_verified": false,
        "employment_type": "INTERN, FULL_TIME",
        "locations": [
          {
            "locality": "Jaipur",
            "region": "Rajasthan",
            "country": "IN"
          }
        ],
        "skills": [
          "Social Media Marketing",
          "Digital Marketing",
          "Email Marketing",
          "MS-Excel",
          "English Proficiency (Spoken)",
          "English Proficiency (Written)"
        ],
        "work_mode": "remote_indicated",
        "industry": "Business , Marketing",
        "experience_months": null,
        "stipend": {
          "value": null,
          "currency": "INR",
          "period": null
        },
        "salary": {
          "min": 1000,
          "max": 10000,
          "currency": "INR",
          "period": null
        },
        "scraped_at": 1783143472,
        "last_seen": 1783143472,
        "source": "internshala",
        "detail_request": {
          "method": "POST",
          "path": "/v1/jobs/internships/detail"
        }
      }
    ],
    "total": 222,
    "page": 0,
    "limit": 3,
    "has_more": true,
    "note": "These are observed internship listings, not verified current vacancies. Posted and crawl dates are separate. Far-future source deadlines are not proof a listing remains open. Stipend periods are not supplied."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:58.817889+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:58.818080+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_internships.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Business Development prefix capture returns three of 222 matching observed internships. The leading MITRA Consultancy listing has four skills, INR 2,200 stipend value, a July 3 posting date and an expired August 2 deadline.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.internships` | Every returned card includes status qualifications and a separate detail request. |
| `data.total` | Count matching these filters in the dedicated internship source. |
| `data.page / limit / has_more` | Zero-based pages ordered by posting date descending and ID as a stable tie-breaker. |
| `data.internships[].work_mode` | remote_indicated from explicit title/locality markers, location_listed or unknown; missing location does not imply remote. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Filter employer/title prefixes, location, skills, part-time, work mode, minimum stipend and posting-date window. Use validity=not_expired to exclude expired and far-future deadlines, then inspect source URLs before treating a role as open.

These records are historical observations, not verified open vacancies. Future or placeholder deadlines do not establish current availability. Stipend currency is supplied where recorded; payment period is unknown. Employer names are not automatically joined to company domains.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/internships-companies-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
