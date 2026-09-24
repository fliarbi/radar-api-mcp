# Check electroCore FY2024 balance-sheet coverage for assets, liabilities and equity.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/get_financials.md)

**POST `/v1/companies/financials`** · MCP tool **`get_financials`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Coverage or failure example — no populated requested result.** 0 periods with numeric metrics in the requested statement family.

## Exact executed request

<!-- scenario-request: 13-balance-sheet -->
```json
{
  "domain": "electrocore.com",
  "statement": "balance_sheet",
  "period_type": "annual",
  "year_from": 2024,
  "year_to": 2024,
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-24T07:00:50.347960+00:00; HTTP **200**;
**qualified**, 0.053 seconds.
Local authenticated gateway with live configured read-only sources.

Empty documentation example: 0 periods with numeric metrics in the requested statement family; Financial history is source-plan limited.

Preserve fiscal year, fiscal period, statement family, source type and available dates. Empty annual rows with access_limited do not prove the archive has no annual statements. No annual values are synthesized by adding quarters, and a filing date is not substituted for an absent period end.

**Blocked worked example, not a populated balance sheet.** electroCore replaces the Microsoft sample, but no numeric balance-sheet metrics were returned. On 2026-09-24, strict read-only checks of both the financial filings and company-resolution stores failed on an unreachable shard. The gateway's upstream currently falls back to news-derived income data, so HTTP 200 and a fiscal-period label do not prove a balance sheet is available. No internal archive or account gate was bypassed. For a populated annual statement, see [electroCore income](14-annual-income.md); it does not establish balance-sheet coverage. This page must be recaptured after the source connection is repaired before being used as a successful balance-sheet demonstration.

The baseline was HTTP 200, **qualified**:
Empty documentation example: 0 periods with numeric metrics in the requested statement family; Financial history is source-plan limited; No rows observed; not proof of a complete negative; No accessible data. This is an explicit sample replacement, not a before/after repair of an identical request. The original question was: Retrieve Microsoft annual assets, liabilities and equity for 2024–2026.

Original baseline request:
```json
{
  "domain": "microsoft.com",
  "statement": "balance_sheet",
  "period_type": "annual",
  "year_from": 2024,
  "year_to": 2026,
  "limit": 3
}
```
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 13-balance-sheet -->
```json
{
  "ok": true,
  "feature": "get_financials",
  "data": {
    "domain": "electrocore.com",
    "statement": "balance_sheet",
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
        "metrics": {},
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
      "returned_periods_with_metrics": 0,
      "requested_metrics": [
        "cash",
        "long_term_debt",
        "stockholders_equity",
        "total_assets",
        "total_liabilities"
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
    "retrieved_at": "2026-09-24T07:00:50.347809+00:00",
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

[Download the current and baseline JSON](../examples/scenarios/13-balance-sheet.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
