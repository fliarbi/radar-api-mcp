# Company events API: business activity and effective date windows

[All endpoints](README.md) · [Workflow guide](../guides/company-monitoring-api.md)

Retrieve a company's event timeline and available activity summaries. Use the timeline for company monitoring and the summaries as context, while inspecting their respective windows. A plan can expose a shorter timeline than the number of days requested.

## Route, authentication and credits

**`POST /v1/companies/events`** · MCP tool **`get_company_events`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |
| `days` | default `365` | integer; minimum: `1`; maximum: `1095` |
| `limit` | default `100` | integer; minimum: `1`; maximum: `100` |
| `event_types` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/events" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com","days":30,"limit":2}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_events -->
```json
{
  "name": "get_company_events",
  "arguments": {
    "request": {
      "domain": "microsoft.com",
      "days": 30,
      "limit": 2
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_company_events -->
```json
{
  "ok": true,
  "feature": "get_company_events",
  "data": {
    "freshness": {
      "future_rows_count": 0,
      "future_rows_filtered": false,
      "latest_event_date": "2026-05-04",
      "latest_inserted_at": "2026-09-20T05:30:00+05:30"
    },
    "truncated": true,
    "buckets_by_month": {},
    "domain": "microsoft.com",
    "events": [],
    "plan": "free",
    "pulse": {
      "badges": [
        "Leadership Turnover"
      ],
      "ceo_transitions": 2,
      "churn_penalty": 10,
      "days_since_latest": 999,
      "event_variety_360d": 6,
      "events_30d_fresh": 0,
      "events_360d": 345,
      "events_prev_360d": 425,
      "label": "Quiet",
      "leadership_churn": true,
      "leadership_churn_level": "elevated",
      "momentum_pct": -18.8,
      "opportunity_score": 0,
      "risk_score": 0,
      "score": 36,
      "top_drivers": [
        {
          "count": 186,
          "event_type": "key_people",
          "label": "Key People Movement"
        },
        {
          "count": 74,
          "event_type": "earnings",
          "label": "Earnings Release"
        },
        {
          "count": 61,
          "event_type": "company_announcement",
          "label": "Company Announcement"
        }
      ],
      "window_days": 360
    },
    "totals_by_type": {},
    "window_days": 30
  },
  "window": {
    "data_through": "2026-05-04",
    "effective_days": 30,
    "requested_days": 30
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:46.111118+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_events.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The captured thirty-day Microsoft request returned events=[] and truncated=true. Its source freshness pointed to an older latest event date, and its pulse included broader historical activity. An empty thirty-day list therefore cannot establish that the company has never had any relevant events.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.events` | Returned timeline rows; an empty list is a valid response shape. |
| `data.window_days / window.effective_days` | The effective source window after account gates. |
| `data.truncated` | Indicates the returned timeline is not an unrestricted complete archive. |
| `data.freshness` | Latest event and insertion timestamps supplied by the source. |
| `data.pulse` | Broader activity indicators can use windows different from the visible event list. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Request a bounded window, read window.effective_days and the source's freshness fields, and deduplicate stable article or event identifiers in your application. Show source dates and retrieval time separately. If you poll, each successful call is a new data operation.

Do not mix a 360-day activity score with a thirty-day visible event count, and do not turn a freshness gap into a claim that no news exists.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-monitoring-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
