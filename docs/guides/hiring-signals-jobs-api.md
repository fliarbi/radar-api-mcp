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
{"company":"microsoft.com","title":"engineer","freshness_days":30,"limit":20,"page":0}
```

Other filters include query text, city, country, skills, remote status and
employment type. Use `companies_hiring` (`POST /v1/jobs/companies`) with the same
input model when your desired output is a company-discovery view.

Job search uses numbered pages with the same bounded `page` and `limit` model as
company search. The upstream account can impose tighter result limits. Check
whether a small result set reflects coverage, query specificity or access limits
before describing it as a complete hiring trend.

## Retrieve a job and inspect a salary benchmark

Pass an ID returned by search to `get_job` (`POST /v1/jobs/detail`), using a body
such as `{"id":"id-returned-by-job-search"}`. This is retrieval only: the gateway
does not submit applications, upload resumes or contact employers.

`salary_benchmark` maps to `POST /v1/jobs/salary-benchmark`:

```json
{"title":"engineer","country":"India","currency":"INR"}
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

<!-- captured-workflow -->
## Handle incomplete hiring searches before counting demand

The actual engineer query returned an empty jobs array, a capped estimate of 10,000
and a partial-timeout flag. Those fields must be interpreted together. The response
does not supply ten thousand accessible job records, and it also cannot prove
there are no matching vacancies. A hiring dashboard should display an incomplete
search state and preserve its previous observations while a narrower retry runs.

Use the returned job ID for detail retrieval only after a successful result gives
you one. This capture supplied no ID, so the job-detail example deliberately
demonstrates a real 404 for a nonexistent identifier. Do not copy that negative
sample ID into a production integration. A role title or company domain cannot
be substituted for a listing identifier.

Hiring-company discovery has its own partial flag, and salary benchmarks require
a sufficient source sample. The India/engineer/INR benchmark returned zero observed
records with `sparse=true`, not a zero salary. Keep role, geography, currency,
freshness and sample count visible in a compensation view. A posted vacancy is a
recruitment observation; it does not establish that an employee was hired or that
the employer's total workforce grew by one.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/jobs/search`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: search_jobs -->
```json
{
  "q": "engineer",
  "limit": 2
}
```

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

See the [complete search_jobs endpoint reference](../reference/search_jobs.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
