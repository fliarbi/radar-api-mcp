# Radar API endpoint reference with captured request and response examples

Every JSON HTTP operation has a request, actual response, field explanation and
integration guidance below. The 38 data operations also show their equivalent
MCP tool call. These examples document observed output, including genuine empty,
partial and failed responses; they are not fabricated success fixtures.

## Capture provenance and limits

The 38 data-operation captures span **2026-09-20 to 2026-09-21**
through the local authenticated gateway. The original eight News captures returned
503 because their service URLs were unset. They have now been replaced by
successful requests through the actual News applications with live archive data,
using isolated test identity and quota dependencies. These are labeled
`live_data_integration`; they do not verify a deployed News URL or production key.
The current set has **35 HTTP 200 responses**. Non-success
primary examples (including expected contact-scope denials): **location_intelligence HTTP 502, get_company_contacts HTTP 403, get_person_contacts HTTP 403**. A twenty-second timeout bounded the original
HTTP upstream captures. The Stripe brief also combines live Radar sections with
a successful News section under the documented News integration identity.
The preview key had no linked Radar session, so the live source applied anonymous
free-tier access. This is neither a Business-tier coverage audit nor a public
deployment test. Some HTTP 200 responses were partial, empty or source-inconsistent.

The 16 account/discovery examples executed actual local gateway code with synthetic
identity and payment providers. They are explicitly labeled; no live purchase or
production account mutation occurred. `/healthz` reports liveness only. Static
browser routes and the MCP handshake are covered in [transports](transports.md).

Outputs now preserve **all captured array rows and business-data sections**;
the documentation no longer cuts arrays to two items or removes profile fields.
The [company depth walkthrough](../COMPANY_DATA_DEPTH.md) shows populated sectors,
feeds, founders, technology, traffic, apps, hiring, products and innovation.
Each [downloadable example](../examples/index.json) lists any remaining prose
omissions, capture provenance and checksums. News examples retain short headlines,
source URLs, dates, classifications and measured values. Article bodies, ledes,
long source quotations, review snippets and biographies are omitted from
documentation reproduction, with every omitted path recorded. Credentials are
explicitly redacted before a response is stored or hashed; checksums use parsed,
sorted JSON and do not represent HTTP wire bytes.
Read the [measured data-quality notes](../DATA_QUALITY.md) before treating the
sample corporate records as independently verified facts.
The [complete example audit](../EXAMPLE_AUDIT.md) also identifies empty, partial,
restricted and fixture-backed HTTP 200 responses.

## Data operations: REST and MCP

| Endpoint / tool reference | HTTP route | Captured status |
|---|---|---|
| [search_companies](search_companies.md) | `POST /v1/companies/search` | 200 |
| [semantic_company_search](semantic_company_search.md) | `POST /v1/companies/semantic-search` | 200 |
| [get_company](get_company.md) | `POST /v1/companies/profile` | 200 |
| [get_company_intelligence](get_company_intelligence.md) | `POST /v1/companies/intelligence` | 200 |
| [get_financials](get_financials.md) | `POST /v1/companies/financials` | 200 |
| [get_company_events](get_company_events.md) | `POST /v1/companies/events` | 200 |
| [get_company_funding](get_company_funding.md) | `POST /v1/companies/funding` | 200 |
| [get_company_enrichment](get_company_enrichment.md) | `POST /v1/companies/enrichment` | 200 |
| [find_competitors](find_competitors.md) | `POST /v1/companies/competitors` | 200 |
| [company_brief](company_brief.md) | `POST /v1/companies/brief` | 200 |
| [compare_companies](compare_companies.md) | `POST /v1/companies/compare` | 200 |
| [search_investors](search_investors.md) | `POST /v1/investors/search` | 200 |
| [investor_directory](investor_directory.md) | `POST /v1/investors/directory` | 200 |
| [get_investor_page](get_investor_page.md) | `POST /v1/investors/page` | 200 |
| [market_pulse](market_pulse.md) | `POST /v1/markets/pulse` | 200 |
| [location_intelligence](location_intelligence.md) | `POST /v1/locations/intelligence` | 502 |
| [discover_industries](discover_industries.md) | `POST /v1/industries/discover` | 200 |
| [search_jobs](search_jobs.md) | `POST /v1/jobs/search` | 200 |
| [companies_hiring](companies_hiring.md) | `POST /v1/jobs/companies` | 200 |
| [get_job](get_job.md) | `POST /v1/jobs/detail` | 200 |
| [salary_benchmark](salary_benchmark.md) | `POST /v1/jobs/salary-benchmark` | 200 |
| [search_people](search_people.md) | `POST /v1/people/search` | 200 |
| [search_news](search_news.md) | `POST /v1/news/search` | 200 |
| [search_business_news](search_business_news.md) | `POST /v1/news/business` | 200 |
| [news_overview](news_overview.md) | `POST /v1/news/overview` | 200 |
| [news_trends](news_trends.md) | `POST /v1/news/trends` | 200 |
| [news_sentiment](news_sentiment.md) | `POST /v1/news/sentiment` | 200 |
| [search_business_events](search_business_events.md) | `POST /v1/news/events` | 200 |
| [search_funding_news](search_funding_news.md) | `POST /v1/news/funding` | 200 |
| [get_article](get_article.md) | `POST /v1/news/article` | 200 |
| [get_company_field](get_company_field.md) | `POST /v1/companies/field` | 200 |
| [company_filter_catalog](company_filter_catalog.md) | `POST /v1/companies/filters` | 200 |
| [company_filter_options](company_filter_options.md) | `POST /v1/companies/filter-options` | 200 |
| [get_company_columns](get_company_columns.md) | `POST /v1/companies/columns` | 200 |
| [people_filter_options](people_filter_options.md) | `POST /v1/people/filter-options` | 200 |
| [get_company_contacts](get_company_contacts.md) | `POST /v1/contacts/company` | 403 |
| [get_person_contacts](get_person_contacts.md) | `POST /v1/contacts/person` | 403 |
| [get_investor_field](get_investor_field.md) | `POST /v1/investors/field` | 200 |

## Accounts, billing and discovery

| Endpoint reference | HTTP route | Local status |
|---|---|---|
| [Health endpoint: process liveness](health.md) | `GET /healthz` | 200 |
| [Reconnect a Radar account session](account_session.md) | `POST /account/session` | 200 |
| [Read Radar plans and API credit policy](account_plans.md) | `GET /account/plans` | 200 |
| [Create an API key: scopes, expiry and one-time reveal](account_create_key.md) | `POST /account/keys` | 200 |
| [Capability discovery: tools, routes and input schemas](capabilities.md) | `GET /v1/capabilities` | 200 |
| [OpenAPI schema endpoint: REST and account contracts](openapi.md) | `GET /v1/openapi.json` | 200 |
| [List API keys: names, expiry and revocation state](account_list_keys.md) | `GET /account/keys` | 200 |
| [Link a News API key to the Radar account](account_link_news.md) | `PUT /account/news-key` | 200 |
| [Follow a company in the API watchlist](account_follow.md) | `PUT /account/following` | 200 |
| [List followed companies and the plan limit](account_list_following.md) | `GET /account/following` | 200 |
| [Set a monthly prepaid credit spending limit](account_spending.md) | `PUT /account/spending` | 200 |
| [Create a prepaid API credit checkout order](account_topup.md) | `POST /account/topups` | 200 |
| [Payment webhook: verify captured payments and credit once](billing_webhook.md) | `POST /billing/webhook` | 200 |
| [Read API usage, prepaid balance and monthly limits](account_usage.md) | `GET /account/usage` | 200 |
| [Remove a company from the API watchlist](account_unfollow.md) | `DELETE /account/following/microsoft.com` | 200 |
| [Revoke an API key owned by the current account](account_revoke_key.md) | `DELETE /account/keys/1d33c1c6992695c69806aa1d` | 200 |

Return to [developer documentation](../README.md) or [workflow guides](../README.md#company-discovery-and-business-data).
