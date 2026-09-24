# Find Indian software candidates with recorded 30–100% revenue growth.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/search_companies.md)

**POST `/v1/companies/search`** · MCP tool **`search_companies`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 companies; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 08-high-growth -->
```json
{
  "filters": {
    "industries": [
      "Software"
    ],
    "locations": [
      "India"
    ],
    "revenue_growth": [
      "high"
    ]
  },
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:31.776382+00:00; HTTP **200**;
**qualified**, 0.088 seconds.
Local authenticated gateway with live configured read-only sources.

Source-labelled predicates; cards do not independently verify financial/classification conditions.

Read each match_tier and the matching/excluded_candidates count before accepting the shortlist. Strict is the source's label, not an independent verification of every company attribute. Financial bands refer to source summary fields, not a selected fiscal year; retrieve financial evidence separately. Advance source pages even if strict filtering leaves an empty page with a continuation hint.

The baseline was HTTP 200, **qualified**:
Source-labelled predicates; cards do not independently verify financial/classification conditions. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 08-high-growth -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
    "companies": [
      {
        "hq": "mumbai",
        "tagline": "SaaS-driven route scheduling software solutions for employee transport management",
        "has_phone": false,
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "domain": "commutec.in",
        "slug": "commutec",
        "company_id": "3tww3wrkqt",
        "linkedin_slug": "commutec",
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
        "founded": "2016",
        "name": "Commutec",
        "size": "51-200",
        "has_email": false,
        "description": "SaaS-driven route scheduling software solutions for employee transport management",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=commutec.in",
        "match_tier": "strict"
      },
      {
        "hq": "noida",
        "tagline": "Cloud-based fleet tracking and management solution",
        "has_phone": false,
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "domain": "ajeevi.com",
        "slug": "ajeevi",
        "company_id": "1m9pls436a",
        "linkedin_slug": "ajeevi",
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
        "founded": "2012",
        "name": "Ajeevi",
        "size": "51-200",
        "has_email": false,
        "description": "Cloud-based fleet tracking and management solution",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=ajeevi.com",
        "match_tier": "strict"
      },
      {
        "hq": "delhi",
        "tagline": "Provides application development services and distributor of software products",
        "has_phone": false,
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "domain": "alpinesoftit.com",
        "slug": "alpinesoft-it-solutions",
        "company_id": "390wz6wkmx",
        "linkedin_slug": "alpinesoft-inc",
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
        "founded": "2010",
        "name": "AlpineSoft IT Solutions",
        "size": "11-50",
        "has_email": false,
        "description": "Provides application development services and distributor of software products",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=alpinesoftit.com",
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
          "count": 38,
          "added": 3
        }
      ],
      "source_rows": 3,
      "excluded_candidates": 0,
      "strict_count_reported": 38,
      "candidate_pool_count_reported": 38,
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
    "retrieved_at": "2026-09-23T03:35:31.776212+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/08-high-growth.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
