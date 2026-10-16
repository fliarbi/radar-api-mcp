# Response depth audit: source data, API retrieval and documentation

The previous investor adapter called a public publication-metadata route and
never reached the database-derived profile. Separately, the docs renderer reduced
professional profiles to seven identity fields. Both were implementation gaps.
A successful HTTP response and correct checksum alone did not detect them.

The investor adapter now reads the verified Atlas business snapshot after the live
publication gate; separate fields expose portfolio rows, sectors, stages, activity,
cohorts, co-investors, research and news. Professional examples now retain skills,
education, experience, founder/investor attributes, scores and access indicators.
Short financial/funding headlines are retained instead of categorically removed.

## What the audit checks

Every primary capture is inventoried below. The machine-readable report lists all
returned top-level keys, nested array lengths, scalar counts, exact request and
omitted paths. Counts measure the example's shape, not source completeness or
accuracy. Request limits explain intentionally small result pages. The renderer
must retain every business field and every returned array row. Only named source
prose, sensitive demographics and embedded discovery schemas may be omitted.
Local checks compare rendered records to original gateway responses; CI checks
fingerprints, expected rich fields and the checked-in inventory.

## Where source depth enters the API

| Data | Source path inspected | Retrieval boundary |
|---|---|---|
| Company identity and native fields | Mongo grouped profile and enrichment records | Compact identity; one fixed-projection field per POST; 54 captures |
| Investor portfolios and research | Published Atlas data built from ClickHouse equity records and reviewed news | Verified release hash and live publication gate; 19 fields across two page types; bounded portfolio/shortlist pages |
| People | Radar people-search response | Preserve all returned non-contact professional attributes in the docs |
| Financial statements and intelligence | Radar company intelligence and earnings | Preserve fiscal periods, metrics, currency, provenance and source-plan limits |
| Funding and events | Radar funding summary and event handlers | Preserve returned rounds, associations and headlines; event window can be empty or gated |
| Company enrichment | Radar enrichment response | Preserve all supplied digital, hiring, innovation, legal and reputation sections; unknown source failures stay documented |
| Company/investor search and competitors | Radar company search and segment handlers | Bounded cards with source restrictions; cards are not the detailed profile |
| General/business/funding news | Actual News applications and live archive queries | Isolated integration identity explicitly labeled; no production-connection claim |
| Individual apps | ClickHouse app profiles, growth, velocity and install history | Compact app profile plus seven selected fields; exact developer-host company association; no developer contacts |
| Dedicated internships | Mongo internship records selected by posting type | Skill/stipend/date filters, exact-name employer groups, description detail and explicit vacancy-status uncertainty |
| Company potential | Radar company filters plus measured display columns | Six transparent growth/investment and B2B prospecting screens; preserve source restrictions and partial evidence |
| Jobs and salary | Radar job handlers | Preserve structured listing fields, salary distributions, sample sizes and paging; long job prose is omitted only from docs |
| Contact retrieval | Existing Radar paid contact handlers | Separate explicit scope and linked source account; primary captures show real default-key denials |

## Primary examples

| Operation | HTTP | Scalar values | Arrays | Prose/schema omissions |
|---|---:|---:|---:|---:|
| [search_companies](reference/search_companies.md) | 200 | 71 | 8 | 0 |
| [semantic_company_search](reference/semantic_company_search.md) | 200 | 47 | 8 | 0 |
| [get_company](reference/get_company.md) | 200 | 54 | 2 | 0 |
| [get_company_intelligence](reference/get_company_intelligence.md) | 200 | 388 | 18 | 3 |
| [get_financials](reference/get_financials.md) | 200 | 85 | 7 | 0 |
| [get_company_events](reference/get_company_events.md) | 200 | 33 | 3 | 0 |
| [get_company_funding](reference/get_company_funding.md) | 200 | 437 | 17 | 2 |
| [get_company_enrichment](reference/get_company_enrichment.md) | 200 | 241 | 10 | 1 |
| [find_competitors](reference/find_competitors.md) | 200 | 180 | 5 | 0 |
| [company_brief](reference/company_brief.md) | 200 | 224 | 14 | 6 |
| [compare_companies](reference/compare_companies.md) | 200 | 308 | 21 | 7 |
| [search_investors](reference/search_investors.md) | 200 | 135 | 13 | 0 |
| [investor_directory](reference/investor_directory.md) | 200 | 1123 | 5 | 0 |
| [get_investor_page](reference/get_investor_page.md) | 200 | 70 | 2 | 0 |
| [market_pulse](reference/market_pulse.md) | 200 | 36 | 7 | 1 |
| [location_intelligence](reference/location_intelligence.md) | 502 | 1 | 0 | 0 |
| [discover_industries](reference/discover_industries.md) | 200 | 7 | 1 | 0 |
| [search_jobs](reference/search_jobs.md) | 200 | 55 | 7 | 3 |
| [companies_hiring](reference/companies_hiring.md) | 200 | 28 | 7 | 0 |
| [get_job](reference/get_job.md) | 200 | 25 | 2 | 2 |
| [salary_benchmark](reference/salary_benchmark.md) | 200 | 13 | 0 | 0 |
| [search_people](reference/search_people.md) | 200 | 52 | 5 | 1 |
| [search_news](reference/search_news.md) | 200 | 22 | 4 | 1 |
| [search_business_news](reference/search_business_news.md) | 200 | 95 | 21 | 5 |
| [news_overview](reference/news_overview.md) | 200 | 16 | 1 | 0 |
| [news_trends](reference/news_trends.md) | 200 | 41 | 1 | 0 |
| [news_sentiment](reference/news_sentiment.md) | 200 | 149 | 3 | 0 |
| [search_business_events](reference/search_business_events.md) | 200 | 42 | 1 | 4 |
| [search_funding_news](reference/search_funding_news.md) | 200 | 146 | 11 | 5 |
| [get_article](reference/get_article.md) | 200 | 21 | 4 | 3 |
| [get_company_field](reference/get_company_field.md) | 200 | 158 | 3 | 0 |
| [company_filter_catalog](reference/company_filter_catalog.md) | 200 | 873 | 62 | 0 |
| [company_filter_options](reference/company_filter_options.md) | 200 | 10 | 1 | 0 |
| [get_company_columns](reference/get_company_columns.md) | 200 | 20 | 1 | 0 |
| [people_filter_options](reference/people_filter_options.md) | 200 | 6 | 1 | 0 |
| [get_company_contacts](reference/get_company_contacts.md) | 403 | 1 | 0 | 0 |
| [get_person_contacts](reference/get_person_contacts.md) | 403 | 1 | 0 | 0 |
| [get_investor_field](reference/get_investor_field.md) | 200 | 148 | 6 | 0 |
| [company_apps](reference/company_apps.md) | 200 | 60 | 1 | 4 |
| [opportunity_presets](reference/opportunity_presets.md) | 200 | 53 | 15 | 0 |
| [search_opportunities](reference/search_opportunities.md) | 200 | 92 | 11 | 0 |
| [job_filter_catalog](reference/job_filter_catalog.md) | 200 | 111 | 15 | 0 |
| [job_filter_options](reference/job_filter_options.md) | 200 | 8 | 1 | 0 |
| [search_internships](reference/search_internships.md) | 200 | 106 | 7 | 3 |
| [companies_offering_internships](reference/companies_offering_internships.md) | 200 | 32 | 7 | 0 |
| [get_internship](reference/get_internship.md) | 200 | 34 | 2 | 1 |
| [search_apps](reference/search_apps.md) | 200 | 47 | 1 | 3 |
| [get_app](reference/get_app.md) | 200 | 32 | 2 | 1 |
| [get_app_field](reference/get_app_field.md) | 200 | 20 | 0 | 0 |
| [app_filter_options](reference/app_filter_options.md) | 200 | 3 | 1 | 0 |
| [screen_company_financials](reference/screen_company_financials.md) | 200 | 418 | 42 | 0 |
| [financial_filter_catalog](reference/financial_filter_catalog.md) | 200 | 428 | 28 | 0 |
| [get_company_team](reference/get_company_team.md) | 200 | 153 | 13 | 3 |
| [health](reference/health.md) | 200 | 1 | 0 | 0 |
| [account_session](reference/account_session.md) | 200 | 1 | 0 | 0 |
| [account_plans](reference/account_plans.md) | 200 | 33 | 1 | 0 |
| [account_create_key](reference/account_create_key.md) | 200 | 5 | 0 | 0 |
| [capabilities](reference/capabilities.md) | 200 | 377 | 1 | 53 |
| [openapi](reference/openapi.md) | 200 | 1 | 0 | 66 |
| [account_list_keys](reference/account_list_keys.md) | 200 | 7 | 1 | 0 |
| [account_link_news](reference/account_link_news.md) | 200 | 1 | 0 | 0 |
| [account_follow](reference/account_follow.md) | 200 | 2 | 0 | 0 |
| [account_list_following](reference/account_list_following.md) | 200 | 4 | 1 | 0 |
| [account_spending](reference/account_spending.md) | 200 | 1 | 0 | 0 |
| [account_topup](reference/account_topup.md) | 200 | 6 | 0 | 0 |
| [billing_webhook](reference/billing_webhook.md) | 200 | 1 | 0 | 0 |
| [account_usage](reference/account_usage.md) | 200 | 7 | 1 | 0 |
| [account_unfollow](reference/account_unfollow.md) | 200 | 1 | 0 | 0 |
| [account_revoke_key](reference/account_revoke_key.md) | 200 | 1 | 0 | 0 |

## Remaining limits are not described as complete data

The location-intelligence source still fails. Microsoft's captured recent event
window is empty and source-plan limited. Paid contact success has not been
verified with a live entitled account. Investor search still includes a source
identity ambiguity; it searches investor-classified companies, not every angel.
The investor dataset is a dated reviewed release, not a real-time feed; directory
shortlists are selected subsets. API schemas and rich captures do not establish
that every company or investor has every field.

See [all investor field captures](INVESTOR_DATA_DEPTH.md), [all company fields](COMPANY_DATA_DEPTH.md),
[error and coverage audit](EXAMPLE_AUDIT.md) and [machine-readable depth inventory](DATA_DEPTH_AUDIT.json).
