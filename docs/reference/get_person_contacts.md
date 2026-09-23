# Professional contact API: email and phone lookup by person ID

[All endpoints](README.md) · [Workflow guide](../guides/founder-contact-data-api.md)

Use the person ID returned by search_people to request only emails and/or phones. The source prefers person-level records and can fall back to the current company’s business contacts. Explicit contacts scope and paid Radar access apply.

## Route, authentication and credits

**`POST /v1/contacts/person`** · MCP tool **`get_person_contacts`** · key scope **`contacts`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `person_id` | required | string; pattern: `^[A-Za-z0-9_-]{1,100}$` |
| `fields` | required | array of string; min items: `1`; max items: `2`; one of `emails`, `phones` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/contacts/person" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"person_id":"example-person-id","fields":["phones"]}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_person_contacts -->
```json
{
  "name": "get_person_contacts",
  "arguments": {
    "request": {
      "person_id": "example-person-id",
      "fields": [
        "phones"
      ]
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_person_contacts -->
```json
{
  "ok": false,
  "feature": "get_person_contacts",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:59.317954+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  },
  "error": {
    "kind": "scope_required",
    "message": "Create a key with the explicit contacts scope for contact retrieval"
  }
}
```

This is the captured **complete response**, HTTP **403**, from
**2026-09-23T06:47:59.318056+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_person_contacts.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The default preview key returns scope_required before contacting the source. Synthetic tests cover paid source responses, requested-field filtering and company-domain fallback. No live private contact values are published in these examples.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.person_id` | ID returned by professional search; do not use a company public ID. |
| `data.emails / phones` | Requested contact types only. |
| `data.contact_source` | person, company_domain, none or unknown; company fallback is never relabeled as personal. |
| `data.available` | Whether a requested value was supplied; not deliverability verification. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Read company founder names, then compare a professional candidate by name, exact recorded company domain and LinkedIn reference. Use only the accepted person ID. Professional founder-role tags can disagree with company founder records; preserve ambiguous or missing joins. Request emails and/or phones separately from discovery.

Company fallback happens only when both person email and phone are absent. A person phone can prevent fallback on an empty email-only request. The person origin label is not a verified-work-email classification; no server-side fallback toggle, email-type filter or deliverability check is exposed.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/founder-contact-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
