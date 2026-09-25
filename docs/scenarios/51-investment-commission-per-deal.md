# Find investment companies whose revenue model is commission per deal

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** Find investment-service companies classified with transaction commissions, then check whether their fee is charged on each completed investment deal.

**Validation status:** request schemas and known catalogue values checked locally.
The company search is an authored recipe, **not a live company-result capture**.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

**POST `/v1/companies/filter-options`** · MCP `company_filter_options`

<!-- business-request: 51-investment-commission-per-deal-lookup -->
```json
{
  "field": "revenue_models",
  "q": "commission",
  "limit": 10
}
```

The following is the actual local output of the catalogue handler. This lookup
used no company-store connection and was not an HTTP/live-company search.

<!-- business-local-output: 51-investment-commission-per-deal-lookup -->
```json
{
  "field": "revenue_models",
  "query": "commission",
  "options": [
    "commission on transaction"
  ],
  "returned": 1,
  "complete": false,
  "note": "Suggestions are bounded matches, not the complete company universe."
}
```

## Main request

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 51-investment-commission-per-deal-search -->
```json
{
  "filters": {
    "industries": [
      "Investment Management & Fund Operators"
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

This intersects the Investment Management & Fund Operators industry with Radar’s exact commission on transaction revenue-model label. It discovers source-classified candidates; the label alone does not establish who pays, the commission rate, the minimum fee, or whether a completed deal triggers payment.

Set `RADAR_BASE_URL` to your operator-supplied gateway and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL/v1/companies/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"industries":["Investment Management & Fund Operators"],"revenue_models":["commission on transaction"]},"match_mode":"strict","page":0,"limit":20}'
```

Equivalent MCP tool call:

<!-- business-mcp: 51-investment-commission-per-deal-search -->
```json
{
  "name": "search_companies",
  "arguments": {
    "request": {
      "filters": {
        "industries": [
          "Investment Management & Fund Operators"
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

### Limit recorded company location to the United States

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 51-investment-commission-per-deal-variant-1 -->
```json
{
  "filters": {
    "industries": [
      "Investment Management & Fund Operators"
    ],
    "revenue_models": [
      "commission on transaction"
    ],
    "locations": [
      "United States"
    ]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

### Explore broker and deal-adviser wording across industries

**POST `/v1/companies/semantic-search`** · MCP `semantic_company_search`

<!-- business-request: 51-investment-commission-per-deal-variant-2 -->
```json
{
  "q": "investment brokers and advisers arranging investment deals and charging a commission per completed deal",
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

### Investor-classified entities with a commission tag

**POST `/v1/investors/search`** · MCP `search_investors`

<!-- business-request: 51-investment-commission-per-deal-variant-3 -->
```json
{
  "filters": {
    "revenue_models": [
      "commission on transaction"
    ]
  },
  "match_mode": "expanded",
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

<!-- business-request: 51-investment-commission-per-deal-columns -->
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

<!-- business-request: 51-investment-commission-per-deal-profile -->
```json
{
  "domain": "candidate.example"
}
```

Inspect `available_fields` and `field_status` before the separate field read:

**POST `/v1/companies/field`** · MCP `get_company_field`

<!-- business-request: 51-investment-commission-per-deal-classification -->
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
| Company activity | Inspect the description and business_models for investment services, investment platforms, advisory or transaction intermediation. An asset manager and a deal broker are different businesses. |
| Billing event | Look for dated pricing or terms saying the fee is triggered by a completed deal, investment placement or executed transaction. A generic commission label leaves the billing event unknown. |
| Fee basis | Retain whether the fee is a percentage of deal value or a fixed transaction amount. Record a percentage only when evidence supplies it. |
| Other income | Keep subscriptions, management fees, carried interest and interest income separate. Do not translate any of them automatically to commission per deal. |

The investor-entity variant explicitly uses expanded mode and retains unverified candidates for review. Do not replace the company request with search_investors plus business_models: investor-mode business-model filters can describe the portfolio, not the firm's own activity. Fundraising deal_sizes are financing bands, not commission rates or service fees.

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
