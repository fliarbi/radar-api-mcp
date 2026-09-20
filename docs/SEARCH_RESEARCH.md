# Search research and documentation coverage

Research date: **2026-09-20**. This record explains how the guides map to real
developer questions. It does not estimate keyword traffic, difficulty, ranking
position or future search performance.

## Google and Bing search through the automation implementation

The follow-up used the existing Google/Bing implementation in the user's automation
workspace through an MCP stdio bridge. That implementation exposes Google general
web search and Google/Bing **News** search over HTTP; it does not implement Bing
general web search. A temporary loopback service and MCP client exercised those
actual routes. Google News RSS was then added as an explicitly labeled public-feed
fallback through the same MCP client. No CAPTCHA bypass was attempted.

The [dated search evidence](research/2026-09-20-search.json) preserves all fifteen
queries, selected result titles/URLs, engine/vertical and outcomes:

| Route used | Queries | Outcome |
|---|---:|---|
| Google general web, automation browser | 6 | All reached a CAPTCHA check; no usable result headings |
| Google News, automation browser | 1 | CAPTCHA check |
| Bing News, automation browser | 4 | All returned results; one pricing query was irrelevant |
| Google News RSS, MCP fallback | 4 | Three returned results; the exact funding-data phrase returned an empty feed |

Thus Google and Bing were both queried and returned usable research through the
listed News routes. The Google browser route remained blocked by its traffic
check. News search results are not general-web ranking evidence. The empty exact
phrase does not demonstrate lack of demand, and these small samples establish no
keyword volume, difficulty, ranking forecast or competitive benchmark.

## What the results changed in these documents

Bing's financial-data query returned both a company-fundamentals/MCP product
announcement and financial-account data exchange results. That ambiguity is why
the financial guide now specifies company statements, fiscal periods, currency,
units and provenance. It does not imply open-banking account access or a trading
feed. The product's own [Wisesheets API page](https://www.wisesheets.io/api) was
checked for the fundamentals/MCP terminology; its coverage and latency claims
were not transferred to Radar.

Bing startup-funding results included funding roundups rather than an API contract.
The funding-news guide therefore explains announcement evidence, deduplication,
proposed versus completed financing and the difference between a news article and
a structured round. Google RSS also returned unrelated company-funding and API
pricing material: those results were retained as evidence of query noise, not
used to set Radar's price or expand its claimed product scope.

Google RSS results for financial-data APIs and MCP company data showed comparison
and agent-integration intent. The guides now answer the practical questions behind
those terms: what the request looks like, what fields actually return, how an MCP
client calls it, how an API key is issued, and what usage costs. They do not claim
Radar is the best-ranked or most complete provider.

The official [News API search documentation](https://newsapi.org/docs/endpoints/everything)
was checked as a primary example of query/date/pagination documentation. Radar's
actual parameter names and outputs come from its own models and captures, not that
provider's response schema. Search results only informed the reader questions;
all Radar capability claims are grounded in this repository's measured behavior.

## Query clusters and the guide that answers them

| Search intent and related phrases | Dedicated guide | Distinct reader task |
|---|---|---|
| B2B data API, business data API, B2B company intelligence | [B2B data API](guides/b2b-data-api.md) | Assemble an account research workflow |
| Company data API, companies data, company lookup API | [Company data](guides/company-data-api.md) | Resolve and retrieve one business by domain |
| Company search API, find companies by industry or location | [Company search](guides/company-search-api.md) | Select filters, discover labels and paginate |
| Company enrichment API, firmographic enrichment, CRM account data | [Enrichment](guides/company-enrichment-api.md) | Add context without overwriting unknown values |
| Financial data API, company revenue API, earnings data | [Financial data](guides/financial-data-api.md) | Preserve currency, periods and metric provenance |
| Financial statements API, income statement API, balance sheet API, cash flow API | [Statements](guides/company-financial-statements-api.md) | Choose a statement and fiscal-period filter |
| Financial news API, company news API, business news API | [Financial news](guides/financial-news-api.md) | Retrieve company-associated articles and evidence |
| Funding news API, startup funding announcements, investment news API | [Funding news](guides/funding-news-api.md) | Search announcement coverage by investor/round |
| Startup funding data API, funding rounds API, venture funding data | [Funding data](guides/startup-funding-data-api.md) | Read structured reported round history |
| Investor data API, venture capital API, investor directory | [Investors](guides/investor-data-api.md) | Discover investors and published profile slugs |
| Company monitoring API, follow companies, company events API | [Monitoring](guides/company-monitoring-api.md) | Maintain an API watchlist and retrieve changes |
| Competitor API, company comparison, competitive intelligence API | [Competitors](guides/competitor-intelligence-api.md) | Find peers and compare evidence carefully |
| Hiring signals API, jobs API, companies hiring, salary data | [Hiring](guides/hiring-signals-jobs-api.md) | Interpret recruitment observations and samples |
| Company intelligence MCP server, B2B data MCP, financial data MCP | [MCP server](guides/company-intelligence-mcp-server.md) | Connect an agent to typed research tools |
| Radar API key, company data API authentication | [API keys](guides/api-keys-authentication.md) | Issue, scope, rotate and revoke credentials |
| Radar API pricing, company data API pay per use | [Pricing](guides/pricing-pay-per-use.md) | Understand plans, credits and spending controls |

Related synonyms share a guide when they serve the same task. There are no copied
city/industry variants, fabricated comparison pages, unsupported “best API” claims
or separate thin pages for every spelling. Each guide includes a concrete workflow,
actual route/tool names, captured output, coverage qualifications and related links.
The [endpoint reference](reference/README.md) adds 46 JSON operation examples,
parameter tables, field-by-field interpretation and downloadable capture records.

## Primary pages used for terminology

- [Olostep company data API](https://www.olostep.com/apis/company-data-api): company lookup and firmographic enrichment vocabulary.
- [CompanyEnrich getting started](https://docs.companyenrich.com/docs/getting-started): company enrichment and AI-agent integration use cases.
- [Grata company data API](https://grata.com/api): company discovery and enrichment as separate workflows.
- [Demandbase B2B API overview](https://developer.demandbase.com/docs/b2b-overview): business information and account-data integration terminology.
- [PitchBook direct-access API](https://pitchbook.com/products/direct-access-data/api): investment research and company/funding-data needs.
- [Moomoo financial statements API](https://openapi.moomoo.com/moomoo-api-doc/en/quote/get-financials-statements.html): statement-family and reporting-period terminology.
- [Specter transactions](https://www.tryspecter.com/transactions): distinction between transaction records and related research signals.
- [Crustdata MCP server](https://crustdata.com/mcp-server): B2B data tools for AI agents.
- [DataLayer's own MCP repository](https://github.com/datalayer-sh/mcp): GitHub-readable MCP and company-data terminology. Radar does not adopt its contact-reveal scope.

## GitHub and future Google discovery

The repository title, description, README opening and topic-specific filenames use
plain product terms. The README links to the documentation hub, and each guide
links to related workflows. GitHub topics can classify the repository for authorized
users, but private content is not publicly searchable.

GitHub notes that topic names themselves are public even when associated
repositories are private. Repository topics therefore use only generic product
terms. Topics do not make the private repository or its documents publicly searchable.
See [GitHub's topic documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).

Repository topics: `b2b-data`, `company-data`, `company-search`, `company-enrichment`,
`financial-data`, `financial-statements`, `financial-news`, `funding-news`,
`funding-data`, `investor-data`, `company-intelligence`, `company-monitoring`,
`mcp`, `mcp-server`, `model-context-protocol`, `rest-api`, `fastapi`.

After the owner approves a public documentation destination, set stable canonical
URLs, accurate page titles/descriptions, crawlable navigation and a sitemap on that
destination. Keep account consoles, secrets and runtime endpoints private. Review
all availability and pricing statements again before publication. No sitemap is
submitted, Google Search Console action taken or GitHub Pages deployment enabled
by this change. Making documentation crawlable does not guarantee indexing or ranking.

The writing approach follows [Google's helpful-content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content):
answer the reader's task with accurate original documentation and descriptive
headings, rather than generating duplicate pages around keyword permutations.
