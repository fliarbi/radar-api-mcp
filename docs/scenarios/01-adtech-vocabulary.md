# Which industry value selects AdTech companies?

[All 50 scenarios](README.md) · [Workflow guide](../guides/company-search-api.md) · [Endpoint reference](../reference/company_filter_options.md)

**POST `/v1/companies/filter-options`** · MCP tool **`company_filter_options`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 1 options; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 01-adtech-vocabulary -->
```json
{
  "field": "industries",
  "q": "AdTech",
  "limit": 5
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:31.422022+00:00; HTTP **200**;
**observed**, 0.001 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

Use the returned values only in the requested filter field. Industry, sector, market and location vocabularies are distinct. The option limit bounds suggestions, not the searchable company population.

The baseline was HTTP 200, **failed**:
AdTech is a valid source industry but suggestion lookup did not return it. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 01-adtech-vocabulary -->
```json
{
  "ok": true,
  "feature": "company_filter_options",
  "data": {
    "field": "industries",
    "query": "AdTech",
    "options": [
      "AdTech"
    ],
    "returned": 1,
    "complete": false,
    "note": "Suggestions are bounded matches, not the complete company universe."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:31.421727+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/01-adtech-vocabulary.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
