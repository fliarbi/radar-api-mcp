# Retrieve Swiggy app growth together with the dated measurements and reliability flag.

[All 50 scenarios](README.md) · [Workflow guide](../guides/apps-data-api.md) · [Endpoint reference](../reference/get_app_field.md)

**POST `/v1/apps/field`** · MCP tool **`get_app_field`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** Selected field growth contains data.

## Exact executed request

<!-- scenario-request: 33-app-growth -->
```json
{
  "app_id": "in.swiggy.android",
  "field": "growth"
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.997724+00:00; HTTP **200**;
**qualified**, 0.016 seconds.
Local authenticated gateway with live configured read-only sources.

Dated store observations, not a live store check; history can contain duplicate rows.

Retain the selected field's source structure and observation date. Install history counts stored rows, including duplicates, rather than unique dates. Growth uses dated measurements and the actual interval; ratings and monetization are observations, not forecasts or revenue estimates.

The baseline was HTTP 200, **qualified**:
Dated store observations, not a live store check; history can contain duplicate rows. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 33-app-growth -->
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
    "field": "growth",
    "value": {
      "install_change": {
        "current_observed_at": "2026-06-07T03:54:55Z",
        "current_installs": 281013619,
        "previous_installs": 223179065,
        "previous_observed_at": "2025-06-11T18:30:00Z",
        "gap_days": 360,
        "observed_change_pct": 25.91,
        "annualized_change_pct": 26.32,
        "reliable": 1
      },
      "velocity": {
        "age_years": 11,
        "avg_installs_per_year": 25551462,
        "release_date_suspect": 0,
        "young_fast_riser": 0
      },
      "note": "Annualized growth is derived from the measured gap, not necessarily a full-year observation. Retain reliable and suspect-date flags; this is not a forecast."
    },
    "status": "available"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:32.997596+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/33-app-growth.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
