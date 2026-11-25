# LinkedIn data depth: why the social example originally contained only links

Investigated and corrected on **2026-09-23** after the Razorpay social example
omitted followers, employee counts and posts that existed in the source store.

## Root cause

## Corrected request and source mapping

The existing `get_company_field` / `POST /v1/companies/field` request with
`field=social` now adds a `value.linkedin` block. No all-fields company response
was introduced. The compact company endpoint reads only existence when checking
this field's availability.

| Source | Selected public data | Selection rule |
|---|---|---|
| Company record | Recorded platform links | Existing exact-domain/public-company-ID resolution |
| Existing social enrichment | Derived benchmark fields when present | Retained separately from dated profile observations |

## Live Companies Radar API results after correction

| Company | Profile snapshots | Distinct stored posts | Complete selected-field capture |
|---|---:|---:|---|
| Razorpay | 1 | 8 | [JSON](../examples/fields/razorpay.com-social.json) |
| Stripe | 1 | 4 | [JSON](../examples/fields/stripe.com-social.json) |
| Swiggy | 1 | 9 | [JSON](../examples/fields/swiggy.com-social.json) |

These are Companies Radar API reads of existing stores, not deployment
or live LinkedIn scraping. Every returned post is retained in the saved examples.
See the [structured evidence](linkedin-social-evidence.json) for request/status
fingerprints and the [LinkedIn workflow](../guides/linkedin-social-data-api.md) for
the complete Razorpay response.

## Interpretation and remaining boundaries

- Publication, profile observation, company update and Companies Radar API retrieval dates
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