# Find investment advisers and deal platforms with success-fee revenue

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** Find investment advisers or capital-raising platforms that may earn a success fee when a deal closes.

**Validation status:** request schemas and known catalogue values checked locally.
The company search is an authored recipe, **not a live company-result capture**.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

**POST `/v1/companies/filter-options`** · MCP `company_filter_options`

<!-- business-request: 52-investment-advisers-success-fees-lookup -->
```json
{
  "field": "business_models",
  "q": "investment",
  "limit": 10
}
```

This business-model lookup depends on Radar's upstream vocabulary service. No fresh
options were captured for this recipe. Select a returned value; do not assume the
query text itself is a valid `business_models` value.

## Main request

**POST `/v1/companies/semantic-search`** · MCP `semantic_company_search`

<!-- business-request: 52-investment-advisers-success-fees-search -->
```json
{
  "q": "investment advisers and capital raising platforms earning a success fee when an investment deal closes",
  "filters": {
    "revenue_models": [
      "commission on transaction"
    ]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

Natural-language discovery covers the activity, while the structured revenue predicate keeps the recorded commission model explicit. Success fee is not a separate revenue_models option. Repeat the investment business-model lookup and use the returned exact value if you want a narrower business_models filter.

Set `RADAR_BASE_URL` to your operator-supplied gateway and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL/v1/companies/semantic-search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q":"investment advisers and capital raising platforms earning a success fee when an investment deal closes","filters":{"revenue_models":["commission on transaction"]},"match_mode":"strict","page":0,"limit":20}'
```

Equivalent MCP tool call:

<!-- business-mcp: 52-investment-advisers-success-fees-search -->
```json
{
  "name": "semantic_company_search",
  "arguments": {
    "request": {
      "q": "investment advisers and capital raising platforms earning a success fee when an investment deal closes",
      "filters": {
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

### Broader advisory candidates with a fee-for-service tag

**POST `/v1/companies/semantic-search`** · MCP `semantic_company_search`

<!-- business-request: 52-investment-advisers-success-fees-variant-1 -->
```json
{
  "q": "investment advisory and capital raising services with completion based fees",
  "filters": {
    "revenue_models": [
      "fee-for-service"
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

<!-- business-request: 52-investment-advisers-success-fees-columns -->
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

<!-- business-request: 52-investment-advisers-success-fees-profile -->
```json
{
  "domain": "candidate.example"
}
```

Inspect `available_fields` and `field_status` before the separate field read:

**POST `/v1/companies/field`** · MCP `get_company_field`

<!-- business-request: 52-investment-advisers-success-fees-classification -->
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
| Service | Distinguish capital raising, acquisition advice, investment execution and general financial advice. |
| Success condition | Retain the contractual event that makes the fee payable. Completion, introduction and signing are not interchangeable. |
| Retainer | Check whether an ongoing advisory retainer exists alongside the success fee; a commission label does not exclude retainers. |

Treat the fee-for-service variant as a separate candidate cohort. It is not evidence that a company charges a success fee. Keep absent evidence as unknown instead of rewriting the label.

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
