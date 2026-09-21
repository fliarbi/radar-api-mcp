# Company data fields: sectors, feeds, founders, technology, traffic and apps

Start with a compact company profile. It returns identity, a short description,
founding year, employee count, a Radar image URL and the names of available fields.
Rich values require a separate JSON POST selecting one field. Availability checks
do not return email addresses, phone numbers, technology arrays or founder records.

## 1. Discover the company and its available fields

```json
{"domain": "razorpay.com"}
```

Send this to `POST /v1/companies/profile`, or MCP `get_company`. Read
`available_fields`, `field_status` and `contacts.availability`. These report stored
coverage. They do not promise current accuracy, email deliverability or paid access.
An unconnected field store returns `profile_depth=card` and unavailable field status.
The normal connected response is `profile_depth=summary`.

## 2. Retrieve one field

```json
{"domain": "razorpay.com", "field": "technology", "item_limit": 100}
```

Send this to `POST /v1/companies/field`, or MCP `get_company_field`. Only `value`
contains the requested field. `item_limit` defaults to 50 and is capped at 100 per
array. Every array reports available/returned/truncated counts in `coverage.arrays`.
No all-fields selector exists. The old `sections` and `item_limit` parameters on
`get_company` are rejected with HTTP 422; move those detail reads to the field endpoint.
Each successful field request costs one operation credit in account mode.

## Real, separate captures

The following JSON files come from authenticated local gateway calls against the
live company store on 2026-09-21. Each includes its request, response, timestamp,
checksums and explicit documentation omission paths. The values are source
observations; they have not been independently verified as current facts.

| Compact company | Available detail fields | Summary JSON |
|---|---:|---|
| Razorpay | 17 | [razorpay.com](examples/profiles/razorpay.com.json) |
| Stripe | 18 | [stripe.com](examples/profiles/stripe.com.json) |
| Swiggy | 17 | [swiggy.com](examples/profiles/swiggy.com.json) |

| Field request | Razorpay | Stripe | Swiggy |
|---|---|---|---|
| `overview` | [JSON](examples/fields/razorpay.com-overview.json) | [JSON](examples/fields/stripe.com-overview.json) | [JSON](examples/fields/swiggy.com-overview.json) |
| `classification` | [JSON](examples/fields/razorpay.com-classification.json) | [JSON](examples/fields/stripe.com-classification.json) | [JSON](examples/fields/swiggy.com-classification.json) |
| `people` | [JSON](examples/fields/razorpay.com-people.json) | [JSON](examples/fields/stripe.com-people.json) | [JSON](examples/fields/swiggy.com-people.json) |
| `technology` | [JSON](examples/fields/razorpay.com-technology.json) | [JSON](examples/fields/stripe.com-technology.json) | [JSON](examples/fields/swiggy.com-technology.json) |
| `web_presence` | [JSON](examples/fields/razorpay.com-web_presence.json) | [JSON](examples/fields/stripe.com-web_presence.json) | [JSON](examples/fields/swiggy.com-web_presence.json) |
| `traffic` | [JSON](examples/fields/razorpay.com-traffic.json) | [JSON](examples/fields/stripe.com-traffic.json) | [JSON](examples/fields/swiggy.com-traffic.json) |
| `apps` | [JSON](examples/fields/razorpay.com-apps.json) | [JSON](examples/fields/stripe.com-apps.json) | [JSON](examples/fields/swiggy.com-apps.json) |
| `products` | [JSON](examples/fields/razorpay.com-products.json) | [JSON](examples/fields/stripe.com-products.json) | [JSON](examples/fields/swiggy.com-products.json) |
| `geography` | [JSON](examples/fields/razorpay.com-geography.json) | [JSON](examples/fields/stripe.com-geography.json) | [JSON](examples/fields/swiggy.com-geography.json) |
| `social` | [JSON](examples/fields/razorpay.com-social.json) | [JSON](examples/fields/stripe.com-social.json) | [JSON](examples/fields/swiggy.com-social.json) |
| `lifecycle` | [JSON](examples/fields/razorpay.com-lifecycle.json) | [JSON](examples/fields/stripe.com-lifecycle.json) | [JSON](examples/fields/swiggy.com-lifecycle.json) |
| `legal` | [JSON](examples/fields/razorpay.com-legal.json) | [JSON](examples/fields/stripe.com-legal.json) | [JSON](examples/fields/swiggy.com-legal.json) |
| `assessments` | [JSON](examples/fields/razorpay.com-assessments.json) | [JSON](examples/fields/stripe.com-assessments.json) | [JSON](examples/fields/swiggy.com-assessments.json) |
| `hiring` | [JSON](examples/fields/razorpay.com-hiring.json) | [JSON](examples/fields/stripe.com-hiring.json) | [JSON](examples/fields/swiggy.com-hiring.json) |
| `innovation` | [JSON](examples/fields/razorpay.com-innovation.json) | [JSON](examples/fields/stripe.com-innovation.json) | [JSON](examples/fields/swiggy.com-innovation.json) |
| `activity` | [JSON](examples/fields/razorpay.com-activity.json) | [JSON](examples/fields/stripe.com-activity.json) | [JSON](examples/fields/swiggy.com-activity.json) |
| `reputation` | [JSON](examples/fields/razorpay.com-reputation.json) | [JSON](examples/fields/stripe.com-reputation.json) | [JSON](examples/fields/swiggy.com-reputation.json) |
| `share_of_voice` | [JSON](examples/fields/razorpay.com-share_of_voice.json) | [JSON](examples/fields/stripe.com-share_of_voice.json) | [JSON](examples/fields/swiggy.com-share_of_voice.json) |

## What the fields mean

- `overview`: alternate names, other domains and the longer description.
- `classification`: sectors, primary and other feeds, industries, business/revenue models and source flags.
- `people`: named key people and founders selected by the source designation. These are professional records; contact values require their own endpoint.
- `technology` and `web_presence`: merged stack, observed technologies and crawl dates versus web performance, SEO and derived digital scores.
- `traffic`: visits, observation date, country shares, keywords and engagement. Visits are not unique customers, and fractions remain fractions.
- `apps`: aggregate app count, downloads and rating. This is not an app roster; downloads are not monthly active users.
- `products`, `geography`, `social`, `lifecycle`, `legal`, `assessments`: separately requested business context. Scores are derived assessments; legal associations may need review.
- `hiring`, `innovation`, `activity`, `reputation`, `share_of_voice`: separate enrichment observations with source coverage and date limitations.

`available` means the field was observed, including an empty list or numeric zero.
`not_observed` means no stored observation; `unavailable` means the store failed;
`partial` and array truncation remain explicit. Missing values never become zero.

## Contacts, financials and briefs

Request company emails or phone numbers with `get_company_contacts`; request a
professional's contact using a person ID returned by `search_people` and
`get_person_contacts`. Both require the explicit `contacts` key scope and the
linked Radar account's paid-plan check. Company-domain fallback is labeled and
must not be treated as a verified personal contact. See [contact retrieval](CONTACTS.md).

Financial history remains in `get_financials` with period, currency, source and
access-limit metadata. `company_brief` now returns concise section summaries and
separate detail requests, rather than embedding the complete profile and archives.
The image URL uses Radar's first-party image route; that route can fall back to a
favicon. Stored provider CDN logo URLs are not passed through.

See [profile reference](reference/get_company.md), [field reference](reference/get_company_field.md),
[filters and listings](FILTERS_AND_LISTINGS.md), [source review](RADAR_SOURCE_REVIEW.md)
and [data quality](DATA_QUALITY.md).
