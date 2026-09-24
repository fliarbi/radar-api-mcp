# Find Indian seed-stage software companies with funding rounds in the USD 10K–100K band.

[All 50 scenarios](README.md) · [Workflow guide](../guides/startup-funding-data-api.md) · [Endpoint reference](../reference/search_companies.md)

**POST `/v1/companies/search`** · MCP tool **`search_companies`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Coverage or failure example — no populated requested result.** 0 companies; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 11-seed-small-round -->
```json
{
  "filters": {
    "industries": [
      "Software"
    ],
    "locations": [
      "India"
    ],
    "stages": [
      "Seed"
    ],
    "deal_sizes": [
      "10-100K"
    ]
  },
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:31.944319+00:00; HTTP **200**;
**qualified**, 0.126 seconds.
Local authenticated gateway with live configured read-only sources.

Empty documentation example: 0 companies; totals and context do not substitute for requested rows; Source-labelled predicates; cards do not independently verify financial/classification conditions; Expanded or unverified source candidates were excluded; No rows observed; not proof of a complete negative.

Read each match_tier and the matching/excluded_candidates count before accepting the shortlist. Strict is the source's label, not an independent verification of every company attribute. Financial bands refer to source summary fields, not a selected fiscal year; retrieve financial evidence separately. Advance source pages even if strict filtering leaves an empty page with a continuation hint.

The baseline returned expanded candidates, including a US company. The repaired strict page is empty because its three source candidates were expanded. Do not change the seed/deal filters merely to produce an attractive example; the empty qualified result is part of the finding.

The baseline was HTTP 200, **failed**:
Company country violates requested location: sep.com. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 11-seed-small-round -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
    "companies": [],
    "page": 0,
    "requested_limit": 3,
    "returned": 0,
    "total": null,
    "access": {
      "plan": "free",
      "results_capped": false,
      "searches_remaining": 50
    },
    "partial_timeout": false,
    "matching": {
      "mode": "strict",
      "tiers": [
        {
          "tier": "strict",
          "added": 0,
          "cumulative": 0
        },
        {
          "tier": "semantic",
          "added": 3,
          "cumulative": 3
        }
      ],
      "source_rows": 3,
      "excluded_candidates": 3,
      "strict_count_reported": 0,
      "candidate_pool_count_reported": 3,
      "count_capped": false,
      "filters_restricted": false,
      "note": "Strict means the source labelled the row strict and did not strip filters. Counts may describe an expanded candidate pool, not all matching companies. Missing tier metadata is unverified."
    },
    "next_page": 1,
    "pagination": "Increment source page even when strict filtering returns no rows; next_page is a continuation hint, not a guarantee of more matches. Account caps apply."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:31.944108+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/11-seed-small-round.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
