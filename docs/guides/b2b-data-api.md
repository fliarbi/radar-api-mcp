# B2B data API for company research and account intelligence

Radar's B2B data API lets an application discover companies, retrieve business
profiles and connect those profiles to financial data, funding rounds, hiring
signals and news. It is useful when a business-to-business research workflow
needs several kinds of evidence about the same account, rather than a name alone.

For example, a sales operations team can find software companies in a market,
resolve their website domains, then attach company profiles and recent business
events to an internal account review. An analyst can use the same domain to
retrieve financial metrics and check the evidence behind reported growth.

## A practical account research workflow

Start with `search_companies` (`POST /v1/companies/search`). This request uses
industry and geography as firmographic filters:

```json
{"filters":{"industries":["Software"],"locations":["India"]},"limit":20,"page":0}
```

Use a returned company domain in `company_brief` (`POST /v1/companies/brief`):

```json
{"domain":"microsoft.com","include_news":false,"event_days":90}
```

A brief assembles profile, financials, derived intelligence, events, funding and
enrichment. Enable `include_news` only when a News service and linked News key are
available. In account mode, this request reserves six credits; successful sections
consume credits and failed sections are refunded. Keep `meta.partial` visible to
the reader so an unavailable section is not mistaken for a complete company record.

## Choosing the right business data

| Need | Use |
|---|---|
| Build a company list | Filtered search or semantic company search |
| Identify one business | Company profile by domain |
| Add context to an existing account | Company enrichment and event history |
| Evaluate reported financial performance | Financial metrics with fiscal periods and source types |
| Investigate recent announcements | Business news, funding news and source articles |

Radar does not expose email-reveal or phone-reveal actions through this gateway.
Professional profile search is a separate retrieval capability. Sending CRM
messages or creating outreach campaigns is outside these tools' behavior.

## Coverage and integration questions

**Is this a downloadable B2B database?** This package provides bounded API
queries. It does not promise a complete company database export or a fixed
number of companies. Account plan restrictions can limit filters and results.

**Can AI agents use the same company data?** Yes. The MCP server exposes the same
typed retrieval operations. REST and MCP share account usage when account mode
is enabled; changing transport or creating another key does not reset credits.

Next: [get an API key](api-keys-authentication.md), [company search](company-search-api.md),
[company enrichment](company-enrichment-api.md), or [MCP setup](company-intelligence-mcp-server.md).
See the [documentation index](../README.md) for the complete guide collection.

## Add founder and professional contact research to an account

Keep company contact values, individual contact records and social URLs in separate
CRM fields. [Company email/phone lookup](company-email-phone-api.md) does not expose
an employee-wide email list. Use [team discovery](teams-people-data-api.md), accept
person identities, then request the selected person's contact types. A company
fallback must stay company-attributed. The [founder guide](founder-contact-data-api.md)
and [24 request recipes](../examples/contacts/requests.json) show the supported
variables without inventing work-email or verification filters.

<!-- captured-workflow -->
## Build a research account from separate evidence

For a sales-research or procurement application, keep three layers of information:
the candidate business, the accepted identity, and observations about it. A search
result belongs in the first layer. Move it into your account model only after
reviewing the returned name, domain and location. Financial periods, hiring signals
and news references then attach as dated observations instead of overwriting one
undifferentiated company record.

A useful account table stores your internal ID, normalized company domain, Radar
record ID, matched name and the time you reviewed that identity. A financial table
adds fiscal label, metric, value, currency and source type. A news association adds
an article identifier and company/topic query. This separation lets a researcher
see that the financial evidence may describe a parent company while the profile
label describes a product or division.

Start with two discovery results, select one accepted domain and request a brief.
In account mode that search costs one successful-operation credit. A brief reserves
six credits without News or seven with News, then refunds failed sections. Cache
the displayed observation with its retrieval date for your own permitted use;
avoid fetching the same seven sections every time a user opens a table row.

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
