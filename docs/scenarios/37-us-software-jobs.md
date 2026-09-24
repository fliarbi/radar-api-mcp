# Find observed US software engineer job postings.

[All 50 scenarios](README.md) · [Workflow guide](../guides/hiring-signals-jobs-api.md) · [Endpoint reference](../reference/search_jobs.md)

**POST `/v1/jobs/search`** · MCP tool **`search_jobs`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 jobs; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 37-us-software-jobs -->
```json
{
  "title": "software engineer",
  "country": "US",
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.447065+00:00; HTTP **200**;
**observed**, 0.396 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

Job listings are observed recruitment records. Preserve role, location, skills, source dates and absent salary/domain values. Employment-type aliases are normalized by the gateway. An advertised vacancy does not prove a hire or a currently open position.

The baseline was HTTP 200, **observed**:
Response contract and declared scenario checks passed; source truth not independently certified. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 37-us-software-jobs -->
```json
{
  "ok": true,
  "feature": "search_jobs",
  "data": {
    "jobs": [
      {
        "id": "talent:636631531523081796",
        "title": "Software Engineer Controls",
        "company": "Optimal Inc.",
        "company_domain": null,
        "logo": null,
        "locations": [
          "Sunrise, Florida, US"
        ],
        "remote": false,
        "salary": {
          "min": null,
          "max": null,
          "currency": null
        },
        "experience": null,
        "skills": [],
        "posted": "2026-09-11",
        "url": "https://www.talent.com/view?id=636631531523081796",
        "direct_apply": false,
        "source": "talent"
      },
      {
        "id": "talent:636864770441742421",
        "title": "Software Engineer (Colorado)",
        "company": "Kestrel Intelligence",
        "company_domain": null,
        "logo": null,
        "locations": [
          "Colorado Springs, Colorado, US"
        ],
        "remote": false,
        "salary": {
          "min": null,
          "max": null,
          "currency": null
        },
        "experience": null,
        "skills": [],
        "posted": "2026-09-11",
        "url": "https://www.talent.com/view?id=636864770441742421",
        "direct_apply": false,
        "source": "talent"
      },
      {
        "id": "talent:636478413375605243",
        "title": "Software Engineer - Backend",
        "company": "Kintara",
        "company_domain": null,
        "logo": null,
        "locations": [
          "Grandview Heights, Ohio, US"
        ],
        "remote": false,
        "salary": {
          "min": null,
          "max": null,
          "currency": null
        },
        "experience": null,
        "skills": [],
        "posted": "2026-09-08",
        "url": "https://www.talent.com/view?id=636478413375605243",
        "direct_apply": false,
        "source": "talent"
      }
    ],
    "total_estimate": 503,
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
    "retrieved_at": "2026-09-23T03:35:33.446903+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/37-us-software-jobs.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
