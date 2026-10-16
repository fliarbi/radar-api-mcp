# Retrieve electroCore’s latest accessible quarterly income periods.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/get_financials.md)

**POST `/v1/companies/financials`** · MCP tool **`get_financials`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 2 periods with numeric metrics in the requested statement family.

## Exact executed request

<!-- scenario-request: 16-quarterly-income -->
```json
{
  "domain": "electrocore.com",
  "statement": "income",
  "period_type": "quarterly",
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-24T07:00:50.364210+00:00; HTTP **200**;
**qualified**, 0.016 seconds.
Local authenticated gateway with live configured read-only sources.

Financial history is source-plan limited.

Preserve fiscal year, fiscal period, statement family, source type and available dates. Empty annual rows with access_limited do not prove the archive has no annual statements. No annual values are synthesized by adding quarters, and a filing date is not substituted for an absent period end.

The baseline was HTTP 200, **qualified**:
Financial history is source-plan limited. This is an explicit sample replacement, not a before/after repair of an identical request. The original question was: Retrieve Microsoft’s three latest accessible quarterly income periods.

Original baseline request:
```json
{
  "domain": "microsoft.com",
  "statement": "income",
  "period_type": "quarterly",
  "limit": 3
}
```
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 16-quarterly-income -->
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
        "period": "Q1 FY2026",
        "fiscal_year": 2026,
        "fiscal_period": "Q1",
        "period_end": null,
        "reported_date": "2026-05-06",
        "filed_date": null,
        "form_type": null,
        "metrics": {
          "eps": {
            "value": -0.59,
            "currency": null,
            "unit": "per_share",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "revenue": {
            "value": 9012000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          }
        },
        "article_ids": [
          "69f9d40c7b2d589e844a9b55"
        ],
        "currency_conversion": null,
        "evidence": {
          "coverage_count": 1,
          "quality_signals": [],
          "has_official": false,
          "period_has_official": false
        },
        "operating_context": {
          "employees": null,
          "revenue_growth_pct": null,
          "net_income_growth_pct": null,
          "guidance_revenue": 9012000,
          "beat_or_miss": null
        }
      },
      {
        "period": "Q1 FY2025",
        "fiscal_year": 2025,
        "fiscal_period": "Q1",
        "period_end": null,
        "reported_date": "2025-05-07",
        "filed_date": null,
        "form_type": null,
        "metrics": {
          "eps": {
            "value": -0.47,
            "currency": null,
            "unit": "per_share",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "revenue": {
            "value": 6720000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          }
        },
        "article_ids": [
          "68640fb68882abb7e3c0cd10"
        ],
        "currency_conversion": null,
        "evidence": {
          "coverage_count": 1,
          "quality_signals": [
            "Beat estimates"
          ],
          "has_official": false,
          "period_has_official": false
        },
        "operating_context": {
          "employees": null,
          "revenue_growth_pct": null,
          "net_income_growth_pct": null,
          "guidance_revenue": 7620000,
          "beat_or_miss": "Beat"
        }
      }
    ],
    "returned": 2,
    "truncated": false,
    "access_limited": true,
    "available_period_count": 20,
    "coverage": {
      "accessible_periods_before_filters": 3,
      "matching_periods": 2,
      "returned_periods_with_metrics": 2,
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
    "data_through": "2026-05-06"
  },
  "meta": {
    "retrieved_at": "2026-09-24T07:00:50.364052+00:00",
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

[Download the current and baseline JSON](../examples/scenarios/16-quarterly-income.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
