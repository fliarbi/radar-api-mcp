# Find real estate companies earning commission on property deals

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** Find real estate brokerage candidates whose recorded revenue model includes transaction commissions.

**Validation status:** request schemas and known catalogue values checked locally.
The company search is an authored recipe, **not a live company-result capture**.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

**POST `/v1/companies/filter-options`** · MCP `company_filter_options`

<!-- business-request: 53-real-estate-brokerage-commission-lookup -->
```json
{
  "field": "industries",
  "q": "Real Estate",
  "limit": 10
}
```

The following is the actual local output of the catalogue handler. This lookup
used no company-store connection and was not an HTTP/live-company search.

<!-- business-local-output: 53-real-estate-brokerage-commission-lookup -->
```json
{
  "field": "industries",
  "query": "Real Estate",
  "options": [
    "Real Estate & Property Management"
  ],
  "returned": 1,
  "complete": false,
  "note": "Suggestions are bounded matches, not the complete company universe."
}
```

## Main request

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 53-real-estate-brokerage-commission-search -->
```json
{
  "filters": {
    "industries": [
      "Real Estate & Property Management"
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

The industry is broader than brokerage: it can include property management, rental platforms and other property services. Inspect each company’s own activity before describing the result as a list of property brokers.

Set `RADAR_BASE_URL` to your operator-supplied gateway and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL/v1/companies/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"industries":["Real Estate & Property Management"],"revenue_models":["commission on transaction"]},"match_mode":"strict","page":0,"limit":20}'
```

Equivalent MCP tool call:

<!-- business-mcp: 53-real-estate-brokerage-commission-search -->
```json
{
  "name": "search_companies",
  "arguments": {
    "request": {
      "filters": {
        "industries": [
          "Real Estate & Property Management"
        ],
        "revenue_models": [
          "commission on transaction"
        ]
      },
      "match_mode": "strict",
      "page": 0,
      "limit": 20
    }
  }
}
```

## Related request variants

### India property-commission candidates

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 53-real-estate-brokerage-commission-variant-1 -->
```json
{
  "filters": {
    "industries": [
      "Real Estate & Property Management"
    ],
    "revenue_models": [
      "commission on transaction"
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

<!-- business-request: 53-real-estate-brokerage-commission-columns -->
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

<!-- business-request: 53-real-estate-brokerage-commission-profile -->
```json
{
  "domain": "candidate.example"
}
```

Inspect `available_fields` and `field_status` before the separate field read:

**POST `/v1/companies/field`** · MCP `get_company_field`

<!-- business-request: 53-real-estate-brokerage-commission-classification -->
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
| Property activity | Separate sales brokerage, rental brokerage, property management and listing portals. |
| Transaction and payer | Retain whether a seller, buyer, landlord or tenant pays and whether the fee follows a sale, lease or introduction. |
| Alternative models | Advertising, subscriptions and renting / leasing are different labels; do not silently treat them as commission. |

The location filter describes recorded company geography, not the location of every property it handles. A property price or transaction value is not the company’s commission revenue.

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
