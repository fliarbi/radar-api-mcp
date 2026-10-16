# Which source employers have Business Development internship listings?

[All 50 scenarios](README.md) · [Workflow guide](../guides/internships-companies-api.md) · [Endpoint reference](../reference/companies_offering_internships.md)

**POST `/v1/jobs/internships/companies`** · MCP tool **`companies_offering_internships`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 companies; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 42-internship-employers -->
```json
{
  "title": "Business Development",
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.638567+00:00; HTTP **200**;
**qualified**, 0.007 seconds.
Local authenticated gateway with live configured read-only sources.

Observed internship listings; current vacancies unverified, deadlines can be expired.

Employers are grouped by exact source name, not a verified corporate domain. Counts describe observed internship records, including old postings. Use sample IDs to inspect listings; do not call the count verified current vacancies.

The baseline was HTTP 200, **qualified**:
Observed internship listings; current vacancies unverified, deadlines can be expired. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 42-internship-employers -->
```json
{
  "ok": true,
  "feature": "companies_offering_internships",
  "data": {
    "companies": [
      {
        "name": "Across The Globe (ATG)",
        "company_domain": null,
        "observed_internships": 2,
        "latest_posted": "2026-06-19",
        "sample_titles": [
          "Business Development Executive - Internship (WFH & Part Time)",
          "Business Development & Client Relations - Internship (WFH)"
        ],
        "sample_internship_ids": [
          "1781859880",
          "1780995392"
        ],
        "current_openings_verified": false
      },
      {
        "name": "Estate Plus CRM",
        "company_domain": null,
        "observed_internships": 2,
        "latest_posted": "2026-07-03",
        "sample_titles": [
          "Business Development (Sales) - Internship (WFH & Part Time)",
          "Business Development (Sales) - Internship (WFH & Part Time)"
        ],
        "sample_internship_ids": [
          "1783075957",
          "1780743453"
        ],
        "current_openings_verified": false
      },
      {
        "name": "Fin Maverick",
        "company_domain": null,
        "observed_internships": 2,
        "latest_posted": "2026-06-22",
        "sample_titles": [
          "Business Development (NISM Mandatory) - Internship (WFH)",
          "Business Development (Sales) - Internship (WFH)"
        ],
        "sample_internship_ids": [
          "1782126972",
          "1781758426"
        ],
        "current_openings_verified": false
      }
    ],
    "page": 0,
    "limit": 3,
    "has_more": true,
    "grouping": "Exact source employer name, not a verified company identity or domain join",
    "note": "These are observed internship listings, not verified current vacancies. Posted and crawl dates are separate. Far-future source deadlines are not proof a listing remains open. Stipend periods are not supplied."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.638340+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/42-internship-employers.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
