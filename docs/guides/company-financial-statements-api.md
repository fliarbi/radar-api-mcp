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
requests above. It shows actual income, balance-sheet and cash-flow metrics in one
response, with a source label per metric. Before comparing companies, inspect
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
        "filed_date": "2026-04-29",
        "form_type": "10-Q",
        "metrics": {
          "eps": {
            "value": 4.27,
            "currency": null,
            "unit": "per_share",
            "source_type": "filing",
            "native_value": 4.27,
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
          "revenue": {
            "value": 82886000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 82886000000.0,
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
          "69f87f9d43843dd771ce0936"
        ],
        "currency_conversion": "native_usd"
      }
    ],
    "returned": 2,
    "truncated": true,
    "access_limited": true,
    "available_period_count": 20,
    "computed_at": "2026-09-19T17:19:34.120000Z"
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

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_financials.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The captured request returned two periods from an archive count of twenty, with access_limited=true. Its first period was Q3 FY2026 and its revenue metric carried source_type=filing. The exact period end was null, while EPS currency was also null despite a supplied native currency. These are source-response examples, not an independent audit of Microsoft's financial results.

See the [complete get_financials endpoint reference](../reference/get_financials.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
