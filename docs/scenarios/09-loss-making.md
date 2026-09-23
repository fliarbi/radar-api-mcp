# Find Indian payments companies with recorded net losses.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/search_companies.md)

**POST `/v1/companies/search`** · MCP tool **`search_companies`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 09-loss-making -->
```json
{
  "filters": {
    "markets": [
      "Payments"
    ],
    "locations": [
      "India"
    ],
    "profitability": [
      "loss"
    ]
  },
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:31.817179+00:00; HTTP **200**;
**qualified**, 0.07 seconds.
Local authenticated gateway with live configured read-only sources.

Source-labelled predicates; cards do not independently verify financial/classification conditions.

Read each match_tier and the matching/excluded_candidates count before accepting the shortlist. Strict is the source's label, not an independent verification of every company attribute. Financial bands refer to source summary fields, not a selected fiscal year; retrieve financial evidence separately. Advance source pages even if strict filtering leaves an empty page with a continuation hint.

The baseline was HTTP 200, **qualified**:
Source-labelled predicates; cards do not independently verify financial/classification conditions. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 09-loss-making -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
    "companies": [
      {
        "hq": "guwahati",
        "tagline": "Provider of personal line of credits for consumers",
        "has_phone": false,
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "domain": "sliceit.com",
        "slug": "slice",
        "company_id": "29izb4bkra",
        "linkedin_slug": "slicepayy",
        "location": {
          "c": "india",
          "rg": "assam",
          "l": "guwahati",
          "lc": "guwahati, assam, india",
          "hq": "guwahati",
          "cc": "in",
          "coord": [
            91.7458,
            26.1844
          ],
          "g": "26.1844,91.7458"
        },
        "founded": "2015",
        "name": "slice",
        "size": "51-200",
        "has_email": false,
        "description": "Provider of personal line of credits for consumers",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=sliceit.com",
        "match_tier": "strict"
      },
      {
        "hq": "mumbai",
        "tagline": "Provider of mobile-based prepaid payment instruments and voucher services",
        "has_phone": false,
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "domain": "zipcash.in",
        "slug": "zipcash",
        "company_id": "2pr2w41fo2",
        "linkedin_slug": "zipcash-card-services-pvt-ltd-",
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
        "founded": "2007",
        "name": "Zipcash",
        "size": "51-200",
        "has_email": false,
        "description": "Provider of mobile-based prepaid payment instruments and voucher services",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=zipcash.in",
        "match_tier": "strict"
      },
      {
        "hq": "bengaluru",
        "tagline": "Providing escrow payment solutions for buyers and sellers",
        "has_phone": false,
        "flags": [
          [
            "Tiny Enterprise",
            "size"
          ]
        ],
        "domain": "neutron.money",
        "slug": "neutron",
        "company_id": "oghk6chbl2",
        "linkedin_slug": "neutronmoney",
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
        "founded": "2021",
        "name": "Neutron",
        "size": "1-10",
        "has_email": false,
        "description": "Providing escrow payment solutions for buyers and sellers",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=neutron.money",
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
          "count": 60,
          "added": 3
        }
      ],
      "source_rows": 3,
      "excluded_candidates": 0,
      "strict_count_reported": 60,
      "candidate_pool_count_reported": 60,
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
    "retrieved_at": "2026-09-23T03:35:31.817003+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/09-loss-making.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
