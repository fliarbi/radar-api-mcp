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

<!-- captured-workflow -->
## Choose peers before comparing financial and derived evidence

Competitor discovery accepts a market label, not a company domain. Start by deciding
what the firms compete to supply, which buyers they serve and which geography
matters. A broad Software label returned an empty grouping in the captured query.
That is a signal to review the classification and query specificity, not a factual
finding that the company has no competitors.

After reviewing candidate companies, pass two to five distinct domains to
`compare_companies`. Each company has separate profile, financial and intelligence
sections. Display a revenue value with its fiscal period and source type; display
an intelligence score with its derived label and computation date. The API does not
convert those different quantities into a single investment ranking.

The captured Microsoft/Salesforce comparison returned both companies' research
sections, but corporate identity and fiscal alignment still require review. A
missing metric should remain unknown even if the other company supplies it.
If one section fails, keep the successful peer's evidence visible and label the
gap. Account mode reserves three credits per requested company and refunds failed
sections, so the final billing metadata is the appropriate source for actual
charged usage rather than multiplying every partial section as a success.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/competitors`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: find_competitors -->
```json
{
  "market": "Software",
  "per_stage": 3
}
```

<!-- response-example: find_competitors -->
```json
{
  "ok": true,
  "feature": "find_competitors",
  "data": {
    "market": "Software",
    "companies": {
      "Public": [],
      "Seed": [],
      "Series A": [],
      "Series B": [],
      "Series C": []
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:46.274343+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/find_competitors.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The broad Software query returned HTTP 200 with an empty companies dictionary. That is a real empty discovery result, not a successful list of zero competitors in the economy. A more specific recognized market label may be needed.

See the [complete find_competitors endpoint reference](../reference/find_competitors.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
