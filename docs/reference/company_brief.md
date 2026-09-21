# Company brief API: compact summaries and detail requests

[All endpoints](README.md) · [Workflow guide](../guides/b2b-data-api.md)

Combine compact profile, financial, intelligence, event, funding, enrichment and news summaries. This endpoint does not embed full rich company records, funding rosters or article bodies. Every successful section includes a separate detail_request so clients can choose the next read.

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
  -d '{"domain":"stripe.com","include_news":true,"news_limit":3,"event_days":30}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: company_brief -->
```json
{
  "name": "company_brief",
  "arguments": {
    "request": {
      "domain": "stripe.com",
      "include_news": true,
      "news_limit": 3,
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
    "domain": "stripe.com",
    "sections": {
      "profile": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company",
          "data": {
            "company": {
              "company_id": "1x532zlgk5",
              "domain": "stripe.com",
              "name": "Stripe",
              "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=stripe.com",
              "description": "Provider of financial infrastructure solutions for revenue growth and payment processing",
              "founded": 2010,
              "employee_count": 5904
            },
            "profile_depth": "summary",
            "available_fields": [
              "overview",
              "classification",
              "people",
              "technology",
              "web_presence",
              "traffic",
              "apps",
              "products",
              "geography",
              "social",
              "lifecycle",
              "legal",
              "assessments",
              "hiring",
              "innovation",
              "activity",
              "reputation",
              "share_of_voice"
            ],
            "field_status": {
              "overview": "available",
              "classification": "available",
              "people": "available",
              "technology": "available",
              "web_presence": "available",
              "traffic": "available",
              "apps": "available",
              "products": "available",
              "geography": "available",
              "social": "available",
              "lifecycle": "available",
              "legal": "available",
              "assessments": "available",
              "hiring": "available",
              "innovation": "available",
              "activity": "available",
              "reputation": "available",
              "share_of_voice": "available"
            },
            "contacts": {
              "availability": {
                "emails": true,
                "phones": true
              },
              "path": "/v1/contacts/company",
              "required_scope": "contacts",
              "access": "linked Radar paid-plan check"
            },
            "field_request": {
              "method": "POST",
              "path": "/v1/companies/field",
              "required": [
                "domain",
                "field"
              ]
            },
            "updated_at": "2026-06-01T04:43:22.775000+00:00",
            "coverage": {
              "partial": false
            },
            "financial_history": "Use get_financials; financial archive and estimated-revenue access remain upstream-controlled"
          },
          "window": {
            "data_through": null
          },
          "meta": {
            "retrieved_at": "2026-09-21T04:09:01.414892+00:00",
            "partial": false,
            "notes": [
              "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
            ],
            "provider": "Fliar BI"
          }
        },
        "detail_request": {
          "method": "POST",
          "path": "/v1/companies/profile"
        }
      },
      "financials": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_financials",
          "data": {
            "domain": "stripe.com",
            "has_data": true,
            "summary": {
              "narrative": "Latest reported FY2024: revenue $500M. Growth has been erratic across reported periods. Recent signals: Reported a loss, Record revenue, Profitable."
            },
            "access_limited": false,
            "available_period_count": 3,
            "computed_at": "2026-09-20T06:35:42.892000Z",
            "latest_period": {
              "period": "FY2024",
              "fiscal_year": 2024,
              "fiscal_period": "FY",
              "period_end": null,
              "reported_date": "2025-02-28",
              "filed_date": null,
              "form_type": null,
              "metrics": {
                "revenue": {
                  "value": 500000000,
                  "currency": "USD",
                  "unit": "absolute",
                  "source_type": "news_report",
                  "native_value": null,
                  "native_currency": null
                }
              },
              "article_ids": [
                "69982217a9a137bc0bdfce10"
              ],
              "currency_conversion": null
            },
            "detail_required_for_history": true
          },
          "window": {
            "data_through": "2025-02-28"
          },
          "meta": {
            "retrieved_at": "2026-09-21T04:09:01.419097+00:00",
            "partial": false,
            "notes": [
              "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
              "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies."
            ],
            "provider": "Fliar BI"
          }
        },
        "detail_request": {
          "method": "POST",
          "path": "/v1/companies/financials"
        }
      },
      "intelligence": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company_intelligence",
          "data": {
            "domain": "stripe.com",
            "computed_at": "2026-09-20T06:35:42.892000Z",
            "assessments": {
              "innovation_index": {
                "score": 12
              },
              "investment_readiness": {
                "score": 55,
                "label": "Moderate"
              },
              "management_quality": {
                "score": 90
              },
              "market_position": {
                "score": 42
              },
              "risk_profile": {
                "score": 0
              }
            },
            "detail_required_for_analysis": true
          },
          "window": {
            "data_through": null
          },
          "meta": {
            "retrieved_at": "2026-09-21T04:09:01.418438+00:00",
            "partial": false,
            "notes": [
              "Scores and narratives are derived assessments. Financial metrics are retrieved evidence."
            ],
            "provider": "Fliar BI"
          }
        },
        "detail_request": {
          "method": "POST",
          "path": "/v1/companies/intelligence"
        }
      },
      "events": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company_events",
          "data": {
            "domain": "stripe.com",
            "freshness": {
              "future_rows_count": 0,
              "future_rows_filtered": false,
              "latest_event_date": "2026-04-15",
              "latest_inserted_at": "2026-09-21T05:30:00+05:30"
            },
            "truncated": true,
            "window_days": 30,
            "totals_by_type": {},
            "returned_event_count": 0,
            "detail_required_for_records": true
          },
          "window": {
            "data_through": "2026-04-15",
            "effective_days": 30,
            "requested_days": 30
          },
          "meta": {
            "retrieved_at": "2026-09-21T04:09:01.603300+00:00",
            "partial": false,
            "notes": [],
            "provider": "Fliar BI"
          }
        },
        "detail_request": {
          "method": "POST",
          "path": "/v1/companies/events"
        }
      },
      "funding": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company_funding",
          "data": {
            "amount_approx": true,
            "stages": {
              "Equity (2023)": 6800000000,
              "Fourth Funding Round (2017)": 150000000,
              "Funding round (2012)": 20000000,
              "Funding round (2014)": 70000000,
              "Funding round (2016)": 150000000,
              "Funding round (2018)": 245000000,
              "Funding round (2019)": 10000000,
              "Funding round (2020)": 600000000,
              "Funding round (2021)": 1000000000,
              "Funding round (Apr 2014)": 120000000,
              "Funding round (Jan 2014)": 80000000,
              "Raise (2021)": 600000000,
              "Seed (2026)": 2000000,
              "Series C (2014)": 80000000,
              "Series G (2020)": 600000000,
              "Series H (2021)": 600000000,
              "Series I (2023)": 6500000000,
              "Series, unspecified (2019)": 250000000,
              "Series?? (2024)": 1800000000
            },
            "returned_round_count": 22,
            "returned_event_count": 10,
            "returned_investor_count": 4,
            "detail_required_for_records": true
          },
          "window": {
            "data_through": null
          },
          "meta": {
            "retrieved_at": "2026-09-21T04:09:01.508777+00:00",
            "partial": false,
            "notes": [],
            "provider": "Fliar BI"
          }
        },
        "detail_request": {
          "method": "POST",
          "path": "/v1/companies/funding"
        }
      },
      "enrichment": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company_enrichment",
          "data": {
            "domain": "stripe.com",
            "has_data": true,
            "available_fields": [
              "activity",
              "digital",
              "hiring",
              "innovation",
              "legal",
              "reputation",
              "social",
              "sov"
            ],
            "detail_required": true
          },
          "window": {
            "data_through": null
          },
          "meta": {
            "retrieved_at": "2026-09-21T04:09:01.421225+00:00",
            "partial": false,
            "notes": [
              "Absent enrichment sections have unknown coverage; the source does not distinguish missing data from a failed section."
            ],
            "provider": "Fliar BI"
          }
        },
        "detail_request": {
          "method": "POST",
          "path": "/v1/companies/enrichment"
        }
      },
      "news": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "search_business_news",
          "data": {
            "items": [
              {
                "id": "69e84c0f9baafc73566e4cdb",
                "headline": "Fintech SolvaPay raises €2.4M from Redstone for guardrails on AI agent transactions — TFN",
                "url": "https://techfundingnews.com/solvapay-2-4m-redstone-ai-agent-payments/",
                "published_at": "2026-04-15T08:00:00"
              },
              {
                "id": "69e8d0f45cfa3e5ba541a5e5",
                "headline": "Stripe powers Mercor’s expert marketplace for advancing AI models",
                "url": "https://globalfintechseries.com/finance/stripe-powers-mercors-expert-marketplace-for-advancing-ai-models/",
                "published_at": "2026-04-14T15:02:32"
              },
              {
                "id": "69e50227430a4927fdc4740c",
                "headline": "Stripe appoints Manish Maheshwari to lead Revenue and Growth in India - Exchange4media",
                "url": "https://www.exchange4media.com/digital-news/stripe-appoints-manish-maheshwari-to-lead-revenue-and-growth-in-india-153659.html",
                "published_at": "2026-04-08T17:06:57"
              }
            ],
            "detail_required_for_full_articles": true
          },
          "window": {
            "since": "2026-02-04",
            "until": "2026-05-05",
            "days": 91,
            "data_through": "2026-08-24",
            "freshness": "volume thins after 2026-05; the last months are partial"
          },
          "meta": {
            "retrieved_at": "2026-09-21T04:09:01.844635+00:00",
            "partial": false,
            "notes": [
              "company-linked news is available through 2026-05-05; the window was defaulted to end there — pass `until` to override"
            ],
            "provider": "Fliar BI",
            "coverage": {
              "available": true
            }
          }
        },
        "detail_request": {
          "method": "POST",
          "path": "/v1/news/business"
        }
      }
    },
    "partial": false
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T04:09:01.844736+00:00",
    "partial": false,
    "notes": [
      "Each section retains its own date window and access limits. Missing data is not zero."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-21T04:09:01.845017+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/company_brief.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

**Capture method:** Executed authenticated local Radar gateway and actual Prism News application code against live data; isolated test identity and quota dependencies, with the News Free plan's data limits retained. No deployed News URL, production News-key authentication or customer billing was verified. Radar sections use the existing live HTTP service with anonymous access and the configured detailed profile store.

The refreshed Stripe brief uses real Radar data and the documented isolated News integration identity. It returns summaries for seven available sections and short linked headlines; it does not establish a deployed News connection. The source Tracxn logo URL is no longer exposed.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.sections.*.available` | Whether the source section supplied data. Empty recent-event windows can still be available. |
| `data.sections.*.result` | A compact summary with the original section window, source metadata and partial flag. |
| `data.sections.*.detail_request` | Method, path and JSON body for a separate read. |
| `data.sections.profile.result.data.available_fields` | Observed company fields to request individually. |
| `data.partial` | True if a section failed or has partial coverage. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Review the compact identity and latest financial period, inspect section availability and dates, then call only the detail endpoint required for your workflow. Use the profile available_fields list to retrieve a single field.

Financial periods and source windows differ between sections. Summaries are not a complete company archive; follow the detail request and its access limits.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/b2b-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
