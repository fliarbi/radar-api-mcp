# Potential-company data: actual investment and sales-research outputs

These are two additional local authenticated gateway captures of
`POST /v1/companies/opportunities/search`. They complement the
[mobile-scale example](reference/search_opportunities.md) and use the same
companies scope, API key and one-credit successful-operation contract.
No source stores, Radar accounts or public deployment were changed.

The profitable-growth screen returned Quantafic Business Solution and Fino Payments
Bank, with recorded revenue display values of $853K and $218.5M. The hiring screen
returned FreeCharge and One97 Communications, with revenue display values of
$36.9M and $902.0M. These are source display columns, not independently verified
financial statements or current purchase intent. Retrieve dated financials and
hiring details before interpreting them. Missing employee/funding cells stay null.

Both captured responses retain the free source plan and exact submitted criteria.
The source supplies no per-row proof explaining every matched predicate; a result
is a source-filtered candidate, not a fully verified investment or sales lead.

## profitable_growth

```json
{
  "preset": "profitable_growth",
  "filters": {
    "locations": [
      "India"
    ],
    "markets": [
      "Payments"
    ]
  },
  "limit": 2
}
```

<!-- opportunity-response: profitable_growth -->
```json
{
  "ok": true,
  "feature": "search_opportunities",
  "data": {
    "companies": [
      {
        "description": "Web-based customer background verification platform",
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
        "name": "Quantafic Business Solution",
        "linkedin_slug": "quantafic-business-solutions-llp",
        "founded": "2014",
        "has_phone": false,
        "domain": "quantafic.com",
        "tagline": "Web-based customer background verification platform",
        "slug": "quantafic-business-solution",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "company_id": "xo3gd09cot",
        "hq": "mumbai",
        "size": "51-200",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=quantafic.com"
      },
      {
        "description": "Commercial bank offering cost-effective, digital financial services",
        "location": {
          "l": "mumbai",
          "rg": "maharashtra",
          "c": "india",
          "cc": "IN",
          "cnt": "asia",
          "coord": [
            72.845,
            18.9681
          ],
          "rg_w": "southern and central asia"
        },
        "has_email": false,
        "name": "Fino Payments Bank",
        "linkedin_slug": "fino",
        "founded": "2006",
        "has_phone": false,
        "domain": "finobank.com",
        "tagline": "Commercial bank offering cost-effective, digital financial services",
        "slug": "fino-agency",
        "flags": [
          [
            "3 Financing Rounds",
            "rounds"
          ],
          [
            "$35.0M Total Funding",
            "total_funding"
          ]
        ],
        "company_id": 278941,
        "hq": "mumbai",
        "size": "",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=finobank.com"
      }
    ],
    "page": 0,
    "requested_limit": 2,
    "returned": 2,
    "total": null,
    "access": {
      "plan": "free",
      "results_capped": false,
      "searches_remaining": 50
    },
    "partial_timeout": false,
    "matching": {},
    "pagination": "Increment page; account caps can apply. No total is inferred from a page.",
    "preset": "profitable_growth",
    "effective_filters": {
      "markets": [
        "Payments"
      ],
      "locations": [
        "India"
      ],
      "revenue_growth": [
        "growing"
      ],
      "profitability": [
        "profitable"
      ]
    },
    "sort_by": "finance",
    "evidence": [
      {
        "domain": "quantafic.com",
        "columns": {
          "latest_revenue": {
            "label": "Revenue",
            "value": "$853K"
          },
          "growth_stage": null,
          "total_funding": null
        },
        "status": "available"
      },
      {
        "domain": "finobank.com",
        "columns": {
          "latest_revenue": {
            "label": "Revenue",
            "value": "$218.5M"
          },
          "growth_stage": null,
          "total_funding": null
        },
        "status": "available"
      }
    ],
    "interpretation": "Recorded financial bands can be stale or source-plan restricted; use financial statements for exact periods.",
    "coverage": {
      "partial": false,
      "evidence_available": true
    },
    "note": "These are source-filtered candidates, not verified opportunities. Inspect access/restricted_filters and matching metadata; display columns may suppress zero or negative values. Retrieve exact financials and detail fields separately."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T10:50:35.062880+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the actual HTTP 200 capture](examples/opportunities/profitable_growth.json),
recorded 2026-09-21T10:50:35.063071+00:00. No business arrays are shortened.

## hiring_expansion

```json
{
  "preset": "hiring_expansion",
  "filters": {
    "locations": [
      "India"
    ],
    "markets": [
      "Payments"
    ]
  },
  "limit": 2
}
```

<!-- opportunity-response: hiring_expansion -->
```json
{
  "ok": true,
  "feature": "search_opportunities",
  "data": {
    "companies": [
      {
        "description": "Digital wallet for consumer payments",
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
        "name": "FreeCharge",
        "linkedin_slug": "freecharge-in",
        "founded": "2010",
        "has_phone": false,
        "domain": "freecharge.in",
        "tagline": "Digital wallet for consumer payments",
        "slug": "freecharge",
        "flags": [],
        "company_id": "2zsvidbhj9",
        "hq": "gurugram",
        "size": "10000+",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=freecharge.in"
      },
      {
        "description": "Provider of online platform for payments, recharges, financial, and travel services",
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
        "name": "One97 Communications",
        "linkedin_slug": "one97-communications-limited",
        "founded": "2000",
        "has_phone": false,
        "domain": "one97.com",
        "tagline": "Provider of online platform for payments, recharges, financial, and travel services",
        "slug": "one97-communications",
        "flags": [],
        "company_id": "1etlyfq8u9",
        "hq": "noida",
        "size": "10000+",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=one97.com"
      }
    ],
    "page": 0,
    "requested_limit": 2,
    "returned": 2,
    "total": null,
    "access": {
      "plan": "free",
      "results_capped": false,
      "searches_remaining": 50
    },
    "partial_timeout": false,
    "matching": {},
    "pagination": "Increment page; account caps can apply. No total is inferred from a page.",
    "preset": "hiring_expansion",
    "effective_filters": {
      "markets": [
        "Payments"
      ],
      "locations": [
        "India"
      ],
      "hiring": {
        "is_hiring": true,
        "min_open_roles": 1,
        "roles": [],
        "cities": [],
        "recency_days": 90
      }
    },
    "sort_by": "employees",
    "evidence": [
      {
        "domain": "freecharge.in",
        "columns": {
          "employees": null,
          "latest_revenue": {
            "label": "Revenue",
            "value": "$36.9M"
          }
        },
        "status": "available"
      },
      {
        "domain": "one97.com",
        "columns": {
          "employees": null,
          "latest_revenue": {
            "label": "Revenue",
            "value": "$902.0M"
          }
        },
        "status": "available"
      }
    ],
    "interpretation": "Hiring is an observed demand signal, not verified intent to buy a service.",
    "coverage": {
      "partial": false,
      "evidence_available": true
    },
    "note": "These are source-filtered candidates, not verified opportunities. Inspect access/restricted_filters and matching metadata; display columns may suppress zero or negative values. Retrieve exact financials and detail fields separately."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T10:50:35.226428+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the actual HTTP 200 capture](examples/opportunities/hiring_expansion.json),
recorded 2026-09-21T10:50:35.226617+00:00. No business arrays are shortened.

Read the [potential company guide](guides/potential-company-data-api.md) for
investment and sales workflows, nested hiring-role filters and source limitations.
Use [company field details](COMPANY_DATA_DEPTH.md) for follow-up evidence and
[contact access](CONTACTS.md) for the separate email/phone retrieval contract.
