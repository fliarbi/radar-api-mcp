# Company listing columns API: selected company data points

[All endpoints](README.md) · [Workflow guide](../guides/company-search-api.md)

Select up to fourteen listing columns for up to twenty visible company domains. This matches Radar’s Show columns workflow: search cards first, chosen data points in a separate request.

## Route, authentication and credits

**`POST /v1/companies/columns`** · MCP tool **`get_company_columns`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domains` | required | array of string; min items: `1`; max items: `20` |
| `columns` | required | array of string; min items: `1`; max items: `14`; one of `founded_year`, `employees`, `total_funding`, `latest_revenue`, `valuation`, `financing_rounds`, `growth_stage`, `funding_stage`, `web_presence`, `mobile_downloads`, `mobile_growth`, `revenue_model`, `business_model`, `industry`, `country`, `ownership` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

`RADAR_API_URL` is `https://radar-api.fliarbi.com` (the [installer](../../README.md#install-in-one-line) sets it);
load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/columns" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domains":["razorpay.com","stripe.com"],"columns":["employees","total_funding","latest_revenue","web_presence","mobile_downloads"]}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_columns -->
```json
{
  "name": "get_company_columns",
  "arguments": {
    "request": {
      "domains": [
        "razorpay.com",
        "stripe.com"
      ],
      "columns": [
        "employees",
        "total_funding",
        "latest_revenue",
        "web_presence",
        "mobile_downloads"
      ]
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_company_columns -->
```json
{
  "ok": true,
  "feature": "get_company_columns",
  "data": {
    "companies": [
      {
        "domain": "razorpay.com",
        "columns": {
          "employees": null,
          "total_funding": null,
          "latest_revenue": {
            "label": "Revenue",
            "value": "$465.1M"
          },
          "web_presence": {
            "label": "Web Presence",
            "value": "91/100"
          },
          "mobile_downloads": {
            "label": "App Downloads",
            "value": "3.8M"
          }
        },
        "status": "available"
      },
      {
        "domain": "stripe.com",
        "columns": {
          "employees": null,
          "total_funding": null,
          "latest_revenue": null,
          "web_presence": {
            "label": "Web Presence",
            "value": "86/100"
          },
          "mobile_downloads": {
            "label": "App Downloads",
            "value": "3.0M"
          }
        },
        "status": "available"
      }
    ],
    "note": "Radar display values only. Missing values may be suppressed zero/negative values or source failure; use get_financials for precise values and provenance."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:27.822118+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:27.822273+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_columns.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live Razorpay/Stripe request returned the selected employee, funding, revenue, web-presence and app-download display columns, with missing values retained as null.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.companies[].columns` | Only requested column names; source display label/value pairs or null. |
| `data.companies[].status` | available if the source supplied columns; otherwise unknown. |
| `data.note` | Display values are rounded and may suppress zero/negative values; use financials for precise evidence. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Inspect the request schema and returned coverage; use the related discovery response before selecting an identifier or field. Preserve access errors and unknown values in your application.

A successful HTTP response does not independently establish current accuracy or complete coverage. Contact access checks and source plan limits remain authoritative.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-search-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
