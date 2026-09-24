# Find internship-type records from Shine using the public internship alias.

[All 50 scenarios](README.md) · [Workflow guide](../guides/hiring-signals-jobs-api.md) · [Endpoint reference](../reference/search_jobs.md)

**POST `/v1/jobs/search`** · MCP tool **`search_jobs`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Coverage or failure example — no populated requested result.** 0 jobs; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 38-normalized-interns -->
```json
{
  "title": "intern",
  "employment_type": "internship",
  "sources": [
    "shine"
  ],
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.698841+00:00; HTTP **200**;
**qualified**, 0.248 seconds.
Local authenticated gateway with live configured read-only sources.

Empty documentation example: 0 jobs; totals and context do not substitute for requested rows; No rows observed; not proof of a complete negative.

Job listings are observed recruitment records. Preserve role, location, skills, source dates and absent salary/domain values. Employment-type aliases are normalized by the gateway. An advertised vacancy does not prove a hire or a currently open position.

**Empty coverage case.** The normalized job source returned no rows for this exact Shine/internship filter. A broader internship-type job query was also empty on 2026-09-24. Use the separate [internship corpus example](41-remote-part-time-interns.md) for populated internship records; that source has a different contract and does not establish that Shine contains matching rows.

The baseline was HTTP 200, **qualified**:
Empty documentation example: 0 jobs; totals and context do not substitute for requested rows; No rows observed; not proof of a complete negative. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 38-normalized-interns -->
```json
{
  "ok": true,
  "feature": "search_jobs",
  "data": {
    "jobs": [],
    "total_estimate": 0,
    "total_capped": false,
    "page": 0,
    "page_size": 3,
    "access": {
      "plan": "free",
      "results_per_query": 15,
      "searches_per_month": 50,
      "anonymous": true
    },
    "plan": "free",
    "partial_timeout": false
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.698726+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/38-normalized-interns.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
