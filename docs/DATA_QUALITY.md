# Observed data quality: company identity, financial coverage and news availability

These observations come from the **2026-09-20 and 2026-09-21 endpoint captures**, not a statistical
audit of the full database. They describe exact integration consequences. A
successful HTTP response establishes retrieval, not the truth or completeness of
every source field. The [endpoint index](reference/README.md) links each captured
request to its response and provenance.

| Observed behavior | Example | What an application should do |
|---|---|---|
| A company domain can match several distinct records | Earlier card lookup selected Microsoft Dynamics CRM; the new detailed reader found multiple `microsoft.com` records | The detailed route now returns 409 until a public company ID disambiguates the domain |
| Legal enrichment can include unreconciled associations | [Stripe enrichment](reference/get_company_enrichment.md) includes Stripe, Inc. and entries such as STRIPE WOOD s.r.o. | Do not treat a similar name or every returned registration as a verified subsidiary; retain an unresolved state |
| Financial archive exists beyond current access | [Financials](reference/get_financials.md) returned 2 periods from an archive count of 20 with `access_limited=true` | Display the access qualification and avoid inferring complete history |
| Fiscal period end can be unknown | The first captured financial period had `period_end=null` | Preserve its fiscal label; do not substitute filed date for period end |
| A metric can have incomplete currency metadata | EPS had `currency=null`, `unit=per_share`, and a supplied native currency | Keep those original distinctions; do not guess a conversion |
| Funding associations require reconciliation | [OpenAI funding](reference/get_company_funding.md) included approximate amounts and source/structured-association disagreements | Review announcements, transaction direction and duplicate reports before summing rounds |
| A “recent funding” row can have a future date | [Market pulse](reference/market_pulse.md) returned years 2074/2072 and `latest_deal_amount=-1` | Exclude from a current timeline pending review; do not interpret -1 as negative dollars |
| A narrower query can recover from an empty timeout | [Jobs](reference/search_jobs.md) now returns three listings from 503 US software-engineer matches; the earlier broad query was partial and empty | Keep the actual filters and partial flags; do not treat the old timeout as zero vacancies |
| Salary coverage depends on the requested sample | [Salary benchmark](reference/salary_benchmark.md) now has 206 US/USD observations; the earlier India/INR query was sparse | Keep geography and currency distinct; do not substitute US values for a missing India sample or invent a salary period |
| Company event windows and pulse history differ | [Events](reference/get_company_events.md) returned an empty 30-day list plus broader activity indicators | Label each window separately; empty recent history is not no company activity |
| A role category is not a verified employment fact | [Professional search](reference/search_people.md) combined a Microsoft executive title with an Angel Investor category | Review professional context before using the category in a funding relationship |
| A successful investor page can contain only metadata | [Investor page](reference/get_investor_page.md) returned slug, kind, family, heading and edition | Do not imply an unrestricted portfolio or contact roster |
| A successful brief still combines different windows and access methods | [Company brief](reference/company_brief.md) now returns seven sections, using live Radar and an isolated News integration identity | Retain section dates and provenance; this does not activate a deployed News connection |
| HTTP 200 can contain an unresolved investor identity | [Investor search](reference/search_investors.md) includes Anon with domain linkedin.com alongside named investors | Review identity before associating a card with a fund, mandate or financing transaction |

## Failed requests are recorded, not replaced with fictional successes

The original eight News operations returned **503 `service_unavailable`** before
querying any data because their service URLs were unset. Updated examples now
return **HTTP 200** through the actual News applications against live archive data,
using isolated test identity/quota dependencies. Their `capture_kind` is
`live_data_integration`; customer-key authentication and a deployed News service
are not verified by these captures. Ordinary runtime use still requires both
service URLs and an authorized News key.

The exact software earnings query matches one April article; Microsoft's query
matches 4,401. A small filtered result does not measure the entire archive. General
news reports `data_through=2026-08-24`, while events and funding report 2026-05-05.
Recent news ingestion is explicitly marked thinner after May. Funding aggregates
include unverified outliers and fixed-rate conversions, with unknown amounts
counted separately. Search-engine research is not used as API response data.

Investor search now returns **HTTP 200** with five cards, and job detail returns
**HTTP 200** for an ID actually returned by search. The previous timeout and
deliberate nonexistent-ID examples were superseded by these new captures.
Location intelligence was retried and still returns **502 `upstream_unavailable`**;
a direct source request returned HTTP 500. That remains an unresolved source
failure, not zero economic activity. The [complete audit](EXAMPLE_AUDIT.md) records
all successful, empty, partial, restricted, failed and fixture-backed examples.

## Read the examples without confusing excerpts and service limits

Documentation examples now retain all captured business fields and array rows.
The prior one-period/six-metric financial excerpt and two-item array cap have been
removed. Short News headlines and source links are retained; full article bodies,
ledes, long source quotations, job-description prose, review snippets and biographies are explicitly
omitted where applicable. API-level profile limits are separately recorded in
`coverage.arrays`; a default limit of 100 did not truncate any array in the three
[deep company examples](COMPANY_DATA_DEPTH.md). The financial endpoint continues
to preserve its source account gates and available period counts.

Account, payment and key-management examples execute real local code against
synthetic providers. Their sample wallet and test price do not prove live payment
processing or commercial activation. See [account usage](reference/account_usage.md),
[pricing](guides/pricing-pay-per-use.md) and [verification](VERIFICATION.md).

## Refresh a capture

From an authorized private checkout, run `scripts/capture_live_examples.py` with
an existing preview key or configured account key, then review the ignored raw
output. `scripts/capture_account_examples.py` exercises a temporary synthetic
account and `scripts/capture_transport_examples.py` records an initialized MCP
session. These commands perform queries and can consume configured upstream/API
quotas; they do not publish the repository or enable a payment tariff.

`scripts/capture_news_examples.py` instead loads the sibling News applications
in process with isolated test identity/quota dependencies and real read-only data
queries. It opens no listener and creates no production key or customer usage.
This separate capture method is recorded in each updated News example.

After reviewing retained fields and source associations, run
`scripts/build_endpoint_docs.py` and `scripts/check_docs.py`. The latter verifies
operation coverage, request models, response envelopes, capture checksums and
rendered JSON. When private raw captures are available locally, it also checks
that every published field is an unchanged projection of the original response.
Do not replace a failed example with an invented successful payload to improve the
appearance of a guide. Capture and review an actual successful response instead.

## Compact profiles, contact gates and display columns

`get_company` returns identity and availability metadata. The eighteen rich fields
have separate requests and [captured outputs](COMPANY_DATA_DEPTH.md). `company_brief`
returns summaries and links to detail requests. Source CDN logo URLs are no longer
passed through; the Radar image route can fall back to a favicon.

The two contact examples intentionally show the default key's `403 scope_required`.
This is not an upstream outage. The paid source check, explicit key scope, selected
email/phone output and per-account limits are implemented and fixture-tested;
live production contact access has not been verified. Company fallback contact
details are labeled and are not verified person-specific addresses.

Listing-column values are formatted display strings. The source can suppress zero
and negative numbers or return an empty map on failure, so absent values remain
unknown. These columns cannot replace the precise, provenance-bearing financials
endpoint. See [filters and listings](FILTERS_AND_LISTINGS.md) and [contacts](CONTACTS.md).
