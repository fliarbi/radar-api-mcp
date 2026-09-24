# Company search API: find companies by industry, location and business signals

Radar supports two company discovery methods: a structured company search API
for explicit filters and semantic company search for a natural-language business
description. Use structured filters when reproducibility matters; use semantic
search to explore an unfamiliar market and then inspect individual matches.

## Search a defined business segment

`search_companies` maps to `POST /v1/companies/search`:

```json
{"filters":{"industries":["Software"],"locations":["India"],"revenue_bands":["10m-100m"],"profitability":["profitable"]},"page":0,"limit":20}
```

The revenue band uses Radar's existing USD classification. It is not a newly
calculated annual revenue figure. For specific amounts and reporting periods,
retrieve the company's financial data after discovery.

Available filter families include company names, industries, sectors, markets,
business models, geography, size, funding stage, technologies, products, skills,
events, financing status and ownership status. The complete accepted names and
values are in the [capability schema](../CAPABILITIES.md), rather than a guessed
list of industry labels.

Use `company_filter_options` (`POST /v1/companies/filter-options`) with field
`industries` to discover the actual Radar industry vocabulary, including AdTech.
Select `sectors`, `markets` or another field to get that field's vocabulary.
The [filter audit](../FILTER_AUDIT.md) explains the source mappings.

Structured searches default to `match_mode=strict`: only source-labelled strict
rows are returned, and no rows qualify if the source stripped requested filters.
Set `match_mode=expanded` to deliberately include fallback candidates. Every card
has `match_tier`; unlabelled source rows are `unverified`. Matching metadata records
excluded rows and source tiers without exposing diagnostic queries.

The source can widen sparse searches through taxonomy, radius and semantic tiers.
[The 50-scenario audit](../SCENARIO_AUDIT.md) found US results in India searches
before matching metadata was preserved. Strict mode now excludes those results.
An empty strict page can still have `next_page`; source pagination includes the
excluded candidates. Counts may describe a bounded expanded pool, not a whole market.

For the exact question “USA AdTech startups below $10,000 revenue”, use the
[financial screening guide](financial-filters-data-api.md), not `under1m`.

## Search by a natural-language description

`semantic_company_search` maps to `POST /v1/companies/semantic-search`:

```json
{"q":"enterprise software companies providing supply chain analytics","filters":{"locations":["India"]},"limit":10,"page":0}
```

Semantic results are candidates for review. This preview does not claim a measured
relevance score or that every result exactly satisfies the description. Retrieve
profiles and evidence before building a final shortlist.

## Pagination and plan limits

Company search uses zero-based `page`, with a maximum accepted page of 200, and
`limit` from 1 to 100. The linked Radar plan may further cap results or remove
restricted filters. Inspect returned access metadata, and do not interpret a
page's item count as the number of companies in the entire market.

Use small pages during development. In account mode, each successful search
request costs one API credit; empty successful results still represent a
completed query. Avoid restarting from page zero after transient errors if your
application has already saved earlier results.

Related: [company profiles](company-data-api.md), [B2B data API](b2b-data-api.md),
[competitor intelligence](competitor-intelligence-api.md), [pricing](pricing-pay-per-use.md).

<!-- scenario-links -->
## Executed scenarios for this workflow

- [01-adtech-vocabulary: Which industry value selects AdTech companies?](../scenarios/01-adtech-vocabulary.md)
- [02-usa-vocabulary: Which location value selects the United States?](../scenarios/02-usa-vocabulary.md)
- [10-startup-age: Find US AdTech companies founded from 2021 through 2026 without assuming a funding stage.](../scenarios/10-startup-age.md)
- [12-subscription-model: Find US software companies classified with subscription revenue models.](../scenarios/12-subscription-model.md)
<!-- /scenario-links -->

<!-- captured-workflow -->
## Turn a market question into a repeatable company query

Suppose an analyst asks for Indian software companies. Begin with a small structured
query, inspect the returned classifications and refine it to the intended product
market. Use `company_filter_options` for the exact field you intend to filter.
`discover_industries` spans several taxonomies; a returned legacy industry label
is not automatically a valid label in the Radar industry dropdown. The observed software lookup returned Software
Libraries as a market. Placing every vocabulary match in `industries` loses that
distinction.

Save the exact filter body and page number with each research run. Page zero is the
first page, and an effective plan can restrict filters or return fewer rows than
the requested limit. When `total` is null, a user interface can truthfully say
“2 results on this page” without manufacturing a market-size count. If the source
marks a query partial, retain the previous complete import until a replacement
query finishes.

Use semantic search when the analyst knows the business need but lacks an exact
classification label. Its returned order does not carry a public relevance score
in the captured example. Review descriptions before converting those candidates
into a saved structured segment. Headquarters filters also do not establish every
country where a company sells or maintains subsidiaries.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/search`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: search_companies -->
```json
{
  "filters": {
    "industries": [
      "Software"
    ],
    "locations": [
      "India"
    ]
  },
  "limit": 2
}
```

<!-- response-example: search_companies -->
```json
{
  "ok": true,
  "feature": "search_companies",
  "data": {
    "companies": [
      {
        "has_phone": false,
        "linkedin_slug": "e2enetworks",
        "founded": "2009",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "company_id": "3gf4ksfp7x",
        "description": "Provider of cloud infrastructure for artificial intelligence and machine learning",
        "hq": "delhi",
        "location": {
          "c": "india",
          "rg": "delhi",
          "l": "delhi",
          "lc": "delhi, delhi, india",
          "hq": "delhi",
          "cc": "in",
          "coord": [
            77.23149,
            28.65195
          ],
          "g": "28.65195,77.23149"
        },
        "has_email": false,
        "tagline": "Provider of cloud infrastructure for artificial intelligence and machine learning",
        "size": "51-200",
        "domain": "e2enetworks.com",
        "slug": "e2e-networks",
        "name": "E2E Networks",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=e2enetworks.com",
        "match_tier": "strict"
      },
      {
        "has_phone": false,
        "linkedin_slug": "sun-telematics-private-ltd",
        "founded": "2013",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "company_id": "2olp0s0nzf",
        "description": "Saas-enabled fleet management solutions",
        "hq": "bengaluru",
        "location": {
          "c": "india",
          "rg": "karnataka",
          "l": "bengaluru",
          "lc": "bengaluru, karnataka, india",
          "hq": "bengaluru",
          "cc": "in",
          "coord": [
            77.59369,
            12.97194
          ],
          "g": "12.97194,77.59369"
        },
        "has_email": false,
        "tagline": "Saas-enabled fleet management solutions",
        "size": "51-200",
        "domain": "suntelematics.com",
        "slug": "sun-telematics",
        "name": "Sun Telematics",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=suntelematics.com",
        "match_tier": "strict"
      }
    ],
    "page": 0,
    "requested_limit": 2,
    "returned": 2,
    "total": null,
    "access": {
      "plan": "free",
      "results_capped": false,
      "searches_remaining": 50
    },
    "partial_timeout": false,
    "matching": {
      "mode": "strict",
      "tiers": [
        {
          "tier": "strict",
          "count": 1171,
          "added": 2
        }
      ],
      "source_rows": 2,
      "excluded_candidates": 0,
      "strict_count_reported": 1171,
      "candidate_pool_count_reported": 1171,
      "count_capped": false,
      "filters_restricted": false,
      "note": "Strict means the source labelled the row strict and did not strip filters. Counts may describe an expanded candidate pool, not all matching companies. Missing tier metadata is unverified."
    },
    "next_page": 1,
    "pagination": "Increment source page even when strict filtering returns no rows; next_page is a continuation hint, not a guarantee of more matches. Account caps apply."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:27.234141+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:27.234341+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_companies.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The current Software/India capture preserves two source company cards and access metadata. Full detail values require get_company_field; sortable listings and on-demand columns are separate documented requests.

See the [complete search_companies endpoint reference](../reference/search_companies.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
