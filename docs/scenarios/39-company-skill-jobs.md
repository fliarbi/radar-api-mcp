# Find Connvertex job listings with Python in the role title.

[All 50 scenarios](README.md) · [Workflow guide](../guides/hiring-signals-jobs-api.md) · [Endpoint reference](../reference/search_jobs.md)

**POST `/v1/jobs/search`** · MCP tool **`search_jobs`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 2 jobs; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 39-company-skill-jobs -->
```json
{
  "company": "Connvertex",
  "title": "Python",
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-24T07:00:50.413961+00:00; HTTP **200**;
**observed**, 0.034 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

Job listings are observed recruitment records. Preserve role, location, skills, source dates and absent salary/domain values. Employment-type aliases are normalized by the gateway. An advertised vacancy does not prove a hire or a currently open position.

This sample searches Connvertex and a Python role title. Its source skills array can be empty: a title match is not evidence that a structured skills filter matched. The original Microsoft/skills request remains in the baseline below; the stable scenario URL is retained for existing links.

The baseline was HTTP 200, **qualified**:
Empty documentation example: 0 jobs; totals and context do not substitute for requested rows; No rows observed; not proof of a complete negative. This is an explicit sample replacement, not a before/after repair of an identical request. The original question was: Find Microsoft job listings mentioning Python skills.

Original baseline request:
```json
{
  "company": "Microsoft",
  "skills": [
    "Python"
  ],
  "limit": 3
}
```
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 39-company-skill-jobs -->
```json
{
  "ok": true,
  "feature": "search_jobs",
  "data": {
    "jobs": [
      {
        "id": "talent:636510706419959364",
        "title": "Python Developer",
        "company": "Connvertex Technologies Inc.",
        "company_domain": null,
        "logo": null,
        "locations": [
          "Nashville, Tennessee, US"
        ],
        "remote": false,
        "salary": {
          "min": null,
          "max": null,
          "currency": null
        },
        "experience": null,
        "skills": [],
        "posted": "2026-09-09",
        "url": "https://www.talent.com/view?id=636510706419959364",
        "direct_apply": false,
        "source": "talent"
      },
      {
        "id": "talent:633229694522230473",
        "title": "Python/PySpark Developer",
        "company": "Connvertex Technologies Inc.",
        "company_domain": null,
        "logo": null,
        "locations": [
          "Des Moines, Iowa, US"
        ],
        "remote": false,
        "salary": {
          "min": null,
          "max": null,
          "currency": null
        },
        "experience": null,
        "skills": [],
        "posted": "2026-08-19",
        "url": "https://www.talent.com/view?id=633229694522230473",
        "direct_apply": false,
        "source": "talent"
      }
    ],
    "total_estimate": 2,
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
    "retrieved_at": "2026-09-24T07:00:50.413805+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/39-company-skill-jobs.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
