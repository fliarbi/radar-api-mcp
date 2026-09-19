# Radar user guide

This preview provides company research through REST and MCP. Your operator supplies
an API base URL and preview key. Every data request requires the key. Radar and News
access depend on the accounts linked to that key; no preview key implies unlimited
coverage.

## Authentication and discovery

Send either `Authorization: Bearer YOUR_KEY` or `X-API-Key: YOUR_KEY`. If both are
provided, they must agree. Do not place keys in URLs or request bodies.

`GET /v1/capabilities` lists operation descriptions, JSON input schemas and whether
the required connection is configured. Configured does not mean healthy or entitled
for every query. `GET /v1/openapi.json` gives the REST schema. Both need a key.
`GET /healthz` is unauthenticated and proves only that this process is running.

All data operations use JSON `POST` requests. MCP exposes matching tool names;
each tool takes one `request` object with the same JSON as REST.

## Find a company

`POST /v1/companies/semantic-search` / `semantic_company_search`:

```json
{"q":"enterprise AI software companies in India","limit":10,"page":0}
```

`POST /v1/companies/search` / `search_companies`:

```json
{
  "filters": {
    "industries": ["Software"],
    "locations": ["bengaluru, karnataka, india"],
    "profitability": ["profitable"]
  },
  "limit": 20,
  "page": 0
}
```

Use `discover_industries` with a specific query to find up to five matching names.
The returned `kind` is `industry`, `sector` or `market`; use `industries`, `sectors`
or `markets` in a filtered search respectively. Company filters also include names,
business models, sizes, stages, technologies, products, skills, event types,
financing and ownership status. The capability schema is the complete field list.

Financial filters each accept at most one band:

| Filter | Values |
|---|---|
| `revenue_bands` | `under1m`, `1m-10m`, `10m-100m`, `100m-1b`, `1b+` (USD) |
| `revenue_growth` | `declining`, `flat`, `growing`, `high`, `hyper` |
| `profitability` | `profitable`, `loss` |

These use Radar's existing bands, not newly computed metrics. Upstream account
restrictions can remove filters or cap results; inspect the response's `access`.
Some text fields reject quotes, backslashes, semicolons and control characters
because the existing Radar service cannot safely accept them in every handler.

Use company domains, such as `microsoft.com`, for retrieval. A URL, port, IP address
or path is rejected. Domains are normalized to lowercase and a leading `www.` is
removed. Company search uses zero-based `page`, a maximum page of 200 and a maximum
requested limit of 100. A page count is not presented as a total company count.

## Read financials

`POST /v1/companies/financials` / `get_financials`:

```json
{
  "domain":"microsoft.com",
  "statement":"all",
  "period_type":"annual",
  "year_from":2022,
  "limit":40
}
```

`statement` accepts `all`, `income`, `balance_sheet` or `cash_flow`.
`period_type` accepts `all`, `annual` or `quarterly`. Years refer to the source's
fiscal year. Each period retains the fiscal label, filing date, reporting date,
form type and exact period end when supplied. A reporting date is not a fiscal
period end; an unavailable period end remains `null`.

Each metric includes:

| Field | Meaning |
|---|---|
| `value`, `currency`, `unit` | Retrieved value; USD metrics are absolute amounts, EPS is per share |
| `source_type` | `filing`, `news_report` or `unspecified` |
| `native_value`, `native_currency` | Native-currency figure when supplied by Radar |

Zero and negative amounts are retained. Missing metrics are omitted, never changed
to zero. EPS currency remains unspecified when Radar does not supply it. Currency
conversion metadata is preserved; the gateway does not apply new FX rates or
combine different currencies.

`article_ids` link to available news evidence through `get_article`. The gateway
does not invent filing URLs or assume that a news article is an official filing.
`access_limited` means the linked Radar account exposes only part of the archive.
`available_period_count` is Radar's reported archive count, not necessarily the
number accessible to you. Annual filtering can return no rows when your accessible
window contains only quarters. The independently gated balance-sheet summary is
not reconstructed; the endpoint returns only metrics present in accessible history.

## Build a research brief

`POST /v1/companies/brief` / `company_brief`:

```json
{"domain":"microsoft.com","include_news":true,"news_limit":10,"event_days":365}
```

The response groups profile, financials, intelligence, events, funding, enrichment
and news. Each section has `available` and either a result or an error. Overall
`meta.partial` is true when a requested section is unavailable. All sections retain
their own data windows. If every section is unavailable, the request fails with
`coverage_unavailable`.

`compare_companies` accepts two to five distinct domains. Periods remain separate:
two companies' “FY2025” can cover different dates. Scores are Radar's derived
assessments; they are not filing facts or independently validated investment advice.

## Retrieve associated news

`POST /v1/news/search` / `search_news`:

```json
{
  "company":"microsoft.com",
  "date_from":"2026-01-01",
  "date_to":"2026-08-31",
  "sentiment":"negative",
  "priority_min":7,
  "limit":100
}
```

Supply a topic `q` or a company domain. A company query always uses business-news
coverage so the association is preserved. General topic queries use the general
News service. `search_business_news` explicitly scopes topic queries to business.
Priority is 1–9. News results default to 100 per page, subject to the linked News
account's plan. For the next page, send the returned `next_cursor` as `cursor`
with unchanged filters and sorting. Never increment a news page number.

Use `get_article` with a returned article ID for full text and attribution.
`news_trends` and `news_sentiment` accept `daily`, `weekly` or `monthly` granularity;
`news_overview` provides an overview. Company events and funding coverage are also
available through `search_business_events` and `search_funding_news`.
News queries retain the provider's date window and notes. Missing recent coverage
does not establish a decline in company activity.

## Investors, jobs and people

`search_investors` uses company filters while selecting investor entities.
Locations refer to investor headquarters; sector/market filters refer to portfolio
activity under Radar's existing rules. `investor_directory` returns published slugs
for `get_investor_page`. Some editions expose public metadata only; the API respects
that upstream gate.

`search_jobs`, `companies_hiring`, `get_job` and `salary_benchmark` retrieve hiring
data. Salary results retain the reported currency and sample size. `search_people`
supports professional name, role, company, skills, sector and location filters.
This preview has no contact-reveal, application, referral, CRM-send or billing tools.

## Response and error handling

Responses contain `ok`, `feature`, `data`, `window` and `meta`; failures add `error`.
`meta.retrieved_at` is the time of the API request, not the freshness of the data.
Unknown freshness is `null`. `meta.partial`, section availability, access limits,
`total_capped`, `partial_timeout` and event truncation must remain visible in clients.

| HTTP status | Action |
|---|---|
| 400 / 422 | Correct the request using the capability schema |
| 401 | Supply a valid, unexpired preview key |
| 402 | The linked service account's quota is exhausted |
| 403 | The linked service account needs access, or the request origin is disallowed |
| 404 | No matching data is available |
| 413 | Reduce the request body below 256 KiB |
| 429 | Wait for `Retry-After` before retrying |
| 502 / 503 / 504 | Service failure, missing configuration, unavailable coverage or timeout; do not treat it as an empty dataset |

MCP returns the same envelope as structured content and sets `isError` on failed
operations. Retry only transient failures; do not repeatedly retry authentication
or validation errors.
