# Startup funding data API: company funding rounds and investors

Radar's startup funding data API retrieves reported funding rounds for a company
identified by its domain. Use it to add fundraising history to a company profile,
review available investor associations or explore funding activity in a market.
The endpoint represents available reported data; it is not a cap table or a
guarantee that every financing event has been captured.

## Retrieve a company's funding history

`get_company_funding` maps to `POST /v1/companies/funding`:

```json
{"domain":"microsoft.com"}
```

The domain is an input-format example, not a claim that the company is a startup
or that a particular round exists. Use a domain discovered from your own company
search results when researching a startup.

Keep returned round labels, investor names, dates and amount qualifiers together.
If Radar marks an amount as approximate, show that qualifier in the application.
Do not silently turn an undisclosed amount into zero or treat a reported round
amount as a valuation.

## Explore market-level funding context

`market_pulse` (`POST /v1/markets/pulse`) gives a bounded view of recent funding,
markets, sectors and investors:

```json
{"days":30,"limit":5}
```

Use it for discovery and context, then inspect individual companies and funding
evidence. It is not a complete investment-flow accounting dataset, and the number
of returned records should not be presented as all funding in an economy.

## Join structured rounds to funding news

The [funding news API](funding-news-api.md) answers a different question: it finds
articles about fundraising announcements. Retrieve article evidence when available
and licensed through the linked News account. A company can have a structured
funding record even when News is unavailable, and a funding article may not yet be
represented in structured history.

For deduplication, compare company identity, round label, timing, participants and
the original report. Do not assume that matching dollar amounts prove two records
are the same transaction. Preserve uncertainty when sources disagree.

## Frequently asked questions

**Does this include private-company ownership percentages?** The gateway exposes
reported funding retrieval, not shareholder-register or capitalization-table
management.

**Does a paid API key unlock every round?** Credits pay for API usage. Existing
Radar entitlements and source coverage continue to determine returned data.

Related: [company data](company-data-api.md), [investor discovery](investor-data-api.md),
[funding news](funding-news-api.md), [API pricing](pricing-pay-per-use.md).
