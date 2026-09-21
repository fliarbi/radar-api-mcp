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
The published response keeps all captured rounds and investor associations;
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
    "events": [
      {
        "amount": 41000000000,
        "date": "2025-01-28",
        "round_type": "Funding round"
      },
      {
        "amount": 6600000000,
        "date": "2024-03-10",
        "headline": "The hottest AI startup, OpenAI, recently raised $6.6 billion at a valuation of $157 billion.",
        "round_type": "Funding round"
      },
      {
        "amount": 13000000000,
        "date": "2023-10-28",
        "headline": "OpenAI, which has garnered a whopping $13 billion in funding from Microsoft since 2019",
        "round_type": "Funding round"
      },
      {
        "amount": 175000000,
        "date": "2023-07-11",
        "headline": "OpenAI, the company behind the viral chatbot ChatGPT, has raised a $175 million fund to invest in AI startups.",
        "round_type": "Equity"
      },
      {
        "amount": 1500000000,
        "date": "2023-03-16",
        "round_type": "Funding round"
      },
      {
        "amount": 10000000000,
        "date": "2023-01-10",
        "headline": "Microsoft Corp. is in conversations to put $10 billion into OpenAI.",
        "round_type": "Funding round"
      },
      {
        "amount": 1000000000,
        "date": "2022-01-27",
        "headline": "In July 2019, Microsoft backed OpenAI with $1 billion.",
        "round_type": "Investment"
      },
      {
        "amount": 100000000,
        "date": "2021-05-27",
        "headline": "OpenAI startup fund announced it is investing $100 million in AI companies.",
        "round_type": "Venture Capital"
      },
      {
        "amount": 1000000000,
        "date": "2019-07-26",
        "headline": "the $1 billion investment OpenAI received from Microsoft.",
        "round_type": "Equity"
      },
      {
        "amount": 1000000000,
        "date": "2015-12-12",
        "headline": "In total, these funders have committed $1 billion.",
        "round_type": "Funding round"
      }
    ],
    "investors": [
      {
        "current_investment": [
          "Funding round",
          2025
        ],
        "domain": "microsoft.com",
        "company_id": 335807,
        "name": "microsoft",
        "slug": "microsoft-corporation",
        "description": "Leading MNC offering computer software, hardware solutions & services"
      },
      {
        "current_investment": [
          "Funding round",
          2025
        ],
        "domain": "thrivecap.com",
        "company_id": 1030626,
        "name": "thrive capital",
        "slug": "thrive-capital",
        "description": "Thrive Capital is an investment firm that builds and invests in internet, software, and technology-enabled companies."
      },
      {
        "current_investment": [
          "Funding round",
          2025
        ],
        "domain": "apple.com",
        "company_id": 184780,
        "name": "apple",
        "slug": "a-p-s-hydrotech-engineers",
        "description": "Apple is a corporation that designs, manufactures, and markets consumer electronics, personal computers, and software."
      },
      {
        "current_investment": [
          "Funding round",
          2025
        ],
        "domain": "nvidia.com",
        "company_id": 350448,
        "name": "nvidia",
        "slug": "nvidia",
        "description": "NVIDIA, inventor of the GPU, which creates interactive graphics on laptops, workstations, mobile devices, notebooks, PCs, and more."
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
          },
          {
            "name": "apple",
            "domain": "apple.com"
          },
          {
            "name": "nvidia",
            "domain": "nvidia.com"
          },
          {
            "name": "Apple Inc.",
            "domain": ""
          },
          {
            "name": "Sam Altman",
            "domain": ""
          },
          {
            "name": "khosla ventures",
            "domain": "khoslaventures.com"
          },
          {
            "name": "sequoia capital",
            "domain": "sequoiacap.com"
          },
          {
            "name": "tiger global",
            "domain": "tigerglobal.co.uk"
          },
          {
            "name": "MGX",
            "domain": "mgxdigital.com"
          },
          {
            "name": "softbank vision fund",
            "domain": "visionfund.com"
          },
          {
            "name": "UAE-based MGX",
            "domain": ""
          },
          {
            "name": "tiger global management",
            "domain": "tigerglobal.com"
          },
          {
            "name": "SoftBank's Vision Fund",
            "domain": ""
          },
          {
            "name": "softbank group",
            "domain": "global.softbank"
          },
          {
            "name": "softbank",
            "domain": "group.softbank"
          },
          {
            "name": "fidelity",
            "domain": "fidelityinternational.com"
          },
          {
            "name": "altimeter capital",
            "domain": "altimeter.com"
          },
          {
            "name": "Fidelity Management & Research Company",
            "domain": ""
          },
          {
            "name": "Microsoft Corporation",
            "domain": "microsoft.com"
          },
          {
            "name": "Ark Venture Fund",
            "domain": ""
          },
          {
            "name": "wells fargo",
            "domain": "wellsfargo.com"
          },
          {
            "name": "jpmorgan chase",
            "domain": "jpmorganchase.com"
          },
          {
            "name": "santander",
            "domain": "santander.com"
          },
          {
            "name": "Abu Dhabi MGX",
            "domain": ""
          },
          {
            "name": "coatue",
            "domain": "coatue.com"
          },
          {
            "name": "jp morgan",
            "domain": "jpmorgan.com"
          },
          {
            "name": "city",
            "domain": "city.com.pl"
          },
          {
            "name": "goldman sachs",
            "domain": "goldmansachs.com"
          },
          {
            "name": "morgan stanley",
            "domain": "morganstanley.com"
          },
          {
            "name": "banco santander",
            "domain": "santanderrio.com.ar"
          },
          {
            "name": "hsbc",
            "domain": "hsbc.com"
          },
          {
            "name": "citi",
            "domain": "citigroup.com"
          },
          {
            "name": "smbc",
            "domain": "smbc.re.kr"
          },
          {
            "name": "ubs",
            "domain": "unibiz.com"
          },
          {
            "name": "Citigroup",
            "domain": "citigroup.com"
          },
          {
            "name": "sumitomo mitsui banking corporation",
            "domain": "smbc.co.jp"
          },
          {
            "name": "UBS Group AG",
            "domain": ""
          },
          {
            "name": "HSBC Holdings plc",
            "domain": ""
          },
          {
            "name": "Citi (C)",
            "domain": ""
          },
          {
            "name": "SMBC (SMFG)",
            "domain": ""
          },
          {
            "name": "UBS (UBS)",
            "domain": ""
          },
          {
            "name": "HSBC (HSBC)",
            "domain": ""
          },
          {
            "name": "suro capital",
            "domain": "surocap.com"
          },
          {
            "name": "CoreNest Capital",
            "domain": ""
          },
          {
            "name": "oracle",
            "domain": "oracle.com"
          },
          {
            "name": "arm",
            "domain": "arm.com"
          },
          {
            "name": "President Trump",
            "domain": ""
          },
          {
            "name": "openai",
            "domain": "openai.com"
          },
          {
            "name": "Vision Fund",
            "domain": "visionfund.org"
          },
          {
            "name": "Elon Musk",
            "domain": ""
          },
          {
            "name": "magnetar capital",
            "domain": "magnetar.com"
          },
          {
            "name": "Coatue Management",
            "domain": "coatue.com"
          },
          {
            "name": "founders fund",
            "domain": "foundersfund.com"
          },
          {
            "name": "Altimeter Capital Management",
            "domain": "altimetergrowth.com"
          },
          {
            "name": "Investor Syndicate",
            "domain": "investorsyndicate.io"
          },
          {
            "name": "syndicate",
            "domain": "syndicate.io"
          },
          {
            "name": "JPMorgan",
            "domain": ""
          },
          {
            "name": "dragoneer investment group",
            "domain": "dragoneer.com"
          },
          {
            "name": "blackstone",
            "domain": "blackstone.com"
          },
          {
            "name": "tpg",
            "domain": "preservationgroup.com"
          },
          {
            "name": "t. rowe price",
            "domain": "troweprice.com"
          },
          {
            "name": "Andreessen Horowitz",
            "domain": ""
          },
          {
            "name": "D1 Capital Partners",
            "domain": "d1capital.com"
          },
          {
            "name": "Fidelity Management",
            "domain": ""
          },
          {
            "name": "sequoia",
            "domain": "sequoia.com.au"
          },
          {
            "name": "Altimeter",
            "domain": "altimetersoftware.com"
          },
          {
            "name": "D1 Capital",
            "domain": ""
          },
          {
            "name": "amazon",
            "domain": "amazon.com"
          },
          {
            "name": "Blue Owl Capital",
            "domain": "blueowl.com"
          },
          {
            "name": "crusoe",
            "domain": "crusoe.ai"
          },
          {
            "name": "Japanese banks",
            "domain": ""
          },
          {
            "name": "Walt Disney",
            "domain": ""
          },
          {
            "name": "The Walt Disney Co.",
            "domain": ""
          },
          {
            "name": "SoftBank Vision Fund 2",
            "domain": ""
          },
          {
            "name": "Third-party co-investors",
            "domain": ""
          },
          {
            "name": "Co-investors",
            "domain": ""
          },
          {
            "name": "other backers",
            "domain": ""
          },
          {
            "name": "sovereign wealth funds in the Middle East",
            "domain": ""
          },
          {
            "name": "thrive",
            "domain": "thrivenextgen.com"
          },
          {
            "name": "Third-party investors",
            "domain": ""
          },
          {
            "name": "Amazon.com Inc.",
            "domain": ""
          },
          {
            "name": "cerebras",
            "domain": "cerebras.ai"
          },
          {
            "name": "Middle Eastern sovereign wealth funds",
            "domain": ""
          },
          {
            "name": "UAE’s MGX fund",
            "domain": ""
          },
          {
            "name": "Sovereign Wealth Funds",
            "domain": ""
          },
          {
            "name": "D.E. Shaw Ventures",
            "domain": ""
          },
          {
            "name": "Abu Dhabi-backed MGX",
            "domain": ""
          },
          {
            "name": "D. E. Shaw & Co.",
            "domain": ""
          },
          {
            "name": "Amazon.com Inc",
            "domain": ""
          },
          {
            "name": "appaloosa management",
            "domain": "amlp.com"
          },
          {
            "name": "ARK Invest",
            "domain": "ark-invest.com"
          },
          {
            "name": "ARK Invest–managed funds",
            "domain": ""
          },
          {
            "name": "D. E. Shaw Ventures",
            "domain": ""
          },
          {
            "name": "appaloosa",
            "domain": "appaloosa.io"
          },
          {
            "name": "affiliated funds of BlackRock",
            "domain": ""
          },
          {
            "name": "dragoneer",
            "domain": "dragoneergrowth.com"
          },
          {
            "name": "goanna capital",
            "domain": "goannacapital.com"
          },
          {
            "name": "insight partners",
            "domain": "insightpartners.com"
          },
          {
            "name": "the paragon group",
            "domain": "theparagongroup-inc.com"
          },
          {
            "name": "sands capital",
            "domain": "sandscapital.com"
          },
          {
            "name": "a16z",
            "domain": "a16z.com"
          },
          {
            "name": "MGX of Abu Dhabi",
            "domain": ""
          },
          {
            "name": "T. Rowe Price Associates",
            "domain": ""
          },
          {
            "name": "blackrock",
            "domain": "blackrock.com"
          },
          {
            "name": "Fidelity Management & Research",
            "domain": ""
          },
          {
            "name": "temasek",
            "domain": "temasek.com.sg"
          },
          {
            "name": "UC Investments",
            "domain": "uc-investments.lu"
          },
          {
            "name": "advent international",
            "domain": "adventinternational.com"
          },
          {
            "name": "bain capital",
            "domain": "baincapital.com"
          },
          {
            "name": "brookfield asset management",
            "domain": "brookfield.com"
          },
          {
            "name": "Individual Investors",
            "domain": ""
          },
          {
            "name": "funds affiliated with BlackRock",
            "domain": ""
          },
          {
            "name": "sound ventures",
            "domain": "soundventures.com"
          },
          {
            "name": "winslow capital",
            "domain": "winslowcapital.com"
          },
          {
            "name": "Robinhood Ventures Fund I",
            "domain": ""
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
          },
          {
            "name": "microsoft",
            "domain": "microsoft.com"
          },
          {
            "name": "flat capital",
            "domain": "flatcapital.com"
          },
          {
            "name": "tiger global management",
            "domain": "tigerglobal.com"
          },
          {
            "name": "sequoia capital",
            "domain": "sequoiacap.com"
          },
          {
            "name": "a16z",
            "domain": "a16z.com"
          },
          {
            "name": "k2 global",
            "domain": "k2global.co"
          },
          {
            "name": "founders fund",
            "domain": "foundersfund.com"
          },
          {
            "name": "Global Investors",
            "domain": "globalinvestors.com.au"
          },
          {
            "name": "nvidia",
            "domain": "nvidia.com"
          },
          {
            "name": "softbank",
            "domain": "group.softbank"
          },
          {
            "name": "MGX",
            "domain": "mgxdigital.com"
          },
          {
            "name": "altimeter capital",
            "domain": "altimeter.com"
          },
          {
            "name": "fidelity",
            "domain": "fidelityinternational.com"
          },
          {
            "name": "khosla ventures",
            "domain": "khoslaventures.com"
          },
          {
            "name": "amazon",
            "domain": "amazon.com"
          }
        ],
        "name": "Funding round"
      },
      {
        "amount": 13000000000,
        "date": "2023-10-28",
        "investors": [
          {
            "name": "khosla ventures",
            "domain": "khoslaventures.com"
          },
          {
            "name": "microsoft",
            "domain": "microsoft.com"
          }
        ],
        "name": "Funding round"
      },
      {
        "amount": 175000000,
        "date": "2023-07-11",
        "investors": [
          {
            "name": "openai",
            "domain": "openai.com"
          }
        ],
        "name": "Equity"
      },
      {
        "amount": 1500000000,
        "date": "2023-03-16",
        "investors": [
          {
            "name": "altimeter capital",
            "domain": "altimeter.com"
          },
          {
            "name": "microsoft",
            "domain": "microsoft.com"
          },
          {
            "name": "Reid Hoffman",
            "domain": "reidhoffman.org"
          },
          {
            "name": "khosla ventures",
            "domain": "khoslaventures.com"
          },
          {
            "name": "tiger global",
            "domain": "tigerglobal.co.uk"
          },
          {
            "name": "sequoia capital",
            "domain": "sequoiacap.com"
          },
          {
            "name": "Andreessen Horowitz",
            "domain": ""
          },
          {
            "name": "thrive",
            "domain": "thrivenextgen.com"
          },
          {
            "name": "k2 global",
            "domain": "k2global.co"
          },
          {
            "name": "founders fund",
            "domain": "foundersfund.com"
          },
          {
            "name": "thrive capital",
            "domain": "thrivecap.com"
          },
          {
            "name": "tiger global management",
            "domain": "tigerglobal.com"
          }
        ],
        "name": "Funding round"
      },
      {
        "amount": 10000000000,
        "date": "2023-01-10",
        "investors": [
          {
            "name": "microsoft",
            "domain": "microsoft.com"
          },
          {
            "name": "thrive capital",
            "domain": "thrivecap.com"
          },
          {
            "name": "founders fund",
            "domain": "foundersfund.com"
          },
          {
            "name": "other venture firms",
            "domain": ""
          }
        ],
        "name": "Funding round"
      },
      {
        "amount": 1000000000,
        "date": "2022-01-27",
        "investors": [
          {
            "name": "microsoft",
            "domain": "microsoft.com"
          }
        ],
        "name": "Investment"
      },
      {
        "amount": 100000000,
        "date": "2021-05-27",
        "investors": [
          {
            "name": "microsoft",
            "domain": "microsoft.com"
          }
        ],
        "name": "Venture Capital"
      },
      {
        "amount": 1000000000,
        "date": "2019-07-26",
        "investors": [
          {
            "name": "microsoft",
            "domain": "microsoft.com"
          }
        ],
        "name": "Equity"
      },
      {
        "amount": 1000000000,
        "date": "2015-12-12",
        "investors": [
          {
            "name": "Elon Musk",
            "domain": ""
          },
          {
            "name": "Peter Thiel",
            "domain": "http://www.linkedin.com/in/peterthiel"
          },
          {
            "name": "Reid Hoffman",
            "domain": "reidhoffman.org"
          },
          {
            "name": "Jessica Livingston",
            "domain": "https://www.linkedin.com/in/jessicalivingston1"
          },
          {
            "name": "amazon web services",
            "domain": "aws.amazon.com"
          },
          {
            "name": "infosys",
            "domain": "infosys.com"
          },
          {
            "name": "Tesla's Elon Musk",
            "domain": ""
          },
          {
            "name": "Sam Altman",
            "domain": ""
          },
          {
            "name": "Greg Brockman",
            "domain": "gregbrockman.com"
          },
          {
            "name": "yc research",
            "domain": "ycr.org"
          }
        ],
        "name": "Funding round"
      }
    ],
    "stages": {
      "Equity (2019)": 1000000000,
      "Equity (2023)": 175000000,
      "Funding round (2015)": 1000000000,
      "Funding round (2023)": 13000000000,
      "Funding round (2024)": 6600000000,
      "Funding round (2025)": 41000000000,
      "Funding round (Jan 2023)": 10000000000,
      "Funding round (Mar 2023)": 1500000000,
      "Investment (2022)": 1000000000,
      "Venture Capital (2021)": 100000000
    }
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
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The OpenAI capture contained ten round records and amount_approx=true. Its source announcement text and structured investor associations were not fully reconciled: one announcement referred to SoftBank while a structured association named Microsoft. The excerpt retains numerical and identity fields but omits long announcement text. Review the source before treating a particular association as confirmed participation.

See the [complete get_company_funding endpoint reference](../reference/get_company_funding.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 66 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
