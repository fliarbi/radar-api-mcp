# Find US software companies classified with subscription revenue models.

[All 50 scenarios](README.md) · [Workflow guide](../guides/company-search-api.md) · [Endpoint reference](../reference/search_companies.md)

**POST `/v1/companies/search`** · MCP tool **`search_companies`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 companies; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 12-subscription-model -->
```json
{
  "filters": {
    "industries": [
      "Software"
    ],
    "locations": [
      "United States"
    ],
    "revenue_models": [
      "subscription"
    ]
  },
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.172522+00:00; HTTP **200**;
**qualified**, 0.291 seconds.
Local authenticated gateway with live configured read-only sources.

Source-labelled predicates; cards do not independently verify financial/classification conditions.

Read each match_tier and the matching/excluded_candidates count before accepting the shortlist. Strict is the source's label, not an independent verification of every company attribute. Financial bands refer to source summary fields, not a selected fiscal year; retrieve financial evidence separately. Advance source pages even if strict filtering leaves an empty page with a continuation hint.

The baseline was HTTP 200, **qualified**:
Source-labelled predicates; cards do not independently verify financial/classification conditions. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 12-subscription-model -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
    "companies": [
      {
        "hq": "san jose",
        "tagline": "AI based data annotation, model fine-tuning, and validation solutions",
        "has_phone": false,
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "domain": "imerit.net",
        "slug": "imerit",
        "company_id": "208ojrc21t",
        "linkedin_slug": "imerit",
        "location": {
          "c": "united states",
          "rg": "california",
          "l": "san jose",
          "lc": "san jose, california, united states",
          "hq": "san jose",
          "cc": "us",
          "coord": [
            -121.89496,
            37.33939
          ],
          "g": "37.33939,-121.89496"
        },
        "founded": "2012",
        "name": "iMerit",
        "size": "1001-5000",
        "has_email": false,
        "description": "AI based data annotation, model fine-tuning, and validation solutions",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=imerit.net",
        "match_tier": "strict"
      },
      {
        "hq": "san jose",
        "tagline": "Cloud-based video conferencing software",
        "has_phone": false,
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "domain": "zoom.us",
        "slug": "zoom",
        "company_id": "3dziosb08w",
        "linkedin_slug": "2532259",
        "location": {
          "c": "united states",
          "rg": "california",
          "l": "san jose",
          "lc": "san jose, california, united states",
          "hq": "san jose",
          "cc": "us",
          "coord": [
            -121.89496,
            37.33939
          ],
          "g": "37.33939,-121.89496"
        },
        "founded": "2011",
        "name": "Zoom",
        "size": "5001-10000",
        "has_email": false,
        "description": "Cloud-based video conferencing software",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=zoom.us",
        "match_tier": "strict"
      },
      {
        "hq": "fort lauderdale",
        "tagline": "Provider of cloud based integrated compliance management solutions",
        "has_phone": false,
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "domain": "processmap.com",
        "slug": "processmap",
        "company_id": "inexvchr0n",
        "linkedin_slug": "processmap",
        "location": {
          "c": "united states",
          "rg": "florida",
          "l": "fort lauderdale",
          "lc": "fort lauderdale, florida, united states",
          "hq": "fort lauderdale",
          "cc": "us",
          "coord": [
            -80.14338,
            26.12231
          ],
          "g": "26.12231,-80.14338"
        },
        "founded": "2000",
        "name": "ProcessMAP",
        "size": "51-200",
        "has_email": false,
        "description": "Provider of cloud based integrated compliance management solutions",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=processmap.com",
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
          "count": 4079,
          "added": 3
        }
      ],
      "source_rows": 3,
      "excluded_candidates": 0,
      "strict_count_reported": 4079,
      "candidate_pool_count_reported": 4079,
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
    "retrieved_at": "2026-09-23T03:35:32.172354+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/12-subscription-model.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
