# Company enrichment API: legal, digital and reputation data

[All endpoints](README.md) · [Workflow guide](../guides/company-enrichment-api.md)

Add context to an existing company domain using available legal registrations, digital audience information, reputation summaries and share-of-voice data. These sections come from different source processes and should not be presented as if all were measured on the same date.

## Route, authentication and credits

**`POST /v1/companies/enrichment`** · MCP tool **`get_company_enrichment`** · key scope **`companies`**.
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
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/enrichment" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_enrichment -->
```json
{
  "name": "get_company_enrichment",
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

<!-- response-example: get_company_enrichment -->
```json
{
  "ok": true,
  "feature": "get_company_enrichment",
  "data": {
    "digital": {
      "authority": 100,
      "global_rank": 26,
      "visits": 1222875095,
      "visits_date": "2026-05-01"
    },
    "domain": "microsoft.com",
    "has_data": true,
    "legal": [
      {
        "country": "United States",
        "id_no": "2357303",
        "legal_name": "Microsoft Corporation",
        "registry": "Others"
      },
      {
        "country": "Latvia",
        "id_no": "40203171831",
        "legal_name": "BI Partners",
        "registry": "ur.gov.lv"
      }
    ],
    "reputation": {
      "category": "Electronics & Technology",
      "n": 3789,
      "n_12m": 1062,
      "score": 1.2,
      "stars": 1
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:46.234462+00:00",
    "partial": false,
    "notes": [
      "Absent enrichment sections have unknown coverage; the source does not distinguish missing data from a failed section."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_enrichment.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The Microsoft capture returned a Microsoft Corporation legal record and digital observations dated in May 2026. That legal name differed from the product label in the profile example. Reputation text and individual reviews are deliberately omitted from the documentation excerpt; aggregate fields remain captured values.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.has_data` | Some enrichment exists; this is not a completeness certificate. |
| `data.legal` | Available legal names and registry identifiers, which can help review domain-identity ambiguity. |
| `data.digital.visits / visits_date` | Traffic observation and its source period; not company revenue or customer count. |
| `data.reputation.score / n` | A source-specific score and review count, not a gateway quality guarantee. |
| `data.sov` | Available comparison context whose denominator depends on the source cohort. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Retrieve the base company profile, then inspect enrichment sections relevant to your use case. Preserve section dates, units and source categories. Map known values into your account model; leave existing data intact when a section is missing or its coverage is unknown.

The source does not always distinguish a missing section from a failed enrichment subsection. Do not interpret an omitted legal, reputation or digital field as proof of nonexistence.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-enrichment-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
