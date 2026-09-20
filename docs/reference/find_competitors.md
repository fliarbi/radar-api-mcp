# Competitor discovery API: companies grouped by funding stage

[All endpoints](README.md) · [Workflow guide](../guides/competitor-intelligence-api.md)

Find candidate peer companies for a named market, optionally narrowed by business model. The source groups returned companies by funding stage. This is market discovery, not a verified competitive-ranking model or a list centered on an input company domain.

## Route, authentication and credits

**`POST /v1/companies/competitors`** · MCP tool **`find_competitors`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `market` | required | string; min characters: `1`; max characters: `200` |
| `business_model` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `per_stage` | default `5` | integer; minimum: `3`; maximum: `10` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/competitors" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"market":"Software","per_stage":3}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: find_competitors -->
```json
{
  "name": "find_competitors",
  "arguments": {
    "request": {
      "market": "Software",
      "per_stage": 3
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: find_competitors -->
```json
{
  "ok": true,
  "feature": "find_competitors",
  "data": {
    "market": "Software",
    "summary": {
      "country": {},
      "stage": {},
      "total": 0
    },
    "companies": {
      "Public": [],
      "Seed": [],
      "Series A": [],
      "Series B": [],
      "Series C": []
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:46.274343+00:00",
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
The [downloadable JSON example](../examples/find_competitors.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The broad Software query returned HTTP 200 with an empty companies dictionary. That is a real empty discovery result, not a successful list of zero competitors in the economy. A more specific recognized market label may be needed.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.market` | The market label supplied in the request. |
| `data.companies` | A dictionary of returned stage groups, each containing company cards. |
| `data.summary` | Additional source summary fields when available. |
| `per_stage` | Requested companies per stage, between three and ten; this is not a global result limit. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Choose a precise market label from industry discovery, request a small number of companies per stage, and review each candidate's product and geography. Pass selected distinct domains to compare_companies for separate profile and financial evidence.

Do not describe an empty or narrow source result as the full competitive landscape. A similar industry label does not establish that two businesses compete for the same buyer.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/competitor-intelligence-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
