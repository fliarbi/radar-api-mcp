# Investor page API: retrieve a published profile by slug

[All endpoints](README.md) · [Workflow guide](../guides/investor-data-api.md)

Retrieve the source representation of a published investor profile or investor list. The accepted identifier is the slug returned by investor_directory. Page types and detail depth vary; this gateway does not bypass additional roster gates.

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
    "h1": "Anupam Mittal",
    "edition": "founder-atlas"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T02:35:04.829625+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T02:35:04.829813+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_investor_page.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

Using the directory's anupam-mittal slug returned HTTP 200 with investor_profile, investor and the heading Anupam Mittal. The captured response was metadata only. It contained no unrestricted portfolio or contact roster.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.slug` | The published-page identifier. |
| `data.kind / family` | The source page classification. |
| `data.h1` | The page's heading as returned by Radar. |
| `data.edition` | A source edition label; it is not a financial reporting period. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Discover a slug, request it exactly, and use kind and family to select the appropriate interface. If the response supplies metadata only, render that as metadata and continue to funding data or the authorized published page for additional research.

Do not claim a page's missing roster is an empty portfolio or that metadata exposes a current verified fund mandate. A successful page lookup proves retrieval, not completeness.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/investor-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
