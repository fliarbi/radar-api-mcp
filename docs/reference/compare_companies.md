# Company comparison API: profiles, financials and intelligence

[All endpoints](README.md) · [Workflow guide](../guides/competitor-intelligence-api.md)

Retrieve comparable research sections for two to five selected company domains. The response organizes each company's profile, financials and intelligence separately. It does not normalize fiscal calendars, compute a combined valuation or rank investment opportunities.

## Route, authentication and credits

**`POST /v1/companies/compare`** · MCP tool **`compare_companies`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs three credits per company; failed sections are refunded. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domains` | required | array of string; min items: `2`; max items: `5` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/compare" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domains":["microsoft.com","salesforce.com"]}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: compare_companies -->
```json
{
  "name": "compare_companies",
  "arguments": {
    "request": {
      "domains": [
        "microsoft.com",
        "salesforce.com"
      ]
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: compare_companies -->
```json
{
  "ok": true,
  "feature": "compare_companies",
  "data": {
    "companies": [
      {
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
                "retrieved_at": "2026-09-20T04:58:46.551598+00:00",
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
                "retrieved_at": "2026-09-20T04:58:46.537800+00:00",
                "partial": false,
                "notes": [
                  "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
                  "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies."
                ],
                "provider": "Fliar BI"
              }
            }
          }
        },
        "partial": false
      },
      {
        "domain": "salesforce.com",
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
                    "cc": "ca",
                    "coord": [
                      -75.69812,
                      45.41117
                    ],
                    "g": "45.41117,-75.69812",
                    "hq": "san francisco",
                    "l": "san francisco",
                    "lc": "san francisco, california, united states",
                    "rg": "california"
                  },
                  "size": "10000+",
                  "founded": "1999",
                  "company_id": "52cbdd3fe4b093852fc32b66",
                  "name": "Salesforce",
                  "domain": "salesforce.com"
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
                "retrieved_at": "2026-09-20T04:58:46.721116+00:00",
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
                "domain": "salesforce.com",
                "statement": "all",
                "has_data": true,
                "periods": [
                  {
                    "period": "Q4 FY2027",
                    "fiscal_year": 2027,
                    "fiscal_period": "Q4",
                    "period_end": null,
                    "reported_date": "2026-02-26",
                    "filed_date": null,
                    "form_type": null,
                    "metrics": {
                      "revenue": {
                        "value": 11200000000,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "news_report",
                        "native_value": null,
                        "native_currency": null
                      }
                    },
                    "article_ids": [
                      "69c9ce02b7c587db32feb03a"
                    ],
                    "currency_conversion": null
                  }
                ],
                "returned": 3,
                "truncated": false,
                "access_limited": true,
                "available_period_count": 20,
                "computed_at": "2026-09-20T04:58:47.067000Z"
              },
              "window": {
                "data_through": "2026-02-26"
              },
              "meta": {
                "retrieved_at": "2026-09-20T04:58:47.074963+00:00",
                "partial": false,
                "notes": [
                  "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
                  "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies."
                ],
                "provider": "Fliar BI"
              }
            }
          }
        },
        "partial": false
      }
    ],
    "partial": false,
    "comparison_note": "Fiscal calendars and available periods differ. No cross-company totals or investment ranking are calculated."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:47.075771+00:00",
    "partial": false,
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
The [downloadable JSON example](../examples/compare_companies.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The live Microsoft/Salesforce comparison returned both companies with their three research sections. The documentation excerpt keeps profile and financial evidence for both and omits larger intelligence sections. It is not evidence that their fiscal quarters cover identical dates.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.companies[].domain` | Which requested company each section set describes. |
| `data.companies[].sections` | Profile, financials and intelligence envelopes for that company. |
| `data.companies[].partial / error` | Company-level gaps can coexist with successful peers. |
| `data.comparison_note` | The response explicitly avoids cross-company totals or ranking. |
| `meta.billing` | Account mode reserves three credits per company and refunds failed sections. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Select companies through search or competitor discovery, verify their identities, and request distinct domains. Build a comparison table from available metrics while retaining period labels, currency and source type. Leave cells unknown when one company lacks a metric or section.

Never convert a missing financial value to zero just to make a comparison table rectangular. An alias in a company profile must be reviewed before attaching a corporate parent's financial history.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/competitor-intelligence-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
