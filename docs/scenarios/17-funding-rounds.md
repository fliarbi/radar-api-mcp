# Retrieve OpenAI funding rounds separately from revenue.

[All 50 scenarios](README.md) · [Workflow guide](../guides/startup-funding-data-api.md) · [Endpoint reference](../reference/get_company_funding.md)

**POST `/v1/companies/funding`** · MCP tool **`get_company_funding`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 17-funding-rounds -->
```json
{
  "domain": "openai.com"
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.177451+00:00; HTTP **200**;
**observed**, 0.151 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

These are reported whole-round amounts and associations, not sales revenue or a particular investor's cheque. Reconcile approximate values, recipient identity and repeated announcements before totaling capital raised.

The baseline was HTTP 200, **observed**:
Response contract and declared scenario checks passed; source truth not independently certified. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 17-funding-rounds -->
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
    "retrieved_at": "2026-09-23T03:35:32.177194+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/17-funding-rounds.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
