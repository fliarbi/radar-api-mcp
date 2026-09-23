# App profile API: compact identity, install metrics and available detail fields

[All endpoints](README.md) · [Workflow guide](../guides/apps-data-api.md)

Read a compact app profile and discover the separately retrievable fields. Large listing descriptions, rating histograms and install histories are not bundled into the profile.

## Route, authentication and credits

**`POST /v1/apps/profile`** · MCP tool **`get_app`** · key scope **`apps`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `app_id` | required | string; min characters: `3`; max characters: `255`; pattern: `^[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+$` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/apps/profile" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"app_id":"in.swiggy.android"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_app -->
```json
{
  "name": "get_app",
  "arguments": {
    "request": {
      "app_id": "in.swiggy.android"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_app -->
```json
{
  "ok": true,
  "feature": "get_app",
  "data": {
    "app_id": "in.swiggy.android",
    "store": "google_play",
    "observed_at": "2026-06-07T03:54:55Z",
    "coverage": {
      "live_store_verified": false,
      "source": "radar_app_records"
    },
    "app": {
      "app_id": "in.swiggy.android",
      "name": "Swiggy: Food Instamart Dineout",
      "developer": "Swiggy",
      "developer_website": "https://www.swiggy.com",
      "category": "Food & Drink",
      "installs": 281013619,
      "rating": 4.663636,
      "rating_count": 12718296,
      "observed_at": "2026-06-07T03:54:55Z",
      "summary": "Online Food Delivery | Exciting Dineout Deals | Grocery Delivery",
      "store": "google_play",
      "url": "https://play.google.com/store/apps/details?id=in.swiggy.android",
      "detail_request": {
        "method": "POST",
        "path": "/v1/apps/profile"
      }
    },
    "available_fields": [
      "listing",
      "ratings",
      "monetization",
      "release",
      "developer",
      "growth",
      "install_history"
    ],
    "history_points": 15,
    "history_points_note": "Stored observation rows, including any source duplicates; not distinct days.",
    "field_request": {
      "method": "POST",
      "path": "/v1/apps/field",
      "required": [
        "app_id",
        "field"
      ]
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:59.177508+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:59.177650+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_app.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

Swiggy’s main app has 281,013,619 recorded installs, seven available field groups and 15 install-history observations. The observation is from June 2026, not a live September count.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.app` | App identity, store URL, summary, observed install estimate and rating. |
| `data.available_fields` | Supported recorded field groups; individual values inside a group can be null. |
| `data.history_points` | Number of recorded install observations, not number of users or days. |
| `data.field_request` | POST contract for requesting one selected field. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Choose a field from available_fields and POST app_id plus field to /v1/apps/field. The profile does not reveal developer email, phone or street address.

Coverage is observed Google Play / Android data. Apple App Store coverage is not connected. Capture time is not store freshness; observation timestamps are UTC. Zero ratings and unknown ratings remain distinct.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/apps-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
