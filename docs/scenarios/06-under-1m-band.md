# Find US AdTech candidates in Radar’s positive-revenue under-USD-1M band.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/search_companies.md)

**POST `/v1/companies/search`** · MCP tool **`search_companies`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 companies; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 06-under-1m-band -->
```json
{
  "filters": {
    "industries": [
      "AdTech"
    ],
    "locations": [
      "United States"
    ],
    "revenue_bands": [
      "under1m"
    ]
  },
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:31.687122+00:00; HTTP **200**;
**qualified**, 0.059 seconds.
Local authenticated gateway with live configured read-only sources.

Source-labelled predicates; cards do not independently verify financial/classification conditions.

Read each match_tier and the matching/excluded_candidates count before accepting the shortlist. Strict is the source's label, not an independent verification of every company attribute. Financial bands refer to source summary fields, not a selected fiscal year; retrieve financial evidence separately. Advance source pages even if strict filtering leaves an empty page with a continuation hint.

The baseline was HTTP 200, **qualified**:
Source-labelled predicates; cards do not independently verify financial/classification conditions. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 06-under-1m-band -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
    "companies": [
      {
        "hq": "redwood city",
        "tagline": "Offers supply side and demand side platform",
        "has_phone": false,
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "domain": "yume.com",
        "slug": "yume",
        "company_id": "3bajdhc7lb",
        "linkedin_slug": "yume",
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
        "founded": "2004",
        "name": "YuMe",
        "size": "51-200",
        "has_email": false,
        "description": "Offers supply side and demand side platform",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=yume.com",
        "match_tier": "strict"
      },
      {
        "hq": "minneapolis",
        "tagline": "Digital marketing agency driving growth through innovative strategies and measurable results",
        "has_phone": false,
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "domain": "trybrick.com",
        "slug": "brick",
        "company_id": "119hd631z2",
        "linkedin_slug": "brick-inc-",
        "location": {
          "c": "united states",
          "rg": "minnesota",
          "l": "minneapolis",
          "lc": "minneapolis, minnesota, united states",
          "hq": "minneapolis",
          "cc": "us",
          "coord": [
            -93.26384,
            44.97997
          ],
          "g": "44.97997,-93.26384"
        },
        "founded": "1996",
        "name": "Brick",
        "size": "1-10",
        "has_email": false,
        "description": "Digital marketing agency driving growth through innovative strategies and measurable results",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=trybrick.com",
        "match_tier": "strict"
      },
      {
        "hq": "new york city",
        "tagline": "Provider of data management platform for forecasting locations",
        "has_phone": false,
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "domain": "unacast.com",
        "slug": "unacast",
        "company_id": "1ts1rmlkzy",
        "linkedin_slug": "unacast",
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
        "founded": "2015",
        "name": "Unacast",
        "size": "11-50",
        "has_email": false,
        "description": "Provider of data management platform for forecasting locations",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=unacast.com",
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
          "count": 13,
          "added": 3
        }
      ],
      "source_rows": 3,
      "excluded_candidates": 0,
      "strict_count_reported": 13,
      "candidate_pool_count_reported": 13,
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
    "retrieved_at": "2026-09-23T03:35:31.686938+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/06-under-1m-band.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
