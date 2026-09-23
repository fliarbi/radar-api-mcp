# App data depth: seven separate live field responses

These captures used the local authenticated gateway against Radar's stored
Google Play data. They do not prove public deployment or a current store refresh.
The app is `in.swiggy.android`; its profile reports 15 stored history rows.
The live pagination audit found 13 duplicate rows, leaving two distinct
observations. The API preserves the source sequence and explicitly reports that
history is not deduplicated. Do not treat those rows as 15 distinct dates.
All business fields and returned array rows are retained. Long listing prose is
omitted explicitly, with its original-response hash preserved in the JSON record.

Use [app discovery and field requests](guides/apps-data-api.md) to reproduce the
workflow. Responses below correspond to one selected field per POST, not a single
oversized company or app profile. Developer contacts are not included.

## listing

POST `/v1/apps/field`:

```json
{
  "app_id": "in.swiggy.android",
  "field": "listing",
  "limit": 5
}
```

<!-- app-field-response: listing -->
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
    "field": "listing",
    "value": {
      "name": "Swiggy: Food Instamart Dineout",
      "summary": "Online Food Delivery | Exciting Dineout Deals | Grocery Delivery",
      "category": "Food & Drink",
      "categories": [
        {
          "name": "Food & Drink",
          "id": "FOOD_AND_DRINK"
        }
      ],
      "content_rating": "Everyone",
      "privacy_policy": "https://www.swiggy.com/privacy-policy",
      "screenshots": [
        "https://play-lh.googleusercontent.com/2GzVPLgHzUYGbvSXKNlQSV2CrRT8brHzdbY71end-YKc0OE70EK3YFz92oIV0pAySIjcQ9k5wetGAxgr0_HPcQ",
        "https://play-lh.googleusercontent.com/eQrtxNFpjUgoV26weTu1bQvqJTJAcgqdFteZKMvJ7zL5ZOJBMVhf6N1B72_n-lJ7SA3zBM8lUuU2kJ9t2vl-9Q",
        "https://play-lh.googleusercontent.com/Io6RNySrwPVdXXP-LoOYWlDYqAFQfttc6lJVXG9kyVL5bE2f55v7ihu6v9RUBTtKWCXsnf8-3Zm4Yqud15lcdHA",
        "https://play-lh.googleusercontent.com/iiP5zB2r5hWmNILYO140cUdTQRM0OW9qOXEp9cW-0_KQ-w7ES4WCsJvkkC7E1GweLvZ2NNxedVKAwxUq4WalSQ",
        "https://play-lh.googleusercontent.com/x782Q17Ne2Y1B1JcTApwo4sF9Yf-hfoOf4olLoUF-GfBzUZNsnKgSrqTWHHwVGtWeiieHMmyu0jF6zw3ZIoo",
        "https://play-lh.googleusercontent.com/jyTnGQu-jyVv3efLBSyiN0jGA9OjMzccbLvlVYwwesNT-Ir4aQSLl7FiB9d-bteQpB3fLfDpHNfLQG8JGK9nVA",
        "https://play-lh.googleusercontent.com/MDt7uyGdwkaM0OKbGkzWJZDVE3tRNhwY93tcQBBjxIZs7Piw1KB6Ee5k8QfYfWe2G02j5rws_XYM7CBlkDybCg",
        "https://play-lh.googleusercontent.com/2_-cWtXgPEtRh5YeWVc1NEKluqamwCwQ-I0GQmBifK-H7bBbWpsFIJll8AIO_O_unCuseTL30EIpN-3bu7njhzE",
        "https://play-lh.googleusercontent.com/2GzVPLgHzUYGbvSXKNlQSV2CrRT8brHzdbY71end-YKc0OE70EK3YFz92oIV0pAySIjcQ9k5wetGAxgr0_HPcQ",
        "https://play-lh.googleusercontent.com/eQrtxNFpjUgoV26weTu1bQvqJTJAcgqdFteZKMvJ7zL5ZOJBMVhf6N1B72_n-lJ7SA3zBM8lUuU2kJ9t2vl-9Q",
        "https://play-lh.googleusercontent.com/Io6RNySrwPVdXXP-LoOYWlDYqAFQfttc6lJVXG9kyVL5bE2f55v7ihu6v9RUBTtKWCXsnf8-3Zm4Yqud15lcdHA",
        "https://play-lh.googleusercontent.com/iiP5zB2r5hWmNILYO140cUdTQRM0OW9qOXEp9cW-0_KQ-w7ES4WCsJvkkC7E1GweLvZ2NNxedVKAwxUq4WalSQ",
        "https://play-lh.googleusercontent.com/x782Q17Ne2Y1B1JcTApwo4sF9Yf-hfoOf4olLoUF-GfBzUZNsnKgSrqTWHHwVGtWeiieHMmyu0jF6zw3ZIoo",
        "https://play-lh.googleusercontent.com/jyTnGQu-jyVv3efLBSyiN0jGA9OjMzccbLvlVYwwesNT-Ir4aQSLl7FiB9d-bteQpB3fLfDpHNfLQG8JGK9nVA",
        "https://play-lh.googleusercontent.com/MDt7uyGdwkaM0OKbGkzWJZDVE3tRNhwY93tcQBBjxIZs7Piw1KB6Ee5k8QfYfWe2G02j5rws_XYM7CBlkDybCg",
        "https://play-lh.googleusercontent.com/2_-cWtXgPEtRh5YeWVc1NEKluqamwCwQ-I0GQmBifK-H7bBbWpsFIJll8AIO_O_unCuseTL30EIpN-3bu7njhzE",
        "https://play-lh.googleusercontent.com/2GzVPLgHzUYGbvSXKNlQSV2CrRT8brHzdbY71end-YKc0OE70EK3YFz92oIV0pAySIjcQ9k5wetGAxgr0_HPcQ",
        "https://play-lh.googleusercontent.com/eQrtxNFpjUgoV26weTu1bQvqJTJAcgqdFteZKMvJ7zL5ZOJBMVhf6N1B72_n-lJ7SA3zBM8lUuU2kJ9t2vl-9Q",
        "https://play-lh.googleusercontent.com/Io6RNySrwPVdXXP-LoOYWlDYqAFQfttc6lJVXG9kyVL5bE2f55v7ihu6v9RUBTtKWCXsnf8-3Zm4Yqud15lcdHA",
        "https://play-lh.googleusercontent.com/iiP5zB2r5hWmNILYO140cUdTQRM0OW9qOXEp9cW-0_KQ-w7ES4WCsJvkkC7E1GweLvZ2NNxedVKAwxUq4WalSQ",
        "https://play-lh.googleusercontent.com/x782Q17Ne2Y1B1JcTApwo4sF9Yf-hfoOf4olLoUF-GfBzUZNsnKgSrqTWHHwVGtWeiieHMmyu0jF6zw3ZIoo",
        "https://play-lh.googleusercontent.com/jyTnGQu-jyVv3efLBSyiN0jGA9OjMzccbLvlVYwwesNT-Ir4aQSLl7FiB9d-bteQpB3fLfDpHNfLQG8JGK9nVA",
        "https://play-lh.googleusercontent.com/MDt7uyGdwkaM0OKbGkzWJZDVE3tRNhwY93tcQBBjxIZs7Piw1KB6Ee5k8QfYfWe2G02j5rws_XYM7CBlkDybCg",
        "https://play-lh.googleusercontent.com/2_-cWtXgPEtRh5YeWVc1NEKluqamwCwQ-I0GQmBifK-H7bBbWpsFIJll8AIO_O_unCuseTL30EIpN-3bu7njhzE"
      ],
      "available": true,
      "installs_display": "100,000,000+",
      "minimum_installs": 100000000,
      "maximum_installs": 281013619,
      "observed_installs": 281013619
    },
    "status": "available"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:51:11.465695+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download this captured response](examples/apps/swiggy-listing.json). HTTP 200 captured
2026-09-23T06:51:11.465906+00:00. Omitted paths: `/data/value/description`.

## ratings

POST `/v1/apps/field`:

```json
{
  "app_id": "in.swiggy.android",
  "field": "ratings",
  "limit": 5
}
```

<!-- app-field-response: ratings -->
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
    "field": "ratings",
    "value": {
      "rating": 4.663636,
      "rating_count": 12718296,
      "review_count": 3487,
      "histogram": {
        "1": 619718,
        "2": 92288,
        "3": 235797,
        "4": 1049783,
        "5": 10720247
      },
      "rating_display": "4.7"
    },
    "status": "available"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:51:11.508768+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download this captured response](examples/apps/swiggy-ratings.json). HTTP 200 captured
2026-09-23T06:51:11.508916+00:00. Omitted paths: none.

## monetization

POST `/v1/apps/field`:

```json
{
  "app_id": "in.swiggy.android",
  "field": "monetization",
  "limit": 5
}
```

<!-- app-field-response: monetization -->
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
    "field": "monetization",
    "value": {
      "price": 0,
      "free": 1,
      "currency": "USD",
      "offers_in_app_purchases": 0,
      "ad_supported": 0,
      "contains_ads": 0,
      "play_pass": false,
      "price_display": "Free"
    },
    "status": "available"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:51:11.553929+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download this captured response](examples/apps/swiggy-monetization.json). HTTP 200 captured
2026-09-23T06:51:11.554073+00:00. Omitted paths: none.

## release

POST `/v1/apps/field`:

```json
{
  "app_id": "in.swiggy.android",
  "field": "release",
  "limit": 5
}
```

<!-- app-field-response: release -->
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
    "field": "release",
    "value": {
      "released": "Jun 16, 2015",
      "updated": "2026-06-02",
      "version": "4.109.1",
      "minimum_android_version": "7.0",
      "maximum_android_version": "VARY",
      "preregister": false,
      "early_access": false,
      "recent_changes": null,
      "android_version_display": "7.0"
    },
    "status": "available"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:51:11.597963+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download this captured response](examples/apps/swiggy-release.json). HTTP 200 captured
2026-09-23T06:51:11.598119+00:00. Omitted paths: none.

## developer

POST `/v1/apps/field`:

```json
{
  "app_id": "in.swiggy.android",
  "field": "developer",
  "limit": 5
}
```

<!-- app-field-response: developer -->
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
    "field": "developer",
    "value": {
      "name": "Swiggy",
      "store_developer_id": "Swiggy",
      "website": "https://www.swiggy.com",
      "legal_name": "SWIGGY LIMITED"
    },
    "status": "available"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:51:11.635111+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download this captured response](examples/apps/swiggy-developer.json). HTTP 200 captured
2026-09-23T06:51:11.635304+00:00. Omitted paths: none.

## growth

POST `/v1/apps/field`:

```json
{
  "app_id": "in.swiggy.android",
  "field": "growth",
  "limit": 5
}
```

<!-- app-field-response: growth -->
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
    "retrieved_at": "2026-09-23T06:51:11.689181+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download this captured response](examples/apps/swiggy-growth.json). HTTP 200 captured
2026-09-23T06:51:11.689319+00:00. Omitted paths: none.

## install_history

POST `/v1/apps/field`:

```json
{
  "app_id": "in.swiggy.android",
  "field": "install_history",
  "limit": 5
}
```

<!-- app-field-response: install_history -->
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
        "observed_at": "2026-06-07T03:54:55Z",
        "installs": 281013619,
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
      "offset": 0,
      "limit": 5,
      "deduplicated": false,
      "note": "Exact duplicate source observations are preserved; source_total counts stored rows.",
      "next_offset": 5
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:51:11.726483+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download this captured response](examples/apps/swiggy-install_history.json). HTTP 200 captured
2026-09-23T06:51:11.726627+00:00. Omitted paths: none.

## Interpret dates, estimates and flags

The growth example compares 223,179,065 and 281,013,619 recorded installs across
360 days. Its 25.91% observed change and 26.32% annualized change are different
quantities. `reliable` and `release_date_suspect` remain visible, including zero.
Install totals are source estimates, not monthly users or revenue. Observation
timestamps are normalized to UTC. Source release text and update epoch retain
their original formats. Install-history pagination exposes `source_total` and
`next_offset`; each response contains every requested row without docs truncation.

See [profile output](reference/get_app.md), [exact-domain company app output](reference/company_apps.md)
and [potential-company evidence](guides/potential-company-data-api.md).
