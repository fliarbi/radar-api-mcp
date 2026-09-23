# Company technology stack, website traffic and digital presence data API

Use company digital evidence to research installed technologies, market
classification, website reach and mobile products. Each section is fetched
explicitly after company lookup; a list search does not return every detail field.
The company domain connects these observations, but their timestamps and coverage
can differ.

## Classification: industry, sector, feeds and business models

```json
{"domain":"razorpay.com","field":"classification","item_limit":100}
```

Send this body to **`POST /v1/companies/field`**, MCP `get_company_field`.
[Example 47](../scenarios/47-company-taxonomy.md) preserves the actual classification
hierarchy and business fields. Industry (`industries`), broad practice-area sector
(`sectors`) and more specific feed/market (`markets`) are different query dimensions.
A business model describes the activity, while a revenue model describes how the
company earns money. Do not move a discovered feed label into an industry filter.
Use `company_filter_options` for the particular field you will filter.

## Technology stack and implementation evidence

```json
{"domain":"stripe.com","field":"technology","item_limit":100}
```

[Example 48](../scenarios/48-company-technologies.md) includes all captured structured
technology fields and array entries. Technologies can be detected website software
or source company classifications; they do not necessarily identify every internal
system. Inspect the field's status and update date before describing a technology
as currently installed. A missing observation does not establish that the business
has never used a product.

To find candidate companies, use `filters.technologies` in company search, with
values discovered by `company_filter_options`. Review the detailed evidence before
using a detected product as a migration-sales signal. Recorded usage does not
establish procurement authority, renewal timing or purchase intent.

## Traffic and web presence are separate sections

```json
{"domain":"swiggy.com","field":"traffic","item_limit":100}
```

```json
{"domain":"swiggy.com","field":"web_presence","item_limit":100}
```

[Example 49](../scenarios/49-company-traffic.md) retains the captured traffic data.
The [complete company field collection](../COMPANY_DATA_DEPTH.md) separately shows
web presence. Preserve available measurement periods, geographic breakdowns,
source update dates and missing values. Website traffic is neither revenue nor
verified unique paying customers. Do not add overlapping traffic observations
across periods or devices without a known denominator.

Discovery supports web popularity, Core Web Vitals category, speed, SEO maturity,
structured-data maturity, business hints and web score bands. The `<40` score band
actually selects scores above zero and below 40; it does not include missing scores
or zero. These source categories are screening signals, not independent audits of
site quality. The [filter audit](../FILTER_AUDIT.md) records exact band boundaries.

## Join mobile apps, hiring and financial evidence

Use [company apps and app details](apps-data-api.md) to resolve developer website
hosts to products, then retrieve dated install history, ratings and monetization.
A store install count does not measure website traffic. Mobile-growth buckets
refer to source derived growth, while the app field exposes the observations used
to calculate growth and their reliability flags.

For investment potential, combine digital evidence with
[dated financials](financial-filters-data-api.md), company history and funding.
For sales research, combine it with [hiring demand](hiring-signals-jobs-api.md) and
[company opportunity presets](potential-company-data-api.md). Keep each signal's
date, source and limitation; several weak signals do not become verified buying
intent merely because they appear in the same response.

<!-- scenario-links -->
## Executed scenarios for this workflow

- [47-company-taxonomy: Retrieve Razorpay sectors, primary feeds and other business classifications.](../scenarios/47-company-taxonomy.md)
- [48-company-technologies: Retrieve Stripe’s observed technologies with their available source structure.](../scenarios/48-company-technologies.md)
- [49-company-traffic: Retrieve Swiggy traffic and geography observations.](../scenarios/49-company-traffic.md)

<!-- captured-workflow -->
## Read a captured company technology section

The primary capture below is Razorpay technology, distinct from the Stripe technology request and Swiggy traffic request above. Each has its own executed example in the scenario collection. Preserve field status, update date and bounded-array coverage before interpreting missing observations.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/field`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_company_field -->
```json
{
  "domain": "razorpay.com",
  "field": "technology",
  "item_limit": 100
}
```

<!-- response-example: get_company_field -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "razorpay.com",
    "company_id": "2gowls1wmc",
    "field": "technology",
    "value": {
      "website_stack": [
        "amazon cloudfront",
        "amazon s3",
        "amazon web services",
        "angular",
        "animate.css",
        "antv g2",
        "apple icloud mail",
        "aws certificate manager",
        "bootstrap",
        "cart functionality",
        "cdnjs",
        "chakra ui",
        "chart.js",
        "cloudflare",
        "cloudflare bot management",
        "cloudflare browser insights",
        "core-js",
        "datadog",
        "emotion",
        "express",
        "facebook pixel",
        "font awesome",
        "framer sites",
        "google analytics",
        "google font api",
        "google sign-in",
        "google tag manager",
        "google workspace",
        "hotjar",
        "hsts",
        "http/3",
        "hubspot",
        "hubspot analytics",
        "hubspot chat",
        "jquery",
        "jquery cdn",
        "jsdelivr",
        "linkedin insight tag",
        "loadable-components",
        "lodash",
        "lottiefiles",
        "marked",
        "microsoft clarity",
        "next.js",
        "next.js app router",
        "nginx",
        "node.js",
        "open graph",
        "pdf.js",
        "preact",
        "priority hints",
        "pwa",
        "radix ui",
        "razorpay",
        "react",
        "react router",
        "recaptcha",
        "rss",
        "salesforce",
        "segment",
        "sentry",
        "shadcn/ui",
        "styled-components",
        "substack",
        "tailwind css",
        "typescript",
        "webpack",
        "yellow.ai",
        "zoho",
        "zone.js"
      ],
      "technographics": [],
      "observed_technologies": [
        "amazon cloudfront",
        "amazon s3",
        "amazon web services",
        "angular",
        "animate.css",
        "antv g2",
        "apple icloud mail",
        "bootstrap",
        "cart functionality",
        "cdnjs",
        "chakra ui",
        "chart.js",
        "cloudflare",
        "cloudflare bot management",
        "cloudflare browser insights",
        "core-js",
        "datadog",
        "emotion",
        "express",
        "facebook pixel",
        "font awesome",
        "framer sites",
        "google analytics",
        "google font api",
        "google sign-in",
        "google tag manager",
        "google workspace",
        "hotjar",
        "hsts",
        "http/3",
        "hubspot",
        "hubspot analytics",
        "hubspot chat",
        "jquery",
        "jquery cdn",
        "jsdelivr",
        "linkedin insight tag",
        "loadable-components",
        "lodash",
        "lottiefiles",
        "marked",
        "microsoft clarity",
        "next.js",
        "next.js app router",
        "nginx",
        "node.js",
        "open graph",
        "pdf.js",
        "preact",
        "priority hints",
        "pwa",
        "radix ui",
        "razorpay",
        "react",
        "react router",
        "recaptcha",
        "rss",
        "salesforce",
        "segment",
        "sentry",
        "shadcn/ui",
        "styled-components",
        "substack",
        "tailwind css",
        "typescript",
        "webpack",
        "yellow.ai",
        "zoho",
        "zone.js"
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
          "available": 70,
          "returned": 70,
          "truncated": false
        },
        "/value/technographics": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/observed_technologies": {
          "available": 69,
          "returned": 69,
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
    "retrieved_at": "2026-09-21T04:08:59.470819+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T04:08:59.471147+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_field.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The technology example preserves all seventy Razorpay stack entries with item_limit=100. Other company fields have separate real JSON captures.

See the [complete get_company_field endpoint reference](../reference/get_company_field.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
