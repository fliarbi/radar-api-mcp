# Combine a software-development business model with fee-for-service revenue

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** Find companies whose own activity is software development and whose recorded revenue model is fee-for-service.

**Validation status:** request schemas and known catalogue values checked locally.
The exact main-search response is captured below, including any empty result or denial.
Additional variants are request recipes unless their captured output is shown.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

**POST `/v1/companies/filter-options`** · MCP `company_filter_options`

<!-- business-request: 60-software-services-business-model-lookup -->
```json
{
  "field": "business_models",
  "q": "software",
  "limit": 5
}
```

The [saved lookup](../examples/company_filter_options.json), captured on
2026-09-23, returned these exact values. This is historical vocabulary evidence.

<!-- business-saved-output: software-options -->
```json
{
  "field": "business_models",
  "query": "software",
  "options": [
    "software",
    "software development",
    "ecommerce software suite",
    "farm management software",
    "software developers"
  ],
  "returned": 5,
  "complete": false,
  "note": "Suggestions are bounded matches, not the complete company universe."
}
```

## Main request

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 60-software-services-business-model-search -->
```json
{
  "filters": {
    "business_models": [
      "software development"
    ],
    "revenue_models": [
      "fee-for-service"
    ]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

software development is a value in the saved business-model lookup. It describes the activity; fee-for-service describes how the business earns money. The two filters are ANDed across dimensions. Repeat the business-model lookup before using the stored label against a new source revision.

Set `RADAR_BASE_URL=https://radar-api.fliarbi.com` and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL/v1/companies/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"business_models":["software development"],"revenue_models":["fee-for-service"]},"match_mode":"strict","page":0,"limit":20}'
```

Equivalent MCP tool call:

<!-- business-mcp: 60-software-services-business-model-search -->
```json
{
  "name": "search_companies",
  "arguments": {
    "request": {
      "filters": {
        "business_models": [
          "software development"
        ],
        "revenue_models": [
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

**HTTP 403: access_required**, captured **2026-09-25T16:17:58.727396+00:00** through the authenticated
local gateway calling its configured Radar source. This is an actual response,
including empty results and denials. Retrieval time does not certify the age of
the underlying source or independently verify a company's fee contract.

The linked session was denied access. A separate diagnostic with that session
returned `login_required`; reconnect a current Radar session before retrying.
This response establishes no matching-company count. See [API-key and session help](../guides/api-keys-authentication.md).

<details open>
<summary>Complete captured search_companies response</summary>

<!-- business-live-response: 60-software-services-business-model-search -->
```json
{
  "ok": false,
  "feature": "search_companies",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-25T16:17:58.727303+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  },
  "error": {
    "kind": "access_required",
    "message": "The linked account does not have access to this data"
  }
}
```

</details>

[Download this request and full response](../examples/business-models/60-software-services-business-model-search.json). All returned fields and rows are preserved; SHA-256 fingerprints are included.

## Related request variants

### India software-development services

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 60-software-services-business-model-variant-1 -->
```json
{
  "filters": {
    "business_models": [
      "software development"
    ],
    "revenue_models": [
      "fee-for-service"
    ],
    "locations": [
      "India"
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

<!-- business-request: 60-software-services-business-model-columns -->
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

<!-- business-request: 60-software-services-business-model-profile -->
```json
{
  "domain": "candidate.example"
}
```

Inspect `available_fields` and `field_status` before the separate field read:

**POST `/v1/companies/field`** · MCP `get_company_field`

<!-- business-request: 60-software-services-business-model-classification -->
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
| Business activity | Retain the returned software-development tag and the company’s description; do not substitute an industry label for a business-model value. |
| Service billing | A fee-for-service tag does not establish hourly billing, fixed-price projects, milestone payments or a retainer. |
| Hybrid companies | Companies may also sell licensed software or subscriptions; retain all recorded revenue labels. |

Do not infer the fee model from the word software alone. This recipe uses a saved vocabulary value, not a newly executed company search.

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
