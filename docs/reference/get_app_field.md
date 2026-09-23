# App detail fields API: ratings, monetization, releases and install growth

[All endpoints](README.md) · [Workflow guide](../guides/apps-data-api.md)

Retrieve one of listing, ratings, monetization, release, developer, growth or install_history. The response preserves the measured inputs and flags behind growth calculations.

## Route, authentication and credits

**`POST /v1/apps/field`** · MCP tool **`get_app_field`** · key scope **`apps`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `app_id` | required | string; min characters: `3`; max characters: `255`; pattern: `^[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+$` |
| `field` | required | string; one of `listing`, `ratings`, `monetization`, `release`, `developer`, `growth`, `install_history` |
| `limit` | default `20` | integer; minimum: `1`; maximum: `100` |
| `offset` | default `0` | integer; minimum: `0`; maximum: `10000` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/apps/field" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"app_id":"in.swiggy.android","field":"growth"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_app_field -->
```json
{
  "name": "get_app_field",
  "arguments": {
    "request": {
      "app_id": "in.swiggy.android",
      "field": "growth"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_app_field -->
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
    "retrieved_at": "2026-09-23T06:47:59.196089+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:59.196210+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_app_field.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The captured growth comparison spans 360 days: 223,179,065 to 281,013,619 installs, 25.91% observed change and 26.32% annualized change. The source reliable flag is 1. All seven separate field outputs are linked from the app depth walkthrough.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.field / value` | Selected group and its complete public structure; see the seven field captures. |
| `data.status` | available or not_observed. Missing values are not manufactured zeros. |
| `data.value.install_change` | Earlier/later install counts and observation dates, gap days, observed percent change, annualized change and source reliable flag. |
| `data.value.velocity` | Age-derived installs per year plus suspect-release and young-fast-riser flags. |
| `data.pagination` | Install history only: source_total, offset, limit and next_offset. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

For install_history, follow next_offset until null. For ratings, retain histogram buckets and counts. Release fields and monetization fields preserve the source formats; updated is a source Unix timestamp.

Coverage is observed Google Play / Android data. Apple App Store coverage is not connected. Capture time is not store freshness; observation timestamps are UTC. Zero ratings and unknown ratings remain distinct. Annualization is not a forecast or a guarantee of a full-year observation. Offset is rejected for non-history fields.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/apps-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
