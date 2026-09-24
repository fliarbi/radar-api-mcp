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
{"domain":"electrocore.com","statement":"income","period_type":"annual","year_from":2024,"year_to":2024,"limit":3}
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

The electroCore capture below selects annual income in FY2024 and returns revenue
of USD 25,200,000, net income of USD -11,890,000, EBITDA of USD -9,000,000 and
EPS -1.59. Every metric retains its source type (`news_report` here). This is an
actual API response, not an independent reconciliation against a company filing.
[Mastech Digital](../EXAMPLE_REPAIRS.md) provides another populated annual example.

Keep `period_end`, `reported_date` and `filed_date` distinct. A known fiscal label
can coexist with an unknown exact end date. EPS has a per-share unit; its unknown
currency must not be borrowed from another metric. Preserve negative and zero
values rather than treating them as absent.

`periods[].evidence` preserves article coverage, quality signals and official-source
flags. `operating_context` carries recorded headcount, revenue/profit growth and
guidance for income/all requests. `summary.assessment` has its own comparison
window; it is not recomputed over your selected fiscal year. Source account gates
remain explicit and this single annual period is not the whole archive.

`coverage.returned_periods_with_metrics` separates fiscal labels from usable
metrics. The separate [balance-sheet](../scenarios/13-balance-sheet.md) and
[cash-flow](../scenarios/15-annual-cash-flow.md) samples currently return no numeric
metrics in their requested families. Strict source checks on 2026-09-24 failed
on an unreachable financial-store shard. Those pages are blocked examples;
HTTP 200 alone is not successful statement coverage.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/financials`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_financials -->
```json
{
  "domain": "electrocore.com",
  "statement": "income",
  "period_type": "annual",
  "year_from": 2024,
  "year_to": 2024,
  "limit": 3
}
```

<!-- response-example: get_financials -->
```json
{
  "ok": true,
  "feature": "get_financials",
  "data": {
    "domain": "electrocore.com",
    "statement": "income",
    "has_data": true,
    "periods": [
      {
        "period": "FY2024",
        "fiscal_year": 2024,
        "fiscal_period": "FY",
        "period_end": null,
        "reported_date": "2025-03-12",
        "filed_date": null,
        "form_type": null,
        "metrics": {
          "ebitda": {
            "value": -9000000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "eps": {
            "value": -1.59,
            "currency": null,
            "unit": "per_share",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "net_income": {
            "value": -11890000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "revenue": {
            "value": 25200000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          }
        },
        "article_ids": [
          "68187d87661375d1a517a41d",
          "69bcabbc3ca60e76cf303f56"
        ],
        "currency_conversion": null,
        "evidence": {
          "coverage_count": 2,
          "quality_signals": [
            "Reported a loss",
            "Record revenue"
          ],
          "headline": "Reported record full year of 2024 revenue of $25.2 million, an increase of approximately 57% over full year of 2023.",
          "has_official": false,
          "period_has_official": false
        },
        "operating_context": {
          "employees": null,
          "revenue_growth_pct": 57.0,
          "net_income_growth_pct": -37.0,
          "guidance_revenue": null,
          "beat_or_miss": null
        }
      }
    ],
    "returned": 1,
    "truncated": false,
    "access_limited": true,
    "available_period_count": 20,
    "coverage": {
      "accessible_periods_before_filters": 3,
      "matching_periods": 1,
      "returned_periods_with_metrics": 1,
      "requested_metrics": [
        "ebitda",
        "eps",
        "gross_profit",
        "net_income",
        "operating_income",
        "revenue"
      ],
      "note": "Only entitled upstream periods are evaluated. A period can lack metrics for the selected statement; missing is not zero. Growth, guidance and evidence are source observations, not independently verified forecasts."
    },
    "computed_at": "2026-09-24T06:51:22.743000Z",
    "summary": {
      "narrative": "Latest reported Q1 FY2026: revenue $9.01M, EPS $-0.59. YoY +34.1% (1.34× prior period). Growth pattern is consistent across reported periods. Recent signals: Raised guidance, Beat estimates, Reported a loss, Record revenue.",
      "assessment": {
        "score": 87,
        "growth_consistency": 82,
        "yoy_pct": 34.1,
        "yoy_multiple": 1.34,
        "yoy_basis": "numeric",
        "quality_signals_aggregate": [
          "Raised guidance",
          "Beat estimates",
          "Reported a loss",
          "Record revenue"
        ]
      },
      "comparison_periods": {
        "latest": {
          "period_label": "Q1 FY2026",
          "period_year": 2026,
          "period_qtr": "Q1",
          "date": "2026-05-06"
        },
        "prior": {
          "period_label": "Q1 FY2025",
          "period_year": 2025,
          "period_qtr": "Q1",
          "date": "2025-05-07"
        }
      },
      "source_coverage": {
        "bi_periods": 22,
        "currencies": [],
        "form_types": [],
        "fx_converted": false,
        "official_periods": 0
      },
      "note": "Summary assessments describe the upstream company window, not the filtered statement rows. Source coverage may count observations beyond the entitled archive. Guidance currency and horizon are not supplied; do not compare it with USD actuals without checking the article."
    }
  },
  "window": {
    "data_through": "2025-03-12"
  },
  "meta": {
    "retrieved_at": "2026-09-24T07:00:50.335260+00:00",
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
**2026-09-24T07:00:50.335438+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_financials.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The electroCore annual-income request returned FY2024 revenue of USD 25,200,000, net income of USD -11,890,000, EBITDA of USD -9,000,000 and EPS -1.59, with news_report provenance. The negative values are preserved. This is an actual populated income example, not independently audited financials. The separate balance-sheet and cash-flow scenario pages are marked blocked because they returned no requested metrics; strict source checks on 2026-09-24 failed on an unreachable financial-store shard.

See the [complete get_financials endpoint reference](../reference/get_financials.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
