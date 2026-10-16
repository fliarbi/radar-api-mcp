# Mobile app data API: search Android apps, categories, installs and ratings

[All endpoints](README.md) · [Workflow guide](../guides/apps-data-api.md)

Discover app records by name, developer, exact website host, category, minimum installs, minimum rating and free/paid status. Sort by installs, rating, observation date or name.

## Route, authentication and credits

**`POST /v1/apps/search`** · MCP tool **`search_apps`** · key scope **`apps`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `page` | default `0` | integer; minimum: `0`; maximum: `200` |
| `limit` | default `20` | integer; minimum: `1`; maximum: `100` |
| `q` | default `null` | string or null; min characters: `2`; max characters: `500` |
| `developer` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `domain` | default `null` | string or null |
| `category` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `min_installs` | default `null` | integer or null; minimum: `1`; maximum: `1000000000000000` |
| `min_score` | default `null` | number or null; minimum: `0`; maximum: `5` |
| `free` | default `null` | boolean or null |
| `sort_by` | default `"installs"` | string; one of `installs`, `rating`, `observed`, `name` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

`RADAR_API_URL` is `https://radar-api.fliarbi.com` (the [installer](../../README.md#install-in-one-line) sets it);
load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/apps/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q":"Swiggy","min_installs":1000000,"limit":3}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_apps -->
```json
{
  "name": "search_apps",
  "arguments": {
    "request": {
      "q": "Swiggy",
      "min_installs": 1000000,
      "limit": 3
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: search_apps -->
```json
{
  "ok": true,
  "feature": "search_apps",
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
        "app_id": "in.swiggy.deliveryapp",
        "name": "Swiggy Delivery Partner App",
        "developer": "Swiggy",
        "developer_website": "https://ride.swiggy.com",
        "category": "Food & Drink",
        "installs": 34456156,
        "rating": 4.2,
        "rating_count": 395330,
        "observed_at": "2026-06-08T12:09:16Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=in.swiggy.deliveryapp",
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
      }
    ],
    "page": 0,
    "limit": 3,
    "has_more": false,
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
    "retrieved_at": "2026-09-23T06:47:59.164321+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:59.164476+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_apps.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Swiggy query with at least one million installs returns the consumer, delivery-partner and merchant-partner apps. Their different hosts remain visible.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.apps` | Identity, developer website, category, cumulative install estimate, rating and rating count. |
| `data.page / limit / has_more` | Zero-based pagination; use the same filters and order on later pages. |
| `data.coverage` | Store coverage and whether the live store was independently checked. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Use app_filter_options to discover category labels. Search with at least a name, developer, domain, category or minimum installs. Use returned app_id values for profile and field requests.

Coverage is observed Google Play / Android data. Apple App Store coverage is not connected. Capture time is not store freshness; observation timestamps are UTC. Zero ratings and unknown ratings remain distinct.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/apps-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
