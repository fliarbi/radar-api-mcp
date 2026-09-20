# Company funding API: reported rounds, amounts and investors

[All endpoints](README.md) · [Workflow guide](../guides/startup-funding-data-api.md)

Retrieve reported company funding rounds and associated investor information. The endpoint is designed for a fundraising-history section or a research drilldown from company discovery. It does not represent a capitalization table, audited capital receipts or confirmed current ownership percentages.

## Route, authentication and credits

**`POST /v1/companies/funding`** · MCP tool **`get_company_funding`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/funding" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"openai.com"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_funding -->
```json
{
  "name": "get_company_funding",
  "arguments": {
    "request": {
      "domain": "openai.com"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_company_funding -->
```json
{
  "ok": true,
  "feature": "get_company_funding",
  "data": {
    "amount_approx": true,
    "investors": [
      {
        "current_investment": [
          "Funding round",
          2025
        ],
        "domain": "microsoft.com",
        "company_id": 335807,
        "name": "microsoft",
        "slug": "microsoft-corporation"
      },
      {
        "current_investment": [
          "Funding round",
          2025
        ],
        "domain": "thrivecap.com",
        "company_id": 1030626,
        "name": "thrive capital",
        "slug": "thrive-capital"
      }
    ],
    "rounds": [
      {
        "amount": 41000000000,
        "date": "2025-01-28",
        "investors": [
          {
            "name": "microsoft",
            "domain": "microsoft.com"
          },
          {
            "name": "thrive capital",
            "domain": "thrivecap.com"
          }
        ],
        "name": "Funding round"
      },
      {
        "amount": 6600000000,
        "date": "2024-03-10",
        "investors": [
          {
            "name": "thrive capital",
            "domain": "thrivecap.com"
          },
          {
            "name": "g42",
            "domain": "g42.ai"
          }
        ],
        "name": "Funding round"
      }
    ]
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:46.218682+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_funding.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The OpenAI capture contained ten round records and amount_approx=true. Its source announcement text and structured investor associations were not fully reconciled: one announcement referred to SoftBank while a structured association named Microsoft. The excerpt retains numerical and identity fields but omits long announcement text. Review the source before treating a particular association as confirmed participation.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.rounds` | Reported financing entries with a name, date, amount and investor associations when available. |
| `data.amount_approx` | A source qualifier that must travel with displayed amounts. |
| `data.investors` | Company-level investor records, not automatically participants in every round. |
| `data.stages` | Source stage summaries; avoid adding these to individual rounds as if they were separate transactions. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Review round dates, labels and amount_approx together. Compare reported investors with the underlying announcement when available through News. Keep debt, equity, valuation, cumulative funding and individual round amounts separate in your own data model.

Several reports can describe the same transaction. Summing every round, stage summary and announcement together can double-count capital; a funding amount is not automatically a valuation.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/startup-funding-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
