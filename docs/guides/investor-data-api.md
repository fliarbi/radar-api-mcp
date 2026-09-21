# Investor data API for venture capital, angel investors and portfolio research

Radar's investor API exposes company portfolios, sector and stage distributions,
co-investment relationships, financing cohorts, sourced funding news and measured
market shortlists. A compact summary identifies available fields; a separate
JSON POST retrieves the selected research with source dates and pagination.

## Discover an investor or market page

`search_investors` (`POST /v1/investors/search`) searches investor-classified
company entities through Radar's company index. It is useful for investment
firms; it is not a complete name-search index for individual angel investors.
Company search filters describe the headquarters and portfolio classifications
supported by that source. Linked-plan restrictions remain visible.

```json
{"filters":{"locations":["India"],"industries":["Software"]},"limit":20,"page":0}
```

`investor_directory` (`POST /v1/investors/directory`) returns published categories
and featured profile/list slugs. These featured entries are not the entire
published or database investor population.

```json
{}
```

Retain the returned slug, kind and family. `anupam-mittal` is an investor profile;
`fintech-investors-in-bengaluru` is a market directory. Request the summary with
`get_investor_page` at `/v1/investors/page`, using the returned slug. Its metrics,
field counts and definitions describe what can be retrieved next.

## Request portfolio data, research or news separately

`get_investor_field` maps to `POST /v1/investors/field`. Send the slug and one field:
portfolio, undated_portfolio, sectors, stages, activity, follow_on, co_investors,
news, analysis or related. Directory pages expose investors, stages, activity,
recent_rounds, themes, research, geography, selection and related. Discover the applicable
names from each summary's `available_fields`.

Portfolio and investor arrays support bounded pagination and filters. The
[complete field walkthrough](../INVESTOR_DATA_DEPTH.md) contains real output for
every supported field, including the full follow-on cohort and sourced-news
structure. The profile lookup no longer stops at a heading and edition label.

Contact retrieval uses the separate [contact workflow](../CONTACTS.md). Historical
portfolio patterns do not establish a current mandate, available capital or
intent to fund a new deal. Source cutoff, computation date and retrieval time
are separate fields throughout the workflow.

Related: [startup funding](startup-funding-data-api.md), [funding news](funding-news-api.md),
[company fields](../COMPANY_DATA_DEPTH.md), [MCP integration](company-intelligence-mcp-server.md).

<!-- captured-workflow -->
## Read complete portfolio rows, then follow their evidence

The directory returned `anupam-mittal`. Its summary now reports 270 recorded
companies and 303 equity participations, with 268 dated companies and 301 dated
participations. Two companies have undated investments and remain separately
retrievable. The worked request below reads the first five complete dated
portfolio rows. Pagination exposes all 268; it does not silently discard the rest.

Each row preserves company identity, sectors, entry stage, entry and latest
investment dates, whole-round USD amount, lead flag, number of other backers,
repeat participation and subsequent financing observations. Null means an
observation is unavailable; zero and false remain zero and false.

Separate `follow_on`, `co_investors`, `sectors`, `stages`, `activity`, `news` and
`analysis` requests expose the remaining research. The measured cohort is 215
companies: 125 received another equity round within 24 months, while 25 were
backed again by this investor. These are different outcomes. The six news stories
preserve publisher, date, source link, factual summary, interpretation and whether
they fall after the deal cutoff. See [all investor fields](../INVESTOR_DATA_DEPTH.md)
for nineteen field captures across a profile and a market directory.

Coverage ends on 2026-05-22; the most recent recorded Mittal investment is
2026-03-28. A request made today does not establish present investment activity.
Amounts describe entire disclosed funding rounds, not his individual cheque.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/investors/field`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_investor_field -->
```json
{
  "slug": "anupam-mittal",
  "field": "portfolio",
  "limit": 5
}
```

<!-- response-example: get_investor_field -->
```json
{
  "ok": true,
  "feature": "get_investor_field",
  "data": {
    "slug": "anupam-mittal",
    "kind": "investor_profile",
    "family": "investor",
    "coverage": {
      "data_through": "2026-05-22",
      "computed_on": "2026-09-14",
      "last_investment": "2026-03-28",
      "first_investment": "2011-04-21",
      "recent_window_start": "2024-05-22",
      "previous_window_start": "2022-05-22",
      "release": "atlas-20260914-v1",
      "snapshot_sha256": "ce205691ab49871ec3e14f25ea4fabc89c1b8a75c4d8053ae755453869946979",
      "partial": false,
      "source": "verified_published_atlas_snapshot"
    },
    "field": "portfolio",
    "status": "available",
    "definitions": {
      "portfolio": "Dated equity investments; undated companies are retrieved separately. Debt and grants are excluded.",
      "amounts": "USD whole-round amounts, not the investor's cheque, fund size, assets under management or investment returns.",
      "follow_on": "Another investor's later financing and this investor's repeat backing are distinct. Only entries with a full 24-month observation window enter the cohort.",
      "sectors": "Historical company tags can overlap; their counts are not additive and do not establish a current investment mandate.",
      "directory": "A directory's stored shortlist is a selected subset of its measured investor universe, not every investor in the database."
    },
    "value": [
      {
        "domain": "lickcious.com",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=lickcious.com",
        "name": "Lickcious",
        "url": "/company/lickcious/2ylzom93uz/",
        "description": "Online retailer of oral sprays, lubes, intimate washes, and perfumes",
        "city": "",
        "country": "India",
        "sectors": [
          "B2C E-Commerce",
          "Beauty E-Commerce",
          "Beauty Tech",
          "Internet First Brands",
          "Retail Tech"
        ],
        "stage": "Angel",
        "entry": "2026-03-28",
        "last": "2026-03-28",
        "entry_amount": 52845,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 0,
        "repeat": false,
        "repeat_date": null,
        "next_date": null,
        "next_days": null,
        "mature_24m": false,
        "funded_24m": false,
        "repeat_24m": false
      },
      {
        "domain": "circato.in",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=circato.in",
        "name": "Circato",
        "url": "/company/circato/2s08ott0kw/",
        "description": "Manufacturer of recycled plastic wall panels for net zero construction",
        "city": "Bengaluru",
        "country": "India",
        "sectors": [
          "Green Buildings"
        ],
        "stage": "Angel",
        "entry": "2026-03-17",
        "last": "2026-03-17",
        "entry_amount": 97444,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 0,
        "repeat": false,
        "repeat_date": null,
        "next_date": null,
        "next_days": null,
        "mature_24m": false,
        "funded_24m": false,
        "repeat_24m": false
      },
      {
        "domain": "ctruh.com",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=ctruh.com",
        "name": "Ctruh",
        "url": "/company/ctruh/17y2slqltk/",
        "description": "Provider of a no-code content creation platform for the metaverse",
        "city": "Bengaluru",
        "country": "India",
        "sectors": [
          "Augmented Reality",
          "Augmented Reality Development Tools",
          "Blockchain",
          "Metaverse",
          "Spatial Computing",
          "Virtual Reality"
        ],
        "stage": "Angel",
        "entry": "2026-03-12",
        "last": "2026-03-12",
        "entry_amount": 108603,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 1,
        "repeat": false,
        "repeat_date": null,
        "next_date": "2026-04-28",
        "next_days": 47,
        "mature_24m": false,
        "funded_24m": true,
        "repeat_24m": false
      },
      {
        "domain": "landofcakesbakery.com",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=landofcakesbakery.com",
        "name": "Land of Cakes",
        "url": "/company/land-of-cakes/3crk6yenfz/",
        "description": "Retailer of cakes, cheesecakes, tarts, brownies, and ice cream desserts",
        "city": "Kolkata",
        "country": "India",
        "sectors": [
          "Food & Beverage Products"
        ],
        "stage": "Angel",
        "entry": "2026-03-03",
        "last": "2026-03-03",
        "entry_amount": 109292,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 0,
        "repeat": false,
        "repeat_date": null,
        "next_date": null,
        "next_days": null,
        "mature_24m": false,
        "funded_24m": false,
        "repeat_24m": false
      },
      {
        "domain": "cotopay.in",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=cotopay.in",
        "name": "CotoPay",
        "url": "/company/cotopay/13zqy88k0j/",
        "description": "Provider of UPI voucher platform for business expense management solutions",
        "city": "Delhi",
        "country": "India",
        "sectors": [
          "CFO Stack",
          "Expense Analytics Software",
          "FinTech",
          "Finance & Accounting Tech"
        ],
        "stage": "Angel",
        "entry": "2026-02-11",
        "last": "2026-02-11",
        "entry_amount": 82770,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 1,
        "repeat": false,
        "repeat_date": null,
        "next_date": null,
        "next_days": null,
        "mature_24m": false,
        "funded_24m": false,
        "repeat_24m": false
      }
    ],
    "pagination": {
      "source_total": 268,
      "matched_total": 268,
      "offset": 0,
      "limit": 5,
      "returned": 5,
      "next_offset": 5
    }
  },
  "window": {
    "data_through": "2026-05-22"
  },
  "meta": {
    "retrieved_at": "2026-09-21T07:51:40.589489+00:00",
    "partial": false,
    "notes": [
      "Investor metrics use the dated, verified Atlas snapshot. Retrieval time is not data freshness. Use available_fields for separate detail requests."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T07:51:40.589665+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_investor_field.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Anupam Mittal portfolio capture returns five complete company rows from 268 dated companies. Separate captures expose all ten available profile fields and nine FinTech/Bengaluru directory fields. Live pagination traversed all 268 portfolio rows and all 1,199 selected directory investors.

See the [complete get_investor_field endpoint reference](../reference/get_investor_field.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 66 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
