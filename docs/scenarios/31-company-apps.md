# Which Google Play apps have swiggy.com as the developer website host?

[All 50 scenarios](README.md) · [Workflow guide](../guides/apps-data-api.md) · [Endpoint reference](../reference/company_apps.md)

**POST `/v1/companies/apps`** · MCP tool **`company_apps`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 4 apps; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 31-company-apps -->
```json
{
  "domain": "swiggy.com",
  "limit": 5
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.926900+00:00; HTTP **200**;
**qualified**, 0.05 seconds.
Local authenticated gateway with live configured read-only sources.

Dated store observations, not a live store check; history can contain duplicate rows.

Company association uses the exact normalized developer website host. It can miss products with a different developer or parent-company domain; it must not accept a lookalike suffix. Store observations are dated and not verified current listings.

The baseline was HTTP 200, **qualified**:
Dated store observations, not a live store check; history can contain duplicate rows. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 31-company-apps -->
```json
{
  "ok": true,
  "feature": "company_apps",
  "data": {
    "apps": [
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
      },
      {
        "app_id": "in.swiggy.partnerapp",
        "name": "Swiggy Partner App",
        "developer": "Swiggy",
        "developer_website": "https://www.swiggy.com",
        "category": "Business",
        "installs": 5189565,
        "rating": 3.9047618,
        "rating_count": 42053,
        "observed_at": "2026-06-08T07:18:48Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=in.swiggy.partnerapp",
        "detail_request": {
          "method": "POST",
          "path": "/v1/apps/profile"
        }
      },
      {
        "app_id": "com.swiggy.swiggyvendorapp",
        "name": "IM Retails Tasks",
        "developer": "SwiggyInstamart",
        "developer_website": "https://www.swiggy.com/",
        "category": "Food & Drink",
        "installs": 218985,
        "rating": 0,
        "rating_count": 0,
        "observed_at": "2026-06-08T07:44:13Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=com.swiggy.swiggyvendorapp",
        "detail_request": {
          "method": "POST",
          "path": "/v1/apps/profile"
        }
      },
      {
        "app_id": "in.swiggy.pulseapp",
        "name": "Swiggy Pulse",
        "developer": "Swiggy",
        "developer_website": "https://www.swiggy.com",
        "category": "Business",
        "installs": 3675,
        "rating": null,
        "rating_count": null,
        "observed_at": "2026-06-08T10:18:55Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=in.swiggy.pulseapp",
        "detail_request": {
          "method": "POST",
          "path": "/v1/apps/profile"
        }
      }
    ],
    "page": 0,
    "limit": 5,
    "has_more": false,
    "total": null,
    "match_method": "Exact normalized developer website host; no fuzzy name, URL substring or ownership inference",
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
    "retrieved_at": "2026-09-23T03:35:32.926724+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/31-company-apps.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
