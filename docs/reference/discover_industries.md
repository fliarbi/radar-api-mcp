# Industry discovery API: find market, sector and industry labels

[All endpoints](README.md) · [Workflow guide](../guides/company-search-api.md)

Find a small set of vocabulary labels that can be used in company and investor filters. A search phrase may match a market, a sector or an industry; the returned kind tells you which structured filter field to use.

## Route, authentication and credits

**`POST /v1/industries/discover`** · MCP tool **`discover_industries`** · key scope **`industries`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `q` | required | string; min characters: `2`; max characters: `500` |
| `limit` | default `5` | integer; minimum: `1`; maximum: `5` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

`RADAR_API_URL` is `https://radar-api.fliarbi.com` (the [installer](../../README.md#install-in-one-line) sets it);
load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/industries/discover" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q":"software","limit":3}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: discover_industries -->
```json
{
  "name": "discover_industries",
  "arguments": {
    "request": {
      "q": "software",
      "limit": 3
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: discover_industries -->
```json
{
  "ok": true,
  "feature": "discover_industries",
  "data": {
    "query": "software",
    "matches": [
      {
        "name": "Software Libraries",
        "kind": "market"
      },
      {
        "name": "Software Localisation",
        "kind": "market"
      },
      {
        "name": "Software Testing Tools",
        "kind": "market"
      }
    ]
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:58.667918+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:58.668070+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/discover_industries.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live software lookup returned Software Libraries with kind=market. That should be placed in filters.markets, not automatically in industries simply because the request searched for an industry-like term.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.query` | The submitted lookup phrase. |
| `data.matches[].name` | A source classification label. |
| `data.matches[].kind` | market, sector or industry; use the corresponding plural filter name. |
| `limit` | At most five lookup matches can be requested. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Send a specific term, examine the returned names, and place the chosen label in filters.markets, filters.sectors or filters.industries according to kind. Then run a bounded company search. This reduces errors caused by guessing the classification vocabulary.

A returned label is a vocabulary match, not a count of companies in that category. Do not equate a broad common word with every source classification containing it.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-search-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
