# Company profile API: identity and available fields

[All endpoints](README.md) · [Workflow guide](../guides/company-data-api.md)

Retrieve a compact company identity by domain. The response keeps the important name, domain, company ID, short description, founding year, employee count and Radar image URL. It lists available detail fields and contact availability without returning their values. Use get_company_field for exactly one rich field per separate JSON POST.

## Route, authentication and credits

**`POST /v1/companies/profile`** · MCP tool **`get_company`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |
| `company_id` | default `null` | string or null; min characters: `1`; max characters: `100`; pattern: `^[A-Za-z0-9_-]+$` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/profile" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"razorpay.com"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company -->
```json
{
  "name": "get_company",
  "arguments": {
    "request": {
      "domain": "razorpay.com"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_company -->
```json
{
  "ok": true,
  "feature": "get_company",
  "data": {
    "company": {
      "company_id": "2gowls1wmc",
      "domain": "razorpay.com",
      "name": "Razorpay",
      "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=razorpay.com",
      "description": "Provider of payment and business banking solutions for enterprises",
      "founded": 2014,
      "employee_count": 1952
    },
    "profile_depth": "summary",
    "available_fields": [
      "overview",
      "classification",
      "people",
      "technology",
      "web_presence",
      "traffic",
      "apps",
      "products",
      "geography",
      "social",
      "lifecycle",
      "legal",
      "assessments",
      "hiring",
      "reputation",
      "share_of_voice"
    ],
    "field_status": {
      "overview": "available",
      "classification": "available",
      "people": "available",
      "technology": "available",
      "web_presence": "available",
      "traffic": "available",
      "apps": "available",
      "products": "available",
      "geography": "available",
      "social": "available",
      "lifecycle": "available",
      "legal": "available",
      "assessments": "available",
      "hiring": "available",
      "innovation": "not_observed",
      "activity": "not_observed",
      "reputation": "available",
      "share_of_voice": "available"
    },
    "contacts": {
      "availability": {
        "emails": true,
        "phones": true
      },
      "path": "/v1/contacts/company",
      "required_scope": "contacts",
      "access": "linked Radar paid-plan check"
    },
    "field_request": {
      "method": "POST",
      "path": "/v1/companies/field",
      "required": [
        "domain",
        "field"
      ]
    },
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "partial": false
    },
    "financial_history": "Use get_financials; financial archive and estimated-revenue access remain upstream-controlled"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:27.254901+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:27.255033+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live Razorpay response contains compact identity and available-field metadata. Its richer classification, founders, seventy technology entries, traffic and app observations are captured through separate field requests in COMPANY_DATA_DEPTH.md. The profile no longer embeds them.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.company` | Compact identity only; no founder roster, technology arrays, traffic or legal archive. |
| `data.available_fields` | Names of observed detail fields, not their values. |
| `data.field_status` | available, not_observed, unavailable or partial for each field. |
| `data.contacts.availability` | Email/phone presence booleans; not contact values or entitlement. |
| `data.field_request` | The separate field endpoint and its required JSON keys. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Find a company, verify its identity, inspect available_fields and field_status, then POST domain and field to /v1/companies/field. Email and phone values use the separate contact endpoints and paid-access checks.

Availability is a stored-data observation. It is not a promise of current facts or contact entitlement. Old sections/item_limit inputs on get_company now return HTTP 422.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
