# Getting started with the Radar API

[README](../README.md) · [Use cases](use-cases/README.md) · [Endpoint reference](reference/README.md) · [User guide](USER_GUIDE.md)

From no key to a working company-data, financial-data or financial-news query in about five
minutes, then every command of the `radar` client.

## 1. Get a key

Sign in to the [Fliar dashboard](https://fliarbi.com/radar/dashboard?tab=radarapi), open
**API keys** (in the Radar or the Fliar Prism workspace) and choose **Create or manage API keys**.
On the key page, choose **Connect Radar session**, enter an application name, pick the data
access (**All data** includes news) and an expiry, and create the key. Copy it when shown;
it is displayed once. The key starts with `rdr_` and also works on the Prism News APIs.

## 2. Install the client in one line

Requires Bash, curl and Python 3.8+ (standard library only).

```bash
curl -fsSL https://raw.githubusercontent.com/fliarbi/radar-api-mcp/main/scripts/install.sh | bash
```

| Installer setting | Default | Meaning |
|---|---|---|
| `RADAR_BIN_DIR` | `~/.local/bin` | Where `radar` is placed |
| `RADAR_REF` | `main` | Branch, tag or commit to install |
| `RADAR_NO_PROFILE` | `0` | `1` = do not add the env.sh line to your shell startup files |
| `GH_TOKEN` | — | Only for installing from a private fork |

The installer downloads `scripts/radar_cli.py` to `~/.local/share/radar-cli/`, writes
`~/.config/radar/env.sh` (`RADAR_API_URL=https://radar-api.fliarbi.com` and the command folder)
and adds one line that loads it to `~/.bashrc`, `~/.zshrc` and `~/.profile`. It never uses sudo
or starts a service.

**Uninstall:** `rm ~/.local/bin/radar && rm -r ~/.local/share/radar-cli ~/.config/radar`, then
delete the line ending in `# radar-api` from your shell startup files.

## 3. Log in once

```bash
radar login          # checks the key with /v1/capabilities, then saves it owner-only
```

| Environment variable | Overrides |
|---|---|
| `RADAR_API_KEY` | The saved key |
| `RADAR_API_URL` | The API URL (default `https://radar-api.fliarbi.com`) |

## 4. First queries

```bash
radar features
radar get-financials --domain zomato.com --period-type annual
radar search-companies --filters.industries FinTech --filters.locations India --limit 10 --table
radar search-business-news --q "stock market" --priority-min 7 --limit 10 --table
```

## 5. Copy a use case

Every [use-case page](use-cases/README.md) ends with its exact `radar`, curl, Python and MCP
calls. Copy them and change the company domain, industry or topic.

## How options become requests

| You type | The request gets |
|---|---|
| `--domain zomato.com` | `"domain": "zomato.com"` (dashes become underscores; numbers and true/false are typed) |
| `--filters.industries FinTech --filters.locations India` | `"filters": {"industries": ["FinTech"], "locations": ["India"]}` |
| `--json '{...}'` | That JSON body, merged with other options |
| `--table` | A compact table of the first list in the response |
| `-o file.json` | The full response written to a file |

Exit status is 0 on success and 1 on an API error.

## MCP clients

`radar mcp-config` prints a configuration for clients that support remote MCP servers with
headers (Claude Code, Codex and others): URL `https://radar-api.fliarbi.com/mcp` and
`Authorization: Bearer $RADAR_API_KEY`. The 53 operations below are the MCP tools.

## Command reference

| Command | Request | What it does |
|---|---|---|
| `radar search-companies` | `POST /v1/companies/search` | Filter companies by industry, market, location, size, stage, technology, funding and financial bands |
| `radar semantic-company-search` | `POST /v1/companies/semantic-search` | Find companies using a natural-language description plus optional filters |
| `radar get-company` | `POST /v1/companies/profile` | Read compact company identity and available fields |
| `radar get-company-field` | `POST /v1/companies/field` | Retrieve one explicitly selected company field, such as classification, people, technology, traffic or apps, with coverage and bounded arrays |
| `radar company-apps` | `POST /v1/companies/apps` | List individual Play Store apps whose normalized developer website exactly matches the company domain |
| `radar opportunity-presets` | `POST /v1/companies/opportunities/presets` | Discover explainable growth, hiring, financial and technology prospecting screens and their limits |
| `radar search-opportunities` | `POST /v1/companies/opportunities/search` | Find companies using an explicit opportunity preset plus additional filters |
| `radar company-filter-catalog` | `POST /v1/companies/filters` | Discover company filters, accepted values, sort options, pagination and selectable result columns |
| `radar company-filter-options` | `POST /v1/companies/filter-options` | Look up matching company filter values using Radar's sidebar vocabulary and typeahead services |
| `radar get-company-columns` | `POST /v1/companies/columns` | Fetch only selected display columns for up to twenty company domains |
| `radar get-company-intelligence` | `POST /v1/companies/intelligence` | Read company scores, peer comparisons, earnings and risk narratives |
| `radar financial-filter-catalog` | `POST /v1/companies/financials/filters` | Discover precise USD screening, source financial band boundaries, fiscal-period semantics and limits |
| `radar screen-company-financials` | `POST /v1/companies/financials/screen` | Screen a bounded candidate page or explicit domains against exact dated USD financial constraints |
| `radar get-company-team` | `POST /v1/companies/team` | Retrieve recorded company founders, key people or exactly affiliated professional cards with separate group requests and bounded pagination |
| `radar get-financials` | `POST /v1/companies/financials` | Retrieve income, balance-sheet and cash-flow metrics by fiscal period |
| `radar get-company-events` | `POST /v1/companies/events` | Read a company's event timeline, momentum, risks and the effective account-limited date window |
| `radar get-company-funding` | `POST /v1/companies/funding` | Read reported funding rounds and investors |
| `radar get-company-enrichment` | `POST /v1/companies/enrichment` | Read legal identity, hiring, reputation, digital presence, innovation and social activity when available |
| `radar find-competitors` | `POST /v1/companies/competitors` | Find competitors in a named market, grouped by funding stage |
| `radar company-brief` | `POST /v1/companies/brief` | Return compact summaries of profile, financials, intelligence, events, funding, enrichment and news with separate detail requests and explicit coverage |
| `radar compare-companies` | `POST /v1/companies/compare` | Compare two to five companies with separately labelled fiscal periods and partial-coverage flags |
| `radar search-investors` | `POST /v1/investors/search` | Find investors by headquarters and portfolio industries or markets |
| `radar investor-directory` | `POST /v1/investors/directory` | List published investor pages, sectors and cities |
| `radar get-investor-page` | `POST /v1/investors/page` | Read investor identity, measured portfolio metrics, dated coverage and available detail fields by published slug |
| `radar get-investor-field` | `POST /v1/investors/field` | Retrieve one investor field: paginated portfolio or shortlist, sector/stage analysis, follow-on cohorts, co-investors or sourced news |
| `radar market-pulse` | `POST /v1/markets/pulse` | Read recent funding, trending markets, sectors and investors for a bounded window |
| `radar location-intelligence` | `POST /v1/locations/intelligence` | Retrieve Radar's existing business intelligence for a named location |
| `radar discover-industries` | `POST /v1/industries/discover` | Find up to five matching industry or market names using a specific query |
| `radar search-jobs` | `POST /v1/jobs/search` | Find job listings by company, skills, role, geography and freshness |
| `radar job-filter-catalog` | `POST /v1/jobs/filters` | Discover job filters, source values, sorting and source matching semantics |
| `radar job-filter-options` | `POST /v1/jobs/filter-options` | Suggest observed job titles, skills, employer names or locations |
| `radar search-internships` | `POST /v1/jobs/internships/search` | Search dedicated internship records by employer, title, location, skills, stipend and posted dates |
| `radar companies-offering-internships` | `POST /v1/jobs/internships/companies` | Group matching observed internship listings by exact employer name, with counts, titles and detail IDs |
| `radar get-internship` | `POST /v1/jobs/internships/detail` | Retrieve a source internship with description, stipend, skills, dates, application URL and validity qualifications |
| `radar companies-hiring` | `POST /v1/jobs/companies` | Find hiring companies for the same job filters |
| `radar get-job` | `POST /v1/jobs/detail` | Retrieve a job listing by an ID returned by search_jobs |
| `radar salary-benchmark` | `POST /v1/jobs/salary-benchmark` | Read salary statistics for a role, geography and optional currency |
| `radar search-apps` | `POST /v1/apps/search` | Search individual Android apps by name, developer, exact website host, category, installs, ratings and price model |
| `radar get-app` | `POST /v1/apps/profile` | Read compact app identity, observed installs and rating, detail availability and history count |
| `radar get-app-field` | `POST /v1/apps/field` | Retrieve one app field: listing, ratings, monetization, release, developer, growth or paginated install history |
| `radar app-filter-options` | `POST /v1/apps/filter-options` | List matching observed Play Store categories for app discovery |
| `radar search-people` | `POST /v1/people/search` | Find professional profiles by name, role, company, schools, skills, seniority and location |
| `radar people-filter-options` | `POST /v1/people/filter-options` | Look up canonical schools, skills and sectors accepted by people search |
| `radar get-company-contacts` | `POST /v1/contacts/company` | Request company emails and/or phones separately |
| `radar get-person-contacts` | `POST /v1/contacts/person` | Request one person's emails and/or phones |
| `radar search-news` | `POST /v1/news/search` | Search associated news |
| `radar search-business-news` | `POST /v1/news/business` | Search business headlines for a topic or company with date, sentiment and priority filters |
| `radar news-overview` | `POST /v1/news/overview` | Read measured coverage, headline examples and topic context in a bounded date window |
| `radar news-trends` | `POST /v1/news/trends` | Measure daily, weekly or monthly news volume while preserving the available date window |
| `radar news-sentiment` | `POST /v1/news/sentiment` | Read the distribution and timeline of news sentiment |
| `radar search-business-events` | `POST /v1/news/events` | Read structured business events associated with a topic or company and their article references |
| `radar search-funding-news` | `POST /v1/news/funding` | Find funding coverage by company, topic, investor, sector, round and reported USD amount |
| `radar get-article` | `POST /v1/news/article` | Retrieve the full article and attribution for an article ID returned by news or company events |
| `radar call PATH [JSON]` | any | Any operation by path |
| `radar login` / `logout` / `features` / `mcp-config` | — | Key, discovery and MCP setup |

## Troubleshooting

| Message | What to do |
|---|---|
| `No API key` | Run `radar login`, or set `RADAR_API_KEY` |
| `command not found` | Open a new terminal (the installer updates PATH) or run `~/.local/bin/radar` |
| `401 unauthorized` | The key is wrong, expired or revoked; create a new one on the key page |
| `402 credits_required` | Included credits are used: buy prepaid credits and set a monthly spending limit on the key page |
| `403 scope_required` | Create a key with the needed access (contacts need the explicit contacts scope) |
| `429 rate_limited` / `concurrency_limited` / `daily_limit` | Wait for `Retry-After`; limits rise with your usage level |
| `503` | A data source is temporarily unavailable; retry later and do not record the result as zero |
