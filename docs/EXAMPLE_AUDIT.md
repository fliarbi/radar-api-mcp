# Endpoint example audit: errors, empty results and coverage limits

This report checks every published JSON endpoint example, including HTTP 200
responses that are empty, partial, restricted or produced with test identities.
Each row links to its request, actual response and field explanations. Capture
dates below are the dates of that operation's evidence; this audit does not imply
that every endpoint was retested on the same day or that a public service exists.

The 2026-09-21 review replaced the empty job-search, hiring-company and salary
examples with narrower successful requests; job detail now uses a returned real
ID. A Payments query supplies populated competitor groups. Investor search was
recaptured successfully, and the Stripe brief now contains a successful News
section using the documented isolated News integration identity.

The compact-profile revision adds separate field retrieval, filter discovery,
selected listing columns and scoped contact lookups. The default key is correctly
denied contact access; paid contact response shapes are tested with synthetic data.

**Remaining limitations:** location intelligence still returns a real upstream
failure. Investor profiles now expose measured summaries and separate verified detail fields. The company
event example has an empty account-limited recent window. Market pulse contains
future dates and an unknown-amount sentinel. Successful investor search also
contains an ambiguous anonymous identity. These conditions remain visible; they
are not replaced with invented statistics or unrestricted records.

The [machine-readable audit](EXAMPLE_AUDIT.json) records response fingerprints;
the documentation validator rejects stale audit output. See [data quality](DATA_QUALITY.md)
and [verification](VERIFICATION.md) for source and deployment boundaries.

| Operation | HTTP | Observed data and qualifications | Capture date | Method |
|---|---:|---|---|---|
| [search_companies](reference/search_companies.md) | 200 | 2 companies | 2026-09-23 | `live_gateway` |
| [semantic_company_search](reference/semantic_company_search.md) | 200 | 1 companies | 2026-09-23 | `live_gateway` |
| [get_company](reference/get_company.md) | 200 | Profile depth: summary | 2026-09-23 | `live_gateway` |
| [get_company_intelligence](reference/get_company_intelligence.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [get_financials](reference/get_financials.md) | 200 | Financial archive access limited; Source history/result window truncated | 2026-09-23 | `live_gateway` |
| [get_company_events](reference/get_company_events.md) | 200 | 0 events; empty result; Source history/result window truncated | 2026-09-23 | `live_gateway` |
| [get_company_funding](reference/get_company_funding.md) | 200 | 10 events; Approximate reported funding | 2026-09-23 | `live_gateway` |
| [get_company_enrichment](reference/get_company_enrichment.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [find_competitors](reference/find_competitors.md) | 200 | 15 peer cards across stages | 2026-09-23 | `live_gateway` |
| [company_brief](reference/company_brief.md) | 200 | Partial response; 6/7 sections available; news: upstream_unavailable; Real data with isolated News identity/quota; no deployed News connection verified | 2026-09-23 | `live_data_integration` |
| [compare_companies](reference/compare_companies.md) | 200 | 2 companies | 2026-09-23 | `live_gateway` |
| [search_investors](reference/search_investors.md) | 200 | 5 companies; Ambiguous investor identity present; review source association | 2026-09-23 | `live_gateway` |
| [investor_directory](reference/investor_directory.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [get_investor_page](reference/get_investor_page.md) | 200 | Investor depth: summary; 10 available detail fields | 2026-09-23 | `live_gateway` |
| [market_pulse](reference/market_pulse.md) | 200 | Future-dated funding candidate; not verified recent activity; Unknown funding amount sentinel -1 | 2026-09-23 | `live_gateway` |
| [location_intelligence](reference/location_intelligence.md) | 502 | Unsuccessful: upstream_unavailable | 2026-09-23 | `live_gateway` |
| [discover_industries](reference/discover_industries.md) | 200 | 3 matches | 2026-09-23 | `live_gateway` |
| [search_jobs](reference/search_jobs.md) | 200 | 3 jobs | 2026-09-23 | `live_gateway` |
| [companies_hiring](reference/companies_hiring.md) | 200 | 3 companies; Count or aggregation capped | 2026-09-23 | `live_gateway` |
| [get_job](reference/get_job.md) | 200 | Resolved listing ID; salary can be missing | 2026-09-23 | `live_gateway` |
| [salary_benchmark](reference/salary_benchmark.md) | 200 | 206 salary observations; USD | 2026-09-23 | `live_gateway` |
| [search_people](reference/search_people.md) | 200 | 1 people | 2026-09-23 | `live_gateway` |
| [search_news](reference/search_news.md) | 200 | 1 items; Source freshness qualification applies; Real data with isolated News identity/quota; no deployed News connection verified | 2026-09-20 | `live_data_integration` |
| [search_business_news](reference/search_business_news.md) | 200 | 5 items; Source freshness qualification applies; Real data with isolated News identity/quota; no deployed News connection verified | 2026-09-20 | `live_data_integration` |
| [news_overview](reference/news_overview.md) | 200 | Source freshness qualification applies; Real data with isolated News identity/quota; no deployed News connection verified | 2026-09-20 | `live_data_integration` |
| [news_trends](reference/news_trends.md) | 200 | Source freshness qualification applies; Real data with isolated News identity/quota; no deployed News connection verified | 2026-09-20 | `live_data_integration` |
| [news_sentiment](reference/news_sentiment.md) | 200 | Source freshness qualification applies; Real data with isolated News identity/quota; no deployed News connection verified | 2026-09-20 | `live_data_integration` |
| [search_business_events](reference/search_business_events.md) | 200 | Partial response; 5 items; Source freshness qualification applies; Real data with isolated News identity/quota; no deployed News connection verified | 2026-09-23 | `live_data_integration` |
| [search_funding_news](reference/search_funding_news.md) | 200 | Partial response; 5 items; Source freshness qualification applies; Real data with isolated News identity/quota; no deployed News connection verified | 2026-09-23 | `live_data_integration` |
| [get_article](reference/get_article.md) | 200 | Source freshness qualification applies; Real data with isolated News identity/quota; no deployed News connection verified | 2026-09-20 | `live_data_integration` |
| [get_company_field](reference/get_company_field.md) | 200 | Requested field: technology; available | 2026-09-23 | `live_gateway` |
| [company_filter_catalog](reference/company_filter_catalog.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [company_filter_options](reference/company_filter_options.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [get_company_columns](reference/get_company_columns.md) | 200 | 2 companies | 2026-09-23 | `live_gateway` |
| [people_filter_options](reference/people_filter_options.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [get_company_contacts](reference/get_company_contacts.md) | 403 | Expected default-key contact denial: scope_required | 2026-09-23 | `live_gateway` |
| [get_person_contacts](reference/get_person_contacts.md) | 403 | Expected default-key contact denial: scope_required | 2026-09-23 | `live_gateway` |
| [get_investor_field](reference/get_investor_field.md) | 200 | 5 returned; 268 stored rows | 2026-09-23 | `live_gateway` |
| [company_apps](reference/company_apps.md) | 200 | 4 apps; Dated Google Play observations; not a current store check | 2026-09-23 | `live_gateway` |
| [opportunity_presets](reference/opportunity_presets.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [search_opportunities](reference/search_opportunities.md) | 200 | 2 companies; Explicit mobile_scale screen with 2 evidence rows; no predicted returns or verified purchase intent | 2026-09-23 | `live_gateway` |
| [job_filter_catalog](reference/job_filter_catalog.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [job_filter_options](reference/job_filter_options.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [search_internships](reference/search_internships.md) | 200 | 3 internships; Observed internship records; current openings are unverified and deadlines can be expired or placeholders | 2026-09-23 | `live_gateway` |
| [companies_offering_internships](reference/companies_offering_internships.md) | 200 | 3 companies; Observed internship records; current openings are unverified and deadlines can be expired or placeholders | 2026-09-23 | `live_gateway` |
| [get_internship](reference/get_internship.md) | 200 | Observed internship records; current openings are unverified and deadlines can be expired or placeholders | 2026-09-23 | `live_gateway` |
| [search_apps](reference/search_apps.md) | 200 | 3 apps; Dated Google Play observations; not a current store check | 2026-09-23 | `live_gateway` |
| [get_app](reference/get_app.md) | 200 | Dated Google Play observations; not a current store check; 15 stored history rows; source duplicates can repeat dates | 2026-09-23 | `live_gateway` |
| [get_app_field](reference/get_app_field.md) | 200 | Dated Google Play observations; not a current store check | 2026-09-23 | `live_gateway` |
| [app_filter_options](reference/app_filter_options.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [screen_company_financials](reference/screen_company_financials.md) | 200 | Partial response; 2 matches | 2026-09-23 | `live_gateway` |
| [financial_filter_catalog](reference/financial_filter_catalog.md) | 200 | Captured response; source accuracy and completeness not independently audited | 2026-09-23 | `live_gateway` |
| [get_company_team](reference/get_company_team.md) | 200 | 3 people | 2026-09-23 | `live_gateway` |
| [health](reference/health.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_session](reference/account_session.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_plans](reference/account_plans.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_create_key](reference/account_create_key.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [capabilities](reference/capabilities.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [openapi](reference/openapi.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_list_keys](reference/account_list_keys.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_link_news](reference/account_link_news.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_follow](reference/account_follow.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_list_following](reference/account_list_following.md) | 200 | 1 companies; Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_spending](reference/account_spending.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_topup](reference/account_topup.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [billing_webhook](reference/billing_webhook.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_usage](reference/account_usage.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_unfollow](reference/account_unfollow.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
| [account_revoke_key](reference/account_revoke_key.md) | 200 | Synthetic identity/payment fixture; no production activation verified | 2026-09-23 | `local_account_fixture` |
