# B2B data API for company research and account intelligence

Radar's B2B data API lets an application discover companies, retrieve business
profiles and connect those profiles to financial data, funding rounds, hiring
signals and news. It is useful when a business-to-business research workflow
needs several kinds of evidence about the same account, rather than a name alone.

For example, a sales operations team can find software companies in a market,
resolve their website domains, then attach company profiles and recent business
events to an internal account review. An analyst can use the same domain to
retrieve financial metrics and check the evidence behind reported growth.

## A practical account research workflow

Start with `search_companies` (`POST /v1/companies/search`). This request uses
industry and geography as firmographic filters:

```json
{"filters":{"industries":["Software"],"locations":["India"]},"limit":20,"page":0}
```

Use a returned company domain in `company_brief` (`POST /v1/companies/brief`):

```json
{"domain":"microsoft.com","include_news":false,"event_days":90}
```

A brief assembles profile, financials, derived intelligence, events, funding and
enrichment. Enable `include_news` only when a News service and linked News key are
available. In account mode, this request reserves six credits; successful sections
consume credits and failed sections are refunded. Keep `meta.partial` visible to
the reader so an unavailable section is not mistaken for a complete company record.

## Choosing the right business data

| Need | Use |
|---|---|
| Build a company list | Filtered search or semantic company search |
| Identify one business | Company profile by domain |
| Add context to an existing account | Company enrichment and event history |
| Evaluate reported financial performance | Financial metrics with fiscal periods and source types |
| Investigate recent announcements | Business news, funding news and source articles |

Radar does not expose email-reveal or phone-reveal actions through this gateway.
Professional profile search is a separate retrieval capability. Sending CRM
messages or creating outreach campaigns is outside these tools' behavior.

## Coverage and integration questions

**Is this a downloadable B2B database?** This package provides bounded API
queries. It does not promise a complete company database export or a fixed
number of companies. Account plan restrictions can limit filters and results.

**Can AI agents use the same company data?** Yes. The MCP server exposes the same
typed retrieval operations. REST and MCP share account usage when account mode
is enabled; changing transport or creating another key does not reset credits.

Next: [get an API key](api-keys-authentication.md), [company search](company-search-api.md),
[company enrichment](company-enrichment-api.md), or [MCP setup](company-intelligence-mcp-server.md).
See the [documentation index](../README.md) for the complete guide collection.
