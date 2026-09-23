# Funding news API: announcements by investor, sector and round

[All endpoints](README.md) · [Workflow guide](../guides/funding-news-api.md)

Search funding-announcement coverage using a topic or company plus optional investor, sector, round type and reported amount. This retrieves news evidence, not a verified cap table or a transaction settlement ledger.

## Route, authentication and credits

**`POST /v1/news/funding`** · MCP tool **`search_funding_news`** · key scope **`news`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `q` | default `null` | string or null; min characters: `2`; max characters: `120` |
| `company` | default `null` | string or null |
| `country` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `date_from` | default `null` | string or null |
| `date_to` | default `null` | string or null |
| `sentiment` | default `null` | string or null; one of `positive`, `neutral`, `negative` |
| `priority_min` | default `null` | integer or null; minimum: `1`; maximum: `9` |
| `limit` | default `100` | integer; minimum: `1`; maximum: `100` |
| `cursor` | default `null` | string or null; max characters: `2048`; pattern: `^[A-Za-z0-9_=+-]+$` |
| `sort` | default `"newest"` | string; one of `newest`, `oldest`, `priority` |
| `investor` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `sector` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `round_type` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `min_amount_usd` | default `null` | number or null; minimum: `0` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/news/funding" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q":"funding","limit":5,"date_from":"2026-04-01","date_to":"2026-04-30"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_funding_news -->
```json
{
  "name": "search_funding_news",
  "arguments": {
    "request": {
      "q": "funding",
      "limit": 5,
      "date_from": "2026-04-01",
      "date_to": "2026-04-30"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: search_funding_news -->
```json
{
  "ok": true,
  "feature": "search_funding_news",
  "data": {
    "items": [
      {
        "id": "2146b783282e70a6",
        "company_name": "Featherless.ai",
        "domain": null,
        "round_type": "Series A",
        "amount_usd": 20000000.0,
        "valuation_usd": null,
        "currency": "USD",
        "amount": 20000000.0,
        "valuation": null,
        "investors": [
          {
            "name": "AMD Ventures",
            "domain": "amdventures.com",
            "amount": null
          },
          {
            "name": "airbus ventures",
            "domain": "airbusventures.vc",
            "amount": null
          },
          {
            "name": "bmw i ventures",
            "domain": "bmwiventures.com",
            "amount": null
          },
          {
            "name": "kickstart ventures",
            "domain": "kickstart.ph",
            "amount": null
          },
          {
            "name": "panache ventures",
            "domain": "panache.vc",
            "amount": null
          },
          {
            "name": "Wavemaker Ventures",
            "domain": null,
            "amount": null
          }
        ],
        "sector": "AI",
        "country": null,
        "city": null,
        "use_of_funds": "Scale global infrastructure, launch a dedicated marketplace for specialized open models, and deepen technical integration with diverse hardware architectures",
        "published_at": "2026-04-30T23:33:54",
        "coverage_count": 1,
        "article_ids": [
          "69f8a6fb43843dd771d249ae"
        ],
        "article_id": "69f8a6fb43843dd771d249ae"
      },
      {
        "id": "760835c67cc74f24",
        "company_name": "Primogene",
        "domain": null,
        "round_type": null,
        "amount_usd": 4800000.0,
        "valuation_usd": null,
        "currency": "USD",
        "amount": 4800000.0,
        "valuation": null,
        "investors": [],
        "sector": null,
        "country": "Germany",
        "city": null,
        "use_of_funds": null,
        "published_at": "2026-04-30T20:35:26",
        "coverage_count": 1,
        "article_ids": [
          "69f8a6d28937ef12fc0ae01e"
        ],
        "article_id": "69f8a6d28937ef12fc0ae01e"
      },
      {
        "id": "291d02119eb021db",
        "company_name": "lafleur",
        "domain": "lafleur.link",
        "round_type": "prepayment financing",
        "amount_usd": 22200000.0,
        "valuation_usd": null,
        "currency": "CAD",
        "amount": 30000000.0,
        "valuation": null,
        "investors": [
          {
            "name": "trafigura",
            "domain": "trafigura.com",
            "amount": null
          }
        ],
        "sector": "gold mining",
        "country": "Canada",
        "city": null,
        "use_of_funds": "restart of Beacon Gold Mill and initial production",
        "published_at": "2026-04-30T19:36:16",
        "coverage_count": 1,
        "article_ids": [
          "69f9dde77b2d589e84521a9e"
        ],
        "article_id": "69f9dde77b2d589e84521a9e"
      },
      {
        "id": "97a3e8634c0623aa",
        "company_name": "koda health",
        "domain": "kodahealthcare.com",
        "round_type": "Series A",
        "amount_usd": 14000000.0,
        "valuation_usd": null,
        "currency": "USD",
        "amount": 14000000.0,
        "valuation": null,
        "investors": [
          {
            "name": "evidenced",
            "domain": "evidenced.app",
            "amount": null
          },
          {
            "name": "Mudita Venture Partners",
            "domain": "muditavp.com",
            "amount": null
          },
          {
            "name": "techstars",
            "domain": "techstars.com",
            "amount": null
          },
          {
            "name": "texas medical center",
            "domain": "texasmedicalcenter.org",
            "amount": null
          },
          {
            "name": "upmc enterprises",
            "domain": "enterprises.upmc.com",
            "amount": null
          }
        ],
        "sector": "Healthcare",
        "country": "USA",
        "city": null,
        "use_of_funds": "Scale operations and expand engineering, clinical strategy and customer success",
        "published_at": "2026-04-30T17:00:01",
        "coverage_count": 1,
        "article_ids": [
          "69f8a62fbbf1d314559a1e89"
        ],
        "article_id": "69f8a62fbbf1d314559a1e89"
      },
      {
        "id": "591d0ae7d74a43f0",
        "company_name": "ebury",
        "domain": "ebury.com",
        "round_type": "Financing",
        "amount_usd": 698500000.0,
        "valuation_usd": null,
        "currency": "GBP",
        "amount": 550000000.0,
        "valuation": null,
        "investors": [
          {
            "name": "centerbridge partners",
            "domain": "centerbridge.com",
            "amount": null
          },
          {
            "name": "santander",
            "domain": "santander.com",
            "amount": 50000000.0
          },
          {
            "name": "vitruvian partners",
            "domain": "vitruvianpartners.com",
            "amount": null
          },
          {
            "name": "83north",
            "domain": "83north.com",
            "amount": null
          }
        ],
        "sector": "Payments",
        "country": null,
        "city": null,
        "use_of_funds": null,
        "published_at": "2026-04-30T11:36:09",
        "coverage_count": 1,
        "article_ids": [
          "69f8947d8937ef12fc0abbc0"
        ],
        "article_id": "69f8947d8937ef12fc0abbc0"
      }
    ],
    "returned": 5,
    "total_estimate": 1085,
    "next_cursor": "eyJ2IjoxLCJ0IjoiZnIiLCJzIjoibmV3ZXN0IiwiZCI6IjIwMjYtMDQtMzAgMTE6MzY6MDkiLCJrIjoiNjQyMTMwMDYzNDU2NTg4Njk2MCJ9",
    "totals": {
      "deals": 1085,
      "deals_with_amount": 953,
      "deals_without_amount": 132,
      "sum_amount_usd": 515844387971.16,
      "median_amount_usd": 13400000.0,
      "largest_amount_usd": 122000000000.0,
      "currency": "USD",
      "note": "Each matched deal record counts once, regardless of how many articles report it. Counts are measured over the entire filtered window, independent of result limits. USD amounts use fixed conversion rates, not current or transaction-date exchange rates. Only finite, positive reported amounts enter sums, medians and maxima. Missing, zero, negative and non-finite amounts count as unknown; amount statistics are null when no matched deal has a usable amount. Reported figures and outliers are retained, not independently verified financial amounts."
    },
    "limit": 5,
    "sort": "newest"
  },
  "window": {
    "since": "2026-04-01",
    "until": "2026-04-30",
    "days": 30,
    "data_through": "2026-05-05",
    "freshness": "this business dataset is available through 2026-05-05; company events, funding and company-linked news may have different latest available dates"
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:51:49.856005+00:00",
    "partial": true,
    "notes": [],
    "provider": "Fliar BI",
    "coverage": {
      "available": false
    }
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:51:49.856193+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_funding_news.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

**Capture method:** Executed authenticated local Radar gateway and actual Prism News application code against live data; isolated test identity and quota dependencies, with the News Free plan's data limits retained. No deployed News URL, production News-key authentication or customer billing was verified.

The captured response was executed through the real gateway and News application against live data, with an isolated test identity and quota dependencies. It verifies data retrieval, not a deployed News URL, production key authentication or customer billing. The April funding query returned five records from 1,085 matching deal records, including company/domain, round, amounts, investors, sector, geography and source article IDs. Of the matched records, 953 contain usable positive amounts and 132 do not. Source totals include large unverified outliers and fixed-rate currency conversions; they are not audited funding statistics.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data when connected` | funding announcement records, reported amount qualifiers and source article references when supplied |
| `window` | Effective source dates and data-through information, not an assurance of complete or current coverage. |
| `meta.coverage / plan / quota` | Relayed when the connected News service provides them. |
| `error.kind=service_unavailable` | The gateway has no configured connection for this operation. |
| `error.kind=access_required` | A linked News key is missing or the upstream account rejects access. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Supply q or company, use explicit dates for a historical investigation, and check the returned coverage before interpreting results. For cursor-based searches, send the returned cursor unchanged with the same filters. Overview, trend and sentiment operations use their own analysis models rather than headline pagination.

The example is a historical query, not a current news feed. Read each dataset's data_through and freshness values. Configure both News service URLs and link an authorized News key for normal use; local integration identities never enter the deployed gateway. Search-engine results are not API responses.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/funding-news-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
