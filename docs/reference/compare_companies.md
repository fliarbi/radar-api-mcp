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
                  "name": "Razorpay",
                  "domain": "razorpay.com",
                  "alternate_names": [],
                  "other_domains": [],
                  "description": "Provider of payment and business banking solutions for enterprises",
                  "detailed_description": "Provider of payment and business banking solutions for enterprises. The company offers tools for payment acceptance, automated payroll, and business banking. Solutions include payment gateways, current accounts, and corporate credit cards. It also provides developer resources such as API documentation and integration tools.",
                  "founded": 2014,
                  "logo_url": "https://tracxn-data-image.s3.amazonaws.com/logo/company/razorpay_com_e9750920-57d7-4fee-8850-e1fb86a6c42c",
                  "employee_count": 1952,
                  "company_id": "2gowls1wmc",
                  "classification": {
                    "sectors": [
                      "FinTech",
                      "Enterprise Applications"
                    ],
                    "markets": [
                      "Payments",
                      "Banking Tech",
                      "HRTech"
                    ],
                    "feeds": {
                      "primary": [
                        "Payments",
                        "Banking Tech",
                        "HRTech"
                      ],
                      "other": [
                        "Business Payments Solutions",
                        "Commerce Enablers",
                        "Enterprise Tech - India",
                        "FinTech - India",
                        "Enterprise Tech - Karnataka",
                        "SaaS - India",
                        "SaaS",
                        "Enterprise Software",
                        "FinTech SaaS",
                        "Cloud Banking",
                        "CFO Stack",
                        "Embedded Finance",
                        "Y Combinator Batches",
                        "Banking as a Service",
                        "Open Banking",
                        "Banking Tech - India",
                        "Payroll Management",
                        "HR SaaS"
                      ]
                    },
                    "business_models": [
                      "Business Payments",
                      "Diversified",
                      "Payments",
                      "Gateway",
                      "Accounting Solutions",
                      "Procure to Pay",
                      "Account Payables",
                      "Invoice Processing"
                    ],
                    "revenue_models": [
                      "subscription"
                    ],
                    "industries": [
                      "computer software"
                    ],
                    "company_types": [
                      "Startup"
                    ],
                    "flags": {
                      "Tech": "YES",
                      "Consumer": "NO",
                      "Enterprise": "YES",
                      "Marketplace": "NO",
                      "SaaS": "YES",
                      "Software": "YES",
                      "Social Impact": "NO",
                      "Blockchain": "NO",
                      "Tech Hardware": "NO",
                      "Artificial Intelligence": "Untagged",
                      "Agentic AI": "Untagged"
                    }
                  },
                  "people": {
                    "key_people": [
                      {
                        "name": "Shashank Kumar",
                        "designation": "Co-Founder & Managing Director"
                      },
                      {
                        "name": "Harshil Mathur",
                        "designation": "Co-Founder & CEO"
                      }
                    ],
                    "founders": [
                      {
                        "name": "Shashank Kumar",
                        "designation": "Co-Founder & Managing Director"
                      },
                      {
                        "name": "Harshil Mathur",
                        "designation": "Co-Founder & CEO"
                      }
                    ],
                    "key_people_count": 2,
                    "background_flags": [
                      {
                        "name": "Indian School of Business",
                        "category": "College Wise"
                      },
                      {
                        "name": "Intel",
                        "category": "Company Wise"
                      },
                      {
                        "name": "IIT Roorkee",
                        "category": "College Wise"
                      }
                    ],
                    "founder_selection": "Source designation contains founder; not an independent verification"
                  },
                  "technology": {
                    "website_stack": [
                      "amazon cloudfront",
                      "amazon s3",
                      "amazon web services",
                      "angular",
                      "animate.css",
                      "antv g2",
                      "apple icloud mail",
                      "aws certificate manager",
                      "bootstrap",
                      "cart functionality",
                      "cdnjs",
                      "chakra ui",
                      "chart.js",
                      "cloudflare",
                      "cloudflare bot management",
                      "cloudflare browser insights",
                      "core-js",
                      "datadog",
                      "emotion",
                      "express",
                      "facebook pixel",
                      "font awesome",
                      "framer sites",
                      "google analytics",
                      "google font api",
                      "google sign-in",
                      "google tag manager",
                      "google workspace",
                      "hotjar",
                      "hsts",
                      "http/3",
                      "hubspot",
                      "hubspot analytics",
                      "hubspot chat",
                      "jquery",
                      "jquery cdn",
                      "jsdelivr",
                      "linkedin insight tag",
                      "loadable-components",
                      "lodash",
                      "lottiefiles",
                      "marked",
                      "microsoft clarity",
                      "next.js",
                      "next.js app router",
                      "nginx",
                      "node.js",
                      "open graph",
                      "pdf.js",
                      "preact",
                      "priority hints",
                      "pwa",
                      "radix ui",
                      "razorpay",
                      "react",
                      "react router",
                      "recaptcha",
                      "rss",
                      "salesforce",
                      "segment",
                      "sentry",
                      "shadcn/ui",
                      "styled-components",
                      "substack",
                      "tailwind css",
                      "typescript",
                      "webpack",
                      "yellow.ai",
                      "zoho",
                      "zone.js"
                    ],
                    "technographics": [],
                    "observed_technologies": [
                      "amazon cloudfront",
                      "amazon s3",
                      "amazon web services",
                      "angular",
                      "animate.css",
                      "antv g2",
                      "apple icloud mail",
                      "bootstrap",
                      "cart functionality",
                      "cdnjs",
                      "chakra ui",
                      "chart.js",
                      "cloudflare",
                      "cloudflare bot management",
                      "cloudflare browser insights",
                      "core-js",
                      "datadog",
                      "emotion",
                      "express",
                      "facebook pixel",
                      "font awesome",
                      "framer sites",
                      "google analytics",
                      "google font api",
                      "google sign-in",
                      "google tag manager",
                      "google workspace",
                      "hotjar",
                      "hsts",
                      "http/3",
                      "hubspot",
                      "hubspot analytics",
                      "hubspot chat",
                      "jquery",
                      "jquery cdn",
                      "jsdelivr",
                      "linkedin insight tag",
                      "loadable-components",
                      "lodash",
                      "lottiefiles",
                      "marked",
                      "microsoft clarity",
                      "next.js",
                      "next.js app router",
                      "nginx",
                      "node.js",
                      "open graph",
                      "pdf.js",
                      "preact",
                      "priority hints",
                      "pwa",
                      "radix ui",
                      "razorpay",
                      "react",
                      "react router",
                      "recaptcha",
                      "rss",
                      "salesforce",
                      "segment",
                      "sentry",
                      "shadcn/ui",
                      "styled-components",
                      "substack",
                      "tailwind css",
                      "typescript",
                      "webpack",
                      "yellow.ai",
                      "zoho",
                      "zone.js"
                    ],
                    "observed_at": "2026-05-01"
                  },
                  "web_presence": {
                    "rank": 10000,
                    "rank_bucket": "top_10k",
                    "popularity_label": "high",
                    "tech_count": 69,
                    "technologies": [
                      "amazon cloudfront",
                      "amazon s3",
                      "amazon web services",
                      "angular",
                      "animate.css",
                      "antv g2",
                      "apple icloud mail",
                      "bootstrap",
                      "cart functionality",
                      "cdnjs",
                      "chakra ui",
                      "chart.js",
                      "cloudflare",
                      "cloudflare bot management",
                      "cloudflare browser insights",
                      "core-js",
                      "datadog",
                      "emotion",
                      "express",
                      "facebook pixel",
                      "font awesome",
                      "framer sites",
                      "google analytics",
                      "google font api",
                      "google sign-in",
                      "google tag manager",
                      "google workspace",
                      "hotjar",
                      "hsts",
                      "http/3",
                      "hubspot",
                      "hubspot analytics",
                      "hubspot chat",
                      "jquery",
                      "jquery cdn",
                      "jsdelivr",
                      "linkedin insight tag",
                      "loadable-components",
                      "lodash",
                      "lottiefiles",
                      "marked",
                      "microsoft clarity",
                      "next.js",
                      "next.js app router",
                      "nginx",
                      "node.js",
                      "open graph",
                      "pdf.js",
                      "preact",
                      "priority hints",
                      "pwa",
                      "radix ui",
                      "razorpay",
                      "react",
                      "react router",
                      "recaptcha",
                      "rss",
                      "salesforce",
                      "segment",
                      "sentry",
                      "shadcn/ui",
                      "styled-components",
                      "substack",
                      "tailwind css",
                      "typescript",
                      "webpack",
                      "yellow.ai",
                      "zoho",
                      "zone.js"
                    ],
                    "cdn": "Amazon CloudFront",
                    "has_cdn": true,
                    "perf": {
                      "cwv_label": "needs_improvement",
                      "lcp_label": "good",
                      "cls_label": "good",
                      "inp_label": "needs_improvement",
                      "page_weight_label": "heavy",
                      "dom_label": "complex",
                      "speed_label": "average",
                      "bytes_total": 5038099,
                      "dom_elements": 5015,
                      "req_total": 213,
                      "ttfb_ms": 782,
                      "speed_index": 5271
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
                      "maturity_label": "rich",
                      "has_json_ld": true,
                      "has_microdata": false,
                      "has_rdfa": true,
                      "has_open_graph": true,
                      "has_twitter_card": true,
                      "schema_types": [
                        "Organization",
                        "SoftwareApplication"
                      ],
                      "business_hints": [
                        "saas"
                      ]
                    },
                    "digital_presence_score": 91,
                    "crawl_date": "2026-05-01"
                  },
                  "traffic": {
                    "authority": 70,
                    "global_rank": 2108,
                    "country_rank": 135,
                    "country": "India",
                    "visits": 23096401,
                    "visits_date": "2026-05-01",
                    "bounce": 0.6271,
                    "ppv": 3.3131,
                    "keywords": [
                      {
                        "k": "tripura university question paper 2018 pdf",
                        "pos": 8,
                        "vol": 5000000
                      },
                      {
                        "k": "gst search",
                        "pos": 6,
                        "vol": 823000
                      },
                      {
                        "k": "gst number search",
                        "pos": 6,
                        "vol": 550000
                      }
                    ],
                    "audience": [
                      {
                        "cc": "IN",
                        "country": "India",
                        "share": 0.8925,
                        "visits": 20613671
                      },
                      {
                        "cc": "US",
                        "country": "United States",
                        "share": 0.0294,
                        "visits": 678910
                      },
                      {
                        "cc": "MY",
                        "country": "Malaysia",
                        "share": 0.0184,
                        "visits": 424855
                      },
                      {
                        "cc": "BD",
                        "country": "Bangladesh",
                        "share": 0.0056,
                        "visits": 129752
                      },
                      {
                        "cc": "CA",
                        "country": "Canada",
                        "share": 0.0055,
                        "visits": 127382
                      }
                    ]
                  },
                  "apps": {
                    "count": 5,
                    "downloads": 3780330,
                    "weighted_rating": 3.799999952316284
                  },
                  "products": [],
                  "geography": {
                    "hq_country": "India",
                    "hq_state": "Karnataka",
                    "hq_city": "Bengaluru",
                    "country_code": "IN",
                    "coord": {
                      "type": "Point",
                      "coordinates": [
                        77.59369,
                        12.97194
                      ]
                    },
                    "geo_served": [
                      "India"
                    ],
                    "locations": [
                      {
                        "city": {
                          "name": "Bengaluru"
                        },
                        "cityGroup": [
                          {
                            "name": "Bengaluru Metropolitan Area"
                          },
                          {
                            "name": "India Tier-1 Cities"
                          }
                        ],
                        "state": {
                          "name": "Karnataka"
                        },
                        "country": {
                          "name": "India"
                        },
                        "countryGroup": [
                          {
                            "name": "South Asia"
                          },
                          {
                            "name": "Asia"
                          },
                          {
                            "name": "APAC"
                          }
                        ],
                        "continent": {
                          "name": "Asia"
                        }
                      }
                    ],
                    "addresses": [
                      {
                        "text": "1ST FLOOR ,SJR CYBER, 22 LASKAR HOSUR ROAD   ADUGODI, Bangalore, BANGLORE, Karnataka, India, 560030",
                        "is_hq": false,
                        "pincode": "560030",
                        "country": "India",
                        "country_id": "57ada2abe4b0e0fbead7d6da"
                      },
                      {
                        "text": "GROUND FLOOR,SJR CYBER,22   LASKAR HOSUR ROAD,ADUGODI, Bangalore, BANGALORE, Karnataka, India, 560030",
                        "is_hq": false,
                        "pincode": "560030",
                        "country": "India",
                        "country_id": "57ada2abe4b0e0fbead7d6da"
                      },
                      {
                        "text": "1st Floor, SJR Cyber   22, Laskar Hosur Road, Adugodi, Bangalore, Bangalore, Karnataka, India, 560030",
                        "is_hq": false,
                        "pincode": "560030",
                        "country": "India",
                        "country_id": "57ada2abe4b0e0fbead7d6da"
                      },
                      {
                        "text": "Ground & 1st Floor, SJR Cyber Laskar, Hosur Road",
                        "is_hq": false,
                        "pincode": null,
                        "country": "India",
                        "country_id": "57ada2abe4b0e0fbead7d6da"
                      },
                      {
                        "text": "1st Floor, SJR Cyber, 22   Laskar Hosur Road, Adugodi, Bangalore, Bangalore, Karnataka, India, 560030",
                        "is_hq": false,
                        "pincode": "560030",
                        "country": "India",
                        "country_id": "57ada2abe4b0e0fbead7d6da"
                      },
                      {
                        "text": "1st Floor, SJR Cyber, 22   Laskar Hosur Road, Adugodi, Bangalore, Bangalore, Karnataka, India, 560030",
                        "is_hq": false,
                        "pincode": "560030",
                        "country": "India",
                        "country_id": "57ada2abe4b0e0fbead7d6da"
                      },
                      {
                        "text": "First Floor, SJR Cyber, 22, Laskar Hosur Road, Adugodi, Bangalore, Karnataka, India, 560030, Adugodi, Bangalore, Bangalore South, Karnataka, India, 560030",
                        "is_hq": false,
                        "pincode": "560030",
                        "country": "India",
                        "country_id": "57ada2abe4b0e0fbead7d6da"
                      }
                    ],
                    "coord_precision": "city"
                  },
                  "social": {
                    "links": {
                      "linkedin": "https://linkedin.com/company/razorpay/about",
                      "x": "https://twitter.com/razorpay",
                      "facebook": "https://facebook.com/razorpay",
                      "blog": "https://razorpay.com/blog"
                    }
                  },
                  "lifecycle": {
                    "stage": "Series F",
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
                      "name": "RAZORPAY TECHNOLOGIES PRIVATE LIMITED",
                      "entity_id": "U67100KA2015FTC082538",
                      "registrar": "mca.gov.in",
                      "country": "India"
                    },
                    {
                      "name": "Razorpay Software Limited",
                      "entity_id": "U72200KA2013PLC097389",
                      "registrar": "mca.gov.in",
                      "country": "India"
                    },
                    {
                      "name": "Razorpay Inc",
                      "entity_id": "5648881",
                      "registrar": "Others",
                      "country": "United States"
                    },
                    {
                      "name": "MARSSHOT VENTURES LLP ",
                      "entity_id": "AAU-9729",
                      "registrar": "mca.gov.in",
                      "country": "India"
                    },
                    {
                      "name": "RAZORPAY FINANCIAL AGGREGATOR PRIVATE LIMITED",
                      "entity_id": "U67190KA2020PTC133358",
                      "registrar": "mca.gov.in",
                      "country": "India"
                    },
                    {
                      "name": "RAZORPAY FINANCIAL SERVICES PRIVATE LIMITED",
                      "entity_id": "U65999KA2018PTC114468",
                      "registrar": "mca.gov.in",
                      "country": "India"
                    },
                    {
                      "name": "RZPX PRIVATE LIMITED",
                      "entity_id": "U72900KA2020PTC139072",
                      "registrar": "mca.gov.in",
                      "country": "India"
                    },
                    {
                      "name": "Jhkp Technologies Private Limited",
                      "entity_id": "U74999KA2018PTC192034",
                      "registrar": "mca.gov.in",
                      "country": "India"
                    }
                  ],
                  "assessments": {
                    "completion": 92,
                    "finance": 27,
                    "scalability": 90,
                    "momentum": 57,
                    "data_confidence": 80,
                    "maturity": 70,
                    "innovation": 39,
                    "prominence": 58
                  },
                  "hiring": {
                    "total": 63,
                    "last_dt": "2026-09-16",
                    "first_dt": "2023-01-20",
                    "active_12m": 7,
                    "avg_12m": 4.8,
                    "freq_label": "Hires frequently",
                    "freq_detail": "57 roles tracked across 7 of the last 12 months",
                    "months": [
                      {
                        "m": "2025-05",
                        "n": 1
                      },
                      {
                        "m": "2025-06",
                        "n": 1
                      },
                      {
                        "m": "2026-02",
                        "n": 1
                      },
                      {
                        "m": "2026-04",
                        "n": 1
                      },
                      {
                        "m": "2026-05",
                        "n": 4
                      },
                      {
                        "m": "2026-06",
                        "n": 28
                      },
                      {
                        "m": "2026-07",
                        "n": 11
                      },
                      {
                        "m": "2026-08",
                        "n": 10
                      },
                      {
                        "m": "2026-09",
                        "n": 2
                      }
                    ],
                    "years": [
                      {
                        "y": "2023",
                        "n": 3
                      },
                      {
                        "y": "2024",
                        "n": 1
                      },
                      {
                        "y": "2025",
                        "n": 2
                      },
                      {
                        "y": "2026",
                        "n": 57
                      }
                    ],
                    "recent": [
                      {
                        "d": "2026-09-16",
                        "title": "FinTech Business Analyst Intern",
                        "location": "Delhi"
                      },
                      {
                        "d": "2026-09-05",
                        "title": "Cyber Security Operations Lead",
                        "location": "Bangalore"
                      },
                      {
                        "d": "2026-08-20",
                        "title": "Director of CRM Marketing",
                        "location": "Bangalore"
                      },
                      {
                        "d": "2026-08-20",
                        "title": "Backend Developer Intern",
                        "location": "All India"
                      },
                      {
                        "d": "2026-08-15",
                        "title": "Associate Manager, Key Accounts Management",
                        "location": "Surat"
                      },
                      {
                        "d": "2026-08-11",
                        "title": "Senior Territory Manager, Bank Retail & Direct Enterprise Sales (Nalgonda)",
                        "location": "Hyderabad"
                      },
                      {
                        "d": "2026-08-11",
                        "title": "Senior Territory Manager, Bank Retail & Direct Enterprise Sales (Mahbubnagar)",
                        "location": "Mahbubnagar"
                      },
                      {
                        "d": "2026-08-09",
                        "title": "Territory Manager, Bank Retail & Direct Enterprise Sales",
                        "location": "Jalandhar"
                      },
                      {
                        "d": "2026-08-09",
                        "title": "Senior Territory Manager, Bank Retail & Direct Enterprise Sales (Hyderabad)",
                        "location": "Hyderabad"
                      },
                      {
                        "d": "2026-08-07",
                        "title": "Senior Territory Manager, Bank Retail & Direct Enterprise Sales",
                        "location": "Hyderabad"
                      }
                    ],
                    "roles": [
                      "Senior Software Development Engineer",
                      "Associate Manager, Key Accounts Management",
                      "Associate Director, Finance",
                      "Backend Developer Intern",
                      "Territory Manager, Bank Retail & Direct Enterprise Sales",
                      "Manager, Retention & Growth",
                      "Analyst - Risk Management",
                      "Director of CRM Marketing"
                    ],
                    "locations": [
                      "Bengaluru / Bangalore, Karnataka, India",
                      "Bangalore",
                      "All India",
                      "Hyderabad",
                      "Gurugram",
                      "Bengaluru (Bangalore)",
                      "Surat",
                      "Bengaluru"
                    ]
                  },
                  "innovation": {
                    "families": 2,
                    "granted": 0,
                    "citations": 12,
                    "years": [
                      {
                        "y": "2017",
                        "n": 1
                      },
                      {
                        "y": "2024",
                        "n": 1
                      }
                    ],
                    "areas": [
                      "Physics & computing"
                    ],
                    "momentum": "active",
                    "notable": [
                      {
                        "title": "Simultaneous transactions on shared display devices using scannable codes",
                        "citations": 9,
                        "y": "2024"
                      },
                      {
                        "title": "Facilitating authentication for online payment",
                        "citations": 3,
                        "y": "2017"
                      }
                    ]
                  },
                  "reputation": {
                    "score": 1.3,
                    "stars": 1,
                    "n": 432,
                    "n_12m": 51,
                    "category": "Business Services"
                  },
                  "share_of_voice": {
                    "home_cc": "in",
                    "home_country": "India",
                    "peers": [
                      {
                        "domain": "razorpay.com",
                        "name": "Razorpay",
                        "world_visits": 23096401,
                        "home_visits": 20613671,
                        "followers": null,
                        "reviews": 432
                      },
                      {
                        "domain": "stablemoney.in",
                        "name": "Stable Money",
                        "world_visits": 367837,
                        "home_visits": 354178,
                        "followers": 47263,
                        "reviews": 0
                      },
                      {
                        "domain": "getswipe.in",
                        "name": "Swipe",
                        "world_visits": 449791,
                        "home_visits": 429591,
                        "followers": 20775,
                        "reviews": 0
                      },
                      {
                        "domain": "mastersindia.co",
                        "name": "Masters India",
                        "world_visits": 329864,
                        "home_visits": 319759,
                        "followers": 18324,
                        "reviews": 0
                      },
                      {
                        "domain": "razor.com",
                        "name": "Razor",
                        "world_visits": 254305,
                        "home_visits": null,
                        "followers": null,
                        "reviews": null
                      },
                      {
                        "domain": "razorpayx.com",
                        "name": "razorpayx.com",
                        "world_visits": 237588,
                        "home_visits": 232265,
                        "followers": null,
                        "reviews": 1
                      }
                    ],
                    "shares": {
                      "world_traffic": {
                        "razorpay.com": 0.9337,
                        "stablemoney.in": 0.0149,
                        "getswipe.in": 0.0182,
                        "mastersindia.co": 0.0133,
                        "razor.com": 0.0103,
                        "razorpayx.com": 0.0096
                      },
                      "home_traffic": {
                        "razorpay.com": 0.9391,
                        "stablemoney.in": 0.0161,
                        "getswipe.in": 0.0196,
                        "mastersindia.co": 0.0146,
                        "razorpayx.com": 0.0106
                      },
                      "followers": {
                        "stablemoney.in": 0.5473,
                        "getswipe.in": 0.2406,
                        "mastersindia.co": 0.2122
                      },
                      "reviews": {
                        "razorpay.com": 0.9977,
                        "stablemoney.in": 0.0,
                        "getswipe.in": 0.0,
                        "mastersindia.co": 0.0,
                        "razorpayx.com": 0.0023
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
                      "available": false,
                      "status": "not_observed"
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
                      "available": 2,
                      "returned": 2,
                      "truncated": false
                    },
                    "/company/classification/markets": {
                      "available": 3,
                      "returned": 3,
                      "truncated": false
                    },
                    "/company/classification/feeds/primary": {
                      "available": 3,
                      "returned": 3,
                      "truncated": false
                    },
                    "/company/classification/feeds/other": {
                      "available": 18,
                      "returned": 18,
                      "truncated": false
                    },
                    "/company/classification/business_models": {
                      "available": 8,
                      "returned": 8,
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
                      "available": 2,
                      "returned": 2,
                      "truncated": false
                    },
                    "/company/people/founders": {
                      "available": 2,
                      "returned": 2,
                      "truncated": false
                    },
                    "/company/people/background_flags": {
                      "available": 3,
                      "returned": 3,
                      "truncated": false
                    },
                    "/company/technology/website_stack": {
                      "available": 70,
                      "returned": 70,
                      "truncated": false
                    },
                    "/company/technology/technographics": {
                      "available": 0,
                      "returned": 0,
                      "truncated": false
                    },
                    "/company/technology/observed_technologies": {
                      "available": 69,
                      "returned": 69,
                      "truncated": false
                    },
                    "/company/web_presence/technologies": {
                      "available": 69,
                      "returned": 69,
                      "truncated": false
                    },
                    "/company/web_presence/structured_data/schema_types": {
                      "available": 2,
                      "returned": 2,
                      "truncated": false
                    },
                    "/company/web_presence/structured_data/business_hints": {
                      "available": 1,
                      "returned": 1,
                      "truncated": false
                    },
                    "/company/traffic/keywords": {
                      "available": 3,
                      "returned": 3,
                      "truncated": false
                    },
                    "/company/traffic/audience": {
                      "available": 5,
                      "returned": 5,
                      "truncated": false
                    },
                    "/company/products": {
                      "available": 0,
                      "returned": 0,
                      "truncated": false
                    },
                    "/company/geography/coord/coordinates": {
                      "available": 2,
                      "returned": 2,
                      "truncated": false
                    },
                    "/company/geography/geo_served": {
                      "available": 1,
                      "returned": 1,
                      "truncated": false
                    },
                    "/company/geography/locations": {
                      "available": 1,
                      "returned": 1,
                      "truncated": false
                    },
                    "/company/geography/locations/0/cityGroup": {
                      "available": 2,
                      "returned": 2,
                      "truncated": false
                    },
                    "/company/geography/locations/0/countryGroup": {
                      "available": 3,
                      "returned": 3,
                      "truncated": false
                    },
                    "/company/geography/addresses": {
                      "available": 7,
                      "returned": 7,
                      "truncated": false
                    },
                    "/company/legal": {
                      "available": 8,
                      "returned": 8,
                      "truncated": false
                    },
                    "/company/hiring/months": {
                      "available": 9,
                      "returned": 9,
                      "truncated": false
                    },
                    "/company/hiring/years": {
                      "available": 4,
                      "returned": 4,
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
                      "available": 2,
                      "returned": 2,
                      "truncated": false
                    },
                    "/company/innovation/areas": {
                      "available": 1,
                      "returned": 1,
                      "truncated": false
                    },
                    "/company/innovation/notable": {
                      "available": 2,
                      "returned": 2,
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
                "retrieved_at": "2026-09-20T06:35:42.931026+00:00",
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
                "domain": "razorpay.com",
                "statement": "all",
                "has_data": true,
                "periods": [
                  {
                    "period": "FY2025",
                    "fiscal_year": 2025,
                    "fiscal_period": "FY",
                    "period_end": null,
                    "reported_date": "2025-10-16",
                    "filed_date": "2025-03-31",
                    "form_type": "tracxn_financials",
                    "metrics": {
                      "cash": {
                        "value": 323321563.019583,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": 27740990000.0,
                        "native_currency": "INR"
                      },
                      "net_income": {
                        "value": -140576340.868965,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": -12061450000.0,
                        "native_currency": "INR"
                      },
                      "operating_income": {
                        "value": -38945221.59555,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": -3341500000.0,
                        "native_currency": "INR"
                      },
                      "revenue": {
                        "value": 440889745.291578,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": 37828340000.0,
                        "native_currency": "INR"
                      }
                    },
                    "article_ids": [
                      "68f7191fe97e6da31e2cb7f5",
                      "68f71b6fb5f4abc34a2cf07a",
                      "68f737d9f3ba9a3da52d30db",
                      "6989485b94d3f481f3e2d117"
                    ],
                    "currency_conversion": "fx"
                  },
                  {
                    "period": "FY2024",
                    "fiscal_year": 2024,
                    "fiscal_period": "FY",
                    "period_end": null,
                    "reported_date": "2024-10-29",
                    "filed_date": "2024-03-31",
                    "form_type": "tracxn_financials",
                    "metrics": {
                      "cash": {
                        "value": 207957298.40402,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": 17337400000.0,
                        "native_currency": "INR"
                      },
                      "net_income": {
                        "value": -136856542.867979,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": -11409730000.0,
                        "native_currency": "INR"
                      },
                      "operating_income": {
                        "value": -59648674.472893,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": -4972910000.0,
                        "native_currency": "INR"
                      },
                      "revenue": {
                        "value": 275421374.08592397,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": 22961880000.0,
                        "native_currency": "INR"
                      }
                    },
                    "article_ids": [
                      "6790d74020ebe526db1c7f04",
                      "67911997b9c985b6b17649fc",
                      "67b2f16168916ca487463495",
                      "682e1bbb99cad2df4881bd98",
                      "68485c2eb1d86578b1caadbc",
                      "68640ff48882abb7e3d0ec32",
                      "68b437203ddf2630a8caa0f9",
                      "68fe216641f75f68272857ee",
                      "6989dca594d3f481f3edbd3f",
                      "699737cd219d71cf48d25388",
                      "69c8d52f4ca06a20fbc548cb"
                    ],
                    "currency_conversion": "fx"
                  },
                  {
                    "period": "FY2023",
                    "fiscal_year": 2023,
                    "fiscal_period": "FY",
                    "period_end": null,
                    "reported_date": "2024-02-29",
                    "filed_date": "2023-03-31",
                    "form_type": "tracxn_financials",
                    "metrics": {
                      "cash": {
                        "value": 111267235.39072,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": 9135040000.0,
                        "native_currency": "INR"
                      },
                      "net_income": {
                        "value": 888063.33988,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": 72910000.0,
                        "native_currency": "INR"
                      },
                      "operating_income": {
                        "value": 1243483.56012,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": 102090000.0,
                        "native_currency": "INR"
                      },
                      "revenue": {
                        "value": 277629720.63119996,
                        "currency": "USD",
                        "unit": "absolute",
                        "source_type": "filing",
                        "native_value": 22793400000.0,
                        "native_currency": "INR"
                      }
                    },
                    "article_ids": [
                      "67911997b9c985b6b17649fc",
                      "67911a0ab9c985b6b176da0f",
                      "67b241d968916ca487c5aad4",
                      "67b2f16568916ca487464f2b",
                      "69bb0028c08180591b81af5b"
                    ],
                    "currency_conversion": "fx"
                  }
                ],
                "returned": 3,
                "truncated": false,
                "access_limited": true,
                "available_period_count": 12,
                "computed_at": "2026-09-20T06:35:44.106000Z",
                "summary": {
                  "narrative": "Latest reported FY2025: revenue $440.89M, net income $—. YoY +60.1% (1.6× prior period). Recent signals: Reported a loss, Record revenue, Profitable. Financials sourced from official filings (mca_financials, tracxn_financials) (converted to USD); news/BI estimates fill any gaps."
                }
              },
              "window": {
                "data_through": "2025-10-16"
              },
              "meta": {
                "retrieved_at": "2026-09-20T06:35:44.114690+00:00",
                "partial": false,
                "notes": [
                  "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
                  "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies.",
                  "The linked Radar account exposes only part of the financial archive."
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
                "domain": "razorpay.com",
                "intel": {
                  "company_meta": {
                    "country": "india",
                    "current_stage": "Series F",
                    "estimated_revenue": null,
                    "progress_label": "",
                    "size_label": "very large",
                    "markets": [
                      "payments",
                      "banking tech",
                      "hrtech"
                    ],
                    "total_funding": null,
                    "valuation": 7500000000
                  },
                  "computed_at": "2026-09-20T06:35:44Z",
                  "earnings": {
                    "balance_sheet": null,
                    "estimated_revenue_usd": null,
                    "gated": true,
                    "growth_consistency": 56,
                    "has_data": true,
                    "history": [
                      {
                        "beat_or_miss": null,
                        "cash_usd": 323321563.019583,
                        "coverage_count": 4,
                        "currency_native": "INR",
                        "date": "2025-10-16",
                        "ebitda_usd": null,
                        "employees": null,
                        "eps": null,
                        "article_id": "68f7191fe97e6da31e2cb7f5",
                        "metric_sources": {
                          "cash_usd": "filing",
                          "net_income_usd": "filing",
                          "operating_income_usd": "filing",
                          "revenue_usd": "filing"
                        },
                        "filed_date": "2025-03-31",
                        "form_type": "tracxn_financials",
                        "fx_source": "fx",
                        "gross_profit_usd": null,
                        "guidance_revenue": null,
                        "has_official": true,
                        "long_term_debt_usd": null,
                        "native": {
                          "cash_usd": 27740990000.0,
                          "net_income_usd": -12061450000.0,
                          "operating_income_usd": -3341500000.0,
                          "revenue_usd": 37828340000.0
                        },
                        "net_income_growth_pct": null,
                        "net_income_usd": -140576340.868965,
                        "operating_cash_flow_usd": null,
                        "operating_income_usd": -38945221.59555,
                        "period_has_official": true,
                        "period_label": "FY2025",
                        "period_qtr": "FY",
                        "period_sort": 20255,
                        "period_year": 2025,
                        "source_type": "filing",
                        "quality_signals": [
                          "Reported a loss",
                          "Record revenue"
                        ],
                        "revenue_growth_pct": 65.0,
                        "revenue_usd": 440889745.291578,
                        "article_ids": [
                          "68f7191fe97e6da31e2cb7f5",
                          "68f71b6fb5f4abc34a2cf07a",
                          "68f737d9f3ba9a3da52d30db",
                          "6989485b94d3f481f3e2d117"
                        ],
                        "stockholders_equity_usd": null,
                        "total_assets_usd": null,
                        "total_liabilities_usd": null
                      },
                      {
                        "beat_or_miss": null,
                        "cash_usd": 207957298.40402,
                        "coverage_count": 11,
                        "currency_native": "INR",
                        "date": "2024-10-29",
                        "ebitda_usd": null,
                        "employees": null,
                        "eps": null,
                        "article_id": "6790d74020ebe526db1c7f04",
                        "metric_sources": {
                          "cash_usd": "filing",
                          "net_income_usd": "filing",
                          "operating_income_usd": "filing",
                          "revenue_usd": "filing"
                        },
                        "filed_date": "2024-03-31",
                        "form_type": "tracxn_financials",
                        "fx_source": "fx",
                        "gross_profit_usd": null,
                        "guidance_revenue": null,
                        "has_official": true,
                        "long_term_debt_usd": null,
                        "native": {
                          "cash_usd": 17337400000.0,
                          "net_income_usd": -11409730000.0,
                          "operating_income_usd": -4972910000.0,
                          "revenue_usd": 22961880000.0
                        },
                        "net_income_growth_pct": 370.0,
                        "net_income_usd": -136856542.867979,
                        "operating_cash_flow_usd": null,
                        "operating_income_usd": -59648674.472893,
                        "period_has_official": true,
                        "period_label": "FY2024",
                        "period_qtr": "FY",
                        "period_sort": 20245,
                        "period_year": 2024,
                        "source_type": "filing",
                        "quality_signals": [
                          "Reported a loss"
                        ],
                        "revenue_growth_pct": 24.0,
                        "revenue_usd": 275421374.08592397,
                        "article_ids": [
                          "6790d74020ebe526db1c7f04",
                          "67911997b9c985b6b17649fc",
                          "67b2f16168916ca487463495",
                          "682e1bbb99cad2df4881bd98",
                          "68485c2eb1d86578b1caadbc",
                          "68640ff48882abb7e3d0ec32",
                          "68b437203ddf2630a8caa0f9",
                          "68fe216641f75f68272857ee",
                          "6989dca594d3f481f3edbd3f",
                          "699737cd219d71cf48d25388",
                          "69c8d52f4ca06a20fbc548cb"
                        ],
                        "stockholders_equity_usd": null,
                        "total_assets_usd": null,
                        "total_liabilities_usd": null
                      },
                      {
                        "beat_or_miss": null,
                        "cash_usd": 111267235.39072,
                        "coverage_count": 5,
                        "currency_native": "INR",
                        "date": "2024-02-29",
                        "ebitda_usd": null,
                        "employees": null,
                        "eps": null,
                        "article_id": "67911997b9c985b6b17649fc",
                        "metric_sources": {
                          "cash_usd": "filing",
                          "net_income_usd": "filing",
                          "operating_income_usd": "filing",
                          "revenue_usd": "filing"
                        },
                        "filed_date": "2023-03-31",
                        "form_type": "tracxn_financials",
                        "fx_source": "fx",
                        "gross_profit_usd": null,
                        "guidance_revenue": null,
                        "has_official": true,
                        "long_term_debt_usd": null,
                        "native": {
                          "cash_usd": 9135040000.0,
                          "net_income_usd": 72910000.0,
                          "operating_income_usd": 102090000.0,
                          "revenue_usd": 22793400000.0
                        },
                        "net_income_growth_pct": -1.0,
                        "net_income_usd": 888063.33988,
                        "operating_cash_flow_usd": null,
                        "operating_income_usd": 1243483.56012,
                        "period_has_official": true,
                        "period_label": "FY2023",
                        "period_qtr": "FY",
                        "period_sort": 20235,
                        "period_year": 2023,
                        "source_type": "filing",
                        "quality_signals": [
                          "Profitable",
                          "Record revenue"
                        ],
                        "revenue_growth_pct": 53.88,
                        "revenue_usd": 277629720.63119996,
                        "article_ids": [
                          "67911997b9c985b6b17649fc",
                          "67911a0ab9c985b6b176da0f",
                          "67b241d968916ca487c5aad4",
                          "67b2f16568916ca487464f2b",
                          "69bb0028c08180591b81af5b"
                        ],
                        "stockholders_equity_usd": null,
                        "total_assets_usd": null,
                        "total_liabilities_usd": null
                      }
                    ],
                    "history_public_count": 3,
                    "history_total_count": 12,
                    "latest": {
                      "beat_or_miss": null,
                      "cash_usd": 323321563.019583,
                      "coverage_count": 4,
                      "currency_native": "INR",
                      "date": "2025-10-16",
                      "ebitda_usd": null,
                      "employees": null,
                      "eps": null,
                      "article_id": "68f7191fe97e6da31e2cb7f5",
                      "metric_sources": {
                        "cash_usd": "filing",
                        "net_income_usd": "filing",
                        "operating_income_usd": "filing",
                        "revenue_usd": "filing"
                      },
                      "filed_date": "2025-03-31",
                      "form_type": "tracxn_financials",
                      "fx_source": "fx",
                      "gross_profit_usd": null,
                      "guidance_revenue": null,
                      "has_official": true,
                      "long_term_debt_usd": null,
                      "native": {
                        "cash_usd": 27740990000.0,
                        "net_income_usd": -12061450000.0,
                        "operating_income_usd": -3341500000.0,
                        "revenue_usd": 37828340000.0
                      },
                      "net_income_growth_pct": null,
                      "net_income_usd": -140576340.868965,
                      "operating_cash_flow_usd": null,
                      "operating_income_usd": -38945221.59555,
                      "period_has_official": true,
                      "period_label": "FY2025",
                      "period_qtr": "FY",
                      "period_sort": 20255,
                      "period_year": 2025,
                      "source_type": "filing",
                      "quality_signals": [
                        "Reported a loss",
                        "Record revenue"
                      ],
                      "revenue_growth_pct": 65.0,
                      "revenue_usd": 440889745.291578,
                      "article_ids": [
                        "68f7191fe97e6da31e2cb7f5",
                        "68f71b6fb5f4abc34a2cf07a",
                        "68f737d9f3ba9a3da52d30db",
                        "6989485b94d3f481f3e2d117"
                      ],
                      "stockholders_equity_usd": null,
                      "total_assets_usd": null,
                      "total_liabilities_usd": null
                    },
                    "narrative": "Latest reported FY2025: revenue $440.89M, net income $—. YoY +60.1% (1.6× prior period). Recent signals: Reported a loss, Record revenue, Profitable. Financials sourced from official filings (mca_financials, tracxn_financials) (converted to USD); news/BI estimates fill any gaps.",
                    "official_coverage": {
                      "bi_periods": 0,
                      "currencies": [
                        "INR"
                      ],
                      "form_types": [
                        "mca_financials",
                        "tracxn_financials"
                      ],
                      "fx_converted": true,
                      "official_periods": 12
                    },
                    "prior": {
                      "beat_or_miss": null,
                      "cash_usd": 207957298.40402,
                      "coverage_count": 11,
                      "currency_native": "INR",
                      "date": "2024-10-29",
                      "ebitda_usd": null,
                      "employees": null,
                      "eps": null,
                      "article_id": "6790d74020ebe526db1c7f04",
                      "metric_sources": {
                        "cash_usd": "filing",
                        "net_income_usd": "filing",
                        "operating_income_usd": "filing",
                        "revenue_usd": "filing"
                      },
                      "filed_date": "2024-03-31",
                      "form_type": "tracxn_financials",
                      "fx_source": "fx",
                      "gross_profit_usd": null,
                      "guidance_revenue": null,
                      "has_official": true,
                      "long_term_debt_usd": null,
                      "native": {
                        "cash_usd": 17337400000.0,
                        "net_income_usd": -11409730000.0,
                        "operating_income_usd": -4972910000.0,
                        "revenue_usd": 22961880000.0
                      },
                      "net_income_growth_pct": 370.0,
                      "net_income_usd": -136856542.867979,
                      "operating_cash_flow_usd": null,
                      "operating_income_usd": -59648674.472893,
                      "period_has_official": true,
                      "period_label": "FY2024",
                      "period_qtr": "FY",
                      "period_sort": 20245,
                      "period_year": 2024,
                      "source_type": "filing",
                      "quality_signals": [
                        "Reported a loss"
                      ],
                      "revenue_growth_pct": 24.0,
                      "revenue_usd": 275421374.08592397,
                      "article_ids": [
                        "6790d74020ebe526db1c7f04",
                        "67911997b9c985b6b17649fc",
                        "67b2f16168916ca487463495",
                        "682e1bbb99cad2df4881bd98",
                        "68485c2eb1d86578b1caadbc",
                        "68640ff48882abb7e3d0ec32",
                        "68b437203ddf2630a8caa0f9",
                        "68fe216641f75f68272857ee",
                        "6989dca594d3f481f3edbd3f",
                        "699737cd219d71cf48d25388",
                        "69c8d52f4ca06a20fbc548cb"
                      ],
                      "stockholders_equity_usd": null,
                      "total_assets_usd": null,
                      "total_liabilities_usd": null
                    },
                    "quality_signals_aggregate": [
                      "Reported a loss",
                      "Record revenue",
                      "Profitable"
                    ],
                    "score": 78,
                    "source": "official_filings",
                    "source_count": 10,
                    "yoy_basis": "numeric",
                    "yoy_multiple": 1.6,
                    "yoy_pct": 60.1
                  },
                  "events_by_role": {
                    "acquirer": 28,
                    "client": 4,
                    "contractor": 2,
                    "defendant": 1,
                    "primary": 263,
                    "target": 1
                  },
                  "events_by_type": {
                    "buyback": 7,
                    "capital_infusion": 4,
                    "company_announcement": 27,
                    "contracts": 6,
                    "earnings": 10,
                    "funding_rounds": 46,
                    "incorporation": 2,
                    "ipo": 3,
                    "job_creation": 14,
                    "key_people": 45,
                    "lawsuit": 1,
                    "ma": 29,
                    "new_product": 86,
                    "regulatory": 19
                  },
                  "events_by_year": {
                    "2015": 9,
                    "2016": 6,
                    "2017": 8,
                    "2018": 14,
                    "2019": 21,
                    "2020": 38,
                    "2021": 41,
                    "2022": 48,
                    "2023": 48,
                    "2024": 35,
                    "2025": 22,
                    "2026": 9
                  },
                  "financial_trajectory": {
                    "buyback_events": 7,
                    "funding_events_360d": 0,
                    "funding_events_lifetime": 50,
                    "highest_stage": "Series F",
                    "highest_stage_rank": 7,
                    "ipo_events": 3,
                    "narrative": "Active fundraising history — 50 events, latest stage Series F.",
                    "score": 70,
                    "stage_pace_years": 0.2
                  },
                  "innovation_index": {
                    "announcements_360d": 1,
                    "fda_approvals": 0,
                    "narrative": "Slow product cadence: 86 lifetime launches, 6 in last year.",
                    "new_products_360d": 6,
                    "new_products_lifetime": 86,
                    "score": 23,
                    "velocity_change_pct": -53.8
                  },
                  "investment_readiness": {
                    "breakdown": {
                      "earnings": 78,
                      "financial_trajectory": 70,
                      "innovation": 23,
                      "management": 90,
                      "market_position": 17,
                      "risk": 7
                    },
                    "label": "Moderate",
                    "private_equity_score": 60,
                    "public_shares_score": 53,
                    "recommendation": "Mixed signals; tilt depends on whether the upside or risk drivers matter more for your thesis.",
                    "score": 57
                  },
                  "management_quality": {
                    "board_updates_360d": 0,
                    "ceo_cfo_change_signals_90d": 0,
                    "ceo_transition_window_years": 4,
                    "ceo_transitions": [],
                    "ceo_transitions_count": 0,
                    "churn_penalty": 0,
                    "key_people_events_360d": 2,
                    "key_people_events_all": 45,
                    "leadership_churn": false,
                    "leadership_churn_level": "none",
                    "narrative": "Leadership shows strong stability — modest exec movement and no CEO/CFO change signals in the last 90 days.",
                    "score": 90,
                    "warning_flags": []
                  },
                  "market_position": {
                    "asset_acquisitions": 0,
                    "asset_roles": {},
                    "contracts_360d": 0,
                    "contracts_all": 6,
                    "ma_involvement": {
                      "acquirer": 28,
                      "target": 1
                    },
                    "ma_total": 29,
                    "narrative": "Limited market signal: 6 contracts and 29 M&A events lifetime.",
                    "partnerships_all": 0,
                    "score": 17
                  },
                  "peer_comparison": {
                    "cohort_size": 61,
                    "country": "india",
                    "event_count_percentile": 75,
                    "event_count_quantiles": {
                      "p25": 1,
                      "p50": 3,
                      "p75": 8,
                      "p90": 24,
                      "p95": 32
                    },
                    "market": "payments",
                    "innovation_percentile": 95,
                    "innovation_quantiles": {
                      "p50": 0,
                      "p90": 2,
                      "p95": 3
                    },
                    "risk_percentile": 25,
                    "risk_quantiles": {
                      "p50": 0,
                      "p90": 3,
                      "p95": 4
                    },
                    "this_company": {
                      "event_count": 14,
                      "innovation": 7,
                      "risk": 2
                    }
                  },
                  "raw_event_count": 299,
                  "risk_profile": {
                    "bankruptcy_events": 0,
                    "lawsuits_360d": 0,
                    "lawsuits_all": 1,
                    "lawsuits_as_defendant": 1,
                    "layoffs_180d": 0,
                    "narrative": "Low risk profile. A handful of legal/regulatory mentions but nothing systemic.",
                    "regulatory_360d": 2,
                    "score": 7,
                    "warning_flags": []
                  }
                },
                "computed_at": "2026-09-20T06:35:44.106000Z"
              },
              "window": {
                "data_through": null
              },
              "meta": {
                "retrieved_at": "2026-09-20T06:35:44.113797+00:00",
                "partial": false,
                "notes": [
                  "Scores and narratives are derived assessments. Financial metrics are retrieved evidence."
                ],
                "provider": "Fliar BI"
              }
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
                "retrieved_at": "2026-09-20T06:35:44.140781+00:00",
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
                "computed_at": "2026-09-20T06:35:42.892000Z",
                "summary": {
                  "narrative": "Latest reported FY2024: revenue $500M. Growth has been erratic across reported periods. Recent signals: Reported a loss, Record revenue, Profitable."
                }
              },
              "window": {
                "data_through": "2025-02-28"
              },
              "meta": {
                "retrieved_at": "2026-09-20T06:35:44.146414+00:00",
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
                "retrieved_at": "2026-09-20T06:35:44.146686+00:00",
                "partial": false,
                "notes": [
                  "Scores and narratives are derived assessments. Financial metrics are retrieved evidence."
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
    "retrieved_at": "2026-09-20T06:35:44.146715+00:00",
    "partial": false,
    "notes": [
      "Each section retains its own date window and access limits. Missing data is not zero."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T06:35:44.147757+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/compare_companies.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live Razorpay/Stripe comparison returned both companies with their three research sections. The example keeps the detailed profiles, all available financial evidence and full intelligence sections. It is not evidence that their fiscal periods cover identical dates.

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
