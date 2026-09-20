# Investor directory API: published profiles, lists and locations

[All endpoints](README.md) · [Workflow guide](../guides/investor-data-api.md)

Discover published investor pages without guessing URL slugs. The directory includes page counts and selected profiles, lists, cities and sectors. It is particularly useful when an application needs navigable investor research pages rather than a free-form company query.

## Route, authentication and credits

**`POST /v1/investors/directory`** · MCP tool **`investor_directory`** · key scope **`investors`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

This operation accepts an empty JSON object: `{}`.

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/investors/directory" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: investor_directory -->
```json
{
  "name": "investor_directory",
  "arguments": {
    "request": {}
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: investor_directory -->
```json
{
  "ok": true,
  "feature": "investor_directory",
  "data": {
    "counts": {
      "investor_list": 7589,
      "investor_list_angel": 1450,
      "investor_profile": 5269
    },
    "top_lists": [
      {
        "slug": "fintech-investors-in-london",
        "city_display": "London",
        "companies": 1235,
        "family": "investors",
        "h1": "FinTech investors in London",
        "investors": 3878,
        "sector_display": "FinTech",
        "usd": 216769236909
      },
      {
        "slug": "fintech-investors-in-new-york-city",
        "city_display": "New York City",
        "companies": 1062,
        "family": "investors",
        "h1": "FinTech investors in New York City",
        "investors": 3425,
        "sector_display": "FinTech",
        "usd": 289019143774
      }
    ],
    "top_angel_lists": [
      {
        "slug": "b2c-e-commerce-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 407,
        "family": "angel_investors",
        "h1": "B2C E-Commerce angel investors in Bengaluru",
        "investors": 4750,
        "sector_display": "B2C E-Commerce",
        "usd": 50146513809
      },
      {
        "slug": "retail-tech-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 365,
        "family": "angel_investors",
        "h1": "Retail Tech angel investors in Bengaluru",
        "investors": 4438,
        "sector_display": "Retail Tech",
        "usd": 37764196690
      }
    ],
    "top_profiles": [
      {
        "slug": "anupam-mittal",
        "family": "investor",
        "h1": "Anupam Mittal",
        "usd": 263435545
      },
      {
        "slug": "kunal-bahl",
        "family": "investor",
        "h1": "Kunal Bahl",
        "usd": 1395040786
      }
    ],
    "cities": [
      {
        "name": "San Francisco",
        "pages": 619,
        "investors": 3476
      },
      {
        "name": "London",
        "pages": 448,
        "investors": 3878
      }
    ],
    "sectors": [
      {
        "name": "Life Sciences",
        "pages": 227,
        "investors": 1650
      },
      {
        "name": "FinTech",
        "pages": 184,
        "investors": 5456
      }
    ]
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:59:07.175811+00:00",
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
The [downloadable JSON example](../examples/investor_directory.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The live directory supplied anupam-mittal as a profile slug. That returned identifier was used for the separate successful investor-page capture. The source also returned counts for investor lists, angel lists and profiles; those categories should not be summed into a unique-investor estimate.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.counts` | Published-page counts by source category, not necessarily unique investor entities. |
| `data.top_profiles[].slug` | The identifier to use in the investor-page request. |
| `data.top_lists / top_angel_lists` | Published list references when available. |
| `data.cities / sectors` | Navigation categories with source counts that can overlap. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Request the directory with an empty JSON body, select a returned slug and pass it to get_investor_page. Keep the record's family or kind so your application can distinguish an investor profile from a curated list. Do not construct slugs by lowercasing a display name.

Directory metadata may be available even when the detailed roster behind a published page has another access gate. Do not imply that every directory entry includes an unrestricted investor dataset.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/investor-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
