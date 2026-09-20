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
  -d '{"domain":"stripe.com","include_news":true,"news_limit":2,"event_days":30}'
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
    "domain": "stripe.com",
    "sections": {
      "profile": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company",
          "data": {
            "company": {
              "name": "Stripe",
              "domain": "stripe.com",
              "alternate_names": [],
              "other_domains": [],
              "description": "Provider of financial infrastructure solutions for revenue growth and payment processing",
              "detailed_description": "Provider of financial infrastructure solutions for revenue growth and payment processing. It offers tools designed for individual or combined use to grow businesses. These tools enable payment acceptance and optimisation globally, both online and in person. The company facilitates various billing models and provides access to borderless money movement. It also offers resources for startups and platforms to build and scale their operations.",
              "founded": 2010,
              "logo_url": "https://s3.amazonaws.com/tracxn-data-image/logo/company/ce2961944191fef21464bbd2b3ea8d",
              "employee_count": 5904,
              "company_id": "1x532zlgk5",
              "classification": {
                "sectors": [
                  "FinTech"
                ],
                "markets": [
                  "Payments"
                ],
                "feeds": {
                  "primary": [
                    "Payments"
                  ],
                  "other": [
                    "Enterprise Tech - US",
                    "FinTech - US",
                    "Enterprise Tech - California",
                    "500 Startups Portfolio",
                    "SaaS",
                    "SaaS - US",
                    "Enterprise Software",
                    "Business Payments Solutions",
                    "Commerce Enablers",
                    "Y Combinator Batches"
                  ]
                },
                "business_models": [
                  "Business Payments",
                  "Online Payments"
                ],
                "revenue_models": [
                  "subscription"
                ],
                "industries": [
                  "internet"
                ],
                "company_types": [
                  "Corporate"
                ],
                "flags": {
                  "Tech": "YES",
                  "Consumer": "NO",
                  "Enterprise": "YES",
                  "Marketplace": "NO",
                  "SaaS": "YES",
                  "Software": "YES",
                  "Tech Hardware": "NO",
                  "Social Impact": "NO",
                  "Artificial Intelligence": "NO",
                  "Blockchain": "NO",
                  "Agentic AI": "Untagged"
                }
              },
              "people": {
                "key_people": [
                  {
                    "name": "John Collison",
                    "designation": "Co-Founder & President"
                  },
                  {
                    "name": "Patrick Collison",
                    "designation": "Co-Founder & CEO"
                  },
                  {
                    "name": "Maia Josebachevilli",
                    "designation": "Head of M&A"
                  },
                  {
                    "name": "Ross Sheil",
                    "designation": "Ex- Head of Venture Capital"
                  }
                ],
                "founders": [
                  {
                    "name": "John Collison",
                    "designation": "Co-Founder & President"
                  },
                  {
                    "name": "Patrick Collison",
                    "designation": "Co-Founder & CEO"
                  }
                ],
                "key_people_count": 4,
                "background_flags": [
                  {
                    "name": "Massachusetts Institute of Technology",
                    "category": "College Wise"
                  },
                  {
                    "name": "Serial Entrepreneur",
                    "category": "Top Rated Teams"
                  }
                ],
                "founder_selection": "Source designation contains founder; not an independent verification"
              },
              "technology": {
                "website_stack": [
                  "algolia",
                  "amazon cloudfront",
                  "amazon s3",
                  "amazon web services",
                  "apple icloud mail",
                  "bootstrap",
                  "cart functionality",
                  "cloudflare",
                  "cloudflare bot management",
                  "contentful",
                  "core-js",
                  "digicert",
                  "docusign",
                  "envoy",
                  "google analytics",
                  "google workspace",
                  "hcaptcha",
                  "hsts",
                  "jquery",
                  "jquery migrate",
                  "jquery ui",
                  "lodash",
                  "next.js",
                  "nginx",
                  "node.js",
                  "open graph",
                  "priority hints",
                  "prism",
                  "pwa",
                  "react",
                  "rss",
                  "sentry",
                  "stripe",
                  "three.js",
                  "webpack"
                ],
                "technographics": [],
                "observed_technologies": [
                  "algolia",
                  "amazon cloudfront",
                  "amazon s3",
                  "amazon web services",
                  "apple icloud mail",
                  "bootstrap",
                  "cart functionality",
                  "cloudflare",
                  "cloudflare bot management",
                  "core-js",
                  "docusign",
                  "google analytics",
                  "google workspace",
                  "hcaptcha",
                  "hsts",
                  "jquery",
                  "jquery migrate",
                  "jquery ui",
                  "lodash",
                  "next.js",
                  "nginx",
                  "node.js",
                  "open graph",
                  "priority hints",
                  "prism",
                  "pwa",
                  "react",
                  "rss",
                  "sentry",
                  "stripe",
                  "three.js",
                  "webpack"
                ],
                "observed_at": "2026-05-01"
              },
              "web_presence": {
                "rank": 10000,
                "rank_bucket": "top_10k",
                "popularity_label": "high",
                "tech_count": 32,
                "technologies": [
                  "algolia",
                  "amazon cloudfront",
                  "amazon s3",
                  "amazon web services",
                  "apple icloud mail",
                  "bootstrap",
                  "cart functionality",
                  "cloudflare",
                  "cloudflare bot management",
                  "core-js",
                  "docusign",
                  "google analytics",
                  "google workspace",
                  "hcaptcha",
                  "hsts",
                  "jquery",
                  "jquery migrate",
                  "jquery ui",
                  "lodash",
                  "next.js",
                  "nginx",
                  "node.js",
                  "open graph",
                  "priority hints",
                  "prism",
                  "pwa",
                  "react",
                  "rss",
                  "sentry",
                  "stripe",
                  "three.js",
                  "webpack"
                ],
                "cdn": "",
                "has_cdn": false,
                "perf": {
                  "cwv_label": "needs_improvement",
                  "lcp_label": "good",
                  "cls_label": "good",
                  "inp_label": "needs_improvement",
                  "page_weight_label": "light",
                  "dom_label": "complex",
                  "speed_label": "fast",
                  "bytes_total": 1835232,
                  "dom_elements": 2440,
                  "req_total": 103,
                  "ttfb_ms": 1007,
                  "speed_index": 4340
                },
                "seo": {
                  "maturity_label": "advanced",
                  "has_open_graph": true,
                  "has_twitter_card": true,
                  "img_alt_label": "poor",
                  "has_favicon": true,
                  "has_manifest": false,
                  "has_amp": false
                },
                "structured_data": {
                  "maturity_label": "basic",
                  "has_json_ld": true,
                  "has_microdata": false,
                  "has_rdfa": true,
                  "has_open_graph": true,
                  "has_twitter_card": true,
                  "schema_types": [],
                  "business_hints": []
                },
                "digital_presence_score": 86,
                "crawl_date": "2026-05-01"
              },
              "traffic": {
                "authority": 79,
                "global_rank": 167,
                "country_rank": 165,
                "country": "United States",
                "visits": 190046716,
                "visits_date": "2026-05-01",
                "bounce": 0.6053,
                "ppv": 2.8708,
                "keywords": [
                  {
                    "k": "stripe",
                    "pos": 1,
                    "vol": 550000
                  },
                  {
                    "k": "online payments",
                    "pos": 3,
                    "vol": 1000000
                  },
                  {
                    "k": "stripe careers",
                    "pos": 1,
                    "vol": 18100
                  },
                  {
                    "k": "stripe vacancies",
                    "pos": 1,
                    "vol": 14800
                  }
                ],
                "audience": [
                  {
                    "cc": "US",
                    "country": "United States",
                    "share": 0.2792,
                    "visits": 53060565
                  },
                  {
                    "cc": "GB",
                    "country": "United Kingdom",
                    "share": 0.0679,
                    "visits": 12908445
                  },
                  {
                    "cc": "DE",
                    "country": "Germany",
                    "share": 0.0483,
                    "visits": 9172588
                  },
                  {
                    "cc": "IN",
                    "country": "India",
                    "share": 0.0453,
                    "visits": 8602699
                  },
                  {
                    "cc": "NL",
                    "country": "Netherlands",
                    "share": 0.0359,
                    "visits": 6823857
                  }
                ]
              },
              "apps": {
                "count": 2,
                "downloads": 3000300,
                "weighted_rating": 4.400000095367432
              },
              "products": [
                "Payments",
                "Payouts",
                "API-based integration",
                "Low- to no-code solutions"
              ],
              "geography": {
                "hq_country": "United States",
                "hq_state": "California",
                "hq_city": "San Francisco",
                "country_code": "US",
                "coord": {
                  "type": "Point",
                  "coordinates": [
                    -122.41942,
                    37.77493
                  ]
                },
                "geo_served": [
                  "Japan",
                  "Australia",
                  "Thailand",
                  "India",
                  "United Kingdom",
                  "France",
                  "United States",
                  "United Arab Emirates",
                  "Sweden",
                  "Spain",
                  "Germany",
                  "Netherlands",
                  "Ireland",
                  "Poland",
                  "Singapore",
                  "Mexico",
                  "Indonesia",
                  "Brazil"
                ],
                "locations": [
                  {
                    "city": {
                      "name": "San Francisco"
                    },
                    "cityGroup": [
                      {
                        "name": "Bay Area"
                      }
                    ],
                    "state": {
                      "name": "California"
                    },
                    "country": {
                      "name": "United States"
                    },
                    "countryGroup": [
                      {
                        "name": "North America"
                      },
                      {
                        "name": "US & Canada"
                      }
                    ],
                    "continent": {
                      "name": "North America"
                    }
                  }
                ],
                "addresses": [
                  {
                    "text": "Revoluční 1403 11000 Praha",
                    "is_hq": false,
                    "pincode": null,
                    "country": "Czech Republic",
                    "country_id": "57ada336e4b0e0fbead7ef60"
                  },
                  {
                    "text": "San Francisco, California",
                    "is_hq": false,
                    "pincode": null,
                    "country": "United States",
                    "country_id": "57ada2f0e4b0e0fbead7ddfe"
                  },
                  {
                    "text": "Prestige Tech Pacific Park, 11th Floor, Building No. 2, Kadubeesanahalli Village, Varthur, Hobli, Bangalore East Taluk, Panathur, Bangalore, Bangalore South, Karnataka, India, 560103",
                    "is_hq": false,
                    "pincode": "560103",
                    "country": "India",
                    "country_id": "57ada2abe4b0e0fbead7d6da"
                  },
                  {
                    "text": "TREVIOT HOUSE,186-192 HIGH ROAD,ILFORD,ESSEX,IG1 1LR",
                    "is_hq": false,
                    "pincode": null,
                    "country": "United Kingdom",
                    "country_id": "57ada2b1e4b0e0fbead7d84b"
                  }
                ],
                "coord_precision": "city"
              },
              "social": {
                "links": {
                  "linkedin": "https://linkedin.com/company/stripe",
                  "x": "https://twitter.com/stripe",
                  "facebook": "https://facebook.com/stripehq",
                  "blog": "http://stripe.com/blog"
                },
                "followers": 1528731,
                "posts_12m": 4,
                "engagement_per_post": 0,
                "rate": 0.0,
                "cadence_per_month": 0.3,
                "sector": "Payments",
                "industry_median_rate": 0.00567,
                "ratio_vs_median": 0.0,
                "band": "below the industry typical range"
              },
              "lifecycle": {
                "stage": "Series I",
                "is_funded": true,
                "is_acquirer": true,
                "is_deadpooled": false,
                "deadpooled_date": null,
                "has_ever_been_public": false,
                "ownership": "Private",
                "financing_status": "VC-Backed"
              },
              "legal": [
                {
                  "name": "Stripe, Inc.",
                  "entity_id": "270465600",
                  "registrar": "Others",
                  "country": "United States"
                },
                {
                  "name": "SQUARE MILE BUSINESS SERVICES LIMITED",
                  "entity_id": "4675506",
                  "registrar": "companieshouse.gov.uk",
                  "country": "United Kingdom"
                },
                {
                  "name": "STRIPE WOOD s.r.o.",
                  "entity_id": "08667900",
                  "registrar": "czso.cz",
                  "country": "Czech Republic"
                },
                {
                  "name": "STRIPE INDIA PRIVATE LIMITED",
                  "entity_id": "U72200KA2016FTC096320",
                  "registrar": "mca.gov.in",
                  "country": "India"
                },
                {
                  "name": "Stripe Payments Singapore Pte. Ltd",
                  "entity_id": "201524528H",
                  "registrar": "acra.gov.sg",
                  "country": "Singapore"
                }
              ],
              "assessments": {
                "completion": 91,
                "finance": 42,
                "scalability": 100,
                "momentum": 65,
                "data_confidence": 60,
                "maturity": 64,
                "innovation": 36,
                "prominence": 75
              },
              "hiring": {
                "total": 368,
                "last_dt": "2026-09-16",
                "first_dt": "2024-05-08",
                "active_12m": 13,
                "avg_12m": 21.9,
                "freq_label": "Hires continuously",
                "freq_detail": "263 roles tracked across 13 of the last 12 months",
                "months": [
                  {
                    "m": "2024-11",
                    "n": 3
                  },
                  {
                    "m": "2025-01",
                    "n": 5
                  },
                  {
                    "m": "2025-03",
                    "n": 6
                  },
                  {
                    "m": "2025-04",
                    "n": 7
                  },
                  {
                    "m": "2025-05",
                    "n": 2
                  },
                  {
                    "m": "2025-06",
                    "n": 16
                  },
                  {
                    "m": "2025-07",
                    "n": 19
                  },
                  {
                    "m": "2025-08",
                    "n": 23
                  },
                  {
                    "m": "2025-09",
                    "n": 30
                  },
                  {
                    "m": "2025-10",
                    "n": 32
                  },
                  {
                    "m": "2025-11",
                    "n": 42
                  },
                  {
                    "m": "2025-12",
                    "n": 18
                  },
                  {
                    "m": "2026-01",
                    "n": 33
                  },
                  {
                    "m": "2026-02",
                    "n": 16
                  },
                  {
                    "m": "2026-03",
                    "n": 6
                  },
                  {
                    "m": "2026-04",
                    "n": 15
                  },
                  {
                    "m": "2026-05",
                    "n": 29
                  },
                  {
                    "m": "2026-06",
                    "n": 20
                  },
                  {
                    "m": "2026-07",
                    "n": 9
                  },
                  {
                    "m": "2026-08",
                    "n": 9
                  },
                  {
                    "m": "2026-09",
                    "n": 4
                  }
                ],
                "years": [
                  {
                    "y": "2024",
                    "n": 31
                  },
                  {
                    "y": "2025",
                    "n": 200
                  },
                  {
                    "y": "2026",
                    "n": 141
                  }
                ],
                "recent": [
                  {
                    "d": "2026-09-16",
                    "title": "Head of Finance Operations",
                    "location": "Bangalore"
                  },
                  {
                    "d": "2026-09-07",
                    "title": "Contracting Operations Specialist | Bangalore, IN",
                    "location": "Bangalore"
                  },
                  {
                    "d": "2026-09-07",
                    "title": "Fraud Operations Manager",
                    "location": "Bangalore"
                  },
                  {
                    "d": "2026-09-05",
                    "title": "Software Engineer, New Grad",
                    "location": "Bangalore"
                  },
                  {
                    "d": "2026-08-27",
                    "title": "RN CLIN DOCUMENTATION COORD, FCH - ENTERPRISE QUALITY CDI/UR/DM",
                    "location": "All India"
                  },
                  {
                    "d": "2026-08-27",
                    "title": "Credit Risk Operations Team Lead",
                    "location": "Bangalore"
                  },
                  {
                    "d": "2026-08-21",
                    "title": "Operations Associate, GTM Accelerate (Bangalore)",
                    "location": "Bangalore"
                  },
                  {
                    "d": "2026-08-16",
                    "title": "Data Science Manager, Risk (Bengaluru)",
                    "location": "Bangalore"
                  },
                  {
                    "d": "2026-08-16",
                    "title": "Marketing Services Program Manager",
                    "location": "Bangalore"
                  },
                  {
                    "d": "2026-08-11",
                    "title": "Staff Engineer, Revenue (Bengaluru)",
                    "location": "Bangalore"
                  }
                ],
                "roles": [
                  "Technical Account Manager",
                  "People Partner",
                  "Corporate Strategy",
                  "Broadcast Engineer",
                  "Staff Security Engineer, Security Partnerships",
                  "EMEA Real Estate Transaction Manager",
                  "Design Recruiter",
                  "Company Strategy & Operations"
                ],
                "locations": [
                  "Toronto",
                  "South San Francisco",
                  "Chicago",
                  "Seattle",
                  "San Francisco",
                  "Bengaluru / Bangalore, Karnataka, India",
                  "New York",
                  "Atlanta"
                ]
              },
              "innovation": {
                "families": 276,
                "granted": 188,
                "citations": 10175,
                "years": [
                  {
                    "y": "2013",
                    "n": 1
                  },
                  {
                    "y": "2017",
                    "n": 7
                  },
                  {
                    "y": "2018",
                    "n": 10
                  },
                  {
                    "y": "2019",
                    "n": 12
                  },
                  {
                    "y": "2020",
                    "n": 11
                  },
                  {
                    "y": "2021",
                    "n": 23
                  },
                  {
                    "y": "2022",
                    "n": 51
                  },
                  {
                    "y": "2023",
                    "n": 100
                  },
                  {
                    "y": "2024",
                    "n": 134
                  },
                  {
                    "y": "2025",
                    "n": 143
                  },
                  {
                    "y": "2026",
                    "n": 36
                  }
                ],
                "areas": [
                  "Physics & computing",
                  "Electricity & electronics"
                ],
                "momentum": "accelerating",
                "notable": [
                  {
                    "title": "Method and apparatus for ordering goods, services and content over an internetwork using a virtual payment account",
                    "citations": 390,
                    "y": "2023"
                  },
                  {
                    "title": "System and method for indicating entry of personal identification number",
                    "citations": 110,
                    "y": "2024"
                  },
                  {
                    "title": "Methods and systems for providing payment interface services using a payment platform",
                    "citations": 92,
                    "y": "2025"
                  }
                ]
              },
              "activity": [
                {
                  "d": "2026-06-22",
                  "type": "product_launch",
                  "label": "Product launch",
                  "detail": "Stripe Directory"
                }
              ],
              "reputation": {
                "score": 1.7,
                "stars": 1,
                "n": 17267,
                "n_12m": 1226,
                "category": "Payment Service"
              },
              "share_of_voice": {
                "home_cc": "us",
                "home_country": "United States",
                "peers": [
                  {
                    "domain": "stripe.com",
                    "name": "Stripe",
                    "world_visits": 190046716,
                    "home_visits": 53060565,
                    "followers": 1528731,
                    "reviews": 17267
                  },
                  {
                    "domain": "gocardless.com",
                    "name": "GoCardless",
                    "world_visits": 2688810,
                    "home_visits": 301098,
                    "followers": 70647,
                    "reviews": 2438
                  },
                  {
                    "domain": "sba.gov",
                    "name": "u.s. small business administration",
                    "world_visits": 3959133,
                    "home_visits": 3721219,
                    "followers": 277487,
                    "reviews": 15
                  },
                  {
                    "domain": "airwallex.com",
                    "name": "Airwallex",
                    "world_visits": 9558412,
                    "home_visits": 3704482,
                    "followers": 178694,
                    "reviews": 2493
                  },
                  {
                    "domain": "stripeandstare.com",
                    "name": "Stripe & Stare",
                    "world_visits": 119042,
                    "home_visits": 20833,
                    "followers": 5227,
                    "reviews": 1651
                  },
                  {
                    "domain": "stripersonline.com",
                    "name": "stripersonline.com",
                    "world_visits": 88627,
                    "home_visits": 80103,
                    "followers": null,
                    "reviews": null
                  }
                ],
                "shares": {
                  "world_traffic": {
                    "stripe.com": 0.9205,
                    "gocardless.com": 0.013,
                    "sba.gov": 0.0192,
                    "airwallex.com": 0.0463,
                    "stripeandstare.com": 0.0006,
                    "stripersonline.com": 0.0004
                  },
                  "home_traffic": {
                    "stripe.com": 0.8714,
                    "gocardless.com": 0.0049,
                    "sba.gov": 0.0611,
                    "airwallex.com": 0.0608,
                    "stripeandstare.com": 0.0003,
                    "stripersonline.com": 0.0013
                  },
                  "followers": {
                    "stripe.com": 0.7418,
                    "gocardless.com": 0.0343,
                    "sba.gov": 0.1347,
                    "airwallex.com": 0.0867,
                    "stripeandstare.com": 0.0025
                  },
                  "reviews": {
                    "stripe.com": 0.7236,
                    "gocardless.com": 0.1022,
                    "sba.gov": 0.0006,
                    "airwallex.com": 0.1045,
                    "stripeandstare.com": 0.0692
                  }
                }
              }
            },
            "profile_depth": "detailed",
            "updated_at": "2026-06-01T04:43:22.775000+00:00",
            "coverage": {
              "sections": {
                "classification": {
                  "available": true,
                  "status": "available"
                },
                "people": {
                  "available": true,
                  "status": "available"
                },
                "technology": {
                  "available": true,
                  "status": "available"
                },
                "web_presence": {
                  "available": true,
                  "status": "available"
                },
                "traffic": {
                  "available": true,
                  "status": "available"
                },
                "apps": {
                  "available": true,
                  "status": "available"
                },
                "products": {
                  "available": true,
                  "status": "available"
                },
                "geography": {
                  "available": true,
                  "status": "available"
                },
                "social": {
                  "available": true,
                  "status": "available"
                },
                "lifecycle": {
                  "available": true,
                  "status": "available"
                },
                "legal": {
                  "available": true,
                  "status": "available"
                },
                "assessments": {
                  "available": true,
                  "status": "available"
                },
                "hiring": {
                  "available": true,
                  "status": "available"
                },
                "innovation": {
                  "available": true,
                  "status": "available"
                },
                "activity": {
                  "available": true,
                  "status": "available"
                },
                "reputation": {
                  "available": true,
                  "status": "available"
                },
                "share_of_voice": {
                  "available": true,
                  "status": "available"
                }
              },
              "arrays": {
                "/company/classification/sectors": {
                  "available": 1,
                  "returned": 1,
                  "truncated": false
                },
                "/company/classification/markets": {
                  "available": 1,
                  "returned": 1,
                  "truncated": false
                },
                "/company/classification/feeds/primary": {
                  "available": 1,
                  "returned": 1,
                  "truncated": false
                },
                "/company/classification/feeds/other": {
                  "available": 10,
                  "returned": 10,
                  "truncated": false
                },
                "/company/classification/business_models": {
                  "available": 2,
                  "returned": 2,
                  "truncated": false
                },
                "/company/classification/revenue_models": {
                  "available": 1,
                  "returned": 1,
                  "truncated": false
                },
                "/company/classification/industries": {
                  "available": 1,
                  "returned": 1,
                  "truncated": false
                },
                "/company/classification/company_types": {
                  "available": 1,
                  "returned": 1,
                  "truncated": false
                },
                "/company/people/key_people": {
                  "available": 4,
                  "returned": 4,
                  "truncated": false
                },
                "/company/people/founders": {
                  "available": 2,
                  "returned": 2,
                  "truncated": false
                },
                "/company/people/background_flags": {
                  "available": 2,
                  "returned": 2,
                  "truncated": false
                },
                "/company/technology/website_stack": {
                  "available": 35,
                  "returned": 35,
                  "truncated": false
                },
                "/company/technology/technographics": {
                  "available": 0,
                  "returned": 0,
                  "truncated": false
                },
                "/company/technology/observed_technologies": {
                  "available": 32,
                  "returned": 32,
                  "truncated": false
                },
                "/company/web_presence/technologies": {
                  "available": 32,
                  "returned": 32,
                  "truncated": false
                },
                "/company/web_presence/structured_data/schema_types": {
                  "available": 0,
                  "returned": 0,
                  "truncated": false
                },
                "/company/web_presence/structured_data/business_hints": {
                  "available": 0,
                  "returned": 0,
                  "truncated": false
                },
                "/company/traffic/keywords": {
                  "available": 4,
                  "returned": 4,
                  "truncated": false
                },
                "/company/traffic/audience": {
                  "available": 5,
                  "returned": 5,
                  "truncated": false
                },
                "/company/products": {
                  "available": 4,
                  "returned": 4,
                  "truncated": false
                },
                "/company/geography/coord/coordinates": {
                  "available": 2,
                  "returned": 2,
                  "truncated": false
                },
                "/company/geography/geo_served": {
                  "available": 18,
                  "returned": 18,
                  "truncated": false
                },
                "/company/geography/locations": {
                  "available": 1,
                  "returned": 1,
                  "truncated": false
                },
                "/company/geography/locations/0/cityGroup": {
                  "available": 1,
                  "returned": 1,
                  "truncated": false
                },
                "/company/geography/locations/0/countryGroup": {
                  "available": 2,
                  "returned": 2,
                  "truncated": false
                },
                "/company/geography/addresses": {
                  "available": 4,
                  "returned": 4,
                  "truncated": false
                },
                "/company/legal": {
                  "available": 5,
                  "returned": 5,
                  "truncated": false
                },
                "/company/hiring/months": {
                  "available": 21,
                  "returned": 21,
                  "truncated": false
                },
                "/company/hiring/years": {
                  "available": 3,
                  "returned": 3,
                  "truncated": false
                },
                "/company/hiring/recent": {
                  "available": 10,
                  "returned": 10,
                  "truncated": false
                },
                "/company/hiring/roles": {
                  "available": 8,
                  "returned": 8,
                  "truncated": false
                },
                "/company/hiring/locations": {
                  "available": 8,
                  "returned": 8,
                  "truncated": false
                },
                "/company/innovation/years": {
                  "available": 11,
                  "returned": 11,
                  "truncated": false
                },
                "/company/innovation/areas": {
                  "available": 2,
                  "returned": 2,
                  "truncated": false
                },
                "/company/innovation/notable": {
                  "available": 3,
                  "returned": 3,
                  "truncated": false
                },
                "/company/activity": {
                  "available": 1,
                  "returned": 1,
                  "truncated": false
                },
                "/company/reputation/snippets": {
                  "available": 3,
                  "returned": 3,
                  "truncated": false
                },
                "/company/share_of_voice/peers": {
                  "available": 6,
                  "returned": 6,
                  "truncated": false
                }
              },
              "partial": false
            },
            "financial_history": "Use get_financials; financial archive and estimated-revenue access remain upstream-controlled"
          },
          "window": {
            "data_through": null
          },
          "meta": {
            "retrieved_at": "2026-09-20T06:35:41.320426+00:00",
            "partial": false,
            "notes": [
              "Profile scores and founder categories are source assessments; app totals do not include an app-by-app roster."
            ],
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
            "domain": "stripe.com",
            "statement": "all",
            "has_data": true,
            "periods": [
              {
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
              {
                "period": "FY2020",
                "fiscal_year": 2020,
                "fiscal_period": "FY",
                "period_end": null,
                "reported_date": "2021-10-05",
                "filed_date": null,
                "form_type": null,
                "metrics": {
                  "net_income": {
                    "value": -138200000,
                    "currency": "USD",
                    "unit": "absolute",
                    "source_type": "news_report",
                    "native_value": null,
                    "native_currency": null
                  },
                  "revenue": {
                    "value": 7400000000,
                    "currency": "USD",
                    "unit": "absolute",
                    "source_type": "news_report",
                    "native_value": null,
                    "native_currency": null
                  }
                },
                "article_ids": [
                  "677d37b5f5048a28df250dac"
                ],
                "currency_conversion": null
              },
              {
                "period": "FY2019",
                "fiscal_year": 2019,
                "fiscal_period": "FY",
                "period_end": null,
                "reported_date": "2021-05-06",
                "filed_date": null,
                "form_type": null,
                "metrics": {
                  "net_income": {
                    "value": 46900000,
                    "currency": "USD",
                    "unit": "absolute",
                    "source_type": "news_report",
                    "native_value": null,
                    "native_currency": null
                  },
                  "revenue": {
                    "value": 800400000,
                    "currency": "USD",
                    "unit": "absolute",
                    "source_type": "news_report",
                    "native_value": null,
                    "native_currency": null
                  }
                },
                "article_ids": [
                  "677d37086730ec3c22fc08d6"
                ],
                "currency_conversion": null
              }
            ],
            "returned": 3,
            "truncated": false,
            "access_limited": false,
            "available_period_count": 3,
            "computed_at": "2026-09-20T06:35:42.859000Z",
            "summary": {
              "narrative": "Latest reported FY2024: revenue $500M. Growth has been erratic across reported periods. Recent signals: Reported a loss, Record revenue, Profitable."
            }
          },
          "window": {
            "data_through": "2025-02-28"
          },
          "meta": {
            "retrieved_at": "2026-09-20T06:35:42.866827+00:00",
            "partial": false,
            "notes": [
              "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
              "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies."
            ],
            "provider": "Fliar BI"
          }
        }
      },
      "intelligence": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company_intelligence",
          "data": {
            "domain": "stripe.com",
            "intel": {
              "company_meta": {
                "country": "united states",
                "current_stage": "Series I",
                "estimated_revenue": null,
                "progress_label": "",
                "size_label": "giant",
                "markets": [
                  "payments"
                ],
                "total_funding": null,
                "valuation": 65000000000
              },
              "computed_at": "2026-09-20T06:35:42Z",
              "earnings": {
                "balance_sheet": null,
                "estimated_revenue_usd": null,
                "gated": false,
                "growth_consistency": 0,
                "has_data": true,
                "history": [
                  {
                    "beat_or_miss": null,
                    "cash_usd": null,
                    "coverage_count": 1,
                    "currency_native": "",
                    "date": "2025-02-28",
                    "ebitda_usd": null,
                    "employees": null,
                    "eps": null,
                    "article_id": "69982217a9a137bc0bdfce10",
                    "metric_sources": {
                      "revenue_usd": "news_report"
                    },
                    "filed_date": null,
                    "form_type": "",
                    "fx_source": "",
                    "gross_profit_usd": null,
                    "guidance_revenue": null,
                    "has_official": false,
                    "long_term_debt_usd": null,
                    "native": {},
                    "net_income_growth_pct": null,
                    "net_income_usd": null,
                    "operating_cash_flow_usd": null,
                    "operating_income_usd": null,
                    "period_has_official": false,
                    "period_label": "FY2024",
                    "period_qtr": "FY",
                    "period_sort": 20245,
                    "period_year": 2024,
                    "source_type": "news_report",
                    "quality_signals": [],
                    "revenue_growth_pct": null,
                    "revenue_usd": 500000000,
                    "article_ids": [
                      "69982217a9a137bc0bdfce10"
                    ],
                    "stockholders_equity_usd": null,
                    "total_assets_usd": null,
                    "total_liabilities_usd": null
                  },
                  {
                    "beat_or_miss": null,
                    "cash_usd": null,
                    "coverage_count": 1,
                    "currency_native": "",
                    "date": "2021-10-05",
                    "ebitda_usd": null,
                    "employees": null,
                    "eps": null,
                    "article_id": "677d37b5f5048a28df250dac",
                    "metric_sources": {
                      "net_income_usd": "news_report",
                      "revenue_usd": "news_report"
                    },
                    "filed_date": null,
                    "form_type": "",
                    "fx_source": "",
                    "gross_profit_usd": null,
                    "guidance_revenue": null,
                    "has_official": false,
                    "long_term_debt_usd": null,
                    "native": {},
                    "net_income_growth_pct": null,
                    "net_income_usd": -138200000,
                    "operating_cash_flow_usd": null,
                    "operating_income_usd": null,
                    "period_has_official": false,
                    "period_label": "FY2020",
                    "period_qtr": "FY",
                    "period_sort": 20205,
                    "period_year": 2020,
                    "source_type": "news_report",
                    "quality_signals": [
                      "Reported a loss",
                      "Record revenue"
                    ],
                    "revenue_growth_pct": 70.0,
                    "revenue_usd": 7400000000,
                    "article_ids": [
                      "677d37b5f5048a28df250dac"
                    ],
                    "stockholders_equity_usd": null,
                    "total_assets_usd": null,
                    "total_liabilities_usd": null
                  },
                  {
                    "beat_or_miss": null,
                    "cash_usd": null,
                    "coverage_count": 1,
                    "currency_native": "",
                    "date": "2021-05-06",
                    "ebitda_usd": null,
                    "employees": null,
                    "eps": null,
                    "article_id": "677d37086730ec3c22fc08d6",
                    "metric_sources": {
                      "net_income_usd": "news_report",
                      "revenue_usd": "news_report"
                    },
                    "filed_date": null,
                    "form_type": "",
                    "fx_source": "",
                    "gross_profit_usd": null,
                    "guidance_revenue": null,
                    "has_official": false,
                    "long_term_debt_usd": null,
                    "native": {},
                    "net_income_growth_pct": null,
                    "net_income_usd": 46900000,
                    "operating_cash_flow_usd": null,
                    "operating_income_usd": null,
                    "period_has_official": false,
                    "period_label": "FY2019",
                    "period_qtr": "FY",
                    "period_sort": 20195,
                    "period_year": 2019,
                    "source_type": "news_report",
                    "quality_signals": [
                      "Profitable"
                    ],
                    "revenue_growth_pct": null,
                    "revenue_usd": 800400000,
                    "article_ids": [
                      "677d37086730ec3c22fc08d6"
                    ],
                    "stockholders_equity_usd": null,
                    "total_assets_usd": null,
                    "total_liabilities_usd": null
                  }
                ],
                "history_public_count": 3,
                "history_total_count": 3,
                "latest": {
                  "beat_or_miss": null,
                  "cash_usd": null,
                  "coverage_count": 1,
                  "currency_native": "",
                  "date": "2025-02-28",
                  "ebitda_usd": null,
                  "employees": null,
                  "eps": null,
                  "article_id": "69982217a9a137bc0bdfce10",
                  "metric_sources": {
                    "revenue_usd": "news_report"
                  },
                  "filed_date": null,
                  "form_type": "",
                  "fx_source": "",
                  "gross_profit_usd": null,
                  "guidance_revenue": null,
                  "has_official": false,
                  "long_term_debt_usd": null,
                  "native": {},
                  "net_income_growth_pct": null,
                  "net_income_usd": null,
                  "operating_cash_flow_usd": null,
                  "operating_income_usd": null,
                  "period_has_official": false,
                  "period_label": "FY2024",
                  "period_qtr": "FY",
                  "period_sort": 20245,
                  "period_year": 2024,
                  "source_type": "news_report",
                  "quality_signals": [],
                  "revenue_growth_pct": null,
                  "revenue_usd": 500000000,
                  "article_ids": [
                    "69982217a9a137bc0bdfce10"
                  ],
                  "stockholders_equity_usd": null,
                  "total_assets_usd": null,
                  "total_liabilities_usd": null
                },
                "narrative": "Latest reported FY2024: revenue $500M. Growth has been erratic across reported periods. Recent signals: Reported a loss, Record revenue, Profitable.",
                "official_coverage": {
                  "bi_periods": 3,
                  "currencies": [],
                  "form_types": [],
                  "fx_converted": false,
                  "official_periods": 0
                },
                "prior": null,
                "quality_signals_aggregate": [
                  "Reported a loss",
                  "Record revenue",
                  "Profitable"
                ],
                "score": 48,
                "source": "earnings_table",
                "source_count": 4,
                "yoy_basis": null,
                "yoy_multiple": null,
                "yoy_pct": null
              },
              "events_by_role": {
                "acquirer": 25,
                "client": 12,
                "contractor": 7,
                "primary": 216
              },
              "events_by_type": {
                "buyback": 4,
                "capital_infusion": 8,
                "company_announcement": 35,
                "contracts": 19,
                "earnings": 4,
                "funding_rounds": 52,
                "funds_raising": 1,
                "ipo": 2,
                "job_creation": 12,
                "key_people": 39,
                "layoffs": 14,
                "ma": 25,
                "new_product": 36,
                "regulatory": 9
              },
              "events_by_year": {
                "2011": 1,
                "2012": 1,
                "2013": 2,
                "2014": 8,
                "2015": 1,
                "2016": 9,
                "2017": 1,
                "2018": 5,
                "2019": 11,
                "2020": 37,
                "2021": 48,
                "2022": 34,
                "2023": 37,
                "2024": 26,
                "2025": 29,
                "2026": 10
              },
              "financial_trajectory": {
                "buyback_events": 4,
                "funding_events_360d": 1,
                "funding_events_lifetime": 61,
                "highest_stage": "Public",
                "highest_stage_rank": 12,
                "ipo_events": 2,
                "narrative": "Strong financial trajectory: 61 funding events lifetime reaching Public; 1 in last 12 months.",
                "score": 86,
                "stage_pace_years": 0.3
              },
              "innovation_index": {
                "announcements_360d": 2,
                "fda_approvals": 0,
                "narrative": "Slow product cadence: 36 lifetime launches, 1 in last year.",
                "new_products_360d": 1,
                "new_products_lifetime": 36,
                "score": 12,
                "velocity_change_pct": -80.0
              },
              "investment_readiness": {
                "breakdown": {
                  "earnings": 48,
                  "financial_trajectory": 86,
                  "innovation": 12,
                  "management": 90,
                  "market_position": 42,
                  "risk": 0
                },
                "label": "Moderate",
                "private_equity_score": 59,
                "public_shares_score": 52,
                "recommendation": "Mixed signals; tilt depends on whether the upside or risk drivers matter more for your thesis.",
                "score": 55
              },
              "management_quality": {
                "board_updates_360d": 0,
                "ceo_cfo_change_signals_90d": 0,
                "ceo_transition_window_years": 4,
                "ceo_transitions": [],
                "ceo_transitions_count": 0,
                "churn_penalty": 0,
                "key_people_events_360d": 1,
                "key_people_events_all": 39,
                "leadership_churn": false,
                "leadership_churn_level": "none",
                "narrative": "Leadership shows strong stability — modest exec movement and no CEO/CFO change signals in the last 90 days.",
                "score": 90,
                "warning_flags": []
              },
              "market_position": {
                "asset_acquisitions": 0,
                "asset_roles": {},
                "contracts_360d": 4,
                "contracts_all": 19,
                "ma_involvement": {
                  "acquirer": 25
                },
                "ma_total": 25,
                "narrative": "Moderate market footprint — 4 recent contracts, 25 M&A events.",
                "partnerships_all": 0,
                "score": 42
              },
              "peer_comparison": {
                "cohort_size": 128,
                "country": "united states",
                "event_count_percentile": 0,
                "event_count_quantiles": {
                  "p25": 1,
                  "p50": 3,
                  "p75": 5,
                  "p90": 12,
                  "p95": 24
                },
                "market": "payments",
                "innovation_percentile": 25,
                "innovation_quantiles": {
                  "p50": 0,
                  "p90": 3,
                  "p95": 4
                },
                "risk_percentile": 25,
                "risk_quantiles": {
                  "p50": 0,
                  "p90": 0,
                  "p95": 1
                },
                "this_company": {
                  "event_count": 0,
                  "innovation": 0,
                  "risk": 0
                }
              },
              "raw_event_count": 260,
              "risk_profile": {
                "bankruptcy_events": 0,
                "lawsuits_360d": 0,
                "lawsuits_all": 0,
                "lawsuits_as_defendant": 0,
                "layoffs_180d": 0,
                "narrative": "Clean risk profile — no lawsuits, regulatory, or layoff events on record.",
                "regulatory_360d": 0,
                "score": 0,
                "warning_flags": []
              }
            },
            "computed_at": "2026-09-20T06:35:42.892000Z"
          },
          "window": {
            "data_through": null
          },
          "meta": {
            "retrieved_at": "2026-09-20T06:35:42.898920+00:00",
            "partial": false,
            "notes": [
              "Scores and narratives are derived assessments. Financial metrics are retrieved evidence."
            ],
            "provider": "Fliar BI"
          }
        }
      },
      "events": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company_events",
          "data": {
            "freshness": {
              "future_rows_count": 0,
              "future_rows_filtered": false,
              "latest_event_date": "2026-04-15",
              "latest_inserted_at": "2026-09-20T05:30:00+05:30"
            },
            "truncated": true,
            "buckets_by_month": {},
            "domain": "stripe.com",
            "events": [],
            "plan": "free",
            "pulse": {
              "badges": [
                "Possible Fundraise"
              ],
              "ceo_transitions": 0,
              "churn_penalty": 0,
              "days_since_latest": 999,
              "event_variety_360d": 3,
              "events_30d_fresh": 0,
              "events_360d": 4,
              "events_prev_360d": 17,
              "label": "Dormant",
              "leadership_churn": false,
              "leadership_churn_level": "none",
              "momentum_pct": -76.5,
              "opportunity_score": 0,
              "risk_score": 0,
              "score": 1,
              "top_drivers": [
                {
                  "count": 2,
                  "event_type": "company_announcement",
                  "label": "Company Announcement"
                },
                {
                  "count": 1,
                  "event_type": "key_people",
                  "label": "Key People Movement"
                },
                {
                  "count": 1,
                  "event_type": "funding_rounds",
                  "label": "Funding"
                }
              ],
              "window_days": 360
            },
            "totals_by_type": {},
            "window_days": 30
          },
          "window": {
            "data_through": "2026-04-15",
            "effective_days": 30,
            "requested_days": 30
          },
          "meta": {
            "retrieved_at": "2026-09-20T06:35:41.617536+00:00",
            "partial": false,
            "notes": [],
            "provider": "Fliar BI"
          }
        }
      },
      "funding": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company_funding",
          "data": {
            "amount_approx": true,
            "events": [
              {
                "amount": 2000000,
                "date": "2026-03-26",
                "round_type": "Seed"
              },
              {
                "amount": 0,
                "date": "2025-03-12",
                "round_type": "Equity"
              },
              {
                "amount": 1800000000,
                "date": "2024-08-30",
                "round_type": "Series??"
              },
              {
                "amount": 6800000000,
                "date": "2023-08-10",
                "round_type": "Equity"
              },
              {
                "amount": 6500000000,
                "date": "2023-03-15",
                "round_type": "Series I"
              },
              {
                "amount": 0,
                "date": "2022-04-12",
                "round_type": "Venture Capital"
              },
              {
                "amount": 600000000,
                "date": "2021-08-10",
                "round_type": "Raise"
              },
              {
                "amount": 1000000000,
                "date": "2021-06-14",
                "round_type": "Funding round"
              },
              {
                "amount": 600000000,
                "date": "2021-03-15",
                "round_type": "Series H"
              },
              {
                "amount": 600000000,
                "date": "2020-07-30",
                "round_type": "Funding round"
              }
            ],
            "investors": [
              {
                "current_investment": [
                  "Seed",
                  2026
                ],
                "domain": "sequoiacap.com",
                "company_id": 71884,
                "name": "sequoia capital",
                "slug": "sequoia-capital",
                "description": "Sequoia Capital is a VC firm that invests in startups in the energy, financial, enterprise, healthcare, internet, and mobile industries."
              },
              {
                "current_investment": [
                  "Series??",
                  2024
                ],
                "domain": "thrivecap.com",
                "company_id": 1030626,
                "name": "thrive capital",
                "slug": "thrive-capital",
                "description": "Thrive Capital is an investment firm that builds and invests in internet, software, and technology-enabled companies."
              },
              {
                "current_investment": [
                  "Series I",
                  2023
                ],
                "name": "General Catalyst Partners"
              },
              {
                "current_investment": [
                  "Series I",
                  2023
                ],
                "name": "Founders Fund Management"
              }
            ],
            "rounds": [
              {
                "amount": 2000000,
                "date": "2026-03-26",
                "investors": [
                  {
                    "name": "sequoia capital",
                    "domain": "sequoiacap.com"
                  }
                ],
                "name": "Seed"
              },
              {
                "amount": 0,
                "date": "2025-03-12",
                "investors": [],
                "name": "Equity"
              },
              {
                "amount": 1800000000,
                "date": "2024-08-30",
                "investors": [
                  {
                    "name": "thrive capital",
                    "domain": "thrivecap.com"
                  }
                ],
                "name": "Series??"
              },
              {
                "amount": 6800000000,
                "date": "2023-08-10",
                "investors": [],
                "name": "Equity"
              },
              {
                "amount": 6500000000,
                "date": "2023-03-15",
                "investors": [
                  {
                    "name": "thrive capital",
                    "domain": "thrivecap.com"
                  },
                  {
                    "name": "General Catalyst Partners",
                    "domain": ""
                  },
                  {
                    "name": "Founders Fund Management",
                    "domain": ""
                  },
                  {
                    "name": "Andreessen Horowitz",
                    "domain": ""
                  },
                  {
                    "name": "goldman sachs",
                    "domain": "goldmansachs.com"
                  },
                  {
                    "name": "jp morgan",
                    "domain": "jpmorgan.com"
                  },
                  {
                    "name": "gic",
                    "domain": "gic.com.sg"
                  },
                  {
                    "name": "Goldman Sachs Asset and Wealth Management",
                    "domain": ""
                  },
                  {
                    "name": "temasek",
                    "domain": "temasek.com.sg"
                  },
                  {
                    "name": "baillie gifford",
                    "domain": "bailliegifford.com"
                  },
                  {
                    "name": "founders fund",
                    "domain": "foundersfund.com"
                  },
                  {
                    "name": "general catalyst",
                    "domain": "generalcatalyst.com"
                  },
                  {
                    "name": "msd partners",
                    "domain": "msdpartners.com"
                  }
                ],
                "name": "Series I"
              },
              {
                "amount": 0,
                "date": "2022-04-12",
                "investors": [
                  {
                    "name": "Meta Platforms",
                    "domain": "meta.com"
                  },
                  {
                    "name": "mckinsey",
                    "domain": "mckinseyalston.com"
                  }
                ],
                "name": "Venture Capital"
              },
              {
                "amount": 600000000,
                "date": "2021-08-10",
                "investors": [],
                "name": "Raise"
              },
              {
                "amount": 1000000000,
                "date": "2021-06-14",
                "investors": [
                  {
                    "name": "shopify",
                    "domain": "shopify.com"
                  },
                  {
                    "name": "capital group",
                    "domain": "capitalgroup.com"
                  },
                  {
                    "name": "sequoia capital",
                    "domain": "sequoiacap.com"
                  },
                  {
                    "name": "silver lake",
                    "domain": "silverlake.com"
                  }
                ],
                "name": "Funding round"
              },
              {
                "amount": 600000000,
                "date": "2021-03-15",
                "investors": [
                  {
                    "name": "tiger global management",
                    "domain": "tigerglobal.com"
                  },
                  {
                    "name": "dst global",
                    "domain": "dst-global.com"
                  },
                  {
                    "name": "sequoia capital",
                    "domain": "sequoiacap.com"
                  },
                  {
                    "name": "allianz x",
                    "domain": "allianzx.com"
                  },
                  {
                    "name": "axa",
                    "domain": "axa-egypt.com"
                  },
                  {
                    "name": "baillie gifford",
                    "domain": "bailliegifford.com"
                  },
                  {
                    "name": "Fidelity Management & Research Company",
                    "domain": ""
                  },
                  {
                    "name": "Ireland’s National Treasury Management Agency (NTMA)",
                    "domain": ""
                  },
                  {
                    "name": "ireland strategic investment fund",
                    "domain": "isif.ie"
                  },
                  {
                    "name": "Ireland's National Treasury Management Agency (NTMA)",
                    "domain": ""
                  }
                ],
                "name": "Series H"
              },
              {
                "amount": 600000000,
                "date": "2020-07-30",
                "investors": [],
                "name": "Funding round"
              },
              {
                "amount": 600000000,
                "date": "2020-04-16",
                "investors": [
                  {
                    "name": "Andreessen Horowitz",
                    "domain": ""
                  },
                  {
                    "name": "general catalyst",
                    "domain": "generalcatalyst.com"
                  },
                  {
                    "name": "Alphabet's GV",
                    "domain": ""
                  },
                  {
                    "name": "sequoia capital",
                    "domain": "sequoiacap.com"
                  },
                  {
                    "name": "GV",
                    "domain": ""
                  },
                  {
                    "name": "sequoia",
                    "domain": "sequoia.com.au"
                  }
                ],
                "name": "Series G"
              },
              {
                "amount": 250000000,
                "date": "2019-09-21",
                "investors": [
                  {
                    "name": "general catalyst",
                    "domain": "generalcatalyst.com"
                  },
                  {
                    "name": "sequoia",
                    "domain": "sequoia.com.au"
                  },
                  {
                    "name": "Andreessen Horowitz",
                    "domain": ""
                  }
                ],
                "name": "Series, unspecified"
              },
              {
                "amount": 10000000,
                "date": "2019-02-01",
                "investors": [
                  {
                    "name": "Capital G",
                    "domain": ""
                  },
                  {
                    "name": "sequoia capital",
                    "domain": "sequoiacap.com"
                  },
                  {
                    "name": "kleiner perkins",
                    "domain": "kleinerperkins.com"
                  }
                ],
                "name": "Funding round"
              },
              {
                "amount": 245000000,
                "date": "2018-09-26",
                "investors": [
                  {
                    "name": "tiger global management",
                    "domain": "tigerglobal.com"
                  },
                  {
                    "name": "dst global",
                    "domain": "dst-global.com"
                  },
                  {
                    "name": "sequoia",
                    "domain": "sequoia.com.au"
                  },
                  {
                    "name": "Andreessen Horowitz",
                    "domain": ""
                  },
                  {
                    "name": "kleiner perkins",
                    "domain": "kleinerperkins.com"
                  },
                  {
                    "name": "khosla ventures",
                    "domain": "khoslaventures.com"
                  },
                  {
                    "name": "general catalyst",
                    "domain": "generalcatalyst.com"
                  },
                  {
                    "name": "thrive capital",
                    "domain": "thrivecap.com"
                  }
                ],
                "name": "Funding round"
              },
              {
                "amount": 150000000,
                "date": "2017-07-25",
                "investors": [],
                "name": "Fourth Funding Round"
              },
              {
                "amount": 150000000,
                "date": "2016-11-25",
                "investors": [
                  {
                    "name": "general catalyst",
                    "domain": "generalcatalyst.com"
                  },
                  {
                    "name": "capitalg",
                    "domain": "capitalg.com"
                  },
                  {
                    "name": "sequoia capital",
                    "domain": "sequoiacap.com"
                  },
                  {
                    "name": "Other previous investors",
                    "domain": ""
                  },
                  {
                    "name": "General Catalyst Partners",
                    "domain": ""
                  }
                ],
                "name": "Funding round"
              },
              {
                "amount": 70000000,
                "date": "2014-12-02",
                "investors": [
                  {
                    "name": "thrive capital",
                    "domain": "thrivecap.com"
                  },
                  {
                    "name": "sequoia",
                    "domain": "sequoia.com.au"
                  },
                  {
                    "name": "general catalyst",
                    "domain": "generalcatalyst.com"
                  },
                  {
                    "name": "founders fund",
                    "domain": "foundersfund.com"
                  },
                  {
                    "name": "khosla ventures",
                    "domain": "khoslaventures.com"
                  }
                ],
                "name": "Funding round"
              },
              {
                "amount": 120000000,
                "date": "2014-04-26",
                "investors": [],
                "name": "Funding round"
              },
              {
                "amount": 80000000,
                "date": "2014-03-10",
                "investors": [
                  {
                    "name": "Founder’s Fund",
                    "domain": ""
                  },
                  {
                    "name": "sequoia capital",
                    "domain": "sequoiacap.com"
                  },
                  {
                    "name": "Allen & Co",
                    "domain": "allenandco.us"
                  },
                  {
                    "name": "Khosla",
                    "domain": ""
                  }
                ],
                "name": "Series C"
              },
              {
                "amount": 80000000,
                "date": "2014-01-22",
                "investors": [
                  {
                    "name": "founders fund",
                    "domain": "foundersfund.com"
                  },
                  {
                    "name": "sequoia capital",
                    "domain": "sequoiacap.com"
                  },
                  {
                    "name": "General Catalyst Partners",
                    "domain": ""
                  },
                  {
                    "name": "khosla ventures",
                    "domain": "khoslaventures.com"
                  }
                ],
                "name": "Funding round"
              },
              {
                "amount": 20000000,
                "date": "2012-07-12",
                "investors": [
                  {
                    "name": "sequoia capital",
                    "domain": "sequoiacap.com"
                  }
                ],
                "name": "Funding round"
              },
              {
                "amount": 0,
                "date": "2011-03-29",
                "investors": [
                  {
                    "name": "PayPal founders",
                    "domain": ""
                  }
                ],
                "name": "Funding round"
              }
            ],
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
            }
          },
          "window": {
            "data_through": null
          },
          "meta": {
            "retrieved_at": "2026-09-20T06:35:41.754699+00:00",
            "partial": false,
            "notes": [],
            "provider": "Fliar BI"
          }
        }
      },
      "enrichment": {
        "available": true,
        "result": {
          "ok": true,
          "feature": "get_company_enrichment",
          "data": {
            "activity": [
              {
                "d": "2026-06-22",
                "detail": "Stripe Directory",
                "label": "Product launch",
                "type": "product_launch"
              }
            ],
            "digital": {
              "audience": [
                {
                  "cc": "US",
                  "country": "United States",
                  "share": 0.2792,
                  "visits": 53060565
                },
                {
                  "cc": "GB",
                  "country": "United Kingdom",
                  "share": 0.0679,
                  "visits": 12908445
                },
                {
                  "cc": "DE",
                  "country": "Germany",
                  "share": 0.0483,
                  "visits": 9172588
                },
                {
                  "cc": "IN",
                  "country": "India",
                  "share": 0.0453,
                  "visits": 8602699
                },
                {
                  "cc": "NL",
                  "country": "Netherlands",
                  "share": 0.0359,
                  "visits": 6823857
                }
              ],
              "authority": 79,
              "bounce": 0.6053,
              "country": "United States",
              "country_rank": 165,
              "global_rank": 167,
              "keywords": [
                {
                  "k": "stripe",
                  "pos": 1,
                  "vol": 550000
                },
                {
                  "k": "online payments",
                  "pos": 3,
                  "vol": 1000000
                },
                {
                  "k": "stripe careers",
                  "pos": 1,
                  "vol": 18100
                },
                {
                  "k": "stripe vacancies",
                  "pos": 1,
                  "vol": 14800
                }
              ],
              "ppv": 2.8708,
              "visits": 190046716,
              "visits_date": "2026-05-01"
            },
            "domain": "stripe.com",
            "has_data": true,
            "hiring": {
              "active_12m": 13,
              "avg_12m": 21.9,
              "first_dt": "2024-05-08",
              "freq_detail": "263 roles tracked across 13 of the last 12 months",
              "freq_label": "Hires continuously",
              "last_dt": "2026-09-16",
              "locations": [
                "Toronto",
                "South San Francisco",
                "Chicago",
                "Seattle",
                "San Francisco",
                "Bengaluru / Bangalore, Karnataka, India",
                "New York",
                "Atlanta"
              ],
              "months": [
                {
                  "m": "2024-11",
                  "n": 3
                },
                {
                  "m": "2025-01",
                  "n": 5
                },
                {
                  "m": "2025-03",
                  "n": 6
                },
                {
                  "m": "2025-04",
                  "n": 7
                },
                {
                  "m": "2025-05",
                  "n": 2
                },
                {
                  "m": "2025-06",
                  "n": 16
                },
                {
                  "m": "2025-07",
                  "n": 19
                },
                {
                  "m": "2025-08",
                  "n": 23
                },
                {
                  "m": "2025-09",
                  "n": 30
                },
                {
                  "m": "2025-10",
                  "n": 32
                },
                {
                  "m": "2025-11",
                  "n": 42
                },
                {
                  "m": "2025-12",
                  "n": 18
                },
                {
                  "m": "2026-01",
                  "n": 33
                },
                {
                  "m": "2026-02",
                  "n": 16
                },
                {
                  "m": "2026-03",
                  "n": 6
                },
                {
                  "m": "2026-04",
                  "n": 15
                },
                {
                  "m": "2026-05",
                  "n": 29
                },
                {
                  "m": "2026-06",
                  "n": 20
                },
                {
                  "m": "2026-07",
                  "n": 9
                },
                {
                  "m": "2026-08",
                  "n": 9
                },
                {
                  "m": "2026-09",
                  "n": 4
                }
              ],
              "recent": [
                {
                  "d": "2026-09-16",
                  "location": "Bangalore",
                  "title": "Head of Finance Operations"
                },
                {
                  "d": "2026-09-07",
                  "location": "Bangalore",
                  "title": "Contracting Operations Specialist | Bangalore, IN"
                },
                {
                  "d": "2026-09-07",
                  "location": "Bangalore",
                  "title": "Fraud Operations Manager"
                },
                {
                  "d": "2026-09-05",
                  "location": "Bangalore",
                  "title": "Software Engineer, New Grad"
                },
                {
                  "d": "2026-08-27",
                  "location": "All India",
                  "title": "RN CLIN DOCUMENTATION COORD, FCH - ENTERPRISE QUALITY CDI/UR/DM"
                },
                {
                  "d": "2026-08-27",
                  "location": "Bangalore",
                  "title": "Credit Risk Operations Team Lead"
                },
                {
                  "d": "2026-08-21",
                  "location": "Bangalore",
                  "title": "Operations Associate, GTM Accelerate (Bangalore)"
                },
                {
                  "d": "2026-08-16",
                  "location": "Bangalore",
                  "title": "Data Science Manager, Risk (Bengaluru)"
                },
                {
                  "d": "2026-08-16",
                  "location": "Bangalore",
                  "title": "Marketing Services Program Manager"
                },
                {
                  "d": "2026-08-11",
                  "location": "Bangalore",
                  "title": "Staff Engineer, Revenue (Bengaluru)"
                }
              ],
              "roles": [
                "Technical Account Manager",
                "People Partner",
                "Corporate Strategy",
                "Broadcast Engineer",
                "Staff Security Engineer, Security Partnerships",
                "EMEA Real Estate Transaction Manager",
                "Design Recruiter",
                "Company Strategy & Operations"
              ],
              "total": 368,
              "years": [
                {
                  "n": 31,
                  "y": "2024"
                },
                {
                  "n": 200,
                  "y": "2025"
                },
                {
                  "n": 141,
                  "y": "2026"
                }
              ]
            },
            "innovation": {
              "areas": [
                "Physics & computing",
                "Electricity & electronics"
              ],
              "citations": 10175,
              "families": 276,
              "granted": 188,
              "momentum": "accelerating",
              "notable": [
                {
                  "citations": 390,
                  "title": "Method and apparatus for ordering goods, services and content over an internetwork using a virtual payment account",
                  "y": "2023"
                },
                {
                  "citations": 110,
                  "title": "System and method for indicating entry of personal identification number",
                  "y": "2024"
                },
                {
                  "citations": 92,
                  "title": "Methods and systems for providing payment interface services using a payment platform",
                  "y": "2025"
                }
              ],
              "years": [
                {
                  "n": 1,
                  "y": "2013"
                },
                {
                  "n": 7,
                  "y": "2017"
                },
                {
                  "n": 10,
                  "y": "2018"
                },
                {
                  "n": 12,
                  "y": "2019"
                },
                {
                  "n": 11,
                  "y": "2020"
                },
                {
                  "n": 23,
                  "y": "2021"
                },
                {
                  "n": 51,
                  "y": "2022"
                },
                {
                  "n": 100,
                  "y": "2023"
                },
                {
                  "n": 134,
                  "y": "2024"
                },
                {
                  "n": 143,
                  "y": "2025"
                },
                {
                  "n": 36,
                  "y": "2026"
                }
              ]
            },
            "legal": [
              {
                "country": "United States",
                "id_no": "270465600",
                "legal_name": "Stripe, Inc.",
                "registry": "Others"
              },
              {
                "country": "United Kingdom",
                "id_no": "4675506",
                "legal_name": "SQUARE MILE BUSINESS SERVICES LIMITED",
                "registry": "companieshouse.gov.uk"
              },
              {
                "country": "Czech Republic",
                "id_no": "08667900",
                "legal_name": "STRIPE WOOD s.r.o.",
                "registry": "czso.cz"
              },
              {
                "country": "India",
                "id_no": "U72200KA2016FTC096320",
                "legal_name": "STRIPE INDIA PRIVATE LIMITED",
                "registry": "mca.gov.in"
              },
              {
                "country": "Singapore",
                "id_no": "201524528H",
                "legal_name": "Stripe Payments Singapore Pte. Ltd",
                "registry": "acra.gov.sg"
              }
            ],
            "reputation": {
              "category": "Payment Service",
              "n": 17267,
              "n_12m": 1226,
              "score": 1.7,
              "stars": 1
            },
            "social": {
              "band": "below the industry typical range",
              "cadence_per_month": 0.3,
              "engagement_per_post": 0,
              "followers": 1528731,
              "industry_median_rate": 0.00567,
              "posts_12m": 4,
              "rate": 0.0,
              "ratio_vs_median": 0.0,
              "sector": "Payments"
            },
            "sov": {
              "home_cc": "us",
              "home_country": "United States",
              "peers": [
                {
                  "domain": "stripe.com",
                  "followers": 1528731,
                  "home_visits": 53060565,
                  "name": "Stripe",
                  "reviews": 17267,
                  "world_visits": 190046716
                },
                {
                  "domain": "gocardless.com",
                  "followers": 70647,
                  "home_visits": 301098,
                  "name": "GoCardless",
                  "reviews": 2438,
                  "world_visits": 2688810
                },
                {
                  "domain": "sba.gov",
                  "followers": 277487,
                  "home_visits": 3721219,
                  "name": "u.s. small business administration",
                  "reviews": 15,
                  "world_visits": 3959133
                },
                {
                  "domain": "airwallex.com",
                  "followers": 178694,
                  "home_visits": 3704482,
                  "name": "Airwallex",
                  "reviews": 2493,
                  "world_visits": 9558412
                },
                {
                  "domain": "stripeandstare.com",
                  "followers": 5227,
                  "home_visits": 20833,
                  "name": "Stripe & Stare",
                  "reviews": 1651,
                  "world_visits": 119042
                },
                {
                  "domain": "stripersonline.com",
                  "followers": null,
                  "home_visits": 80103,
                  "name": "stripersonline.com",
                  "reviews": null,
                  "world_visits": 88627
                }
              ],
              "shares": {
                "followers": {
                  "airwallex.com": 0.0867,
                  "gocardless.com": 0.0343,
                  "sba.gov": 0.1347,
                  "stripe.com": 0.7418,
                  "stripeandstare.com": 0.0025
                },
                "home_traffic": {
                  "airwallex.com": 0.0608,
                  "gocardless.com": 0.0049,
                  "sba.gov": 0.0611,
                  "stripe.com": 0.8714,
                  "stripeandstare.com": 0.0003,
                  "stripersonline.com": 0.0013
                },
                "reviews": {
                  "airwallex.com": 0.1045,
                  "gocardless.com": 0.1022,
                  "sba.gov": 0.0006,
                  "stripe.com": 0.7236,
                  "stripeandstare.com": 0.0692
                },
                "world_traffic": {
                  "airwallex.com": 0.0463,
                  "gocardless.com": 0.013,
                  "sba.gov": 0.0192,
                  "stripe.com": 0.9205,
                  "stripeandstare.com": 0.0006,
                  "stripersonline.com": 0.0004
                }
              }
            }
          },
          "window": {
            "data_through": null
          },
          "meta": {
            "retrieved_at": "2026-09-20T06:35:41.772062+00:00",
            "partial": false,
            "notes": [
              "Absent enrichment sections have unknown coverage; the source does not distinguish missing data from a failed section."
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
    "retrieved_at": "2026-09-20T06:35:42.898965+00:00",
    "partial": true,
    "notes": [
      "Each section retains its own date window and access limits. Missing data is not zero."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T06:35:42.899829+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/company_brief.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live Stripe brief returned six available Radar sections and an unavailable News section with service_unavailable. HTTP status was 200 and partial=true. All six successful sections are now included, including the detailed company profile, complete available financials, intelligence, events, funding and enrichment.

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
