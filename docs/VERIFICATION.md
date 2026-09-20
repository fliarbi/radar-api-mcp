# Verification record

This record separates local implementation, fixture verification, live Radar reads,
live News access, repository visibility and deployment. It does not claim public
availability.

## Local implementation

- 30 operations generated from one registry into REST and MCP.
- Typed request validation and a shared documented response envelope.
- HTTP key authentication, per-client upstream credentials, revocation, expiry,
  per-process rate limits, host/origin checks and request/response bounds.
- Financial statement/period filtering with source, currency, zero-value and
  access-limit preservation.
- Partial briefs and comparisons retain section-level failures.
- User guide, operator guide, generated capability/OpenAPI reference and CI.
- Optional account mode: verified Radar session bridge, self-service key console,
  encrypted upstream links, scoped expiring keys, account-wide quotas, transactional
  usage reservations, prepaid spending caps and plan-limited API watchlists.
- Signed Razorpay captured-payment processing, replay protection and refund/dispute
  account suspension. Checkout remains disabled without a configured rate and keys.
- 16 expanded task-specific guides covering B2B/company data, financial data/statements,
  financial/funding news, investors, monitoring, hiring, MCP, keys and pricing.
- 46 endpoint references with captured output, downloadable JSON projections,
  parameter tables, field explanations and REST/MCP requests; a separate transport
  reference contains a real MCP initialization and browser-route responses.
- Optional, bounded read-only company profile connection with seventeen selectable
  sections: sectors and feeds, founders, technology, traffic, apps, products,
  geography, social, lifecycle, legal, assessments, hiring, innovation, activity,
  reputation, share of voice and website observations. Detailed profiles also
  appear in briefs and comparisons. Financial history retains its existing gates.
- Three complete live company examples and a field-by-field
  [data-depth walkthrough](COMPANY_DATA_DEPTH.md). Swagger includes a captured
  detailed profile, and documentation no longer cuts arrays to two items or
  financial examples to one period and six metrics.

## Automated checks

The test suite covers all REST operations and all 30 MCP tools through a real
Streamable HTTP client. Stdio MCP is tested through a spawned server process,
including invalid-key rejection. Other checks cover input attacks, secret
redaction, account isolation, immediate revocation, expiry, rate limits,
financial provenance, zero/negative amounts, date/cursor mapping, partial results,
upstream timeouts, redirects, oversized replies and application errors returned
with HTTP 200. Test data is synthetic.

Measured locally on 2026-09-20: **103 tests passed**, lint passed, shell syntax passed, and
wheel/source builds succeeded. Package contents and Git's selected files were
checked for credential material; the generated local key and key store are ignored.
Python 3.12 was exercised locally. The Python 3.11/3.12 GitHub CI matrix also
passed for the preceding detailed-profile commit `925410c` in
[Private preview checks](https://github.com/fliarbi/radar-api-mcp/actions/runs/35495285290).
The current revision is checked by the same workflow on push. A test-only fix
freezes the quota clock during the spoofed-forwarded-IP check and explicitly tests
the next minute; the first local run exposed a wall-clock rollover in that test.
No production rate-limit behavior was changed.

The added account tests cover verified/blocked identity rechecks, key ownership,
scope restrictions, creation/expiry limits, static-key bypass rejection, shared
REST/MCP usage, simultaneous workers, prepaid overspend prevention, partial/failure
refunds, downgrade gates, captured-payment amount/signature validation, duplicate
delivery, refund suspension, watchlist ownership and disabled checkout.

The detailed-profile tests cover native data depth, nested classification shapes,
source dates and zeros, section selection and array counts, authentication before
database reads, account scope/credit enforcement, public-ID/domain matching,
ambiguous domains, sanitized database failures, partial enrichment, response
bounds and REST/MCP parity. Source financial history and contact documents are
excluded from the profile projection.

Documentation checks validated **724 local links, 39 guide request examples,
62 displayed response blocks, 46 JSON endpoint captures and 30 MCP call examples**.
All published response excerpts matched unchanged fields from their 46 private
original captures. Three additional detailed company examples and the Swagger
example also passed schema, checksum and unchanged-projection checks. The validator
checks complete HTTP operation coverage against the account-mode OpenAPI schema,
response envelopes, request models and checksums.

Browser QA for the account implementation used a loopback server with synthetic
Radar identity/data responses at 1440px, 390px and 320px: key creation/revocation,
usage, spending limits, follow/unfollow, disabled checkout and disconnect passed;
no page overflow or JavaScript errors were observed. See the
[account QA summary](../qa/account-smoke.json). Screenshots remain local under
ignored `qa/private/`; they are not deployed assets.

Payment calls and webhook events were tested using synthetic provider fixtures.
No real card payment, provider sandbox Checkout session, live commercial charge,
production identity sign-in or production dashboard integration was exercised.
The expanded search research used an MCP bridge to the existing automation
Google/Bing routes: seven Google browser queries reached CAPTCHA, four Bing News
queries returned results, and four Google News RSS fallback queries completed
(three nonempty, one empty). Relevant primary pages were checked separately.
The [search research](SEARCH_RESEARCH.md) records those verticals and limitations;
it does not claim keyword volumes or general-web rankings.

## Private GitHub repository

[fliarbi/radar-api-mcp](https://github.com/fliarbi/radar-api-mcp) was created and
uploaded on 2026-09-20. GitHub's repository API confirmed `private: true` and
`visibility: private` after the push, and the remote main commit matched the local
implementation commit. The GitHub credential was used only at runtime and was not
stored in this repository or the GitHub CLI credential store.

## Live reads on 2026-09-19

The recorded [live smoke results](../qa/live-smoke.json) used the gateway against
the existing Radar service with anonymous upstream coverage:

| Capability | Result |
|---|---|
| Microsoft profile | HTTP 200 |
| Microsoft financials | HTTP 200; financial archive access limited |
| Microsoft events | HTTP 200; effective window preserved |
| OpenAI funding | HTTP 200 |
| Microsoft enrichment | HTTP 200 |
| Investor directory | HTTP 200 |
| Microsoft jobs | HTTP 200 |
| Professional name search | HTTP 200 |
| Microsoft business news | HTTP 503 `service_unavailable`; no connected News service |

That older smoke file stores only status, counts and access flags. The newer
endpoint documentation below adds full captured business fields and array rows;
raw captures and credentials remain uncommitted. Successful responses do not
establish complete dataset coverage or validate the source's financial figures.

Earlier direct source inspection also found that a company-name search could
exceed the probe timeout. The gateway reports upstream timeouts as 504; no broader
search-latency or all-feature live-availability claim is made. A Radar semantic
search returned results during exploration, but its relevance was not audited.

## Complete endpoint capture on 2026-09-20

The [capture index](examples/index.json) records all 30 data operations through
an authenticated local ASGI gateway and its configured live upstream HTTP service.
The existing preview key had no linked Radar session; anonymous free-tier source
limits applied. The capture used a twenty-second upstream timeout.
The company profile, brief and comparison were subsequently refreshed with the
private detailed company connection enabled; each refreshed record carries its
own capture timestamp.

- **27 HTTP 200 responses**, including empty and partial outputs and eight updated
  News integration captures described below.
- The original **8 HTTP 503 responses** came from unset News URLs before any news
  data query. They are superseded by explicit live-data integration captures;
  ordinary deployed News connectivity is still a separate setup requirement.
- Investor search **504 upstream_timeout**; location intelligence **502 upstream_unavailable**.
- Job detail **404 no_data**, using a deliberate nonexistent ID because the partial
  job search supplied no real ID. No successful job detail was fabricated.

The [data-quality record](DATA_QUALITY.md) documents identity ambiguity, conflicting
legal associations, approximate funding, future-dated pulse records, unknown
period ends, partial job counts and sparse salary coverage. Published examples
are unchanged projections with explicit omissions, not independently verified
company facts or claims of complete dataset availability.

Sixteen account/discovery operations were separately executed against a temporary
SQLite store and synthetic identity/payment providers. The sequence exercised
key creation/list/revocation, session reconnection, plan inspection, News linking,
watchlist add/list/remove, spending limits, order creation, signed capture and usage.
The sample ten-paise price and wallet are fixtures, not a launched tariff.

A real Streamable HTTP MCP client also initialized a temporary loopback gateway,
listed all 30 tools and retrieved the detailed live Razorpay profile. `/docs`, `/developer`,
`/developer/console.js` and `/developer/console.css` returned HTTP 200 with their
correct non-JSON content types. Developer assets were fetched in local account
mode. The [transport capture](examples/transports.json) records observed output.
Temporary documentation/search processes were stopped after capture; this work
made no production deployment or upstream service change.

### News data integration refresh

`scripts/capture_news_examples.py` loads the actual private general and business
News applications in process, routes authenticated Radar gateway requests through
them, and executes their real queries, article resolution, coverage gates, filters
and response sanitizers. An isolated test principal retains the News Free plan's
data limits; identity and quota dependencies are test fixtures. No listener,
production credential, customer account or customer usage charge is created.
The eight records use `capture_kind=live_data_integration` and explicitly state
that deployed connectivity and production News-key authentication are unverified.

All eight operations returned HTTP 200 on 2026-09-20. The examples query April
2026: software earnings matched one article; Microsoft company news returned five
of 4,401 matches; Microsoft events returned five of 68; funding returned five of
1,085. Overview, weekly trends and sentiment returned measured aggregates. The
article endpoint resolved the ID from news search and returned a 5,891-character
body. Documentation retains short headlines, attribution, dates, classifications
and numeric data, and lists omitted article prose explicitly. No external search
results or synthetic headlines were substituted for API results.

General news reported a latest available date of 2026-08-24, while business events
and funding reported 2026-05-05. These are historical examples with separate
dataset windows, not evidence of a current news feed. The source's ingestion
freshness warnings and unverified funding-outlier notes remain in the examples.

The additional live [Razorpay](examples/profiles/razorpay.com.json),
[Stripe](examples/profiles/stripe.com.json) and
[Swiggy](examples/profiles/swiggy.com.json) responses contain populated sectors,
primary/other feeds, founders, technology stacks, traffic and app metrics.
Razorpay returned two founders, seventy stack entries and eighteen other feeds;
no array in these three examples required truncation. MongoDB reads used fixed
collections, projected fields and indexed equality predicates. No database writes,
service restarts or changes to the production Radar application were performed.

## Remaining external setup

- Configure a read-only `RADAR_PROFILE_MONGO_URI` for the intended private runtime.
  The connection was enabled for local live verification; it is not a production
  deployment. Without it, the gateway explicitly labels profiles as `card` depth.
- Link authorized Radar sessions for deeper financial archive access.
- Activate private account mode behind an appropriate proxy, retain its encryption
  key, and validate the same-origin Radar sign-in connection with a test account.
- Set the per-credit INR rate and provider test credentials, then validate actual
  sandbox Checkout and webhook delivery before commercial activation.
- Connect the private News services and link a News API key, then run the news
  integration checks against those live authenticated services.
- No public service, public repository, package publication or release is approved
  or performed by this work. The repository must remain private until separate
  owner approval.
