# Retrieve Anupam Mittal’s measured co-investor relationships.

[All 50 scenarios](README.md) · [Workflow guide](../guides/investor-data-api.md) · [Endpoint reference](../reference/get_investor_field.md)

**POST `/v1/investors/field`** · MCP tool **`get_investor_field`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** Selected field co_investors contains data.

## Exact executed request

<!-- scenario-request: 45-investor-co-backers -->
```json
{
  "slug": "anupam-mittal",
  "field": "co_investors"
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.670442+00:00; HTTP **200**;
**qualified**, 0.004 seconds.
Local authenticated gateway with live configured read-only sources.

Dated published research snapshot; not current investment activity.

This is a dated published research snapshot. Keep data_through, release and cohort definitions. Portfolio amounts are whole-round amounts, sectors can overlap, and a co-investor relationship is not proof of a current partnership or investment mandate.

The baseline was HTTP 200, **qualified**:
Dated published research snapshot; not current investment activity. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 45-investor-co-backers -->
```json
{
  "ok": true,
  "feature": "get_investor_field",
  "data": {
    "slug": "anupam-mittal",
    "kind": "investor_profile",
    "family": "investor",
    "coverage": {
      "data_through": "2026-05-22",
      "computed_on": "2026-09-14",
      "last_investment": "2026-03-28",
      "first_investment": "2011-04-21",
      "recent_window_start": "2024-05-22",
      "previous_window_start": "2022-05-22",
      "release": "atlas-20260914-v1",
      "snapshot_sha256": "ce205691ab49871ec3e14f25ea4fabc89c1b8a75c4d8053ae755453869946979",
      "partial": false,
      "source": "verified_published_atlas_snapshot"
    },
    "field": "co_investors",
    "status": "available",
    "definitions": {
      "portfolio": "Dated equity investments; undated companies are retrieved separately. Debt and grants are excluded.",
      "amounts": "USD whole-round amounts, not the investor's cheque, fund size, assets under management or investment returns.",
      "follow_on": "Another investor's later financing and this investor's repeat backing are distinct. Only entries with a full 24-month observation window enter the cohort.",
      "sectors": "Historical company tags can overlap; their counts are not additive and do not establish a current investment mandate.",
      "directory": "A directory's stored shortlist is a selected subset of its measured investor universe, not every investor in the database."
    },
    "value": [
      {
        "name": "Aman Gupta",
        "kind": "angel",
        "rounds": 43,
        "image_url": "https://in-api-radar.fliarbi.com/investors/photo?slug=aman-gupta",
        "companies": 43,
        "last": "2026-01-28",
        "url": "/investor/aman-gupta/"
      },
      {
        "name": "Peyush Bansal",
        "kind": "angel",
        "rounds": 38,
        "image_url": "https://in-api-radar.fliarbi.com/investors/photo?slug=peyush-bansal",
        "companies": 38,
        "last": "2025-08-26",
        "url": "/investor/peyush-bansal/"
      },
      {
        "name": "Vineeta Singh",
        "kind": "angel",
        "rounds": 35,
        "image_url": null,
        "companies": 35,
        "last": "2026-03-12",
        "url": "/investor/vineeta-tejpal-singh/"
      },
      {
        "name": "LetsVenture",
        "kind": "firm",
        "rounds": 29,
        "image_url": "https://in-api-radar.fliarbi.com/company_logo?domain=letsventure.com",
        "companies": 28,
        "last": "2025-01-28",
        "url": null
      },
      {
        "name": "Namita Thapar",
        "kind": "angel",
        "rounds": 28,
        "image_url": "https://in-api-radar.fliarbi.com/investors/photo?slug=namita-thapar",
        "companies": 28,
        "last": "2026-01-28",
        "url": "/investor/namita-thapar/"
      },
      {
        "name": "Kunal Bahl",
        "kind": "angel",
        "rounds": 25,
        "image_url": "https://in-api-radar.fliarbi.com/investors/photo?slug=kunal-bahl",
        "companies": 23,
        "last": "2026-02-11",
        "url": "/investor/kunal-bahl/"
      },
      {
        "name": "Rajesh Sawhney",
        "kind": "angel",
        "rounds": 23,
        "image_url": "https://in-api-radar.fliarbi.com/investors/photo?slug=rajesh-sawhney",
        "companies": 21,
        "last": "2021-03-16",
        "url": "/investor/rajesh-sawhney/"
      },
      {
        "name": "Dinesh Agarwal",
        "kind": "angel",
        "rounds": 22,
        "image_url": "https://in-api-radar.fliarbi.com/investors/photo?slug=dinesh-agarwal",
        "companies": 19,
        "last": "2015-12-05",
        "url": "/investor/dinesh-agarwal/"
      }
    ],
    "pagination": {
      "source_total": 8,
      "matched_total": 8,
      "offset": 0,
      "limit": 20,
      "returned": 8,
      "next_offset": null
    }
  },
  "window": {
    "data_through": "2026-05-22"
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.670273+00:00",
    "partial": false,
    "notes": [
      "Investor metrics use the dated, verified Atlas snapshot. Retrieval time is not data freshness. Use available_fields for separate detail requests."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/45-investor-co-backers.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
