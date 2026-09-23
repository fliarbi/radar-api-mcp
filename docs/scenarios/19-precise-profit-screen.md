# Check whether Microsoft has positive annual profit and revenue above USD 1B in its latest accessible year.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/screen_company_financials.md)

**POST `/v1/companies/financials/screen`** · MCP tool **`screen_company_financials`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 19-precise-profit-screen -->
```json
{
  "domains": [
    "microsoft.com"
  ],
  "constraints": [
    {
      "metric": "net_income",
      "gt": 0
    },
    {
      "metric": "revenue",
      "gte": 1000000000
    }
  ],
  "period_type": "annual"
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.185025+00:00; HTTP **200**;
**qualified**, 0.006 seconds.
Local authenticated gateway with live configured read-only sources.

Partial result or source timeout; Coverage is explicitly bounded; No rows observed; not proof of a complete negative.

Read all evaluated rows, not just matches. Numeric conditions use the same latest accessible fiscal period. Unknown means missing or disallowed evidence; unavailable means a failed read. Neither becomes zero. This is a bounded candidate screen with source gates, not an exhaustive company database query. Its per-metric checks preserve currency, source type and inclusive/exclusive bounds.

The baseline was an unavailable operation registry check (no HTTP request), **unavailable**:
not_implemented. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 19-precise-profit-screen -->
```json
{
  "ok": true,
  "feature": "screen_company_financials",
  "data": {
    "matches": [],
    "evaluated": [
      {
        "domain": "microsoft.com",
        "company": {
          "domain": "microsoft.com"
        },
        "status": "unknown",
        "reason": "No accessible period matches the requested type/year window",
        "period": null,
        "checks": [],
        "access_limited": true,
        "successful_read": true
      }
    ],
    "counts": {
      "unknown": 1
    },
    "constraints": [
      {
        "metric": "net_income",
        "gt": 0.0
      },
      {
        "metric": "revenue",
        "gte": 1000000000.0
      }
    ],
    "period_type": "annual",
    "source_type": "any",
    "discovery": null,
    "next_page": null,
    "coverage": {
      "complete": false,
      "partial": true,
      "candidate_count": 1,
      "company_filters_independently_verified": false,
      "note": "Numeric matches are verified against returned dated metrics. Candidate company classification/geography remains source-filtered; inspect source access and matching. Empty matches do not mean there are no matching companies elsewhere."
    },
    "successful_financial_reads": 1
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:32.184908+00:00",
    "partial": true,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/19-precise-profit-screen.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
