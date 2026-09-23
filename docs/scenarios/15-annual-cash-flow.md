# Retrieve Microsoft annual operating cash flow, capex and free cash flow.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/get_financials.md)

**POST `/v1/companies/financials`** · MCP tool **`get_financials`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 15-annual-cash-flow -->
```json
{
  "domain": "microsoft.com",
  "statement": "cash_flow",
  "period_type": "annual",
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.004380+00:00; HTTP **200**;
**qualified**, 0.028 seconds.
Local authenticated gateway with live configured read-only sources.

Financial history is source-plan limited; No rows observed; not proof of a complete negative; No accessible data.

Preserve fiscal year, fiscal period, statement family, source type and available dates. Empty annual rows with access_limited do not prove the archive has no annual statements. No annual values are synthesized by adding quarters, and a filing date is not substituted for an absent period end.

The baseline was HTTP 200, **qualified**:
Financial history is source-plan limited; No rows observed; not proof of a complete negative; No accessible data. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 15-annual-cash-flow -->
```json
{
  "ok": true,
  "feature": "get_financials",
  "data": {
    "domain": "microsoft.com",
    "statement": "cash_flow",
    "has_data": false,
    "periods": [],
    "returned": 0,
    "truncated": false,
    "access_limited": true,
    "available_period_count": 20,
    "computed_at": "2026-09-23T03:22:51.284000Z",
    "summary": {
      "narrative": "Latest reported Q3 FY2026: revenue $82.89B, net income $31.8B, EPS $4.27. YoY +34.0% (1.34× prior period). Growth has been erratic across reported periods. Recent signals: Raised guidance, Beat estimates, Profitable."
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:32.003750+00:00",
    "partial": false,
    "notes": [
      "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
      "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies.",
      "The linked Radar account exposes only part of the financial archive."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/15-annual-cash-flow.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
