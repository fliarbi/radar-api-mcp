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
| [get_financials](reference/get_financials.md) | 200 | Financial archive access limited | 2026-09-24 | `live_gateway` |
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

## All saved response captures

Checked **234** captures across every example folder. **20 empty**; **3 expected_denial**; **207 populated**; **4 unavailable**.

A financial example needs a numeric metric in the requested statement family. A period label, archive count or company summary alone does not qualify. Zero and negative values do qualify as data. Empty matches are retained as coverage cases, never advertised as positive results. Synthetic contact/account examples retain their fixture labels. See [sample replacements and source failures](EXAMPLE_REPAIRS.md).

| Capture | Requested output | Content | Detail | Evidence date | Method |
|---|---|---|---|---|---|
| [examples/account_create_key.json](examples/account_create_key.json) | `account_create_key` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_follow.json](examples/account_follow.json) | `account_follow` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_link_news.json](examples/account_link_news.json) | `account_link_news` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_list_following.json](examples/account_list_following.json) | `account_list_following` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_list_keys.json](examples/account_list_keys.json) | `account_list_keys` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_plans.json](examples/account_plans.json) | `account_plans` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_revoke_key.json](examples/account_revoke_key.json) | `account_revoke_key` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_session.json](examples/account_session.json) | `account_session` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_spending.json](examples/account_spending.json) | `account_spending` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_topup.json](examples/account_topup.json) | `account_topup` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_unfollow.json](examples/account_unfollow.json) | `account_unfollow` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/account_usage.json](examples/account_usage.json) | `account_usage` | populated | Response content present; empty arrays: features | 2026-09-23 | `local_account_fixture` |
| [examples/additional/mastech-annual-income.json](examples/additional/mastech-annual-income.json) | `get_financials` | populated | 1 periods with numeric metrics in the requested statement family | 2026-09-24 | `live_gateway` |
| [examples/additional/yext-activity.json](examples/additional/yext-activity.json) | `get_company_field` | populated | Selected field activity contains data | 2026-09-24 | `live_gateway` |
| [examples/additional/yext-products.json](examples/additional/yext-products.json) | `get_company_field` | populated | Selected field products contains data | 2026-09-24 | `live_gateway` |
| [examples/app_filter_options.json](examples/app_filter_options.json) | `app_filter_options` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/apps/swiggy-developer.json](examples/apps/swiggy-developer.json) | `get_app_field` | populated | Selected field developer contains data | 2026-09-23 | `live_gateway` |
| [examples/apps/swiggy-growth.json](examples/apps/swiggy-growth.json) | `get_app_field` | populated | Selected field growth contains data | 2026-09-23 | `live_gateway` |
| [examples/apps/swiggy-install_history.json](examples/apps/swiggy-install_history.json) | `get_app_field` | populated | Selected field install_history contains data | 2026-09-23 | `live_gateway` |
| [examples/apps/swiggy-listing.json](examples/apps/swiggy-listing.json) | `get_app_field` | populated | Selected field listing contains data | 2026-09-23 | `live_gateway` |
| [examples/apps/swiggy-monetization.json](examples/apps/swiggy-monetization.json) | `get_app_field` | populated | Selected field monetization contains data | 2026-09-23 | `live_gateway` |
| [examples/apps/swiggy-ratings.json](examples/apps/swiggy-ratings.json) | `get_app_field` | populated | Selected field ratings contains data | 2026-09-23 | `live_gateway` |
| [examples/apps/swiggy-release.json](examples/apps/swiggy-release.json) | `get_app_field` | populated | Selected field release contains data | 2026-09-23 | `live_gateway` |
| [examples/billing_webhook.json](examples/billing_webhook.json) | `billing_webhook` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/business-models/51-investment-commission-per-deal-search.json](examples/business-models/51-investment-commission-per-deal-search.json) | `search_companies` | empty | 0 companies; totals and context do not substitute for requested rows; empty arrays: companies | 2026-09-25 | `live_gateway` |
| [examples/business-models/52-investment-advisers-success-fees-search.json](examples/business-models/52-investment-advisers-success-fees-search.json) | `semantic_company_search` | populated | Response content present; empty arrays: companies | 2026-09-25 | `live_gateway` |
| [examples/business-models/53-real-estate-brokerage-commission-search.json](examples/business-models/53-real-estate-brokerage-commission-search.json) | `search_companies` | empty | 0 companies; totals and context do not substitute for requested rows; empty arrays: companies | 2026-09-25 | `live_gateway` |
| [examples/business-models/54-insurance-broker-commission-classification.json](examples/business-models/54-insurance-broker-commission-classification.json) | `get_company_field` | populated | Selected field classification contains data | 2026-09-25 | `live_gateway` |
| [examples/business-models/54-insurance-broker-commission-profile.json](examples/business-models/54-insurance-broker-commission-profile.json) | `get_company` | populated | Response content present | 2026-09-25 | `live_gateway` |
| [examples/business-models/54-insurance-broker-commission-search.json](examples/business-models/54-insurance-broker-commission-search.json) | `search_companies` | populated | 20 companies; totals and context do not substitute for requested rows | 2026-09-25 | `live_gateway` |
| [examples/business-models/55-recruitment-placement-fees-search.json](examples/business-models/55-recruitment-placement-fees-search.json) | `search_companies` | empty | 0 companies; totals and context do not substitute for requested rows; empty arrays: companies | 2026-09-25 | `live_gateway` |
| [examples/business-models/56-marketplace-transaction-commission-search.json](examples/business-models/56-marketplace-transaction-commission-search.json) | `search_companies` | empty | 0 companies; totals and context do not substitute for requested rows; empty arrays: companies | 2026-09-25 | `live_gateway` |
| [examples/business-models/57-hybrid-subscription-and-commission-classification.json](examples/business-models/57-hybrid-subscription-and-commission-classification.json) | `get_company_field` | populated | Selected field classification contains data | 2026-09-25 | `live_gateway` |
| [examples/business-models/57-hybrid-subscription-and-commission-profile.json](examples/business-models/57-hybrid-subscription-and-commission-profile.json) | `get_company` | populated | Response content present | 2026-09-25 | `live_gateway` |
| [examples/business-models/57-hybrid-subscription-and-commission-search.json](examples/business-models/57-hybrid-subscription-and-commission-search.json) | `search_companies` | populated | 20 companies; totals and context do not substitute for requested rows | 2026-09-25 | `live_gateway` |
| [examples/business-models/58-lending-interest-vs-commission-search.json](examples/business-models/58-lending-interest-vs-commission-search.json) | `search_companies` | empty | 0 companies; totals and context do not substitute for requested rows; empty arrays: companies | 2026-09-25 | `live_gateway` |
| [examples/business-models/59-data-vendors-licensing-search.json](examples/business-models/59-data-vendors-licensing-search.json) | `search_companies` | unavailable | access_required | 2026-09-25 | `live_gateway` |
| [examples/business-models/60-software-services-business-model-search.json](examples/business-models/60-software-services-business-model-search.json) | `search_companies` | unavailable | access_required | 2026-09-25 | `live_gateway` |
| [examples/capabilities.json](examples/capabilities.json) | `capabilities` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/companies_hiring.json](examples/companies_hiring.json) | `companies_hiring` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/companies_offering_internships.json](examples/companies_offering_internships.json) | `companies_offering_internships` | populated | 3 companies; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/company_apps.json](examples/company_apps.json) | `company_apps` | populated | 4 apps; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/company_brief.json](examples/company_brief.json) | `company_brief` | populated | Response content present | 2026-09-23 | `live_data_integration` |
| [examples/company_filter_catalog.json](examples/company_filter_catalog.json) | `company_filter_catalog` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/company_filter_options.json](examples/company_filter_options.json) | `company_filter_options` | populated | 5 options; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/compare_companies.json](examples/compare_companies.json) | `compare_companies` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/contacts/company-email-only.json](examples/contacts/company-email-only.json) | `get_company_contacts` | populated | 2 values in requested contact types; fixture provenance remains separate | 2026-09-23 | `local_contact_fixture` |
| [examples/contacts/company-phone-only.json](examples/contacts/company-phone-only.json) | `get_company_contacts` | populated | 1 values in requested contact types; fixture provenance remains separate | 2026-09-23 | `local_contact_fixture` |
| [examples/contacts/founder-professional.json](examples/contacts/founder-professional.json) | `search_people` | empty | 0 people; totals and context do not substitute for requested rows; empty arrays: people | 2026-09-23 | `live_gateway` |
| [examples/contacts/founder-shashank.json](examples/contacts/founder-shashank.json) | `search_people` | populated | 1 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/contacts/founder-team.json](examples/contacts/founder-team.json) | `get_company_team` | populated | 3 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/contacts/paid-plan-denial.json](examples/contacts/paid-plan-denial.json) | `get_company_contacts` | expected_denial | access_required | 2026-09-23 | `local_contact_fixture` |
| [examples/contacts/person-company-fallback.json](examples/contacts/person-company-fallback.json) | `get_person_contacts` | populated | 1 values in requested contact types; fixture provenance remains separate | 2026-09-23 | `local_contact_fixture` |
| [examples/contacts/person-direct.json](examples/contacts/person-direct.json) | `get_person_contacts` | populated | 2 values in requested contact types; fixture provenance remains separate | 2026-09-23 | `local_contact_fixture` |
| [examples/contacts/person-no-data.json](examples/contacts/person-no-data.json) | `get_person_contacts` | empty | 0 values in requested contact types; fixture provenance remains separate; empty arrays: emails, phones | 2026-09-23 | `local_contact_fixture` |
| [examples/contacts/person-phone-only-source.json](examples/contacts/person-phone-only-source.json) | `get_person_contacts` | empty | 0 values in requested contact types; fixture provenance remains separate; empty arrays: emails | 2026-09-23 | `local_contact_fixture` |
| [examples/contacts/person-unknown-origin.json](examples/contacts/person-unknown-origin.json) | `get_person_contacts` | populated | 1 values in requested contact types; fixture provenance remains separate | 2026-09-23 | `local_contact_fixture` |
| [examples/discover_industries.json](examples/discover_industries.json) | `discover_industries` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-activity.json](examples/fields/razorpay.com-activity.json) | `get_company_field` | empty | Selected field activity has no returned value | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-apps.json](examples/fields/razorpay.com-apps.json) | `get_company_field` | populated | Selected field apps contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-assessments.json](examples/fields/razorpay.com-assessments.json) | `get_company_field` | populated | Selected field assessments contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-classification.json](examples/fields/razorpay.com-classification.json) | `get_company_field` | populated | Selected field classification contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-geography.json](examples/fields/razorpay.com-geography.json) | `get_company_field` | populated | Selected field geography contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-hiring.json](examples/fields/razorpay.com-hiring.json) | `get_company_field` | populated | Selected field hiring contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-innovation.json](examples/fields/razorpay.com-innovation.json) | `get_company_field` | empty | Selected field innovation has no returned value | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-legal.json](examples/fields/razorpay.com-legal.json) | `get_company_field` | populated | Selected field legal contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-lifecycle.json](examples/fields/razorpay.com-lifecycle.json) | `get_company_field` | populated | Selected field lifecycle contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-overview.json](examples/fields/razorpay.com-overview.json) | `get_company_field` | populated | Selected field overview contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-people.json](examples/fields/razorpay.com-people.json) | `get_company_field` | populated | Selected field people contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-products.json](examples/fields/razorpay.com-products.json) | `get_company_field` | empty | Selected field products has no returned value; empty arrays: value | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-reputation.json](examples/fields/razorpay.com-reputation.json) | `get_company_field` | populated | Selected field reputation contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-share_of_voice.json](examples/fields/razorpay.com-share_of_voice.json) | `get_company_field` | populated | Selected field share_of_voice contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-social.json](examples/fields/razorpay.com-social.json) | `get_company_field` | populated | Selected field social contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-technology.json](examples/fields/razorpay.com-technology.json) | `get_company_field` | populated | Selected field technology contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-traffic.json](examples/fields/razorpay.com-traffic.json) | `get_company_field` | populated | Selected field traffic contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/razorpay.com-web_presence.json](examples/fields/razorpay.com-web_presence.json) | `get_company_field` | populated | Selected field web_presence contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-activity.json](examples/fields/stripe.com-activity.json) | `get_company_field` | populated | Selected field activity contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-apps.json](examples/fields/stripe.com-apps.json) | `get_company_field` | populated | Selected field apps contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-assessments.json](examples/fields/stripe.com-assessments.json) | `get_company_field` | populated | Selected field assessments contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-classification.json](examples/fields/stripe.com-classification.json) | `get_company_field` | populated | Selected field classification contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-geography.json](examples/fields/stripe.com-geography.json) | `get_company_field` | populated | Selected field geography contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-hiring.json](examples/fields/stripe.com-hiring.json) | `get_company_field` | populated | Selected field hiring contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-innovation.json](examples/fields/stripe.com-innovation.json) | `get_company_field` | empty | Selected field innovation has no returned value | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-legal.json](examples/fields/stripe.com-legal.json) | `get_company_field` | populated | Selected field legal contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-lifecycle.json](examples/fields/stripe.com-lifecycle.json) | `get_company_field` | populated | Selected field lifecycle contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-overview.json](examples/fields/stripe.com-overview.json) | `get_company_field` | populated | Selected field overview contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-people.json](examples/fields/stripe.com-people.json) | `get_company_field` | populated | Selected field people contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-products.json](examples/fields/stripe.com-products.json) | `get_company_field` | populated | Selected field products contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-reputation.json](examples/fields/stripe.com-reputation.json) | `get_company_field` | populated | Selected field reputation contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-share_of_voice.json](examples/fields/stripe.com-share_of_voice.json) | `get_company_field` | populated | Selected field share_of_voice contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-social.json](examples/fields/stripe.com-social.json) | `get_company_field` | populated | Selected field social contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-technology.json](examples/fields/stripe.com-technology.json) | `get_company_field` | populated | Selected field technology contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-traffic.json](examples/fields/stripe.com-traffic.json) | `get_company_field` | populated | Selected field traffic contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/stripe.com-web_presence.json](examples/fields/stripe.com-web_presence.json) | `get_company_field` | populated | Selected field web_presence contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-activity.json](examples/fields/swiggy.com-activity.json) | `get_company_field` | populated | Selected field activity contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-apps.json](examples/fields/swiggy.com-apps.json) | `get_company_field` | populated | Selected field apps contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-assessments.json](examples/fields/swiggy.com-assessments.json) | `get_company_field` | populated | Selected field assessments contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-classification.json](examples/fields/swiggy.com-classification.json) | `get_company_field` | populated | Selected field classification contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-geography.json](examples/fields/swiggy.com-geography.json) | `get_company_field` | populated | Selected field geography contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-hiring.json](examples/fields/swiggy.com-hiring.json) | `get_company_field` | populated | Selected field hiring contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-innovation.json](examples/fields/swiggy.com-innovation.json) | `get_company_field` | empty | Selected field innovation has no returned value | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-legal.json](examples/fields/swiggy.com-legal.json) | `get_company_field` | populated | Selected field legal contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-lifecycle.json](examples/fields/swiggy.com-lifecycle.json) | `get_company_field` | populated | Selected field lifecycle contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-overview.json](examples/fields/swiggy.com-overview.json) | `get_company_field` | populated | Selected field overview contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-people.json](examples/fields/swiggy.com-people.json) | `get_company_field` | populated | Selected field people contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-products.json](examples/fields/swiggy.com-products.json) | `get_company_field` | empty | Selected field products has no returned value; empty arrays: value | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-reputation.json](examples/fields/swiggy.com-reputation.json) | `get_company_field` | populated | Selected field reputation contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-share_of_voice.json](examples/fields/swiggy.com-share_of_voice.json) | `get_company_field` | populated | Selected field share_of_voice contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-social.json](examples/fields/swiggy.com-social.json) | `get_company_field` | populated | Selected field social contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-technology.json](examples/fields/swiggy.com-technology.json) | `get_company_field` | populated | Selected field technology contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-traffic.json](examples/fields/swiggy.com-traffic.json) | `get_company_field` | populated | Selected field traffic contains data | 2026-09-23 | `live_gateway` |
| [examples/fields/swiggy.com-web_presence.json](examples/fields/swiggy.com-web_presence.json) | `get_company_field` | populated | Selected field web_presence contains data | 2026-09-23 | `live_gateway` |
| [examples/financial_filter_catalog.json](examples/financial_filter_catalog.json) | `financial_filter_catalog` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/find_competitors.json](examples/find_competitors.json) | `find_competitors` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/get_app.json](examples/get_app.json) | `get_app` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/get_app_field.json](examples/get_app_field.json) | `get_app_field` | populated | Selected field growth contains data | 2026-09-23 | `live_gateway` |
| [examples/get_article.json](examples/get_article.json) | `get_article` | populated | Response content present | 2026-09-20 | `live_data_integration` |
| [examples/get_company.json](examples/get_company.json) | `get_company` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/get_company_columns.json](examples/get_company_columns.json) | `get_company_columns` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/get_company_contacts.json](examples/get_company_contacts.json) | `get_company_contacts` | expected_denial | scope_required | 2026-09-23 | `live_gateway` |
| [examples/get_company_enrichment.json](examples/get_company_enrichment.json) | `get_company_enrichment` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/get_company_events.json](examples/get_company_events.json) | `get_company_events` | empty | 0 events; totals and context do not substitute for requested rows; empty arrays: events | 2026-09-23 | `live_gateway` |
| [examples/get_company_field.json](examples/get_company_field.json) | `get_company_field` | populated | Selected field technology contains data | 2026-09-23 | `live_gateway` |
| [examples/get_company_funding.json](examples/get_company_funding.json) | `get_company_funding` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/get_company_intelligence.json](examples/get_company_intelligence.json) | `get_company_intelligence` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/get_company_team.json](examples/get_company_team.json) | `get_company_team` | populated | 3 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/get_financials.json](examples/get_financials.json) | `get_financials` | populated | 1 periods with numeric metrics in the requested statement family | 2026-09-24 | `live_gateway` |
| [examples/get_internship.json](examples/get_internship.json) | `get_internship` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/get_investor_field.json](examples/get_investor_field.json) | `get_investor_field` | populated | Selected field portfolio contains data | 2026-09-23 | `live_gateway` |
| [examples/get_investor_page.json](examples/get_investor_page.json) | `get_investor_page` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/get_job.json](examples/get_job.json) | `get_job` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/get_person_contacts.json](examples/get_person_contacts.json) | `get_person_contacts` | expected_denial | scope_required | 2026-09-23 | `live_gateway` |
| [examples/health.json](examples/health.json) | `health` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/investor_directory.json](examples/investor_directory.json) | `investor_directory` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-activity.json](examples/investors/anupam-mittal-activity.json) | `get_investor_field` | populated | Selected field activity contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-analysis.json](examples/investors/anupam-mittal-analysis.json) | `get_investor_field` | populated | Selected field analysis contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-co_investors.json](examples/investors/anupam-mittal-co_investors.json) | `get_investor_field` | populated | Selected field co_investors contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-follow_on.json](examples/investors/anupam-mittal-follow_on.json) | `get_investor_field` | populated | Selected field follow_on contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-news.json](examples/investors/anupam-mittal-news.json) | `get_investor_field` | populated | Selected field news contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-portfolio.json](examples/investors/anupam-mittal-portfolio.json) | `get_investor_field` | populated | Selected field portfolio contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-related.json](examples/investors/anupam-mittal-related.json) | `get_investor_field` | populated | Selected field related contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-sectors.json](examples/investors/anupam-mittal-sectors.json) | `get_investor_field` | populated | Selected field sectors contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-stages.json](examples/investors/anupam-mittal-stages.json) | `get_investor_field` | populated | Selected field stages contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-summary.json](examples/investors/anupam-mittal-summary.json) | `get_investor_page` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/investors/anupam-mittal-undated_portfolio.json](examples/investors/anupam-mittal-undated_portfolio.json) | `get_investor_field` | populated | Selected field undated_portfolio contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/fintech-investors-in-bengaluru-activity.json](examples/investors/fintech-investors-in-bengaluru-activity.json) | `get_investor_field` | populated | Selected field activity contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/fintech-investors-in-bengaluru-geography.json](examples/investors/fintech-investors-in-bengaluru-geography.json) | `get_investor_field` | populated | Selected field geography contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/fintech-investors-in-bengaluru-investors.json](examples/investors/fintech-investors-in-bengaluru-investors.json) | `get_investor_field` | populated | Selected field investors contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/fintech-investors-in-bengaluru-recent_rounds.json](examples/investors/fintech-investors-in-bengaluru-recent_rounds.json) | `get_investor_field` | populated | Selected field recent_rounds contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/fintech-investors-in-bengaluru-related.json](examples/investors/fintech-investors-in-bengaluru-related.json) | `get_investor_field` | populated | Selected field related contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/fintech-investors-in-bengaluru-research.json](examples/investors/fintech-investors-in-bengaluru-research.json) | `get_investor_field` | populated | Selected field research contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/fintech-investors-in-bengaluru-selection.json](examples/investors/fintech-investors-in-bengaluru-selection.json) | `get_investor_field` | populated | Selected field selection contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/fintech-investors-in-bengaluru-stages.json](examples/investors/fintech-investors-in-bengaluru-stages.json) | `get_investor_field` | populated | Selected field stages contains data | 2026-09-23 | `live_gateway` |
| [examples/investors/fintech-investors-in-bengaluru-summary.json](examples/investors/fintech-investors-in-bengaluru-summary.json) | `get_investor_page` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/investors/fintech-investors-in-bengaluru-themes.json](examples/investors/fintech-investors-in-bengaluru-themes.json) | `get_investor_field` | populated | Selected field themes contains data | 2026-09-23 | `live_gateway` |
| [examples/job_filter_catalog.json](examples/job_filter_catalog.json) | `job_filter_catalog` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/job_filter_options.json](examples/job_filter_options.json) | `job_filter_options` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/location_intelligence.json](examples/location_intelligence.json) | `location_intelligence` | unavailable | upstream_unavailable | 2026-09-23 | `live_gateway` |
| [examples/market_pulse.json](examples/market_pulse.json) | `market_pulse` | populated | Response content present; empty arrays: trending_sectors, winning_industries | 2026-09-23 | `live_gateway` |
| [examples/news_overview.json](examples/news_overview.json) | `news_overview` | populated | Response content present | 2026-09-20 | `live_data_integration` |
| [examples/news_sentiment.json](examples/news_sentiment.json) | `news_sentiment` | populated | Response content present | 2026-09-20 | `live_data_integration` |
| [examples/news_trends.json](examples/news_trends.json) | `news_trends` | populated | Response content present | 2026-09-20 | `live_data_integration` |
| [examples/openapi.json](examples/openapi.json) | `openapi` | populated | Response content present | 2026-09-23 | `local_account_fixture` |
| [examples/opportunities/hiring_expansion.json](examples/opportunities/hiring_expansion.json) | `search_opportunities` | populated | Response content present | 2026-09-21 | `live_gateway` |
| [examples/opportunities/profitable_growth.json](examples/opportunities/profitable_growth.json) | `search_opportunities` | populated | Response content present | 2026-09-21 | `live_gateway` |
| [examples/opportunity_presets.json](examples/opportunity_presets.json) | `opportunity_presets` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/people_filter_options.json](examples/people_filter_options.json) | `people_filter_options` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/profiles/razorpay.com.json](examples/profiles/razorpay.com.json) | `get_company` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/profiles/stripe.com.json](examples/profiles/stripe.com.json) | `get_company` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/profiles/swiggy.com.json](examples/profiles/swiggy.com.json) | `get_company` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/salary_benchmark.json](examples/salary_benchmark.json) | `salary_benchmark` | populated | 206 salary observations | 2026-09-23 | `live_gateway` |
| [examples/scenarios/01-adtech-vocabulary.json](examples/scenarios/01-adtech-vocabulary.json) | `company_filter_options` | populated | 1 options; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/02-usa-vocabulary.json](examples/scenarios/02-usa-vocabulary.json) | `company_filter_options` | populated | 5 options; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/03-usa-adtech-under-10k.json](examples/scenarios/03-usa-adtech-under-10k.json) | `screen_company_financials` | empty | 0 matches; totals and context do not substitute for requested rows; empty arrays: matches | 2026-09-23 | `live_gateway` |
| [examples/scenarios/04-usa-adtech-over-1m.json](examples/scenarios/04-usa-adtech-over-1m.json) | `screen_company_financials` | populated | 2 matches; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/05-india-profitable.json](examples/scenarios/05-india-profitable.json) | `search_companies` | populated | 2 companies; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/06-under-1m-band.json](examples/scenarios/06-under-1m-band.json) | `search_companies` | populated | 3 companies; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/07-10m-100m-band.json](examples/scenarios/07-10m-100m-band.json) | `search_companies` | populated | 3 companies; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/08-high-growth.json](examples/scenarios/08-high-growth.json) | `search_companies` | populated | 3 companies; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/09-loss-making.json](examples/scenarios/09-loss-making.json) | `search_companies` | populated | 3 companies; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/10-startup-age.json](examples/scenarios/10-startup-age.json) | `search_companies` | populated | 3 companies; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/11-seed-small-round.json](examples/scenarios/11-seed-small-round.json) | `search_companies` | empty | 0 companies; totals and context do not substitute for requested rows; empty arrays: companies | 2026-09-23 | `live_gateway` |
| [examples/scenarios/12-subscription-model.json](examples/scenarios/12-subscription-model.json) | `search_companies` | populated | 3 companies; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/13-balance-sheet.json](examples/scenarios/13-balance-sheet.json) | `get_financials` | empty | 0 periods with numeric metrics in the requested statement family | 2026-09-24 | `live_gateway` |
| [examples/scenarios/14-annual-income.json](examples/scenarios/14-annual-income.json) | `get_financials` | populated | 1 periods with numeric metrics in the requested statement family | 2026-09-24 | `live_gateway` |
| [examples/scenarios/15-annual-cash-flow.json](examples/scenarios/15-annual-cash-flow.json) | `get_financials` | empty | 0 periods with numeric metrics in the requested statement family | 2026-09-24 | `live_gateway` |
| [examples/scenarios/16-quarterly-income.json](examples/scenarios/16-quarterly-income.json) | `get_financials` | populated | 2 periods with numeric metrics in the requested statement family | 2026-09-24 | `live_gateway` |
| [examples/scenarios/17-funding-rounds.json](examples/scenarios/17-funding-rounds.json) | `get_company_funding` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/scenarios/18-finance-columns.json](examples/scenarios/18-finance-columns.json) | `get_company_columns` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/scenarios/19-precise-profit-screen.json](examples/scenarios/19-precise-profit-screen.json) | `screen_company_financials` | populated | 1 matches; totals and context do not substitute for requested rows | 2026-09-24 | `live_gateway` |
| [examples/scenarios/20-financial-filter-definitions.json](examples/scenarios/20-financial-filter-definitions.json) | `financial_filter_catalog` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/scenarios/21-razorpay-founders.json](examples/scenarios/21-razorpay-founders.json) | `get_company_team` | populated | 2 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/22-stripe-leadership.json](examples/scenarios/22-stripe-leadership.json) | `get_company_team` | populated | 4 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/23-swiggy-leadership.json](examples/scenarios/23-swiggy-leadership.json) | `get_company_team` | populated | 3 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/24-microsoft-team.json](examples/scenarios/24-microsoft-team.json) | `get_company_team` | populated | 3 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/25-stripe-executives.json](examples/scenarios/25-stripe-executives.json) | `get_company_team` | populated | 3 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/26-razorpay-chief.json](examples/scenarios/26-razorpay-chief.json) | `get_company_team` | populated | 1 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/27-founder-education.json](examples/scenarios/27-founder-education.json) | `search_people` | populated | 3 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/28-professional-skills.json](examples/scenarios/28-professional-skills.json) | `search_people` | populated | 3 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/29-professional-experience.json](examples/scenarios/29-professional-experience.json) | `search_people` | populated | 3 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/30-india-senior-executives.json](examples/scenarios/30-india-senior-executives.json) | `search_people` | populated | 3 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/31-company-apps.json](examples/scenarios/31-company-apps.json) | `company_apps` | populated | 4 apps; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/32-food-apps.json](examples/scenarios/32-food-apps.json) | `search_apps` | populated | 3 apps; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/33-app-growth.json](examples/scenarios/33-app-growth.json) | `get_app_field` | populated | Selected field growth contains data | 2026-09-23 | `live_gateway` |
| [examples/scenarios/34-app-history-page.json](examples/scenarios/34-app-history-page.json) | `get_app_field` | populated | Selected field install_history contains data | 2026-09-23 | `live_gateway` |
| [examples/scenarios/35-app-monetization.json](examples/scenarios/35-app-monetization.json) | `get_app_field` | populated | Selected field monetization contains data | 2026-09-23 | `live_gateway` |
| [examples/scenarios/36-app-ratings.json](examples/scenarios/36-app-ratings.json) | `get_app_field` | populated | Selected field ratings contains data | 2026-09-23 | `live_gateway` |
| [examples/scenarios/37-us-software-jobs.json](examples/scenarios/37-us-software-jobs.json) | `search_jobs` | populated | 3 jobs; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/38-normalized-interns.json](examples/scenarios/38-normalized-interns.json) | `search_jobs` | empty | 0 jobs; totals and context do not substitute for requested rows; empty arrays: jobs | 2026-09-23 | `live_gateway` |
| [examples/scenarios/39-company-skill-jobs.json](examples/scenarios/39-company-skill-jobs.json) | `search_jobs` | populated | 2 jobs; totals and context do not substitute for requested rows | 2026-09-24 | `live_gateway` |
| [examples/scenarios/40-salary-benchmark.json](examples/scenarios/40-salary-benchmark.json) | `salary_benchmark` | populated | 206 salary observations | 2026-09-23 | `live_gateway` |
| [examples/scenarios/41-remote-part-time-interns.json](examples/scenarios/41-remote-part-time-interns.json) | `search_internships` | populated | 3 internships; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/42-internship-employers.json](examples/scenarios/42-internship-employers.json) | `companies_offering_internships` | populated | 3 companies; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/43-internship-stipend.json](examples/scenarios/43-internship-stipend.json) | `search_internships` | populated | 3 internships; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/scenarios/44-investor-fintech.json](examples/scenarios/44-investor-fintech.json) | `get_investor_field` | populated | Selected field portfolio contains data | 2026-09-23 | `live_gateway` |
| [examples/scenarios/45-investor-co-backers.json](examples/scenarios/45-investor-co-backers.json) | `get_investor_field` | populated | Selected field co_investors contains data | 2026-09-23 | `live_gateway` |
| [examples/scenarios/46-investor-directory.json](examples/scenarios/46-investor-directory.json) | `get_investor_field` | populated | Selected field investors contains data | 2026-09-23 | `live_gateway` |
| [examples/scenarios/47-company-taxonomy.json](examples/scenarios/47-company-taxonomy.json) | `get_company_field` | populated | Selected field classification contains data | 2026-09-23 | `live_gateway` |
| [examples/scenarios/48-company-technologies.json](examples/scenarios/48-company-technologies.json) | `get_company_field` | populated | Selected field technology contains data | 2026-09-23 | `live_gateway` |
| [examples/scenarios/49-company-traffic.json](examples/scenarios/49-company-traffic.json) | `get_company_field` | populated | Selected field traffic contains data | 2026-09-23 | `live_gateway` |
| [examples/scenarios/50-company-news.json](examples/scenarios/50-company-news.json) | `search_business_news` | unavailable | upstream_unavailable | 2026-09-23 | `live_data_integration` |
| [examples/screen_company_financials.json](examples/screen_company_financials.json) | `screen_company_financials` | populated | 2 matches; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/search_apps.json](examples/search_apps.json) | `search_apps` | populated | 3 apps; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/search_business_events.json](examples/search_business_events.json) | `search_business_events` | populated | 5 items; totals and context do not substitute for requested rows | 2026-09-23 | `live_data_integration` |
| [examples/search_business_news.json](examples/search_business_news.json) | `search_business_news` | populated | 5 items; totals and context do not substitute for requested rows | 2026-09-20 | `live_data_integration` |
| [examples/search_companies.json](examples/search_companies.json) | `search_companies` | populated | 2 companies; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/search_funding_news.json](examples/search_funding_news.json) | `search_funding_news` | populated | Response content present | 2026-09-23 | `live_data_integration` |
| [examples/search_internships.json](examples/search_internships.json) | `search_internships` | populated | 3 internships; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/search_investors.json](examples/search_investors.json) | `search_investors` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/search_jobs.json](examples/search_jobs.json) | `search_jobs` | populated | 3 jobs; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/search_news.json](examples/search_news.json) | `search_news` | populated | 1 items; totals and context do not substitute for requested rows | 2026-09-20 | `live_data_integration` |
| [examples/search_opportunities.json](examples/search_opportunities.json) | `search_opportunities` | populated | Response content present | 2026-09-23 | `live_gateway` |
| [examples/search_people.json](examples/search_people.json) | `search_people` | populated | 1 people; totals and context do not substitute for requested rows | 2026-09-23 | `live_gateway` |
| [examples/semantic_company_search.json](examples/semantic_company_search.json) | `semantic_company_search` | populated | Response content present | 2026-09-23 | `live_gateway` |
