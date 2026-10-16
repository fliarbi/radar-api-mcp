# Compare available revenue and funding display columns for Razorpay and Stripe.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/get_company_columns.md)

**POST `/v1/companies/columns`** · MCP tool **`get_company_columns`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** Response content present.

## Exact executed request

<!-- scenario-request: 18-finance-columns -->
```json
{
  "domains": [
    "razorpay.com",
    "stripe.com"
  ],
  "columns": [
    "latest_revenue",
    "total_funding",
    "employees"
  ]
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.195423+00:00; HTTP **200**;
**observed**, 0.021 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

Columns contain formatted display values. Empty display values do not establish zero; source formatting can suppress zero or negative numbers. For exact financial comparisons use dated numeric financials.

The baseline was HTTP 200, **observed**:
Response contract and declared scenario checks passed; source truth not independently certified. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 18-finance-columns -->
```json
{
  "ok": true,
  "feature": "get_company_columns",
  "data": {
    "companies": [
      {
        "domain": "razorpay.com",
        "columns": {
          "latest_revenue": {
            "label": "Revenue",
            "value": "$465.1M"
          },
          "total_funding": null,
          "employees": null
        },
        "status": "available"
      },
      {
        "domain": "stripe.com",
        "columns": {
          "latest_revenue": null,
          "total_funding": null,
          "employees": null
        },
        "status": "unknown"
      }
    ],
    "note": "Radar display values only. Missing values may be suppressed zero/negative values or source failure; use get_financials for precise values and provenance."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:32.195320+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/18-finance-columns.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
