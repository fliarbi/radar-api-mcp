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

<!-- captured-workflow -->
## Separate an announcement from a confirmed funding transaction

Funding coverage may report a completed round, negotiations, a target raise, a fund
launch or a company's investment into another business. Those statements should
not all become incoming equity transactions for the company mentioned in the
headline. Retain the source article and inspect who received capital, who invested,
the reported date and whether the amount is approximate or proposed.

Use an investor or round filter to narrow a discovery query, then inspect the
returned evidence before joining it to a structured funding record. A company's
valuation, its cumulative funding and the amount in one round are different
quantities. A repeated announcement syndicated across several publishers should
not increase a transaction total. Deduplicate article IDs for news presentation
and separately reconcile transaction identity for a funding-history table.

The local funding-news call below returned 503 because business News was not
configured. In contrast, the [company funding endpoint](../reference/get_company_funding.md)
returned reported round data from Radar, including unresolved associations. That
difference is useful: a structured funding record can be available while its
associated news evidence remains unavailable. Preserve the missing-evidence state
until an authorized connected service supplies the article; do not turn it into
a claim that the round has been independently verified.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/news/funding`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: search_funding_news -->
```json
{
  "q": "startup funding",
  "limit": 2
}
```

<!-- response-example: search_funding_news -->
```json
{
  "ok": false,
  "feature": "search_funding_news",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:59:24.816244+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  },
  "error": {
    "kind": "service_unavailable",
    "message": "This data service is not connected to the private preview"
  }
}
```

This is the captured **complete response**, HTTP **503**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_funding_news.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

This live gateway capture returned HTTP 503 service_unavailable because the News connection was not configured. The response below is the actual output. No headlines, sentiment counts, funding amounts or event records are fabricated to make the example look successful.

See the [complete search_funding_news endpoint reference](../reference/search_funding_news.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
