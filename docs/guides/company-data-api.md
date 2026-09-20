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

<!-- captured-workflow -->
## Resolve the company before attaching financial history

The sample below is deliberately revealing: `microsoft.com` matched a profile
called Microsoft Dynamics CRM. A separate enrichment response included a Microsoft
Corporation legal record and also a second legal entry whose association requires
review. Domain matching alone therefore does not settle which legal entity a
record describes. Preserve the original response label and record your own identity
decision explicitly rather than silently correcting the API output.

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
  "domain": "microsoft.com"
}
```

<!-- response-example: get_company -->
```json
{
  "ok": true,
  "feature": "get_company",
  "data": {
    "company": {
      "location": {
        "c": "united states",
        "cc": "",
        "coord": [
          -122.12151,
          47.67399
        ],
        "g": "47.67399,-122.12151",
        "hq": "redmond",
        "l": "redmond",
        "lc": "redmond, washington, united states",
        "rg": "washington"
      },
      "size": "",
      "founded": "2003",
      "company_id": "58edbbfde4b053044e6a387d",
      "name": "Microsoft Dynamics CRM",
      "domain": "microsoft.com"
    },
    "access": {
      "anonymous": true,
      "plan": "free",
      "results_per_query": 50,
      "searches_per_month": 50
    },
    "extras_gated": true
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:45.936850+00:00",
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
The [downloadable JSON example](../examples/get_company.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The microsoft.com request returned the label Microsoft Dynamics CRM, rather than a normalized Microsoft Corporation parent profile. This is an observed identity ambiguity, not a spelling correction made for the example. The accompanying enrichment endpoint returned a Microsoft Corporation legal record. Review such disagreements before joining a corporate group, product profile and filing series.

See the [complete get_company endpoint reference](../reference/get_company.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
