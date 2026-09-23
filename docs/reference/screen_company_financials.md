# Exact company financial screening API: dated revenue and profit conditions

[All endpoints](README.md) · [Workflow guide](../guides/financial-filters-data-api.md)

Evaluate one bounded candidate page or up to ten explicit company domains against one to five USD financial conditions. Return the evidence and distinguish matches, non-matches, unknown values and failed reads.

## Route, authentication and credits

**`POST /v1/companies/financials/screen`** · MCP tool **`screen_company_financials`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one screen credit plus successful financial reads; reserve one plus candidate capacity and refund unused or failed reads. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `filters` | optional; empty by default | CompanyFilters |
| `domains` | optional; empty by default | array of string; max items: `10` |
| `constraints` | required | array of FinancialConstraint; min items: `1`; max items: `5` |
| `period_type` | required | string; one of `annual`, `quarterly` |
| `year_from` | default `null` | integer or null; minimum: `1900`; maximum: `2100` |
| `year_to` | default `null` | integer or null; minimum: `1900`; maximum: `2100` |
| `source_type` | default `"any"` | string; one of `any`, `filing`, `news_report` |
| `page` | default `0` | integer; minimum: `0`; maximum: `200` |
| `candidate_limit` | default `5` | integer; minimum: `1`; maximum: `10` |

### Fields inside `filters`

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `company_names` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `industries` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `sectors` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `markets` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `business_models` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `locations` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `sizes` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `stages` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `technologies` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `products` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `skills` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `event_types` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `financing_status` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `ownership_status` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `revenue_bands` | optional; empty by default | array of string; max items: `1`; one of `under1m`, `1m-10m`, `10m-100m`, `100m-1b`, `1b+` |
| `revenue_growth` | optional; empty by default | array of string; max items: `1`; one of `declining`, `flat`, `growing`, `high`, `hyper` |
| `profitability` | optional; empty by default | array of string; max items: `1`; one of `profitable`, `loss` |
| `entity_type` | default `"all"` | string; one of `all`, `investor`, `incubator` |
| `revenue_models` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `business_approaches` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `scalability` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `growth_stages` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `operating_status` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `organization_types` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `deal_sizes` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `ages` | optional; empty by default | array of string; max items: `1`; one of `Most Recent`, `< 5y`, `5-10y`, `10-25y`, `25+y` |
| `founded_year_from` | default `null` | integer or null; minimum: `1800`; maximum: `2100` |
| `founded_year_to` | default `null` | integer or null; minimum: `1800`; maximum: `2100` |
| `positions` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `verticals` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `industrial_applications` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `founders_background` | optional; empty by default | array of string; max items: `10`; one of `serial_entrepreneur`, `first_time_founder`, `founder_with_exit`, `top_ranked_founder`, `top_tier_university`, `elite_alumni`, `technical_founder`, `ex_notable_employer`, `c_level_exec`, `seasoned_15y` |
| `web_popularity` | optional; empty by default | array of string; max items: `3`; one of `high`, `medium`, `low` |
| `web_cwv` | optional; empty by default | array of string; max items: `3`; one of `pass`, `needs_improvement`, `poor` |
| `web_speed` | optional; empty by default | array of string; max items: `3`; one of `fast`, `average`, `slow` |
| `web_seo_maturity` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `web_sd_maturity` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `web_business_hints` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `web_score` | optional; empty by default | array of string; max items: `1`; one of `80+`, `60-80`, `40-60`, `<40` |
| `mobile_downloads` | optional; empty by default | array of string; max items: `1`; one of `1k+`, `100k+`, `1m+`, `10m+` |
| `mobile_growth` | optional; empty by default | array of string; max items: `1`; one of `declining`, `flat`, `growing`, `high`, `hyper` |
| `hiring` | default `null` | HiringFilter or null |
| `radius_km` | default `null` | integer or null; minimum: `21`; maximum: `250` |

### Fields inside `filters.hiring`

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `is_hiring` | default `true` | boolean |
| `min_open_roles` | default `1` | integer; minimum: `1`; maximum: `100000` |
| `roles` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `cities` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `recency_days` | default `30` | integer; minimum: `1`; maximum: `365` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/financials/screen" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"industries":["AdTech"],"locations":["United States"]},"constraints":[{"metric":"revenue","gte":1000000}],"period_type":"annual","candidate_limit":3}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: screen_company_financials -->
```json
{
  "name": "screen_company_financials",
  "arguments": {
    "request": {
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
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: screen_company_financials -->
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

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T03:35:31.627402+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/screen_company_financials.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The US AdTech annual-revenue screen above $1 million returned two measured matches and one unknown. The separate startup screen below $10,000 had three unknown annual observations and no verified match; see scenario 03.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.matches` | Rows whose available USD metrics satisfy every condition. |
| `data.evaluated` | Every inspected domain, including failed and unresolved reads; successful rows retain the dated financial period. |
| `data.counts` | Counts by matched, not_matched, unknown or unavailable outcome. |
| `data.discovery` | Source candidate page, strict matching labels, excluded rows and access limits; null for explicit domains. |
| `data.next_page` | Source continuation hint; keep the same filters and page size. It does not guarantee more matches. |
| `data.coverage` | Always bounded; partial indicates missing evidence, restricted filters, failed reads or source limits. |
| `data.successful_financial_reads` | Used to settle composite account credits; an empty successful financial read still counts. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Select annual or quarterly periods and optional fiscal-year bounds. All conditions use the same latest accessible period. Review evaluated rows, source-plan limits and matching metadata before continuing to another candidate page.

This is not a global financial query or an exhaustive export. It does not infer startup status, bypass source plan gates or fall back to older periods to manufacture a match.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/financial-filters-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
