# News sentiment API: company tone distributions over time

[All endpoints](README.md) · [Workflow guide](../guides/financial-news-api.md)

Retrieve the source's sentiment distribution and timeline for a company or topic. Sentiment is a derived classification of observed content, not a factual determination that a business is performing well or badly.

## Route, authentication and credits

**`POST /v1/news/sentiment`** · MCP tool **`news_sentiment`** · key scope **`news`**.
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
| `granularity` | default `"weekly"` | string; one of `daily`, `weekly`, `monthly` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/news/sentiment" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"company":"microsoft.com","granularity":"weekly","date_from":"2026-04-01","date_to":"2026-04-30"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: news_sentiment -->
```json
{
  "name": "news_sentiment",
  "arguments": {
    "request": {
      "company": "microsoft.com",
      "granularity": "weekly",
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

<!-- response-example: news_sentiment -->
```json
{
  "ok": true,
  "feature": "news_sentiment",
  "data": {
    "matched": 4401,
    "carrying": 4401,
    "carrier_share_pct": 100.0,
    "labels": [
      {
        "label": "extreme_neg",
        "group": "negative",
        "count": 8,
        "share": 0.18
      },
      {
        "label": "very_neg",
        "group": "negative",
        "count": 175,
        "share": 3.98
      },
      {
        "label": "fair_neg",
        "group": "negative",
        "count": 11,
        "share": 0.25
      },
      {
        "label": "slight_neg",
        "group": "negative",
        "count": 947,
        "share": 21.52
      },
      {
        "label": "none",
        "group": "neutral",
        "count": 43,
        "share": 0.98
      },
      {
        "label": "slight_pos",
        "group": "positive",
        "count": 1555,
        "share": 35.33
      },
      {
        "label": "fair_pos",
        "group": "positive",
        "count": 249,
        "share": 5.66
      },
      {
        "label": "very_pos",
        "group": "positive",
        "count": 1383,
        "share": 31.42
      },
      {
        "label": "extreme_pos",
        "group": "positive",
        "count": 30,
        "share": 0.68
      }
    ],
    "groups": [
      {
        "group": "negative",
        "count": 1141,
        "share": 25.93
      },
      {
        "group": "neutral",
        "count": 43,
        "share": 0.98
      },
      {
        "group": "positive",
        "count": 3217,
        "share": 73.1
      }
    ],
    "negative_to_positive_ratio": 0.355,
    "baseline": {
      "since": "2026-07-26",
      "until": "2026-08-24",
      "days": 30,
      "articles": 14930,
      "carrying": 14893,
      "note": "Archive comparison over the 30 days ending at data_through",
      "groups": {
        "negative": {
          "count": 6055,
          "share": 40.66
        },
        "neutral": {
          "count": 671,
          "share": 4.51
        },
        "positive": {
          "count": 8167,
          "share": 54.84
        }
      },
      "negative_to_positive_ratio": 0.741
    },
    "vs_baseline_ratio": 0.48,
    "granularity": "weekly",
    "timeline": [
      {
        "period": "2026-03-30",
        "total": 516,
        "negative": 118,
        "neutral": 6,
        "positive": 392,
        "negative_share": 22.87,
        "positive_share": 75.97,
        "labels": {
          "extreme_neg": 0,
          "very_neg": 38,
          "fair_neg": 2,
          "slight_neg": 78,
          "none": 6,
          "slight_pos": 214,
          "fair_pos": 40,
          "very_pos": 134,
          "extreme_pos": 4
        },
        "partial_period": true
      },
      {
        "period": "2026-04-06",
        "total": 1144,
        "negative": 272,
        "neutral": 22,
        "positive": 850,
        "negative_share": 23.78,
        "positive_share": 74.3,
        "labels": {
          "extreme_neg": 0,
          "very_neg": 29,
          "fair_neg": 5,
          "slight_neg": 238,
          "none": 22,
          "slight_pos": 409,
          "fair_pos": 55,
          "very_pos": 379,
          "extreme_pos": 7
        },
        "partial_period": false
      },
      {
        "period": "2026-04-13",
        "total": 975,
        "negative": 187,
        "neutral": 8,
        "positive": 780,
        "negative_share": 19.18,
        "positive_share": 80.0,
        "labels": {
          "extreme_neg": 6,
          "very_neg": 27,
          "fair_neg": 2,
          "slight_neg": 152,
          "none": 8,
          "slight_pos": 336,
          "fair_pos": 76,
          "very_pos": 362,
          "extreme_pos": 6
        },
        "partial_period": false
      },
      {
        "period": "2026-04-20",
        "total": 905,
        "negative": 247,
        "neutral": 2,
        "positive": 656,
        "negative_share": 27.29,
        "positive_share": 72.49,
        "labels": {
          "extreme_neg": 2,
          "very_neg": 51,
          "fair_neg": 2,
          "slight_neg": 192,
          "none": 2,
          "slight_pos": 300,
          "fair_pos": 46,
          "very_pos": 301,
          "extreme_pos": 9
        },
        "partial_period": false
      },
      {
        "period": "2026-04-27",
        "total": 861,
        "negative": 317,
        "neutral": 5,
        "positive": 539,
        "negative_share": 36.82,
        "positive_share": 62.6,
        "labels": {
          "extreme_neg": 0,
          "very_neg": 30,
          "fair_neg": 0,
          "slight_neg": 287,
          "none": 5,
          "slight_pos": 296,
          "fair_pos": 32,
          "very_pos": 207,
          "extreme_pos": 4
        },
        "partial_period": true
      }
    ]
  },
  "window": {
    "since": "2026-04-01",
    "until": "2026-04-30",
    "days": 30,
    "data_through": "2026-08-24",
    "freshness": "volume thins after 2026-05; the last months are partial",
    "granularity": "weekly"
  },
  "meta": {
    "retrieved_at": "2026-09-20T10:58:50.836087+00:00",
    "partial": false,
    "notes": [
      "shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)"
    ],
    "provider": "Fliar BI",
    "coverage": {
      "available": true
    }
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-20T10:58:50.836251+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/news_sentiment.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

**Capture method:** Executed authenticated local Radar gateway and actual Prism News application code against live data; isolated test identity and quota dependencies, with the News Free plan's data limits retained. No deployed News URL, production News-key authentication or customer billing was verified.

The captured response was executed through the real gateway and News application against live data, with an isolated test identity and quota dependencies. It verifies data retrieval, not a deployed News URL, production key authentication or customer billing. The Microsoft analysis matched 4,401 April articles and returned label/group counts, baseline comparisons and a weekly timeline. Preserve the source denominator and baseline window when interpreting percentages or ratios.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data when connected` | source sentiment categories, timelines and coverage when supplied |
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

Continue with the [workflow guide](../guides/financial-news-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
