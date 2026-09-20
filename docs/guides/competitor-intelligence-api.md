# Competitor intelligence API and company financial comparisons

Radar offers market-based competitor discovery and a separate company comparison
operation. Use competitor discovery to find candidates in a named market; use
comparison to review selected companies' profiles, financial evidence and derived
intelligence. Keeping these stages separate helps avoid treating an automatically
returned peer as a proven direct competitor.

## Discover peers in a market

`find_competitors` maps to `POST /v1/companies/competitors`:

```json
{"market":"Software","per_stage":5}
```

An optional `business_model` can narrow the query. Results are grouped by funding
stage; `per_stage` accepts 3 through 10. Start with a specific market label from
industry discovery when possible. Review each candidate's description, location
and product context before including it in an analysis.

## Compare selected companies

`compare_companies` maps to `POST /v1/companies/compare`:

```json
{"domains":["microsoft.com","salesforce.com"]}
```

The example demonstrates the input shape, not a claim that every line of business
is comparable. Supply two to five distinct domains. The response keeps each
company's profile, financials and intelligence in separate sections, with missing
coverage and section failures explicitly indicated.

In account mode, the gateway reserves three credits per company and refunds
failed sections. It does not calculate a cross-company total, rank investments
or normalize every company's fiscal calendar into a common reporting period.

## Read financial and intelligence sections differently

Financial metrics retain source types and currency information. Company scores,
risk narratives and other intelligence are derived assessments. Do not present
a score as a filed financial fact, and do not compare two fiscal-year labels
without inspecting the underlying dates and available coverage.

If one company's financial section is unavailable, preserve that gap in your
comparison table. Substituting zero would falsely imply a measured value and can
distort growth or margin calculations. Retrieve associated company events and
news separately when they help explain a difference.

## Useful applications

This workflow can support a business-development shortlist, a product-market
landscape review or an internal research brief. It does not replace source review
or establish that the returned list contains every relevant competitor.

Related: [company search](company-search-api.md), [financial data](financial-data-api.md),
[financial statements](company-financial-statements-api.md), [company monitoring](company-monitoring-api.md).
