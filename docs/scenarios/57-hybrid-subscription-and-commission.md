# Find companies with both subscription and transaction-commission models

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** Build a candidate set for businesses combining recurring subscriptions and transaction commissions, then require both recorded tags.

**Validation status:** request schemas and known catalogue values checked locally.
The company search is an authored recipe, **not a live company-result capture**.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

**POST `/v1/companies/filter-options`** · MCP `company_filter_options`

<!-- business-request: 57-hybrid-subscription-and-commission-lookup -->
```json
{
  "field": "revenue_models",
  "q": "subscription",
  "limit": 10
}
```

The following is the actual local output of the catalogue handler. This lookup
used no company-store connection and was not an HTTP/live-company search.

<!-- business-local-output: 57-hybrid-subscription-and-commission-lookup -->
```json
{
  "field": "revenue_models",
  "query": "subscription",
  "options": [
    "subscription"
  ],
  "returned": 1,
  "complete": false,
  "note": "Suggestions are bounded matches, not the complete company universe."
}
```

## Main request

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 57-hybrid-subscription-and-commission-search -->
```json
{
  "filters": {
    "revenue_models": [
      "subscription",
      "commission on transaction"
    ]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

Two values in revenue_models generally mean OR, not AND. The request finds candidates with either label. Read each candidate’s classification and perform a client-side all-of check before labeling a row as a recorded hybrid model.

Set `RADAR_BASE_URL` to your operator-supplied gateway and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL/v1/companies/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"filters":{"revenue_models":["subscription","commission on transaction"]},"match_mode":"strict","page":0,"limit":20}'
```

Equivalent MCP tool call:

<!-- business-mcp: 57-hybrid-subscription-and-commission-search -->
```json
{
  "name": "search_companies",
  "arguments": {
    "request": {
      "filters": {
        "revenue_models": [
          "subscription",
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

### Narrow the OR candidate pool to online marketplaces

**POST `/v1/companies/search`** · MCP `search_companies`

<!-- business-request: 57-hybrid-subscription-and-commission-variant-1 -->
```json
{
  "filters": {
    "industries": [
      "Online Marketplaces"
    ],
    "revenue_models": [
      "subscription",
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

<!-- business-request: 57-hybrid-subscription-and-commission-columns -->
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

<!-- business-request: 57-hybrid-subscription-and-commission-profile -->
```json
{
  "domain": "candidate.example"
}
```

Inspect `available_fields` and `field_status` before the separate field read:

**POST `/v1/companies/field`** · MCP `get_company_field`

<!-- business-request: 57-hybrid-subscription-and-commission-classification -->
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
| Both tags | Require subscription and commission on transaction in the same company classification. A search match alone cannot satisfy the all-of condition. |
| Missing classification | Keep unavailable, truncated or incomplete classifications unresolved. Absence from a bounded array does not prove the tag is absent. |
| Economic importance | Having two labels says nothing about their revenue shares, active plans or current prices. |

The separate classification store and the search index can disagree or have different dates. Retain that discrepancy; do not overwrite one source with the other.

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

## Saved evidence: a marketplace flag is not a commission tag

This is a selected-field projection from the [complete saved Swiggy classification](../examples/fields/swiggy.com-classification.json),
captured 2026-09-23. It is not a response to this new search.

<!-- business-saved-output: swiggy-models -->
```json
{
  "domain": "swiggy.com",
  "updated_at": "2026-06-01T04:43:22.775000+00:00",
  "revenue_models": [
    "e-commerce - service",
    "subscription"
  ],
  "marketplace_flag": "YES",
  "revenue_models_coverage": {
    "available": 2,
    "returned": 2,
    "truncated": false
  }
}
```

The snapshot includes a Marketplace flag and subscription/e-commerce service tags,
but no `commission on transaction` label. It therefore does not support a
subscription-plus-commission tag match. It also does not prove what Swiggy’s actual
commercial contracts charge. Do not fill the missing label from brand familiarity.

## Require both tags in the client

The API request above is an OR search. Given a saved or newly returned
`get_company_field` response, this client-side check retains an explicit unknown
state when coverage is unavailable. It evaluates the observed snapshot only.

```python
required = {"subscription", "commission on transaction"}
data = response.get("data") or {}
coverage = data.get("coverage") or {}
array = (coverage.get("arrays") or {}).get("/value/revenue_models") or {}
models = (data.get("value") or {}).get("revenue_models")
if (not response.get("ok") or data.get("status") != "available"
        or (response.get("meta") or {}).get("partial")
        or coverage.get("partial") is not False or array.get("truncated") is not False
        or not isinstance(models, list) or not all(isinstance(v, str) for v in models)
        or array.get("returned") != len(models) or array.get("available") != len(models)):
    review = "unknown"
else:
    observed = {v.casefold() for v in models}
    review = "both tags observed" if required <= observed else "not both tags in this snapshot"
```

The saved Swiggy example evaluates to `not both tags in this snapshot`. A missing
classification must evaluate to `unknown`. A future pricing check is a separate
review outcome; do not label the catalogue test as fee verification.
