# Find recruitment agencies earning placement or success fees

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** Find recruitment firms classified with transaction commission or fee-for-service revenue, then distinguish placement fees from subscriptions.

**Validation status:** request schemas and known catalogue values checked locally.
The exact main-search response is captured below, including any empty result or denial.
Additional variants are request recipes unless their captured output is shown.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

**POST `/v1/companies/filter-options`** · MCP `company_filter_options`

<!-- business-request: 55-recruitment-placement-fees-lookup -->
```json
{
  "field": "industries",
  "q": "Recruitment",
  "limit": 10
}
```

The following is the actual local output of the catalogue handler. This lookup
used no company-store connection and was not an HTTP/live-company search.

<!-- business-local-output: 55-recruitment-placement-fees-lookup -->
```json
{
  "field": "industries",
  "query": "Recruitment",
  "options": [
    "Recruitment Jobs"
  ],
  "returned": 1,
  "complete": false,
  "note": "Suggestions are bounded matches, not the complete company universe."
}
```

## Main request

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 55-recruitment-placement-fees-search -->
```json
{
  "filters": {
    "industries": [
      "Recruitment Jobs"
    ],
    "revenue_models": [
      "commission on transaction",
      "fee-for-service"
    ]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

The two revenue-model values are OR candidates: a company may have either tag. The industry may contain job boards, recruitment software and staffing firms as well as placement agencies.

Set `RADAR_BASE_URL=https://radar-api.fliarbi.com` and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL/v1/companies/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"industries":["Recruitment Jobs"],"revenue_models":["commission on transaction","fee-for-service"]},"match_mode":"strict","page":0,"limit":20}'
```

Equivalent MCP tool call:

<!-- business-mcp: 55-recruitment-placement-fees-search -->
```json
{
  "name": "search_companies",
  "arguments": {
    "request": {
      "filters": {
        "industries": [
          "Recruitment Jobs"
        ],
        "revenue_models": [
          "commission on transaction",
          "fee-for-service"
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

**HTTP 200: 0 returned companies**, captured **2026-09-25T16:18:05.170589+00:00** through the authenticated
local gateway calling its configured Radar source. This is an actual response,
including empty results and denials. Retrieval time does not certify the age of
the underlying source or independently verify a company's fee contract.

The source supplied **20 candidates**; strict filtering
excluded **20** on this page. `next_page=1` remains available. An empty strict page is not proof that no such business exists.

<details open>
<summary>Complete captured search_companies response</summary>

<!-- business-live-response: 55-recruitment-placement-fees-search -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
    "companies": [],
    "page": 0,
    "requested_limit": 20,
    "returned": 0,
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
          "added": 0,
          "cumulative": 0
        },
        {
          "tier": "semantic",
          "added": 35,
          "cumulative": 35
        }
      ],
      "source_rows": 20,
      "excluded_candidates": 20,
      "strict_count_reported": 0,
      "candidate_pool_count_reported": 35,
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
    "retrieved_at": "2026-09-25T16:18:05.170401+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

</details>

[Download this request and full response](../examples/business-models/55-recruitment-placement-fees-search.json). All returned fields and rows are preserved; SHA-256 fingerprints are included.

## Related request variants

### Commission-tagged recruitment only

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 55-recruitment-placement-fees-variant-1 -->
```json
{
  "filters": {
    "industries": [
      "Recruitment Jobs"
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

<!-- business-request: 55-recruitment-placement-fees-columns -->
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

<!-- business-request: 55-recruitment-placement-fees-profile -->
```json
{
  "domain": "candidate.example"
}
```

Inspect `available_fields` and `field_status` before the separate field read:

**POST `/v1/companies/field`** · MCP `get_company_field`

<!-- business-request: 55-recruitment-placement-fees-classification -->
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
| Recruitment model | Separate contingency placement, retained search, staffing markup, job advertising and software subscriptions. |
| Fee trigger | Check whether billing happens on placement, start date, a retained milestone or hours worked. |
| Fee unit | Keep salary percentage, fixed placement fee and hourly markup as different units; the API has no placement-fee percentage filter. |

A hiring company is not automatically a recruitment agency. The existence of job listings does not establish the company’s revenue model.

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
