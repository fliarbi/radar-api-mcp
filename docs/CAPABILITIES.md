# Capability reference

All data operations are authenticated JSON POST requests. MCP uses the same tool
name and a single `request` object containing the REST body. The input schema is
available from `/v1/capabilities` and [openapi.json](openapi.json).

The [endpoint reference with captured output](reference/README.md) includes
parameter tables, actual JSON responses, REST/MCP calls and field explanations
for every operation. Read the [data-quality observations](DATA_QUALITY.md) alongside
the examples; a successful request does not establish complete or accurate coverage.

This is retrieval coverage, not parity with every Radar account-management or
application action. Existing upstream plan gates remain authoritative. Financial
archive depth depends on the linked Radar session; associated news requires the
connected News services and a linked News key. Derived scores are labelled as
assessments, with financial evidence available separately.

| MCP tool | REST path | Purpose |
|---|---|---|
| [search_companies](reference/search_companies.md) | `/v1/companies/search` | Filter companies by industry, market, location, size, stage, technology, funding and financial bands. |
| [semantic_company_search](reference/semantic_company_search.md) | `/v1/companies/semantic-search` | Find companies using a natural-language description plus optional filters. |
| [get_company](reference/get_company.md) | `/v1/companies/profile` | Read compact company identity and available fields. Retrieve field data separately with get_company_field. |
| [get_company_field](reference/get_company_field.md) | `/v1/companies/field` | Retrieve one explicitly selected company field, such as classification, people, technology, traffic or apps, with coverage and bounded arrays. |
| [company_filter_catalog](reference/company_filter_catalog.md) | `/v1/companies/filters` | Discover company filters, accepted values, sort options, pagination and selectable result columns. |
| [company_filter_options](reference/company_filter_options.md) | `/v1/companies/filter-options` | Look up matching company filter values using Radar's sidebar vocabulary and typeahead services. |
| [get_company_columns](reference/get_company_columns.md) | `/v1/companies/columns` | Fetch only selected display columns for up to twenty company domains. Formatted values are not financial statements. |
| [get_company_intelligence](reference/get_company_intelligence.md) | `/v1/companies/intelligence` | Read company scores, peer comparisons, earnings and risk narratives. Scores are derived assessments, not financial facts. |
| [get_financials](reference/get_financials.md) | `/v1/companies/financials` | Retrieve income, balance-sheet and cash-flow metrics by fiscal period; distinguish filings from news reports and preserve currency and access limits. |
| [get_company_events](reference/get_company_events.md) | `/v1/companies/events` | Read a company's event timeline, momentum, risks and the effective account-limited date window. |
| [get_company_funding](reference/get_company_funding.md) | `/v1/companies/funding` | Read reported funding rounds and investors; retain approximate-amount flags. |
| [get_company_enrichment](reference/get_company_enrichment.md) | `/v1/companies/enrichment` | Read legal identity, hiring, reputation, digital presence, innovation and social activity when available. |
| [find_competitors](reference/find_competitors.md) | `/v1/companies/competitors` | Find competitors in a named market, grouped by funding stage. |
| [company_brief](reference/company_brief.md) | `/v1/companies/brief` | Return compact summaries of profile, financials, intelligence, events, funding, enrichment and news with separate detail requests and explicit coverage. |
| [compare_companies](reference/compare_companies.md) | `/v1/companies/compare` | Compare two to five companies with separately labelled fiscal periods and partial-coverage flags. |
| [search_investors](reference/search_investors.md) | `/v1/investors/search` | Find investors by headquarters and portfolio industries or markets. |
| [investor_directory](reference/investor_directory.md) | `/v1/investors/directory` | List published investor pages, sectors and cities. |
| [get_investor_page](reference/get_investor_page.md) | `/v1/investors/page` | Retrieve a published investor profile or investor list by the slug from investor_directory. |
| [market_pulse](reference/market_pulse.md) | `/v1/markets/pulse` | Read recent funding, trending markets, sectors and investors for a bounded window. |
| [location_intelligence](reference/location_intelligence.md) | `/v1/locations/intelligence` | Retrieve Radar's existing business intelligence for a named location. |
| [discover_industries](reference/discover_industries.md) | `/v1/industries/discover` | Find up to five matching industry or market names using a specific query. |
| [search_jobs](reference/search_jobs.md) | `/v1/jobs/search` | Find job listings by company, skills, role, geography and freshness. |
| [companies_hiring](reference/companies_hiring.md) | `/v1/jobs/companies` | Find hiring companies for the same job filters. |
| [get_job](reference/get_job.md) | `/v1/jobs/detail` | Retrieve a job listing by an ID returned by search_jobs. |
| [salary_benchmark](reference/salary_benchmark.md) | `/v1/jobs/salary-benchmark` | Read salary statistics for a role, geography and optional currency; retain sample size and coverage. |
| [search_people](reference/search_people.md) | `/v1/people/search` | Find professional profiles by name, role, company, schools, skills, seniority and location; contact values require a separate request. |
| [people_filter_options](reference/people_filter_options.md) | `/v1/people/filter-options` | Look up canonical schools, skills and sectors accepted by people search. |
| [get_company_contacts](reference/get_company_contacts.md) | `/v1/contacts/company` | Request company emails and/or phones separately; requires explicit contacts scope and a paid linked Radar account. |
| [get_person_contacts](reference/get_person_contacts.md) | `/v1/contacts/person` | Request one person's emails and/or phones; preserve whether the source is the person or a company-domain fallback. Requires contacts scope and paid Radar access. |
| [search_news](reference/search_news.md) | `/v1/news/search` | Search associated news; a company filter uses business-news coverage. Headlines default to 100 per page. |
| [search_business_news](reference/search_business_news.md) | `/v1/news/business` | Search business headlines for a topic or company with date, sentiment and priority filters. |
| [news_overview](reference/news_overview.md) | `/v1/news/overview` | Read measured coverage, headline examples and topic context in a bounded date window. |
| [news_trends](reference/news_trends.md) | `/v1/news/trends` | Measure daily, weekly or monthly news volume while preserving the available date window. |
| [news_sentiment](reference/news_sentiment.md) | `/v1/news/sentiment` | Read the distribution and timeline of news sentiment. |
| [search_business_events](reference/search_business_events.md) | `/v1/news/events` | Read structured business events associated with a topic or company and their article references. |
| [search_funding_news](reference/search_funding_news.md) | `/v1/news/funding` | Find funding coverage by company, topic, investor, sector, round and reported USD amount. |
| [get_article](reference/get_article.md) | `/v1/news/article` | Retrieve the full article and attribution for an article ID returned by news or company events. |

The retrieval tool list deliberately does not expose login, payment changes,
CRM delivery, saved-search writes, application submissions, resume uploads,
report-generation jobs, arbitrary queries or arbitrary upstream routes. Financial
statement coverage is limited to the metrics Radar supplies; a missing metric is
not backfilled or fabricated. The existing market-analysis report application and
conversational agent are separate workflows, not generic pass-through tools here.

Optional account mode adds HTTP-only key management, usage, spending limits,
API watchlists and prepaid checkout. See [account operations](ACCOUNTS.md),
[API-key onboarding](guides/api-keys-authentication.md), and the
[account-mode schema](account-openapi.json). Contact retrieval is explicit, scoped and plan-gated. The MCP tool list remains read-only.
