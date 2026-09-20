# Company search API: find companies by industry, location and business signals

Radar supports two company discovery methods: a structured company search API
for explicit filters and semantic company search for a natural-language business
description. Use structured filters when reproducibility matters; use semantic
search to explore an unfamiliar market and then inspect individual matches.

## Search a defined business segment

`search_companies` maps to `POST /v1/companies/search`:

```json
{"filters":{"industries":["Software"],"locations":["India"],"revenue_bands":["10m-100m"],"profitability":["profitable"]},"page":0,"limit":20}
```

The revenue band uses Radar's existing USD classification. It is not a newly
calculated annual revenue figure. For specific amounts and reporting periods,
retrieve the company's financial data after discovery.

Available filter families include company names, industries, sectors, markets,
business models, geography, size, funding stage, technologies, products, skills,
events, financing status and ownership status. The complete accepted names and
values are in the [capability schema](../CAPABILITIES.md), rather than a guessed
list of industry labels.

Use `discover_industries` (`POST /v1/industries/discover`) with
`{"q":"software","limit":5}` to find candidate labels. Map the returned kind to
the corresponding `industries`, `sectors` or `markets` filter.

## Search by a natural-language description

`semantic_company_search` maps to `POST /v1/companies/semantic-search`:

```json
{"q":"enterprise software companies providing supply chain analytics","filters":{"locations":["India"]},"limit":10,"page":0}
```

Semantic results are candidates for review. This preview does not claim a measured
relevance score or that every result exactly satisfies the description. Retrieve
profiles and evidence before building a final shortlist.

## Pagination and plan limits

Company search uses zero-based `page`, with a maximum accepted page of 200, and
`limit` from 1 to 100. The linked Radar plan may further cap results or remove
restricted filters. Inspect returned access metadata, and do not interpret a
page's item count as the number of companies in the entire market.

Use small pages during development. In account mode, each successful search
request costs one API credit; empty successful results still represent a
completed query. Avoid restarting from page zero after transient errors if your
application has already saved earlier results.

Related: [company profiles](company-data-api.md), [B2B data API](b2b-data-api.md),
[competitor intelligence](competitor-intelligence-api.md), [pricing](pricing-pay-per-use.md).
