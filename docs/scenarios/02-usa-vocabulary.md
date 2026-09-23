# Which location value selects the United States?

[All 50 scenarios](README.md) · [Workflow guide](../guides/company-search-api.md) · [Endpoint reference](../reference/company_filter_options.md)

**POST `/v1/companies/filter-options`** · MCP tool **`company_filter_options`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 02-usa-vocabulary -->
```json
{
  "field": "locations",
  "q": "United States",
  "limit": 5
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:31.484728+00:00; HTTP **200**;
**observed**, 0.062 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

Use the returned values only in the requested filter field. Industry, sector, market and location vocabularies are distinct. The option limit bounds suggestions, not the searchable company population.

The baseline was HTTP 200, **observed**:
Response contract and declared scenario checks passed; source truth not independently certified. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 02-usa-vocabulary -->
```json
{
  "ok": true,
  "feature": "company_filter_options",
  "data": {
    "field": "locations",
    "query": "United States",
    "options": [
      "United States",
      "United States,California",
      "United,Louisiana,United States",
      "United States Air Force Academy",
      "Unity,Maine,United States"
    ],
    "returned": 5,
    "complete": false,
    "note": "Suggestions are bounded matches, not the complete company universe."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:31.484580+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/02-usa-vocabulary.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
