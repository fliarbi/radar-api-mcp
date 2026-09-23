# Company financial statements API: income, balance sheet and cash flow

Use Radar's financial statements API to select a statement family and reporting
period for an identified company. It returns available statement metrics from
Radar's financial history, with source and currency information retained. It does
not fabricate complete statements from incomplete records.

The shared endpoint is `POST /v1/companies/financials`; the MCP tool is
`get_financials`. `statement` accepts `all`, `income`, `balance_sheet` or
`cash_flow`. `period_type` accepts `all`, `annual` or `quarterly`.

## Income statement API example

```json
{"domain":"microsoft.com","statement":"income","period_type":"annual","year_from":2022,"year_to":2025,"limit":20}
```

Use returned revenue and earnings metrics only when present. Keep each metric's
`source_type`: a reported earnings value extracted from news has a different
provenance from a filing-derived figure, even when both describe the same year.

## Balance sheet API example

```json
{"domain":"microsoft.com","statement":"balance_sheet","period_type":"quarterly","limit":12}
```

Read assets, liabilities or equity metrics as figures tied to their returned
period context. The gateway does not reconstruct Radar's separately gated
balance-sheet summary, and a missing metric does not imply a zero balance.

## Cash-flow statement API example

```json
{"domain":"microsoft.com","statement":"cash_flow","period_type":"annual","limit":10}
```

Available operating, investing or financing cash-flow metrics remain separated
from income statement amounts. Preserve negative signs. Do not treat revenue,
net income and operating cash flow as interchangeable measures.

## Fiscal periods, history depth and missing rows

`year_from` and `year_to` filter source fiscal years, and the start year must not
exceed the end year. Requested `limit` is between 1 and 100. An annual query can
return no periods if the account's accessible history contains only quarters.
Check `access_limited` and the archive count before interpreting that result.

The reporting date, filing date and period end describe different events. Use an
exact period end only if supplied; do not substitute the article publication date.
For a multi-company comparison, align fiscal periods deliberately instead of
joining rows by a similar-looking year label.

This guide covers statement retrieval mechanics. The [financial data guide](financial-data-api.md)
explains metric provenance, units, currencies and evidence. Also see
[competitor comparisons](competitor-intelligence-api.md) and [financial news](financial-news-api.md).

<!-- captured-workflow -->
## Keep statement families separate in a financial model

Income statements describe activity over a reporting period; balance-sheet values
describe a position at a point in time; cash-flow values describe movements over
a period. Label these families in a table even when a single API response contains
all three. Adding total assets to quarterly revenue does not produce a meaningful
company-size metric, and adding successive balance-sheet snapshots double-counts
the same stock of assets.

Use `statement=income`, `balance_sheet` or `cash_flow` to request the relevant
family, and retain the returned fiscal label alongside each metric. Annual and
quarterly filters reduce the source records that are exposed; they do not create
missing annual statements by adding quarters. A missing quarterly figure can
reflect inaccessible history, a missing source metric or an absent period.

The capture below used the default all-statements, all-period-types request with
`limit=2`. It is not a separately executed example of each of the three filter
requests above. The current entitled response has income metrics; balance-sheet
and cash-flow metrics are not supplied. Before comparing companies, inspect
available dates and currencies; leave unmatched fiscal periods separate until you
have enough evidence to align them.

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
        "filed_date": null,
        "form_type": null,
        "metrics": {
          "eps": {
            "value": 4.27,
            "currency": null,
            "unit": "per_share",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "net_income": {
            "value": 31800000000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "operating_income": {
            "value": 38400000000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "revenue": {
            "value": 82890000000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          }
        },
        "article_ids": [
          "69e99ba475f157062cafcd91",
          "69f87f9d43843dd771ce0936",
          "69f8a61b43843dd771d24172",
          "69f9d902713680636eef61bb"
        ],
        "currency_conversion": null,
        "evidence": {
          "coverage_count": 4,
          "quality_signals": [
            "Beat estimates",
            "Profitable"
          ],
          "has_official": false,
          "period_has_official": false
        },
        "operating_context": {
          "employees": null,
          "revenue_growth_pct": 18.0,
          "net_income_growth_pct": 23.0,
          "guidance_revenue": 81296200000,
          "beat_or_miss": "Beat"
        }
      },
      {
        "period": "Q2 FY2026",
        "fiscal_year": 2026,
        "fiscal_period": "Q2",
        "period_end": null,
        "reported_date": "2025-12-31",
        "filed_date": null,
        "form_type": null,
        "metrics": {
          "eps": {
            "value": 5.16,
            "currency": null,
            "unit": "per_share",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "operating_income": {
            "value": 38300000000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "revenue": {
            "value": 77670000000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
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
        "currency_conversion": null,
        "evidence": {
          "coverage_count": 8,
          "quality_signals": [
            "Beat estimates"
          ],
          "headline": "The Zacks Consensus Estimate for revenues is pegged at $80.23 billion, indicating growth of 15.22% from the figure reported in the year-ago quarter.",
          "has_official": false,
          "period_has_official": false
        },
        "operating_context": {
          "employees": null,
          "revenue_growth_pct": 15.22,
          "net_income_growth_pct": 20.12,
          "guidance_revenue": 80230000000,
          "beat_or_miss": "Beat"
        }
      }
    ],
    "returned": 2,
    "truncated": true,
    "access_limited": true,
    "available_period_count": 20,
    "coverage": {
      "accessible_periods_before_filters": 3,
      "matching_periods": 3,
      "returned_periods_with_metrics": 2,
      "requested_metrics": [
        "capex",
        "cash",
        "ebitda",
        "eps",
        "financing_cash_flow",
        "free_cash_flow",
        "gross_profit",
        "investing_cash_flow",
        "long_term_debt",
        "net_income",
        "operating_cash_flow",
        "operating_income",
        "revenue",
        "stockholders_equity",
        "total_assets",
        "total_liabilities"
      ],
      "note": "Only entitled upstream periods are evaluated. A period can lack metrics for the selected statement; missing is not zero. Growth, guidance and evidence are source observations, not independently verified forecasts."
    },
    "computed_at": "2026-09-23T03:22:51.284000Z",
    "summary": {
      "narrative": "Latest reported Q3 FY2026: revenue $82.89B, net income $31.8B, EPS $4.27. YoY +34.0% (1.34× prior period). Growth has been erratic across reported periods. Recent signals: Raised guidance, Beat estimates, Profitable.",
      "assessment": {
        "score": 77,
        "growth_consistency": 22,
        "yoy_pct": 34.0,
        "yoy_multiple": 1.34,
        "yoy_basis": "numeric",
        "quality_signals_aggregate": [
          "Raised guidance",
          "Beat estimates",
          "Profitable"
        ]
      },
      "comparison_periods": {
        "latest": {
          "period_label": "Q3 FY2026",
          "period_year": 2026,
          "period_qtr": "Q3",
          "date": "2026-04-29"
        },
        "prior": {
          "period_label": "Q3 FY2025",
          "period_year": 2025,
          "period_qtr": "Q3",
          "date": "2025-03-31"
        }
      },
      "source_coverage": {
        "bi_periods": 108,
        "currencies": [],
        "form_types": [],
        "fx_converted": false,
        "official_periods": 0
      },
      "note": "Summary assessments describe the upstream company window, not the filtered statement rows. Source coverage may count observations beyond the entitled archive. Guidance currency and horizon are not supplied; do not compare it with USD actuals without checking the article."
    }
  },
  "window": {
    "data_through": "2026-04-29"
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:28.432729+00:00",
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

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:28.432907+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_financials.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The captured request returned two periods from an archive count of twenty, with access_limited=true. Its first period was Q3 FY2026 and its revenue metric carried source_type=news_report. The exact period end, filing date and EPS currency were null. Four associated reports and 18% recorded revenue growth accompany its first period. These are source-response examples, not an independent audit of Microsoft's financial results.

See the [complete get_financials endpoint reference](../reference/get_financials.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
