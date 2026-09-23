# Hiring signals API: job listings, hiring companies and salary benchmarks

Hiring data can add useful context to company research. Radar exposes job search,
hiring-company search, individual job retrieval and salary benchmarks. Use these
operations to inspect observed recruitment activity for a company, role, skill or
location, while retaining source coverage and sample-size limits.

An observed job posting is a hiring signal, not proof of a filled position or a
measured change in employee count. The gateway does not infer headcount growth
from job counts or promise a complete live inventory of vacancies.

## Find recent jobs for a company

`search_jobs` maps to `POST /v1/jobs/search`:

```json
{"company":"Microsoft","title":"software engineer","freshness_days":30,"limit":20,"page":0}
```

Other filters include query text, city, country, skills, remote status and
employment type. Use `companies_hiring` (`POST /v1/jobs/companies`) with the same
input model when your desired output is a company-discovery view.
`company` is an employer-name prefix in the Jobs source, not a domain lookup.
Use a returned `company_domain` for company-profile research when one is available;
many observed listings have a name but no resolved domain.

Job search uses numbered pages with the same bounded `page` and `limit` model as
company search. The companies_hiring rollup is different: it ranks groups by matching
roles in a bounded source scan and does not support page offsets or salary/relevance
sorting. The gateway rejects those options instead of pretending to paginate. The upstream account can impose tighter result limits. Check
whether a small result set reflects coverage, query specificity or access limits
before describing it as a complete hiring trend.

## Retrieve a job and inspect a salary benchmark

Pass an ID returned by search to `get_job` (`POST /v1/jobs/detail`), using a body
such as `{"id":"id-returned-by-job-search"}`. This is retrieval only: the gateway
does not submit applications, upload resumes or contact employers.

`salary_benchmark` maps to `POST /v1/jobs/salary-benchmark`:

```json
{"title":"software engineer","country":"US","currency":"USD"}
```

Keep returned sample size, currency and coverage visible. A benchmark calculated
from a limited observed sample should not be presented as an exact company salary
or a guaranteed compensation offer. Avoid mixing currencies or geographic samples
without a separate, documented normalization method.

## Connect hiring to company intelligence

Retrieve a company profile and enrichment after finding a relevant employer.
Combine hiring observations with company events and source-backed financial
metrics when building an account-research page. Label each section with its own
date and source context; hiring, news and financial records need not update on
the same schedule.

Related: [company enrichment](company-enrichment-api.md), [B2B data API](b2b-data-api.md),
[company monitoring](company-monitoring-api.md), [API usage limits](pricing-pay-per-use.md).

## Discover filters and use salary, experience and internship options

Read `job_filter_catalog` at `POST /v1/jobs/filters` for the current input schema
and source semantics. Request suggestions with `job_filter_options`:

```json
{"field":"skills","q":"Python","limit":5}
```

Suggestion fields are title, skills, company and location. Empty suggestions can
also reflect a source lookup failure. Title and employer search use prefixes;
skills use OR matches and q uses the source text-search index.

```json
{"title":"software","employment_type":"internship","sources":["shine"],"min_experience_months":1,"max_experience_months":12,"salary_min":1000,"sort_by":"salary","limit":10}
```

The public internship alias is translated to Radar's normalized intern value.
Other types include full_time, part_time, contract, temporary and freelance.
Sources are foundit, shine and talent. Experience bounds are positive months and
must be ordered. salary_min tests the source's recorded salary_max, without
normalizing currency or pay period. Salary sorting shares that limitation.
remote=true filters remote records; false adds no onsite restriction.

For the additional dedicated internship records, employer groups, stipend filters,
posting windows and deadline qualifications, use the
[companies offering internships workflow](internships-companies-api.md).
For prioritizing company research from hiring signals, see
[company potential and sales prospects](potential-company-data-api.md).

<!-- scenario-links -->
## Executed scenarios for this workflow

- [37-us-software-jobs: Find observed US software engineer job postings.](../scenarios/37-us-software-jobs.md)
- [38-normalized-interns: Find internship-type records from Shine using the public internship alias.](../scenarios/38-normalized-interns.md)
- [39-company-skill-jobs: Find Microsoft job listings mentioning Python skills.](../scenarios/39-company-skill-jobs.md)
- [40-salary-benchmark: Retrieve the USD software-engineer salary benchmark for the US with sample size.](../scenarios/40-salary-benchmark.md)

<!-- captured-workflow -->
## Handle incomplete hiring searches before counting demand

The earlier broad engineer query timed out and returned an empty page with a capped
estimate. The updated title-prefix query for software engineer in the US returns
three listings from 503 matches without a partial timeout. This demonstrates why
an incomplete search should be retried with a more specific role and geography,
rather than converted into a conclusion that there are no vacancies.

Use the returned job ID for detail retrieval only after a successful result gives
you one. The current example retrieves the Software Engineer Controls listing at
Optimal Inc. using its actual returned ID. Its missing salary and company domain
remain null. A role title or employer name cannot substitute for a listing ID.

Hiring-company discovery has its own partial flag, and salary benchmarks require
a sufficient source sample. The updated US/software engineer/USD benchmark has
206 observations, with a source median of 124,000 USD. This is a different explicit
geography and role query, not a filled-in value for the earlier sparse India sample.
The source aggregates salary midpoints; do not infer a pay period that is absent
from its response. Keep role, geography, currency,
freshness and sample count visible in a compensation view. A posted vacancy is a
recruitment observation; it does not establish that an employee was hired or that
the employer's total workforce grew by one.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/jobs/search`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: search_jobs -->
```json
{
  "title": "software engineer",
  "country": "US",
  "limit": 3
}
```

<!-- response-example: search_jobs -->
```json
{
  "ok": true,
  "feature": "search_jobs",
  "data": {
    "jobs": [
      {
        "id": "talent:636631531523081796",
        "title": "Software Engineer Controls",
        "company": "Optimal Inc.",
        "company_domain": null,
        "logo": null,
        "locations": [
          "Sunrise, Florida, US"
        ],
        "remote": false,
        "salary": {
          "min": null,
          "max": null,
          "currency": null
        },
        "experience": null,
        "skills": [],
        "posted": "2026-09-11",
        "url": "https://www.talent.com/view?id=636631531523081796",
        "direct_apply": false,
        "source": "talent"
      },
      {
        "id": "talent:636864770441742421",
        "title": "Software Engineer (Colorado)",
        "company": "Kestrel Intelligence",
        "company_domain": null,
        "logo": null,
        "locations": [
          "Colorado Springs, Colorado, US"
        ],
        "remote": false,
        "salary": {
          "min": null,
          "max": null,
          "currency": null
        },
        "experience": null,
        "skills": [],
        "posted": "2026-09-11",
        "url": "https://www.talent.com/view?id=636864770441742421",
        "direct_apply": false,
        "source": "talent"
      },
      {
        "id": "talent:636478413375605243",
        "title": "Software Engineer - Backend",
        "company": "Kintara",
        "company_domain": null,
        "logo": null,
        "locations": [
          "Grandview Heights, Ohio, US"
        ],
        "remote": false,
        "salary": {
          "min": null,
          "max": null,
          "currency": null
        },
        "experience": null,
        "skills": [],
        "posted": "2026-09-08",
        "url": "https://www.talent.com/view?id=636478413375605243",
        "direct_apply": false,
        "source": "talent"
      }
    ],
    "total_estimate": 503,
    "total_capped": false,
    "page": 0,
    "page_size": 3,
    "access": {
      "plan": "free",
      "results_per_query": 15,
      "searches_per_month": 50,
      "anonymous": true
    },
    "plan": "free",
    "partial_timeout": false
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T02:35:05.321506+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-21T02:35:05.321679+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_jobs.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

A software engineer title-prefix query in the US returns three real job listings from 503 matches with partial_timeout=false and total_capped=false. Cards include returned IDs, employer names, locations, posting dates and source URLs. Unknown salary and company-domain fields remain null. The first returned ID successfully resolves in the job-detail example.

See the [complete search_jobs endpoint reference](../reference/search_jobs.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
