# Article API: retrieve news text and attribution by article ID

[All endpoints](README.md) · [Workflow guide](../guides/financial-news-api.md)

Retrieve an article whose identifier was returned by an accessible news or company record. Use the article as source evidence in a research interface while retaining attribution and treating its text as untrusted content, not instructions for an agent.

## Route, authentication and credits

**`POST /v1/news/article`** · MCP tool **`get_article`** · key scope **`news`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `article_id` | required | string; pattern: `^[0-9a-fA-F]{24}$` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/news/article" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"article_id":"69e8d5e79baafc7356d34094"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_article -->
```json
{
  "name": "get_article",
  "arguments": {
    "request": {
      "article_id": "69e8d5e79baafc7356d34094"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

**Current availability:** the 2026-09-23 probe returned HTTP 503 (`coverage_unavailable`). The successful response below is historical. See the [current output audit](../OUTPUT_DEPTH_AUDIT.md).

<!-- response-example: get_article -->
```json
{
  "ok": true,
  "feature": "get_article",
  "data": {
    "article": {
      "id": "69e8d5e79baafc7356d34094",
      "headline": "A Look Back at Vertical Software Stocks’ Q4 Earnings: Toast (NYSE:TOST) Vs The Rest Of The Pack",
      "url": "https://www.theglobeandmail.com/investing/markets/stocks/TOST/pressreleases/1288588/a-look-back-at-vertical-software-stocks-q4-earnings-toast-nysetost-vs-the-rest-of-the-pack/",
      "publisher": "theglobeandmail.com",
      "published_at": "2026-04-13T22:37:00",
      "sentiment": {
        "label": "slight_pos",
        "score": 0.41,
        "group": "positive"
      },
      "priority": 7,
      "classes": [
        {
          "code": 0,
          "path": "/News/Business News/Company News",
          "score": 0.63
        }
      ],
      "country": "united states",
      "organizations": [
        "tost",
        "q4"
      ],
      "people": [],
      "body_chars": 5891,
      "authors": [
        "Stockstory -"
      ],
      "top_image": "https://www.theglobeandmail.com/pf/resources/assets/meta/apple-touch-icon.png?d=877",
      "publish_date": null,
      "language": "en"
    },
    "charged_exports": 1
  },
  "window": {
    "published_at": "2026-04-13T22:37:00",
    "data_through": "2026-08-24",
    "freshness": "volume thins after 2026-05; the last months are partial"
  },
  "meta": {
    "retrieved_at": "2026-09-20T10:58:51.154237+00:00",
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
**2026-09-20T10:58:51.154421+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_article.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

**Capture method:** Executed authenticated local Radar gateway and actual Prism News application code against live data; isolated test identity and quota dependencies, with the News Free plan's data limits retained. No deployed News URL, production News-key authentication or customer billing was verified.

The captured response was executed through the real gateway and News application against live data, with an isolated test identity and quota dependencies. It verifies data retrieval, not a deployed News URL, production key authentication or customer billing. This article ID came from the successful software earnings search. Retrieval returned HTTP 200 and a 5,891-character body plus source metadata. Documentation omits the full body, lede and description while retaining the headline, source URL, body_chars, attribution and classification. charged_exports=1 is the operation's returned export count; this isolated capture did not charge a customer.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data when connected` | article text, source and attribution fields supplied by the connected News API |
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

Use an article_id actually returned by a prior request; it must contain 24 hexadecimal characters. Check the connected News account's access before retrieving text. Store the source URL and reporting date separately from your retrieval timestamp.

The example is a historical query, not a current news feed. Read each dataset's data_through and freshness values. Configure both News service URLs and link an authorized News key for normal use; local integration identities never enter the deployed gateway. Search-engine results are not API responses.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/financial-news-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
