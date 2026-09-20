# Company profile API: sectors, feeds, founders, technology, traffic and apps

[All endpoints](README.md) · [Workflow guide](../guides/company-data-api.md)

Retrieve a detailed company record by domain, including seventeen selectable sections: classification, people, technology, web presence, traffic, apps, products, geography, social, lifecycle, legal, assessments, hiring, innovation, activity, reputation and share of voice. The operator must connect the detailed profile store. A card-only deployment reports profile_depth=card explicitly.

## Route, authentication and credits

**`POST /v1/companies/profile`** · MCP tool **`get_company`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |
| `company_id` | default `null` | string or null; min characters: `1`; max characters: `100`; pattern: `^[A-Za-z0-9_-]+$` |
| `sections` | default `["classification", "people", "technology", "web_presence", "traffic", "apps", "products", "geography", "social", "lifecycle", "legal", "assessments", "hiring", "innovation", "activity", "reputation", "share_of_voice"]` | array of string; max items: `17`; one of `classification`, `people`, `technology`, `web_presence`, `traffic`, `apps`, `products`, `geography`, `social`, `lifecycle`, `legal`, `assessments`, `hiring`, `innovation`, `activity`, `reputation`, `share_of_voice` |
| `item_limit` | default `100` | integer; minimum: `1`; maximum: `250` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/profile" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"razorpay.com"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company -->
```json
{
  "name": "get_company",
  "arguments": {
    "request": {
      "domain": "razorpay.com"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_company -->
```json
{
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
    "retrieved_at": "2026-09-20T06:35:41.268173+00:00",
    "partial": false,
    "notes": [
      "Profile scores and founder categories are source assessments; app totals do not include an app-by-app roster."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T06:35:41.268563+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Razorpay capture returned FinTech and Enterprise Applications sectors; Payments, Banking Tech and HRTech primary feeds; eighteen other feeds; two founders; seventy website-stack entries; traffic by geography; five apps with download and rating totals; hiring and patent observations. The documentation preserves all captured array rows. Multiple records share microsoft.com, so the detailed reader returns 409 ambiguous_company unless a public company_id disambiguates the domain.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.company.classification` | Sectors, markets, primary and other feeds, business/revenue models, industries and classification flags. |
| `data.company.people` | Named key people and designations, derived founder selection and background categories; no contact reveal. |
| `data.company.technology / web_presence` | Complete returned technology lists, technographics, crawl date, CDN, performance, SEO and structured-data observations. |
| `data.company.traffic` | Visits with measurement date, country audience shares, keywords, bounce rate and pages per visit. |
| `data.company.apps` | Aggregate count, downloads and weighted rating; source does not supply an app-by-app roster here. |
| `data.company.products / hiring / innovation / social` | Products, job history/roles/locations, patent observations and social links/engagement when present. |
| `data.coverage.sections` | Available, not_observed, unavailable or partial state for every requested section. |
| `data.coverage.arrays` | Exact available/returned/truncated counts for every array. item_limit is per array, not a global row limit. |
| `data.profile_depth` | detailed when the company record reader is connected; card explicitly identifies the fallback mode. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Search for candidates first if you only know a name. Retrieve the profile, compare its returned name and description with the business you intend, and consult enrichment for available legal identity. Only then join financial and news records into a named company brief.

A domain may be shared by a corporate parent, product or division. Do not overwrite an independently verified legal name solely because a domain lookup returned another label.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
