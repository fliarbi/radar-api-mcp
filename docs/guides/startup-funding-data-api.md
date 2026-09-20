# Startup funding data API: company funding rounds and investors

Radar's startup funding data API retrieves reported funding rounds for a company
identified by its domain. Use it to add fundraising history to a company profile,
review available investor associations or explore funding activity in a market.
The endpoint represents available reported data; it is not a cap table or a
guarantee that every financing event has been captured.

## Retrieve a company's funding history

`get_company_funding` maps to `POST /v1/companies/funding`:

```json
{"domain":"microsoft.com"}
```

The domain is an input-format example, not a claim that the company is a startup
or that a particular round exists. Use a domain discovered from your own company
search results when researching a startup.

Keep returned round labels, investor names, dates and amount qualifiers together.
If Radar marks an amount as approximate, show that qualifier in the application.
Do not silently turn an undisclosed amount into zero or treat a reported round
amount as a valuation.

## Explore market-level funding context

`market_pulse` (`POST /v1/markets/pulse`) gives a bounded view of recent funding,
markets, sectors and investors:

```json
{"days":30,"limit":5}
```

Use it for discovery and context, then inspect individual companies and funding
evidence. It is not a complete investment-flow accounting dataset, and the number
of returned records should not be presented as all funding in an economy.

## Join structured rounds to funding news

The [funding news API](funding-news-api.md) answers a different question: it finds
articles about fundraising announcements. Retrieve article evidence when available
and licensed through the linked News account. A company can have a structured
funding record even when News is unavailable, and a funding article may not yet be
represented in structured history.

For deduplication, compare company identity, round label, timing, participants and
the original report. Do not assume that matching dollar amounts prove two records
are the same transaction. Preserve uncertainty when sources disagree.

## Frequently asked questions

**Does this include private-company ownership percentages?** The gateway exposes
reported funding retrieval, not shareholder-register or capitalization-table
management.

**Does a paid API key unlock every round?** Credits pay for API usage. Existing
Radar entitlements and source coverage continue to determine returned data.

Related: [company data](company-data-api.md), [investor discovery](investor-data-api.md),
[funding news](funding-news-api.md), [API pricing](pricing-pay-per-use.md).

<!-- captured-workflow -->
## Build a funding timeline that can survive source corrections

Store each reported round with its source label, reported date, amount, approximate
flag and investor associations. Keep your reconciliation status separate from
the retrieved values. This lets an analyst correct a duplicate or disputed
association without losing the original observation. A company-level investor
list must not be copied wholesale into every individual round.

The captured OpenAI record illustrates why that matters. It contains ten rounds
and marks amounts approximate. Some source text and structured investor
associations require reconciliation, and source announcements can describe a
company's fund or an investment made by the company rather than capital received.
The published excerpt keeps the actual numeric fields and a small investor subset;
it intentionally omits the longer source announcement text.

The separate market-pulse capture has a stronger recency problem: records labeled
recent include future years such as 2074 and an amount of -1. That value is an
unknown-amount sentinel in the observed row, not a negative transaction. Exclude
such rows from a current funding chart pending review and retain the reason.
Do not use an approximate, duplicated or future-dated record to calculate a
market's total capital raised. The endpoint reference exposes the actual row so
an integrator can build and evaluate that handling explicitly.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/funding`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_company_funding -->
```json
{
  "domain": "openai.com"
}
```

<!-- response-example: get_company_funding -->
```json
{
  "ok": true,
  "feature": "get_company_funding",
  "data": {
    "amount_approx": true,
    "investors": [
      {
        "current_investment": [
          "Funding round",
          2025
        ],
        "domain": "microsoft.com",
        "company_id": 335807,
        "name": "microsoft",
        "slug": "microsoft-corporation"
      },
      {
        "current_investment": [
          "Funding round",
          2025
        ],
        "domain": "thrivecap.com",
        "company_id": 1030626,
        "name": "thrive capital",
        "slug": "thrive-capital"
      }
    ],
    "rounds": [
      {
        "amount": 41000000000,
        "date": "2025-01-28",
        "investors": [
          {
            "name": "microsoft",
            "domain": "microsoft.com"
          },
          {
            "name": "thrive capital",
            "domain": "thrivecap.com"
          }
        ],
        "name": "Funding round"
      },
      {
        "amount": 6600000000,
        "date": "2024-03-10",
        "investors": [
          {
            "name": "thrive capital",
            "domain": "thrivecap.com"
          },
          {
            "name": "g42",
            "domain": "g42.ai"
          }
        ],
        "name": "Funding round"
      }
    ]
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:46.218682+00:00",
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
The [downloadable JSON example](../examples/get_company_funding.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The OpenAI capture contained ten round records and amount_approx=true. Its source announcement text and structured investor associations were not fully reconciled: one announcement referred to SoftBank while a structured association named Microsoft. The excerpt retains numerical and identity fields but omits long announcement text. Review the source before treating a particular association as confirmed participation.

See the [complete get_company_funding endpoint reference](../reference/get_company_funding.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
