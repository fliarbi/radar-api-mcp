# Radar developer documentation: B2B company data, financial data and news APIs

Build applications that search for businesses, enrich company profiles, compare
financial statements, investigate startup funding and retrieve associated news.
Radar exposes 30 data operations through a REST API and a Model Context Protocol
(MCP) server. Choose a guide based on the information your application needs.

**Private preview.** Access is by invitation and operator configuration. The
repository is private; these pages are not publicly searchable or Google-indexed.
No public endpoint or production checkout is advertised. News connections require
separate setup; see the [measured verification record](VERIFICATION.md).

## Start here

1. [Get an API key and connect your account](guides/api-keys-authentication.md).
2. [Understand Radar plans, API credits and pay-per-use](guides/pricing-pay-per-use.md).
3. Choose a data guide below, then inspect the [complete capability reference](CAPABILITIES.md).
4. For an AI assistant, follow [MCP company intelligence](guides/company-intelligence-mcp-server.md).

## Company discovery and business data

| Guide | What it helps you build |
|---|---|
| [B2B data API](guides/b2b-data-api.md) | Account research and business-to-business data workflows |
| [Company data API](guides/company-data-api.md) | Company lookup by website domain and structured company profiles |
| [Company search API](guides/company-search-api.md) | Company lists filtered by industry, geography, funding and financial bands |
| [Company enrichment API](guides/company-enrichment-api.md) | Firmographic, legal, hiring and digital context for existing accounts |
| [Competitor intelligence API](guides/competitor-intelligence-api.md) | Market peers and evidence-aware company comparisons |
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

## Integration references

- [REST and MCP user guide](USER_GUIDE.md): request shapes, response semantics and errors.
- [Data API OpenAPI schema](openapi.json) and [account-mode OpenAPI schema](account-openapi.json).
- [Account operations and anti-abuse controls](ACCOUNTS.md): private activation, payment reconciliation and limits.
- [Operator guide](OPERATIONS.md): upstream connections, private deployment and secret handling.
- [Search research and documentation map](SEARCH_RESEARCH.md): query clusters, primary sources and publication boundary.

Every example uses a placeholder domain or a real company domain as an input,
not as a promise that the company has complete coverage. Preserve returned dates,
currencies, source types and access flags when showing data to your users.
