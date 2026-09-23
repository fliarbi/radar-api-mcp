# Company enrichment API for firmographic and business context

Company enrichment adds information to a company you already know. Radar's
enrichment workflow begins with a website domain and combines a company profile
with available legal, hiring, reputation, digital-presence, innovation and social
activity information. It can support CRM account research or an internal business
intelligence application without creating a new company-discovery workflow.

## Enrich an existing company record

Call `get_company_enrichment` using `POST /v1/companies/enrichment`:

```json
{"domain":"microsoft.com"}
```

Retrieve `get_company` separately when you also need the base company card. The
enrichment endpoint and profile endpoint provide different views; do not assume
that one response is a complete replacement for the other.

For a CRM integration, store the normalized domain, the response retrieval time
and the returned sections together. Map each available value to a specific field
in your own account model. Leave existing values intact when the API returns no
coverage, instead of overwriting them with empty strings or zero.

## Interpret enrichment signals carefully

Hiring activity describes observed job information, not necessarily total
headcount growth. Digital-presence details describe available evidence, not a
guaranteed current technology inventory. Reputation or intelligence narratives
are derived assessments, while legal identifiers and source-backed financial
figures have different meanings and validation needs.

Some upstream enrichment sections do not distinguish absent data from a section
that failed to load. The gateway therefore cannot certify that every omitted
section represents a negative finding. Preserve its coverage notes in a research
view and allow the user to inspect other sources.

## Common implementation questions

**Does enrichment reveal personal emails or phone numbers?** No. The gateway
omits email/phone values from enrichment. Professional discovery and explicitly
scoped company/person contact retrieval are separate operations; see [contacts](../CONTACTS.md).

**Can I enrich a list of domains?** Issue individual requests within account rate
and concurrency limits. There is no arbitrary bulk-enrichment or full-database
export endpoint in this preview. `compare_companies` supports two to five domains
for a specific comparison workflow, not unrestricted enrichment batches.

**Does paying for API credits unlock all enrichment?** No. API credits control
gateway usage. The linked Radar account and upstream services still determine
the data and features available to that request.

Continue with [company data](company-data-api.md), [hiring signals](hiring-signals-jobs-api.md),
[company monitoring](company-monitoring-api.md), or [API keys](api-keys-authentication.md).

## Social references and explicit contact retrieval

For company LinkedIn/X/Facebook/blog URLs, use the selected `social` company field;
for a person's references, inspect their professional card. The
[social-link guide](linkedin-social-data-api.md) distinguishes those references
from enrichment social-activity metrics. Emails and phone numbers use
[separate entitled lookups](../CONTACTS.md), with company versus person attribution
preserved. [Founder linkage](founder-contact-data-api.md) is a separate identity step.

<!-- captured-workflow -->
## Map enrichment into a CRM without losing provenance

For each destination field, decide which enrichment section is allowed to supply
it and how old that observation may be. A legal registration belongs to legal
identity, while a digital visits estimate belongs to audience context. Neither is
a substitute for revenue, paid customers or employee count. Keep the section's
measurement date beside its value; the gateway retrieval timestamp only tells you
when the response was fetched.

The captured response includes website visits dated May 2026 and a source-specific
reputation aggregate. A score of 1.2 with a review count has meaning only within
that review source and scale; it is not Radar's overall rating of the business.
The sample also includes more than one legal entry. Review whether each entry
actually belongs to the target entity before copying a registration number into
an account record.

For an application update, write known values into their mapped fields and retain
the last verified value when a new section is absent. Record an unknown-coverage
state instead of replacing a missing section with zero visits or an empty legal
name. The source currently cannot always distinguish missing enrichment from a
failed subsection, so `has_data=true` is an existence signal for some data, not a
certificate that every subsection is complete.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/enrichment`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_company_enrichment -->
```json
{
  "domain": "stripe.com"
}
```

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
        "Atlanta",
        "New York"
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
        "Writer, Content Marketing",
        "Technical Account Manager",
        "Data Scientist",
        "AMER GTM Finance & Strategy Segment Lead",
        "Manager, Technical Account Management",
        "Data Analyst",
        "Company Strategy & Operations",
        "Specialist Solutions Architect, Radar (FraudRisk)"
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
    "retrieved_at": "2026-09-23T06:47:28.920757+00:00",
    "partial": false,
    "notes": [
      "Absent enrichment sections have unknown coverage; the source does not distinguish missing data from a failed section."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:28.920961+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_enrichment.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Stripe capture returned digital traffic and audience, hiring history and roles, innovation and patents, social engagement, activity, legal entries, reputation aggregates and share-of-voice peers. All these business-data sections and their array rows are shown. Individual review snippets are excluded from documentation reproduction.

See the [complete get_company_enrichment endpoint reference](../reference/get_company_enrichment.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
