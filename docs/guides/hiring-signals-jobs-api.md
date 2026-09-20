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
