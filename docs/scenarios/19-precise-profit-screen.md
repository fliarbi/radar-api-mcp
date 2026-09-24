# Check whether Qualys has positive annual profit and revenue of at least USD 100M in its latest accessible year.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/screen_company_financials.md)

**POST `/v1/companies/financials/screen`** · MCP tool **`screen_company_financials`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 1 matches; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 19-precise-profit-screen -->
```json
{
  "domains": [
    "qualys.com"
  ],
  "constraints": [
    {
      "metric": "net_income",
      "gt": 0
    },
    {
      "metric": "revenue",
      "gte": 100000000
    }
  ],
  "period_type": "annual"
}
```

## Observed result and interpretation

Captured 2026-09-24T07:00:50.401818+00:00; HTTP **200**;
**qualified**, 0.037 seconds.
Local authenticated gateway with live configured read-only sources.

Partial result or source timeout; Coverage is explicitly bounded.

Read all evaluated rows, not just matches. Numeric conditions use the same latest accessible fiscal period. Unknown means missing or disallowed evidence; unavailable means a failed read. Neither becomes zero. This is a bounded candidate screen with source gates, not an exhaustive company database query. Its per-metric checks preserve currency, source type and inclusive/exclusive bounds.

The smaller-company sample uses Qualys and a USD 100M revenue threshold. This deliberately replaces the old Microsoft/USD 1B demonstration; it is not a claim that the old request now matches. Both positive net income and revenue must pass in the same accessible annual period, retaining their metric source types.

The baseline was an unavailable operation registry check (no HTTP request), **unavailable**:
not_implemented. This is an explicit sample replacement, not a before/after repair of an identical request. The original question was: Check whether Microsoft has positive annual profit and revenue above USD 1B in its latest accessible year.

Original baseline request:
```json
{
  "domains": [
    "microsoft.com"
  ],
  "constraints": [
    {
      "metric": "net_income",
      "gt": 0
    },
    {
      "metric": "revenue",
      "gte": 1000000000
    }
  ],
  "period_type": "annual"
}
```
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 19-precise-profit-screen -->
```json
{
  "ok": true,
  "feature": "screen_company_financials",
  "data": {
    "matches": [
      {
        "domain": "qualys.com",
        "company": {
          "domain": "qualys.com"
        },
        "status": "matched",
        "period": {
          "period": "FY2025",
          "fiscal_year": 2025,
          "fiscal_period": "FY",
          "period_end": null,
          "reported_date": "2026-02-05",
          "filed_date": null,
          "form_type": null,
          "metrics": {
            "ebitda": {
              "value": 313400000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "eps": {
              "value": 5.44,
              "currency": null,
              "unit": "per_share",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "net_income": {
              "value": 198300000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "operating_income": {
              "value": 222000000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "revenue": {
              "value": 669100000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            }
          },
          "article_ids": [
            "6986bfd7ca3bd326c77d619c",
            "6991dad740184cd708667115"
          ],
          "currency_conversion": null,
          "evidence": {
            "coverage_count": 2,
            "quality_signals": [
              "Profitable"
            ],
            "headline": "Revenues for 2025 increased by 10% to $669.1 million compared to $607.6 million for 2024.",
            "has_official": false,
            "period_has_official": false
          },
          "operating_context": {
            "employees": null,
            "revenue_growth_pct": 10.0,
            "net_income_growth_pct": 14.0,
            "guidance_revenue": null,
            "beat_or_miss": null
          }
        },
        "checks": [
          {
            "metric": "net_income",
            "status": "matched",
            "value": 198300000,
            "currency": "USD",
            "bounds": {
              "gt": 0.0
            },
            "source_type": "news_report"
          },
          {
            "metric": "revenue",
            "status": "matched",
            "value": 669100000,
            "currency": "USD",
            "bounds": {
              "gte": 100000000.0
            },
            "source_type": "news_report"
          }
        ],
        "access_limited": true,
        "successful_read": true
      }
    ],
    "evaluated": [
      {
        "domain": "qualys.com",
        "company": {
          "domain": "qualys.com"
        },
        "status": "matched",
        "period": {
          "period": "FY2025",
          "fiscal_year": 2025,
          "fiscal_period": "FY",
          "period_end": null,
          "reported_date": "2026-02-05",
          "filed_date": null,
          "form_type": null,
          "metrics": {
            "ebitda": {
              "value": 313400000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "eps": {
              "value": 5.44,
              "currency": null,
              "unit": "per_share",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "net_income": {
              "value": 198300000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "operating_income": {
              "value": 222000000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "revenue": {
              "value": 669100000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            }
          },
          "article_ids": [
            "6986bfd7ca3bd326c77d619c",
            "6991dad740184cd708667115"
          ],
          "currency_conversion": null,
          "evidence": {
            "coverage_count": 2,
            "quality_signals": [
              "Profitable"
            ],
            "headline": "Revenues for 2025 increased by 10% to $669.1 million compared to $607.6 million for 2024.",
            "has_official": false,
            "period_has_official": false
          },
          "operating_context": {
            "employees": null,
            "revenue_growth_pct": 10.0,
            "net_income_growth_pct": 14.0,
            "guidance_revenue": null,
            "beat_or_miss": null
          }
        },
        "checks": [
          {
            "metric": "net_income",
            "status": "matched",
            "value": 198300000,
            "currency": "USD",
            "bounds": {
              "gt": 0.0
            },
            "source_type": "news_report"
          },
          {
            "metric": "revenue",
            "status": "matched",
            "value": 669100000,
            "currency": "USD",
            "bounds": {
              "gte": 100000000.0
            },
            "source_type": "news_report"
          }
        ],
        "access_limited": true,
        "successful_read": true
      }
    ],
    "counts": {
      "matched": 1
    },
    "constraints": [
      {
        "metric": "net_income",
        "gt": 0.0
      },
      {
        "metric": "revenue",
        "gte": 100000000.0
      }
    ],
    "period_type": "annual",
    "source_type": "any",
    "discovery": null,
    "next_page": null,
    "coverage": {
      "complete": false,
      "partial": true,
      "candidate_count": 1,
      "company_filters_independently_verified": false,
      "note": "Numeric matches are verified against returned dated metrics. Candidate company classification/geography remains source-filtered; inspect source access and matching. Empty matches do not mean there are no matching companies elsewhere."
    },
    "successful_financial_reads": 1
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-24T07:00:50.401647+00:00",
    "partial": true,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/19-precise-profit-screen.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
