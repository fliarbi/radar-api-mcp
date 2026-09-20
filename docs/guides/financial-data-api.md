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
