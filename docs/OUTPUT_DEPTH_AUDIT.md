# Radar API output audit: company, financial, investor, app, jobs and news data

The audit covers every data operation and every account/discovery JSON operation.
It compares gateway output with the source adapter, reviews endpoint ownership,
and records a new live probe rather than treating an old HTTP 200 as current proof.
The [machine-readable evidence](research/endpoint-output-audit.json) contains all
requests, statuses, timestamps, response fingerprints, before/after shape changes
and reviewed adapter hashes. Private raw source responses remain outside the repo.

## What became richer

| Data requested | New retained information | Separate owner |
|---|---|---|
| Company traffic | Ranks, device visits/shares, engagement, backlinks, referring domains, traffic connections, countries and keywords | `get_company_field`, `field=traffic` |
| Customer reputation | Stored review profile and distinct review samples, with separate observation dates and source totals | `get_company_field`, `field=reputation` |
| Company classification | Structured sector context alongside existing sector names | `get_company_field`, `field=classification` |
| Lifecycle | Source xcorn rationale, parent/listing/acquisition context and achievements | `get_company_field`, `field=lifecycle` |
| Assessments | Uniqueness/scalability label, tagline and rationale alongside scores | `get_company_field`, `field=assessments` |
| Financial statements | Per-period evidence/quality, headcount, recorded growth and guidance; source summary comparisons and coverage | `get_financials` |
| App details | Install display/bands, score/price text, release changes and Android version display | Selected `get_app_field` |
| Internship detail | First-seen epoch and direct-apply indicator, separate from posted/expiry dates | `get_internship` |
| Investor fields | Observed empty arrays remain available and discoverable, distinct from missing/null | `get_investor_page` / `get_investor_field` |
| News failures | Explicit strict-coverage error instead of generic upstream failure | Existing News operations |

See [complete company examples](COMPANY_DATA_DEPTH.md), [financial evidence](guides/financial-data-api.md),
[all seven app fields](APP_DATA_DEPTH.md), and [investor fields](INVESTOR_DATA_DEPTH.md).
The refreshed company samples include three traffic snapshots and 60 distinct
stored customer-review sample rows across Razorpay, Stripe and Swiggy. Sample
counts do not represent the source review populations.

## How endpoint boundaries are preserved

Compact company and app profiles still return identity and field discovery. New
traffic/review values require a selected field request. Existing keys, value types
and arrays remain; native detail is not copied into search cards or the legacy
enrichment bundle. Briefs/comparisons retain compact sections and follow-up requests.
Financial screens reuse entitled normalized financial evidence and their existing
bounded candidate rules. Financial context never reads a deeper native archive.

The [selected-field conservation check](research/selected-field-conservation.json)
compares all 54 company fields and seven app fields with the previous commit.
Every existing business value survives unchanged in 56 of 61 captures. Three
hiring snapshots changed at source; Razorpay and Stripe innovation sections are
currently absent from derived enrichment. All five differences were independently
matched to the current native source projection. The API does not fill these
gaps with stale values from earlier examples. Primary before/after shape checks
removed only error branches for recovered component requests, not business fields.

Company founders and professional affiliation belong to team/people reads;
emails/phones belong to explicit, scoped, paid-plan contact reads. App developer
contacts and review author identities are not selected. Investor publication and
snapshot integrity checks remain in force. Authentication, usage charging, request
limits, response caps and read-only MCP behavior are unchanged.

Traffic source connections can repeat labels, and direction/denominators were not
retained. They cannot be summed into a complete acquisition mix. Review samples are
not a representative survey. Source corporate milestones and assessment rationale
are claims, not independently verified company facts. An unknown value stays null;
observed zeros/negative financial values survive. Partial store failures retain
available data while marking the missing part unavailable.

## Current live limitations

The two contact probes correctly returned `403 scope_required`; no paid contact
values were retrieved. Location intelligence still returned an upstream error.
The general News corpus could not establish strict coverage because a database
shard was unreachable. The gateway now preserves `503 coverage_unavailable` and
does not report incomplete corpus totals as success. Business-event and funding
queries have separate coverage and succeeded. These isolated News integration
calls verify actual data queries, not deployed production-key authentication.

Historical successful News examples remain visibly dated. Use the current probe
below for current availability. Live probes are bounded examples, not a guarantee
of every filter combination or full database parity. Employee-review analytics
keyed only by unverified company slugs were not joined by guessed names; those
need an authoritative domain mapping before they can safely extend reputation.

## Every data endpoint

| Operation | Owner/family | Latest probe HTTP | Outcome |
|---|---|---:|---|
| [search_companies](reference/search_companies.md) | Company discovery | 200 | Response captured |
| [semantic_company_search](reference/semantic_company_search.md) | Company discovery | 200 | Response captured |
| [get_company](reference/get_company.md) | Compact company identity | 200 | Response captured |
| [get_company_field](reference/get_company_field.md) | Selected company detail | 200 | Response captured |
| [company_apps](reference/company_apps.md) | App data | 200 | Response captured |
| [opportunity_presets](reference/opportunity_presets.md) | Potential-company research | 200 | Response captured |
| [search_opportunities](reference/search_opportunities.md) | Potential-company research | 200 | Response captured |
| [company_filter_catalog](reference/company_filter_catalog.md) | Company discovery schema | 200 | Response captured |
| [company_filter_options](reference/company_filter_options.md) | Company discovery schema | 200 | Response captured |
| [get_company_columns](reference/get_company_columns.md) | Company discovery schema | 200 | Response captured |
| [get_company_intelligence](reference/get_company_intelligence.md) | Company assessments and events | 200 | Response captured |
| [financial_filter_catalog](reference/financial_filter_catalog.md) | Financial research | 200 | Response captured |
| [screen_company_financials](reference/screen_company_financials.md) | Financial research | 200 | Response captured |
| [get_company_team](reference/get_company_team.md) | Company team | 200 | Response captured |
| [get_financials](reference/get_financials.md) | Financial research | 200 | Response captured |
| [get_company_events](reference/get_company_events.md) | Company assessments and events | 200 | Response captured |
| [get_company_funding](reference/get_company_funding.md) | Company assessments and events | 200 | Response captured |
| [get_company_enrichment](reference/get_company_enrichment.md) | Company assessments and events | 200 | Response captured |
| [find_competitors](reference/find_competitors.md) | Company discovery | 200 | Response captured |
| [company_brief](reference/company_brief.md) | Compact research composition | 200 | Response captured |
| [compare_companies](reference/compare_companies.md) | Compact research composition | 200 | Response captured |
| [search_investors](reference/search_investors.md) | Company discovery | 200 | Response captured |
| [investor_directory](reference/investor_directory.md) | Investor data | 200 | Response captured |
| [get_investor_page](reference/get_investor_page.md) | Investor data | 200 | Response captured |
| [get_investor_field](reference/get_investor_field.md) | Investor data | 200 | Response captured |
| [market_pulse](reference/market_pulse.md) | Market and geographic discovery | 200 | Response captured |
| [location_intelligence](reference/location_intelligence.md) | Market and geographic discovery | 502 | upstream_unavailable |
| [discover_industries](reference/discover_industries.md) | Market and geographic discovery | 200 | Response captured |
| [search_jobs](reference/search_jobs.md) | Jobs and salaries | 200 | Response captured |
| [job_filter_catalog](reference/job_filter_catalog.md) | Jobs and salaries | 200 | Response captured |
| [job_filter_options](reference/job_filter_options.md) | Jobs and salaries | 200 | Response captured |
| [search_internships](reference/search_internships.md) | Internship data | 200 | Response captured |
| [companies_offering_internships](reference/companies_offering_internships.md) | Internship data | 200 | Response captured |
| [get_internship](reference/get_internship.md) | Internship data | 200 | Response captured |
| [companies_hiring](reference/companies_hiring.md) | Jobs and salaries | 200 | Response captured |
| [get_job](reference/get_job.md) | Jobs and salaries | 200 | Response captured |
| [salary_benchmark](reference/salary_benchmark.md) | Jobs and salaries | 200 | Response captured |
| [search_apps](reference/search_apps.md) | App data | 200 | Response captured |
| [get_app](reference/get_app.md) | App data | 200 | Response captured |
| [get_app_field](reference/get_app_field.md) | App data | 200 | Response captured |
| [app_filter_options](reference/app_filter_options.md) | App data | 200 | Response captured |
| [search_people](reference/search_people.md) | Professional discovery | 200 | Response captured |
| [people_filter_options](reference/people_filter_options.md) | Professional discovery | 200 | Response captured |
| [get_company_contacts](reference/get_company_contacts.md) | Scoped contacts | 403 | scope_required |
| [get_person_contacts](reference/get_person_contacts.md) | Scoped contacts | 403 | scope_required |
| [search_news](reference/search_news.md) | News and business evidence | 503 | coverage_unavailable |
| [search_business_news](reference/search_business_news.md) | News and business evidence | 503 | coverage_unavailable |
| [news_overview](reference/news_overview.md) | News and business evidence | 503 | coverage_unavailable |
| [news_trends](reference/news_trends.md) | News and business evidence | 503 | coverage_unavailable |
| [news_sentiment](reference/news_sentiment.md) | News and business evidence | 503 | coverage_unavailable |
| [search_business_events](reference/search_business_events.md) | News and business evidence | 200 | Response captured |
| [search_funding_news](reference/search_funding_news.md) | News and business evidence | 200 | Response captured |
| [get_article](reference/get_article.md) | News and business evidence | 503 | coverage_unavailable |

## Account and discovery operations

All 16 JSON control operations were recaptured using the isolated account fixture. Key creation/revocation, plans, usage, spending, following and checkout keep their existing minimal control contracts. No real payment, customer account or live key was created.

The audit is reproducible from the ignored baseline/after captures with `scripts/audit_endpoint_outputs.py`. The public docs validator checks registry coverage, typed requests and adapter fingerprints. Regression tests cover field isolation, source counts, empty-vs-missing, gated periods, zero/negative values and coverage failures.
