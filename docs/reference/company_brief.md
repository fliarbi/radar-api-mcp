# Company brief API: profile, financials, funding, events and news

[All endpoints](README.md) · [Workflow guide](../guides/b2b-data-api.md)

Assemble a company's research sections through one bounded operation. A brief combines profile, financials, intelligence, events, funding and enrichment, with optional associated news. Each section retains its own response envelope so its date, access and coverage can be interpreted independently.

## Route, authentication and credits

**`POST /v1/companies/brief`** · MCP tool **`company_brief`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs six credits without News, seven with News; failed sections are refunded. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |
| `include_news` | default `true` | boolean |
| `news_limit` | default `10` | integer; minimum: `1`; maximum: `100` |
| `event_days` | default `365` | integer; minimum: `1`; maximum: `1095` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/brief" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com","include_news":true,"news_limit":2,"event_days":30}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: company_brief -->
```json
{
  "name": "company_brief",
  "arguments": {
    "request": {
      "domain": "microsoft.com",
      "include_news": true,
      "news_limit": 2,
      "event_days": 30
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: company_brief -->
```json
{
  "ok": true,
  "feature": "company_brief",
  "data": {
    "domain": "microsoft.com",
    "sections": {
      "profile": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company",
          "data": {
            "company": {
              "location": {
                "c": "united states",
                "cc": "",
                "coord": [
                  -122.12151,
                  47.67399
                ],
                "g": "47.67399,-122.12151",
                "hq": "redmond",
                "l": "redmond",
                "lc": "redmond, washington, united states",
                "rg": "washington"
              },
              "size": "",
              "founded": "2003",
              "company_id": "58edbbfde4b053044e6a387d",
              "name": "Microsoft Dynamics CRM",
              "domain": "microsoft.com"
            },
            "access": {
              "anonymous": true,
              "plan": "free",
              "results_per_query": 50,
              "searches_per_month": 50
            },
            "extras_gated": true
          },
          "window": {
            "data_through": null
          },
          "meta": {
            "retrieved_at": "2026-09-20T04:58:46.348256+00:00",
            "partial": false,
            "notes": [],
            "provider": "Fliar BI"
          }
        }
      },
      "financials": {
        "available": true,
        "result": {
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
            "returned": 3,
            "truncated": false,
            "access_limited": true,
            "available_period_count": 20,
            "computed_at": "2026-09-19T17:19:34.120000Z"
          },
          "window": {
            "data_through": "2026-04-29"
          },
          "meta": {
            "retrieved_at": "2026-09-20T04:58:46.322281+00:00",
            "partial": false,
            "notes": [
              "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
              "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies."
            ],
            "provider": "Fliar BI"
          }
        }
      },
      "news": {
        "available": false,
        "error": {
          "kind": "service_unavailable",
          "message": "This data service is not connected to the private preview"
        }
      }
    },
    "partial": true
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:46.487748+00:00",
    "partial": true,
    "notes": [
      "Each section retains its own date window and access limits. Missing data is not zero."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/company_brief.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The live Microsoft brief returned six available Radar sections and an unavailable News section with service_unavailable. The overall HTTP status was 200 and partial=true. The excerpt includes profile, financials and the news failure; other successful sections are intentionally omitted for readability.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.sections.<name>.available` | Whether that section supplied available data. |
| `data.sections.<name>.result` | The section's own envelope, including its source window and notes. |
| `data.sections.<name>.error` | A specific unavailable-section error, rather than invented empty data. |
| `data.partial / meta.partial` | At least one requested section was unavailable or partial. |
| `meta.billing` | In account mode, actual charged credits after failed-section refunds. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Use a reviewed company domain. Set include_news=false if you only need Radar data; otherwise connect News first. Render each requested section with its available flag, result or error. Preserve the top-level partial flag instead of failing the entire research page when one optional section is unavailable.

A partial brief is not a uniform snapshot. Financial, digital, profile and news sections may have different timestamps or disagree about entity labels; retain those distinctions.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/b2b-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
