# Find Food & Drink apps with at least one million installs and rating at least four.

[All 50 scenarios](README.md) · [Workflow guide](../guides/apps-data-api.md) · [Endpoint reference](../reference/search_apps.md)

**POST `/v1/apps/search`** · MCP tool **`search_apps`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 apps; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 32-food-apps -->
```json
{
  "category": "Food & Drink",
  "min_installs": 1000000,
  "min_score": 4,
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.978630+00:00; HTTP **200**;
**qualified**, 0.048 seconds.
Local authenticated gateway with live configured read-only sources.

Dated store observations, not a live store check; history can contain duplicate rows.

The rating and install predicates are checked against captured structured app values. Keep category, observation date and developer identity. Installs are not active users, revenue or paying customers.

The baseline was HTTP 200, **qualified**:
Dated store observations, not a live store check; history can contain duplicate rows. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 32-food-apps -->
```json
{
  "ok": true,
  "feature": "search_apps",
  "data": {
    "apps": [
      {
        "app_id": "com.application.zomato",
        "name": "Zomato: Food Delivery & Dining",
        "developer": "Zomato",
        "developer_website": "https://www.zomato.com",
        "category": "Food & Drink",
        "installs": 369641274,
        "rating": 4.655456,
        "rating_count": 12792674,
        "observed_at": "2026-06-07T03:54:55Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=com.application.zomato",
        "detail_request": {
          "method": "POST",
          "path": "/v1/apps/profile"
        }
      },
      {
        "app_id": "com.ubercab.eats",
        "name": "Uber Eats: Food and Grocery",
        "developer": "Uber Technologies, Inc.",
        "developer_website": "https://www.ubereats.com",
        "category": "Food & Drink",
        "installs": 288197333,
        "rating": 4.6257734,
        "rating_count": 7544586,
        "observed_at": "2026-06-07T03:54:55Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=com.ubercab.eats",
        "detail_request": {
          "method": "POST",
          "path": "/v1/apps/profile"
        }
      },
      {
        "app_id": "in.swiggy.android",
        "name": "Swiggy: Food Instamart Dineout",
        "developer": "Swiggy",
        "developer_website": "https://www.swiggy.com",
        "category": "Food & Drink",
        "installs": 281013619,
        "rating": 4.663636,
        "rating_count": 12718296,
        "observed_at": "2026-06-07T03:54:55Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=in.swiggy.android",
        "detail_request": {
          "method": "POST",
          "path": "/v1/apps/profile"
        }
      }
    ],
    "page": 0,
    "limit": 3,
    "has_more": true,
    "total": null,
    "match_method": "Explicit app filters",
    "coverage": {
      "store": "google_play",
      "live_store_verified": false
    },
    "note": "Observed Play Store data only. Installs are cumulative source estimates; row observation dates are not current download dates."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:32.978484+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/32-food-apps.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
