# Financial filters and data API: revenue, profit, cash flow and startup screening

Use this guide to find companies by an exact financial amount, a source revenue
band, profitability or revenue growth, and then retrieve the financial evidence.
A company listing, a financial statement, a funding round and an estimated revenue
label describe different things. The API exposes them separately.

## USA AdTech startups with revenue below $10,000

Send this JSON to **`POST /v1/companies/financials/screen`**, or pass it as
`request` to the MCP tool `screen_company_financials`:

```json
{"filters":{"industries":["AdTech"],"locations":["United States"],"founded_year_from":2021},"constraints":[{"metric":"revenue","gte":0,"lt":10000}],"period_type":"annual","candidate_limit":3}
```

Here “startup” means founded since 2021, an explicit research definition rather
than an inferred universal startup flag. Geography is recorded company location;
it does not establish US incorporation, every operating market or US customers.
`gte:0` includes known zero revenue; `lt:10000` excludes exactly $10,000. Omit neither
the currency interpretation nor the reporting period when describing the result.
This endpoint accepts normalized USD metrics, not an arbitrary currency parameter.

[Executed example 03](../scenarios/03-usa-adtech-under-10k.md) includes the complete
captured response. It found Adster, Marko Polo and Topsort as strict source
candidates, but no accessible annual financial periods for those three. Therefore
`matches` is empty and `counts.unknown` is 3. **It does not establish that any of
them earns below $10,000, or that no matching startup exists.** Do not turn absent
revenue into zero. Increase `page` to inspect another bounded source candidate page;
keep all filters and the candidate limit stable while paging.

For a worked positive result, [example 04](../scenarios/04-usa-adtech-over-1m.md)
screens US AdTech companies at or above $1 million and retains two matches, one
unknown and the actual fiscal periods and metric sources. Both queries are
executed examples; neither is a fabricated marketing response.

## Choose the financial operation

| Requirement | Operation and HTTP route | What it establishes |
|---|---|---|
| Read numeric and band definitions | `financial_filter_catalog`, `/v1/companies/financials/filters` | Supported metrics, source bucket edges and screen schema |
| Exact amount or multiple financial conditions | `screen_company_financials`, `/v1/companies/financials/screen` | Dated numeric checks for a bounded candidate page or explicit domains |
| Quick revenue/growth/profitability shortlist | `search_companies`, `/v1/companies/search` | Source summary predicates; no chosen financial year |
| Financial statements and historical periods | `get_financials`, `/v1/companies/financials` | Income, balance-sheet and cash-flow metrics with period/source labels |
| Add readable financial columns to a list | `get_company_columns`, `/v1/companies/columns` | Display values; these can suppress zero or negative values |
| Reported fundraising and investors | `get_company_funding`, `/v1/companies/funding` | Reported rounds, not company sales revenue |

All are POST requests, require your API key and share REST/MCP account usage.
[Key onboarding](api-keys-authentication.md) explains obtaining a key; clients need
only the operator-supplied API URL and that credential.

## Exact comparisons, periods and source types

```json
{"domains":["microsoft.com"],"constraints":[{"metric":"net_income","gt":0},{"metric":"revenue","gte":1000000000}],"period_type":"annual","year_from":2024,"year_to":2026,"source_type":"filing"}
```

Use either `domains` (one to ten unique domains) or nonempty company `filters`.
The screen takes one to five distinct metric constraints. `gt`/`lt` are exclusive;
`gte`/`lte` are inclusive. Contradictory bounds, nonfinite numbers and two lower
bounds for the same metric are rejected. Multiple constraints are ANDed against
**one latest accessible period** within the requested year window and annual or
quarterly type. Missing values in that period do not trigger a search for an older
period that happens to pass. `source_type` can be `any`, `filing` or `news_report`;
it qualifies each constrained metric, not just the whole company.

Supported USD metrics include revenue, net income, operating income, gross profit,
EBITDA, total assets, total liabilities, stockholders' equity, cash, long-term debt,
operating/investing/financing/free cash flow and capex. EPS is a per-share measure
and is deliberately outside this USD-amount screen. See the
[financial filter reference](../reference/financial_filter_catalog.md) for the
machine-readable schema and [screen reference](../reference/screen_company_financials.md)
for limits, errors and MCP syntax.

`matched` means every numeric condition passed. `not_matched` means at least one
known value failed. `unknown` means the accessible evidence could not resolve the
conditions. `unavailable` identifies a failed financial read. Each evaluated row
retains the source period, values, currency and access status. Source filing labels
are provenance supplied by Radar; the screen does not independently audit filings.

## Legacy bands have important boundaries

| Filter | Actual source comparison |
|---|---|
| `under1m` | Revenue strictly greater than 0 and strictly below 1,000,000 |
| `1m-10m` | Strictly greater than 1,000,000 and strictly below 10,000,000 |
| `10m-100m` | Strictly greater than 10,000,000 and strictly below 100,000,000 |
| `100m-1b` | Strictly greater than 100,000,000 and strictly below 1,000,000,000 |
| `1b+` | Strictly greater than 1,000,000,000 |
| `profitable` / `loss` | Source latest net profit strictly above / below zero |

The source bands leave exact million/ten-million/hundred-million/billion boundary
values out. They also exclude zero. Use the exact screen when inclusion at an edge
matters. Revenue growth bands use the source one-year revenue growth field:
`declining <0`, `flat [0,10)`, `growing [10,30)`, `high [30,100)`, `hyper >=100`, in
percent. “Flat” therefore includes positive growth below 10%; these are product
labels, not accounting definitions. One revenue band and one growth band can be
selected per request. Funding `deal_sizes` and subscription `revenue_models` do
not filter financial revenue.

## Retrieve statements without inventing missing periods

```json
{"domain":"microsoft.com","statement":"balance_sheet","period_type":"annual","year_from":2024,"year_to":2026,"limit":3}
```

```json
{"domain":"microsoft.com","statement":"income","period_type":"quarterly","limit":3}
```

The captured annual balance-sheet, income and cash-flow scenarios returned no
accessible annual rows under the preview entitlement; the quarterly income request
returned three periods. The archive can contain more history than the key can
access. Keep `access_limited`, archive counts, fiscal labels and missing dates.
Do not synthesize annual statements by adding quarters or treat a filing date as
an unknown period end. [Examples 13–16](../scenarios/README.md) preserve these
contrasting results, and [statement guidance](company-financial-statements-api.md)
explains metric families.

## Completeness, pagination and cost

Filtered screens inspect at most ten candidates per call, with up to three
financial reads running concurrently. Strict source matching is required; expanded
fallback candidates and searches whose filters were stripped are excluded. An empty
strict page may still have `next_page` because pagination belongs to the underlying
source pool. Missing tier metadata is unverified and is excluded. A null continuation
is not an independent proof of exhaustive market coverage.

In account mode, reserve one screen credit plus the requested candidate capacity
(or number of explicit domains). Settle one credit plus successful financial reads;
unused capacity and failed reads are refunded. A successful financial read with no
accessible periods still consumes its read credit. Preview captures do not establish
a deployed tariff or a production billing transaction. Check `meta.billing` for
actual charges and [pricing](pricing-pay-per-use.md) for account policy.

<!-- scenario-links -->
## Executed scenarios for this workflow

- [03-usa-adtech-under-10k: Find US AdTech startups founded since 2021 with latest annual revenue below USD 10,000.](../scenarios/03-usa-adtech-under-10k.md)
- [04-usa-adtech-over-1m: Find US AdTech companies with latest annual revenue of at least USD 1 million.](../scenarios/04-usa-adtech-over-1m.md)
- [05-india-profitable: Find profitable Indian software companies with recorded revenue growth.](../scenarios/05-india-profitable.md)
- [06-under-1m-band: Find US AdTech candidates in Radar’s positive-revenue under-USD-1M band.](../scenarios/06-under-1m-band.md)
- [07-10m-100m-band: Find Indian software companies in the USD 10M–100M revenue band.](../scenarios/07-10m-100m-band.md)
- [08-high-growth: Find Indian software candidates with recorded 30–100% revenue growth.](../scenarios/08-high-growth.md)
- [09-loss-making: Find Indian payments companies with recorded net losses.](../scenarios/09-loss-making.md)
- [13-balance-sheet: Retrieve Microsoft annual assets, liabilities and equity for 2024–2026.](../scenarios/13-balance-sheet.md)
- [14-annual-income: Retrieve Microsoft’s FY2025 income figures without quarterly mixing.](../scenarios/14-annual-income.md)
- [15-annual-cash-flow: Retrieve Microsoft annual operating cash flow, capex and free cash flow.](../scenarios/15-annual-cash-flow.md)
- [16-quarterly-income: Retrieve Microsoft’s three latest accessible quarterly income periods.](../scenarios/16-quarterly-income.md)
- [18-finance-columns: Compare available revenue and funding display columns for Razorpay and Stripe.](../scenarios/18-finance-columns.md)
- [19-precise-profit-screen: Check whether Microsoft has positive annual profit and revenue above USD 1B in its latest accessible year.](../scenarios/19-precise-profit-screen.md)
- [20-financial-filter-definitions: Discover exact financial thresholds, growth meanings and screening limits.](../scenarios/20-financial-filter-definitions.md)

<!-- captured-workflow -->
## Read the evidence behind a positive financial screen

This capture uses US AdTech companies and a USD 1 million inclusive lower bound on annual revenue. It is a different, explicitly labelled query from the startup-under-$10,000 example above. Both matched periods, all evaluated companies and the unknown result are retained. A partial response can contain valid measured matches while leaving other companies unresolved.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/financials/screen`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: screen_company_financials -->
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
          "has_phone": false,
          "linkedin_slug": "inuvo-inc",
          "founded": "2009",
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "company_id": "20pyrmqhov",
          "description": "Platform offering privacy based advertising solution",
          "hq": "clearwater",
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
          "has_email": false,
          "tagline": "Platform offering privacy based advertising solution",
          "size": "51-200",
          "domain": "inuvo.com",
          "slug": "inuvo",
          "name": "Inuvo",
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
          "currency_conversion": null,
          "evidence": {
            "coverage_count": 1,
            "quality_signals": [
              "Missed estimates"
            ],
            "headline": "Inuvo sees FY25 revenue $86M, consensus $99.28M",
            "has_official": false,
            "period_has_official": false
          },
          "operating_context": {
            "employees": null,
            "revenue_growth_pct": null,
            "net_income_growth_pct": null,
            "guidance_revenue": 99280000,
            "beat_or_miss": "Miss"
          }
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
          "has_phone": false,
          "linkedin_slug": "pubmatic",
          "founded": "2006",
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "company_id": "fqzfzfnaqh",
          "description": "Provider of a platform for digital advertising supply chain management",
          "hq": "redwood city",
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
          "has_email": false,
          "tagline": "Provider of a platform for digital advertising supply chain management",
          "size": "51-200",
          "domain": "pubmatic.com",
          "slug": "pubmatic",
          "name": "PubMatic",
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
          "currency_conversion": null,
          "evidence": {
            "coverage_count": 1,
            "quality_signals": [
              "Beat estimates",
              "Reported a loss"
            ],
            "headline": "Revenue for the full year 2025 was $282.9 million , compared to $291.3 million in 2024;",
            "has_official": false,
            "period_has_official": false
          },
          "operating_context": {
            "employees": null,
            "revenue_growth_pct": -3.0,
            "net_income_growth_pct": null,
            "guidance_revenue": null,
            "beat_or_miss": "Beat"
          }
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
          "has_phone": false,
          "linkedin_slug": "inuvo-inc",
          "founded": "2009",
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "company_id": "20pyrmqhov",
          "description": "Platform offering privacy based advertising solution",
          "hq": "clearwater",
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
          "has_email": false,
          "tagline": "Platform offering privacy based advertising solution",
          "size": "51-200",
          "domain": "inuvo.com",
          "slug": "inuvo",
          "name": "Inuvo",
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
          "currency_conversion": null,
          "evidence": {
            "coverage_count": 1,
            "quality_signals": [
              "Missed estimates"
            ],
            "headline": "Inuvo sees FY25 revenue $86M, consensus $99.28M",
            "has_official": false,
            "period_has_official": false
          },
          "operating_context": {
            "employees": null,
            "revenue_growth_pct": null,
            "net_income_growth_pct": null,
            "guidance_revenue": 99280000,
            "beat_or_miss": "Miss"
          }
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
          "has_phone": false,
          "linkedin_slug": "pubmatic",
          "founded": "2006",
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "company_id": "fqzfzfnaqh",
          "description": "Provider of a platform for digital advertising supply chain management",
          "hq": "redwood city",
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
          "has_email": false,
          "tagline": "Provider of a platform for digital advertising supply chain management",
          "size": "51-200",
          "domain": "pubmatic.com",
          "slug": "pubmatic",
          "name": "PubMatic",
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
          "currency_conversion": null,
          "evidence": {
            "coverage_count": 1,
            "quality_signals": [
              "Beat estimates",
              "Reported a loss"
            ],
            "headline": "Revenue for the full year 2025 was $282.9 million , compared to $291.3 million in 2024;",
            "has_official": false,
            "period_has_official": false
          },
          "operating_context": {
            "employees": null,
            "revenue_growth_pct": -3.0,
            "net_income_growth_pct": null,
            "guidance_revenue": null,
            "beat_or_miss": "Beat"
          }
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
          "has_phone": false,
          "linkedin_slug": "smaato",
          "founded": "2005",
          "flags": [
            [
              "Medium Enterprise",
              "size"
            ]
          ],
          "company_id": "3ochu76ehs",
          "description": "Mobile RTB ad exchange and SSP",
          "hq": "san francisco",
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
          "has_email": false,
          "tagline": "Mobile RTB ad exchange and SSP",
          "size": "201-500",
          "domain": "smaato.com",
          "slug": "smaato",
          "name": "Smaato",
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
          "has_phone": false,
          "linkedin_slug": "inuvo-inc",
          "founded": "2009",
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "company_id": "20pyrmqhov",
          "description": "Platform offering privacy based advertising solution",
          "hq": "clearwater",
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
          "has_email": false,
          "tagline": "Platform offering privacy based advertising solution",
          "size": "51-200",
          "domain": "inuvo.com",
          "slug": "inuvo",
          "name": "Inuvo",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=inuvo.com",
          "match_tier": "strict"
        },
        {
          "has_phone": false,
          "linkedin_slug": "pubmatic",
          "founded": "2006",
          "flags": [
            [
              "Small Enterprise",
              "size"
            ]
          ],
          "company_id": "fqzfzfnaqh",
          "description": "Provider of a platform for digital advertising supply chain management",
          "hq": "redwood city",
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
          "has_email": false,
          "tagline": "Provider of a platform for digital advertising supply chain management",
          "size": "51-200",
          "domain": "pubmatic.com",
          "slug": "pubmatic",
          "name": "PubMatic",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=pubmatic.com",
          "match_tier": "strict"
        },
        {
          "has_phone": false,
          "linkedin_slug": "smaato",
          "founded": "2005",
          "flags": [
            [
              "Medium Enterprise",
              "size"
            ]
          ],
          "company_id": "3ochu76ehs",
          "description": "Mobile RTB ad exchange and SSP",
          "hq": "san francisco",
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
          "has_email": false,
          "tagline": "Mobile RTB ad exchange and SSP",
          "size": "201-500",
          "domain": "smaato.com",
          "slug": "smaato",
          "name": "Smaato",
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
    "retrieved_at": "2026-09-23T06:47:28.329850+00:00",
    "partial": true,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:28.330098+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/screen_company_financials.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The US AdTech annual-revenue screen above $1 million returned two measured matches and one unknown. The separate startup screen below $10,000 had three unknown annual observations and no verified match; see scenario 03.

See the [complete screen_company_financials endpoint reference](../reference/screen_company_financials.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
