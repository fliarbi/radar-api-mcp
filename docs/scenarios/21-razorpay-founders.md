# Retrieve Razorpay’s recorded founders with role descriptions.

[All 50 scenarios](README.md) · [Workflow guide](../guides/teams-people-data-api.md) · [Endpoint reference](../reference/get_company_team.md)

**POST `/v1/companies/team`** · MCP tool **`get_company_team`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 2 people; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 21-razorpay-founders -->
```json
{
  "domain": "razorpay.com",
  "group": "founders",
  "limit": 10
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.198845+00:00; HTTP **200**;
**qualified**, 0.006 seconds.
Local authenticated gateway with live configured read-only sources.

Recorded professional or key-person data; current roles and complete resumes are unverified; Coverage is explicitly bounded.

Founders and key people are company records; professionals are source profile cards filtered to an exact recorded company domain. Neither is a verified current employee roster. Keep update dates, excluded affiliations and partial flags. Highest career seniority can differ from a current role, and card count is not headcount.

The baseline was an unavailable operation registry check (no HTTP request), **unavailable**:
not_implemented. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 21-razorpay-founders -->
```json
{
  "ok": true,
  "feature": "get_company_team",
  "data": {
    "domain": "razorpay.com",
    "group": "founders",
    "people": [
      {
        "name": "Shashank Kumar",
        "designation": "Co-Founder & Managing Director"
      },
      {
        "name": "Harshil Mathur",
        "designation": "Co-Founder & CEO"
      }
    ],
    "returned": 2,
    "matched_observed_rows": 2,
    "page": 0,
    "next_page": null,
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "complete": false,
      "partial": false,
      "source_status": "available",
      "note": "Company key-person records, not a full employee roster or verified headcount. Founders are selected by recorded designation; no contacts are included."
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:32.198739+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/21-razorpay-founders.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
