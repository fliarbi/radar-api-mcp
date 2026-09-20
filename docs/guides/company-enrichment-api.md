# Company enrichment API for firmographic and business context

Company enrichment adds information to a company you already know. Radar's
enrichment workflow begins with a website domain and combines a company profile
with available legal, hiring, reputation, digital-presence, innovation and social
activity information. It can support CRM account research or an internal business
intelligence application without creating a new company-discovery workflow.

## Enrich an existing company record

Call `get_company_enrichment` using `POST /v1/companies/enrichment`:

```json
{"domain":"microsoft.com"}
```

Retrieve `get_company` separately when you also need the base company card. The
enrichment endpoint and profile endpoint provide different views; do not assume
that one response is a complete replacement for the other.

For a CRM integration, store the normalized domain, the response retrieval time
and the returned sections together. Map each available value to a specific field
in your own account model. Leave existing values intact when the API returns no
coverage, instead of overwriting them with empty strings or zero.

## Interpret enrichment signals carefully

Hiring activity describes observed job information, not necessarily total
headcount growth. Digital-presence details describe available evidence, not a
guaranteed current technology inventory. Reputation or intelligence narratives
are derived assessments, while legal identifiers and source-backed financial
figures have different meanings and validation needs.

Some upstream enrichment sections do not distinguish absent data from a section
that failed to load. The gateway therefore cannot certify that every omitted
section represents a negative finding. Preserve its coverage notes in a research
view and allow the user to inspect other sources.

## Common implementation questions

**Does enrichment reveal personal emails or phone numbers?** No. The gateway
filters contact-reveal content and exposes no reveal mutation. Professional
search is a separate, bounded capability.

**Can I enrich a list of domains?** Issue individual requests within account rate
and concurrency limits. There is no arbitrary bulk-enrichment or full-database
export endpoint in this preview. `compare_companies` supports two to five domains
for a specific comparison workflow, not unrestricted enrichment batches.

**Does paying for API credits unlock all enrichment?** No. API credits control
gateway usage. The linked Radar account and upstream services still determine
the data and features available to that request.

Continue with [company data](company-data-api.md), [hiring signals](hiring-signals-jobs-api.md),
[company monitoring](company-monitoring-api.md), or [API keys](api-keys-authentication.md).
