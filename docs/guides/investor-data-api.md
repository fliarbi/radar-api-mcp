# Investor data API for venture capital and investment research

Radar's investor data API supports investor discovery, a directory of published
investor pages and retrieval of those pages by slug. Use it to explore investors
associated with a sector or geography and then connect the research to company
funding data or funding news.

Investor search and company funding history answer different questions. Search
discovers investor entities; a funding record supplies reported associations with
a particular company or round. Neither alone establishes an investor's current
mandate, available capital or intention to fund a new deal.

## Search for investors

`search_investors` maps to `POST /v1/investors/search`:

```json
{"filters":{"locations":["India"],"industries":["Software"]},"limit":20,"page":0}
```

The filter vocabulary follows the company search model. Radar interprets relevant
investor filters through its existing headquarters and portfolio classifications.
Check account access metadata because the linked plan can restrict filters or
result counts.

## Discover published investor profiles

Call `investor_directory` (`POST /v1/investors/directory`) with an empty body:

```json
{}
```

Choose a returned slug and pass it to `get_investor_page`
(`POST /v1/investors/page`). For example, the body shape is
`{"slug":"slug-returned-by-directory"}`. Do not invent slugs from names and assume
they exist. Some published pages provide metadata while a detailed roster remains
behind another access gate; the API does not bypass that gate.

## Turn investor discovery into a research workflow

Start with a sector or location, review investor identity, then retrieve relevant
company funding histories. Use [funding news](funding-news-api.md) to examine
reported announcements involving an investor, keeping article dates and source
links. Review the evidence before inferring a pattern in stage or sector preference.

A directory page is not a promise of an up-to-date fund size or a verified contact
address. These read-only APIs do not send messages, create introductions or expose
contact-reveal actions. Investor shortlists should remain research artifacts until
you validate current information through appropriate sources.

Related: [startup funding data](startup-funding-data-api.md), [B2B company search](company-search-api.md),
[company monitoring](company-monitoring-api.md), [MCP integration](company-intelligence-mcp-server.md).
