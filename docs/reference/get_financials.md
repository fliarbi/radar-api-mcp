# Financial data API: company statements with fiscal periods and sources

[All endpoints](README.md) · [Workflow guide](../guides/financial-data-api.md)

Retrieve available income-statement, balance-sheet and cash-flow metrics in one normalized period model. Each numerical metric retains currency, unit, original-currency information where supplied, and a source type. This is useful for a financial research table that must explain what each number represents.

## Route, authentication and credits

**`POST /v1/companies/financials`** · MCP tool **`get_financials`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |
| `statement` | default `"all"` | string; one of `all`, `income`, `balance_sheet`, `cash_flow` |
| `period_type` | default `"all"` | string; one of `all`, `annual`, `quarterly` |
| `year_from` | default `null` | integer or null; minimum: `1900`; maximum: `2100` |
| `year_to` | default `null` | integer or null; minimum: `1900`; maximum: `2100` |
| `limit` | default `40` | integer; minimum: `1`; maximum: `100` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/financials" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com","limit":2}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_financials -->
```json
{
  "name": "get_financials",
  "arguments": {
    "request": {
      "domain": "microsoft.com",
      "limit": 2
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

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

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.periods[].period / fiscal_year / fiscal_period` | Source fiscal labels, not necessarily calendar-year labels. |
| `data.periods[].period_end / reported_date / filed_date` | Different date meanings. An unknown period end remains null. |
| `data.periods[].metrics.*` | value, currency, unit, source_type, native_value and native_currency. |
| `data.periods[].evidence / operating_context` | Article counts, source quality flags and income-specific headcount, growth and guidance. Guidance currency/horizon can be unknown. |
| `data.summary.assessment / comparison_periods / source_coverage` | Upstream company-window context, independent of the request filters. Not additional accessible archive rows. |
| `data.coverage` | Accessible, matching and metric-bearing period counts; statement metrics requested. |
| `data.access_limited / available_period_count` | A larger known archive may exist beyond the linked account's view. |
| `data.returned / truncated` | The response limit and account gates can both reduce visible history. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Choose statement and annual/quarterly filters, inspect the accessible periods, and display every value with its currency and fiscal label. Follow article_ids only through an authorized News connection. Align actual fiscal dates before making a cross-company comparison; do not substitute reporting date for period_end.

Missing metrics are omitted; zero and negative values are real values and must be retained. Do not invent filing URLs, calculate FX conversions from guessed rates, or assume that available_period_count equals accessible rows.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/financial-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
