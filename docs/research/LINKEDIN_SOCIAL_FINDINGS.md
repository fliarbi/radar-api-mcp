# LinkedIn data depth: why the social example originally contained only links

Investigated and corrected on **2026-09-23** after the Razorpay social example
omitted followers, employee counts and posts that existed in the source store.

## Root cause

The company-field implementation read `main_data.descriptive.social` and the
optional `company_enrichment.social` Mongo block. It did not query the underlying
ClickHouse LinkedIn profile logs or social posts. The documentation therefore
described the limited adapter's output as the available social capability.

The source enrichment builder computes its social block from `li_company_signals`,
requiring positive followers and at least one post in its 12-month measure. That
derived signal table had **no Razorpay row** at review time, and Razorpay's Mongo
enrichment had **no social block**. Neither absence established that its underlying
LinkedIn records were missing.

An exact-domain source read found one Razorpay LinkedIn profile snapshot with
**1,252,056 followers**, **4,052 employees**, company size **1,001–5,000**, and eight
stored LinkedIn posts. The snapshot was observed at **2026-07-02T15:19:12Z**.
This was an adapter coverage gap, not justification for fabricating missing values
or claiming the database held only links.

## Corrected request and source mapping

The existing `get_company_field` / `POST /v1/companies/field` request with
`field=social` now adds a `value.linkedin` block. No all-fields company response
was introduced. The compact company endpoint reads only existence when checking
this field's availability.

| Source | Selected public data | Selection rule |
|---|---|---|
| Company record | Recorded platform links | Existing exact-domain/public-company-ID resolution |
| `linkedin_profile_logs` | Latest profile, follower/headcount snapshots, size, observed page-card counters and dates | Exact domain; deduplicate identical observations; newest snapshots first |
| `social_media_posts` | Post ID, URLs, text, author, media, hashtags, counters and dates | LinkedIn plus exact domain; latest fetched tuple per post ID; publication time descending, unknown dates last |
| Existing social enrichment | Derived benchmark fields when present | Retained separately from dated profile observations |

Source queries are fixed and parameterized, use read-only mode and resource
ceilings, and return no caller-specified fields or SQL. Operator credentials are
supplied through blank-by-default private runtime settings. Authentication and
the existing company scope, rate/concurrency limits and metering still apply.

## Live gateway results after correction

| Company | Profile snapshots | Distinct stored posts | Complete selected-field capture |
|---|---:|---:|---|
| Razorpay | 1 | 8 | [JSON](../examples/fields/razorpay.com-social.json) |
| Stripe | 1 | 4 | [JSON](../examples/fields/stripe.com-social.json) |
| Swiggy | 1 | 9 | [JSON](../examples/fields/swiggy.com-social.json) |

These are authenticated local gateway reads of existing stores, not deployment
or live LinkedIn scraping. Every returned post is retained in the saved examples.
See the [structured evidence](linkedin-social-evidence.json) for request/status
fingerprints and the [LinkedIn workflow](../guides/linkedin-social-data-api.md) for
the complete Razorpay response.

## Interpretation and remaining boundaries

- Publication, profile observation, company update and gateway retrieval dates
  are distinct. July observations do not become September observations on retrieval.
- Observed employee counts are platform headcount, not audited payroll. One
  stored profile point does not establish a growth trend.
- Source sector `HRTech` conflicts with Razorpay's company classification; it is
  preserved as `recorded_sector` rather than promoted to an authoritative sector.
- Counter values use the latest post crawl. They are not summed across duplicate
  observations. Negative sentinels become null; source zeros can include parser defaults.
- Unknown publication dates remain null. Missing titles remain empty even when
  a post has text. Page-card engagement totals are not lifetime totals.
- Each list is bounded by `item_limit` (maximum 100), with source counts and
  truncation. There is no offset/full-archive export in this field contract.
- Query failure returns null plus `unavailable`; an unconfigured reader is
  `not_configured`. Existing links remain accessible with partial coverage.
- Company posts do not add person-post search, comment threads, a reverse-URL
  resolver, contact reveal or social messaging.

## Reproduce

With the existing preview key and the two operator read connections configured,
run `python scripts/capture_company_social.py`, then
`python scripts/build_endpoint_docs.py` and `python scripts/check_docs.py`.
Refresh this dated evidence assessment if source rows change. The capture script
writes raw originals under ignored `qa/private/`; the documentation generator
preserves response hashes and complete business arrays in the public-ready files.
