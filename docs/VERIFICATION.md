# Verification record

This record separates local implementation, synthetic account/contact checks,
live data reads, GitHub state and deployment. The repository remains a private
preview; no public API, production checkout or paid contact access is claimed.

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
