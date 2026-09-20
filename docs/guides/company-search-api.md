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

Use `discover_industries` (`POST /v1/industries/discover`) with
`{"q":"software","limit":5}` to find candidate labels. Map the returned kind to
the corresponding `industries`, `sectors` or `markets` filter.

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

<!-- captured-workflow -->
## Turn a market question into a repeatable company query

Suppose an analyst asks for Indian software companies. Begin with a small structured
query, inspect the returned classifications and refine it to the intended product
market. `discover_industries` can return a match whose `kind` is market, sector or
industry; those values select `filters.markets`, `filters.sectors` or
`filters.industries`, respectively. The observed software lookup returned Software
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
        "company_id": "3gf4ksfp7x",
        "name": "E2E Networks",
        "size": "51-200",
        "slug": "e2e-networks",
        "hq": "delhi",
        "tagline": "Provider of cloud infrastructure for artificial intelligence and machine learning",
        "linkedin_slug": "e2enetworks",
        "domain": "e2enetworks.com",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "description": "Provider of cloud infrastructure for artificial intelligence and machine learning",
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
        "founded": "2009"
      },
      {
        "company_id": "2olp0s0nzf",
        "name": "Sun Telematics",
        "size": "51-200",
        "slug": "sun-telematics",
        "hq": "bengaluru",
        "tagline": "Saas-enabled fleet management solutions",
        "linkedin_slug": "sun-telematics-private-ltd",
        "domain": "suntelematics.com",
        "flags": [
          [
            "Small Enterprise",
            "size"
          ]
        ],
        "description": "Saas-enabled fleet management solutions",
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
        "founded": "2013"
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
    "pagination": "Increment page; account caps can apply. No total is inferred from a page."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T06:35:41.229928+00:00",
    "partial": false,
    "notes": [
      "Filters and result counts remain subject to the linked Radar account's limits."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-20T06:35:41.230131+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_companies.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live Software/India query returned two cards, including E2E Networks, with total=null and plan=free. A visible result does not establish complete segment coverage. The example preserves the real source fields and counts, including available classifications and products. Full company records are available through get_company.

See the [complete search_companies endpoint reference](../reference/search_companies.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
