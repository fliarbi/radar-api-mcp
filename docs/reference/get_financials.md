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
  -d '{"domain":"electrocore.com","statement":"income","period_type":"annual","year_from":2024,"year_to":2024,"limit":3}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_financials -->
```json
{
  "name": "get_financials",
  "arguments": {
    "request": {
      "domain": "electrocore.com",
      "statement": "income",
      "period_type": "annual",
      "year_from": 2024,
      "year_to": 2024,
      "limit": 3
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
