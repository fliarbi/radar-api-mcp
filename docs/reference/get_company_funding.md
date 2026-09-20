# Company funding API: reported rounds, amounts and investors

[All endpoints](README.md) · [Workflow guide](../guides/startup-funding-data-api.md)

Retrieve reported company funding rounds and associated investor information. The endpoint is designed for a fundraising-history section or a research drilldown from company discovery. It does not represent a capitalization table, audited capital receipts or confirmed current ownership percentages.

## Route, authentication and credits

**`POST /v1/companies/funding`** · MCP tool **`get_company_funding`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/funding" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"openai.com"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_funding -->
```json
{
  "name": "get_company_funding",
  "arguments": {
    "request": {
      "domain": "openai.com"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

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
        "round_type": "Funding round"
      },
      {
        "amount": 13000000000,
        "date": "2023-10-28",
        "round_type": "Funding round"
      },
      {
        "amount": 175000000,
        "date": "2023-07-11",
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
        "round_type": "Funding round"
      },
      {
        "amount": 1000000000,
        "date": "2022-01-27",
        "round_type": "Investment"
      },
      {
        "amount": 100000000,
        "date": "2021-05-27",
        "round_type": "Venture Capital"
      },
      {
        "amount": 1000000000,
        "date": "2019-07-26",
        "round_type": "Equity"
      },
      {
        "amount": 1000000000,
        "date": "2015-12-12",
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

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.rounds` | Reported financing entries with a name, date, amount and investor associations when available. |
| `data.amount_approx` | A source qualifier that must travel with displayed amounts. |
| `data.investors` | Company-level investor records, not automatically participants in every round. |
| `data.stages` | Source stage summaries; avoid adding these to individual rounds as if they were separate transactions. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Review round dates, labels and amount_approx together. Compare reported investors with the underlying announcement when available through News. Keep debt, equity, valuation, cumulative funding and individual round amounts separate in your own data model.

Several reports can describe the same transaction. Summing every round, stage summary and announcement together can double-count capital; a funding amount is not automatically a valuation.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/startup-funding-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
