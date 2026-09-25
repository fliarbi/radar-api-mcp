# Company filters, sorting and B2B data listing options

Radar separates discovery from detail retrieval. Search returns a bounded page of
company cards. The column picker makes a second request for selected data points;
the company profile lists available fields; contact values need their own request.

For activity and monetization filters, see the [business-model and revenue-model guide](guides/business-model-revenue-model-api.md)
and [investment companies earning commission per deal](scenarios/51-investment-commission-per-deal.md).
The ten recipes distinguish `business_models` from `revenue_models`, show OR versus
AND matching and request company classification separately from search cards.

## Discover supported filters

POST `{}` to `/v1/companies/filters` (MCP `company_filter_catalog`). The response
lists public filter names, schemas, known categorical options, typeahead support,
sort choices, page bounds and selectable columns. An empty `options` array with
`options_complete=false` means there is no complete option list; it does not mean
the corresponding company filter has no data.

Filters include industry, sector, market/feed, business and revenue models,
technology, products, skills, geography, employee-size bands, funding stage,
financing and ownership status, company age, founded-year range, recent event
types, founder-background categories, web performance, app downloads/growth,
financial bands, profitability and hiring signals. Founder-background and business
scores remain source classifications, not independently verified judgments.

For a vocabulary lookup, POST to `/v1/companies/filter-options`:

```json
{"field":"business_models","q":"software","limit":5}
```

Use returned suggestion values in the corresponding filter. Suggestions are
bounded, not exhaustive. Filters that only accept typed inputs have no suggestion
lookup and return 422 from this endpoint; their input schema remains in the catalog.
People have a separate `/v1/people/filter-options` endpoint for schools, skills and
sectors. Do not assume that company and people taxonomies are interchangeable.

## Search and sort a company list

POST to `/v1/companies/search`:

```json
{
  "filters": {
    "markets": ["Payments"],
    "locations": ["India"],
    "revenue_models": ["subscription"],
    "founded_year_from": 2010,
    "founded_year_to": 2025
  },
  "sort_by": "employees",
  "page": 0,
  "limit": 20
}
```

This illustrates a valid query, not a promise that all these filters have matches.
Structured searches now default to `match_mode=strict`; use `expanded` explicitly to include labelled fallback candidates. The [source filter audit](FILTER_AUDIT.md) documents all 43 fields, matching tiers, boundary gaps and pagination.

Values generally OR within one filter and AND across filters. Some taxonomy filters
are combined by Radar, and its progressive search can expand matching. Inspect
`access`, `matching`, `partial_timeout` and source restrictions. Band filters take
one value because the source applies one numeric band. Geographic radius requires
`locations`; `radius_km` explicitly requests expansion and is capped at 250 km.

Page zero is first. `limit` is 1–100 and `page` is 0–200; the linked plan can cap
results further. Null totals remain unknown. There is no unrestricted select-all
or raw-query endpoint. Sorts include relevance, valuation, funding, estimated
revenue, financing rounds, latest deal, employees and the supported derived scores.
All non-relevance sorts use the source's descending order. Estimated revenue and
valuation are not interchangeable with filing-sourced financial statements.

## Request chosen columns separately

POST to `/v1/companies/columns`:

```json
{
  "domains": ["razorpay.com", "stripe.com"],
  "columns": ["employees", "total_funding", "latest_revenue", "web_presence"]
}
```

The response contains only those columns for each domain. Requests accept at most
20 domains and 14 selected columns. Returned values such as `$1.2B` are formatted
display strings. Radar's display formatter can suppress zero and negative values;
missing columns therefore remain null/unknown. Use `get_financials` for numerical
values, fiscal periods, currencies and evidence. Columns are not a way to retrieve
contact values or a complete financial archive.

For technology, traffic, founders or apps, use a separate company field request.
For emails and phone numbers, use the [contact endpoints](CONTACTS.md).

See the real [filter catalog](reference/company_filter_catalog.md),
[suggestions](reference/company_filter_options.md), [selected-column response](reference/get_company_columns.md)
and [company field examples](COMPANY_DATA_DEPTH.md).
