# Company data depth: real sectors, feeds, founders, technology, traffic and apps

Radar's company profile API now reads the grouped company record and associated
enrichment. The earlier gateway used a shortlist card, and its documentation then
removed fields and cut arrays to two items. Those choices understated the available
data. The API now exposes seventeen selectable sections, and documentation preserves
all captured business fields and all returned array rows.

## Three live examples with meaningful depth

These are measured fields from authenticated local API calls on **2026-09-20**.
They are source observations, not independently audited current company facts.
Traffic dates and website crawl dates are returned separately; downloads are
aggregate source totals, not active users or downloads in a stated recent month.

| Complete captured company JSON | Sectors | Primary / other feeds | Founders | Stack entries | Visits in source observation | Apps / downloads |
|---|---:|---:|---:|---:|---:|---:|
| [Razorpay](examples/profiles/razorpay.com.json) | 2 | 3 / 18 | 2 | 70 | 23,096,401 | 5 / 3,780,330 |
| [Stripe](examples/profiles/stripe.com.json) | 1 | 1 / 10 | 2 | 35 | 190,046,716 | 2 / 3,000,300 |
| [Swiggy](examples/profiles/swiggy.com.json) | 1 | 2 / 13 | 3 | 72 | 16,549,799 | 4 / 382,800,000 |

Each linked file contains the exact request, response, capture date, omission paths
and checksums. No company array is cut to two entries. The longer review snippets
are omitted from documentation reproduction, with their paths recorded explicitly.
The [profile endpoint reference](reference/get_company.md) shows the complete primary
Razorpay response inline, including sections beyond the five highlighted below.

## Retrieve the data

```bash
curl --fail-with-body "$RADAR_API_URL/v1/companies/profile" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"razorpay.com","item_limit":100}'
```

With the detailed store connected, omitting `sections` requests all seventeen.
For a focused integration, use `sections=["classification","people","technology",
"traffic","apps"]`. This is one `get_company` operation and one successful-operation
credit in account mode. REST and MCP share the same result; MCP wraps this body
in `arguments.request`. `item_limit` defaults to 100 per array and supports 1–250.
Every capped array reports its available and returned count in `coverage.arrays`.
None of the arrays in these three captures needed truncation.

The operator enables this data connection with `RADAR_PROFILE_MONGO_URI`; caller
requests never accept database names, collection names, queries or connection
strings. An unconfigured deployment explicitly returns `profile_depth=card`.
See [private operator setup](OPERATIONS.md); these captures do not represent a
production deployment or public API launch.

## Classification is more than one industry label

`classification.sectors` contains practice-area labels. `markets` preserves the
existing primary-market convention, while `feeds.primary` and `feeds.other` make
the richer feed hierarchy explicit. Business models describe how the company
operates; revenue models describe its monetization categories. Flags retain their
source values such as YES, NO or Untagged instead of turning unknown into false.

Razorpay's full captured classification, founder, technology, traffic and app blocks:

<!-- depth-highlight: razorpay.com -->
```json
{
  "classification": {
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
  "people": {
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
  "technology": {
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
  "traffic": {
    "authority": 70,
    "global_rank": 2108,
    "country_rank": 135,
    "country": "India",
    "visits": 23096401,
    "visits_date": "2026-05-01",
    "bounce": 0.6271,
    "ppv": 3.3131,
    "keywords": [
      {
        "k": "tripura university question paper 2018 pdf",
        "pos": 8,
        "vol": 5000000
      },
      {
        "k": "gst search",
        "pos": 6,
        "vol": 823000
      },
      {
        "k": "gst number search",
        "pos": 6,
        "vol": 550000
      }
    ],
    "audience": [
      {
        "cc": "IN",
        "country": "India",
        "share": 0.8925,
        "visits": 20613671
      },
      {
        "cc": "US",
        "country": "United States",
        "share": 0.0294,
        "visits": 678910
      },
      {
        "cc": "MY",
        "country": "Malaysia",
        "share": 0.0184,
        "visits": 424855
      },
      {
        "cc": "BD",
        "country": "Bangladesh",
        "share": 0.0056,
        "visits": 129752
      },
      {
        "cc": "CA",
        "country": "Canada",
        "share": 0.0055,
        "visits": 127382
      }
    ]
  },
  "apps": {
    "count": 5,
    "downloads": 3780330,
    "weighted_rating": 3.799999952316284
  }
}
```

## Founders and professional context

Razorpay's record names Shashank Kumar as Co-Founder & Managing Director and Harshil
Mathur as Co-Founder & CEO. The `founders` array is selected from key people whose
source designation contains “founder”; it is not an independent current-role audit.
Stripe has four key-person records and two matching founders. Other executive
roles remain in `key_people`, including source labels that explicitly describe
former positions. Professional names and roles are separate from contact reveal.

## Technology, website quality and traffic are different observations

`technology.website_stack` retains the grouped technology list. The observed web
scan can have a different count: Razorpay has 70 merged stack entries and 69 in its
observed-technology array. The API preserves both and the observation date.
`technographics` can separately identify a category and technology, such as an
infrastructure platform. No technology name is inferred from the company's sector.

`web_presence` adds rank, CDN, performance measurements, SEO signals, structured
data, schema types and a derived digital-presence score. `traffic` instead contains
visits, observation date, bounce fraction, pages per visit, search keywords and
country audience shares. A rank is not a visit count, and visits are not unique
customers. Numeric fractions are retained as fractions, not silently multiplied
into percentages or combined into an invented growth rate.

## App metrics have explicit scope

`apps.count`, `downloads` and `weighted_rating` are aggregate source fields. These
records do not expose an app-by-app list, package IDs, store URLs or rating dates;
the API does not invent them. Preserve the full returned numeric rating or round it
only for presentation. Do not interpret a missing rating as zero or total downloads
as monthly active users.

## Products, hiring, patents and social data

Stripe's populated product and social blocks illustrate additional depth:

<!-- depth-highlight: stripe.com -->
```json
{
  "products": [
    "Payments",
    "Payouts",
    "API-based integration",
    "Low- to no-code solutions"
  ],
  "social": {
    "links": {
      "linkedin": "https://linkedin.com/company/stripe",
      "x": "https://twitter.com/stripe",
      "facebook": "https://facebook.com/stripehq",
      "blog": "http://stripe.com/blog"
    },
    "followers": 1528731,
    "posts_12m": 4,
    "engagement_per_post": 0,
    "rate": 0.0,
    "cadence_per_month": 0.3,
    "sector": "Payments",
    "industry_median_rate": 0.00567,
    "ratio_vs_median": 0.0,
    "band": "below the industry typical range"
  }
}
```

The complete Stripe example also contains hiring totals and first/last dates,
monthly/yearly counts, roles and locations; innovation includes patent-family,
grant, citation, year and area observations. Those represent the source's stored
history and aggregates, not a guarantee that every vacancy is still open or that
every patent represents a current commercial product. The detailed profile and
[enrichment endpoint](reference/get_company_enrichment.md) both expose this context.

## Field dictionary and availability

| Section | Content | Important distinction |
|---|---|---|
| `classification` | Sectors, primary/other feeds, business/revenue models, industries, company types, flags | Untagged is not NO |
| `people` | Key people, designations, derived founder subset, background categories | Source role is not a verified current appointment |
| `technology` | Merged stack, observed technologies, technographics, observation date | Merged and observed counts can differ |
| `web_presence` | Rank, CDN, performance, SEO, structured data, score, crawl date | Measurements and derived labels retain separate meanings |
| `traffic` | Visits/date, countries, keywords, bounce and pages per visit | Traffic is not revenue or customer count |
| `apps` | Count, downloads, weighted rating | Aggregates, not a per-app roster |
| `products` | Returned product labels | Empty source list is not proof of no products |
| `geography` | Headquarters, locations, served geographies, coordinates, business addresses | Headquarters and markets served are different |
| `social` | Profile links, followers, engagement, posting cadence and benchmarks | Source dates/denominators may differ |
| `lifecycle` | Stage, financing/ownership status and public/deadpool indicators | Unknown values remain unknown |
| `legal` | Legal names, registration identifiers, registrars and countries | Review entity associations before joining filings |
| `assessments` | Completion, finance, scalability, momentum and other scores | Derived scores are not financial amounts |
| `hiring` | Counts, dates, history, roles and locations | Stored observations do not certify current vacancies |
| `innovation` | Patent families, grants, citations, years, areas and notable items | Patents are not a complete product inventory |
| `activity` | Dated source activity entries | Available history varies by company |
| `reputation` | Source review aggregates and counts | Documentation omits individual review snippets |
| `share_of_voice` | Peers and available audience/review/follower shares | Denominator is the supplied comparison cohort |

`coverage.sections` distinguishes available, not_observed, unavailable and partial.
Empty arrays and numeric zero remain valid source values. Database failures return
503; they do not silently become an empty company. If optional enrichment fails,
the available base profile survives with explicit partial coverage.

Several company records can share a domain. In that case, the detailed lookup
returns **409 `ambiguous_company`** and accepts a public `company_id` alongside
the domain for disambiguation. A wrong ID/domain pair cannot return another entity.
Financial history and estimated-revenue access continue through the existing
entitlement-checked financial endpoint; adding profile depth does not unlock them.

Related: [company lookup](guides/company-data-api.md), [enrichment](guides/company-enrichment-api.md),
[financial data](guides/financial-data-api.md), [all endpoint outputs](reference/README.md).
