# Location intelligence API: business context by geography

[All endpoints](README.md) · [Workflow guide](../guides/b2b-data-api.md)

Request Radar's existing analytical context for a named geography. The location_type tells the source whether the name is a city, state, country or country code. This endpoint is a specific geographical-research request, not arbitrary SQL or a general report-generation job.

## Route, authentication and credits

**`POST /v1/locations/intelligence`** · MCP tool **`location_intelligence`** · key scope **`locations`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `location` | required | string; min characters: `1`; max characters: `200` |
| `location_type` | default `"country"` | string; one of `city`, `state`, `country`, `cc` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/locations/intelligence" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"location":"India","location_type":"country"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: location_intelligence -->
```json
{
  "name": "location_intelligence",
  "arguments": {
    "request": {
      "location": "India",
      "location_type": "country"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: location_intelligence -->
```json
{
  "ok": false,
  "feature": "location_intelligence",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:59:07.413700+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  },
  "error": {
    "kind": "upstream_unavailable",
    "message": "The data service could not complete this request"
  }
}
```

This is the captured **complete response**, HTTP **502**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/location_intelligence.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The India/country live request returned HTTP 502 upstream_unavailable. The documentation includes that actual failure rather than inventing geographic statistics. A future successful response should be captured and reviewed before promising a particular location metric.

## Read the response

| Field | Meaning and handling |
|---|---|
| `location` | The place name supplied to the source. |
| `location_type` | city, state, country or cc; the default is country. |
| `data` | The source analytical payload when available; no universal metric completeness is promised. |
| `error.kind / message` | Explicit source availability failures. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Choose the intended geographic level explicitly. If the source returns data, preserve the geography and the source's definitions before comparing it with another place. Avoid treating similarly named cities or states as interchangeable identifiers.

Do not interpret a service error as zero companies, zero funding or no economic activity in the location. Data availability and the underlying economic quantity are different questions.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/b2b-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
