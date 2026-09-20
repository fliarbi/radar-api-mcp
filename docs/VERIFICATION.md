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
- 16 task-specific guides covering B2B/company data, financial data/statements,
  financial/funding news, investors, monitoring, hiring, MCP, keys and pricing.

## Automated checks

The test suite covers all REST operations and all 30 MCP tools through a real
Streamable HTTP client. Stdio MCP is tested through a spawned server process,
including invalid-key rejection. Other checks cover input attacks, secret
redaction, account isolation, immediate revocation, expiry, rate limits,
financial provenance, zero/negative amounts, date/cursor mapping, partial results,
upstream timeouts, redirects, oversized replies and application errors returned
with HTTP 200. Test data is synthetic.

Measured locally on 2026-09-20: **88 tests passed**, lint passed, shell syntax passed, and
wheel/source builds succeeded. Package contents and Git's selected files were
checked for credential material; the generated local key and key store are ignored.
Python 3.12 was exercised locally. The Python 3.11/3.12 GitHub CI matrix also
passed for the earlier 71-test implementation commit `7cab8a7` in
[Private preview checks](https://github.com/fliarbi/radar-api-mcp/actions/runs/35483543316).

The added account tests cover verified/blocked identity rechecks, key ownership,
scope restrictions, creation/expiry limits, static-key bypass rejection, shared
REST/MCP usage, simultaneous workers, prepaid overspend prevention, partial/failure
refunds, downgrade gates, captured-payment amount/signature validation, duplicate
delivery, refund suspension, watchlist ownership and disabled checkout.

Documentation checks validated **154 local links and 24 guide request examples**
against the API input models. Browser QA used a loopback server with synthetic
Radar identity/data responses at 1440px, 390px and 320px: key creation/revocation,
usage, spending limits, follow/unfollow, disabled checkout and disconnect passed;
no page overflow or JavaScript errors were observed. See the
[account QA summary](../qa/account-smoke.json). Screenshots remain local under
ignored `qa/private/`; they are not deployed assets.

Payment calls and webhook events were tested using synthetic provider fixtures.
No real card payment, provider sandbox Checkout session, live commercial charge,
production identity sign-in or production dashboard integration was exercised.
Google result pages returned an unreadable redirect and then a browser traffic check; the documentation's terminology
research used available web search and primary pages, as recorded in
[search research](SEARCH_RESEARCH.md).

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

Only response status, list counts and coverage/access flags are stored. No full
financial/news payloads or credentials are committed. Successful responses do not
establish complete dataset coverage or validate the source's financial figures.

Earlier direct source inspection also found that a company-name search could
exceed the probe timeout. The gateway reports upstream timeouts as 504; no broader
search-latency or all-feature live-availability claim is made. A Radar semantic
search returned results during exploration, but its relevance was not audited.

## Remaining external setup

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
