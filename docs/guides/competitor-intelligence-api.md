# Competitor intelligence API and company financial comparisons

Radar offers market-based competitor discovery and a separate company comparison
operation. Use competitor discovery to find candidates in a named market; use
comparison to review selected companies' profiles, financial evidence and derived
intelligence. Keeping these stages separate helps avoid treating an automatically
returned peer as a proven direct competitor.

## Discover peers in a market

`find_competitors` maps to `POST /v1/companies/competitors`:

```json
{"market":"Software","per_stage":5}
```

An optional `business_model` can narrow the query. Results are grouped by funding
stage; `per_stage` accepts 3 through 10. Start with a specific market label from
industry discovery when possible. Review each candidate's description, location
and product context before including it in an analysis.

## Compare selected companies

`compare_companies` maps to `POST /v1/companies/compare`:

```json
{"domains":["microsoft.com","salesforce.com"]}
```

The example demonstrates the input shape, not a claim that every line of business
is comparable. Supply two to five distinct domains. The response keeps each
company's profile, financials and intelligence in separate sections, with missing
coverage and section failures explicitly indicated.

In account mode, the gateway reserves three credits per company and refunds
failed sections. It does not calculate a cross-company total, rank investments
or normalize every company's fiscal calendar into a common reporting period.

## Read financial and intelligence sections differently

Financial metrics retain source types and currency information. Company scores,
risk narratives and other intelligence are derived assessments. Do not present
a score as a filed financial fact, and do not compare two fiscal-year labels
without inspecting the underlying dates and available coverage.

If one company's financial section is unavailable, preserve that gap in your
comparison table. Substituting zero would falsely imply a measured value and can
distort growth or margin calculations. Retrieve associated company events and
news separately when they help explain a difference.

## Useful applications

This workflow can support a business-development shortlist, a product-market
landscape review or an internal research brief. It does not replace source review
or establish that the returned list contains every relevant competitor.

Related: [company search](company-search-api.md), [financial data](financial-data-api.md),
[financial statements](company-financial-statements-api.md), [company monitoring](company-monitoring-api.md).

<!-- captured-workflow -->
## Choose peers before comparing financial and derived evidence

Competitor discovery accepts a market label, not a company domain. Start by deciding
what the firms compete to supply, which buyers they serve and which geography
matters. The updated Payments example returns three peers in each of five stage
groups. Its summary also covers stages outside those five groups, so the summary
total is not the length of the delivered company arrays. The earlier broad Software
query was empty; it did not establish an absence of competitors.

After reviewing candidate companies, pass two to five distinct domains to
`compare_companies`. Each company has separate profile, financial and intelligence
sections. Display a revenue value with its fiscal period and source type; display
an intelligence score with its derived label and computation date. The API does not
convert those different quantities into a single investment ranking.

The captured Razorpay/Stripe comparison returned both companies' research
sections, but corporate identity and fiscal alignment still require review. A
missing metric should remain unknown even if the other company supplies it.
If one section fails, keep the successful peer's evidence visible and label the
gap. Account mode reserves three credits per requested company and refunds failed
sections, so the final billing metadata is the appropriate source for actual
charged usage rather than multiplying every partial section as a success.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/competitors`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: find_competitors -->
```json
{
  "market": "Payments",
  "per_stage": 3
}
```

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

See the [complete find_competitors endpoint reference](../reference/find_competitors.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
