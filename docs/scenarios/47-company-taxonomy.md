# Retrieve Razorpay sectors, primary feeds and other business classifications.

[All 50 scenarios](README.md) · [Workflow guide](../guides/technology-traffic-data-api.md) · [Endpoint reference](../reference/get_company_field.md)

**POST `/v1/companies/field`** · MCP tool **`get_company_field`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 47-company-taxonomy -->
```json
{
  "domain": "razorpay.com",
  "field": "classification",
  "item_limit": 100
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.704164+00:00; HTTP **200**;
**observed**, 0.007 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

Only the requested detail field is returned. Preserve field_status, source update date, nested business structures and array coverage. Missing observations do not become zero or proof that the company lacks a technology, market or traffic source.

The baseline was HTTP 200, **observed**:
Response contract and declared scenario checks passed; source truth not independently certified. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 47-company-taxonomy -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "razorpay.com",
    "company_id": "2gowls1wmc",
    "field": "classification",
    "value": {
      "sectors": [
        "FinTech",
        "Enterprise Applications"
      ],
      "markets": [
        "Payments",
        "Banking Tech",
        "HRTech"
      ],
      "feeds": {
        "primary": [
          "Payments",
          "Banking Tech",
          "HRTech"
        ],
        "other": [
          "Business Payments Solutions",
          "Commerce Enablers",
          "Enterprise Tech - India",
          "FinTech - India",
          "Enterprise Tech - Karnataka",
          "SaaS - India",
          "SaaS",
          "Enterprise Software",
          "FinTech SaaS",
          "Cloud Banking",
          "CFO Stack",
          "Embedded Finance",
          "Y Combinator Batches",
          "Banking as a Service",
          "Open Banking",
          "Banking Tech - India",
          "Payroll Management",
          "HR SaaS"
        ]
      },
      "business_models": [
        "Business Payments",
        "Diversified",
        "Payments",
        "Gateway",
        "Accounting Solutions",
        "Procure to Pay",
        "Account Payables",
        "Invoice Processing"
      ],
      "revenue_models": [
        "subscription"
      ],
      "industries": [
        "computer software"
      ],
      "company_types": [
        "Startup"
      ],
      "flags": {
        "Tech": "YES",
        "Consumer": "NO",
        "Enterprise": "YES",
        "Marketplace": "NO",
        "SaaS": "YES",
        "Software": "YES",
        "Social Impact": "NO",
        "Blockchain": "NO",
        "Tech Hardware": "NO",
        "Artificial Intelligence": "Untagged",
        "Agentic AI": "Untagged"
      }
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "classification": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/sectors": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/markets": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/feeds/primary": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/feeds/other": {
          "available": 18,
          "returned": 18,
          "truncated": false
        },
        "/value/business_models": {
          "available": 8,
          "returned": 8,
          "truncated": false
        },
        "/value/revenue_models": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/industries": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/company_types": {
          "available": 1,
          "returned": 1,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.704022+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/47-company-taxonomy.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
