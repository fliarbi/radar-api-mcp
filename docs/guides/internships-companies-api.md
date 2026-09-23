# Internship data API: find companies offering internships, roles, skills and stipends

Radar provides both normalized job search and a dedicated internship collection.
Use this workflow to build employer lists, research early-career hiring activity,
find skill requirements and inspect source application pages. Keep historical
listings separate from verified current openings.

## Search dedicated internship records

`POST /v1/jobs/internships/search` / `search_internships`:

```json
{"title":"Business Development","skills":["English Proficiency (Spoken)"],"part_time":true,"work_mode":"remote","stipend_min":1000,"limit":20,"page":0}
```

The source also stores ordinary jobs; this endpoint explicitly selects only
posting_type=internship. Filters support title and employer-name prefixes,
location prefixes (locality, region or country), an OR list of exact skill names,
part_time=true, work_mode, minimum stipend, posting-date windows and validity.
Country values can be source codes such as IN rather than spelled-out names.
Text is escaped; clients cannot supply database expressions.

Use posted_since and posted_until in YYYY-MM-DD. Results are ordered by posting
date descending, then ID; pages start at zero, limits are 1–100 and has_more
indicates continuation. total counts records matching the same source query.
part_time=false adds no part-time filter; it does not mean full-time-only.

Remote matching requires an explicit remote, work-from-home or WFH marker in the
source title or locality. Empty locations remain unknown. The onsite filter means
a location is listed without an explicit remote marker; it does not independently
confirm an office-attendance requirement. Returned work_mode is remote_indicated,
location_listed or unknown, preserving this distinction.

## Discover employers and retrieve actual listings

`POST /v1/jobs/internships/companies` / `companies_offering_internships`:

```json
{"title":"Business Development","limit":10,"page":0}
```

The employer response contains exact source name, observed_internships count,
latest_posted, up to five sample titles and sample_internship_ids. It is ranked
by matching observation count, then name, and supports pages. A count reflects
only your filters. Exact-name grouping may split name variants or combine
ambiguous names; company_domain stays null until identity is resolved separately.

`POST /v1/jobs/internships/detail` / `get_internship`:

```json
{"id":"1783055647"}
```

This captured ID belongs to MITRA Consultancy's Business Development (Sales)
internship. The API returns description, skills, locations, industry, experience,
stipend and salary fields, application URL, posting/deadline dates and crawl
observations. Use IDs returned by the dedicated internship workflow. Normalized
job IDs belong to `/v1/jobs/detail` instead.

## Dates and compensation are part of the result

The real Business Development search found 222 matching historical observations.
The leading example was posted July 3, 2026, with an August 2 deadline; its
validity_status is expired. It records an INR 2,200 stipend, but no payment period.
Do not label that value monthly, annual or per internship without source evidence.
Crawl timestamps are Unix seconds; posted dates and deadline strings retain source
formatting. A listing may be remote even when a city is also recorded.

`validity=observed` includes dated history. `validity=not_expired` keeps source
deadlines from today through less than a year ahead, excluding far-future values
such as 2035 placeholders. Even these results have current_opening_verified=false:
a deadline alone cannot establish that applications remain open. The four status
values are expired, future_deadline_unverified, not_expired_by_source_date and unknown.

For internships indexed with general jobs, request employment_type=internship
(or intern) through search_jobs. The gateway translates internship to Radar's
normalized intern value. The dedicated and general indexes are not deduplicated;
do not sum their totals into a universal vacancy count.

All dedicated internship operations use the jobs scope and cost one successful
operation credit in account mode. Responses retain public listing URLs; the API
does not submit applications, upload resumes or send messages.

Related: [jobs and salary filters](hiring-signals-jobs-api.md), [employer reference](../reference/companies_offering_internships.md),
[detail output](../reference/get_internship.md), [company search](company-search-api.md).

<!-- scenario-links -->
## Executed scenarios for this workflow

- [41-remote-part-time-interns: Find observed remote part-time internships with explicit work-mode evidence.](../scenarios/41-remote-part-time-interns.md)
- [42-internship-employers: Which source employers have Business Development internship listings?](../scenarios/42-internship-employers.md)
- [43-internship-stipend: Find observed internship listings with stipend value at least 10,000, preserving currency and unknown period.](../scenarios/43-internship-stipend.md)

<!-- captured-workflow -->
## Use observed internship data without inventing current vacancies

This source contains ordinary jobs as well as internships. The API always selects internship records explicitly. The example retains three complete structured cards, including skills, stipend, source dates, validity and application URLs. Its total is 222 matching observations; it is not 222 verified current vacancies.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/jobs/internships/search`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: search_internships -->
```json
{
  "title": "Business Development",
  "limit": 3
}
```

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
    "retrieved_at": "2026-09-21T10:48:29.937867+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-21T10:48:29.938073+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_internships.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Business Development prefix capture returns three of 222 matching observed internships. The leading MITRA Consultancy listing has four skills, INR 2,200 stipend value, a July 3 posting date and an expired August 2 deadline.

See the [complete search_internships endpoint reference](../reference/search_internships.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
