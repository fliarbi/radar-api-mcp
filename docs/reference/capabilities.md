# Capability discovery: tools, routes and input schemas

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

Lists the shared data-operation registry. Use it to discover the exact tool name, REST route and accepted input model instead of building arbitrary upstream calls.

## Method and authentication

**`GET /v1/capabilities`**

Use a data API key in `Authorization: Bearer`. Discovery does not reserve data-operation credits. Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

This request has no JSON body.

```bash
curl --fail-with-body -X GET "$RADAR_API_URL/v1/capabilities" \
  -H "Authorization: Bearer $RADAR_API_KEY"
```

Set the private base URL without a trailing slash. Example IDs identify the
temporary documentation account; use your own returned identifiers when integrating.
Do not paste the redacted credential placeholders into a running application.

## Executed local output

**Provenance: real gateway code and a temporary SQLite account store, with a
synthetic verified Radar identity and synthetic Razorpay provider responses.**
No live user was created, payment collected or production account changed.
The synthetic Business plan and ten-paise credit price exercise the flow;
they do not announce an enabled checkout or an approved pay-per-use tariff.

<!-- response-example: capabilities -->
```json
{
  "ok": true,
  "feature": "capabilities",
  "data": {
    "features": [
      {
        "name": "search_companies",
        "method": "POST",
        "path": "/v1/companies/search",
        "description": "Filter companies by industry, market, location, size, stage, technology, funding and financial bands.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "semantic_company_search",
        "method": "POST",
        "path": "/v1/companies/semantic-search",
        "description": "Find companies using a natural-language description plus optional filters.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_company",
        "method": "POST",
        "path": "/v1/companies/profile",
        "description": "Read compact company identity and available fields. Retrieve field data separately with get_company_field.",
        "read_only": true,
        "detailed_profile_configured": false,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_company_field",
        "method": "POST",
        "path": "/v1/companies/field",
        "description": "Retrieve one explicitly selected company field, such as classification, people, technology, traffic or apps, with coverage and bounded arrays.",
        "read_only": true,
        "detailed_profile_configured": false,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "company_apps",
        "method": "POST",
        "path": "/v1/companies/apps",
        "description": "List individual Play Store apps whose normalized developer website exactly matches the company domain.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "opportunity_presets",
        "method": "POST",
        "path": "/v1/companies/opportunities/presets",
        "description": "Discover explainable growth, hiring, financial and technology prospecting screens and their limits.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "search_opportunities",
        "method": "POST",
        "path": "/v1/companies/opportunities/search",
        "description": "Find companies using an explicit opportunity preset plus additional filters; return measured display evidence and source restrictions.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "company_filter_catalog",
        "method": "POST",
        "path": "/v1/companies/filters",
        "description": "Discover company filters, accepted values, sort options, pagination and selectable result columns.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "company_filter_options",
        "method": "POST",
        "path": "/v1/companies/filter-options",
        "description": "Look up matching company filter values using Radar's sidebar vocabulary and typeahead services.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_company_columns",
        "method": "POST",
        "path": "/v1/companies/columns",
        "description": "Fetch only selected display columns for up to twenty company domains. Formatted values are not financial statements.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_company_intelligence",
        "method": "POST",
        "path": "/v1/companies/intelligence",
        "description": "Read company scores, peer comparisons, earnings and risk narratives. Scores are derived assessments, not financial facts.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_financials",
        "method": "POST",
        "path": "/v1/companies/financials",
        "description": "Retrieve income, balance-sheet and cash-flow metrics by fiscal period; distinguish filings from news reports and preserve currency and access limits.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_company_events",
        "method": "POST",
        "path": "/v1/companies/events",
        "description": "Read a company's event timeline, momentum, risks and the effective account-limited date window.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_company_funding",
        "method": "POST",
        "path": "/v1/companies/funding",
        "description": "Read reported funding rounds and investors; retain approximate-amount flags.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_company_enrichment",
        "method": "POST",
        "path": "/v1/companies/enrichment",
        "description": "Read legal identity, hiring, reputation, digital presence, innovation and social activity when available.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "find_competitors",
        "method": "POST",
        "path": "/v1/companies/competitors",
        "description": "Find competitors in a named market, grouped by funding stage.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "company_brief",
        "method": "POST",
        "path": "/v1/companies/brief",
        "description": "Return compact summaries of profile, financials, intelligence, events, funding, enrichment and news with separate detail requests and explicit coverage.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "compare_companies",
        "method": "POST",
        "path": "/v1/companies/compare",
        "description": "Compare two to five companies with separately labelled fiscal periods and partial-coverage flags.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "search_investors",
        "method": "POST",
        "path": "/v1/investors/search",
        "description": "Find investors by headquarters and portfolio industries or markets.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "investor_directory",
        "method": "POST",
        "path": "/v1/investors/directory",
        "description": "List published investor pages, sectors and cities.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_investor_page",
        "method": "POST",
        "path": "/v1/investors/page",
        "description": "Read investor identity, measured portfolio metrics, dated coverage and available detail fields by published slug.",
        "read_only": true,
        "detailed_investor_configured": false,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_investor_field",
        "method": "POST",
        "path": "/v1/investors/field",
        "description": "Retrieve one investor field: paginated portfolio or shortlist, sector/stage analysis, follow-on cohorts, co-investors or sourced news.",
        "read_only": true,
        "detailed_investor_configured": false,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "market_pulse",
        "method": "POST",
        "path": "/v1/markets/pulse",
        "description": "Read recent funding, trending markets, sectors and investors for a bounded window.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "location_intelligence",
        "method": "POST",
        "path": "/v1/locations/intelligence",
        "description": "Retrieve Radar's existing business intelligence for a named location.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "discover_industries",
        "method": "POST",
        "path": "/v1/industries/discover",
        "description": "Find up to five matching industry or market names using a specific query.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "search_jobs",
        "method": "POST",
        "path": "/v1/jobs/search",
        "description": "Find job listings by company, skills, role, geography and freshness.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "job_filter_catalog",
        "method": "POST",
        "path": "/v1/jobs/filters",
        "description": "Discover job filters, source values, sorting and source matching semantics.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "job_filter_options",
        "method": "POST",
        "path": "/v1/jobs/filter-options",
        "description": "Suggest observed job titles, skills, employer names or locations.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "search_internships",
        "method": "POST",
        "path": "/v1/jobs/internships/search",
        "description": "Search dedicated internship records by employer, title, location, skills, stipend and posted dates; preserve vacancy-status uncertainty.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "companies_offering_internships",
        "method": "POST",
        "path": "/v1/jobs/internships/companies",
        "description": "Group matching observed internship listings by exact employer name, with counts, titles and detail IDs.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "get_internship",
        "method": "POST",
        "path": "/v1/jobs/internships/detail",
        "description": "Retrieve a source internship with description, stipend, skills, dates, application URL and validity qualifications.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "companies_hiring",
        "method": "POST",
        "path": "/v1/jobs/companies",
        "description": "Find hiring companies for the same job filters.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_job",
        "method": "POST",
        "path": "/v1/jobs/detail",
        "description": "Retrieve a job listing by an ID returned by search_jobs.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "salary_benchmark",
        "method": "POST",
        "path": "/v1/jobs/salary-benchmark",
        "description": "Read salary statistics for a role, geography and optional currency; retain sample size and coverage.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "search_apps",
        "method": "POST",
        "path": "/v1/apps/search",
        "description": "Search individual Android apps by name, developer, exact website host, category, installs, ratings and price model.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "get_app",
        "method": "POST",
        "path": "/v1/apps/profile",
        "description": "Read compact app identity, observed installs and rating, detail availability and history count.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "get_app_field",
        "method": "POST",
        "path": "/v1/apps/field",
        "description": "Retrieve one app field: listing, ratings, monetization, release, developer, growth or paginated install history.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "app_filter_options",
        "method": "POST",
        "path": "/v1/apps/filter-options",
        "description": "List matching observed Play Store categories for app discovery.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "search_people",
        "method": "POST",
        "path": "/v1/people/search",
        "description": "Find professional profiles by name, role, company, schools, skills, seniority and location; contact values require a separate request.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "people_filter_options",
        "method": "POST",
        "path": "/v1/people/filter-options",
        "description": "Look up canonical schools, skills and sectors accepted by people search.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": true
      },
      {
        "name": "get_company_contacts",
        "method": "POST",
        "path": "/v1/contacts/company",
        "description": "Request company emails and/or phones separately; requires explicit contacts scope and a paid linked Radar account.",
        "read_only": true,
        "requires_explicit_scope": "contacts",
        "connection_configured": true
      },
      {
        "name": "get_person_contacts",
        "method": "POST",
        "path": "/v1/contacts/person",
        "description": "Request one person's emails and/or phones; preserve whether the source is the person or a company-domain fallback. Requires contacts scope and paid Radar access.",
        "read_only": true,
        "requires_explicit_scope": "contacts",
        "connection_configured": true
      },
      {
        "name": "search_news",
        "method": "POST",
        "path": "/v1/news/search",
        "description": "Search associated news; a company filter uses business-news coverage. Headlines default to 100 per page.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "search_business_news",
        "method": "POST",
        "path": "/v1/news/business",
        "description": "Search business headlines for a topic or company with date, sentiment and priority filters.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "news_overview",
        "method": "POST",
        "path": "/v1/news/overview",
        "description": "Read measured coverage, headline examples and topic context in a bounded date window.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "news_trends",
        "method": "POST",
        "path": "/v1/news/trends",
        "description": "Measure daily, weekly or monthly news volume while preserving the available date window.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "news_sentiment",
        "method": "POST",
        "path": "/v1/news/sentiment",
        "description": "Read the distribution and timeline of news sentiment.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "search_business_events",
        "method": "POST",
        "path": "/v1/news/events",
        "description": "Read structured business events associated with a topic or company and their article references.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "search_funding_news",
        "method": "POST",
        "path": "/v1/news/funding",
        "description": "Find funding coverage by company, topic, investor, sector, round and reported USD amount.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      },
      {
        "name": "get_article",
        "method": "POST",
        "path": "/v1/news/article",
        "description": "Retrieve the full article and attribution for an article ID returned by news or company events.",
        "read_only": true,
        "requires_explicit_scope": null,
        "connection_configured": false
      }
    ]
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T10:43:29.894640+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI",
    "coverage": null,
    "plan": null,
    "quota": null,
    "billing": null
  },
  "error": null
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-21T10:43:29.427936+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/capabilities.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

## What this response means

connection_configured means configuration is present for the caller, not that the service is healthy or that every query is entitled. The response shows all 50 tools, omitting only their lengthy embedded input schemas; the complete schemas remain in OpenAPI.

The capture sequence connected a session, inspected plans, created and listed a
key, linked a placeholder News key, followed one domain, set a spending limit,
created a synthetic order, delivered its signed captured event, inspected usage,
then unfollowed the domain and revoked the key. Responses reflect that order.

Handle `401` by reconnecting an authorized session, `403` by checking plan/access,
and `429` with backoff and the supplied retry interval. Do not automate repeating
checkout requests after an ambiguous network failure: first inspect the provider
order and reconcile its captured status. Key creation reveals a credential once;
key listing is metadata-only. See the [account controls](../ACCOUNTS.md) for
creation caps, shared limits, spending reservations and payment reversal behavior.

Related: [API-key onboarding](../guides/api-keys-authentication.md),
[plans and pay-per-use](../guides/pricing-pay-per-use.md),
[full account schema](../account-openapi.json).
