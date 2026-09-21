# Radar API feature coverage: companies, potential, apps, jobs and internships

The API now has **50 read operations shared by REST and MCP**, plus HTTP-only
account/key/billing controls. This map distinguishes connected retrieval from
source-dependent limits and Radar actions that still have separate workflows.
The evidence was reviewed on September 21, 2026. Repository privacy does not
establish that a service is deployed; no public deployment is claimed.

| Radar workflow | API support | Evidence and remaining limits |
|---|---|---|
| Company search, filters and listing columns | Typed filters, vocabulary suggestions, sorts and selected columns | Source plan restrictions and relaxed matches remain visible |
| Company detail | Compact profile plus 18 separately selected fields | Sectors, feeds, founders, technologies, traffic, apps, hiring, products, patents and more; field availability varies |
| Financial statements and company intelligence | Dated financial metrics, source types, briefs and comparisons | Source-plan history gates; missing metrics remain unknown |
| Funding, company events and market pulse | Structured records and dated associations | Some event windows empty; source funding anomalies remain flagged |
| Investor intelligence | Measured summaries and 19 profile/directory field types | Reviewed dated Atlas snapshot plus live publication gate; selected shortlist coverage |
| Professional search and contacts | Rich profiles and filters; separate email/phone requests | Contacts require explicit scope and paid linked source access; live paid reveal unverified |
| Growth and investment potential | Six transparent company-opportunity presets and evidence lookup | Source criteria and restrictions exposed; no forecast, return estimate or active mandate inferred |
| B2B sales prospect research | Hiring, technology, financial and app-scale screens plus company/news follow-up | Prioritization evidence, not verified purchase intent, budget or automated outreach |
| Individual mobile apps | Search, category options, exact developer-host company association, compact profiles and seven detail fields | Live captured Google Play records; June snapshots for Swiggy; no connected iOS source |
| Normalized jobs | Search/detail, company rollup, salary benchmark, filter catalog and suggestions | Fixed intern alias; salary/experience/source filters; source currencies/periods not normalized |
| Dedicated internships | Search, skill/stipend/date filters, employer groups and detail | Additional source records beyond jobs index; current vacancy status not independently verified |
| General/business/funding news | Search, articles, overview, trends, sentiment and event associations | Local integration captures use actual archives and isolated identity/quota; production connection not verified |
| Location intelligence | Existing typed operation | Source currently returns 502; not advertised as working data |
| Radar live-signal feed and event-item access | Not added as a generic pass-through | Source token/access model and client-grade pagination need a separate adapter and entitlement verification |
| Report-generation and conversational workflows | Separate Radar workflows | Not exposed as read-only retrieval operations |
| Job applications, resumes, referral introductions and outbound contact | Not retrieval operations | These mutate state or send data and have no MCP action in this package |
| Saved searches and production notification/watchlist automation | Separate Radar workflows | API account watchlist is local account state, not production alert synchronization |
| Checkout and account integration | Private account mode and synthetic end-to-end verification | Per-credit price remains unset by default; no live purchase or production sign-in claim |

## How the new sources were studied

The jobs adapter follows `blueprints/jobs/routes.py` and `jobs-search.js`: normalized
employment type is intern, salary_min tests recorded maximum salary, experience is
in months, skills use OR matching and company rollups ignore page offsets. The API
now translates the public internship alias and rejects unsupported rollup paging
and sorting. Suggestions use the existing dedicated source handler.

The dedicated internship reader selects posting_type=internship from
`companies_data.internshala_jobs`, a mixed jobs/internships collection. It keeps
source IDs and exact employer names and does not guess domain identities. Remote
filters use explicit title/locality markers; deadlines are classified rather than
used as proof of a current opening. Source description remains available in detail.

Radar's existing app intelligence code in `seo/gen_ai_intro.py` already reads
Play Store profiles and growth. The adapter now exposes the underlying
`apps_full`, `app_yoy`, `app_velocity` and `installs_history` data through fixed,
bounded read queries. Domain matching uses the developer website host, avoiding
clone-vendor URL-path matches. Raw payloads and developer contacts are not exposed.

Opportunity presets use the company-search filter model and frontend discovery
criteria. They join a bounded candidate page to selected display columns, preserve
partial failures and direct users to detailed dated evidence. User-visible
potential covers both growth/investment research and B2B sales prospecting.

See [the source review](RADAR_SOURCE_REVIEW.md), [actual app fields](APP_DATA_DEPTH.md),
[internship workflow](guides/internships-companies-api.md),
[potential workflow](guides/potential-company-data-api.md) and [verification](VERIFICATION.md).
