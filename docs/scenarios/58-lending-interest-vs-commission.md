# Separate interest-earning lenders from commission-based financial intermediaries

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** Find banking and financial-services companies tagged with lending or interest income, and compare them with commission-tagged intermediaries.

**Validation status:** request schemas and known catalogue values checked locally.
The exact main-search response is captured below, including any empty result or denial.
Additional variants are request recipes unless their captured output is shown.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

**POST `/v1/companies/filter-options`** · MCP `company_filter_options`

<!-- business-request: 58-lending-interest-vs-commission-lookup -->
```json
{
  "field": "revenue_models",
  "q": "interest",
  "limit": 10
}
```

The following is the actual local output of the catalogue handler. This lookup
used no company-store connection and was not an HTTP/live-company search.

<!-- business-local-output: 58-lending-interest-vs-commission-lookup -->
```json
{
  "field": "revenue_models",
  "query": "interest",
  "options": [
    "interest"
  ],
  "returned": 1,
  "complete": false,
  "note": "Suggestions are bounded matches, not the complete company universe."
}
```

## Main request

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 58-lending-interest-vs-commission-search -->
```json
{
  "filters": {
    "industries": [
      "Banking & Financial Services"
    ],
    "revenue_models": [
      "lending",
      "interest"
    ]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

The lending and interest terms are separate supported tags joined with OR. Build a second commission cohort explicitly; the two result sets can overlap and do not partition the financial-services market.

Set `RADAR_BASE_URL=https://radar-api.fliarbi.com` and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL/v1/companies/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"industries":["Banking & Financial Services"],"revenue_models":["lending","interest"]},"match_mode":"strict","page":0,"limit":20}'
```

Equivalent MCP tool call:

<!-- business-mcp: 58-lending-interest-vs-commission-search -->
```json
{
  "name": "search_companies",
  "arguments": {
    "request": {
      "filters": {
        "industries": [
          "Banking & Financial Services"
        ],
        "revenue_models": [
          "lending",
          "interest"
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

**HTTP 200: 0 returned companies**, captured **2026-09-25T16:17:58.697981+00:00** through the authenticated
local gateway calling its configured Radar source. This is an actual response,
including empty results and denials. Retrieval time does not certify the age of
the underlying source or independently verify a company's fee contract.

The source supplied **0 candidates**; strict filtering
excluded **0** on this page. An empty strict page is not proof that no such business exists.

<details open>
<summary>Complete captured search_companies response</summary>

<!-- business-live-response: 58-lending-interest-vs-commission-search -->
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
      "searches_remaining": 50
    },
    "partial_timeout": false,
    "matching": {
      "mode": "strict",
      "tiers": [
        {
          "added": 0,
          "cumulative": 0,
          "tier": "strict"
        },
        {
          "tier": "semantic"
        }
      ],
      "source_rows": 0,
      "excluded_candidates": 0,
      "strict_count_reported": 0,
      "candidate_pool_count_reported": 0,
      "count_capped": false,
      "filters_restricted": false,
      "note": "Strict means the source labelled the row strict and did not strip filters. Counts may describe an expanded candidate pool, not all matching companies. Missing tier metadata is unverified."
    },
    "next_page": null,
    "pagination": "Increment source page even when strict filtering returns no rows; next_page is a continuation hint, not a guarantee of more matches. Account caps apply."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-25T16:17:58.697821+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

</details>

[Download this request and full response](../examples/business-models/58-lending-interest-vs-commission-search.json). All returned fields and rows are preserved; SHA-256 fingerprints are included.

## Related request variants

### Commission-based financial-service candidates

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 58-lending-interest-vs-commission-variant-1 -->
```json
{
  "filters": {
    "industries": [
      "Banking & Financial Services"
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

<!-- business-request: 58-lending-interest-vs-commission-columns -->
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

<!-- business-request: 58-lending-interest-vs-commission-profile -->
```json
{
  "domain": "candidate.example"
}
```

Inspect `available_fields` and `field_status` before the separate field read:

**POST `/v1/companies/field`** · MCP `get_company_field`

<!-- business-request: 58-lending-interest-vs-commission-classification -->
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
| Capital versus intermediation | Distinguish a lender deploying capital from a broker or platform arranging a loan. |
| Interest versus fees | Record interest, origination fees, referral commissions and software fees separately. |
| Financial denominator | A loan book, assets under management or capital raised is not sales revenue or earned interest. |

Do not describe lending or interest tags as an APR, interest-rate quote, profitability measure or regulatory permission.

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
