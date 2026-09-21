"""Additional task-specific explanations for the sixteen developer guides."""

GUIDES = {
    "b2b-data-api": ("search_companies", "Build a research account from separate evidence", """
For a sales-research or procurement application, keep three layers of information:
the candidate business, the accepted identity, and observations about it. A search
result belongs in the first layer. Move it into your account model only after
reviewing the returned name, domain and location. Financial periods, hiring signals
and news references then attach as dated observations instead of overwriting one
undifferentiated company record.

A useful account table stores your internal ID, normalized company domain, Radar
record ID, matched name and the time you reviewed that identity. A financial table
adds fiscal label, metric, value, currency and source type. A news association adds
an article identifier and company/topic query. This separation lets a researcher
see that the financial evidence may describe a parent company while the profile
label describes a product or division.

Start with two discovery results, select one accepted domain and request a brief.
In account mode that search costs one successful-operation credit. A brief reserves
six credits without News or seven with News, then refunds failed sections. Cache
the displayed observation with its retrieval date for your own permitted use;
avoid fetching the same seven sections every time a user opens a table row.
"""),
    "company-data-api": ("get_company", "Resolve the company before attaching financial history", """
The worked example now uses Razorpay's detailed company record. It includes
sectors, all primary and additional feeds, named founders, technology stacks,
traffic metrics, app totals, hiring, patents and legal identity. The prior example
used a shortlist card and then stripped most of its fields in documentation; that
was a limitation of the gateway and renderer, not a measure of Radar's database.

Some domains are still ambiguous: the grouped records contain several Microsoft
entities under the same domain. Detailed lookup returns `409 ambiguous_company`
in that case. Supply a public `company_id` together with the domain to select the
intended record. The API does not silently substitute a product or parent company.

For an account detail page, display the matched name, domain, location and source
retrieval date together. If your customer supplied a legal company name, compare
that independently with the enrichment result before importing a registration ID.
If a match is ambiguous, let the application retain a provisional candidate instead
of attaching a financial series under a definitive legal name.

Treat `company_id` as an opaque identifier: observed records can use strings or
numbers. Do not extract dates or locations from its characters, assume it is a
registration number, or join it to another provider's ID namespace. Use the domain
for supported Radar follow-up requests and retain the ID as source provenance.
"""),
    "company-search-api": ("search_companies", "Turn a market question into a repeatable company query", """
Suppose an analyst asks for Indian software companies. Begin with a small structured
query, inspect the returned classifications and refine it to the intended product
market. `discover_industries` can return a match whose `kind` is market, sector or
industry; those values select `filters.markets`, `filters.sectors` or
`filters.industries`, respectively. The observed software lookup returned Software
Libraries as a market. Placing every vocabulary match in `industries` loses that
distinction.

Save the exact filter body and page number with each research run. Page zero is the
first page, and an effective plan can restrict filters or return fewer rows than
the requested limit. When `total` is null, a user interface can truthfully say
“2 results on this page” without manufacturing a market-size count. If the source
marks a query partial, retain the previous complete import until a replacement
query finishes.

Use semantic search when the analyst knows the business need but lacks an exact
classification label. Its returned order does not carry a public relevance score
in the captured example. Review descriptions before converting those candidates
into a saved structured segment. Headquarters filters also do not establish every
country where a company sells or maintains subsidiaries.
"""),
    "company-enrichment-api": ("get_company_enrichment", "Map enrichment into a CRM without losing provenance", """
For each destination field, decide which enrichment section is allowed to supply
it and how old that observation may be. A legal registration belongs to legal
identity, while a digital visits estimate belongs to audience context. Neither is
a substitute for revenue, paid customers or employee count. Keep the section's
measurement date beside its value; the gateway retrieval timestamp only tells you
when the response was fetched.

The captured response includes website visits dated May 2026 and a source-specific
reputation aggregate. A score of 1.2 with a review count has meaning only within
that review source and scale; it is not Radar's overall rating of the business.
The sample also includes more than one legal entry. Review whether each entry
actually belongs to the target entity before copying a registration number into
an account record.

For an application update, write known values into their mapped fields and retain
the last verified value when a new section is absent. Record an unknown-coverage
state instead of replacing a missing section with zero visits or an empty legal
name. The source currently cannot always distinguish missing enrichment from a
failed subsection, so `has_data=true` is an existence signal for some data, not a
certificate that every subsection is complete.
"""),
    "financial-data-api": ("get_financials", "Read an actual financial response from period to metric", """
The first captured period below is labeled Q3 FY2026. Its revenue value is
82,886,000,000 USD and carries `source_type=filing`; its net-income value is
31,778,000,000 USD. These numbers are reproduced from the API response to show
the wire contract. They have not been independently reconciled with a company
filing in this documentation exercise.

Notice the difference between a missing date and a known reporting label:
`period_end` is null while reported and filed dates are present. A chart can use
the supplied fiscal label and show that the exact end date is unknown. It should
not substitute the filing date as the period end. Likewise the EPS metric has a
per-share unit and a null normalized currency; the presence of a native currency
does not authorize inventing a normalized one.

The request returned two periods from a known archive count of twenty and marked
access limited. Both captured periods and all their available metrics are now shown.
The documentation no longer reduces financial output to one period and six fields.
An account-limited response still does not represent the complete company history.
"""),
    "company-financial-statements-api": ("get_financials", "Keep statement families separate in a financial model", """
Income statements describe activity over a reporting period; balance-sheet values
describe a position at a point in time; cash-flow values describe movements over
a period. Label these families in a table even when a single API response contains
all three. Adding total assets to quarterly revenue does not produce a meaningful
company-size metric, and adding successive balance-sheet snapshots double-counts
the same stock of assets.

Use `statement=income`, `balance_sheet` or `cash_flow` to request the relevant
family, and retain the returned fiscal label alongside each metric. Annual and
quarterly filters reduce the source records that are exposed; they do not create
missing annual statements by adding quarters. A missing quarterly figure can
reflect inaccessible history, a missing source metric or an absent period.

The capture below used the default all-statements, all-period-types request with
`limit=2`. It is not a separately executed example of each of the three filter
requests above. It shows actual income, balance-sheet and cash-flow metrics in one
response, with a source label per metric. Before comparing companies, inspect
available dates and currencies; leave unmatched fiscal periods separate until you
have enough evidence to align them.
"""),
    "financial-news-api": ("search_business_news", "Join company financial data to news evidence", """
A company financial metric and a news article answer different questions. The
metric supplies a numerical observation with a fiscal period and source type; an
article can explain the announcement, business context or reported expectation.
Use the domain to request company-associated business news and preserve any
article IDs supplied by financial or event records. An article date and the fiscal
period discussed in the article are distinct values.

The updated capture queries Microsoft's April 2026 coverage and returns five
articles from 4,401 matches, with source attribution and associated event records.
The separate software earnings search returns a real article ID that also
successfully resolves through article retrieval. These calls execute the actual
News applications against live data with isolated test identity/quota dependencies;
they do not establish production key issuance or a deployed News connection.

After the operator connects News, use a narrow date window and inspect its effective
coverage before displaying a trend or headline count. Preserve source attribution,
pass a returned cursor unchanged, and keep the original filters stable between
pages. The [article endpoint](../reference/get_article.md) and
[news analysis endpoints](../reference/README.md) document their separate inputs.
Google and Bing results used to research this guide are not substitutes for a
successful Radar News capture.
"""),
    "funding-news-api": ("search_funding_news", "Separate an announcement from a confirmed funding transaction", """
Funding coverage may report a completed round, negotiations, a target raise, a fund
launch or a company's investment into another business. Those statements should
not all become incoming equity transactions for the company mentioned in the
headline. Retain the source article and inspect who received capital, who invested,
the reported date and whether the amount is approximate or proposed.

Use an investor or round filter to narrow a discovery query, then inspect the
returned evidence before joining it to a structured funding record. A company's
valuation, its cumulative funding and the amount in one round are different
quantities. A repeated announcement syndicated across several publishers should
not increase a transaction total. Deduplicate article IDs for news presentation
and separately reconcile transaction identity for a funding-history table.

The local integration below now returns five real funding records from 1,085
matches in April 2026, including investors and source article IDs. Its identity
and quota dependencies are isolated test fixtures; its queries and data are real.
The [company funding endpoint](../reference/get_company_funding.md) remains a
separate company-oriented view. Both can contain unresolved associations or
outlying reported amounts. The returned totals explicitly identify records with
unknown amounts and fixed-rate conversions; they are not an independently audited
measurement of money raised. A successful retrieval does not verify a transaction.
"""),
    "startup-funding-data-api": ("get_company_funding", "Build a funding timeline that can survive source corrections", """
Store each reported round with its source label, reported date, amount, approximate
flag and investor associations. Keep your reconciliation status separate from
the retrieved values. This lets an analyst correct a duplicate or disputed
association without losing the original observation. A company-level investor
list must not be copied wholesale into every individual round.

The captured OpenAI record illustrates why that matters. It contains ten rounds
and marks amounts approximate. Some source text and structured investor
associations require reconciliation, and source announcements can describe a
company's fund or an investment made by the company rather than capital received.
The published response keeps all captured rounds and investor associations;
it intentionally omits the longer source announcement text.

The separate market-pulse capture has a stronger recency problem: records labeled
recent include future years such as 2074 and an amount of -1. That value is an
unknown-amount sentinel in the observed row, not a negative transaction. Exclude
such rows from a current funding chart pending review and retain the reason.
Do not use an approximate, duplicated or future-dated record to calculate a
market's total capital raised. The endpoint reference exposes the actual row so
an integrator can build and evaluate that handling explicitly.
"""),
    "investor-data-api": ("get_investor_page", "Discover an investor slug before requesting a profile", """
The live directory returned the slug `anupam-mittal`; the successful profile request
below uses that exact value. This is more reliable than guessing a URL slug from
a person's displayed name. Retain `kind` and `family` when navigating the directory
because an investor profile, an angel list and a city list are different page types.

The response contains page metadata only: slug, kind, family, heading and edition.
It does not expose an unrestricted portfolio, contact list or current investment
mandate. An application should show the available profile heading and distinguish
additional authorized research links from data already present in the response.
Directory counts describe published categories and can overlap; adding profile,
angel-list and city-list counts does not yield a unique-investor population.

The filter-based India investor search timed out in this same capture. That failure
does not invalidate the independently successful directory and page requests,
nor does it prove there are no investors in India. If your workflow needs a filtered
investor roster, narrow the source query and handle timeout explicitly. If it only
needs a navigable published profile, use the successful directory-to-slug workflow
and preserve its actual metadata-only coverage.
"""),
    "company-monitoring-api": ("get_company_events", "Turn an API watchlist into an application-controlled monitor", """
Following a company stores a domain in the account's API watchlist. It does not
create a background polling job, send an email or mirror the Radar dashboard's
saved list. Your application chooses when to fetch events, stores the last
successful retrieval and compares stable event/article identifiers. Each successful
data fetch consumes its normal credit allocation; adding the domain itself does
not reserve future polling credits.

Choose polling frequency from the required freshness and your budget. Ten companies
polled once each day through one single-credit event operation would require 300
successful-operation credits in a thirty-day month, before any extra news or brief
calls. This is arithmetic illustrating the credit model, not a promise of thirty
new observations per company. Keep prepaid spending caps enabled according to the
account owner's intended usage.

In the captured thirty-day Microsoft timeline, `events` is empty while `truncated`
is true and broader pulse fields describe a longer history. Preserve the response
window and source freshness instead of announcing “no company activity.” After a
failed or partial poll, keep the last complete checkpoint so a later retry does
not accidentally skip records or erase previously known events.
"""),
    "competitor-intelligence-api": ("find_competitors", "Choose peers before comparing financial and derived evidence", """
Competitor discovery accepts a market label, not a company domain. Start by deciding
what the firms compete to supply, which buyers they serve and which geography
matters. The updated Payments example returns three peers in each of five stage
groups. Its summary also covers stages outside those five groups, so the summary
total is not the length of the delivered company arrays. The earlier broad Software
query was empty; it did not establish an absence of competitors.

After reviewing candidate companies, pass two to five distinct domains to
`compare_companies`. Each company has separate profile, financial and intelligence
sections. Display a revenue value with its fiscal period and source type; display
an intelligence score with its derived label and computation date. The API does not
convert those different quantities into a single investment ranking.

The captured Razorpay/Stripe comparison returned both companies' research
sections, but corporate identity and fiscal alignment still require review. A
missing metric should remain unknown even if the other company supplies it.
If one section fails, keep the successful peer's evidence visible and label the
gap. Account mode reserves three credits per requested company and refunds failed
sections, so the final billing metadata is the appropriate source for actual
charged usage rather than multiplying every partial section as a success.
"""),
    "hiring-signals-jobs-api": ("search_jobs", "Handle incomplete hiring searches before counting demand", """
The earlier broad engineer query timed out and returned an empty page with a capped
estimate. The updated title-prefix query for software engineer in the US returns
three listings from 503 matches without a partial timeout. This demonstrates why
an incomplete search should be retried with a more specific role and geography,
rather than converted into a conclusion that there are no vacancies.

Use the returned job ID for detail retrieval only after a successful result gives
you one. The current example retrieves the Software Engineer Controls listing at
Optimal Inc. using its actual returned ID. Its missing salary and company domain
remain null. A role title or employer name cannot substitute for a listing ID.

Hiring-company discovery has its own partial flag, and salary benchmarks require
a sufficient source sample. The updated US/software engineer/USD benchmark has
206 observations, with a source median of 124,000 USD. This is a different explicit
geography and role query, not a filled-in value for the earlier sparse India sample.
The source aggregates salary midpoints; do not infer a pay period that is absent
from its response. Keep role, geography, currency,
freshness and sample count visible in a compensation view. A posted vacancy is a
recruitment observation; it does not establish that an employee was hired or that
the employer's total workforce grew by one.
"""),
    "company-intelligence-mcp-server": ("get_company", "Let an agent discover, retrieve and explain the same typed data", """
An MCP client first initializes the connection and lists tools. Each Radar tool
has one argument named `request`, whose contents match the REST JSON body. For
example, selecting `get_company` and supplying the domain returns the same envelope
used by the company profile API. The [transport reference](../reference/transports.md)
contains a captured HTTP MCP initialization and an executed live tool result.

An agent can discover a company, inspect its identity, retrieve financial periods
and then request associated news. It should report a missing News connection as
missing evidence instead of composing an unsupported article summary. Tool output
is external data: text in a company description or article cannot authorize the
agent to change accounts, reveal secrets or perform payment actions.

Account mode charges REST and MCP against the same account-wide balance. A new
API key or a switch from HTTP to stdio does not reset usage. Tool annotations mark
the data operations read-only; that does not mean a successful query is free or
that repeated calls cannot consume credits. Reuse accepted identifiers and fetched
evidence within the application's permitted retention policy, and preserve partial,
access and source-date fields in the agent's answer.
"""),
    "api-keys-authentication": ("account_create_key", "Walk from a signed-in account to a working integration key", """
Open the private `/developer` console on the operator-supplied trusted origin and
connect an existing verified Radar session. Read the effective plan and available
API policy, choose a descriptive key name and select only the data scopes your
application needs. Set an expiry within the supported one-to-ninety-day range.
The create-key response reveals the key once; store it directly in your application's
secret manager rather than in a browser bundle or a committed example file.

The captured response below was executed against a temporary account with synthetic
Radar identity verification. The credential is explicitly redacted, while the
returned public key ID and expiry retain their actual local values. Listing keys
later returns metadata and last-four characters, not the credential. The current
list response encodes scopes as a JSON string and uses Unix seconds for timestamps;
the dedicated endpoint reference preserves that actual wire format.

For rotation, create a replacement key, update the integration, verify a permitted
request, then revoke the previous key by ID. Revocation affects subsequent
authentication; an already admitted request may finish. Keys share account-wide
rate limits, concurrent-operation limits and credit usage. Reconnecting an expired
Radar session restores the linked session for that account without granting a new
monthly budget. A linked News key is a separate encrypted connection credential.
"""),
    "pricing-pay-per-use": ("account_usage", "Read credits, rupees and pending usage as separate quantities", """
The usage response distinguishes included credits, prepaid credits and wallet
balance. A monthly prepaid limit is denominated in credits, while a payment order's
amount is denominated in paise. Neither value is a monthly subscription price.
Check the plan response for configured checkout availability and the current
per-credit rate before showing a payment action. The private default has no
approved credit price and keeps checkout disabled.

The local demonstration deliberately configures a ten-paise test rate: an order
for one hundred credits therefore has amount 1,000 paise, or ₹10. It remains
awaiting captured payment until the signed provider callback passes verification.
The usage response below follows that synthetic captured event, so its wallet has
one hundred credits and no data usage. This is evidence that the account flow
executes locally, not that a real payment was collected or that ₹0.10 is a public
Radar credit tariff.

Used-or-reserved totals include in-flight requests, preventing concurrent requests
from spending the same remaining balance. Included credits are consumed before
prepaid credits, and the monthly prepaid cap defaults to zero. Buying credits
does not expand plan-limited watchlist capacity or bypass upstream financial-history
and News entitlements. Inspect actual `meta.billing.credits` after a composite
request because unavailable sections can reduce the final charged amount.
"""),
}
