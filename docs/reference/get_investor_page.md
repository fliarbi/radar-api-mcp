# Investor profile API: portfolio metrics and available research fields

[All endpoints](README.md) · [Workflow guide](../guides/investor-data-api.md)

Retrieve measured investor or directory metrics, source dates and available detail fields from the verified Atlas release. The live Radar publication gate is checked on every request.

## Route, authentication and credits

**`POST /v1/investors/page`** · MCP tool **`get_investor_page`** · key scope **`investors`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `slug` | required | string; min characters: `1`; max characters: `180`; pattern: `^[a-z0-9]+(?:-[a-z0-9]+)*$` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/investors/page" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"slug":"anupam-mittal"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_investor_page -->
```json
{
  "name": "get_investor_page",
  "arguments": {
    "request": {
      "slug": "anupam-mittal"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_investor_page -->
```json
{
  "ok": true,
  "feature": "get_investor_page",
  "data": {
    "slug": "anupam-mittal",
    "kind": "investor_profile",
    "family": "investor",
    "coverage": {
      "data_through": "2026-05-22",
      "computed_on": "2026-09-14",
      "last_investment": "2026-03-28",
      "first_investment": "2011-04-21",
      "recent_window_start": "2024-05-22",
      "previous_window_start": "2022-05-22",
      "release": "atlas-20260914-v1",
      "snapshot_sha256": "ce205691ab49871ec3e14f25ea4fabc89c1b8a75c4d8053ae755453869946979",
      "partial": false,
      "source": "verified_published_atlas_snapshot"
    },
    "name": "Anupam Mittal",
    "location": "Mumbai, India",
    "sector": null,
    "profile_depth": "summary",
    "metrics": {
      "total_companies": 270,
      "total_rounds": 303,
      "portfolio_count": 268,
      "round_count": 301,
      "early_entries": 252,
      "early_pct": 94.0,
      "entry_round_size": {
        "n": 247,
        "q1": 80743.0,
        "median": 222410.0,
        "q3": 671736.5
      },
      "recent_entries": 53,
      "previous_entries": 50,
      "repeat_companies": 28,
      "lead_entries": 81,
      "lead_pct": 30.2,
      "syndicate_median": 5.0
    },
    "available_fields": [
      "portfolio",
      "undated_portfolio",
      "sectors",
      "stages",
      "activity",
      "follow_on",
      "co_investors",
      "news",
      "analysis",
      "related"
    ],
    "field_counts": {
      "portfolio": 268,
      "undated_portfolio": 2,
      "sectors": 12,
      "stages": 7,
      "activity": 16,
      "co_investors": 8,
      "analysis": 4,
      "related": 2
    },
    "field_status": {
      "portfolio": "available",
      "undated_portfolio": "available",
      "sectors": "available",
      "stages": "available",
      "activity": "available",
      "follow_on": "available",
      "co_investors": "available",
      "news": "available",
      "analysis": "available",
      "related": "available"
    },
    "field_request": {
      "method": "POST",
      "path": "/v1/investors/field",
      "required": [
        "slug",
        "field"
      ]
    },
    "definitions": {
      "portfolio": "Dated equity investments; undated companies are retrieved separately. Debt and grants are excluded.",
      "amounts": "USD whole-round amounts, not the investor's cheque, fund size, assets under management or investment returns.",
      "follow_on": "Another investor's later financing and this investor's repeat backing are distinct. Only entries with a full 24-month observation window enter the cohort.",
      "sectors": "Historical company tags can overlap; their counts are not additive and do not establish a current investment mandate.",
      "directory": "A directory's stored shortlist is a selected subset of its measured investor universe, not every investor in the database."
    }
  },
  "window": {
    "data_through": "2026-05-22"
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:55.034463+00:00",
    "partial": false,
    "notes": [
      "Investor metrics use the dated, verified Atlas snapshot. Retrieval time is not data freshness. Use available_fields for separate detail requests."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:55.034614+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_investor_page.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

Anupam Mittal has 270 recorded companies and 303 equity participations; the dated analytical subset is 268 companies and 301 participations. Coverage ends 2026-05-22 and his last recorded investment is 2026-03-28. The median disclosed entry round is USD 222,410 across 247 entries; this is not his personal cheque.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.metrics` | Whole and dated portfolio counts, entry stages, disclosed whole-round size quartiles and activity. Directory pages instead carry measured totals. |
| `data.available_fields / field_counts` | Available field names and stored array counts; no roster is embedded in this summary. |
| `data.coverage` | Source cutoff, computation date, last observation, immutable release and verified snapshot fingerprint. |
| `data.definitions` | Definitions that distinguish round amounts, financing cohorts and selected investor populations. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Discover a slug, request its summary, then POST the slug and one field to get_investor_field. Portfolio, co-investors, cohorts, sourced news and market shortlists have separate retrieval.

Retrieval time does not advance a snapshot cutoff. If detail storage is disconnected, the response is explicitly metadata-only and partial. A live publication gate never substitutes for the rich data connection.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/investor-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
