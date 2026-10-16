# Find US AdTech companies founded from 2021 through 2026 without assuming a funding stage.

[All 50 scenarios](README.md) · [Workflow guide](../guides/company-search-api.md) · [Endpoint reference](../reference/search_companies.md)

**POST `/v1/companies/search`** · MCP tool **`search_companies`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 companies; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 10-startup-age -->
```json
{
  "filters": {
    "industries": [
      "AdTech"
    ],
    "locations": [
      "United States"
    ],
    "founded_year_from": 2021,
    "founded_year_to": 2026
  },
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:31.879605+00:00; HTTP **200**;
**observed**, 0.102 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

Read each match_tier and the matching/excluded_candidates count before accepting the shortlist. Strict is the source's label, not an independent verification of every company attribute. Financial bands refer to source summary fields, not a selected fiscal year; retrieve financial evidence separately. Advance source pages even if strict filtering leaves an empty page with a continuation hint.

The baseline was HTTP 200, **observed**:
Response contract and declared scenario checks passed; source truth not independently certified. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 10-startup-age -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
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
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:31.879416+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/10-startup-age.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
