# Company contact API: request business emails or phone numbers

[All endpoints](README.md) · [Workflow guide](../guides/company-email-phone-api.md)

Retrieve only explicitly requested emails and/or phone numbers for one company. An explicit contacts key scope and an entitled linked Radar account are required; a wildcard key alone does not grant contact access.

## Route, authentication and credits

**`POST /v1/contacts/company`** · MCP tool **`get_company_contacts`** · key scope **`contacts`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |
| `fields` | required | array of string; min items: `1`; max items: `2`; one of `emails`, `phones` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

`RADAR_API_URL` is `https://radar-api.fliarbi.com` (the [installer](../../README.md#install-in-one-line) sets it);
load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/contacts/company" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"razorpay.com","fields":["emails"]}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_contacts -->
```json
{
  "name": "get_company_contacts",
  "arguments": {
    "request": {
      "domain": "razorpay.com",
      "fields": [
        "emails"
      ]
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_company_contacts -->
```json
{
  "ok": false,
  "feature": "get_company_contacts",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:59.312096+00:00",
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
**2026-09-23T06:47:59.312198+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_contacts.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The default preview key is deliberately denied with scope_required. This is an access-control capture, not a service outage. Successful response-shape tests use synthetic example.com contacts; no production paid-contact retrieval is claimed.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.domain` | Requested company domain. |
| `data.emails / phones` | Only the requested contact types, each bounded to twenty-five source values. |
| `data.contact_source` | company_domain: business contacts, not an inferred person-specific address. |
| `data.available` | At least one requested contact type was supplied. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Resolve the company domain, then select emails, phones or both explicitly. For LinkedIn and other company social references, use get_company_field with field=social. For individual professional contacts, discover and accept a professional ID before using get_person_contacts.

Company association does not identify the mailbox owner, department, work-email verification or phone line type. Successful empty lookups cost one API credit in account mode; source errors can sometimes appear as empty arrays. There is no contact-array pagination or source-total count.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-email-phone-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
