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
{"domain":"electrocore.com","statement":"income","period_type":"annual","year_from":2024,"year_to":2024,"limit":3}
```

Use returned revenue and earnings metrics only when present. Keep each metric's
`source_type`: a reported earnings value extracted from news has a different
provenance from a filing-derived figure, even when both describe the same year.

## Balance sheet request: currently blocked

```json
{"domain":"electrocore.com","statement":"balance_sheet","period_type":"annual","year_from":2024,"year_to":2024,"limit":3}
```

**This executed request returned no numeric balance-sheet metrics.** See
[scenario 13](../scenarios/13-balance-sheet.md) for the source-failure diagnosis
and complete response. It is not a working balance-sheet demonstration.

Read assets, liabilities or equity metrics as figures tied to their returned
period context. The gateway does not reconstruct Radar's separately gated
balance-sheet summary, and a missing metric does not imply a zero balance.

## Cash-flow request: currently blocked

```json
{"domain":"electrocore.com","statement":"cash_flow","period_type":"annual","year_from":2024,"year_to":2024,"limit":3}
```

**This executed request returned no numeric cash-flow metrics.** See
[scenario 15](../scenarios/15-annual-cash-flow.md). A filing-store connection failure
remains unresolved; income metrics do not substitute for cash flows.

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

The capture below explicitly selects electroCore annual income for FY2024. It is
a populated income example, not a demonstration of every statement family. The
separate [balance-sheet](../scenarios/13-balance-sheet.md) and
[cash-flow](../scenarios/15-annual-cash-flow.md) samples are marked blocked: they
returned fiscal labels without requested numeric metrics during a financial-store
connection failure. They need a fresh successful capture after source repair.
Before comparing companies, inspect dates and currencies; leave unmatched fiscal
periods separate until there is enough evidence to align them.

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
