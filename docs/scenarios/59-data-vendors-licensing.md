# Find B2B data vendors with data-sales or licensing revenue

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** Find data and market-research businesses whose source labels include selling data or licensing.

**Validation status:** request schemas and known catalogue values checked locally.
The company search is an authored recipe, **not a live company-result capture**.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

**POST `/v1/companies/filter-options`** · MCP `company_filter_options`

<!-- business-request: 59-data-vendors-licensing-lookup -->
```json
{
  "field": "revenue_models",
  "q": "licensing",
  "limit": 10
}
```

The following is the actual local output of the catalogue handler. This lookup
used no company-store connection and was not an HTTP/live-company search.

<!-- business-local-output: 59-data-vendors-licensing-lookup -->
```json
{
  "field": "revenue_models",
  "query": "licensing",
  "options": [
    "licensing"
  ],
  "returned": 1,
  "complete": false,
  "note": "Suggestions are bounded matches, not the complete company universe."
}
```

## Main request

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 59-data-vendors-licensing-search -->
```json
{
  "filters": {
    "industries": [
      "Big Data",
      "Data Analytics",
      "Market Research"
    ],
    "revenue_models": [
      "selling data",
      "licensing"
    ]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

Industry values are ORed within the industry field, and revenue-model values are ORed within their field; the two dimensions are intersected. Inspect products and customer focus before describing a candidate as a B2B company-data or financial-data vendor.

Set `RADAR_BASE_URL` to your operator-supplied gateway and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL/v1/companies/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"industries":["Big Data","Data Analytics","Market Research"],"revenue_models":["selling data","licensing"]},"match_mode":"strict","page":0,"limit":20}'
```

Equivalent MCP tool call:

<!-- business-mcp: 59-data-vendors-licensing-search -->
```json
{
  "name": "search_companies",
  "arguments": {
    "request": {
      "filters": {
        "industries": [
          "Big Data",
          "Data Analytics",
          "Market Research"
        ],
        "revenue_models": [
          "selling data",
          "licensing"
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

### Data-sales classification only

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 59-data-vendors-licensing-variant-1 -->
```json
{
  "filters": {
    "industries": [
      "Big Data",
      "Data Analytics",
      "Market Research"
    ],
    "revenue_models": [
      "selling data"
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

<!-- business-request: 59-data-vendors-licensing-columns -->
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

<!-- business-request: 59-data-vendors-licensing-profile -->
```json
{
  "domain": "candidate.example"
}
```

Inspect `available_fields` and `field_status` before the separate field read:

**POST `/v1/companies/field`** · MCP `get_company_field`

<!-- business-request: 59-data-vendors-licensing-classification -->
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
| Product | Distinguish datasets, data feeds, API access, software licensing and consulting reports. |
| Customer and billing unit | Retain evidence for business buyers and whether pricing is per seat, API call, record, dataset or contract. |
| License meaning | A licensing label does not establish redistribution rights, data ownership or a specific contract term. |

B2B and pay-per-use are not revenue_models options in the current catalogue. Verify customer segment and the billing unit from the returned business evidence.

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
