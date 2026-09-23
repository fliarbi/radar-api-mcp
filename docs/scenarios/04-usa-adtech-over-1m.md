# Find US AdTech companies with latest annual revenue of at least USD 1 million.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/screen_company_financials.md)

**POST `/v1/companies/financials/screen`** · MCP tool **`screen_company_financials`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 04-usa-adtech-over-1m -->
```json
{
  "filters": {
    "industries": [
      "AdTech"
    ],
    "locations": [
      "United States"
    ]
  },
  "constraints": [
    {
      "metric": "revenue",
      "gte": 1000000
    }
  ],
  "period_type": "annual",
  "candidate_limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:31.627402+00:00; HTTP **200**;
**qualified**, 0.142 seconds.
Local authenticated gateway with live configured read-only sources.

Partial result or source timeout; Coverage is explicitly bounded.

Read all evaluated rows, not just matches. Numeric conditions use the same latest accessible fiscal period. Unknown means missing or disallowed evidence; unavailable means a failed read. Neither becomes zero. This is a bounded candidate screen with source gates, not an exhaustive company database query. Its per-metric checks preserve currency, source type and inclusive/exclusive bounds.

The source reported FY2025 revenue of USD 86,000,000 for Inuvo and USD 282,900,000 for PubMatic; both metric sources are news_report, not filing. The third candidate was unresolved. The captured values are reproduced as API evidence, not independently audited financial claims.

The baseline was an unavailable operation registry check (no HTTP request), **unavailable**:
not_implemented. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 04-usa-adtech-over-1m -->
```json
{
  "ok": true,
  "feature": "screen_company_financials",
  "data": {
    "matches": [
      {
        "domain": "inuvo.com",
        "company": {
          "hq": "clearwater",
          "tagline": "Platform offering privacy based advertising solution",
          "has_phone": false,
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "domain": "inuvo.com",
          "slug": "inuvo",
          "company_id": "20pyrmqhov",
          "linkedin_slug": "inuvo-inc",
          "location": {
            "c": "united states",
            "rg": "florida",
            "l": "clearwater",
            "lc": "clearwater, florida, united states",
            "hq": "clearwater",
            "cc": "us",
            "coord": [
              -82.8001,
              27.96585
            ],
            "g": "27.96585,-82.8001"
          },
          "founded": "2009",
          "name": "Inuvo",
          "size": "51-200",
          "has_email": false,
          "description": "Platform offering privacy based advertising solution",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=inuvo.com",
          "match_tier": "strict"
        },
        "status": "matched",
        "period": {
          "period": "FY2025",
          "fiscal_year": 2025,
          "fiscal_period": "FY",
          "period_end": null,
          "reported_date": "2026-02-06",
          "filed_date": null,
          "form_type": null,
          "metrics": {
            "revenue": {
              "value": 86000000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            }
          },
          "article_ids": [
            "69baffcd85c39bb46c6e6779"
          ],
          "currency_conversion": null
        },
        "checks": [
          {
            "metric": "revenue",
            "status": "matched",
            "value": 86000000,
            "currency": "USD",
            "bounds": {
              "gte": 1000000.0
            },
            "source_type": "news_report"
          }
        ],
        "access_limited": true,
        "successful_read": true
      },
      {
        "domain": "pubmatic.com",
        "company": {
          "hq": "redwood city",
          "tagline": "Provider of a platform for digital advertising supply chain management",
          "has_phone": false,
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "domain": "pubmatic.com",
          "slug": "pubmatic",
          "company_id": "fqzfzfnaqh",
          "linkedin_slug": "pubmatic",
          "location": {
            "c": "united states",
            "rg": "california",
            "l": "redwood city",
            "lc": "redwood city, california, united states",
            "hq": "redwood city",
            "cc": "us",
            "coord": [
              -122.23635,
              37.48522
            ],
            "g": "37.48522,-122.23635"
          },
          "founded": "2006",
          "name": "PubMatic",
          "size": "51-200",
          "has_email": false,
          "description": "Provider of a platform for digital advertising supply chain management",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=pubmatic.com",
          "match_tier": "strict"
        },
        "status": "matched",
        "period": {
          "period": "FY2025",
          "fiscal_year": 2025,
          "fiscal_period": "FY",
          "period_end": null,
          "reported_date": "2026-02-26",
          "filed_date": null,
          "form_type": null,
          "metrics": {
            "ebitda": {
              "value": 61600000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "eps": {
              "value": -0.31,
              "currency": null,
              "unit": "per_share",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "net_income": {
              "value": -14500000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "revenue": {
              "value": 282900000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            }
          },
          "article_ids": [
            "69e8cd879baafc7356cca261"
          ],
          "currency_conversion": null
        },
        "checks": [
          {
            "metric": "revenue",
            "status": "matched",
            "value": 282900000,
            "currency": "USD",
            "bounds": {
              "gte": 1000000.0
            },
            "source_type": "news_report"
          }
        ],
        "access_limited": true,
        "successful_read": true
      }
    ],
    "evaluated": [
      {
        "domain": "inuvo.com",
        "company": {
          "hq": "clearwater",
          "tagline": "Platform offering privacy based advertising solution",
          "has_phone": false,
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "domain": "inuvo.com",
          "slug": "inuvo",
          "company_id": "20pyrmqhov",
          "linkedin_slug": "inuvo-inc",
          "location": {
            "c": "united states",
            "rg": "florida",
            "l": "clearwater",
            "lc": "clearwater, florida, united states",
            "hq": "clearwater",
            "cc": "us",
            "coord": [
              -82.8001,
              27.96585
            ],
            "g": "27.96585,-82.8001"
          },
          "founded": "2009",
          "name": "Inuvo",
          "size": "51-200",
          "has_email": false,
          "description": "Platform offering privacy based advertising solution",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=inuvo.com",
          "match_tier": "strict"
        },
        "status": "matched",
        "period": {
          "period": "FY2025",
          "fiscal_year": 2025,
          "fiscal_period": "FY",
          "period_end": null,
          "reported_date": "2026-02-06",
          "filed_date": null,
          "form_type": null,
          "metrics": {
            "revenue": {
              "value": 86000000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            }
          },
          "article_ids": [
            "69baffcd85c39bb46c6e6779"
          ],
          "currency_conversion": null
        },
        "checks": [
          {
            "metric": "revenue",
            "status": "matched",
            "value": 86000000,
            "currency": "USD",
            "bounds": {
              "gte": 1000000.0
            },
            "source_type": "news_report"
          }
        ],
        "access_limited": true,
        "successful_read": true
      },
      {
        "domain": "pubmatic.com",
        "company": {
          "hq": "redwood city",
          "tagline": "Provider of a platform for digital advertising supply chain management",
          "has_phone": false,
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "domain": "pubmatic.com",
          "slug": "pubmatic",
          "company_id": "fqzfzfnaqh",
          "linkedin_slug": "pubmatic",
          "location": {
            "c": "united states",
            "rg": "california",
            "l": "redwood city",
            "lc": "redwood city, california, united states",
            "hq": "redwood city",
            "cc": "us",
            "coord": [
              -122.23635,
              37.48522
            ],
            "g": "37.48522,-122.23635"
          },
          "founded": "2006",
          "name": "PubMatic",
          "size": "51-200",
          "has_email": false,
          "description": "Provider of a platform for digital advertising supply chain management",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=pubmatic.com",
          "match_tier": "strict"
        },
        "status": "matched",
        "period": {
          "period": "FY2025",
          "fiscal_year": 2025,
          "fiscal_period": "FY",
          "period_end": null,
          "reported_date": "2026-02-26",
          "filed_date": null,
          "form_type": null,
          "metrics": {
            "ebitda": {
              "value": 61600000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "eps": {
              "value": -0.31,
              "currency": null,
              "unit": "per_share",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "net_income": {
              "value": -14500000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            },
            "revenue": {
              "value": 282900000,
              "currency": "USD",
              "unit": "absolute",
              "source_type": "news_report",
              "native_value": null,
              "native_currency": null
            }
          },
          "article_ids": [
            "69e8cd879baafc7356cca261"
          ],
          "currency_conversion": null
        },
        "checks": [
          {
            "metric": "revenue",
            "status": "matched",
            "value": 282900000,
            "currency": "USD",
            "bounds": {
              "gte": 1000000.0
            },
            "source_type": "news_report"
          }
        ],
        "access_limited": true,
        "successful_read": true
      },
      {
        "domain": "smaato.com",
        "company": {
          "hq": "san francisco",
          "tagline": "Mobile RTB ad exchange and SSP",
          "has_phone": false,
          "flags": [
            [
              "Medium Enterprise",
              "size"
            ]
          ],
          "domain": "smaato.com",
          "slug": "smaato",
          "company_id": "3ochu76ehs",
          "linkedin_slug": "smaato",
          "location": {
            "c": "united states",
            "rg": "california",
            "l": "san francisco",
            "lc": "san francisco, california, united states",
            "hq": "san francisco",
            "cc": "us",
            "coord": [
              -122.41942,
              37.77493
            ],
            "g": "37.77493,-122.41942"
          },
          "founded": "2005",
          "name": "Smaato",
          "size": "201-500",
          "has_email": false,
          "description": "Mobile RTB ad exchange and SSP",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=smaato.com",
          "match_tier": "strict"
        },
        "status": "unknown",
        "reason": "No accessible period matches the requested type/year window",
        "period": null,
        "checks": [],
        "access_limited": false,
        "successful_read": true
      }
    ],
    "counts": {
      "matched": 2,
      "unknown": 1
    },
    "constraints": [
      {
        "metric": "revenue",
        "gte": 1000000.0
      }
    ],
    "period_type": "annual",
    "source_type": "any",
    "discovery": {
      "companies": [
        {
          "hq": "clearwater",
          "tagline": "Platform offering privacy based advertising solution",
          "has_phone": false,
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "domain": "inuvo.com",
          "slug": "inuvo",
          "company_id": "20pyrmqhov",
          "linkedin_slug": "inuvo-inc",
          "location": {
            "c": "united states",
            "rg": "florida",
            "l": "clearwater",
            "lc": "clearwater, florida, united states",
            "hq": "clearwater",
            "cc": "us",
            "coord": [
              -82.8001,
              27.96585
            ],
            "g": "27.96585,-82.8001"
          },
          "founded": "2009",
          "name": "Inuvo",
          "size": "51-200",
          "has_email": false,
          "description": "Platform offering privacy based advertising solution",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=inuvo.com",
          "match_tier": "strict"
        },
        {
          "hq": "redwood city",
          "tagline": "Provider of a platform for digital advertising supply chain management",
          "has_phone": false,
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "domain": "pubmatic.com",
          "slug": "pubmatic",
          "company_id": "fqzfzfnaqh",
          "linkedin_slug": "pubmatic",
          "location": {
            "c": "united states",
            "rg": "california",
            "l": "redwood city",
            "lc": "redwood city, california, united states",
            "hq": "redwood city",
            "cc": "us",
            "coord": [
              -122.23635,
              37.48522
            ],
            "g": "37.48522,-122.23635"
          },
          "founded": "2006",
          "name": "PubMatic",
          "size": "51-200",
          "has_email": false,
          "description": "Provider of a platform for digital advertising supply chain management",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=pubmatic.com",
          "match_tier": "strict"
        },
        {
          "hq": "san francisco",
          "tagline": "Mobile RTB ad exchange and SSP",
          "has_phone": false,
          "flags": [
            [
              "Medium Enterprise",
              "size"
            ]
          ],
          "domain": "smaato.com",
          "slug": "smaato",
          "company_id": "3ochu76ehs",
          "linkedin_slug": "smaato",
          "location": {
            "c": "united states",
            "rg": "california",
            "l": "san francisco",
            "lc": "san francisco, california, united states",
            "hq": "san francisco",
            "cc": "us",
            "coord": [
              -122.41942,
              37.77493
            ],
            "g": "37.77493,-122.41942"
          },
          "founded": "2005",
          "name": "Smaato",
          "size": "201-500",
          "has_email": false,
          "description": "Mobile RTB ad exchange and SSP",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=smaato.com",
          "match_tier": "strict"
        }
      ],
      "page": 0,
      "requested_limit": 3,
      "returned": 3,
      "total": null,
      "access": {
        "plan": "free",
        "results_capped": false,
        "searches_remaining": 50
      },
      "partial_timeout": false,
      "matching": {
        "mode": "strict",
        "tiers": [
          {
            "tier": "strict",
            "count": 3850,
            "added": 3
          }
        ],
        "source_rows": 3,
        "excluded_candidates": 0,
        "strict_count_reported": 3850,
        "candidate_pool_count_reported": 3850,
        "count_capped": false,
        "filters_restricted": false,
        "note": "Strict means the source labelled the row strict and did not strip filters. Counts may describe an expanded candidate pool, not all matching companies. Missing tier metadata is unverified."
      },
      "next_page": 1,
      "pagination": "Increment source page even when strict filtering returns no rows; next_page is a continuation hint, not a guarantee of more matches. Account caps apply."
    },
    "next_page": 1,
    "coverage": {
      "complete": false,
      "partial": true,
      "candidate_count": 3,
      "company_filters_independently_verified": false,
      "note": "Numeric matches are verified against returned dated metrics. Candidate company classification/geography remains source-filtered; inspect source access and matching. Empty matches do not mean there are no matching companies elsewhere."
    },
    "successful_financial_reads": 3
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:31.627167+00:00",
    "partial": true,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/04-usa-adtech-over-1m.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
