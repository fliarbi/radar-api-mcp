# Competitor discovery API: companies grouped by funding stage

[All endpoints](README.md) · [Workflow guide](../guides/competitor-intelligence-api.md)

Find candidate peer companies for a named market, optionally narrowed by business model. The source groups returned companies by funding stage. This is market discovery, not a verified competitive-ranking model or a list centered on an input company domain.

## Route, authentication and credits

**`POST /v1/companies/competitors`** · MCP tool **`find_competitors`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `market` | required | string; min characters: `1`; max characters: `200` |
| `business_model` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `per_stage` | default `5` | integer; minimum: `3`; maximum: `10` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/competitors" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"market":"Payments","per_stage":3}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: find_competitors -->
```json
{
  "name": "find_competitors",
  "arguments": {
    "request": {
      "market": "Payments",
      "per_stage": 3
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: find_competitors -->
```json
{
  "ok": true,
  "feature": "find_competitors",
  "data": {
    "market": "Payments",
    "summary": {
      "country": {
        "australia": 2,
        "brazil": 2,
        "china": 5,
        "india": 7,
        "indonesia": 2,
        "japan": 3,
        "mexico": 2,
        "south korea": 2,
        "united kingdom": 4,
        "united states": 10
      },
      "stage": {
        "acqui-hired": 3,
        "acquired": 3,
        "deadpooled": 3,
        "early stage": 3,
        "funding raised": 3,
        "late stage": 3,
        "private": 3,
        "public": 3,
        "seed": 3,
        "series a": 3,
        "series b": 3,
        "series c": 3,
        "series d": 3,
        "series e": 3,
        "series f": 3,
        "series g": 3,
        "series i": 1,
        "unfunded": 3
      },
      "total": 52
    },
    "companies": {
      "Public": [
        {
          "location": "tokyo",
          "funding": "",
          "company_id": "cb_org_07a6e52d-6b2c-2519-ea0f-04c62cde44bc",
          "slug": "rakuten",
          "domain": "global.rakuten.com",
          "description": "Rakuten is a provider of e-commerce, fintech, digital content, and communications products and services.",
          "size_label": "super giant",
          "name": "rakuten",
          "progress_label": ""
        },
        {
          "location": "chiyoda city",
          "funding": "",
          "company_id": "5c8091afaa3d79117ea5929d",
          "slug": "paypay",
          "domain": "paypay.ne.jp",
          "description": "Provider of a platform for cashless payments via QR codes",
          "size_label": "",
          "name": "PayPay",
          "progress_label": ""
        },
        {
          "location": "united states",
          "funding": "",
          "company_id": "52c24ac1e4b0dafe9baa6022",
          "slug": "paypal",
          "domain": "paypal.com",
          "description": "Provider of online payment solutions, money transfers, and virtual wallets",
          "size_label": "super giant",
          "name": "PayPal",
          "progress_label": ""
        }
      ],
      "Seed": [
        {
          "location": "setagaya",
          "funding": "",
          "company_id": "531ab811e4b0f7e1661627d9",
          "slug": "rakuten card",
          "domain": "rakuten-card.co.jp",
          "description": "Debit card from Rakuten",
          "size_label": "",
          "name": "Rakuten Card",
          "progress_label": ""
        },
        {
          "location": "fortaleza",
          "funding": "",
          "company_id": "5319a0a2e4b0f7e165fcb220",
          "slug": "fortbrasil",
          "domain": "fortbrasil.com.br",
          "description": "Prepaid payment card solutions for individuals",
          "size_label": "very large",
          "name": "FortBrasil",
          "progress_label": ""
        },
        {
          "location": "ankara",
          "funding": "",
          "company_id": "55bf29b4e4b064e369edae66",
          "slug": "param",
          "domain": "param.com.tr",
          "description": "Virtual POS and prepaid cards for individuals and businesses",
          "size_label": "large",
          "name": "Param",
          "progress_label": ""
        }
      ],
      "Series A": [
        {
          "location": "moscow",
          "funding": "",
          "company_id": "531b2c7ce4b0f7e166227035",
          "slug": "ubank",
          "domain": "ubank.ru",
          "description": "Provider of a modular banking platform for online financial services",
          "size_label": "",
          "name": "Ubank",
          "progress_label": ""
        },
        {
          "location": "kuala lumpur",
          "funding": "",
          "company_id": "5bdbc8fce4b0d8eee54fc1d3",
          "slug": "tng digital",
          "domain": "tngdigital.com.my",
          "description": "App-based mobile wallet",
          "size_label": "medium-large",
          "name": "TNG Digital",
          "progress_label": ""
        },
        {
          "location": "atlanta",
          "funding": "",
          "company_id": "5a343d35e4b0a2a93419202c",
          "slug": "parkmobile",
          "domain": "parkmobile.io",
          "description": "App-based platform for booking parking spaces",
          "size_label": "large",
          "name": "Parkmobile",
          "progress_label": ""
        }
      ],
      "Series B": [
        {
          "location": "singapore",
          "funding": "",
          "company_id": "5efb3033e3c5d215f47d8a91",
          "slug": "atome",
          "domain": "atome.sg",
          "description": "Online marketplace offering multi-category products on purchase finance",
          "size_label": "large",
          "name": "Atome",
          "progress_label": ""
        },
        {
          "location": "depok",
          "funding": "",
          "company_id": "576aa31de4b018faefabea6e",
          "slug": "flip",
          "domain": "flip.id",
          "description": "App-based wallet for consumers and businesses",
          "size_label": "medium-large",
          "name": "Flip",
          "progress_label": ""
        },
        {
          "location": "cuauhtemoc",
          "funding": "",
          "company_id": "531c4f11e4b0f7e16646939b",
          "slug": "clara",
          "domain": "clara.com",
          "description": "An end-to-end corporate payment solution for companies",
          "size_label": "medium-large",
          "name": "Clara",
          "progress_label": ""
        }
      ],
      "Series C": [
        {
          "location": "hangzhou",
          "funding": "",
          "company_id": "540488eae4b0e52937944099",
          "slug": "51 credit card",
          "domain": "u51.com",
          "description": "Credit card bill management tool for consumers",
          "size_label": "medium-large",
          "name": "51 Credit Card",
          "progress_label": ""
        },
        {
          "location": "lagos",
          "funding": "",
          "company_id": "5da1e40a6810c45989319b5e",
          "slug": "opay",
          "domain": "opayweb.com",
          "description": "Provider of financial services including transfers, bill payments, and debit cards",
          "size_label": "very large",
          "name": "OPay",
          "progress_label": ""
        },
        {
          "location": "dhaka",
          "funding": "",
          "company_id": "5318f947e4b0f7e165ed6f08",
          "slug": "bkash",
          "domain": "bkash.com",
          "description": "Mobile financial services and payment system for consumers",
          "size_label": "very large",
          "name": "bKash",
          "progress_label": ""
        }
      ]
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T02:38:01.691926+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T02:38:01.692214+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/find_competitors.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Payments query returns fifteen peer cards: three each in Seed, Series A, Series B, Series C and Public. The source summary totals 52 sampled candidates across a wider set of stages; it is not a full-market census or the number of cards delivered in these five groups.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.market` | The market label supplied in the request. |
| `data.companies` | A dictionary of returned stage groups, each containing company cards. |
| `data.summary` | Additional source summary fields when available. |
| `per_stage` | Requested companies per stage, between three and ten; this is not a global result limit. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Choose a precise market label from industry discovery, request a small number of companies per stage, and review each candidate's product and geography. Pass selected distinct domains to compare_companies for separate profile and financial evidence.

Do not describe an empty or narrow source result as the full competitive landscape. A similar industry label does not establish that two businesses compete for the same buyer.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/competitor-intelligence-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
