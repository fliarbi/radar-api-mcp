# Retrieve the USD software-engineer salary benchmark for the US with sample size.

[All 50 scenarios](README.md) · [Workflow guide](../guides/hiring-signals-jobs-api.md) · [Endpoint reference](../reference/salary_benchmark.md)

**POST `/v1/jobs/salary-benchmark`** · MCP tool **`salary_benchmark`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 40-salary-benchmark -->
```json
{
  "title": "software engineer",
  "country": "US",
  "currency": "USD"
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.599059+00:00; HTTP **200**;
**observed**, 0.057 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

Read count, sparse, currency and filter_echo alongside the distribution. The source aggregates salary midpoints. Do not invent a monthly or annual pay period that the response does not supply.

The captured source distribution has 206 observations and a USD 124,000 median. Its absence of an explicit pay period prevents claiming that number is an annual salary solely from this response.

The baseline was HTTP 200, **observed**:
Response contract and declared scenario checks passed; source truth not independently certified. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 40-salary-benchmark -->
```json
{
  "ok": true,
  "feature": "salary_benchmark",
  "data": {
    "count": 206,
    "currency": "USD",
    "filter_echo": {
      "city": null,
      "country": "US",
      "currency": "USD",
      "skills": null,
      "title": "software engineer"
    },
    "max": 226000,
    "median": 124000,
    "min": 20800,
    "p25": 99025,
    "p75": 150000,
    "sparse": false
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.598929+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/40-salary-benchmark.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
