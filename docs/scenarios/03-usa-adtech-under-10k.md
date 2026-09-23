# Find US AdTech startups founded since 2021 with latest annual revenue below USD 10,000.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/screen_company_financials.md)

**POST `/v1/companies/financials/screen`** · MCP tool **`screen_company_financials`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 03-usa-adtech-under-10k -->
```json
{
  "filters": {
    "industries": [
      "AdTech"
    ],
    "locations": [
      "United States"
    ],
    "founded_year_from": 2021
  },
  "constraints": [
    {
      "metric": "revenue",
      "lt": 10000,
      "gte": 0
    }
  ],
  "period_type": "annual",
  "candidate_limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:31.603845+00:00; HTTP **200**;
**qualified**, 0.181 seconds.
Local authenticated gateway with live configured read-only sources.

Partial result or source timeout; Coverage is explicitly bounded; No rows observed; not proof of a complete negative.

Read all evaluated rows, not just matches. Numeric conditions use the same latest accessible fiscal period. Unknown means missing or disallowed evidence; unavailable means a failed read. Neither becomes zero. This is a bounded candidate screen with source gates, not an exhaustive company database query. Its per-metric checks preserve currency, source type and inclusive/exclusive bounds.

The three observed domains were adster.tech, markopolo.ai and topsort.com. All three lacked accessible annual periods, so this run established no below-$10,000 match. Startup is explicitly defined by founded_year_from=2021, not inferred from company size.

The baseline was an unavailable operation registry check (no HTTP request), **unavailable**:
not_implemented. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 03-usa-adtech-under-10k -->
```json
{
  "ok": true,
  "feature": "screen_company_financials",
  "data": {
    "matches": [],
    "evaluated": [
      {
        "domain": "adster.tech",
        "company": {
          "hq": "highland",
          "tagline": "Ad revenue solutions for mobile apps and websites",
          "has_phone": false,
          "flags": [],
          "domain": "adster.tech",
          "slug": "adster",
          "company_id": "1vmw19subl",
          "linkedin_slug": "adster-tech",
          "location": {
            "c": "united states",
            "rg": "new york",
            "l": "highland",
            "lc": "highland, new york, united states",
            "hq": "highland",
            "cc": "",
            "coord": [
              -117.20865,
              34.12834
            ],
            "g": "34.12834,-117.20865"
          },
          "founded": "2023",
          "name": "Adster",
          "size": "",
          "has_email": false,
          "description": "Ad revenue solutions for mobile apps and websites",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=adster.tech",
          "match_tier": "strict"
        },
        "status": "unknown",
        "reason": "No accessible period matches the requested type/year window",
        "period": null,
        "checks": [],
        "access_limited": false,
        "successful_read": true
      },
      {
        "domain": "markopolo.ai",
        "company": {
          "hq": "dover",
          "tagline": "AI based customer data platform for customer insights",
          "has_phone": false,
          "flags": [
            [
              "Tiny Enterprise",
              "size"
            ]
          ],
          "domain": "markopolo.ai",
          "slug": "marko-polo",
          "company_id": "1myf3prr7v",
          "linkedin_slug": "markopolo-ai",
          "location": {
            "c": "united states",
            "rg": "delaware",
            "l": "dover",
            "lc": "dover, delaware, united states",
            "hq": "dover",
            "cc": "us",
            "coord": [
              -75.52437,
              39.15817
            ],
            "g": "39.15817,-75.52437"
          },
          "founded": "2021",
          "name": "Marko Polo",
          "size": "1-10",
          "has_email": false,
          "description": "AI based customer data platform for customer insights",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=markopolo.ai",
          "match_tier": "strict"
        },
        "status": "unknown",
        "reason": "No accessible period matches the requested type/year window",
        "period": null,
        "checks": [],
        "access_limited": false,
        "successful_read": true
      },
      {
        "domain": "topsort.com",
        "company": {
          "hq": "cambridge",
          "tagline": "Provider of an AI-powered platform for retailers to manage advertising businesses",
          "has_phone": false,
          "flags": [
            [
              "Tiny Enterprise",
              "size"
            ]
          ],
          "domain": "topsort.com",
          "slug": "topsort",
          "company_id": "gry5crzx1q",
          "linkedin_slug": "topsort",
          "location": {
            "c": "united states",
            "rg": "massachusetts",
            "l": "cambridge",
            "lc": "cambridge, massachusetts, united states",
            "hq": "cambridge",
            "cc": "us",
            "coord": [
              -71.10561,
              42.3751
            ],
            "g": "42.3751,-71.10561"
          },
          "founded": "2021",
          "name": "Topsort",
          "size": "11-50",
          "has_email": false,
          "description": "Provider of an AI-powered platform for retailers to manage advertising businesses",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=topsort.com",
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
      "unknown": 3
    },
    "constraints": [
      {
        "metric": "revenue",
        "gte": 0.0,
        "lt": 10000.0
      }
    ],
    "period_type": "annual",
    "source_type": "any",
    "discovery": {
      "companies": [
        {
          "hq": "highland",
          "tagline": "Ad revenue solutions for mobile apps and websites",
          "has_phone": false,
          "flags": [],
          "domain": "adster.tech",
          "slug": "adster",
          "company_id": "1vmw19subl",
          "linkedin_slug": "adster-tech",
          "location": {
            "c": "united states",
            "rg": "new york",
            "l": "highland",
            "lc": "highland, new york, united states",
            "hq": "highland",
            "cc": "",
            "coord": [
              -117.20865,
              34.12834
            ],
            "g": "34.12834,-117.20865"
          },
          "founded": "2023",
          "name": "Adster",
          "size": "",
          "has_email": false,
          "description": "Ad revenue solutions for mobile apps and websites",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=adster.tech",
          "match_tier": "strict"
        },
        {
          "hq": "dover",
          "tagline": "AI based customer data platform for customer insights",
          "has_phone": false,
          "flags": [
            [
              "Tiny Enterprise",
              "size"
            ]
          ],
          "domain": "markopolo.ai",
          "slug": "marko-polo",
          "company_id": "1myf3prr7v",
          "linkedin_slug": "markopolo-ai",
          "location": {
            "c": "united states",
            "rg": "delaware",
            "l": "dover",
            "lc": "dover, delaware, united states",
            "hq": "dover",
            "cc": "us",
            "coord": [
              -75.52437,
              39.15817
            ],
            "g": "39.15817,-75.52437"
          },
          "founded": "2021",
          "name": "Marko Polo",
          "size": "1-10",
          "has_email": false,
          "description": "AI based customer data platform for customer insights",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=markopolo.ai",
          "match_tier": "strict"
        },
        {
          "hq": "cambridge",
          "tagline": "Provider of an AI-powered platform for retailers to manage advertising businesses",
          "has_phone": false,
          "flags": [
            [
              "Tiny Enterprise",
              "size"
            ]
          ],
          "domain": "topsort.com",
          "slug": "topsort",
          "company_id": "gry5crzx1q",
          "linkedin_slug": "topsort",
          "location": {
            "c": "united states",
            "rg": "massachusetts",
            "l": "cambridge",
            "lc": "cambridge, massachusetts, united states",
            "hq": "cambridge",
            "cc": "us",
            "coord": [
              -71.10561,
              42.3751
            ],
            "g": "42.3751,-71.10561"
          },
          "founded": "2021",
          "name": "Topsort",
          "size": "11-50",
          "has_email": false,
          "description": "Provider of an AI-powered platform for retailers to manage advertising businesses",
          "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=topsort.com",
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
            "count": 380,
            "added": 3
          }
        ],
        "source_rows": 3,
        "excluded_candidates": 0,
        "strict_count_reported": 380,
        "candidate_pool_count_reported": 380,
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
    "retrieved_at": "2026-09-23T03:35:31.603638+00:00",
    "partial": true,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/03-usa-adtech-under-10k.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
