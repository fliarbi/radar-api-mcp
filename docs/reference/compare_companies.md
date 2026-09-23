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
  -d '{"domains":["razorpay.com","stripe.com"]}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: compare_companies -->
```json
{
  "name": "compare_companies",
  "arguments": {
    "request": {
      "domains": [
        "razorpay.com",
        "stripe.com"
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
        "domain": "razorpay.com",
        "sections": {
          "profile": {
            "available": true,
            "result": {
              "ok": true,
              "feature": "get_company",
              "data": {
                "company": {
                  "company_id": "2gowls1wmc",
                  "domain": "razorpay.com",
                  "name": "Razorpay",
                  "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=razorpay.com",
                  "description": "Provider of payment and business banking solutions for enterprises",
                  "founded": 2014,
                  "employee_count": 1952
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
                  "innovation": "not_observed",
                  "activity": "not_observed",
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
                "retrieved_at": "2026-09-23T06:47:54.822666+00:00",
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
                "domain": "razorpay.com",
                "has_data": true,
                "summary": {
                  "narrative": "Latest reported FY2025: revenue $453.96M, net income $—. YoY +82.9% (1.83× prior period). Recent signals: Reported a loss, Record revenue, Profitable.",
                  "assessment": {
                    "score": 78,
                    "growth_consistency": 50,
                    "yoy_pct": 82.9,
                    "yoy_multiple": 1.83,
                    "yoy_basis": "numeric",
                    "quality_signals_aggregate": [
                      "Reported a loss",
                      "Record revenue",
                      "Profitable"
                    ]
                  },
                  "comparison_periods": {
                    "latest": {
                      "period_label": "FY2025",
                      "period_year": 2025,
                      "period_qtr": "FY",
                      "date": "2025-10-16"
                    },
                    "prior": {
                      "period_label": "FY2024",
                      "period_year": 2024,
                      "period_qtr": "FY",
                      "date": "2024-10-29"
                    }
                  },
                  "source_coverage": {
                    "bi_periods": 7,
                    "currencies": [],
                    "form_types": [],
                    "fx_converted": false,
                    "official_periods": 0
                  },
                  "note": "Summary assessments describe the upstream company window, not the filtered statement rows. Source coverage may count observations beyond the entitled archive. Guidance currency and horizon are not supplied; do not compare it with USD actuals without checking the article."
                },
                "access_limited": true,
                "available_period_count": 7,
                "computed_at": "2026-09-23T06:41:53.825000Z",
                "latest_period": {
                  "period": "FY2025",
                  "fiscal_year": 2025,
                  "fiscal_period": "FY",
                  "period_end": null,
                  "reported_date": "2025-10-16",
                  "filed_date": null,
                  "form_type": null,
                  "metrics": {
                    "net_income": {
                      "value": -145080000,
                      "currency": "USD",
                      "unit": "absolute",
                      "source_type": "news_report",
                      "native_value": null,
                      "native_currency": null
                    },
                    "revenue": {
                      "value": 453960000,
                      "currency": "USD",
                      "unit": "absolute",
                      "source_type": "news_report",
                      "native_value": null,
                      "native_currency": null
                    }
                  },
                  "article_ids": [
                    "68f7191fe97e6da31e2cb7f5",
                    "68f71b6fb5f4abc34a2cf07a",
                    "68f737d9f3ba9a3da52d30db",
                    "6989485b94d3f481f3e2d117"
                  ],
                  "currency_conversion": null,
                  "evidence": {
                    "coverage_count": 4,
                    "quality_signals": [
                      "Reported a loss",
                      "Record revenue"
                    ],
                    "has_official": false,
                    "period_has_official": false
                  },
                  "operating_context": {
                    "employees": null,
                    "revenue_growth_pct": 65.0,
                    "net_income_growth_pct": null,
                    "guidance_revenue": null,
                    "beat_or_miss": null
                  }
                },
                "detail_required_for_history": true
              },
              "window": {
                "data_through": "2025-10-16"
              },
              "meta": {
                "retrieved_at": "2026-09-23T06:47:54.822052+00:00",
                "partial": false,
                "notes": [
                  "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
                  "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies.",
                  "The linked Radar account exposes only part of the financial archive."
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
                "domain": "razorpay.com",
                "computed_at": "2026-09-23T06:41:53.825000Z",
                "assessments": {
                  "innovation_index": {
                    "score": 23
                  },
                  "investment_readiness": {
                    "score": 57,
                    "label": "Moderate"
                  },
                  "management_quality": {
                    "score": 90
                  },
                  "market_position": {
                    "score": 17
                  },
                  "risk_profile": {
                    "score": 7
                  }
                },
                "detail_required_for_analysis": true
              },
              "window": {
                "data_through": null
              },
              "meta": {
                "retrieved_at": "2026-09-23T06:47:54.817976+00:00",
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
          }
        },
        "partial": false
      },
      {
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
                  "innovation": "not_observed",
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
                "retrieved_at": "2026-09-23T06:47:54.840414+00:00",
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
                  "narrative": "Latest reported FY2024: revenue $500M. Growth has been erratic across reported periods. Recent signals: Reported a loss, Record revenue, Profitable.",
                  "assessment": {
                    "score": 48,
                    "growth_consistency": 0,
                    "yoy_pct": null,
                    "yoy_multiple": null,
                    "yoy_basis": null,
                    "quality_signals_aggregate": [
                      "Reported a loss",
                      "Record revenue",
                      "Profitable"
                    ]
                  },
                  "comparison_periods": {
                    "latest": {
                      "period_label": "FY2024",
                      "period_year": 2024,
                      "period_qtr": "FY",
                      "date": "2025-02-28"
                    },
                    "prior": {
                      "period_label": null,
                      "period_year": null,
                      "period_qtr": null,
                      "date": null
                    }
                  },
                  "source_coverage": {
                    "bi_periods": 3,
                    "currencies": [],
                    "form_types": [],
                    "fx_converted": false,
                    "official_periods": 0
                  },
                  "note": "Summary assessments describe the upstream company window, not the filtered statement rows. Source coverage may count observations beyond the entitled archive. Guidance currency and horizon are not supplied; do not compare it with USD actuals without checking the article."
                },
                "access_limited": false,
                "available_period_count": 3,
                "computed_at": "2026-09-23T06:41:19.445000Z",
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
                  "currency_conversion": null,
                  "evidence": {
                    "coverage_count": 1,
                    "quality_signals": [],
                    "headline": "Stripe’s Revenue and Finance Automation Suite, with Billing at its core, recently passed a $500 million revenue run rate.",
                    "has_official": false,
                    "period_has_official": false
                  },
                  "operating_context": {
                    "employees": null,
                    "revenue_growth_pct": null,
                    "net_income_growth_pct": null,
                    "guidance_revenue": null,
                    "beat_or_miss": null
                  }
                },
                "detail_required_for_history": true
              },
              "window": {
                "data_through": "2025-02-28"
              },
              "meta": {
                "retrieved_at": "2026-09-23T06:47:54.851581+00:00",
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
                "computed_at": "2026-09-23T06:41:19.445000Z",
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
                "retrieved_at": "2026-09-23T06:47:54.833051+00:00",
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
    "retrieved_at": "2026-09-23T06:47:54.851669+00:00",
    "partial": false,
    "notes": [
      "Each section retains its own date window and access limits. Missing data is not zero."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:54.851961+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/compare_companies.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live Razorpay/Stripe comparison returned both companies with compact identity, latest-period financial evidence and derived-score summaries. Each section supplies a separate detail_request; full profile fields and financial histories require their own calls.

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
