# Find companies with both subscription and transaction-commission models

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** Build a candidate set for businesses combining recurring subscriptions and transaction commissions, then require both recorded tags.

**Validation status:** request schemas and known catalogue values checked locally.
The exact main-search response is captured below, including any empty result or denial.
Additional variants are request recipes unless their captured output is shown.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

**POST `/v1/companies/filter-options`** · MCP `company_filter_options`

<!-- business-request: 57-hybrid-subscription-and-commission-lookup -->
```json
{
  "field": "revenue_models",
  "q": "subscription",
  "limit": 10
}
```

The following is the actual local output of the catalogue handler. This lookup
used no company-store connection and was not an HTTP/live-company search.

<!-- business-local-output: 57-hybrid-subscription-and-commission-lookup -->
```json
{
  "field": "revenue_models",
  "query": "subscription",
  "options": [
    "subscription"
  ],
  "returned": 1,
  "complete": false,
  "note": "Suggestions are bounded matches, not the complete company universe."
}
```

## Main request

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 57-hybrid-subscription-and-commission-search -->
```json
{
  "filters": {
    "revenue_models": [
      "subscription",
      "commission on transaction"
    ]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

Two values in revenue_models generally mean OR, not AND. The request finds candidates with either label. Read each candidate’s classification and perform a client-side all-of check before labeling a row as a recorded hybrid model.

Set `RADAR_BASE_URL=https://radar-api.fliarbi.com` and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL/v1/companies/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"revenue_models":["subscription","commission on transaction"]},"match_mode":"strict","page":0,"limit":20}'
```

Equivalent MCP tool call:

<!-- business-mcp: 57-hybrid-subscription-and-commission-search -->
```json
{
  "name": "search_companies",
  "arguments": {
    "request": {
      "filters": {
        "revenue_models": [
          "subscription",
          "commission on transaction"
        ]
      },
      "match_mode": "strict",
      "page": 0,
      "limit": 20
    }
  }
}
```

## Captured output for this exact request

**HTTP 200: 20 returned companies**, captured **2026-09-25T16:17:58.533347+00:00** through the authenticated
local gateway calling its configured Radar source. This is an actual response,
including empty results and denials. Retrieval time does not certify the age of
the underlying source or independently verify a company's fee contract.

| Returned company | Domain | Source matching tier |
|---|---|---|
| EMudhra | emudhra.com | strict |
| Altair | altair.com | strict |
| Aptus Value Housing Finance India | aptusindia.com | strict |
| Crowd4Test | crowd4test.com | strict |
| Cvent | cvent.com | strict |
| ESDS | esds.co.in | strict |
| Groww | groww.in | strict |
| HappyLocate | happylocate.com | strict |
| IndiaMART | indiamart.com | strict |
| Infinera | infinera.com | strict |
| Newgen | newgensoft.com | strict |
| Palo Alto Networks | paloaltonetworks.com | strict |
| People10 | people10.com | strict |
| RateGain | rategain.com | strict |
| Reverie Language Technologies | reverieinc.com | strict |
| Spyne.ai | spyne.ai | strict |
| Star Health and Allied Insurance | starhealth.in | strict |
| Suryoday | suryodaybank.com | strict |
| TruckSuvidha | trucksuvidha.com | strict |
| 361 Degree Minds | 361dm.com | strict |

These are source-matched candidates. The classification read below inspects one
returned domain; it does not verify all companies or their pricing terms.

<details open>
<summary>Complete captured search_companies response</summary>

<!-- business-live-response: 57-hybrid-subscription-and-commission-search -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
    "companies": [
      {
        "linkedin_slug": "emudhra",
        "location": {
          "c": "india",
          "rg": "karnataka",
          "l": "bengaluru",
          "lc": "bengaluru, karnataka, india",
          "hq": "bengaluru",
          "cc": "in",
          "coord": [
            77.59369,
            12.97194
          ],
          "g": "12.97194,77.59369"
        },
        "has_email": false,
        "hq": "bengaluru",
        "domain": "emudhra.com",
        "founded": "2008",
        "company_id": "iw8dvjkisr",
        "tagline": "Provider of digital signature certificates, PKI, and e-signature solutions",
        "size": "11-50",
        "description": "Provider of digital signature certificates, PKI, and e-signature solutions",
        "slug": "emudhra",
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "name": "EMudhra",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=emudhra.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "altair-engineering",
        "location": {
          "c": "united states",
          "rg": "michigan",
          "l": "troy",
          "lc": "troy, michigan, united states",
          "hq": "troy",
          "cc": "us",
          "coord": [
            -83.14993,
            42.60559
          ],
          "g": "42.60559,-83.14993"
        },
        "has_email": false,
        "hq": "troy",
        "domain": "altair.com",
        "founded": "1985",
        "company_id": "2ao4xkycgv",
        "tagline": "Provider of enterprise software for simulation, data analytics, AI, and HPC",
        "size": "1001-5000",
        "description": "Provider of enterprise software for simulation, data analytics, AI, and HPC",
        "slug": "altair",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "Altair",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=altair.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "aptus-value-housing-finance-india-limited",
        "location": {
          "c": "india",
          "rg": "tamil nadu",
          "l": "chennai",
          "lc": "chennai, tamil nadu, india",
          "hq": "chennai",
          "cc": "in",
          "coord": [
            80.27847,
            13.08784
          ],
          "g": "13.08784,80.27847"
        },
        "has_email": false,
        "hq": "chennai",
        "domain": "aptusindia.com",
        "founded": "2009",
        "company_id": "3kc1czuq33",
        "tagline": "Provider of loans for affordable housing",
        "size": "1001-5000",
        "description": "Provider of loans for affordable housing",
        "slug": "aptus-value-housing-finance-india",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "Aptus Value Housing Finance India",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=aptusindia.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "crowd4test",
        "location": {
          "c": "india",
          "rg": "karnataka",
          "l": "bengaluru",
          "lc": "bengaluru, karnataka, india",
          "hq": "bengaluru",
          "cc": "in",
          "coord": [
            77.59369,
            12.97194
          ],
          "g": "12.97194,77.59369"
        },
        "has_email": false,
        "hq": "bengaluru",
        "domain": "crowd4test.com",
        "founded": "2015",
        "company_id": "1bzfzdmp85",
        "tagline": "Online based crowd sourced  testing platform and device lab",
        "size": "11-50",
        "description": "Online based crowd sourced  testing platform and device lab",
        "slug": "crowd4test",
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "name": "Crowd4Test",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=crowd4test.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "cvent",
        "location": {
          "c": "united states",
          "rg": "virginia",
          "l": "fairfax",
          "lc": "fairfax, virginia, united states",
          "hq": "fairfax",
          "cc": "us",
          "coord": [
            -77.30637,
            38.84622
          ],
          "g": "38.84622,-77.30637"
        },
        "has_email": false,
        "hq": "fairfax",
        "domain": "cvent.com",
        "founded": "1999",
        "company_id": "16vvtt1go8",
        "tagline": "Provider of software for event management, marketing, and attendee engagement",
        "size": "1001-5000",
        "description": "Provider of software for event management, marketing, and attendee engagement",
        "slug": "cvent",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "Cvent",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=cvent.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "esdsdc",
        "location": {
          "c": "india",
          "rg": "maharashtra",
          "l": "nashik",
          "lc": "nashik, maharashtra, india",
          "hq": "nashik",
          "cc": "in",
          "coord": [
            73.79096,
            19.99727
          ],
          "g": "19.99727,73.79096"
        },
        "has_email": false,
        "hq": "nashik",
        "domain": "esds.co.in",
        "founded": "2005",
        "company_id": "1yl5ll6jfj",
        "tagline": "Provider of cloud and data centre infrastructure solutions",
        "size": "1001-5000",
        "description": "Provider of cloud and data centre infrastructure solutions",
        "slug": "esds",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "ESDS",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=esds.co.in",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "groww.in",
        "location": {
          "c": "india",
          "rg": "karnataka",
          "l": "bengaluru",
          "lc": "bengaluru, karnataka, india",
          "hq": "bengaluru",
          "cc": "in",
          "coord": [
            77.59369,
            12.97194
          ],
          "g": "12.97194,77.59369"
        },
        "has_email": false,
        "hq": "bengaluru",
        "domain": "groww.in",
        "founded": "2016",
        "company_id": "1km286cjpd",
        "tagline": "Provider of an online platform for investments and trading services",
        "size": "201-500",
        "description": "Provider of an online platform for investments and trading services",
        "slug": "groww",
        "flags": [
          [
            "Medium Enterprise",
            "size"
          ]
        ],
        "name": "Groww",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=groww.in",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "13228161",
        "location": {
          "c": "india",
          "rg": "karnataka",
          "l": "bengaluru",
          "lc": "bengaluru, karnataka, india",
          "hq": "bengaluru",
          "cc": "in",
          "coord": [
            77.59369,
            12.97194
          ],
          "g": "12.97194,77.59369"
        },
        "has_email": false,
        "hq": "bengaluru",
        "domain": "happylocate.com",
        "founded": "2016",
        "company_id": "2d510vqpqi",
        "tagline": "Provider of relocation services for households, pets, and corporations",
        "size": "11-50",
        "description": "Provider of relocation services for households, pets, and corporations",
        "slug": "happylocate",
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "name": "HappyLocate",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=happylocate.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "indiamart-intermesh-limited",
        "location": {
          "c": "india",
          "rg": "uttar pradesh",
          "l": "noida",
          "lc": "noida, uttar pradesh, india",
          "hq": "noida",
          "cc": "in",
          "coord": [
            77.33,
            28.58
          ],
          "g": "28.58,77.33"
        },
        "has_email": false,
        "hq": "noida",
        "domain": "indiamart.com",
        "founded": "1999",
        "company_id": "1w493kwbtd",
        "tagline": "B2B marketplace platform connecting buyers and suppliers offering diverse industrial products",
        "size": "1001-5000",
        "description": "B2B marketplace platform connecting buyers and suppliers offering diverse industrial products",
        "slug": "indiamart",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "IndiaMART",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=indiamart.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "infinera",
        "location": {
          "c": "united states",
          "rg": "california",
          "l": "sunnyvale",
          "lc": "sunnyvale, california, united states",
          "hq": "sunnyvale",
          "cc": "us",
          "coord": [
            -122.03635,
            37.36883
          ],
          "g": "37.36883,-122.03635"
        },
        "has_email": false,
        "hq": "sunnyvale",
        "domain": "infinera.com",
        "founded": "2000",
        "company_id": "19locfccm5",
        "tagline": "Provider of networking, infrastructure, and communications solutions across various industries",
        "size": "1001-5000",
        "description": "Provider of networking, infrastructure, and communications solutions across various industries",
        "slug": "infinera",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "Infinera",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=infinera.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "newgen",
        "location": {
          "c": "india",
          "rg": "delhi",
          "l": "delhi",
          "lc": "delhi, delhi, india",
          "hq": "delhi",
          "cc": "in",
          "coord": [
            77.23149,
            28.65195
          ],
          "g": "28.65195,77.23149"
        },
        "has_email": false,
        "hq": "delhi",
        "domain": "newgensoft.com",
        "founded": "1992",
        "company_id": "1k8411eh9f",
        "tagline": "Provider of a unified platform for digital transformation and automation",
        "size": "1001-5000",
        "description": "Provider of a unified platform for digital transformation and automation",
        "slug": "newgen",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "Newgen",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=newgensoft.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "palo-alto-networks",
        "location": {
          "c": "united states",
          "rg": "california",
          "l": "santa clara",
          "lc": "santa clara, california, united states",
          "hq": "santa clara",
          "cc": "us",
          "coord": [
            -121.95524,
            37.35411
          ],
          "g": "37.35411,-121.95524"
        },
        "has_email": false,
        "hq": "santa clara",
        "domain": "paloaltonetworks.com",
        "founded": "2005",
        "company_id": "2t3ufhy6j5",
        "tagline": "Provider of cybersecurity platforms, threat intelligence, and incident response services",
        "size": "51-200",
        "description": "Provider of cybersecurity platforms, threat intelligence, and incident response services",
        "slug": "palo-alto-networks",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "name": "Palo Alto Networks",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=paloaltonetworks.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "people10",
        "location": {
          "c": "india",
          "rg": "karnataka",
          "l": "bengaluru",
          "lc": "bengaluru, karnataka, india",
          "hq": "bengaluru",
          "cc": "us",
          "coord": [
            -77.03637,
            38.89511
          ],
          "g": "38.89511,-77.03637"
        },
        "has_email": false,
        "hq": "bengaluru",
        "domain": "people10.com",
        "founded": "2011",
        "company_id": "2tvh1sdsbl",
        "tagline": "Provides horizontal application development services",
        "size": "201-500",
        "description": "Provides horizontal application development services",
        "slug": "people10",
        "flags": [
          [
            "Medium Enterprise",
            "size"
          ]
        ],
        "name": "People10",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=people10.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "rategain",
        "location": {
          "c": "united kingdom",
          "rg": "england",
          "l": "london",
          "lc": "london, england, united kingdom",
          "hq": "london",
          "cc": "in",
          "coord": [
            77.2148,
            28.62137
          ],
          "g": "28.62137,77.2148"
        },
        "has_email": false,
        "hq": "london",
        "domain": "rategain.com",
        "founded": "2004",
        "company_id": "2eon8s19dn",
        "tagline": "AI-powered solutions for the travel and hospitality industry",
        "size": "501-1000",
        "description": "AI-powered solutions for the travel and hospitality industry",
        "slug": "rategain",
        "flags": [
          [
            "Medium Enterprise",
            "size"
          ]
        ],
        "name": "RateGain",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=rategain.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "reverie-language-technologies-pvt--ltd",
        "location": {
          "c": "india",
          "rg": "karnataka",
          "l": "bengaluru",
          "lc": "bengaluru, karnataka, india",
          "hq": "bengaluru",
          "cc": "in",
          "coord": [
            77.59369,
            12.97194
          ],
          "g": "12.97194,77.59369"
        },
        "has_email": false,
        "hq": "bengaluru",
        "domain": "reverieinc.com",
        "founded": "2009",
        "company_id": "y3bm3f40ew",
        "tagline": "Provider of AI-powered language translation, localization, and voice technology solutions",
        "size": "501-1000",
        "description": "Provider of AI-powered language translation, localization, and voice technology solutions",
        "slug": "reverie-language-technologies",
        "flags": [
          [
            "Medium Enterprise",
            "size"
          ]
        ],
        "name": "Reverie Language Technologies",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=reverieinc.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "spyne-ai",
        "location": {
          "c": "india",
          "rg": "haryana",
          "l": "gurugram",
          "lc": "gurugram, haryana, india",
          "hq": "gurugram",
          "cc": "in",
          "coord": [
            77.02635,
            28.4601
          ],
          "g": "28.4601,77.02635"
        },
        "has_email": false,
        "hq": "gurugram",
        "domain": "spyne.ai",
        "founded": "2018",
        "company_id": "1yrw10h64d",
        "tagline": "Platform offering AI-powered imaging for vehicle photography",
        "size": "51-200",
        "description": "Platform offering AI-powered imaging for vehicle photography",
        "slug": "spyne-ai",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "name": "Spyne.ai",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=spyne.ai",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "star-health-and-allied-insurance-co--ltd",
        "location": {
          "c": "india",
          "rg": "tamil nadu",
          "l": "chennai",
          "lc": "chennai, tamil nadu, india",
          "hq": "chennai",
          "cc": "in",
          "coord": [
            80.27847,
            13.08784
          ],
          "g": "13.08784,80.27847"
        },
        "has_email": false,
        "hq": "chennai",
        "domain": "starhealth.in",
        "founded": "2006",
        "company_id": "21tsejrkxw",
        "tagline": "Provider of health insurance services",
        "size": "10000+",
        "description": "Provider of health insurance services",
        "slug": "star-health-and-allied-insurance",
        "flags": [],
        "name": "Star Health and Allied Insurance",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=starhealth.in",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "suryodaysmallfinancebankltd",
        "location": {
          "c": "india",
          "rg": "maharashtra",
          "l": "mumbai",
          "lc": "mumbai, maharashtra, india",
          "hq": "mumbai",
          "cc": "in",
          "coord": [
            72.88261,
            19.07283
          ],
          "g": "19.07283,72.88261"
        },
        "has_email": false,
        "hq": "mumbai",
        "domain": "suryodaybank.com",
        "founded": "2008",
        "company_id": "1p3aa3yqdm",
        "tagline": "Small finance bank offering savings accounts, deposits, and loan products",
        "size": "5001-10000",
        "description": "Small finance bank offering savings accounts, deposits, and loan products",
        "slug": "suryoday",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "Suryoday",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=suryodaybank.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "trucksuvidha",
        "location": {
          "c": "india",
          "rg": "haryana",
          "l": "yamuna nagar",
          "lc": "yamuna nagar, haryana, india",
          "hq": "yamuna nagar",
          "cc": "in",
          "coord": [
            77.28371,
            30.12796
          ],
          "g": "30.12796,77.28371"
        },
        "has_email": false,
        "hq": "yamuna nagar",
        "domain": "trucksuvidha.com",
        "founded": "2014",
        "company_id": "399lumdu6p",
        "tagline": "Provider of an online platform connecting transporters, brokers, and logistics entities",
        "size": "1-10",
        "description": "Provider of an online platform connecting transporters, brokers, and logistics entities",
        "slug": "trucksuvidha",
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "name": "TruckSuvidha",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=trucksuvidha.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "361-degree-minds",
        "location": {
          "c": "india",
          "rg": "tamil nadu",
          "l": "chennai",
          "lc": "chennai, tamil nadu, india",
          "hq": "chennai",
          "cc": "",
          "coord": [
            80.27847,
            13.08784
          ],
          "g": "13.08784,80.27847"
        },
        "has_email": false,
        "hq": "chennai",
        "domain": "361dm.com",
        "founded": "2006",
        "company_id": "1qibrj4pza",
        "tagline": "Cloud-based LMS platform for the multi industry",
        "size": "11-50",
        "description": "Cloud-based LMS platform for the multi industry",
        "slug": "361-degree-minds",
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "name": "361 Degree Minds",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=361dm.com",
        "match_tier": "strict"
      }
    ],
    "page": 0,
    "requested_limit": 20,
    "returned": 20,
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
          "count": 200000,
          "added": 20
        }
      ],
      "source_rows": 20,
      "excluded_candidates": 0,
      "strict_count_reported": 200000,
      "candidate_pool_count_reported": 200000,
      "count_capped": true,
      "filters_restricted": false,
      "note": "Strict means the source labelled the row strict and did not strip filters. Counts may describe an expanded candidate pool, not all matching companies. Missing tier metadata is unverified."
    },
    "next_page": 1,
    "pagination": "Increment source page even when strict filtering returns no rows; next_page is a continuation hint, not a guarantee of more matches. Account caps apply."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-25T16:17:58.533056+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

</details>

[Download this request and full response](../examples/business-models/57-hybrid-subscription-and-commission-search.json). All returned fields and rows are preserved; SHA-256 fingerprints are included.

### Captured `get_company` for a returned company

POST `/v1/companies/profile`, HTTP **200**, captured **2026-09-25T16:17:58.540751+00:00**.

<!-- business-live-request: 57-hybrid-subscription-and-commission-profile -->
```json
{
  "domain": "emudhra.com"
}
```

<details open>
<summary>Complete captured get_company response</summary>

<!-- business-live-response: 57-hybrid-subscription-and-commission-profile -->
```json
{
  "ok": true,
  "feature": "get_company",
  "data": {
    "company": {
      "company_id": "iw8dvjkisr",
      "domain": "emudhra.com",
      "name": "EMudhra",
      "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=emudhra.com",
      "description": "Provider of digital signature certificates, PKI, and e-signature solutions",
      "founded": 2008,
      "employee_count": 28
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
      "hiring": "not_observed",
      "innovation": "not_observed",
      "activity": "not_observed",
      "reputation": "not_observed",
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
    "retrieved_at": "2026-09-25T16:17:58.540597+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

</details>

[Download this request and full response](../examples/business-models/57-hybrid-subscription-and-commission-profile.json). All returned fields and rows are preserved; SHA-256 fingerprints are included.

### Captured `get_company_field` for a returned company

POST `/v1/companies/field`, HTTP **200**, captured **2026-09-25T16:17:58.543547+00:00**.

<!-- business-live-request: 57-hybrid-subscription-and-commission-classification -->
```json
{
  "domain": "emudhra.com",
  "field": "classification",
  "item_limit": 100
}
```

<details open>
<summary>Complete captured get_company_field response</summary>

<!-- business-live-response: 57-hybrid-subscription-and-commission-classification -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "emudhra.com",
    "company_id": "iw8dvjkisr",
    "field": "classification",
    "value": {
      "sectors": [
        "Enterprise Infrastructure",
        "Business Services",
        "Enterprise Applications"
      ],
      "sector_details": [
        {
          "name": "Enterprise Infrastructure",
          "classification": "Other Markets"
        },
        {
          "name": "Business Services",
          "classification": "Other Markets"
        },
        {
          "name": "Enterprise Applications",
          "classification": "Other Markets"
        }
      ],
      "markets": [
        "Cybersecurity",
        "Digital Transformation Services",
        "Digital Transaction Management",
        "GovTech"
      ],
      "feeds": {
        "primary": [
          "Cybersecurity",
          "Digital Transformation Services",
          "Digital Transaction Management",
          "GovTech"
        ],
        "other": [
          "Website Security",
          "Enterprise Tech - India",
          "Cybersecurity - India",
          "Enterprise Software",
          "E-Governance",
          "Enterprise Tech - Karnataka",
          "SaaS - India",
          "SaaS",
          "Electronic Signature",
          "Government SaaS"
        ]
      },
      "business_models": [
        "Website Security",
        "Digital Certificate",
        "Electronic Signature",
        "Government Operations and Administrative Tools",
        "Analytics",
        "Fraud Detection",
        "Data Management",
        "Digitization"
      ],
      "revenue_models": [
        "advertising",
        "commission on transaction",
        "e-commerce - service",
        "subscription"
      ],
      "industries": [
        "information technology and services"
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
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "classification": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/sectors": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/sector_details": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/markets": {
          "available": 4,
          "returned": 4,
          "truncated": false
        },
        "/value/feeds/primary": {
          "available": 4,
          "returned": 4,
          "truncated": false
        },
        "/value/feeds/other": {
          "available": 10,
          "returned": 10,
          "truncated": false
        },
        "/value/business_models": {
          "available": 8,
          "returned": 8,
          "truncated": false
        },
        "/value/revenue_models": {
          "available": 4,
          "returned": 4,
          "truncated": false
        },
        "/value/industries": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/company_types": {
          "available": 1,
          "returned": 1,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-25T16:17:58.543426+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

</details>

[Download this request and full response](../examples/business-models/57-hybrid-subscription-and-commission-classification.json). All returned fields and rows are preserved; SHA-256 fingerprints are included.

The returned EMudhra classification contains both `subscription` and
`commission on transaction`. This establishes both tags in that snapshot;
it does not establish their revenue shares or the current fee schedule.

## Related request variants

### Narrow the OR candidate pool to online marketplaces

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 57-hybrid-subscription-and-commission-variant-1 -->
```json
{
  "filters": {
    "industries": [
      "Online Marketplaces"
    ],
    "revenue_models": [
      "subscription",
      "commission on transaction"
    ]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

## Inspect the returned company’s own model

Search cards are compact. Use `data.companies[].domain` from a reviewed result;
**`candidate.example` below is a placeholder, not a claimed company match**.
Column batches accept up to 20 domains. Column values are formatted summaries,
not precise dated financial facts.

**POST `/v1/companies/columns`** · MCP `get_company_columns`

<!-- business-request: 57-hybrid-subscription-and-commission-columns -->
```json
{
  "domains": [
    "candidate.example"
  ],
  "columns": [
    "industry",
    "business_model",
    "revenue_model",
    "country",
    "latest_revenue"
  ]
}
```

**POST `/v1/companies/profile`** · MCP `get_company`

<!-- business-request: 57-hybrid-subscription-and-commission-profile -->
```json
{
  "domain": "candidate.example"
}
```

Inspect `available_fields` and `field_status` before the separate field read:

**POST `/v1/companies/field`** · MCP `get_company_field`

<!-- business-request: 57-hybrid-subscription-and-commission-classification -->
```json
{
  "domain": "candidate.example",
  "field": "classification",
  "item_limit": 100
}
```

Keep `data.value.business_models`, `data.value.revenue_models`, `data.updated_at`,
`data.status`, `data.coverage.partial` and the array coverage for
`/value/revenue_models`. An unavailable field is unresolved evidence, not an empty
business model. Use a separate `overview` or `products` field read when listed as
available and inspect dated source pricing/terms for fee details the API does not contain.

| Evidence to review | How to interpret it |
|---|---|
| Both tags | Require subscription and commission on transaction in the same company classification. A search match alone cannot satisfy the all-of condition. |
| Missing classification | Keep unavailable, truncated or incomplete classifications unresolved. Absence from a bounded array does not prove the tag is absent. |
| Economic importance | Having two labels says nothing about their revenue shares, active plans or current prices. |

The separate classification store and the search index can disagree or have different dates. Retain that discrepancy; do not overwrite one source with the other.

## Accept, reject or leave unresolved

Check `data.matching.filters_restricted`, each card’s `match_tier`, excluded
candidates, access limits and partial results. `strict` means the source labelled
the candidate strict and retained the requested filters; it is not independent
verification of the commercial model. Semantic wording still needs review.

Follow `data.next_page` even when a strict page returns no companies: that page
may have contained only excluded candidates. Keep filters fixed, stop when the
continuation hint is absent or the allowed page bound is reached, and deduplicate
by domain. An empty page or failed upstream read does not prove the segment is empty.

For a final export, retain the domain, source model labels, classification date,
review status and any pricing/terms evidence. Leave unsupported rates, billing
events and revenue shares unknown. The [guide’s evidence table](../guides/business-model-revenue-model-api.md#build-a-reviewable-result)
separates API fields from client-reviewed conclusions.

## Saved evidence: a marketplace flag is not a commission tag

This is a selected-field projection from the [complete saved Swiggy classification](../examples/fields/swiggy.com-classification.json),
captured 2026-09-23. It is not a response to this new search.

<!-- business-saved-output: swiggy-models -->
```json
{
  "domain": "swiggy.com",
  "updated_at": "2026-06-01T04:43:22.775000+00:00",
  "revenue_models": [
    "e-commerce - service",
    "subscription"
  ],
  "marketplace_flag": "YES",
  "revenue_models_coverage": {
    "available": 2,
    "returned": 2,
    "truncated": false
  }
}
```

The snapshot includes a Marketplace flag and subscription/e-commerce service tags,
but no `commission on transaction` label. It therefore does not support a
subscription-plus-commission tag match. It also does not prove what Swiggy’s actual
commercial contracts charge. Do not fill the missing label from brand familiarity.

## Require both tags in the client

The API request above is an OR search. Given a saved or newly returned
`get_company_field` response, this client-side check retains an explicit unknown
state when coverage is unavailable. It evaluates the observed snapshot only.

```python
required = {"subscription", "commission on transaction"}
data = response.get("data") or {}
coverage = data.get("coverage") or {}
array = (coverage.get("arrays") or {}).get("/value/revenue_models") or {}
models = (data.get("value") or {}).get("revenue_models")
if (not response.get("ok") or data.get("status") != "available"
        or (response.get("meta") or {}).get("partial")
        or coverage.get("partial") is not False or array.get("truncated") is not False
        or not isinstance(models, list) or not all(isinstance(v, str) for v in models)
        or array.get("returned") != len(models) or array.get("available") != len(models)):
    review = "unknown"
else:
    observed = {v.casefold() for v in models}
    review = "both tags observed" if required <= observed else "not both tags in this snapshot"
```

The saved Swiggy example evaluates to `not both tags in this snapshot`. A missing
classification must evaluate to `unknown`. A future pricing check is a separate
review outcome; do not label the catalogue test as fee verification.
