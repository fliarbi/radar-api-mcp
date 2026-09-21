# Financial data API for company revenue, earnings and financial research

Radar's financial data API retrieves company financial metrics by fiscal period
and labels their source type. Use it to inspect available revenue, profitability,
assets, liabilities and cash-flow evidence for a company, then connect relevant
figures to financial news when article references are available.

This is a company-fundamentals interface. It does not expose a stock-price feed,
tick-level market data, trading orders or a universal archive of regulatory filings.
The amount and depth of company financial data depend on Radar's source coverage
and the linked account's access.

## Request company financial data

Use `get_financials` (`POST /v1/companies/financials`):

```json
{"domain":"microsoft.com","statement":"all","period_type":"annual","year_from":2022,"limit":40}
```

Inspect `data.periods` rather than assuming a fixed time series. Each period can
include the fiscal year and quarter, source label, reported date, filing date,
period end, form type and metrics. Exact dates remain absent when the upstream
record does not provide them.

## Preserve the meaning of each financial metric

| Field | How to use it |
|---|---|
| `value`, `currency`, `unit` | Display the numerical amount with its currency and unit |
| `source_type` | Distinguish `filing`, `news_report` and `unspecified` |
| `native_value`, `native_currency` | Retain the original currency where supplied |
| `article_ids` on a period | Retrieve available news evidence through `get_article` |
| `access_limited` | Tell the reader when account access exposes only part of the archive |

The gateway preserves zero and negative values. Missing metrics are omitted;
they are not converted into zero. Do not sum native values across currencies,
infer an EPS currency when it is unspecified, or label a news-reported estimate
as a filed result. Returned FX metadata describes upstream conversion; the API
does not calculate a new exchange rate.

## Build a comparison that readers can verify

Compare fiscal periods only after checking their labels and available dates.
Two companies can both report “FY2025” while covering different calendar months.
Use [financial statement filters](company-financial-statements-api.md) for a
specific statement family, and [financial news](financial-news-api.md) for the
associated reporting context. Company intelligence scores are separate derived
assessments; they should not replace retrieved financial evidence.

A small response may reflect plan-limited history rather than a company's total
reporting history. The [verification record](../VERIFICATION.md) describes the
measured private-preview coverage and its current limits.

Related: [company lookup](company-data-api.md), [financial statements](company-financial-statements-api.md),
[financial news](financial-news-api.md), [pricing](pricing-pay-per-use.md).

<!-- captured-workflow -->
## Read an actual financial response from period to metric

The first captured period below is labeled Q3 FY2026. Its revenue value is
82,886,000,000 USD and carries `source_type=filing`; its net-income value is
31,778,000,000 USD. These numbers are reproduced from the API response to show
the wire contract. They have not been independently reconciled with a company
filing in this documentation exercise.

Notice the difference between a missing date and a known reporting label:
`period_end` is null while reported and filed dates are present. A chart can use
the supplied fiscal label and show that the exact end date is unknown. It should
not substitute the filing date as the period end. Likewise the EPS metric has a
per-share unit and a null normalized currency; the presence of a native currency
does not authorize inventing a normalized one.

The request returned two periods from a known archive count of twenty and marked
access limited. Both captured periods and all their available metrics are now shown.
The documentation no longer reduces financial output to one period and six fields.
An account-limited response still does not represent the complete company history.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/financials`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_financials -->
```json
{
  "domain": "microsoft.com",
  "limit": 2
}
```

<!-- response-example: get_financials -->
```json
{
  "ok": true,
  "feature": "get_financials",
  "data": {
    "domain": "microsoft.com",
    "statement": "all",
    "has_data": true,
    "periods": [
      {
        "period": "Q3 FY2026",
        "fiscal_year": 2026,
        "fiscal_period": "Q3",
        "period_end": null,
        "reported_date": "2026-04-29",
        "filed_date": "2026-04-29",
        "form_type": "10-Q",
        "metrics": {
          "cash": {
            "value": 32105000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 32105000000.0,
            "native_currency": "USD"
          },
          "eps": {
            "value": 4.27,
            "currency": null,
            "unit": "per_share",
            "source_type": "filing",
            "native_value": 4.27,
            "native_currency": "USD"
          },
          "gross_profit": {
            "value": 56058000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 56058000000.0,
            "native_currency": "USD"
          },
          "long_term_debt": {
            "value": 40262000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 40262000000.0,
            "native_currency": "USD"
          },
          "net_income": {
            "value": 31778000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 31778000000.0,
            "native_currency": "USD"
          },
          "operating_cash_flow": {
            "value": 46679000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 46679000000.0,
            "native_currency": "USD"
          },
          "operating_income": {
            "value": 38398000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 38398000000.0,
            "native_currency": "USD"
          },
          "revenue": {
            "value": 82886000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 82886000000.0,
            "native_currency": "USD"
          },
          "stockholders_equity": {
            "value": 414367000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 414367000000.0,
            "native_currency": "USD"
          },
          "total_assets": {
            "value": 694228000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 694228000000.0,
            "native_currency": "USD"
          },
          "total_liabilities": {
            "value": 279861000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 279861000000.0,
            "native_currency": "USD"
          }
        },
        "article_ids": [
          "69e99ba475f157062cafcd91",
          "69f87f9d43843dd771ce0936",
          "69f8a61b43843dd771d24172",
          "69f9d902713680636eef61bb"
        ],
        "currency_conversion": "native_usd"
      },
      {
        "period": "Q2 FY2026",
        "fiscal_year": 2026,
        "fiscal_period": "Q2",
        "period_end": null,
        "reported_date": "2025-12-31",
        "filed_date": "2026-01-28",
        "form_type": "10-Q",
        "metrics": {
          "cash": {
            "value": 24296000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 24296000000.0,
            "native_currency": "USD"
          },
          "eps": {
            "value": 5.16,
            "currency": null,
            "unit": "per_share",
            "source_type": "filing",
            "native_value": 5.16,
            "native_currency": "USD"
          },
          "gross_profit": {
            "value": 55295000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 55295000000.0,
            "native_currency": "USD"
          },
          "long_term_debt": {
            "value": 40262000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 40262000000.0,
            "native_currency": "USD"
          },
          "net_income": {
            "value": 38458000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 38458000000.0,
            "native_currency": "USD"
          },
          "operating_cash_flow": {
            "value": 35758000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 35758000000.0,
            "native_currency": "USD"
          },
          "operating_income": {
            "value": 38275000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 38275000000.0,
            "native_currency": "USD"
          },
          "revenue": {
            "value": 81273000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 81273000000.0,
            "native_currency": "USD"
          },
          "stockholders_equity": {
            "value": 390875000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 390875000000.0,
            "native_currency": "USD"
          },
          "total_assets": {
            "value": 665302000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 665302000000.0,
            "native_currency": "USD"
          },
          "total_liabilities": {
            "value": 274427000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 274427000000.0,
            "native_currency": "USD"
          }
        },
        "article_ids": [
          "6988a7773757765ee826377c",
          "698e37498d29a990b6e524d5",
          "69bbe6aba75fc0dcb02055d5",
          "69bce327a7b1648247b810ef",
          "69c42f5b7c4635ab38e80104",
          "69cc188adcf7c26bbed60f05",
          "69dfb24286bd23245a9134fc",
          "69dfb6f5c1e955063e150b93"
        ],
        "currency_conversion": "native_usd"
      }
    ],
    "returned": 2,
    "truncated": true,
    "access_limited": true,
    "available_period_count": 20,
    "computed_at": "2026-09-19T17:19:34.120000Z",
    "summary": {
      "narrative": "Latest reported Q3 FY2026: revenue $82.89B, net income $31.78B, EPS $4.27. YoY +18.3% (1.18× prior period). Growth pattern is consistent across reported periods. Recent signals: Raised guidance, Beat estimates, Profitable. Financials sourced from official filings (10-K, 10-Q, 10-Q/A); news/BI estimates fill any gaps."
    }
  },
  "window": {
    "data_through": "2026-04-29"
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:45.976790+00:00",
    "partial": false,
    "notes": [
      "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
      "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies.",
      "The linked Radar account exposes only part of the financial archive."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_financials.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The captured request returned two periods from an archive count of twenty, with access_limited=true. Its first period was Q3 FY2026 and its revenue metric carried source_type=filing. The exact period end was null, while EPS currency was also null despite a supplied native currency. These are source-response examples, not an independent audit of Microsoft's financial results.

See the [complete get_financials endpoint reference](../reference/get_financials.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 66 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
