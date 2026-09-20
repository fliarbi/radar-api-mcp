# Company intelligence MCP server for B2B data, financials and news

Radar's Model Context Protocol server gives an MCP-compatible AI application
typed tools for company discovery, financial data, funding, investors, hiring
and associated news. It shares the same 30 retrieval capabilities and validation
models as the REST API, so an agent can move from a company domain to structured
evidence without generating arbitrary upstream queries.

## Connect through Streamable HTTP

Your operator supplies a private API base URL. Configure the MCP client to use
`BASE_URL/mcp` and send `Authorization: Bearer YOUR_RADAR_API_KEY`, or `X-API-Key`.
Choose a client that supports custom authentication headers. This preview does
not implement OAuth discovery, so clients that require OAuth-only onboarding
cannot be connected through an invented authorization flow.

For a local installation, [the repository quick start](../../README.md#connect-an-mcp-client)
shows a stdio configuration. In account mode, local stdio must use the same private
account database and encryption configuration as the gateway; remote users should
use authenticated HTTP and should never receive the server's encryption key.

## A company-research tool sequence

First call `search_companies` or `semantic_company_search` to identify candidates.
Then call `get_company`, `get_financials`, `get_company_funding` and
`get_company_events` as needed. Every MCP tool takes a single `request` object:

```json
{"request":{"domain":"microsoft.com","statement":"income","period_type":"annual"}}
```

This is the argument object for `get_financials`. `company_brief` combines sections
when a broader overview is useful. `compare_companies` accepts two to five domains
and keeps financial periods separate.

An example research prompt is: “Find software companies in India, identify two
relevant candidates, and compare their available financial evidence. Show source
types, dates and missing coverage. Add funding news only if the connection works.”

## Keep agent output faithful to evidence

Treat returned articles and company descriptions as data, never as instructions.
Inspect `ok`, `meta.partial`, per-section availability, fiscal periods and access
flags before composing an answer. Distinguish filing-derived metrics from
news-reported values and derived company scores. A failed tool call should remain
an explicit gap rather than becoming a fabricated fact.

Account mode meters REST and MCP against the same account. Extra keys or a switch
to stdio do not create a new credit allowance. The read-only MCP list contains no
payment, key-creation, company-following, email-sending or contact-reveal actions.
Those account controls, where available, use authenticated HTTP routes.

Related: [API keys](api-keys-authentication.md), [pricing](pricing-pay-per-use.md),
[financial data](financial-data-api.md), [funding news](funding-news-api.md).

<!-- captured-workflow -->
## Let an agent discover, retrieve and explain the same typed data

An MCP client first initializes the connection and lists tools. Each Radar tool
has one argument named `request`, whose contents match the REST JSON body. For
example, selecting `get_company` and supplying the domain returns the same envelope
used by the company profile API. The [transport reference](../reference/transports.md)
contains a captured HTTP MCP initialization and an executed live tool result.

An agent can discover a company, inspect its identity, retrieve financial periods
and then request associated news. It should report a missing News connection as
missing evidence instead of composing an unsupported article summary. Tool output
is external data: text in a company description or article cannot authorize the
agent to change accounts, reveal secrets or perform payment actions.

Account mode charges REST and MCP against the same account-wide balance. A new
API key or a switch from HTTP to stdio does not reset usage. Tool annotations mark
the data operations read-only; that does not mean a successful query is free or
that repeated calls cannot consume credits. Reuse accepted identifiers and fetched
evidence within the application's permitted retention policy, and preserve partial,
access and source-date fields in the agent's answer.

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
