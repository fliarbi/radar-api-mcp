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

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.periods[].period / fiscal_year / fiscal_period` | Source fiscal labels, not necessarily calendar-year labels. |
| `data.periods[].period_end / reported_date / filed_date` | Different date meanings. An unknown period end remains null. |
| `data.periods[].metrics.*` | value, currency, unit, source_type, native_value and native_currency. |
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
