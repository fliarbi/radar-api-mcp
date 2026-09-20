# Company data API: business profiles and company lookup by domain

A company data API turns a business identifier into a structured company record.
Radar uses the company's website domain as the identifier for profile, financial,
funding, event and enrichment requests. This makes it possible to connect different
types of companies data without matching free-text names repeatedly.

Use this guide when building an account detail page, adding business information
to an internal research application, or resolving a company before requesting
deeper financial or news context.

## Retrieve a company profile

Set `RADAR_API_URL` to your operator-supplied private base URL and keep your key in
`RADAR_API_KEY`. The base URL should not end in a slash.

```bash
curl "$RADAR_API_URL/v1/companies/profile" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com"}'
```

The MCP equivalent is `get_company` with
`{"request":{"domain":"microsoft.com"}}`. Company cards can include the name,
domain, description and additional business attributes supplied by Radar. Missing
fields are not invented, and private contact-reveal fields are excluded.

If you only know a company name, use [company search](company-search-api.md) first.
Inspect the returned domain and business description before selecting a match:
subsidiaries, similarly named businesses and different country operations may
refer to different entities.

## Normalize identifiers before joining records

Submit `microsoft.com`, not a full URL, IP address, port or path. Domains are
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
