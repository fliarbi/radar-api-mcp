# Find insurance distributors with commission-based revenue

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** Find insurance broker, intermediary or distribution-platform candidates tagged with transaction commission revenue.

**Validation status:** request schemas and known catalogue values checked locally.
The exact main-search response is captured below, including any empty result or denial.
Additional variants are request recipes unless their captured output is shown.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

**POST `/v1/companies/filter-options`** · MCP `company_filter_options`

<!-- business-request: 54-insurance-broker-commission-lookup -->
```json
{
  "field": "industries",
  "q": "Insurance",
  "limit": 10
}
```

The following is the actual local output of the catalogue handler. This lookup
used no company-store connection and was not an HTTP/live-company search.

<!-- business-local-output: 54-insurance-broker-commission-lookup -->
```json
{
  "field": "industries",
  "query": "Insurance",
  "options": [
    "Insurance"
  ],
  "returned": 1,
  "complete": false,
  "note": "Suggestions are bounded matches, not the complete company universe."
}
```

## Main request

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 54-insurance-broker-commission-search -->
```json
{
  "filters": {
    "industries": [
      "Insurance"
    ],
    "revenue_models": [
      "commission on transaction"
    ]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

Insurance includes carriers, software providers and distributors. Use classification and product descriptions to establish the candidate’s business activity after applying the revenue-model filter.

Set `RADAR_BASE_URL` to your operator-supplied gateway and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL/v1/companies/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"industries":["Insurance"],"revenue_models":["commission on transaction"]},"match_mode":"strict","page":0,"limit":20}'
```

Equivalent MCP tool call:

<!-- business-mcp: 54-insurance-broker-commission-search -->
```json
{
  "name": "search_companies",
  "arguments": {
    "request": {
      "filters": {
        "industries": [
          "Insurance"
        ],
        "revenue_models": [
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

**HTTP 200: 20 returned companies**, captured **2026-09-25T16:17:58.036862+00:00** through the authenticated
local gateway calling its configured Radar source. This is an actual response,
including empty results and denials. Retrieval time does not certify the age of
the underlying source or independently verify a company's fee contract.

| Returned company | Domain | Source matching tier |
|---|---|---|
| Star Health and Allied Insurance | starhealth.in | strict |
| Root | joinroot.com | strict |
| ACKO | acko.com | strict |
| Assurekit | assurekit.com | strict |
| Brown & Brown Insurance | bbinsurance.com | strict |
| Digit Insurance | godigit.com | strict |
| Hagerty | hagerty.com | strict |
| IndiaFirst Life | indiafirstlife.com | strict |
| Lemonade | lemonade.com | strict |
| Niva Bupa | nivabupa.com | strict |
| QuickInsure | quickinsure.co.in | strict |
| Toffee | toffeeinsurance.com | strict |
| Unknown | Unknown | strict |
| AIG | aig.com | strict |
| American Equity | american-equity.com | strict |
| Allied World Assurance Company | awac.com | strict |
| Azur | azuruw.com | strict |
| Bamboo Insurance | bambooinsurance.com | strict |
| Beacon | beacon.co.in | strict |
| Coverfox Insurance | coverfox.com | strict |

These are source-matched candidates. The classification read below inspects one
returned domain; it does not verify all companies or their pricing terms.

<details open>
<summary>Complete captured search_companies response</summary>

<!-- business-live-response: 54-insurance-broker-commission-search -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
    "companies": [
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
        "linkedin_slug": "rootinsuranceco",
        "location": {
          "c": "united states",
          "rg": "ohio",
          "l": "columbus",
          "lc": "columbus, ohio, united states",
          "hq": "columbus",
          "cc": "us",
          "coord": [
            -82.99879,
            39.96118
          ],
          "g": "39.96118,-82.99879"
        },
        "has_email": false,
        "hq": "columbus",
        "domain": "joinroot.com",
        "founded": "2015",
        "company_id": "1bqeywjfu4",
        "tagline": "Provider of car insurance rates based primarily on driving behavior",
        "size": "1001-5000",
        "description": "Provider of car insurance rates based primarily on driving behavior",
        "slug": "root",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "Root",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=joinroot.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "acko",
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
        "domain": "acko.com",
        "founded": "2016",
        "company_id": "2hhxqo0uwg",
        "tagline": "Provider of car, bike, health, life, and travel insurance policies",
        "size": "1001-5000",
        "description": "Provider of car, bike, health, life, and travel insurance policies",
        "slug": "acko",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "ACKO",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=acko.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "assurekit",
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
        "domain": "assurekit.com",
        "founded": "2019",
        "company_id": "12dvzo5og5",
        "tagline": "Insurance processing and distribution management solution for the insurance industry",
        "size": "11-50",
        "description": "Insurance processing and distribution management solution for the insurance industry",
        "slug": "assurekit",
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "name": "Assurekit",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=assurekit.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "brown-&-brown",
        "location": {
          "c": "united states",
          "rg": "florida",
          "l": "daytona beach",
          "lc": "daytona beach, florida, united states",
          "hq": "daytona beach",
          "cc": "us",
          "coord": [
            -81.02283,
            29.21081
          ],
          "g": "29.21081,-81.02283"
        },
        "has_email": false,
        "hq": "daytona beach",
        "domain": "bbinsurance.com",
        "founded": "1939",
        "company_id": "ylbwklbmof",
        "tagline": "Provider of insurance brokerage services",
        "size": "5001-10000",
        "description": "Provider of insurance brokerage services",
        "slug": "brown-brown-insurance",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "Brown & Brown Insurance",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=bbinsurance.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "godigit",
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
        "domain": "godigit.com",
        "founded": "2016",
        "company_id": "2a4qvopz46",
        "tagline": "Provider of general and life insurance products across various categories",
        "size": "501-1000",
        "description": "Provider of general and life insurance products across various categories",
        "slug": "digit-insurance",
        "flags": [
          [
            "Medium Enterprise",
            "size"
          ]
        ],
        "name": "Digit Insurance",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=godigit.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "hagertycars",
        "location": {
          "c": "united states",
          "rg": "michigan",
          "l": "traverse city",
          "lc": "traverse city, michigan, united states",
          "hq": "traverse city",
          "cc": "us",
          "coord": [
            -85.62063,
            44.76306
          ],
          "g": "44.76306,-85.62063"
        },
        "has_email": false,
        "hq": "traverse city",
        "domain": "hagerty.com",
        "founded": "1983",
        "company_id": "3uwctyusv4",
        "tagline": "Automotive insurance solution provider to users",
        "size": "1001-5000",
        "description": "Automotive insurance solution provider to users",
        "slug": "hagerty",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "Hagerty",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=hagerty.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "indiafirst-life-insurance-company-limited",
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
        "domain": "indiafirstlife.com",
        "founded": "2009",
        "company_id": "397muhyo5i",
        "tagline": "Provider of life & health insurance services to individuals and families",
        "size": "1001-5000",
        "description": "Provider of life & health insurance services to individuals and families",
        "slug": "indiafirst-life",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "IndiaFirst Life",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=indiafirstlife.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "lemonade-inc-",
        "location": {
          "c": "united states",
          "rg": "new york",
          "l": "new york city",
          "lc": "new york city, new york, united states",
          "hq": "new york city",
          "cc": "us",
          "coord": [
            -74.00597,
            40.71427
          ],
          "g": "40.71427,-74.00597"
        },
        "has_email": false,
        "hq": "new york city",
        "domain": "lemonade.com",
        "founded": "2015",
        "company_id": "1zx3q9lqq3",
        "tagline": "Provider of various insurance policies including car, pet, home, and life",
        "size": "1001-5000",
        "description": "Provider of various insurance policies including car, pet, home, and life",
        "slug": "lemonade",
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "name": "Lemonade",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=lemonade.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "niva-bupa",
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
        "domain": "nivabupa.com",
        "founded": "2008",
        "company_id": "9yu6ik8ak5",
        "tagline": "Online platform offering multiple insurance service",
        "size": "10000+",
        "description": "Online platform offering multiple insurance service",
        "slug": "niva-bupa",
        "flags": [],
        "name": "Niva Bupa",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=nivabupa.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "quickinsure",
        "location": {
          "c": "india",
          "rg": "maharashtra",
          "l": "pune",
          "lc": "pune, maharashtra, india",
          "hq": "pune",
          "cc": "in",
          "coord": [
            73.85535,
            18.51957
          ],
          "g": "18.51957,73.85535"
        },
        "has_email": false,
        "hq": "pune",
        "domain": "quickinsure.co.in",
        "founded": "2016",
        "company_id": "wz12j49rsv",
        "tagline": "Provider of platform to compare and buy insurance policies online",
        "size": "51-200",
        "description": "Provider of platform to compare and buy insurance policies online",
        "slug": "quickinsure",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "name": "QuickInsure",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=quickinsure.co.in",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "toffee-insurance",
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
        "domain": "toffeeinsurance.com",
        "founded": "2017",
        "company_id": "27xjbyv8ya",
        "tagline": "Online platform for health and property and casualty insurances",
        "size": "11-50",
        "description": "Online platform for health and property and casualty insurances",
        "slug": "toffee",
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "name": "Toffee",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=toffeeinsurance.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "infinite-finance-australia-pty-ltd",
        "location": {},
        "has_email": false,
        "hq": "",
        "domain": "",
        "founded": "",
        "company_id": 330246,
        "tagline": "Cohort is a business consulting company that provides staffing, payroll, and industrial training services.",
        "size": "",
        "description": "Cohort is a business consulting company that provides staffing, payroll, and industrial training services.",
        "slug": "kadapa-ktm",
        "flags": [],
        "name": "",
        "has_phone": false,
        "logo_url": null,
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "aig",
        "location": {
          "c": "united states",
          "rg": "new york",
          "l": "new york city",
          "lc": "new york city, new york, united states",
          "hq": "new york city",
          "cc": "us",
          "coord": [
            -74.00597,
            40.71427
          ],
          "g": "40.71427,-74.00597"
        },
        "has_email": false,
        "hq": "new york city",
        "domain": "aig.com",
        "founded": "1919",
        "company_id": "vbs583l6nd",
        "tagline": "Internet first provider of life, health, accident & travel insurance services",
        "size": "10000+",
        "description": "Internet first provider of life, health, accident & travel insurance services",
        "slug": "aig",
        "flags": [],
        "name": "AIG",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=aig.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "american-equity",
        "location": {
          "c": "united states",
          "rg": "iowa",
          "l": "west des moines",
          "lc": "west des moines, iowa, united states",
          "hq": "west des moines",
          "cc": "us",
          "coord": [
            -93.71133,
            41.57721
          ],
          "g": "41.57721,-93.71133"
        },
        "has_email": false,
        "hq": "west des moines",
        "domain": "american-equity.com",
        "founded": "1980",
        "company_id": "dxq2is2bdq",
        "tagline": "Internet first provider of life insurance services",
        "size": "501-1000",
        "description": "Internet first provider of life insurance services",
        "slug": "american-equity",
        "flags": [
          [
            "Medium Enterprise",
            "size"
          ]
        ],
        "name": "American Equity",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=american-equity.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "allied-world",
        "location": {
          "c": "switzerland",
          "rg": "canton of zug",
          "l": "zug",
          "lc": "zug, canton of zug, switzerland",
          "hq": "zug",
          "cc": "bm",
          "coord": [
            -64.78303,
            32.2949
          ],
          "g": "32.2949,-64.78303"
        },
        "has_email": false,
        "hq": "zug",
        "domain": "awac.com",
        "founded": "2001",
        "company_id": "11hnu2dpaf",
        "tagline": "Diversified insurance company",
        "size": "501-1000",
        "description": "Diversified insurance company",
        "slug": "allied-world-assurance-company",
        "flags": [
          [
            "Medium Enterprise",
            "size"
          ]
        ],
        "name": "Allied World Assurance Company",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=awac.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "azur-underwriting-ltd",
        "location": {
          "c": "united kingdom",
          "rg": "england",
          "l": "london",
          "lc": "london, england, united kingdom",
          "hq": "london",
          "cc": "gb",
          "coord": [
            -0.12574,
            51.50853
          ],
          "g": "51.50853,-0.12574"
        },
        "has_email": false,
        "hq": "london",
        "domain": "azuruw.com",
        "founded": "2016",
        "company_id": "3fpzc2lmle",
        "tagline": "Developer of insurance products for brokers and clients",
        "size": "51-200",
        "description": "Developer of insurance products for brokers and clients",
        "slug": "azur",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "name": "Azur",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=azuruw.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "bamboo-insurance",
        "location": {
          "c": "united states",
          "rg": "california",
          "l": "gold river",
          "lc": "gold river, california, united states",
          "hq": "gold river",
          "cc": "us",
          "coord": [
            -121.24662,
            38.62629
          ],
          "g": "38.62629,-121.24662"
        },
        "has_email": false,
        "hq": "gold river",
        "domain": "bambooinsurance.com",
        "founded": "2017",
        "company_id": "49cc4zybp1",
        "tagline": "Online comparison platform for property & casualty insurance",
        "size": "51-200",
        "description": "Online comparison platform for property & casualty insurance",
        "slug": "bamboo-insurance",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "name": "Bamboo Insurance",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=bambooinsurance.com",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "beacon-insurance-brokers-pvt.-ltd.",
        "location": {
          "c": "india",
          "rg": "gujarat",
          "l": "vadodara",
          "lc": "vadodara, gujarat, india",
          "hq": "vadodara",
          "cc": "in",
          "coord": [
            73.20812,
            22.29941
          ],
          "g": "22.29941,73.20812"
        },
        "has_email": false,
        "hq": "vadodara",
        "domain": "beacon.co.in",
        "founded": "2005",
        "company_id": "3jd5on731b",
        "tagline": "Provider of insurance broking services for direct and reinsurance business",
        "size": "501-1000",
        "description": "Provider of insurance broking services for direct and reinsurance business",
        "slug": "beacon",
        "flags": [
          [
            "Medium Enterprise",
            "size"
          ]
        ],
        "name": "Beacon",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=beacon.co.in",
        "match_tier": "strict"
      },
      {
        "linkedin_slug": "coverfox-insurance",
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
        "domain": "coverfox.com",
        "founded": "2013",
        "company_id": "2qebz4jglf",
        "tagline": "Provider of platform to compare and purchase various insurance policies online",
        "size": "51-200",
        "description": "Provider of platform to compare and purchase various insurance policies online",
        "slug": "coverfox-insurance",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "name": "Coverfox Insurance",
        "has_phone": false,
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=coverfox.com",
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
          "count": 36796,
          "added": 20
        }
      ],
      "source_rows": 20,
      "excluded_candidates": 0,
      "strict_count_reported": 36796,
      "candidate_pool_count_reported": 36796,
      "count_capped": false,
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
    "retrieved_at": "2026-09-25T16:17:58.036598+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

</details>

[Download this request and full response](../examples/business-models/54-insurance-broker-commission-search.json). All returned fields and rows are preserved; SHA-256 fingerprints are included.

### Captured `get_company` for a returned company

POST `/v1/companies/profile`, HTTP **200**, captured **2026-09-25T16:17:58.046405+00:00**.

<!-- business-live-request: 54-insurance-broker-commission-profile -->
```json
{
  "domain": "starhealth.in"
}
```

<details open>
<summary>Complete captured get_company response</summary>

<!-- business-live-response: 54-insurance-broker-commission-profile -->
```json
{
  "ok": true,
  "feature": "get_company",
  "data": {
    "company": {
      "company_id": "21tsejrkxw",
      "domain": "starhealth.in",
      "name": "Star Health and Allied Insurance",
      "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=starhealth.in",
      "description": "Provider of health insurance services",
      "founded": 2006,
      "employee_count": 17638
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
    "retrieved_at": "2026-09-25T16:17:58.046233+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

</details>

[Download this request and full response](../examples/business-models/54-insurance-broker-commission-profile.json). All returned fields and rows are preserved; SHA-256 fingerprints are included.

### Captured `get_company_field` for a returned company

POST `/v1/companies/field`, HTTP **200**, captured **2026-09-25T16:17:58.048883+00:00**.

<!-- business-live-request: 54-insurance-broker-commission-classification -->
```json
{
  "domain": "starhealth.in",
  "field": "classification",
  "item_limit": 100
}
```

<details open>
<summary>Complete captured get_company_field response</summary>

<!-- business-live-response: 54-insurance-broker-commission-classification -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "starhealth.in",
    "company_id": "21tsejrkxw",
    "field": "classification",
    "value": {
      "sectors": [
        "Financial Services"
      ],
      "sector_details": [
        {
          "name": "Financial Services",
          "classification": "Other Markets"
        }
      ],
      "markets": [
        "Insurance Carriers"
      ],
      "feeds": {
        "primary": [
          "Insurance Carriers"
        ],
        "other": []
      },
      "business_models": [
        "Health"
      ],
      "revenue_models": [
        "commission on transaction",
        "e-commerce - product",
        "e-commerce - service"
      ],
      "industries": [
        "insurance"
      ],
      "company_types": [
        "Corporate"
      ],
      "flags": {
        "Artificial Intelligence": "NO",
        "Consumer": "Untagged",
        "Enterprise": "Untagged",
        "Marketplace": "Untagged",
        "SaaS": "Untagged",
        "Tech": "Untagged",
        "Software": "Untagged",
        "Tech Hardware": "Untagged",
        "Social Impact": "Untagged",
        "Blockchain": "Untagged",
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
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/sector_details": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/markets": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/feeds/primary": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/feeds/other": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/business_models": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/revenue_models": {
          "available": 3,
          "returned": 3,
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
    "retrieved_at": "2026-09-25T16:17:58.048739+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

</details>

[Download this request and full response](../examples/business-models/54-insurance-broker-commission-classification.json). All returned fields and rows are preserved; SHA-256 fingerprints are included.

The returned Star Health classification includes `commission on transaction`,
but that label does not establish that it is a broker. Review the company’s
actual role before accepting it into an insurance-distributor list.

## Related request variants

### Explore distributor wording with the same revenue predicate

**POST `/v1/companies/semantic-search`** · MCP `semantic_company_search`

<!-- business-request: 54-insurance-broker-commission-variant-1 -->
```json
{
  "q": "insurance brokers and distribution platforms earning policy commissions",
  "filters": {
    "industries": [
      "Insurance"
    ],
    "revenue_models": [
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

<!-- business-request: 54-insurance-broker-commission-columns -->
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

<!-- business-request: 54-insurance-broker-commission-profile -->
```json
{
  "domain": "candidate.example"
}
```

Inspect `available_fields` and `field_status` before the separate field read:

**POST `/v1/companies/field`** · MCP `get_company_field`

<!-- business-request: 54-insurance-broker-commission-classification -->
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
| Role | Distinguish underwriting from brokerage, comparison, distribution and insurance software. |
| Commission basis | Check whether the source describes new policies, renewals or premiums as the basis. Preserve the documented payer and date. |
| Revenue versus premium | Do not equate premium volume with the intermediary’s commission revenue. |

A business classification does not establish a licence, regulatory status or current authorization. Those are separate legal-record questions.

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
