# Funding news API for startup investment announcements

The funding news API searches articles about company fundraising and investment
announcements. Use it when the research question is “Which funding announcements
match this sector, investor or company?” For a company's existing structured round
history, use the separate [startup funding data API](startup-funding-data-api.md).

Funding news can help a researcher find emerging companies, review an investor's
reported activity or explain a recent change in a company's profile. An article
and a funding round are different records: several articles may describe one
round, and an announcement may precede the legal closing of a transaction.

## Search funding announcements

`search_funding_news` maps to `POST /v1/news/funding`:

```json
{"q":"software","sector":"Software","round_type":"Series A","date_from":"2026-01-01","date_to":"2026-08-31","min_amount_usd":1000000,"limit":20}
```

You can also supply an `investor` name or a company domain. At least `q` or
`company` is required, even when other funding filters are present. Round and
sector labels depend on the connected service's classification; use the returned
data and coverage notes to assess how well a query matches your intended category.

`min_amount_usd` is a nonnegative dollar threshold. It does not establish the
original currency of a reported funding round, the company's valuation, or the
amount of capital actually received.

## Build an evidence-backed funding feed

Save article identifiers, URLs, dates and any associated company identifiers.
Follow the article with `get_article` when permitted, then retrieve the company's
profile and structured funding record. Before adding amounts across announcements,
check for repeat coverage of the same event, approximate figures and differences
between debt, equity, round amount, cumulative funding and valuation.

Funding news uses News API cursor pagination. Keep the original query and date
window stable while following the cursor. In account mode, each successful search
or article retrieval is a separately metered data operation.

## Access and freshness

The News service and linked News key must both be configured. The private preview
does not yet claim a successful live News connection; see the
[verification record](../VERIFICATION.md). No delivery-latency or complete-global-
coverage claim is made. `window` and `meta` describe the returned coverage, and a
missing announcement should remain an unknown rather than a negative finding.

Related: [funding-round data](startup-funding-data-api.md), [investor data](investor-data-api.md),
[financial news](financial-news-api.md), [company monitoring](company-monitoring-api.md).
