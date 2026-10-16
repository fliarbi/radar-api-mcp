# Retrieve the second page of Swiggy install observations while retaining source duplicates.

[All 50 scenarios](README.md) · [Workflow guide](../guides/apps-data-api.md) · [Endpoint reference](../reference/get_app_field.md)

**POST `/v1/apps/field`** · MCP tool **`get_app_field`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** Selected field install_history contains data.

## Exact executed request

<!-- scenario-request: 34-app-history-page -->
```json
{
  "app_id": "in.swiggy.android",
  "field": "install_history",
  "limit": 5,
  "offset": 5
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.010295+00:00; HTTP **200**;
**qualified**, 0.009 seconds.
Local authenticated gateway with live configured read-only sources.

Dated store observations, not a live store check; history can contain duplicate rows.

Retain the selected field's source structure and observation date. Install history counts stored rows, including duplicates, rather than unique dates. Growth uses dated measurements and the actual interval; ratings and monetization are observations, not forecasts or revenue estimates.

This page has five identical observed dates and values. The source explicitly reports deduplicated=false and source_total=15. These are stored rows, not five new install measurements.

The baseline was HTTP 200, **qualified**:
Dated store observations, not a live store check; history can contain duplicate rows. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 34-app-history-page -->
```json
{
  "ok": true,
  "feature": "get_app_field",
  "data": {
    "app_id": "in.swiggy.android",
    "store": "google_play",
    "observed_at": "2026-06-07T03:54:55Z",
    "coverage": {
      "live_store_verified": false,
      "source": "radar_app_records"
    },
    "field": "install_history",
    "value": [
      {
        "observed_at": "2025-06-11T18:30:00Z",
        "installs": 223179065,
        "minimum_installs": 100000000
      },
      {
        "observed_at": "2025-06-11T18:30:00Z",
        "installs": 223179065,
        "minimum_installs": 100000000
      },
      {
        "observed_at": "2025-06-11T18:30:00Z",
        "installs": 223179065,
        "minimum_installs": 100000000
      },
      {
        "observed_at": "2025-06-11T18:30:00Z",
        "installs": 223179065,
        "minimum_installs": 100000000
      },
      {
        "observed_at": "2025-06-11T18:30:00Z",
        "installs": 223179065,
        "minimum_installs": 100000000
      }
    ],
    "status": "available",
    "pagination": {
      "source_total": 15,
      "offset": 5,
      "limit": 5,
      "deduplicated": false,
      "note": "Exact duplicate source observations are preserved; source_total counts stored rows.",
      "next_offset": 10
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.010168+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/34-app-history-page.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
