# Company mobile apps API: discover apps by developer website domain

[All endpoints](README.md) · [Workflow guide](../guides/apps-data-api.md)

Find individual Google Play apps whose developer website host exactly matches the requested company domain. Retrieve app IDs, install counts, ratings, categories and dates before choosing a separate detail field.

## Route, authentication and credits

**`POST /v1/companies/apps`** · MCP tool **`company_apps`** · key scope **`companies`**.
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
| `domain` | required | string |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

`RADAR_API_URL` is `https://radar-api.fliarbi.com` (the [installer](../../README.md#install-in-one-line) sets it);
load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/apps" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"swiggy.com","limit":5}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: company_apps -->
```json
{
  "name": "company_apps",
  "arguments": {
    "request": {
      "domain": "swiggy.com",
      "limit": 5
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: company_apps -->
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
    "retrieved_at": "2026-09-23T06:47:27.596513+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:27.596675+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/company_apps.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The swiggy.com capture contains four distinct apps. The delivery-partner app uses ride.swiggy.com and appears in the broader app search, not in this exact-host result.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.apps` | All matching app cards on this page, each with store ID and a profile request. |
| `data.match_method` | Exact normalized host, with www removed. Subdomains require their own domain request. |
| `data.has_more` | Whether another result exists beyond this bounded page; total is intentionally unknown. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Start from an accepted company domain, request its apps, then get_app and get_app_field for a selected app ID. Repeat explicitly for a known subdomain when appropriate.

Coverage is observed Google Play / Android data. Apple App Store coverage is not connected. Capture time is not store freshness; observation timestamps are UTC. Zero ratings and unknown ratings remain distinct. A URL path mentioning a company is not a domain match or ownership proof.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/apps-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
