# Verification record

This record separates local implementation, synthetic account/contact checks,
live data reads, GitHub state and deployment. The repository remains a private
preview; no public API, production checkout or paid contact access is claimed.

## Animation redesign: 2026-09-25

- Replaced all seven clips with 32-second, 320-frame GIFs at 1280 × 800 and
  10 fps. A 42px typed prompt slides completely off-screen before a full-screen
  chart and a separate detailed result view. The seven GIFs total 6,386,625 bytes.
- Added seven distinct visual forms: stage distribution, financial columns,
  founder relationship diagram, founding-year dot plot, funding timeline,
  app-install lollipop ranking and contact-coverage donut. Financial detail now
  includes available operating income, EPS and explicitly calculated net margin;
  founder detail includes all saved education entries and skills.
- Checked all seven prompt layouts and fourteen result layouts, then inspected
  both result scenes decoded from every exported GIF. No prompt remains in the
  result area, and every result clears its source note. The renderer now rejects
  overlapping layouts, and the media manifest also hashes the HTML/JS/CSS sources.
- GIF dimensions, duration, loops, source hashes, typed request recipes,
  documentation and JavaScript checks passed. Gallery selection, pause/replay,
  reduced motion, copy feedback and the 390px mobile layout also passed.
- Saved responses and API contracts are unchanged. Illustrated cohorts and
  contacts remain labeled; no live source calls or real contact exports occurred.

## Initial animated use-case gallery: 2026-09-25

- Built seven 1280 × 800 animated GIFs, 190–220 frames each at 10 fps, with
  19–22-second infinite loops and matching still images. The
  [gallery](demos/index.html) and [walkthroughs](ANIMATED_USE_CASES.md) cover every
  requested workflow, including all ten rows in the illustrative dating-app list.
- Competitor, financial and founder-profile illustrations use saved source
  captures. GenAI cohorts, April 2026 San Francisco funding, app rankings/legal
  records and contact exports explicitly use fictional or synthetic rows. The
  client-built UI is not an official Claude Code/Codex recording or a live API run.
- Validated every illustrated Radar request against its actual input model,
  checked source-file hashes, decoded all GIF frames and verified durations,
  dimensions, looping and variation in both the prompt and result regions.
  [The media manifest](demos/media/manifest.json) records file hashes and sizes.
- Inspected rendered stills and intermediate GIF frames. Browser checks passed
  for all seven workflow selections, GIF/poster loading, pause/replay, prompt copy
  or selection fallback, reduced-motion behavior, and a 390px mobile layout without
  horizontal page overflow. No external page requests or JavaScript errors occurred.
- The renderer uses an isolated temporary browser profile and local files. No
  source service, real contact reveal, workbook export, message send or account
  mutation occurred. Shutdown shards were not queried or restarted. The API's
  existing response contracts and historical captures remain unchanged.
- **242 tests passed locally**, along with documentation checks, Ruff, JavaScript
  syntax checks and package builds. The source distribution includes all seven
  GIFs, their gallery and renderer. Credential/archive scanning found no known
  secret values or private paths in 524 repository files and 561 archive members.

## Empty-example review: 2026-09-24

- Audited **220 saved response captures** across all example folders: 200 contain
  requested data, 15 are empty, three are expected access denials and two are
  unsuccessful source calls. These totals include **24 explicitly synthetic
  account/contact fixtures**. This saved-output scan is not 220 fresh live calls.
- Live-recaptured six changed scenarios using electroCore, Qualys and Connvertex,
  and published three populated companion captures for Yext products/activity and
  Mastech Digital annual income. The primary financial example now uses the
  populated electroCore FY2024 income response. All 50 original scenario baseline
  responses, requests, timestamps and hashes were independently preserved.
- Balance-sheet and cash-flow examples remain **blocked**, with no requested
  numeric metrics. Strict financial filings and company-resolution reads failed
  on an unreachable shard. Six company probes returned news-derived income or
  empty data; expired cache snapshots were not used to fabricate live success.
  See [the findings and complete replacements](EXAMPLE_REPAIRS.md).
- Content checks now require numeric metrics in the selected statement family,
  distinguish zero/negative values from missing data, and reject empty positive
  demonstrations. Contact fixtures, strict-filter negatives, source failures and
  unresolved founder matches retain their purpose and provenance.
- **242 tests passed locally**. Ruff, package build, documentation schema/hash/
  projection checks and repository/archive credential scans passed. The docs
  checker also validates original and replacement requests independently and
  preserves manual workflow sections when regenerating scenario links.
- GitHub was verified private with Pages disabled. No public deployment,
  entitlement change or database/service repair was performed.

## All-endpoint output follow-up: 2026-09-23

- Reviewed and live-probed **all 53 REST/MCP data operations** against their
  source adapters and endpoint ownership. Recaptured all **16 account/discovery
  operations** with isolated synthetic identity/payment providers.
- The current data probes returned **44 HTTP 200, six HTTP 503 News coverage
  failures, one HTTP 502 location failure and two expected HTTP 403 contact-scope
  denials**. The News corpus has an unreachable shard; strict coverage remains
  enforced. Historical successful News captures remain dated. No paid contacts,
  production keys, customer accounts or payments were created.
- Refreshed all **54 company-field examples**, three compact company summaries,
  seven app fields and 21 investor field/summary examples. Investor pagination
  still reaches all 268 dated portfolio rows and all 1,199 shortlist rows.
- Added selected traffic/review observations, sector/lifecycle/assessment context,
  financial evidence and operating context, app install/release details and
  internship observation/application metadata. Existing detail ownership,
  financial gates, contact scopes and billing boundaries remain in place.
- **228 tests passed locally**, including 15 new output/selection regressions.
  The [output audit](OUTPUT_DEPTH_AUDIT.md) records exact requests, current errors,
  before/after response shapes and reviewed adapter hashes. Public examples retain
  all captured business arrays; omitted source prose is explicitly listed.
- The 61-capture conservation comparison found 56 unchanged sets of existing
  business values and five independently confirmed source changes: three hiring
  snapshots and two absent innovation sections. No missing source value was
  backfilled from an older example. Docs validation, Ruff, package build and
  repository/archive credential scans passed; GitHub remains private with Pages
  disabled.

## Contact and LinkedIn depth follow-up: 2026-09-23

- Contact documentation now covers founder identity linkage, professional details,
  company/person emails and phones, social references, 24 typed request recipes,
  scopes, costs, fallback behavior and unsupported parameters. Three new guides
  display complete saved outputs and preserve missing/conflicting source results.
- Three live professional discovery calls and eight explicitly synthetic contact
  fixtures were captured. No live paid contact success or production account
  mutation is claimed. The research directory now has a readable index and source
  findings in addition to its original search JSON.
- The selected social field now reads underlying company LinkedIn snapshots and
  stored posts independently of derived enrichment. Real authenticated local
  gateway captures returned one profile each and 8/4/9 distinct posts for
  Razorpay/Stripe/Swiggy. Observation dates, full post content and array counts
  are preserved. See [the LinkedIn investigation](research/LINKEDIN_SOCIAL_FINDINGS.md).
- A live `item_limit=1` Razorpay request reported eight available posts, one
  returned and explicit truncation/partial flags. Compact company retrieval
  reported social availability without exposing followers or posts.
- **213 tests passed locally**, including seven new social-source regressions.
  Documentation checks verify all prior captures plus 18 authored contact
  requests, 20 displayed contact/social responses, 24 readable/JSON recipes,
  11 additional contact/discovery records and three refreshed social fields.
  Ruff and whitespace checks passed. Private GitHub visibility and disabled
  Pages were independently checked before push.

The contact values in fixtures remain fictional. Company and professional live
records remain source observations, not independent identity, current-role,
deliverability or audited-headcount verification.

## Current scenario release: 2026-09-23

- **53 shared REST/MCP data operations**, 16 account/discovery captures, 50 new
  executed business scenarios and all 43 company filter fields inventoried.
- New financial definition catalogue, precise dated USD financial screen and
  separate founders/key-people/professional team operation.
- Strict source matching by default for structured discovery; explicit expanded
  mode retains fallback/unverified labels. Filter-stripped searches cannot return
  a strict shortlist. Industry suggestions use Radar's actual dropdown vocabulary.
- Dedicated [financial](guides/financial-filters-data-api.md),
  [teams](guides/teams-people-data-api.md) and
  [technology/traffic](guides/technology-traffic-data-api.md) guides link every
  relevant scenario, including complete retained business arrays and baseline evidence.
- The [50-scenario audit](SCENARIO_AUDIT.md) found three baseline semantic failures
  and eleven unavailable workflows. After repair: 12 observed, 37 qualified,
  zero tested semantic failures, one unavailable News integration. This is a
  bounded semantic/data-coverage test, not a throughput benchmark or source-truth certification.
- **206 tests passed** locally, including every REST operation, Streamable HTTP
  and stdio MCP, numeric boundaries, missing financial values, financial source
  qualification, period selection, group-specific team filters, scope checks,
  bounded fan-out, metering/refunds and strict/expanded matching behavior.
- Real HTTP MCP initialization listed 53 tools and executed company retrieval.
  Swagger and the developer console/assets returned HTTP 200 on the temporary
  local gateway. No public deployment was performed.
- Docs checks validate 69 primary captures, 53 MCP examples, 91 primary/guide
  response blocks, the 50 additional scenario pages and both baseline/current
  hashes and projections. Existing company, investor, app and opportunity
  detail captures remain separately checked.
- The News test encountered an upstream connection failure. Older successful
  News examples are historical captures, not a claim that News works today.
- Ruff, package builds and documentation checks passed. Credential scanning found
  no known credential values in 455 repository files or 490 archive members.
- GitHub visibility was rechecked as private with Pages disabled before push.
  Public release still requires the user's approval. CI has no publication job.

The previous sections below are dated historical verification, not replacement
results for this release. See [the filter source analysis](FILTER_AUDIT.md) and
[all scenario outputs](scenarios/README.md) for the current evidence.

## Prior contract: 2026-09-21

- 50 shared REST/MCP retrieval operations and 16 account/discovery examples.
- Compact company identity, per-field availability and a required separate POST
  for one of 18 detail fields. No all-fields selector on get_company.
- Summary availability is computed in Mongo without returning contact values or
  rich arrays. Detail lookups use fixed projections and validated domain/public ID.
- Company filter catalog, bounded suggestions, 13 sort choices and separate selected
  columns. People search adds school, degree, seniority and company-name criteria.
- Company and professional contact endpoints require explicit contacts scope,
  linked Radar access and the source paid-plan gate. Only requested email/phone
  fields are returned; company-domain fallback stays labeled.
- Compact briefs/comparisons keep source windows, partial flags, latest financial
  evidence and follow-up requests; full archives stay on their detail endpoints.
- Source-provider CDN logo URLs are removed. The first-party Radar image fallback
  URL can serve a favicon and is not a promise of a high-resolution company logo.

The [source review](RADAR_SOURCE_REVIEW.md) maps these changes to the actual Radar
frontend, company search, column picker, people search and contact handlers.

## Automated verification

The suite verifies all 50 tools over real Streamable HTTP MCP and their REST
counterparts. Stdio is exercised through a spawned server. New regression coverage
includes compact-profile non-disclosure, each field's projection, missing/empty/
failed coverage, company ambiguity, contact scopes and linked credentials, source
plan denial even when the source also supplies values, requested email/phone
selection, company fallback labels, source-name filter translation, validated
sorts/columns, per-account contact throttling across workers and operation billing.

Existing checks cover key revocation/expiry, account isolation and re-verification,
transactional reservations, prepaid overspend prevention, failed-call refunds,
financial provenance and zero/negative values, date windows, oversized responses,
upstream errors, host/origin checks and bounded request bodies.

Local checks on 2026-09-21: **181 tests passed**. Documentation validation covers
all 66 endpoint captures, 50 MCP calls, 85 displayed responses, three compact
profiles, 54 individual company-field examples, 21 investor captures and seven app-field captures, including their original-response
fingerprints. Ruff and package builds passed. Credential/archive scans are
completed before the private push.
The previous private commit `fcef5b5` passed the Python 3.11 and 3.12
[CI matrix](https://github.com/fliarbi/radar-api-mcp/actions/runs/35575381767).
The same workflow checks this revision on push; it contains no deployment,
package publication, Pages or release job.

Earlier console browser QA covered key creation/revocation, usage, spending limits,
following, disabled checkout and disconnect at desktop and mobile widths using
synthetic providers. See [account QA](../qa/account-smoke.json). The current scope
picker additionally offers contact-only and data-plus-contact keys.

## Live company, filter and listing captures

Three authenticated local profile calls returned compact identities for Razorpay,
Stripe and Swiggy. Each company has 18 separate captured field requests (54 total).
The technology example preserves Razorpay's 70 merged stack entries; classification
and founders, traffic and apps appear only in their individual field responses.
See [company field examples](COMPANY_DATA_DEPTH.md). Arrays are not shortened by
the renderer; prose omissions and response fingerprints are recorded explicitly.

Live founded-year/employee-sort and engineer-hiring filters each returned two
company cards without a partial timeout. Live filter suggestions returned five
software business-model values. Selected
column retrieval returned the requested data points for Razorpay and Stripe.
Search, competitor, investor and comparison examples were refreshed through the
existing Radar HTTP service. They retain anonymous source-plan restrictions.
Current JSON captures, status codes, capture dates and limitations are enumerated
in the [complete example audit](EXAMPLE_AUDIT.md); status 200 alone does not prove
accuracy, complete coverage or nonempty results.

The local gateway read the existing native company store with a privately supplied
connection. No database writes, index changes, source restarts or production Radar
code edits were performed. This connection is not a deployed private service.

## Contact verification boundary

The default preview key's two actual contact calls returned 403 scope_required
before retrieving any contacts. These are intentional access-control results,
not upstream outages. Synthetic response tests verify successful email/phone
shapes and source plan gates. No production person contact, account token or
live private contact value is published in documentation. An entitled linked
Radar account is still required to verify live paid contact success.

## News and company-brief integration boundary

Eight News operations use real source applications and live archive queries with
isolated test identity/quota dependencies. They retain capture_kind=live_data_integration.
The refreshed Stripe brief uses the same isolated News identity alongside live
anonymous Radar reads and the native field store; all seven sections supplied
compact summaries. This does not verify a deployed News service or customer key.

Historical News examples query April 2026. General News reports data through
2026-08-24; business events and funding report 2026-05-05. Source freshness and
funding-quality warnings remain. Short headlines, URLs, dates and measured data
are preserved; article bodies and long quoted prose are omitted with explicit paths.

A temporary loopback gateway verifies real MCP initialization, tool discovery and
compact company retrieval. Browser/documentation route statuses are recorded in
[transport evidence](examples/transports.json). No persistent listener is installed.

## Multi-host ledger, proxy addresses and signup limits (2026-10-14)

Account mode can now keep its ledger in PostgreSQL (`RADAR_ACCOUNTS_DATABASE_URL`) for
workers on several hosts, trusts `X-Forwarded-For` only through `RADAR_TRUSTED_PROXIES`,
and admits new API accounts per client address and overall. `radar-api --workers N`
runs several processes in account mode; uvicorn's own proxy-header rewriting is off.
Revoking an unknown key now returns 404 instead of a success body.

Every account test runs against both SQLite and a disposable PostgreSQL 17 server:
288 passed locally (261 plus 27 skipped without `RADAR_TEST_POSTGRES_URL`).
`scripts/e2e_account_mode.py` drove real HTTP against 2 SQLite workers and 4
PostgreSQL workers with a stub identity service: 9/9 checks each for key issuance,
per-address signup limits, exact metering across workers, account budget and
concurrency, revocation, signed/forged/replayed webhooks and refund suspension.
CI runs both. Razorpay itself was not contacted; provider sandbox checkout remains open.

Location intelligence is fixed. After the LAN came back, the source's Redis
container on 192.168.50.2 was still stopped (since 2026-04-17, no restart policy) and
was started. The remaining empty results were a gateway bug: the source compares
exactly against lowercase stored names, so "India" matched nothing. The gateway now
lowercases locations, and sends `cc` codes as country names from the source's own
code lookup (238 codes), because the source's `cc` mode puts that lookup into SQL
unquoted and fails. Live through the gateway: India 458,846 companies (24/27 sections
filled), `cc=IN` identical, Bengaluru 17,069, Karnataka 45,030, Germany 285,750.

Live account-mode sweep (2 workers, a Business test account session, profile and
jobs Mongo plus the apps/social/company ClickHouse connected): 46 of 53 tools return
data, including contacts with an explicit `contacts` key and every detail tool with
real IDs (app, job, internship, investor page). Not live: 8 News tools (News services
not running) and `get_investor_field` (no verified investor release directory configured).

## Remaining limitations and setup

Location intelligence still has an upstream failure. Investor fields require a
verified release connection; event windows can be empty/restricted, and market pulse retains
flagged future-date and unknown-amount source anomalies. Display columns can
suppress zero/negative values or return empty on failure; use financials for
numerical statements and provenance. See [data quality](DATA_QUALITY.md).

Configure the read-only company store, authorized Radar and News links, private
account runtime and production sign-in separately. Checkout requires a configured
per-credit rate, provider credentials and sandbox payment/webhook verification.
Repository visibility, Pages status, remote bytes and CI are rechecked before
reporting a private push. Public release still requires explicit owner approval.

## Investor source depth and documentation regression checks

The local authenticated gateway now checks the live investor publication gate,
validates the immutable Atlas data fingerprint and exposes its business fields.
Anupam Mittal's summary contains 270 companies / 303 equity participations;
268 companies / 301 participations are dated. Ten profile fields and nine
FinTech/Bengaluru directory fields were captured individually, plus both summaries.
Pagination traversed all 268 dated company rows and 1,199 selected directory
investors. Source coverage remains 2026-05-22, with computation on 2026-09-14.
This is a connected read of a dated database-derived release, not live recomputation
or deployment of a public API. Emails and gated LinkedIn reveals stay excluded.

New tests verify source publication denials, held/mismatched release metadata,
SHA-256 integrity, path containment, explicit disconnected states, lossless paging,
filter/sort behavior, retained stage/example-company attributes, zero/null values
and private-field exclusion. REST and MCP exercise all 50 retrieval operations.
Documentation checks now reject shortened returned arrays and unexpected business
field omissions. Professional skills, education, experience and scores plus short
financial/funding headlines have regression coverage. See the full
[depth inventory](DATA_DEPTH_AUDIT.md), not HTTP status alone, when reviewing examples.


## App, internship and company-potential expansion

Twelve new operations were captured through the authenticated local gateway;
all returned HTTP 200. Seven additional app-field calls also returned HTTP 200.
The exact swiggy.com developer-host query returned four apps. The main app profile
exposes seven field groups and 15 install observations; its growth field retains
223,179,065 and 281,013,619 installs across 360 days, 25.91% observed change and
26.32% annualized change, plus source reliability/velocity flags. The snapshots
are June 2026 observations. UTC timestamps were verified on the actual queries.

Business Development internship search returned three of 222 matching records;
employer grouping returned actual names, observation counts, titles and IDs.
The selected detail belongs to MITRA Consultancy and records INR 2,200 without a
payment period. Its August 2 deadline is expired; the API does not describe it as
currently open. Explicit WFH title markers and listed city can coexist. Missing
locations are not guessed to mean remote, and far-future deadlines remain unverified.

The India/Payments mobile-scale screen returned Paytm and Paisabazaar with measured
app download/growth display evidence. All six preset definitions validate against
the real company-filter model. Source plan restrictions still apply; these screens
do not predict investment returns, purchase intent or budgets.

Regression checks cover intern/internship translation, salary/source/experience
forwarding, unsupported rollup paging/sorting, preset override rejection, app scope
and billing, parameterized read-only app queries, source timeouts, response limits,
private-field exclusion, null/zero values, history pagination and original-response
fingerprints. The expanded console scope picker and all 50 REST/MCP registrations
are included. See [source coverage](RADAR_FEATURE_COVERAGE.md) for remaining gaps.

The live [pagination check](../qa/expanded-data-smoke.json) traversed all 15 app
history rows and matched a single complete retrieval exactly. Thirteen rows are
duplicates: there are only two distinct dated measurements. No extra observation
dates are inferred. Two internship pages produced six unique listings and six
unique employer groups; the remote/part-time filter found 441 observed records.

## Business-model documentation recipes — September 25, 2026

[Scenarios 51–60](scenarios/README.md#business-model-and-revenue-model-scenarios)
add investment commissions, success fees, brokerage, insurance distribution,
recruitment fees, marketplaces, hybrid subscription/commission, lending, data
licensing and software services. The [business-model guide](guides/business-model-revenue-model-api.md)
separates company activity, revenue labels, investor portfolio preferences and
fee terms that require additional evidence.

The documentation checker validates 62 request bodies, ten curl/MCP examples,
eight real offline catalogue outputs, saved evidence projections and the hybrid
model check's missing/partial-coverage behavior. Generation was byte-idempotent;
the legacy fifty-scenario builder also preserves the new index section. Original
captured scenario requests, outputs and audit totals remain unchanged.

The initial recipes had no company-search captures. The follow-up now includes
ten exact main-search responses and four separate profile/classification reads:
two populated lists, six empty strict pages and two account denials. The linked
session returned `login_required` in a separate diagnostic. Source caching and
classification dates remain distinct from gateway retrieval times. Static
catalogue lookups remain local; the software vocabulary and Swiggy classification
are dated saved evidence.
See the [source findings](research/BUSINESS_MODEL_FINDINGS.md) and
[request/evidence manifest](research/business-model-recipes.json).

The local Fliar dashboard now includes a Radar API & MCP help panel through the
[optional integration](../integrations/fliar-dashboard/README.md). With no private
connection configured, it clearly reports unavailable key issuance. The account
console supports a same-origin mount prefix and displays the resulting REST/MCP
URLs. This is a local implementation; the public dashboard and proxy have not
been changed. GitHub publication remains private.

Browser verification used a disposable ledger and synthetic identity on loopback:
dashboard panel → console → connect session → create key → list metadata → revoke
→ dismiss reveal. The configured REST/MCP prefix was visible and desktop layout
had no horizontal overflow. The disabled panel displayed the unavailable state
without a launch link. [Enabled panel](images/radar-dashboard-key-enabled.png)
and [disabled panel](images/radar-dashboard-key-help.png) screenshots retain the
local-test banner. No real customer key or payment was created in this UI check.
