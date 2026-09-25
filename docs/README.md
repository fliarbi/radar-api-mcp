# Radar developer documentation: B2B company data, financial data and news APIs

Build applications that search for businesses, enrich company profiles, compare
financial statements, investigate startup funding and retrieve associated news.
Radar exposes 53 data operations through a REST API and a Model Context Protocol
(MCP) server. Choose a guide based on the information your application needs.

**Private preview.** Access is by invitation and operator configuration. The
repository is private; these pages are not publicly searchable or Google-indexed.
No public endpoint or production checkout is advertised. News connections require
separate setup; see the [measured verification record](VERIFICATION.md).

[Watch seven animated UI workflows](ANIMATED_USE_CASES.md) for Claude Code or Codex,
or open the [local gallery](demos/index.html). The clips show prompts, focused Radar
reads and client-built result views, with saved and illustrative data clearly labeled.

Start with [the company data depth walkthrough](COMPANY_DATA_DEPTH.md) to see what
the data actually contains: complete classifications, founder names, dozens of
technologies, traffic by geography, app download/rating totals, hiring and field coverage.
It includes three measured company examples with all returned business rows.
The [smaller-company examples and empty-result review](EXAMPLE_REPAIRS.md) add
electroCore, Mastech Digital, Qualys, Connvertex and Yext, while clearly identifying
the blocked balance-sheet/cash-flow reads and other intentional coverage cases.
Use the [complete example audit](EXAMPLE_AUDIT.md) to check which outputs are
populated, empty, partial, restricted, unsuccessful or based on test identities.

For concrete questions, use [50 executed business scenarios](scenarios/README.md),
[the feedback audit](SCENARIO_AUDIT.md) and [all 43 filter mappings](FILTER_AUDIT.md).
New specialist guides cover [exact financial filters](guides/financial-filters-data-api.md),
[teams and professional profiles](guides/teams-people-data-api.md), and
[technology/traffic data](guides/technology-traffic-data-api.md).

Contact workflows: [company emails and phones](guides/company-email-phone-api.md),
[founder details and contact IDs](guides/founder-contact-data-api.md),
[LinkedIn/social references](guides/linkedin-social-data-api.md), and
[the complete contact variables and response guide](CONTACTS.md), with
[24 copyable request recipes](CONTACT_REQUEST_RECIPES.md).
The [research index](research/README.md) now links source findings, live/fixture
evidence, known gaps and the original search research.

## Start here

1. [Get an API key and connect your account](guides/api-keys-authentication.md).
2. [Understand Radar plans, API credits and pay-per-use](guides/pricing-pay-per-use.md).
3. Choose a data guide below, then inspect the [endpoint reference with real outputs](reference/README.md).
4. For an AI assistant, follow [MCP company intelligence](guides/company-intelligence-mcp-server.md).

## Company discovery and business data

| Guide | What it helps you build |
|---|---|
| [B2B data API](guides/b2b-data-api.md) | Account research and business-to-business data workflows |
| [Company data API](guides/company-data-api.md) | Company lookup by website domain and structured company profiles |
| [Company search API](guides/company-search-api.md) | Company lists filtered by industry, geography, funding and financial bands |
| [Company enrichment API](guides/company-enrichment-api.md) | Firmographic, legal, hiring and digital context for existing accounts |
| [Competitor intelligence API](guides/competitor-intelligence-api.md) | Market peers and evidence-aware company comparisons |
| [Company potential and sales prospects](guides/potential-company-data-api.md) | Explainable investment/growth and B2B discovery with supporting evidence |
| [Company monitoring API](guides/company-monitoring-api.md) | API watchlists, company events and associated news |

## Financial data, investment research and news

| Guide | What it helps you build |
|---|---|
| [Financial data API](guides/financial-data-api.md) | Revenue, profit, assets and cash-flow research with source labels |
| [Financial statements API](guides/company-financial-statements-api.md) | Income statement, balance sheet and cash-flow metrics by fiscal period |
| [Financial news API](guides/financial-news-api.md) | Company earnings and business-news discovery with date windows |
| [Funding news API](guides/funding-news-api.md) | Startup funding announcements filtered by investor, sector and round |
| [Startup funding data API](guides/startup-funding-data-api.md) | Reported funding rounds, investors and market funding context |
| [Investor data API](guides/investor-data-api.md) | Investor discovery, directories and published investment profiles |
| [Hiring signals and jobs API](guides/hiring-signals-jobs-api.md) | Hiring companies, job listings and salary benchmarks |

## App intelligence and internships

| Guide | What it helps you build |
|---|---|
| [Mobile app data API](guides/apps-data-api.md) | Android app discovery, developer-domain matching, ratings, monetization and dated install growth |
| [Companies offering internships](guides/internships-companies-api.md) | Employer lists, role requirements, stipends and source deadline checks |
| [Seven real app field outputs](APP_DATA_DEPTH.md) | Complete captured business structures for separate app detail requests |
| [Radar feature coverage map](RADAR_FEATURE_COVERAGE.md) | Implemented workflows, required connections and remaining source gaps |

## Integration references

- [All 69 JSON endpoint examples](reference/README.md): request tables, captured responses, REST/MCP calls and field explanations.
- [MCP initialization and browser responses](reference/transports.md): actual protocol and HTML/asset results.
- [Downloadable example index](examples/index.json): request, status, provenance, omission paths and checksums.
- [Observed data quality](DATA_QUALITY.md): identity ambiguity, date anomalies, partial searches and unavailable connections.
- [REST and MCP user guide](USER_GUIDE.md): request shapes, response semantics and errors.
- [Data API OpenAPI schema](openapi.json) and [account-mode OpenAPI schema](account-openapi.json).
- [Account operations and anti-abuse controls](ACCOUNTS.md): private activation, payment reconciliation and limits.
- [Operator guide](OPERATIONS.md): upstream connections, private deployment and secret handling.
- [Search research and documentation map](SEARCH_RESEARCH.md): query clusters, primary sources and publication boundary.

The live examples retain actual values, including empty, partial and error results.
Account examples are executed local demonstrations with synthetic identity and
payment providers; credentials are redacted. Response excerpts explicitly list
any omitted source prose in their downloadable records. Preserve returned
dates, currencies, source types and access flags when showing data to your users.

Start with [compact profiles and company fields](COMPANY_DATA_DEPTH.md),
[filter options and selected columns](FILTERS_AND_LISTINGS.md), and
[company/professional email and phone retrieval](CONTACTS.md).
The [Radar source review](RADAR_SOURCE_REVIEW.md) documents the product flows used.

- [Investor data depth](INVESTOR_DATA_DEPTH.md): 19 real detail-field captures plus two measured summaries.
- [Additional potential-data outputs](POTENTIAL_DATA_EXAMPLES.md): live profitable-growth and hiring-based sales-prospect screens.
- [Response depth audit](DATA_DEPTH_AUDIT.md): every endpoint inventoried for fields, arrays and explicit omissions.
