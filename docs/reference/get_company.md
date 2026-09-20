# Company profile API: look up company data by domain

[All endpoints](README.md) · [Workflow guide](../guides/company-data-api.md)

Retrieve a company card after selecting a website domain. This endpoint supplies the identity context for an account page: the name used by Radar, the domain, available founding and size fields, location and classification. It does not return a legal-entity guarantee or all subsidiaries associated with a domain.

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
  -d '{"domain":"microsoft.com"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company -->
```json
{
  "name": "get_company",
  "arguments": {
    "request": {
      "domain": "microsoft.com"
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
      "location": {
        "c": "united states",
        "cc": "",
        "coord": [
          -122.12151,
          47.67399
        ],
        "g": "47.67399,-122.12151",
        "hq": "redmond",
        "l": "redmond",
        "lc": "redmond, washington, united states",
        "rg": "washington"
      },
      "size": "",
      "founded": "2003",
      "company_id": "58edbbfde4b053044e6a387d",
      "name": "Microsoft Dynamics CRM",
      "domain": "microsoft.com"
    },
    "access": {
      "anonymous": true,
      "plan": "free",
      "results_per_query": 50,
      "searches_per_month": 50
    },
    "extras_gated": true
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:45.936850+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The microsoft.com request returned the label Microsoft Dynamics CRM, rather than a normalized Microsoft Corporation parent profile. This is an observed identity ambiguity, not a spelling correction made for the example. The accompanying enrichment endpoint returned a Microsoft Corporation legal record. Review such disagreements before joining a corporate group, product profile and filing series.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.company.name / domain` | The actual matched label and domain. Check both, not the domain alone. |
| `data.company.company_id` | Radar's record identifier; do not assume the same type across all source records. |
| `data.company.location` | Source location fields may contain abbreviated country, region, locality and display-location keys. |
| `data.access` | The captured account's anonymous or signed-in access context. |
| `data.extras_gated` | Additional profile attributes may be restricted. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Search for candidates first if you only know a name. Retrieve the profile, compare its returned name and description with the business you intend, and consult enrichment for available legal identity. Only then join financial and news records into a named company brief.

A domain may be shared by a corporate parent, product or division. Do not overwrite an independently verified legal name solely because a domain lookup returned another label.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
