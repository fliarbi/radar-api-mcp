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

<!-- captured-workflow -->
## Map enrichment into a CRM without losing provenance

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

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/enrichment`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_company_enrichment -->
```json
{
  "domain": "microsoft.com"
}
```

<!-- response-example: get_company_enrichment -->
```json
{
  "ok": true,
  "feature": "get_company_enrichment",
  "data": {
    "digital": {
      "authority": 100,
      "global_rank": 26,
      "visits": 1222875095,
      "visits_date": "2026-05-01"
    },
    "domain": "microsoft.com",
    "has_data": true,
    "legal": [
      {
        "country": "United States",
        "id_no": "2357303",
        "legal_name": "Microsoft Corporation",
        "registry": "Others"
      },
      {
        "country": "Latvia",
        "id_no": "40203171831",
        "legal_name": "BI Partners",
        "registry": "ur.gov.lv"
      }
    ],
    "reputation": {
      "category": "Electronics & Technology",
      "n": 3789,
      "n_12m": 1062,
      "score": 1.2,
      "stars": 1
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:46.234462+00:00",
    "partial": false,
    "notes": [
      "Absent enrichment sections have unknown coverage; the source does not distinguish missing data from a failed section."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_enrichment.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The Microsoft capture returned a Microsoft Corporation legal record and digital observations dated in May 2026. That legal name differed from the product label in the profile example. Reputation text and individual reviews are deliberately omitted from the documentation excerpt; aggregate fields remain captured values.

See the [complete get_company_enrichment endpoint reference](../reference/get_company_enrichment.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
