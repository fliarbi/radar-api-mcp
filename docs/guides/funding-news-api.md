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

The local integration below now returns five real funding records from 1,085
matches in April 2026, including investors and source article IDs. Its identity
and quota dependencies are isolated test fixtures; its queries and data are real.
The [company funding endpoint](../reference/get_company_funding.md) remains a
separate company-oriented view. Both can contain unresolved associations or
outlying reported amounts. The returned totals explicitly identify records with
unknown amounts and fixed-rate conversions; they are not an independently audited
measurement of money raised. A successful retrieval does not verify a transaction.

## Worked example: live News data with an isolated integration identity

The request captured for this example was **`POST /v1/news/funding`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: search_funding_news -->
```json
{
  "q": "funding",
  "limit": 5,
  "date_from": "2026-04-01",
  "date_to": "2026-04-30"
}
```

<!-- response-example: search_funding_news -->
```json
{
  "ok": true,
  "feature": "search_funding_news",
  "data": {
    "items": [
      {
        "id": "2146b783282e70a6",
        "company_name": "Featherless.ai",
        "domain": null,
        "round_type": "Series A",
        "amount_usd": 20000000.0,
        "valuation_usd": null,
        "currency": "USD",
        "amount": 20000000.0,
        "valuation": null,
        "investors": [
          {
            "name": "AMD Ventures",
            "domain": "amdventures.com",
            "amount": null
          },
          {
            "name": "airbus ventures",
            "domain": "airbusventures.vc",
            "amount": null
          },
          {
            "name": "bmw i ventures",
            "domain": "bmwiventures.com",
            "amount": null
          },
          {
            "name": "kickstart ventures",
            "domain": "kickstart.ph",
            "amount": null
          },
          {
            "name": "panache ventures",
            "domain": "panache.vc",
            "amount": null
          },
          {
            "name": "Wavemaker Ventures",
            "domain": null,
            "amount": null
          }
        ],
        "sector": "AI",
        "country": null,
        "city": null,
        "use_of_funds": "Scale global infrastructure, launch a dedicated marketplace for specialized open models, and deepen technical integration with diverse hardware architectures",
        "published_at": "2026-04-30T23:33:54",
        "coverage_count": 1,
        "article_ids": [
          "69f8a6fb43843dd771d249ae"
        ],
        "article_id": "69f8a6fb43843dd771d249ae"
      },
      {
        "id": "760835c67cc74f24",
        "company_name": "Primogene",
        "domain": null,
        "round_type": null,
        "amount_usd": 4800000.0,
        "valuation_usd": null,
        "currency": "USD",
        "amount": 4800000.0,
        "valuation": null,
        "investors": [],
        "sector": null,
        "country": "Germany",
        "city": null,
        "use_of_funds": null,
        "published_at": "2026-04-30T20:35:26",
        "coverage_count": 1,
        "article_ids": [
          "69f8a6d28937ef12fc0ae01e"
        ],
        "article_id": "69f8a6d28937ef12fc0ae01e"
      },
      {
        "id": "291d02119eb021db",
        "company_name": "lafleur",
        "domain": "lafleur.link",
        "round_type": "prepayment financing",
        "amount_usd": 22200000.0,
        "valuation_usd": null,
        "currency": "CAD",
        "amount": 30000000.0,
        "valuation": null,
        "investors": [
          {
            "name": "trafigura",
            "domain": "trafigura.com",
            "amount": null
          }
        ],
        "sector": "gold mining",
        "country": "Canada",
        "city": null,
        "use_of_funds": "restart of Beacon Gold Mill and initial production",
        "published_at": "2026-04-30T19:36:16",
        "coverage_count": 1,
        "article_ids": [
          "69f9dde77b2d589e84521a9e"
        ],
        "article_id": "69f9dde77b2d589e84521a9e"
      },
      {
        "id": "97a3e8634c0623aa",
        "company_name": "koda health",
        "domain": "kodahealthcare.com",
        "round_type": "Series A",
        "amount_usd": 14000000.0,
        "valuation_usd": null,
        "currency": "USD",
        "amount": 14000000.0,
        "valuation": null,
        "investors": [
          {
            "name": "evidenced",
            "domain": "evidenced.app",
            "amount": null
          },
          {
            "name": "Mudita Venture Partners",
            "domain": "muditavp.com",
            "amount": null
          },
          {
            "name": "techstars",
            "domain": "techstars.com",
            "amount": null
          },
          {
            "name": "texas medical center",
            "domain": "texasmedicalcenter.org",
            "amount": null
          },
          {
            "name": "upmc enterprises",
            "domain": "enterprises.upmc.com",
            "amount": null
          }
        ],
        "sector": "Healthcare",
        "country": "USA",
        "city": null,
        "use_of_funds": "Scale operations and expand engineering, clinical strategy and customer success",
        "published_at": "2026-04-30T17:00:01",
        "coverage_count": 1,
        "article_ids": [
          "69f8a62fbbf1d314559a1e89"
        ],
        "article_id": "69f8a62fbbf1d314559a1e89"
      },
      {
        "id": "591d0ae7d74a43f0",
        "company_name": "ebury",
        "domain": "ebury.com",
        "round_type": "Financing",
        "amount_usd": 698500000.0,
        "valuation_usd": null,
        "currency": "GBP",
        "amount": 550000000.0,
        "valuation": null,
        "investors": [
          {
            "name": "centerbridge partners",
            "domain": "centerbridge.com",
            "amount": null
          },
          {
            "name": "santander",
            "domain": "santander.com",
            "amount": 50000000.0
          },
          {
            "name": "vitruvian partners",
            "domain": "vitruvianpartners.com",
            "amount": null
          },
          {
            "name": "83north",
            "domain": "83north.com",
            "amount": null
          }
        ],
        "sector": "Payments",
        "country": null,
        "city": null,
        "use_of_funds": null,
        "published_at": "2026-04-30T11:36:09",
        "coverage_count": 1,
        "article_ids": [
          "69f8947d8937ef12fc0abbc0"
        ],
        "article_id": "69f8947d8937ef12fc0abbc0"
      }
    ],
    "returned": 5,
    "total_estimate": 1085,
    "next_cursor": "eyJ2IjoxLCJ0IjoiZnIiLCJzIjoibmV3ZXN0IiwiZCI6IjIwMjYtMDQtMzAgMTE6MzY6MDkiLCJrIjoiNjQyMTMwMDYzNDU2NTg4Njk2MCJ9",
    "totals": {
      "deals": 1085,
      "deals_with_amount": 953,
      "deals_without_amount": 132,
      "sum_amount_usd": 515844387971.16,
      "median_amount_usd": 13400000.0,
      "largest_amount_usd": 122000000000.0,
      "currency": "USD",
      "note": "Each matched deal record counts once, regardless of how many articles report it. Counts are measured over the entire filtered window, independent of result limits. USD amounts use fixed conversion rates, not current or transaction-date exchange rates. Only finite, positive reported amounts enter sums, medians and maxima. Missing, zero, negative and non-finite amounts count as unknown; amount statistics are null when no matched deal has a usable amount. Reported figures and outliers are retained, not independently verified financial amounts."
    },
    "limit": 5,
    "sort": "newest"
  },
  "window": {
    "since": "2026-04-01",
    "until": "2026-04-30",
    "days": 30,
    "data_through": "2026-05-05",
    "freshness": "this business dataset is available through 2026-05-05; company events, funding and company-linked news may have different latest available dates"
  },
  "meta": {
    "retrieved_at": "2026-09-20T10:59:55.948583+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI",
    "coverage": {
      "available": true
    }
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T10:59:55.948797+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_funding_news.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

**Capture method:** Executed authenticated local Radar gateway and actual Prism News application code against live data; isolated test identity and quota dependencies, with the News Free plan's data limits retained. No deployed News URL, production News-key authentication or customer billing was verified.

The captured response was executed through the real gateway and News application against live data, with an isolated test identity and quota dependencies. It verifies data retrieval, not a deployed News URL, production key authentication or customer billing. The April funding query returned five records from 1,085 matching deal records, including company/domain, round, amounts, investors, sector, geography and source article IDs. Of the matched records, 953 contain usable positive amounts and 132 do not. Source totals include large unverified outliers and fixed-rate currency conversions; they are not audited funding statistics.

See the [complete search_funding_news endpoint reference](../reference/search_funding_news.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
