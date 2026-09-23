# Company data API: business profiles and company lookup by domain

A company data API turns a business identifier into a structured company record.
Radar uses the company's website domain as the identifier for profile, financial,
funding, event and enrichment requests. This makes it possible to connect different
types of companies data without matching free-text names repeatedly.

Use this guide when building an account detail page, adding business information
to an internal research application, or resolving a company before requesting
deeper financial or news context.

## Retrieve compact identity and available fields

Set `RADAR_API_URL` to your operator-supplied private base URL and keep your key in
`RADAR_API_KEY`. The base URL should not end in a slash.

```bash
curl "$RADAR_API_URL/v1/companies/profile" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"razorpay.com"}'
```

With the detailed connection enabled, the response lists eighteen available-field
statuses. Request one field separately with `get_company_field`. See the [full company field dictionary](../COMPANY_DATA_DEPTH.md) for
sectors, feeds, founders, technology, traffic, apps, hiring and innovation.

The MCP equivalent is `get_company` with
`{"request":{"domain":"razorpay.com"}}`. Company cards can include the name,
domain and short description. Rich field values require a separate JSON POST;
email and phone values require the [contact workflow](../CONTACTS.md).

If you only know a company name, use [company search](company-search-api.md) first.
Inspect the returned domain and business description before selecting a match:
subsidiaries, similarly named businesses and different country operations may
refer to different entities.

## Normalize identifiers before joining records

Submit `razorpay.com`, not a full URL, IP address, port or path. Domains are
lowercased and a leading `www.` is removed. Keep the normalized domain alongside
your internal account ID. A website domain is a useful lookup key, but it is not
a legal-entity identifier or a guarantee that a group has one reporting entity.

When you need legal identity or digital-presence details, request
`get_company_enrichment`. For financial metrics, use `get_financials` and retain
its fiscal-period labels. A profile field and a financial statement metric may
have different update dates and should not be merged without context.

## Empty results and access limits

An absent company or an empty attribute does not establish that a business is
inactive. Treat it as missing API coverage. Check `ok`, the response `data`,
`meta.partial`, and any access information. A `403` concerns linked-account access;
a `503` concerns service availability. Neither should become a blank company
record that overwrites information you already hold.

Related: [B2B data workflows](b2b-data-api.md), [company enrichment](company-enrichment-api.md),
[financial data](financial-data-api.md), [API authentication](api-keys-authentication.md).

## Company contacts, founder details and social references

The profile's contact flags describe stored availability, not values or entitlement.
Use [company email and phone retrieval](company-email-phone-api.md) for explicitly
selected contact strings and [LinkedIn/social fields](linkedin-social-data-api.md)
for company page references. Founder names must be resolved to accepted professional
IDs before a person contact lookup; the [founder workflow](founder-contact-data-api.md)
shows actual positive, empty and conflicting discovery results.

<!-- captured-workflow -->
## Resolve the company before attaching financial history

The worked example uses Razorpay's compact identity and available-field metadata.
Request sectors, feeds, founders, technology, traffic or apps separately through
`get_company_field` with a required field selector. Each returned value has its own
coverage; the profile and brief no longer embed all rich sections at once.
The [company field guide](../COMPANY_DATA_DEPTH.md) links every separately captured
field for Razorpay, Stripe and Swiggy.

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

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/profile`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_company -->
```json
{
  "domain": "razorpay.com"
}
```

<!-- response-example: get_company -->
```json
{
  "ok": true,
  "feature": "get_company",
  "data": {
    "company": {
      "company_id": "2gowls1wmc",
      "domain": "razorpay.com",
      "name": "Razorpay",
      "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=razorpay.com",
      "description": "Provider of payment and business banking solutions for enterprises",
      "founded": 2014,
      "employee_count": 1952
    },
    "profile_depth": "summary",
    "available_fields": [
      "overview",
      "classification",
      "people",
      "technology",
      "web_presence",
      "traffic",
      "apps",
      "products",
      "geography",
      "social",
      "lifecycle",
      "legal",
      "assessments",
      "hiring",
      "reputation",
      "share_of_voice"
    ],
    "field_status": {
      "overview": "available",
      "classification": "available",
      "people": "available",
      "technology": "available",
      "web_presence": "available",
      "traffic": "available",
      "apps": "available",
      "products": "available",
      "geography": "available",
      "social": "available",
      "lifecycle": "available",
      "legal": "available",
      "assessments": "available",
      "hiring": "available",
      "innovation": "not_observed",
      "activity": "not_observed",
      "reputation": "available",
      "share_of_voice": "available"
    },
    "contacts": {
      "availability": {
        "emails": true,
        "phones": true
      },
      "path": "/v1/contacts/company",
      "required_scope": "contacts",
      "access": "linked Radar paid-plan check"
    },
    "field_request": {
      "method": "POST",
      "path": "/v1/companies/field",
      "required": [
        "domain",
        "field"
      ]
    },
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "partial": false
    },
    "financial_history": "Use get_financials; financial archive and estimated-revenue access remain upstream-controlled"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:27.254901+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:27.255033+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live Razorpay response contains compact identity and available-field metadata. Its richer classification, founders, seventy technology entries, traffic and app observations are captured through separate field requests in COMPANY_DATA_DEPTH.md. The profile no longer embeds them.

See the [complete get_company endpoint reference](../reference/get_company.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
