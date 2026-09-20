# Observed data quality: company identity, financial coverage and news availability

These observations come from the **2026-09-20 endpoint captures**, not a statistical
audit of the full database. They describe exact integration consequences. A
successful HTTP response establishes retrieval, not the truth or completeness of
every source field. The [endpoint index](reference/README.md) links each captured
request to its response and provenance.

| Observed behavior | Example | What an application should do |
|---|---|---|
| A company domain can match several distinct records | Earlier card lookup selected Microsoft Dynamics CRM; the new detailed reader found multiple `microsoft.com` records | The detailed route now returns 409 until a public company ID disambiguates the domain |
| Legal enrichment can include unreconciled associations | [Enrichment](reference/get_company_enrichment.md) returned Microsoft Corporation and a second legal entry, BI Partners in Latvia | Do not treat every registration as a verified subsidiary; retain an unresolved state |
| Financial archive exists beyond current access | [Financials](reference/get_financials.md) returned 2 periods from an archive count of 20 with `access_limited=true` | Display the access qualification and avoid inferring complete history |
| Fiscal period end can be unknown | The first captured financial period had `period_end=null` | Preserve its fiscal label; do not substitute filed date for period end |
| A metric can have incomplete currency metadata | EPS had `currency=null`, `unit=per_share`, and a supplied native currency | Keep those original distinctions; do not guess a conversion |
| Funding associations require reconciliation | [OpenAI funding](reference/get_company_funding.md) included approximate amounts and source/structured-association disagreements | Review announcements, transaction direction and duplicate reports before summing rounds |
| A “recent funding” row can have a future date | [Market pulse](reference/market_pulse.md) returned years 2074/2072 and `latest_deal_amount=-1` | Exclude from a current timeline pending review; do not interpret -1 as negative dollars |
| Empty data can be partial | [Jobs](reference/search_jobs.md) returned `jobs=[]`, `total_estimate=10000`, `total_capped=true`, `partial_timeout=true` | Show incomplete search, retain earlier observations and narrow a retry |
| A salary query may lack a useful sample | [Salary benchmark](reference/salary_benchmark.md) returned `count=0`, `sparse=true` | Keep salary unknown; no mean or range was supplied |
| Company event windows and pulse history differ | [Events](reference/get_company_events.md) returned an empty 30-day list plus broader activity indicators | Label each window separately; empty recent history is not no company activity |
| A role category is not a verified employment fact | [Professional search](reference/search_people.md) combined a Microsoft executive title with an Angel Investor category | Review professional context before using the category in a funding relationship |
| A successful investor page can contain only metadata | [Investor page](reference/get_investor_page.md) returned slug, kind, family, heading and edition | Do not imply an unrestricted portfolio or contact roster |
| An unavailable section can coexist with a successful brief | [Company brief](reference/company_brief.md) returned six Radar sections and a News error | Render each section's availability and preserve `partial=true` |

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

Investor search returned **504 `upstream_timeout`** under the capture's twenty-second
bound. Location intelligence returned **502 `upstream_unavailable`**. The deliberate
nonexistent job identifier returned **404 `no_data`** because the preceding partial
job search supplied no usable listing ID. None of those failures is evidence of
zero investors, zero economic activity or zero vacancies.

## Read the examples without confusing excerpts and service limits

Documentation examples now retain all captured business fields and array rows.
The prior one-period/six-metric financial excerpt and two-item array cap have been
removed. Short News headlines and source links are retained; full article bodies,
ledes, long source quotations, review snippets and biographies are explicitly
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
