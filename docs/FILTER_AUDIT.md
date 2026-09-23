# Radar filters: source analysis and API mapping

Reviewed the actual Radar frontend filter controls, company-search handler,
progressive matching logic, people-search output and the gateway mapper before
writing the 50-scenario suite. This inventory covers all **43 public company
filter fields**. It separates mapping review from executed data assertions.

Evidence locations in the sibling Radar source are `company_search/routes.py`
(filter mapping, band predicates and progressive tiers), `people_search/routes.py`
(company-prefix and profile-card behavior), and the frontend `search-system.js`
industry options. Gateway implementation lives in `radar_api/catalog.py`,
`radar_api/service.py`, `radar_api/models.py` and `radar_api/research.py`.
These are code references, not customer connection requirements.

## Matching is part of the query contract

The source can expand sparse structured searches through strict, taxonomy,
radius and semantic retrieval. It supplies aggregate tier counts and, for mixed
results, per-card tier labels. Dropping those labels made expanded results look
like exact matches. The baseline returned US-based sep.com in two India searches.

Structured API search now defaults to `match_mode=strict`. It keeps only rows
labelled strict by the source when no requested filters were stripped. If the
whole source page explicitly declares only a strict tier, unlabelled rows inherit
that tier; otherwise missing labels are unverified and excluded. Explicit
`match_mode=expanded` includes fallback candidates with their labels. Semantic
search defaults to expanded because semantic discovery is its purpose.

`matching.source_rows`, `excluded_candidates`, `strict_count_reported` and
`candidate_pool_count_reported` retain the difference between source and returned
rows. The latter counts can refer to a bounded pool; they are not a certified
market total. `next_page` follows the source pool even when strict filtering leaves
zero delivered rows. SQL, source implementation paths and diagnostic queries are
never copied from the source tier objects.

## Complete public filter map

Values generally OR within a filter and AND between filters, but source taxonomy
normalisation and expansion affect exact label interpretation. Use the API's
`company_filter_catalog` and `company_filter_options` for the field being edited.
The map below records the handler input, not a promise that every field has full
source coverage or that every compound query has results.

| Public JSON field | Family | Source request mapping |
|---|---|---|
| `company_names` | Company identity | `company_name` |
| `entity_type` | Company identity | `entity_type` |
| `organization_types` | Company identity | `org_type` |
| `industries` | Industry and market taxonomy | `ai_ind` |
| `sectors` | Industry and market taxonomy | `modern_sectors` |
| `markets` | Industry and market taxonomy | `feeds` |
| `business_models` | Industry and market taxonomy | `business_model` |
| `verticals` | Industry and market taxonomy | `verticals` |
| `industrial_applications` | Industry and market taxonomy | `industrial_applications` |
| `locations` | Location and founding | `selected_location` |
| `radius_km` | Location and founding | `custom_range in metres + radius_explicit` |
| `founded_year_from` | Location and founding | `founded_year[0]` |
| `founded_year_to` | Location and founding | `founded_year[1]` |
| `ages` | Location and founding | `current_age` |
| `sizes` | Company scale and stage | `size` |
| `stages` | Company scale and stage | `funded_as` |
| `growth_stages` | Company scale and stage | `progress_label` |
| `scalability` | Company scale and stage | `scalablity` |
| `financing_status` | Business and financial status | `financing_status` |
| `ownership_status` | Business and financial status | `ownership_status` |
| `operating_status` | Business and financial status | `status` |
| `revenue_models` | Business and financial status | `revenue` |
| `business_approaches` | Business and financial status | `business_approach` |
| `revenue_bands` | Financial summaries | `revenue_band` |
| `revenue_growth` | Financial summaries | `revenue_growth` |
| `profitability` | Financial summaries | `profitable` |
| `deal_sizes` | Financial summaries | `deal_label` |
| `technologies` | Technology and commercial capabilities | `webstack` |
| `products` | Technology and commercial capabilities | `products` |
| `skills` | Technology and commercial capabilities | `skills` |
| `positions` | Technology and commercial capabilities | `positions` |
| `founders_background` | Founders and events | `founders_background` |
| `event_types` | Founders and events | `news_types` |
| `web_popularity` | Web presence | `web_popularity` |
| `web_cwv` | Web presence | `web_cwv` |
| `web_speed` | Web presence | `web_speed` |
| `web_seo_maturity` | Web presence | `web_seo_maturity` |
| `web_sd_maturity` | Web presence | `web_sd_maturity` |
| `web_business_hints` | Web presence | `web_business_hints` |
| `web_score` | Web presence | `web_score` |
| `mobile_downloads` | Mobile presence | `mobile_downloads` |
| `mobile_growth` | Mobile presence | `mobile_growth` |
| `hiring` | Hiring signals | `hiring` |

## Interpretation by family

### Company identity

Source company name and entity/organization categories; entity type selects the source investor/incubator universe. Identity still needs domain review.

### Industry and market taxonomy

Industries use Radar's ai_ind vocabulary; sectors are practice areas; markets are feeds. Business models and verticals are separate source dimensions. Source taxonomy expansion is labelled; not every legacy industry label is a Radar dropdown value.

### Location and founding

Recorded company location, not incorporation or customer geography. Explicit radius is 21–250 km; years use inclusive endpoints. Legacy age bucket labels have boundary gaps described below.

### Company scale and stage

Source size/growth/scalability labels, not exact employee counts or independently verified stage. Funding-stage and derived growth-stage filters describe different dimensions.

### Business and financial status

Source status and business-model labels. Subscription describes a revenue model; it does not imply a particular revenue amount.

### Financial summaries

Revenue and profitability use source financial summary fields; growth uses one-year revenue growth. Deal sizes select funding-round bands by domain, not total revenue or total company funding. Exact financial comparisons use the separate dated-metric screen.

### Technology and commercial capabilities

Observed technology/product/company capability fields. Skills and positions here are company discovery attributes; use people search for an individual professional's skills.

### Founders and events

Founder-background categories AND all selected predicates and resolve associated company domains from people evidence. Events select source company-event types; neither establishes a current executive roster or a future business event.

### Web presence

Source observed categories and derived score bands; not a live website audit. Missing scores do not enter the below-40 band. Scores and categories are not interchangeable with measured traffic.

### Mobile presence

Company-level source mobile install totals and derived app-growth bands. Retrieve company_apps and selected app fields for dated observations; installs are not active users or paying customers.

### Hiring signals

Nested is_hiring, min_open_roles, roles, cities and recency_days are sent to Radar's source hiring predicate. A hiring signal is not a verified filled role. Separate jobs and dedicated internship endpoints expose listings.

## Numeric boundaries verified in the handler

| Predicate | Actual comparison |
|---|---|
| Revenue `under1m` | `0 < revenue < 1,000,000` |
| Other revenue bands | Open lower and upper boundaries; `1b+` is strictly greater than 1 billion |
| Profitability | Net profit `>0` or `<0`; zero belongs to neither |
| Revenue growth / mobile growth | declining `<0`; flat `[0,10)`; growing `[10,30)`; high `[30,100)`; hyper `>=100` |
| Web score | `80+ >=80`; `60-80 [60,80)`; `40-60 [40,60)`; `<40 (0,40)` |
| Mobile downloads | Inclusive minima 1,000; 100,000; 1,000,000; 10,000,000 |
| Founded year | Inclusive `from` and `to`; omit either for a one-sided range |
| Age `< 5y` | Source actually uses `>0` and `<6`: ages 1–5 |
| Age `5-10y` | `>5` and `<11`: ages 6–10 |
| Age `10-25y` | `>10` and `<25`: ages 11–24 |
| Age `25+y` | `>25`; age 25 is excluded |

Use founded-year bounds when a reproducible startup-age definition matters.
The `Most Recent` age value invokes a source label rather than an explicit age
number. Do not infer an exact cutoff from that label. Multiple funding deal bands
are unioned through funding-round associations; they are not collapsed into one
company-total-funding interval. The source dropdown does not expose every possible
numeric funding interval.

The [financial filter guide](guides/financial-filters-data-api.md) explains exact
USD thresholds and reporting periods. The [teams guide](guides/teams-people-data-api.md)
explains career seniority, company prefix matching, exact-domain teams and contact
retrieval. The [technology and traffic guide](guides/technology-traffic-data-api.md)
explains observed digital fields and separate app evidence.

Founder-background discovery has an additional source caveat: failed resolution
can leave the source company query unnarrowed. A strict tier label alone cannot
independently certify that founder evidence was applied. Review founder/team detail
before claiming the predicate, and treat unresolved founder evidence as unknown.
This path was analysed in code, not independently validated by the 50 captured
requests. It remains a source behavior limitation rather than a certified filter.

## Investor-specific source behavior

Investor discovery rewrites sectors, markets and business models to portfolio
criteria but keeps location on the investor headquarters. Its source stage key
currently maps differently from the ordinary company stage predicate; use investor
portfolio/stage detail evidence instead of claiming a verified stage match from
cards. The narrowed investor path currently supplies no strict tier metadata, so
strict gateway mode excludes its unverified rows. Explicit expanded mode preserves
those cards with `match_tier=unverified`, rather than silently certifying them.

## What was executed, and what was only analysed

[50 fixed scenarios](scenarios/README.md) exercise taxonomy discovery, countries,
founded years, financial bands, exact amounts, statements, funding, teams,
professional filters, app fields, jobs, internships, investors, technology,
traffic and news. Assertions verify what is observable in returned evidence.
The [audit report](SCENARIO_AUDIT.md) preserves failed/qualified baseline findings
and current source limitations. This mapping inventory is not a claim of testing
every combination of all filter fields or of certifying source classification truth.
