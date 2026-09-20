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
  -d '{"domain":"stripe.com"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_enrichment -->
```json
{
  "name": "get_company_enrichment",
  "arguments": {
    "request": {
      "domain": "stripe.com"
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
    "activity": [
      {
        "d": "2026-06-22",
        "detail": "Stripe Directory",
        "label": "Product launch",
        "type": "product_launch"
      }
    ],
    "digital": {
      "audience": [
        {
          "cc": "US",
          "country": "United States",
          "share": 0.2792,
          "visits": 53060565
        },
        {
          "cc": "GB",
          "country": "United Kingdom",
          "share": 0.0679,
          "visits": 12908445
        },
        {
          "cc": "DE",
          "country": "Germany",
          "share": 0.0483,
          "visits": 9172588
        },
        {
          "cc": "IN",
          "country": "India",
          "share": 0.0453,
          "visits": 8602699
        },
        {
          "cc": "NL",
          "country": "Netherlands",
          "share": 0.0359,
          "visits": 6823857
        }
      ],
      "authority": 79,
      "bounce": 0.6053,
      "country": "United States",
      "country_rank": 165,
      "global_rank": 167,
      "keywords": [
        {
          "k": "stripe",
          "pos": 1,
          "vol": 550000
        },
        {
          "k": "online payments",
          "pos": 3,
          "vol": 1000000
        },
        {
          "k": "stripe careers",
          "pos": 1,
          "vol": 18100
        },
        {
          "k": "stripe vacancies",
          "pos": 1,
          "vol": 14800
        }
      ],
      "ppv": 2.8708,
      "visits": 190046716,
      "visits_date": "2026-05-01"
    },
    "domain": "stripe.com",
    "has_data": true,
    "hiring": {
      "active_12m": 13,
      "avg_12m": 21.9,
      "first_dt": "2024-05-08",
      "freq_detail": "263 roles tracked across 13 of the last 12 months",
      "freq_label": "Hires continuously",
      "last_dt": "2026-09-16",
      "locations": [
        "Toronto",
        "South San Francisco",
        "Chicago",
        "Seattle",
        "San Francisco",
        "Bengaluru / Bangalore, Karnataka, India",
        "New York",
        "Atlanta"
      ],
      "months": [
        {
          "m": "2024-11",
          "n": 3
        },
        {
          "m": "2025-01",
          "n": 5
        },
        {
          "m": "2025-03",
          "n": 6
        },
        {
          "m": "2025-04",
          "n": 7
        },
        {
          "m": "2025-05",
          "n": 2
        },
        {
          "m": "2025-06",
          "n": 16
        },
        {
          "m": "2025-07",
          "n": 19
        },
        {
          "m": "2025-08",
          "n": 23
        },
        {
          "m": "2025-09",
          "n": 30
        },
        {
          "m": "2025-10",
          "n": 32
        },
        {
          "m": "2025-11",
          "n": 42
        },
        {
          "m": "2025-12",
          "n": 18
        },
        {
          "m": "2026-01",
          "n": 33
        },
        {
          "m": "2026-02",
          "n": 16
        },
        {
          "m": "2026-03",
          "n": 6
        },
        {
          "m": "2026-04",
          "n": 15
        },
        {
          "m": "2026-05",
          "n": 29
        },
        {
          "m": "2026-06",
          "n": 20
        },
        {
          "m": "2026-07",
          "n": 9
        },
        {
          "m": "2026-08",
          "n": 9
        },
        {
          "m": "2026-09",
          "n": 4
        }
      ],
      "recent": [
        {
          "d": "2026-09-16",
          "location": "Bangalore",
          "title": "Head of Finance Operations"
        },
        {
          "d": "2026-09-07",
          "location": "Bangalore",
          "title": "Contracting Operations Specialist | Bangalore, IN"
        },
        {
          "d": "2026-09-07",
          "location": "Bangalore",
          "title": "Fraud Operations Manager"
        },
        {
          "d": "2026-09-05",
          "location": "Bangalore",
          "title": "Software Engineer, New Grad"
        },
        {
          "d": "2026-08-27",
          "location": "All India",
          "title": "RN CLIN DOCUMENTATION COORD, FCH - ENTERPRISE QUALITY CDI/UR/DM"
        },
        {
          "d": "2026-08-27",
          "location": "Bangalore",
          "title": "Credit Risk Operations Team Lead"
        },
        {
          "d": "2026-08-21",
          "location": "Bangalore",
          "title": "Operations Associate, GTM Accelerate (Bangalore)"
        },
        {
          "d": "2026-08-16",
          "location": "Bangalore",
          "title": "Data Science Manager, Risk (Bengaluru)"
        },
        {
          "d": "2026-08-16",
          "location": "Bangalore",
          "title": "Marketing Services Program Manager"
        },
        {
          "d": "2026-08-11",
          "location": "Bangalore",
          "title": "Staff Engineer, Revenue (Bengaluru)"
        }
      ],
      "roles": [
        "Technical Account Manager",
        "People Partner",
        "Corporate Strategy",
        "Broadcast Engineer",
        "Staff Security Engineer, Security Partnerships",
        "EMEA Real Estate Transaction Manager",
        "Design Recruiter",
        "Company Strategy & Operations"
      ],
      "total": 368,
      "years": [
        {
          "n": 31,
          "y": "2024"
        },
        {
          "n": 200,
          "y": "2025"
        },
        {
          "n": 141,
          "y": "2026"
        }
      ]
    },
    "innovation": {
      "areas": [
        "Physics & computing",
        "Electricity & electronics"
      ],
      "citations": 10175,
      "families": 276,
      "granted": 188,
      "momentum": "accelerating",
      "notable": [
        {
          "citations": 390,
          "title": "Method and apparatus for ordering goods, services and content over an internetwork using a virtual payment account",
          "y": "2023"
        },
        {
          "citations": 110,
          "title": "System and method for indicating entry of personal identification number",
          "y": "2024"
        },
        {
          "citations": 92,
          "title": "Methods and systems for providing payment interface services using a payment platform",
          "y": "2025"
        }
      ],
      "years": [
        {
          "n": 1,
          "y": "2013"
        },
        {
          "n": 7,
          "y": "2017"
        },
        {
          "n": 10,
          "y": "2018"
        },
        {
          "n": 12,
          "y": "2019"
        },
        {
          "n": 11,
          "y": "2020"
        },
        {
          "n": 23,
          "y": "2021"
        },
        {
          "n": 51,
          "y": "2022"
        },
        {
          "n": 100,
          "y": "2023"
        },
        {
          "n": 134,
          "y": "2024"
        },
        {
          "n": 143,
          "y": "2025"
        },
        {
          "n": 36,
          "y": "2026"
        }
      ]
    },
    "legal": [
      {
        "country": "United States",
        "id_no": "270465600",
        "legal_name": "Stripe, Inc.",
        "registry": "Others"
      },
      {
        "country": "United Kingdom",
        "id_no": "4675506",
        "legal_name": "SQUARE MILE BUSINESS SERVICES LIMITED",
        "registry": "companieshouse.gov.uk"
      },
      {
        "country": "Czech Republic",
        "id_no": "08667900",
        "legal_name": "STRIPE WOOD s.r.o.",
        "registry": "czso.cz"
      },
      {
        "country": "India",
        "id_no": "U72200KA2016FTC096320",
        "legal_name": "STRIPE INDIA PRIVATE LIMITED",
        "registry": "mca.gov.in"
      },
      {
        "country": "Singapore",
        "id_no": "201524528H",
        "legal_name": "Stripe Payments Singapore Pte. Ltd",
        "registry": "acra.gov.sg"
      }
    ],
    "reputation": {
      "category": "Payment Service",
      "n": 17267,
      "n_12m": 1226,
      "score": 1.7,
      "stars": 1
    },
    "social": {
      "band": "below the industry typical range",
      "cadence_per_month": 0.3,
      "engagement_per_post": 0,
      "followers": 1528731,
      "industry_median_rate": 0.00567,
      "posts_12m": 4,
      "rate": 0.0,
      "ratio_vs_median": 0.0,
      "sector": "Payments"
    },
    "sov": {
      "home_cc": "us",
      "home_country": "United States",
      "peers": [
        {
          "domain": "stripe.com",
          "followers": 1528731,
          "home_visits": 53060565,
          "name": "Stripe",
          "reviews": 17267,
          "world_visits": 190046716
        },
        {
          "domain": "gocardless.com",
          "followers": 70647,
          "home_visits": 301098,
          "name": "GoCardless",
          "reviews": 2438,
          "world_visits": 2688810
        },
        {
          "domain": "sba.gov",
          "followers": 277487,
          "home_visits": 3721219,
          "name": "u.s. small business administration",
          "reviews": 15,
          "world_visits": 3959133
        },
        {
          "domain": "airwallex.com",
          "followers": 178694,
          "home_visits": 3704482,
          "name": "Airwallex",
          "reviews": 2493,
          "world_visits": 9558412
        },
        {
          "domain": "stripeandstare.com",
          "followers": 5227,
          "home_visits": 20833,
          "name": "Stripe & Stare",
          "reviews": 1651,
          "world_visits": 119042
        },
        {
          "domain": "stripersonline.com",
          "followers": null,
          "home_visits": 80103,
          "name": "stripersonline.com",
          "reviews": null,
          "world_visits": 88627
        }
      ],
      "shares": {
        "followers": {
          "airwallex.com": 0.0867,
          "gocardless.com": 0.0343,
          "sba.gov": 0.1347,
          "stripe.com": 0.7418,
          "stripeandstare.com": 0.0025
        },
        "home_traffic": {
          "airwallex.com": 0.0608,
          "gocardless.com": 0.0049,
          "sba.gov": 0.0611,
          "stripe.com": 0.8714,
          "stripeandstare.com": 0.0003,
          "stripersonline.com": 0.0013
        },
        "reviews": {
          "airwallex.com": 0.1045,
          "gocardless.com": 0.1022,
          "sba.gov": 0.0006,
          "stripe.com": 0.7236,
          "stripeandstare.com": 0.0692
        },
        "world_traffic": {
          "airwallex.com": 0.0463,
          "gocardless.com": 0.013,
          "sba.gov": 0.0192,
          "stripe.com": 0.9205,
          "stripeandstare.com": 0.0006,
          "stripersonline.com": 0.0004
        }
      }
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T06:35:41.289332+00:00",
    "partial": false,
    "notes": [
      "Absent enrichment sections have unknown coverage; the source does not distinguish missing data from a failed section."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T06:35:41.289574+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_enrichment.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Stripe capture returned digital traffic and audience, hiring history and roles, innovation and patents, social engagement, activity, legal entries, reputation aggregates and share-of-voice peers. All these business-data sections and their array rows are shown. Individual review snippets are excluded from documentation reproduction.

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
