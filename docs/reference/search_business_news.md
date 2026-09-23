# Business news API: company-associated financial reporting

[All endpoints](README.md) · [Workflow guide](../guides/financial-news-api.md)

Retrieve headlines associated with a company domain or business topic. This is the news side of a company-research workflow, separate from structured financial statements and company-event summaries.

## Route, authentication and credits

**`POST /v1/news/business`** · MCP tool **`search_business_news`** · key scope **`news`**.
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

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/news/business" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"company":"microsoft.com","limit":5,"date_from":"2026-04-01","date_to":"2026-04-30"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_business_news -->
```json
{
  "name": "search_business_news",
  "arguments": {
    "request": {
      "company": "microsoft.com",
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

**Current availability:** the 2026-09-23 probe returned HTTP 503 (`coverage_unavailable`). The successful response below is historical. See the [current output audit](../OUTPUT_DEPTH_AUDIT.md).

<!-- response-example: search_business_news -->
```json
{
  "ok": true,
  "feature": "search_business_news",
  "data": {
    "items": [
      {
        "id": "69f8a8738937ef12fc0af47a",
        "headline": "Apple earning beat forecasts on iPhone 17 demand",
        "url": "http://gulfnews.com/technology/apple-earnings-beat-forecasts-on-iphone-17-demand-1.500525225",
        "publisher": "gulfnews.com",
        "published_at": "2026-04-30T23:58:26",
        "sentiment": {
          "label": "very_pos",
          "score": 0.55,
          "group": "positive"
        },
        "priority": 8,
        "classes": [
          {
            "code": 0,
            "path": "/News/Business News/Company News",
            "score": 0.68
          }
        ],
        "country": "united states",
        "organizations": [],
        "people": [],
        "events": []
      },
      {
        "id": "69f880568937ef12fc06ffef",
        "headline": "Top AI Stocks to Buy in the US 2026 for Long-Term Growth",
        "url": "https://www.analyticsinsight.net/stocks/top-ai-stocks-to-buy-in-the-us-2026-for-long-term-growth",
        "publisher": "analyticsinsight.net",
        "published_at": "2026-04-30T23:30:00",
        "sentiment": {
          "label": "slight_pos",
          "score": 0.43,
          "group": "positive"
        },
        "priority": 8,
        "classes": [
          {
            "code": 76,
            "path": "/Science/Computer Science/Machine Learning & Artificial Intelligence",
            "score": 0.77
          },
          {
            "code": 5,
            "path": "/News/Business News/Financial Markets News",
            "score": 0.55
          },
          {
            "code": 9,
            "path": "/News/Technology News",
            "score": 0.49
          },
          {
            "code": 14,
            "path": "/Finance/Investing/Stocks & Bonds",
            "score": 0.48
          }
        ],
        "country": "united states",
        "organizations": [
          "intel",
          "microsoft"
        ],
        "people": [],
        "events": []
      },
      {
        "id": "69f87fbabbf1d3145595d159",
        "headline": "Anthropic Valuation Soars to $900B in Explosive AI Funding Round Closing Within Two Weeks",
        "url": "https://bitcoinworld.co.in/anthropic-valuation-ai-funding-round/",
        "publisher": "bitcoinworld.co.in",
        "published_at": "2026-04-30T23:25:11",
        "sentiment": {
          "label": "slight_pos",
          "score": 0.37,
          "group": "positive"
        },
        "priority": 7,
        "classes": [
          {
            "code": 55,
            "path": "/Business & Industrial/Business Finance/Venture Capital",
            "score": 0.54
          },
          {
            "code": 0,
            "path": "/News/Business News/Company News",
            "score": 0.51
          }
        ],
        "country": null,
        "organizations": [
          "claude"
        ],
        "people": [],
        "events": []
      },
      {
        "id": "69f8b438bbf1d314559a8f3b",
        "headline": "Breitbart Business Digest: The Best Month for Stocks in Five Years",
        "url": "https://www.breitbart.com/economy/2026/04/30/breitbart-business-digest-the-best-month-for-stocks-in-five-years/",
        "publisher": "breitbart.com",
        "published_at": "2026-04-30T23:03:55",
        "sentiment": {
          "label": "slight_pos",
          "score": 0.38,
          "group": "positive"
        },
        "priority": 6,
        "classes": [
          {
            "code": 5,
            "path": "/News/Business News/Financial Markets News",
            "score": 0.72
          },
          {
            "code": 14,
            "path": "/Finance/Investing/Stocks & Bonds",
            "score": 0.57
          }
        ],
        "country": "united states",
        "organizations": [],
        "people": [],
        "events": []
      },
      {
        "id": "69f880adbbf1d31455966a69",
        "headline": "Here's Why This Remains My Least Favorite \"Magnificent Seven\" Stock -- Even After a Strong Earnings Report | The Motley Fool",
        "url": "https://www.fool.com/investing/2026/04/30/heres-why-this-remains-my-least-favorite-magnifice/",
        "publisher": "fool.com",
        "published_at": "2026-04-30T22:16:00",
        "sentiment": {
          "label": "slight_pos",
          "score": 0.58,
          "group": "positive"
        },
        "priority": 8,
        "classes": [
          {
            "code": 0,
            "path": "/News/Business News/Company News",
            "score": 0.61
          }
        ],
        "country": "united states",
        "organizations": [
          "microsoft"
        ],
        "people": [],
        "events": [
          {
            "event_type": "earnings",
            "domain": "microsoft.com",
            "role": "primary"
          }
        ]
      }
    ],
    "returned": 5,
    "total_estimate": 4401,
    "next_cursor": "eyJ2IjoxLCJzIjoibmV3ZXN0IiwiZCI6IjIwMjYtMDQtMzAgMjI6MTY6MDAiLCJpIjoiNjlmODgwYWRiYmYxZDMxNDU1OTY2YTY5In0",
    "unresolved": 0,
    "duplicates_dropped": 0,
    "limit": 5,
    "sort": "newest",
    "with_events": 1
  },
  "window": {
    "since": "2026-04-01",
    "until": "2026-04-30",
    "days": 30,
    "data_through": "2026-08-24",
    "freshness": "volume thins after 2026-05; the last months are partial"
  },
  "meta": {
    "retrieved_at": "2026-09-20T10:58:50.369681+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI",
    "coverage": {
      "available": true
    }
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T10:58:50.370012+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_business_news.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

**Capture method:** Executed authenticated local Radar gateway and actual Prism News application code against live data; isolated test identity and quota dependencies, with the News Free plan's data limits retained. No deployed News URL, production News-key authentication or customer billing was verified.

The captured response was executed through the real gateway and News application against live data, with an isolated test identity and quota dependencies. It verifies data retrieval, not a deployed News URL, production key authentication or customer billing. Microsoft's April 2026 query returned five items from 4,401 matches, with an opaque next_cursor, source URLs, classifications and associated events. The source's latest news date is 2026-08-24, with a separate warning about thinner recent ingestion.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data when connected` | company-associated headline records, source references and opaque cursor pagination when supplied |
| `window` | Effective source dates and data-through information, not an assurance of complete or current coverage. |
| `meta.coverage / plan / quota` | Relayed when the connected News service provides them. |
| `error.kind=service_unavailable` | The gateway has no configured connection for this operation. |
| `error.kind=access_required` | A linked News key is missing or the upstream account rejects access. |
| `data.items[].id / headline / url / publisher / published_at` | Article identity, short source title, attribution and reporting date; separate from retrieval time. |
| `data.items[].sentiment / priority / classes` | Derived labels and scores; classification paths and codes retain the source's taxonomy. |
| `data.items[].organizations / people / country` | Entities and location labels observed in the article; not proof of corporate ownership or residence. |
| `data.returned / total_estimate / limit` | Delivered page length, matching source count and requested page ceiling are distinct. |
| `data.next_cursor / unresolved / duplicates_dropped` | Continue with the opaque cursor and unchanged filters; missing article records and deduplicated URLs can shorten a page. |

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

Continue with the [workflow guide](../guides/financial-news-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
