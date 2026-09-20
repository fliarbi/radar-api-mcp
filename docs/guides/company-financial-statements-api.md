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
