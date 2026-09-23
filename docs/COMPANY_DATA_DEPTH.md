# Company data examples: financials, founders, apps, LinkedIn, business data and events

Start with a compact company profile. It returns identity, a short description,
founding year, employee count, a Radar image URL and the names of available fields.
Rich values require a separate JSON POST selecting one field. Availability checks
do not return email addresses, phone numbers, technology arrays or founder records.

[Jump to 13 worked examples with complete saved responses](#worked-examples-with-actual-requests-and-outputs),
including [financials](#financial-statements), [founders](#founders-and-background),
[apps](#apps-roster), [LinkedIn-associated profiles](#linkedin-professional),
[business classifications](#business-classification) and [events](#business-events).

## 1. Discover the company and its available fields

```json
{"domain": "razorpay.com"}
```

Send this to `POST /v1/companies/profile`, or MCP `get_company`. Read
`available_fields`, `field_status` and `contacts.availability`. These report stored
coverage. They do not promise current accuracy, email deliverability or paid access.
An unconnected field store returns `profile_depth=card` and unavailable field status.
The normal connected response is `profile_depth=summary`.

## 2. Retrieve one field

```json
{"domain": "razorpay.com", "field": "technology", "item_limit": 100}
```

Send this to `POST /v1/companies/field`, or MCP `get_company_field`. Only `value`
contains the requested field. `item_limit` defaults to 50 and is capped at 100 per
array. Every array reports available/returned/truncated counts in `coverage.arrays`.
No all-fields selector exists. The old `sections` and `item_limit` parameters on
`get_company` are rejected with HTTP 422; move those detail reads to the field endpoint.
Each successful field request costs one operation credit in account mode.

## Real, separate captures

The following JSON files come from authenticated local gateway calls against the
live company store. Most were captured on 2026-09-21; the three social fields were
refreshed on 2026-09-23 with LinkedIn profile logs and stored posts. Each includes its request, response, timestamp,
checksums and explicit documentation omission paths. The values are source
observations; they have not been independently verified as current facts.

| Compact company | Available detail fields | Summary JSON |
|---|---:|---|
| Razorpay | 17 | [razorpay.com](examples/profiles/razorpay.com.json) |
| Stripe | 18 | [stripe.com](examples/profiles/stripe.com.json) |
| Swiggy | 17 | [swiggy.com](examples/profiles/swiggy.com.json) |

| Field request | Razorpay | Stripe | Swiggy |
|---|---|---|---|
| `overview` | [JSON](examples/fields/razorpay.com-overview.json) | [JSON](examples/fields/stripe.com-overview.json) | [JSON](examples/fields/swiggy.com-overview.json) |
| `classification` | [JSON](examples/fields/razorpay.com-classification.json) | [JSON](examples/fields/stripe.com-classification.json) | [JSON](examples/fields/swiggy.com-classification.json) |
| `people` | [JSON](examples/fields/razorpay.com-people.json) | [JSON](examples/fields/stripe.com-people.json) | [JSON](examples/fields/swiggy.com-people.json) |
| `technology` | [JSON](examples/fields/razorpay.com-technology.json) | [JSON](examples/fields/stripe.com-technology.json) | [JSON](examples/fields/swiggy.com-technology.json) |
| `web_presence` | [JSON](examples/fields/razorpay.com-web_presence.json) | [JSON](examples/fields/stripe.com-web_presence.json) | [JSON](examples/fields/swiggy.com-web_presence.json) |
| `traffic` | [JSON](examples/fields/razorpay.com-traffic.json) | [JSON](examples/fields/stripe.com-traffic.json) | [JSON](examples/fields/swiggy.com-traffic.json) |
| `apps` | [JSON](examples/fields/razorpay.com-apps.json) | [JSON](examples/fields/stripe.com-apps.json) | [JSON](examples/fields/swiggy.com-apps.json) |
| `products` | [JSON](examples/fields/razorpay.com-products.json) | [JSON](examples/fields/stripe.com-products.json) | [JSON](examples/fields/swiggy.com-products.json) |
| `geography` | [JSON](examples/fields/razorpay.com-geography.json) | [JSON](examples/fields/stripe.com-geography.json) | [JSON](examples/fields/swiggy.com-geography.json) |
| `social` | [JSON](examples/fields/razorpay.com-social.json) | [JSON](examples/fields/stripe.com-social.json) | [JSON](examples/fields/swiggy.com-social.json) |
| `lifecycle` | [JSON](examples/fields/razorpay.com-lifecycle.json) | [JSON](examples/fields/stripe.com-lifecycle.json) | [JSON](examples/fields/swiggy.com-lifecycle.json) |
| `legal` | [JSON](examples/fields/razorpay.com-legal.json) | [JSON](examples/fields/stripe.com-legal.json) | [JSON](examples/fields/swiggy.com-legal.json) |
| `assessments` | [JSON](examples/fields/razorpay.com-assessments.json) | [JSON](examples/fields/stripe.com-assessments.json) | [JSON](examples/fields/swiggy.com-assessments.json) |
| `hiring` | [JSON](examples/fields/razorpay.com-hiring.json) | [JSON](examples/fields/stripe.com-hiring.json) | [JSON](examples/fields/swiggy.com-hiring.json) |
| `innovation` | [JSON](examples/fields/razorpay.com-innovation.json) | [JSON](examples/fields/stripe.com-innovation.json) | [JSON](examples/fields/swiggy.com-innovation.json) |
| `activity` | [JSON](examples/fields/razorpay.com-activity.json) | [JSON](examples/fields/stripe.com-activity.json) | [JSON](examples/fields/swiggy.com-activity.json) |
| `reputation` | [JSON](examples/fields/razorpay.com-reputation.json) | [JSON](examples/fields/stripe.com-reputation.json) | [JSON](examples/fields/swiggy.com-reputation.json) |
| `share_of_voice` | [JSON](examples/fields/razorpay.com-share_of_voice.json) | [JSON](examples/fields/stripe.com-share_of_voice.json) | [JSON](examples/fields/swiggy.com-share_of_voice.json) |

## What the fields mean

- `overview`: alternate names, other domains and the longer description.
- `classification`: sectors, primary and other feeds, industries, business/revenue models and source flags.
- `people`: named key people and founders selected by the source designation. These are professional records; contact values require their own endpoint.
- `technology` and `web_presence`: merged stack, observed technologies and crawl dates versus web performance, SEO and derived digital scores.
- `traffic`: visits, observation date, country shares, keywords and engagement. Visits are not unique customers, and fractions remain fractions.
- `apps`: aggregate app count, downloads and rating. This is not an app roster; downloads are not monthly active users.
- `products`, `geography`, `social`, `lifecycle`, `legal`, `assessments`: separately requested business context. Scores are derived assessments; legal associations may need review.
- `social` includes platform links plus `linkedin.profile`, bounded `profile_history` and distinct `recent_posts` when its read connection is configured. LinkedIn observations carry their own dates and per-source coverage.
- `hiring`, `innovation`, `activity`, `reputation`, `share_of_voice`: separate enrichment observations with source coverage and date limitations.

`available` means the field was observed, including an empty list or numeric zero.
`not_observed` means no stored observation; `unavailable` means the store failed;
`partial` and array truncation remain explicit. Missing values never become zero.

## Contacts, financials and briefs

Request company emails or phone numbers with `get_company_contacts`; request a
professional's contact using a person ID returned by `search_people` and
`get_person_contacts`. Both require the explicit `contacts` key scope and the
linked Radar account's paid-plan check. Company-domain fallback is labeled and
must not be treated as a verified personal contact. See [contact retrieval](CONTACTS.md).

Financial history remains in `get_financials` with period, currency, source and
access-limit metadata. `company_brief` now returns concise section summaries and
separate detail requests, rather than embedding the complete profile and archives.
The image URL uses Radar's first-party image route; that route can fall back to a
favicon. Stored provider CDN logo URLs are not passed through.

See [profile reference](reference/get_company.md), [field reference](reference/get_company_field.md),
[filters and listings](FILTERS_AND_LISTINGS.md), [source review](RADAR_SOURCE_REVIEW.md)
and [data quality](DATA_QUALITY.md).

<!-- company-depth-examples -->
## Worked examples with actual requests and outputs

The examples below reuse the repository's captured responses. They are not new
live calls made when this page is generated. Each block shows its original capture
time, source mode, exact JSON request and complete saved response. Returned business
arrays are not shortened here; the linked capture lists any earlier documentation
prose omissions and its original-response checksum. Source dates and capture dates
are different, and neither establishes that a record is current today.

Send each body to the stated POST route using your API URL and API key. For MCP,
use the named tool with the same body inside `arguments.request`.
[API-key onboarding](guides/api-keys-authentication.md) explains the credentials.

- [Financial data: income, balance sheet and cash flow](#financial-statements)
- [Founders data: names, designations and background flags](#founders-and-background)
- [A separate founders-only team request](#founders-only)
- [Apps data: company-level totals](#apps-summary)
- [Apps data: individual products matched to the company](#apps-roster)
- [App detail: dated install growth and reliability](#app-growth)
- [LinkedIn company data: followers, headcount, snapshots and stored posts](#linkedin-company)
- [LinkedIn-associated professional data: education and experience](#linkedin-professional)
- [Business data: sectors, feeds and revenue models](#business-classification)
- [Technology data: website stack and dated observations](#technology-stack)
- [Traffic data: visits, countries, keywords and engagement](#website-traffic)
- [Business events: earnings, products, contracts and people changes](#business-events)
- [Company activity events: effective windows and pulse summaries](#company-activity)

<a id="financial-statements"></a>

### Financial data: income, balance sheet and cash flow

**`POST /v1/companies/financials`** · MCP **`get_financials`** ·
[Endpoint details](reference/get_financials.md) · [Captured JSON](examples/get_financials.json).

This Microsoft request returns two fiscal periods with income, balance-sheet and
cash-flow observations together. The captured Q3 FY2026 period reports revenue
of USD 82.886 billion, net income of USD 31.778 billion, total assets of USD 694.228
billion and operating cash flow of USD 46.679 billion. Those are values in the
captured API response, not an independent reconciliation with the company's filings.

Each metric retains its source type, unit, normalized currency and available native
value. EPS is a per-share measure; its null normalized currency must not be filled
in from an unrelated USD metric. Both returned periods and all their metrics appear
below. `available_period_count` is 20 and `access_limited` is true, so two delivered
periods are not the whole archive. `period_end` can be null even when filing or
report dates are available.

For a chosen statement family, use `statement=income`, `balance_sheet` or `cash_flow`;
for time selection, use `period_type`, `year_from` and `year_to`. The
[financial filters guide](guides/financial-filters-data-api.md) explains exact
revenue/profit comparisons, including the executed [US AdTech startup query below
$10,000](scenarios/03-usa-adtech-under-10k.md). Missing revenue remains unknown.

Exact captured request:

<!-- company-depth-request: get_financials.json -->
```json
{
  "domain": "microsoft.com",
  "limit": 2
}
```

Captured **2026-09-20T04:58:42.493744+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: get_financials.json -->
```json
{
  "ok": true,
  "feature": "get_financials",
  "data": {
    "domain": "microsoft.com",
    "statement": "all",
    "has_data": true,
    "periods": [
      {
        "period": "Q3 FY2026",
        "fiscal_year": 2026,
        "fiscal_period": "Q3",
        "period_end": null,
        "reported_date": "2026-04-29",
        "filed_date": "2026-04-29",
        "form_type": "10-Q",
        "metrics": {
          "cash": {
            "value": 32105000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 32105000000.0,
            "native_currency": "USD"
          },
          "eps": {
            "value": 4.27,
            "currency": null,
            "unit": "per_share",
            "source_type": "filing",
            "native_value": 4.27,
            "native_currency": "USD"
          },
          "gross_profit": {
            "value": 56058000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 56058000000.0,
            "native_currency": "USD"
          },
          "long_term_debt": {
            "value": 40262000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 40262000000.0,
            "native_currency": "USD"
          },
          "net_income": {
            "value": 31778000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 31778000000.0,
            "native_currency": "USD"
          },
          "operating_cash_flow": {
            "value": 46679000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 46679000000.0,
            "native_currency": "USD"
          },
          "operating_income": {
            "value": 38398000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 38398000000.0,
            "native_currency": "USD"
          },
          "revenue": {
            "value": 82886000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 82886000000.0,
            "native_currency": "USD"
          },
          "stockholders_equity": {
            "value": 414367000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 414367000000.0,
            "native_currency": "USD"
          },
          "total_assets": {
            "value": 694228000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 694228000000.0,
            "native_currency": "USD"
          },
          "total_liabilities": {
            "value": 279861000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 279861000000.0,
            "native_currency": "USD"
          }
        },
        "article_ids": [
          "69e99ba475f157062cafcd91",
          "69f87f9d43843dd771ce0936",
          "69f8a61b43843dd771d24172",
          "69f9d902713680636eef61bb"
        ],
        "currency_conversion": "native_usd"
      },
      {
        "period": "Q2 FY2026",
        "fiscal_year": 2026,
        "fiscal_period": "Q2",
        "period_end": null,
        "reported_date": "2025-12-31",
        "filed_date": "2026-01-28",
        "form_type": "10-Q",
        "metrics": {
          "cash": {
            "value": 24296000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 24296000000.0,
            "native_currency": "USD"
          },
          "eps": {
            "value": 5.16,
            "currency": null,
            "unit": "per_share",
            "source_type": "filing",
            "native_value": 5.16,
            "native_currency": "USD"
          },
          "gross_profit": {
            "value": 55295000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 55295000000.0,
            "native_currency": "USD"
          },
          "long_term_debt": {
            "value": 40262000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 40262000000.0,
            "native_currency": "USD"
          },
          "net_income": {
            "value": 38458000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 38458000000.0,
            "native_currency": "USD"
          },
          "operating_cash_flow": {
            "value": 35758000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 35758000000.0,
            "native_currency": "USD"
          },
          "operating_income": {
            "value": 38275000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 38275000000.0,
            "native_currency": "USD"
          },
          "revenue": {
            "value": 81273000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 81273000000.0,
            "native_currency": "USD"
          },
          "stockholders_equity": {
            "value": 390875000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 390875000000.0,
            "native_currency": "USD"
          },
          "total_assets": {
            "value": 665302000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 665302000000.0,
            "native_currency": "USD"
          },
          "total_liabilities": {
            "value": 274427000000.0,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "filing",
            "native_value": 274427000000.0,
            "native_currency": "USD"
          }
        },
        "article_ids": [
          "6988a7773757765ee826377c",
          "698e37498d29a990b6e524d5",
          "69bbe6aba75fc0dcb02055d5",
          "69bce327a7b1648247b810ef",
          "69c42f5b7c4635ab38e80104",
          "69cc188adcf7c26bbed60f05",
          "69dfb24286bd23245a9134fc",
          "69dfb6f5c1e955063e150b93"
        ],
        "currency_conversion": "native_usd"
      }
    ],
    "returned": 2,
    "truncated": true,
    "access_limited": true,
    "available_period_count": 20,
    "computed_at": "2026-09-19T17:19:34.120000Z",
    "summary": {
      "narrative": "Latest reported Q3 FY2026: revenue $82.89B, net income $31.78B, EPS $4.27. YoY +18.3% (1.18× prior period). Growth pattern is consistent across reported periods. Recent signals: Raised guidance, Beat estimates, Profitable. Financials sourced from official filings (10-K, 10-Q, 10-Q/A); news/BI estimates fill any gaps."
    }
  },
  "window": {
    "data_through": "2026-04-29"
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:45.976790+00:00",
    "partial": false,
    "notes": [
      "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
      "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies.",
      "The linked Radar account exposes only part of the financial archive."
    ],
    "provider": "Fliar BI"
  }
}
```

<a id="founders-and-background"></a>

### Founders data: names, designations and background flags

**`POST /v1/companies/field`** · MCP **`get_company_field`** ·
[Endpoint details](reference/get_company_field.md) · [Captured JSON](examples/fields/razorpay.com-people.json).

The company `people` field returns Razorpay's recorded key people and founders,
plus background flags such as colleges and prior companies. This capture includes
Shashank Kumar and Harshil Mathur with their recorded designations. Background flags
are company-level source associations; this response does not assign every listed
college or employer to a particular founder.

The same person can occur in both `key_people` and `founders`; those arrays are
views of the source records, not four distinct people. Founder selection is based
on the recorded designation containing “founder”. Keep `updated_at`, the selection
rule and each array's returned/available counts. These are not verified current
employment records, and no email or phone values are embedded in the response.

Exact captured request:

<!-- company-depth-request: fields/razorpay.com-people.json -->
```json
{
  "domain": "razorpay.com",
  "field": "people",
  "item_limit": 100
}
```

Captured **2026-09-21T04:08:57.264471+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: fields/razorpay.com-people.json -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "razorpay.com",
    "company_id": "2gowls1wmc",
    "field": "people",
    "value": {
      "key_people": [
        {
          "name": "Shashank Kumar",
          "designation": "Co-Founder & Managing Director"
        },
        {
          "name": "Harshil Mathur",
          "designation": "Co-Founder & CEO"
        }
      ],
      "founders": [
        {
          "name": "Shashank Kumar",
          "designation": "Co-Founder & Managing Director"
        },
        {
          "name": "Harshil Mathur",
          "designation": "Co-Founder & CEO"
        }
      ],
      "key_people_count": 2,
      "background_flags": [
        {
          "name": "Indian School of Business",
          "category": "College Wise"
        },
        {
          "name": "Intel",
          "category": "Company Wise"
        },
        {
          "name": "IIT Roorkee",
          "category": "College Wise"
        }
      ],
      "founder_selection": "Source designation contains founder; not an independent verification"
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "people": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/key_people": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/founders": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/background_flags": {
          "available": 3,
          "returned": 3,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T04:08:57.264471+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

<a id="founders-only"></a>

### A separate founders-only team request

**`POST /v1/companies/team`** · MCP **`get_company_team`** ·
[Endpoint details](reference/get_company_team.md) · [Captured JSON](examples/scenarios/21-razorpay-founders.json).

When the application needs only founders, request `group=founders` through the team
endpoint. The response returns the two recorded Razorpay founders without the other
company field groups. Choose `key_people` for leadership or `professionals` for
richer professional cards; those choices have different source coverage and filters.

`matched_observed_rows` describes the bounded observed key-person set, not company
headcount. Professional team retrieval requires the `people` scope in addition to
`companies` and checks the exact recorded company domain. See the
[teams and people guide](guides/teams-people-data-api.md) for paging, designation
filters, career seniority and separate contact retrieval.

Exact captured request:

<!-- company-depth-request: scenarios/21-razorpay-founders.json -->
```json
{
  "domain": "razorpay.com",
  "group": "founders",
  "limit": 10
}
```

Captured **2026-09-23T03:35:32.198845+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: scenarios/21-razorpay-founders.json -->
```json
{
  "ok": true,
  "feature": "get_company_team",
  "data": {
    "domain": "razorpay.com",
    "group": "founders",
    "people": [
      {
        "name": "Shashank Kumar",
        "designation": "Co-Founder & Managing Director"
      },
      {
        "name": "Harshil Mathur",
        "designation": "Co-Founder & CEO"
      }
    ],
    "returned": 2,
    "matched_observed_rows": 2,
    "page": 0,
    "next_page": null,
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "complete": false,
      "partial": false,
      "source_status": "available",
      "note": "Company key-person records, not a full employee roster or verified headcount. Founders are selected by recorded designation; no contacts are included."
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:32.198739+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

<a id="apps-summary"></a>

### Apps data: company-level totals

**`POST /v1/companies/field`** · MCP **`get_company_field`** ·
[Endpoint details](reference/get_company_field.md) · [Captured JSON](examples/fields/swiggy.com-apps.json).

This selected company field reports four apps, 382,800,000 aggregate downloads and
a weighted rating for Swiggy. It is an aggregate observation, not a list of app IDs,
monthly active users, company revenue or verified current store statistics.

Use the next request for individual apps. Aggregate values and individual app
observations can have different dates, source coverage and calculation methods;
do not replace an aggregate with a sum of whatever fits on one roster page.

Exact captured request:

<!-- company-depth-request: fields/swiggy.com-apps.json -->
```json
{
  "domain": "swiggy.com",
  "field": "apps",
  "item_limit": 100
}
```

Captured **2026-09-21T04:08:57.311787+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: fields/swiggy.com-apps.json -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "swiggy.com",
    "company_id": "tiwgsjxo90",
    "field": "apps",
    "value": {
      "count": 4,
      "downloads": 382800000,
      "weighted_rating": 4.7090927724363185
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "apps": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {},
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T04:08:57.311787+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

<a id="apps-roster"></a>

### Apps data: individual products matched to the company

**`POST /v1/companies/apps`** · MCP **`company_apps`** ·
[Endpoint details](reference/company_apps.md) · [Captured JSON](examples/company_apps.json).

The company-app lookup returns four Google Play records whose normalized developer
website host matches `swiggy.com`: the consumer app, partner app, IM Retails Tasks
and Swiggy Pulse. Every returned app includes its ID, developer, store URL,
observation date and available install/rating metrics.

This is an exact website-host association, not a fuzzy name match or proof of
corporate ownership. An app belonging to the business under another developer
website can be missed. Retain numeric zero separately from null: IM Retails Tasks
has a captured rating/count of zero, while Swiggy Pulse has missing rating data.
Use a returned `app_id` for `get_app` or `get_app_field`, not the company's domain.

Exact captured request:

<!-- company-depth-request: company_apps.json -->
```json
{
  "domain": "swiggy.com",
  "limit": 5
}
```

Captured **2026-09-21T10:48:29.772077+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: company_apps.json -->
```json
{
  "ok": true,
  "feature": "company_apps",
  "data": {
    "apps": [
      {
        "app_id": "in.swiggy.android",
        "name": "Swiggy: Food Instamart Dineout",
        "developer": "Swiggy",
        "developer_website": "https://www.swiggy.com",
        "category": "Food & Drink",
        "installs": 281013619,
        "rating": 4.663636,
        "rating_count": 12718296,
        "observed_at": "2026-06-07T03:54:55Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=in.swiggy.android",
        "detail_request": {
          "method": "POST",
          "path": "/v1/apps/profile"
        }
      },
      {
        "app_id": "in.swiggy.partnerapp",
        "name": "Swiggy Partner App",
        "developer": "Swiggy",
        "developer_website": "https://www.swiggy.com",
        "category": "Business",
        "installs": 5189565,
        "rating": 3.9047618,
        "rating_count": 42053,
        "observed_at": "2026-06-08T07:18:48Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=in.swiggy.partnerapp",
        "detail_request": {
          "method": "POST",
          "path": "/v1/apps/profile"
        }
      },
      {
        "app_id": "com.swiggy.swiggyvendorapp",
        "name": "IM Retails Tasks",
        "developer": "SwiggyInstamart",
        "developer_website": "https://www.swiggy.com/",
        "category": "Food & Drink",
        "installs": 218985,
        "rating": 0,
        "rating_count": 0,
        "observed_at": "2026-06-08T07:44:13Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=com.swiggy.swiggyvendorapp",
        "detail_request": {
          "method": "POST",
          "path": "/v1/apps/profile"
        }
      },
      {
        "app_id": "in.swiggy.pulseapp",
        "name": "Swiggy Pulse",
        "developer": "Swiggy",
        "developer_website": "https://www.swiggy.com",
        "category": "Business",
        "installs": 3675,
        "rating": null,
        "rating_count": null,
        "observed_at": "2026-06-08T10:18:55Z",
        "store": "google_play",
        "url": "https://play.google.com/store/apps/details?id=in.swiggy.pulseapp",
        "detail_request": {
          "method": "POST",
          "path": "/v1/apps/profile"
        }
      }
    ],
    "page": 0,
    "limit": 5,
    "has_more": false,
    "total": null,
    "match_method": "Exact normalized developer website host; no fuzzy name, URL substring or ownership inference",
    "coverage": {
      "store": "google_play",
      "live_store_verified": false
    },
    "note": "Observed Play Store data only. Installs are cumulative source estimates; row observation dates are not current download dates."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T10:48:29.771858+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

<a id="app-growth"></a>

### App detail: dated install growth and reliability

**`POST /v1/apps/field`** · MCP **`get_app_field`** ·
[Endpoint details](reference/get_app_field.md) · [Captured JSON](examples/get_app_field.json).

A separate `growth` request for `in.swiggy.android` exposes the measurements behind
the derived figure: 223,179,065 installs observed on June 11, 2025 and 281,013,619
on June 7, 2026, a 360-day interval. The source reports 25.91% observed change and
26.32% annualized change. Annualizing a measured interval is not a prediction.

Keep the `reliable`, `release_date_suspect` and observation fields. Other explicit
app fields expose listing, developer, ratings, monetization, release and install
history. [All seven app-field examples](APP_DATA_DEPTH.md) preserve their structured
output; install history can include duplicate stored observations.

Exact captured request:

<!-- company-depth-request: get_app_field.json -->
```json
{
  "app_id": "in.swiggy.android",
  "field": "growth"
}
```

Captured **2026-09-21T10:48:30.099775+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: get_app_field.json -->
```json
{
  "ok": true,
  "feature": "get_app_field",
  "data": {
    "app_id": "in.swiggy.android",
    "store": "google_play",
    "observed_at": "2026-06-07T03:54:55Z",
    "coverage": {
      "live_store_verified": false,
      "source": "radar_app_records"
    },
    "field": "growth",
    "value": {
      "install_change": {
        "current_observed_at": "2026-06-07T03:54:55Z",
        "current_installs": 281013619,
        "previous_installs": 223179065,
        "previous_observed_at": "2025-06-11T18:30:00Z",
        "gap_days": 360,
        "observed_change_pct": 25.91,
        "annualized_change_pct": 26.32,
        "reliable": 1
      },
      "velocity": {
        "age_years": 11,
        "avg_installs_per_year": 25551462,
        "release_date_suspect": 0,
        "young_fast_riser": 0
      },
      "note": "Annualized growth is derived from the measured gap, not necessarily a full-year observation. Retain reliable and suspect-date flags; this is not a forecast."
    },
    "status": "available"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T10:48:30.099630+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

<a id="linkedin-company"></a>

### LinkedIn company data: followers, headcount, snapshots and stored posts

**`POST /v1/companies/field`** · MCP **`get_company_field`** ·
[Endpoint details](reference/get_company_field.md) · [Captured JSON](examples/fields/razorpay.com-social.json).

The selected `social` field combines recorded platform links with LinkedIn profile
observations and stored posts. The refreshed Razorpay capture includes **1,252,056
followers**, **4,052 observed employees**, company size **1,001–5,000**, one profile
snapshot and **eight distinct posts**. Each post retains its URL, text, publication
and observation times, hashtags, media and stored engagement counters.

The profile was observed on **2026-07-02**. Those figures are historical platform
observations, not current audited headcount. `profile_history` holds the available
snapshots; one snapshot cannot establish follower growth. `recent_posts` means the
newest stored posts, not a live feed. Counts use the latest crawl per post, never a
sum across repeated crawls. Source zero engagement values can include parser defaults.

`updated_at` belongs to the company record; LinkedIn records carry their own
`observed_at`. The source labels this profile's sector HRTech, which disagrees with
Razorpay's business classification; the API preserves it as `recorded_sector`.
The compact company endpoint still returns availability without these rich values.
See [the LinkedIn data guide](guides/linkedin-social-data-api.md).

Exact captured request:

<!-- company-depth-request: fields/razorpay.com-social.json -->
```json
{
  "domain": "razorpay.com",
  "field": "social",
  "item_limit": 100
}
```

Captured **2026-09-23T05:26:09.902949+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: fields/razorpay.com-social.json -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "razorpay.com",
    "company_id": "2gowls1wmc",
    "field": "social",
    "value": {
      "links": {
        "linkedin": "https://linkedin.com/company/razorpay/about",
        "x": "https://twitter.com/razorpay",
        "facebook": "https://facebook.com/razorpay",
        "blog": "https://razorpay.com/blog"
      },
      "linkedin": {
        "profile_history": [
          {
            "name": "Razorpay",
            "linkedin_slug": "razorpay",
            "recorded_sector": "HRTech",
            "hq_country": "India",
            "followers": 1252056,
            "employee_count": 4052,
            "company_size": "1,001-5,000",
            "observed_reactions": 719,
            "observed_comments": 25,
            "observed_post_count": 8,
            "observed_at": "2026-07-02T15:19:12Z"
          }
        ],
        "recent_posts": [
          {
            "post_id": "7478336549894426624",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-bangaloreogs-activity-7478336549894426624-oic9",
            "title": "",
            "text": "Keep it simple. That's the whole business philosophy Mr. Narayan Rao has ever needed at Corner House Ice Creams. \n\nFor decades generations of Bangalore have grown up enjoying and bonding over the same Hot Chocolate Fudge and DBC, grandparents and grandchildren alike.\n\nThis is Bangalore OGs, our love letter to the builders who made Bengaluru what it is today.\n\n#Razorpay #BangaloreOGs",
            "media_urls": [],
            "hashtags": [
              "Razorpay",
              "BangaloreOGs"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-07-02T01:09:34Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7478016085380878336",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_event-usmixer-razorpay-activity-7478016085380878336-lUpB",
            "title": "",
            "text": "Outtakes from a very special evening in SF, hosted in partnership with Silicon Valley Bank and Lightspeed. 💫\n\nA room full of Founders and operators from some of the most exciting companies, all building for the globe from Day 1. \n\nA big takeaway from the evening: The old playbook of expanding across geographies (years of groundwork, local entities, endless compliance) is dead. AI collapsed the timeline, and now going global is a decision you make on Day 1, not a milestone you earn years later.\n\nThank you to everyone who came out. This is just the beginning.\n\n#Event #USMixer #Razorpay",
            "media_urls": [],
            "hashtags": [
              "Event",
              "USMixer",
              "Razorpay"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-07-01T03:56:09Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7477959074165260290",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-netbanking-nbbl-activity-7477959074165260290-H5Vb",
            "title": "",
            "text": "\n🥁 Exciting news! Razorpay has partnered with NPCI Bharat BillPay Limited (NBBL) to bring a fast NetBanking experience to businesses and consumers across India.\n\nIntroducing Banking Connect - a standardised, mobile-first NetBanking experience built for the next era of digital payments.\n\n✨ We believe NetBanking has earned India’s trust for years. Today, we’re striving to make the experience even better.\n✅One network connecting banks, PAs, and users.\n✅All participant banks are enabled through one integration.\n✅Mobile-first Intent & QR flows for fast payments.\n✅Unified settlements and refunds .\n\nFor businesses, it means simpler enablement and fewer drop-offs. For users, it means NetBanking that is built for today.\n⚡UPI-like speed.\n🛡️The trust of the bank.\n🚀NetBanking 2.0, entering its next era.\n\nRazorpay🤝NPCI NBBL\n\nTo read more: https://lnkd.in/dhn2Qmah \n\n#Razorpay #NetBanking #NBBL #BankingConnect",
            "media_urls": [],
            "hashtags": [
              "Razorpay",
              "NetBanking",
              "NBBL",
              "BankingConnect"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-07-01T00:09:37Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7477683363114446848",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_event-razorpay-activity-7477683363114446848-H_zu",
            "title": "",
            "text": "Super excited to join the World's Largest Hermes Buildathon as the Ecosystem Partner in Bangalore!\n\nThe buildathon is happening across 10 cities and 5 countries, with builders getting access to $750K worth of credits to build on Hermes.\n\nPresented by GrowthX® alongside incredible partners like OpenAI, ElevenLabs, Wispr Flow, Cloudflare, and Convex, we're excited to bring this global buildathon to Bangalore.\n\nThousands of builders will be building on Hermes, and we're thrilled to welcome some of the best builders to Razorpay.\n\nSuper pumped to be part of this global wave.\n\n#event #razorpay",
            "media_urls": [],
            "hashtags": [
              "event",
              "razorpay"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-06-30T05:54:02Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7477633979073097728",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-activity-7477633979073097728-QbE9",
            "title": "",
            "text": "Revenue leaks are the biggest silent killers of your business 😑\n\nChargebacks, abandoned carts, and failed subscriptions drain your bottom line while you focus on growth.\n\nRazorpay Agent Studio deploys intelligent agents that take care of operational overheads, so you can focus on customers and growth. \n\nNo manual heavy lifting. Just measurable outcomes your CFO will love.\n\nInterested? Sign Up: https://lnkd.in/gYgvU_pi\n\n#Razorpay #3SlidesToConvinceYourCFO #AgentStudio ",
            "media_urls": [],
            "hashtags": [
              "Razorpay",
              "3SlidesToConvinceYourCFO",
              "AgentStudio"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-06-30T02:37:48Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7476884600569618432",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-razorpayftx26-activity-7476884600569618432-EGNA",
            "title": "",
            "text": "Rewinding to FTX 26, where the Agentic Era of Fintech began!\n\n#Razorpay #RazorpayFTX26 ",
            "media_urls": [],
            "hashtags": [
              "Razorpay",
              "RazorpayFTX26"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-06-28T01:00:02Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7476522238662516736",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-whateverittakes-sandoclub-activity-7476522238662516736-u_-o",
            "title": "",
            "text": "How much spice is too much spice? 🌶️\n\nWe put Jassil Jamaludhin and Carl Pinto, founders of Sando Club, through a spicy sando challenge to get their hottest takes on building brands, the F&B space, and everything in between.\n\nAs the sandwich got hotter, so did the questions. And let's just say, some answers were spicier than the sauce itself. 🔥\n\n#Razorpay #WhateverItTakes #SandoClub #Founders",
            "media_urls": [],
            "hashtags": [
              "Razorpay",
              "WhateverItTakes",
              "SandoClub",
              "Founders"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-06-27T01:00:08Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7476244688887263232",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-agenticdashboard-activity-7476244688887263232-beae",
            "title": "",
            "text": "In a sticky situation with a customer who get charged twice? 🫣\n\nRay's got you covered.\n\nRazorpay's Agentic Dashboard spots duplicate payments, flags them instantly, and walks you through the refund, in under a minute.\n\nNo digging. No delays. Just get it done.\n\n#razorpay #agenticdashboard",
            "media_urls": [],
            "hashtags": [
              "razorpay",
              "agenticdashboard"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-06-26T06:37:15Z",
            "observed_at": "2026-07-02T15:19:12Z"
          }
        ],
        "profile": {
          "name": "Razorpay",
          "linkedin_slug": "razorpay",
          "recorded_sector": "HRTech",
          "hq_country": "India",
          "followers": 1252056,
          "employee_count": 4052,
          "company_size": "1,001-5,000",
          "observed_reactions": 719,
          "observed_comments": 25,
          "observed_post_count": 8,
          "observed_at": "2026-07-02T15:19:12Z"
        },
        "coverage": {
          "profile_history": {
            "status": "available"
          },
          "recent_posts": {
            "status": "available"
          }
        },
        "notes": [
          "Stored LinkedIn observations; employee_count is observed platform headcount, not audited payroll.",
          "Recent means newest stored posts, not a live feed. Observation time differs from publication time.",
          "Post counters are latest stored values, not sums across crawls. Source zeros can include parser defaults.",
          "Negative source counters become null. Profile reaction/comment totals cover the observed page cards, not lifetime engagement.",
          "Recorded sector is a source label and can disagree with the company classification."
        ]
      }
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "social": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/linkedin/profile_history": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/linkedin/recent_posts": {
          "available": 8,
          "returned": 8,
          "truncated": false
        },
        "/value/linkedin/recent_posts/0/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/0/hashtags": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/linkedin/recent_posts/1/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/1/hashtags": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/linkedin/recent_posts/2/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/2/hashtags": {
          "available": 4,
          "returned": 4,
          "truncated": false
        },
        "/value/linkedin/recent_posts/3/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/3/hashtags": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/linkedin/recent_posts/4/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/4/hashtags": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/linkedin/recent_posts/5/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/5/hashtags": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/linkedin/recent_posts/6/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/6/hashtags": {
          "available": 4,
          "returned": 4,
          "truncated": false
        },
        "/value/linkedin/recent_posts/7/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/7/hashtags": {
          "available": 2,
          "returned": 2,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:26:09.902949+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

<a id="linkedin-professional"></a>

### LinkedIn-associated professional data: education and experience

**`POST /v1/people/search`** · MCP **`search_people`** ·
[Endpoint details](reference/search_people.md) · [Captured JSON](examples/search_people.json).

The named-person search returns one recorded Satya Nadella profile with a LinkedIn
URL, title, company domain, education entries, experience summaries, professional
ranking fields and investor attributes. The displayed record is the captured Radar
response, not a live verification of his current positions.

`skills` is empty in this particular record; it does not establish that the person
has no skills. Education years are empty strings where no year was returned.
Experience entries containing “present” remain source text and may be stale.
`total_estimate=5` is a search estimate, not five returned people or five confirmed
identities. Review identity and affiliation before joining a person to a company.

People cards have bounded source summaries. Use `get_company_team` with
`group=professionals` when exact recorded company-domain affiliation is required;
plain people search supports company-name/domain prefixes. For contact values,
pass an accepted returned person ID to the separately scoped
[person contact endpoint](CONTACTS.md); `contact_gated` does not contain the contacts.

Exact captured request:

<!-- company-depth-request: search_people.json -->
```json
{
  "name": "Satya Nadella",
  "limit": 1
}
```

Captured **2026-09-20T04:58:42.493744+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: search_people.json -->
```json
{
  "ok": true,
  "feature": "search_people",
  "data": {
    "people": [
      {
        "id": "6a1d2c3900edf351ec4270fc",
        "name": "Satya Nadella",
        "headline": "Chairman & CEO @ Microsoft",
        "current_title": "Chairman & CEO",
        "current_company": "Microsoft",
        "current_company_domain": "microsoft.com",
        "location": "Redmond, United States",
        "gender_t5": "unknown",
        "image_url": "/people_logo?id=6a1d2c3900edf351ec4270fc",
        "summary": "Current CEO at Microsoft, where our mission is to empower every person and every organization on the planet to achieve more. Joined Microsoft in 1992, and have held a variety of roles, most recently executive vice president of Microsoft's Cloud and Enterprise group, prior to beco…",
        "people_types": [
          "Angel Investor"
        ],
        "skills": [],
        "education": [
          {
            "institution": "Manipal",
            "degree": "BE",
            "years": ""
          },
          {
            "institution": "UWM",
            "degree": "Master of Computer Science",
            "years": ""
          },
          {
            "institution": "The University of Chicago",
            "degree": "MBA",
            "years": ""
          }
        ],
        "top_experience": [
          {
            "title": "Chairman & CEO",
            "company": "Microsoft",
            "years": "2014–present"
          },
          {
            "title": "member board of trustees",
            "company": "university of chicago",
            "years": "2018–present"
          },
          {
            "title": "board member",
            "company": "starbucks",
            "years": "2017–present"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/satyanadella",
        "twitter_url": "https://twitter.com/satyanadella",
        "scores": {
          "people_rank": 97.27,
          "founder_rank": null,
          "executive_rank": 99.97,
          "investor_rank": 98.38,
          "college_rank": 94.62,
          "experience_rank": 99.14
        },
        "founder": null,
        "investor": {
          "num_investments": 4,
          "total_invested_usd": null
        },
        "contact_gated": true
      }
    ],
    "total_estimate": 5,
    "total_capped": false,
    "access": {
      "plan": "free",
      "results_per_query": 50,
      "searches_per_month": 50,
      "anonymous": true
    },
    "plan": "free",
    "searches_remaining": 50,
    "page": 0,
    "page_size": 1,
    "partial_timeout": false
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:59:24.776366+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

<a id="business-classification"></a>

### Business data: sectors, feeds and revenue models

**`POST /v1/companies/field`** · MCP **`get_company_field`** ·
[Endpoint details](reference/get_company_field.md) · [Captured JSON](examples/fields/razorpay.com-classification.json).

Razorpay's classification field illustrates business-data depth beyond a company
name: FinTech and Enterprise Applications sectors, Payments/Banking Tech/HRTech
markets, primary and other feeds, business models, revenue models, company types
and source classification flags. All captured arrays are retained below.

These are overlapping source taxonomies, not mutually exclusive segments. A
subscription revenue model is not a revenue amount, and “SaaS” or “Startup” flags
do not independently establish a current business status. Stored profile industry
labels can differ from the company-search dropdown vocabulary; use
`company_filter_options` for the exact search field rather than copying an arbitrary
profile label into `filters.industries`. See the [filter audit](FILTER_AUDIT.md).

Exact captured request:

<!-- company-depth-request: fields/razorpay.com-classification.json -->
```json
{
  "domain": "razorpay.com",
  "field": "classification",
  "item_limit": 100
}
```

Captured **2026-09-21T04:08:57.262999+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: fields/razorpay.com-classification.json -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "razorpay.com",
    "company_id": "2gowls1wmc",
    "field": "classification",
    "value": {
      "sectors": [
        "FinTech",
        "Enterprise Applications"
      ],
      "markets": [
        "Payments",
        "Banking Tech",
        "HRTech"
      ],
      "feeds": {
        "primary": [
          "Payments",
          "Banking Tech",
          "HRTech"
        ],
        "other": [
          "Business Payments Solutions",
          "Commerce Enablers",
          "Enterprise Tech - India",
          "FinTech - India",
          "Enterprise Tech - Karnataka",
          "SaaS - India",
          "SaaS",
          "Enterprise Software",
          "FinTech SaaS",
          "Cloud Banking",
          "CFO Stack",
          "Embedded Finance",
          "Y Combinator Batches",
          "Banking as a Service",
          "Open Banking",
          "Banking Tech - India",
          "Payroll Management",
          "HR SaaS"
        ]
      },
      "business_models": [
        "Business Payments",
        "Diversified",
        "Payments",
        "Gateway",
        "Accounting Solutions",
        "Procure to Pay",
        "Account Payables",
        "Invoice Processing"
      ],
      "revenue_models": [
        "subscription"
      ],
      "industries": [
        "computer software"
      ],
      "company_types": [
        "Startup"
      ],
      "flags": {
        "Tech": "YES",
        "Consumer": "NO",
        "Enterprise": "YES",
        "Marketplace": "NO",
        "SaaS": "YES",
        "Software": "YES",
        "Social Impact": "NO",
        "Blockchain": "NO",
        "Tech Hardware": "NO",
        "Artificial Intelligence": "Untagged",
        "Agentic AI": "Untagged"
      }
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "classification": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/sectors": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/markets": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/feeds/primary": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/feeds/other": {
          "available": 18,
          "returned": 18,
          "truncated": false
        },
        "/value/business_models": {
          "available": 8,
          "returned": 8,
          "truncated": false
        },
        "/value/revenue_models": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/industries": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/company_types": {
          "available": 1,
          "returned": 1,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T04:08:57.262999+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

<a id="technology-stack"></a>

### Technology data: website stack and dated observations

**`POST /v1/companies/field`** · MCP **`get_company_field`** ·
[Endpoint details](reference/get_company_field.md) · [Captured JSON](examples/fields/stripe.com-technology.json).

Stripe's technology field contains 35 merged website-stack entries and 32 dated
observed technologies in this capture. The separate `technographics` array is empty.
That difference is visible in `coverage.arrays` and must not be erased by combining
every source array into an unexplained technology count.

The response preserves the full returned stack, the observation date and update
date. Detected website technologies do not enumerate every internal business
system or establish purchase intent. The [technology and traffic guide](guides/technology-traffic-data-api.md)
explains discovery filters and the distinction between source observations and a
current technical audit.

Exact captured request:

<!-- company-depth-request: fields/stripe.com-technology.json -->
```json
{
  "domain": "stripe.com",
  "field": "technology",
  "item_limit": 100
}
```

Captured **2026-09-21T04:08:57.286726+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: fields/stripe.com-technology.json -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "stripe.com",
    "company_id": "1x532zlgk5",
    "field": "technology",
    "value": {
      "website_stack": [
        "algolia",
        "amazon cloudfront",
        "amazon s3",
        "amazon web services",
        "apple icloud mail",
        "bootstrap",
        "cart functionality",
        "cloudflare",
        "cloudflare bot management",
        "contentful",
        "core-js",
        "digicert",
        "docusign",
        "envoy",
        "google analytics",
        "google workspace",
        "hcaptcha",
        "hsts",
        "jquery",
        "jquery migrate",
        "jquery ui",
        "lodash",
        "next.js",
        "nginx",
        "node.js",
        "open graph",
        "priority hints",
        "prism",
        "pwa",
        "react",
        "rss",
        "sentry",
        "stripe",
        "three.js",
        "webpack"
      ],
      "technographics": [],
      "observed_technologies": [
        "algolia",
        "amazon cloudfront",
        "amazon s3",
        "amazon web services",
        "apple icloud mail",
        "bootstrap",
        "cart functionality",
        "cloudflare",
        "cloudflare bot management",
        "core-js",
        "docusign",
        "google analytics",
        "google workspace",
        "hcaptcha",
        "hsts",
        "jquery",
        "jquery migrate",
        "jquery ui",
        "lodash",
        "next.js",
        "nginx",
        "node.js",
        "open graph",
        "priority hints",
        "prism",
        "pwa",
        "react",
        "rss",
        "sentry",
        "stripe",
        "three.js",
        "webpack"
      ],
      "observed_at": "2026-05-01"
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "technology": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/website_stack": {
          "available": 35,
          "returned": 35,
          "truncated": false
        },
        "/value/technographics": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/observed_technologies": {
          "available": 32,
          "returned": 32,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T04:08:57.286726+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

<a id="website-traffic"></a>

### Traffic data: visits, countries, keywords and engagement

**`POST /v1/companies/field`** · MCP **`get_company_field`** ·
[Endpoint details](reference/get_company_field.md) · [Captured JSON](examples/fields/swiggy.com-traffic.json).

Swiggy's captured traffic field includes 16,549,799 visits dated May 1, 2026, global
and country ranks, keywords, engagement measures and country-level audience shares.
The India share is `0.9678`, a fraction corresponding to 96.78%; it is not 0.9678%.
The bounce value is also returned as a fraction.

These observations describe website traffic, not verified unique customers or app
usage. The five returned audience countries are not proof that the entire audience
is represented. Retain the date and source values; do not present them as today's
traffic or add overlapping website and app figures into one audience number.

Exact captured request:

<!-- company-depth-request: fields/swiggy.com-traffic.json -->
```json
{
  "domain": "swiggy.com",
  "field": "traffic",
  "item_limit": 100
}
```

Captured **2026-09-21T04:08:57.310255+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: fields/swiggy.com-traffic.json -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "swiggy.com",
    "company_id": "tiwgsjxo90",
    "field": "traffic",
    "value": {
      "authority": 83,
      "global_rank": 3127,
      "country_rank": 187,
      "country": "India",
      "visits": 16549799,
      "visits_date": "2026-05-01",
      "bounce": 0.6869,
      "ppv": 3.4375,
      "keywords": [
        {
          "k": "swiggy",
          "pos": 1,
          "vol": 2240000
        },
        {
          "k": "restaurants",
          "pos": 2,
          "vol": 11100000
        },
        {
          "k": "instamart",
          "pos": 1,
          "vol": 1000000
        }
      ],
      "audience": [
        {
          "cc": "IN",
          "country": "India",
          "share": 0.9678,
          "visits": 16017135
        },
        {
          "cc": "US",
          "country": "United States",
          "share": 0.01,
          "visits": 165660
        },
        {
          "cc": "GB",
          "country": "United Kingdom",
          "share": 0.006,
          "visits": 99162
        },
        {
          "cc": "KR",
          "country": "South Korea",
          "share": 0.0017,
          "visits": 27820
        },
        {
          "cc": "CA",
          "country": "Canada",
          "share": 0.0016,
          "visits": 26613
        }
      ]
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "traffic": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/keywords": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/audience": {
          "available": 5,
          "returned": 5,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T04:08:57.310255+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

<a id="business-events"></a>

### Business events: earnings, products, contracts and people changes

**`POST /v1/news/events`** · MCP **`search_business_events`** ·
[Endpoint details](reference/search_business_events.md) · [Captured JSON](examples/search_business_events.json).

This historical Microsoft query covers April 2026. It returned five news-derived
event records from an estimated 68, with a `by_type` breakdown spanning earnings,
key people, contracts, company announcements, lawsuits, layoffs, capital infusion,
M&A, a new product and an asset acquisition. The displayed page includes earnings
and product events; the broader breakdown is not the count of rows on that page.

Preserve event IDs, event type, company domain, the company's recorded role and
publication time. Publication time is not necessarily the date the business event
occurred. Multiple articles can describe one event, so five records do not establish
five distinct corporate actions. `resolved=false` means original article URL,
publisher and title were not joined into the event rows. Company associations
remain source-reported. Pass `next_cursor` unchanged while keeping the
same company, date window and other filters.

This successful September 20 capture used the actual News applications and live
queries with isolated test identity/quota dependencies. It is **historical integration
evidence**, not a fresh service-health check or a verified production News connection.
The later [50-scenario audit](SCENARIO_AUDIT.md) encountered an upstream News connection
failure. Several long headlines were omitted from the saved documentation capture;
the linked JSON lists those prose omissions and retains all event rows and fields
that survived that documented projection.

Exact captured request:

<!-- company-depth-request: search_business_events.json -->
```json
{
  "company": "microsoft.com",
  "limit": 5,
  "date_from": "2026-04-01",
  "date_to": "2026-04-30"
}
```

Captured **2026-09-20T10:58:50.858162+00:00**, mode **`live_data_integration`**,
HTTP **200**. Response:

<!-- company-depth-response: search_business_events.json -->
```json
{
  "ok": true,
  "feature": "search_business_events",
  "data": {
    "items": [
      {
        "id": "69f880adbbf1d31455966a69",
        "event_type": "earnings",
        "role": "primary",
        "domain": "microsoft.com",
        "published_at": "2026-04-30T22:16:00"
      },
      {
        "id": "69f8804a43843dd771ce7099",
        "event_type": "earnings",
        "role": "primary",
        "domain": "microsoft.com",
        "published_at": "2026-04-30T21:20:25"
      },
      {
        "id": "69f8842343843dd771d08309",
        "event_type": "new_product",
        "role": "primary",
        "domain": "microsoft.com",
        "published_at": "2026-04-30T20:11:29"
      },
      {
        "id": "69f8a657bbf1d314559a2139",
        "event_type": "earnings",
        "role": "primary",
        "domain": "microsoft.com",
        "published_at": "2026-04-30T16:36:27"
      },
      {
        "id": "69f881798937ef12fc07b478",
        "headline": "Microsoft (MSFT 3.90%) just reported a quarter that beat on basically every number that matters.",
        "event_type": "earnings",
        "role": "primary",
        "domain": "microsoft.com",
        "published_at": "2026-04-30T13:41:49"
      }
    ],
    "returned": 5,
    "total_estimate": 68,
    "next_cursor": "eyJ2IjoxLCJ0IjoiZXYiLCJzIjoibmV3ZXN0IiwiZCI6IjIwMjYtMDQtMzAgMTM6NDE6NDkiLCJpIjoiNjlmODgxNzk4OTM3ZWYxMmZjMDdiNDc4IiwiZG0iOiJtaWNyb3NvZnQuY29tIiwiZXQiOiJlYXJuaW5ncyIsInJvIjoicHJpbWFyeSJ9",
    "by_type": {
      "key_people": 17,
      "earnings": 16,
      "contracts": 13,
      "company_announcement": 6,
      "lawsuit": 5,
      "layoffs": 5,
      "capital_infusion": 2,
      "ma": 2,
      "new_product": 1,
      "asset_acquisition": 1
    },
    "limit": 5,
    "sort": "newest",
    "resolved": false
  },
  "window": {
    "since": "2026-04-01",
    "until": "2026-04-30",
    "days": 30,
    "data_through": "2026-05-05",
    "freshness": "this business dataset is available through 2026-05-05; company events, funding and company-linked news may have different latest available dates"
  },
  "meta": {
    "retrieved_at": "2026-09-20T10:58:50.858026+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI",
    "coverage": {
      "available": true
    }
  }
}
```

<a id="company-activity"></a>

### Company activity events: effective windows and pulse summaries

**`POST /v1/companies/events`** · MCP **`get_company_events`** ·
[Endpoint details](reference/get_company_events.md) · [Captured JSON](examples/get_company_events.json).

The company event endpoint is distinct from the dated business-news event search.
This captured 30-day Microsoft request has an empty `events` array and
`truncated=true`, while its `pulse` describes a separate 360-day window. The pulse
contains 345 events over that longer window, a derived momentum measure, leadership
signals and top event drivers.

Do not merge those windows or convert the empty 30-day array into “no company
activity”. Source freshness reports the latest event date separately from insertion
time; recently inserted data need not describe a recent event. Scores, badges and
sentinel-looking recency values are source assessments, not verified events or
financial facts. Preserve them for review with their window and access limits.

For financial announcements, follow through to [financial statements](guides/financial-data-api.md)
and [financial news](guides/financial-news-api.md). For reported transactions, use
[funding rounds](guides/startup-funding-data-api.md) and
[funding-news evidence](guides/funding-news-api.md); an announcement is not by itself
proof of a completed transaction.

Exact captured request:

<!-- company-depth-request: get_company_events.json -->
```json
{
  "domain": "microsoft.com",
  "days": 30,
  "limit": 2
}
```

Captured **2026-09-20T04:58:42.493744+00:00**, mode **`live_gateway`**,
HTTP **200**. Response:

<!-- company-depth-response: get_company_events.json -->
```json
{
  "ok": true,
  "feature": "get_company_events",
  "data": {
    "freshness": {
      "future_rows_count": 0,
      "future_rows_filtered": false,
      "latest_event_date": "2026-05-04",
      "latest_inserted_at": "2026-09-20T05:30:00+05:30"
    },
    "truncated": true,
    "buckets_by_month": {},
    "domain": "microsoft.com",
    "events": [],
    "plan": "free",
    "pulse": {
      "badges": [
        "Leadership Turnover"
      ],
      "ceo_transitions": 2,
      "churn_penalty": 10,
      "days_since_latest": 999,
      "event_variety_360d": 6,
      "events_30d_fresh": 0,
      "events_360d": 345,
      "events_prev_360d": 425,
      "label": "Quiet",
      "leadership_churn": true,
      "leadership_churn_level": "elevated",
      "momentum_pct": -18.8,
      "opportunity_score": 0,
      "risk_score": 0,
      "score": 36,
      "top_drivers": [
        {
          "count": 186,
          "event_type": "key_people",
          "label": "Key People Movement"
        },
        {
          "count": 74,
          "event_type": "earnings",
          "label": "Earnings Release"
        },
        {
          "count": 61,
          "event_type": "company_announcement",
          "label": "Company Announcement"
        }
      ],
      "window_days": 360
    },
    "totals_by_type": {},
    "window_days": 30
  },
  "window": {
    "data_through": "2026-05-04",
    "effective_days": 30,
    "requested_days": 30
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:46.111118+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```
