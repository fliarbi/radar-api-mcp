# Connector directory submission kit

Everything a directory reviewer asks for, in one place. The hosted server is live; nothing here
needs a local install.

## Listing

| Field | Value |
|---|---|
| Name | Companies Radar |
| Publisher | Fliar Business Intelligence (Fliar BI) |
| MCP server URL | `https://radar-api.fliarbi.com/mcp` (Streamable HTTP) |
| Authentication | OAuth 2.1 with dynamic client registration and PKCE; discovery from the server URL (RFC 9728). API-key header for developer clients |
| Short description | Company profiles, financials, funding, founders, competitors and business news. Free to start. |
| Long description | Companies Radar answers company research questions with sourced data: search companies by industry, location, size, stage and technology; read profiles, financial statements by fiscal period, funding rounds and investors, founders and key people, competitors, hiring and apps; and follow business and funding news. Every figure keeps its period, currency and source type, and missing data is reported as missing rather than zero. All tools are read-only. |
| Category | Business intelligence, research, finance |
| Website | https://radar-api.fliarbi.com/ |
| Documentation | https://github.com/fliarbi/radar-api-mcp |
| API reference | https://radar-api.fliarbi.com/docs |
| Privacy policy | https://fliarbi.com/privacy |
| Terms | https://fliarbi.com/terms |
| Support | https://github.com/fliarbi/radar-api-mcp/issues |
| Price | Free: 100 lookups a month (25 a day). Then pay as you go from US$5, or the Business plan |
| Registry file | [`server.json`](../server.json) (official MCP registry format) |

## Reviewer access

Reviewers sign in on the consent page with a Companies Radar account. Any new account works
on the free allowance. Give reviewers a dedicated account instead of asking them to register:
create it in the dashboard, verify its email, and put its email and password in the submission
form's test-credentials field (never in this repository).

## Test prompts

1. “Compare Zomato and Swiggy: revenue and profit by fiscal year, with the source of each figure.” (`get_financials`, `compare_companies`)
2. “Find fintech companies in Bengaluru and list their founders.” (`search_companies`, `get_company_team`)
3. “Who competes with Razorpay and what has each raised?” (`find_competitors`, `get_company_funding`)
4. “What funding news came out for AI startups this month?” (`search_funding_news`)
5. “Give me a one-page brief on Freshworks.” (`company_brief`)

Prompts that should **not** call the connector (the ChatGPT form asks for three):

1. “Write a haiku about autumn.” (no company data needed)
2. “What is 18% of 2,450?” (plain arithmetic)
3. “Email the founders of Razorpay and ask for a meeting.” (the connector is read-only and sends nothing)

Expected behaviour: answers cite periods and source types; a company with no data returns a
clear “no data” result; when the free allowance is used the tool returns an error that names
the top-up page.

## Data handling

- Read-only: no tool creates, changes, sends or deletes anything.
- The server receives the tool arguments (company names, domains, filters, search text). It does
  not receive the conversation.
- Contact details (emails, phones) are not available on the free allowance; they need an
  explicit scope and a paid plan.
- Returned text is third-party data and is labelled as data, not instructions, in the server
  instructions.
- A connector is one revocable key on the user's account; revoking it ends access immediately.

## Tool annotations and justification

All 53 tools carry a title and the same annotations, for the same reason:

| Annotation | Value | Why |
|---|---|---|
| `readOnlyHint` | `true` | Every tool only retrieves stored records; none writes to any system |
| `destructiveHint` | `false` | Nothing is modified or deleted |
| `idempotentHint` | `true` | Repeating a call with the same arguments returns the same kind of result and changes nothing |
| `openWorldHint` | `true` | Results describe real companies, people and news gathered from outside sources |

Chat connectors list the tools marked **core**; the rest are listed for API keys and remain callable.

| Tool | Title | Listed for | What it does |
|---|---|---|---|
| `search_companies` | Search companies | core | Filter companies by industry, market, location, size, stage, technology, funding and financial bands. |
| `semantic_company_search` | Semantic company search | core | Find companies using a natural-language description plus optional filters. |
| `get_company` | Get company | core | Read compact company identity and available fields. Retrieve field data separately with get_company_field. |
| `get_company_field` | Get company field | core | Retrieve one explicitly selected company field, such as classification, people, technology, traffic or apps, with coverage and bounded arrays. |
| `company_apps` | Company apps | API keys | List individual Play Store apps whose normalized developer website exactly matches the company domain. |
| `opportunity_presets` | Opportunity presets | API keys | Discover explainable growth, hiring, financial and technology prospecting screens and their limits. |
| `search_opportunities` | Search opportunities | API keys | Find companies using an explicit opportunity preset plus additional filters; return measured display evidence and source restrictions. |
| `company_filter_catalog` | Company filter catalog | API keys | Discover company filters, accepted values, sort options, pagination and selectable result columns. |
| `company_filter_options` | Company filter options | core | Look up matching company filter values using Companies Radar's sidebar vocabulary and typeahead services. |
| `get_company_columns` | Get company columns | API keys | Fetch only selected display columns for up to twenty company domains. Formatted values are not financial statements. |
| `get_company_intelligence` | Get company intelligence | API keys | Read company scores, peer comparisons, earnings and risk narratives. Scores are derived assessments, not financial facts. |
| `financial_filter_catalog` | Financial filter catalog | API keys | Discover precise USD screening, source financial band boundaries, fiscal-period semantics and limits. |
| `screen_company_financials` | Screen company financials | API keys | Screen a bounded candidate page or explicit domains against exact dated USD financial constraints; retain unknowns, source gates and evidence. |
| `get_company_team` | Get company team | core | Retrieve recorded company founders, key people or exactly affiliated professional cards with separate group requests and bounded pagination. |
| `get_financials` | Get financials | core | Retrieve income, balance-sheet and cash-flow metrics by fiscal period; distinguish filings from news reports and preserve currency and access limits. |
| `get_company_events` | Get company events | core | Read a company's event timeline, momentum, risks and the effective account-limited date window. |
| `get_company_funding` | Get company funding | core | Read reported funding rounds and investors; retain approximate-amount flags. |
| `get_company_enrichment` | Get company enrichment | API keys | Read legal identity, hiring, reputation, digital presence, innovation and social activity when available. |
| `find_competitors` | Find competitors | core | Find competitors in a named market, grouped by funding stage. |
| `company_brief` | Company brief | core | Return compact summaries of profile, financials, intelligence, events, funding, enrichment and news with separate detail requests and explicit coverage. |
| `compare_companies` | Compare companies | core | Compare two to five companies with separately labelled fiscal periods and partial-coverage flags. |
| `search_investors` | Search investors | API keys | Find investors by headquarters and portfolio industries or markets. |
| `investor_directory` | Investor directory | API keys | List published investor pages, sectors and cities. |
| `get_investor_page` | Get investor page | core | Read investor identity, measured portfolio metrics, dated coverage and available detail fields by published slug. |
| `get_investor_field` | Get investor field | API keys | Retrieve one investor field: paginated portfolio or shortlist, sector/stage analysis, follow-on cohorts, co-investors or sourced news. |
| `market_pulse` | Market pulse | core | Read recent funding, trending markets, sectors and investors for a bounded window. |
| `location_intelligence` | Location intelligence | core | Retrieve Companies Radar's existing business intelligence for a named location. |
| `discover_industries` | Discover industries | core | Find up to five matching industry or market names using a specific query. |
| `search_jobs` | Search jobs | core | Find job listings by company, skills, role, geography and freshness. |
| `job_filter_catalog` | Job filter catalog | API keys | Discover job filters, source values, sorting and source matching semantics. |
| `job_filter_options` | Job filter options | API keys | Suggest observed job titles, skills, employer names or locations. |
| `search_internships` | Search internships | API keys | Search dedicated internship records by employer, title, location, skills, stipend and posted dates; preserve vacancy-status uncertainty. |
| `companies_offering_internships` | Companies offering internships | API keys | Group matching observed internship listings by exact employer name, with counts, titles and detail IDs. |
| `get_internship` | Get internship | API keys | Retrieve a source internship with description, stipend, skills, dates, application URL and validity qualifications. |
| `companies_hiring` | Companies hiring | core | Find hiring companies for the same job filters. |
| `get_job` | Get job | API keys | Retrieve a job listing by an ID returned by search_jobs. |
| `salary_benchmark` | Salary benchmark | core | Read salary statistics for a role, geography and optional currency; retain sample size and coverage. |
| `search_apps` | Search apps | core | Search individual Android apps by name, developer, exact website host, category, installs, ratings and price model. |
| `get_app` | Get app | API keys | Read compact app identity, observed installs and rating, detail availability and history count. |
| `get_app_field` | Get app field | API keys | Retrieve one app field: listing, ratings, monetization, release, developer, growth or paginated install history. |
| `app_filter_options` | App filter options | API keys | List matching observed Play Store categories for app discovery. |
| `search_people` | Search people | core | Find professional profiles by name, role, company, schools, skills, seniority and location; contact values require a separate request. |
| `people_filter_options` | People filter options | API keys | Look up canonical schools, skills and sectors accepted by people search. |
| `get_company_contacts` | Get company contacts | API keys | Request company emails and/or phones separately; requires explicit contacts scope and a paid linked Companies Radar account. |
| `get_person_contacts` | Get person contacts | API keys | Request one person's emails and/or phones; preserve whether the source is the person or a company-domain fallback. Requires contacts scope and paid Companies Radar access. |
| `search_news` | Search news | API keys | Search associated news; a company filter uses business-news coverage. Headlines default to 100 per page. |
| `search_business_news` | Search business news | core | Search business headlines for a topic or company with date, sentiment and priority filters. |
| `news_overview` | News overview | core | Read measured coverage, headline examples and topic context in a bounded date window. |
| `news_trends` | News trends | API keys | Measure daily, weekly or monthly news volume while preserving the available date window. |
| `news_sentiment` | News sentiment | API keys | Read the distribution and timeline of news sentiment. |
| `search_business_events` | Search business events | API keys | Read structured business events associated with a topic or company and their article references. |
| `search_funding_news` | Search funding news | core | Find funding coverage by company, topic, investor, sector, round and reported USD amount. |
| `get_article` | Get article | core | Retrieve the full article and attribution for an article ID returned by news or company events. |
