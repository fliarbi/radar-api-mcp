# Verification record

This record separates local implementation, synthetic account/contact checks,
live data reads, GitHub state and deployment. The repository remains a private
preview; no public API, production checkout or paid contact access is claimed.

## Current contract: 2026-09-21

- 37 shared REST/MCP retrieval operations and 16 account/discovery examples.
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

The suite verifies all 37 tools over real Streamable HTTP MCP and their REST
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

Local checks on 2026-09-21: **143 tests passed**. Documentation validation covers
all 53 endpoint captures, 37 MCP calls, 69 displayed responses, three compact
profiles and 54 individual field examples, including their original-response
fingerprints. Ruff and package builds passed. Credential/archive scans are
completed before the private push.
The previous private commit `c4b5ce5` passed the Python 3.11 and 3.12
[CI matrix](https://github.com/fliarbi/radar-api-mcp/actions/runs/35555371062).
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

Location intelligence still has an upstream failure. Investor pages can be
metadata-only, event windows can be empty/restricted, and market pulse retains
flagged future-date and unknown-amount source anomalies. Display columns can
suppress zero/negative values or return empty on failure; use financials for
numerical statements and provenance. See [data quality](DATA_QUALITY.md).

Configure the read-only company store, authorized Radar and News links, private
account runtime and production sign-in separately. Checkout requires a configured
per-credit rate, provider credentials and sandbox payment/webhook verification.
Repository visibility, Pages status, remote bytes and CI are rechecked before
reporting a private push. Public release still requires explicit owner approval.
