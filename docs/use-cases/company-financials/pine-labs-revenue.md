# Pine Labs Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “pine labs revenue” · 260/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [pine-labs-revenue.json](../../examples/use-cases/pine-labs-revenue.json).

**Question.** What revenue and profit has Pine Labs reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `pinelabs.com` |
| Fiscal periods with figures | 14 |
| Summary | Latest reported Q4 FY2026: revenue $89.28M, net income $5.04M. YoY +23.0% (1.23× prior period). Recent signals: Profitable. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q4 FY2026 | $89.3M | $5M | — | — | news report |
| Q3 FY2026 | $89.3M | $5M | $20.5M | — | news report |
| Q2 FY2026 | $78M | $720k | $14.6M | — | news report |
| Q1 FY2026 | $73.8M | $576k | — | — | news report |
| Q2 FY2025 | $66.2M | $-3.8M | — | — | news report |
| FY2025 | $272.9M | $-17.4M | $42.7M | — | news report |
| FY2024 | $158M | — | — | — | news report |
| Q4 FY2023 | $89.3M | $5.1M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-11-03 | IPO | $249.6M | Fintech company Pine Labs is opening its IPO on 7 November 2025, targeting a fresh issue of INR 2,080 crore (with an offer for sale in… |
| 2022-02-18 | Funding round | $150M | Merchant commerce platform Pine Labs has raised $150 million in a fresh round from Alpha Wave Global. |
| 2021-05-16 | Funding round | $285M | Pine Labs, a startup that offers merchants payments terminals, invoicing tools and working capital, said on Monday it has completed the… |
| 2021-03-29 | Funding round | $300M | Two of the five largest fintech deals in APAC in 2020 went towards Indian paytech firms: Navi Technologies, which raised US$397 million,… |
| 2020-12-21 | Series H | $300M | Earlier in January, it had scooped up $300 million in Series H round from Mastercard. |
| 2020-07-23 | Investment | $125M | In May 2018, Singapore state investment firm Temasek and American payments giant PayPal Holdings Inc. invested a total of $125 million in… |
| 2020-01-25 | Funding round | $100M | Pine Labs — the merchant payment solution startup launched in 1998 and last valued at reportedly $900 million around its $125 million… |
| 2019-07-30 | Equity investment | $125M | "In May last year, Temasek and PayPal Holdings Inc had acquired minority stakes in the company for a combined $125 million (about Rs 843… |
| 2018-11-28 | Private Placement | $125M | Another large funding round in this subsector was $125m raised by Pine Labs in a private equity round. |
| 2018-05-31 | Funding round | $125M | Temasek and PayPal Holdings Inc have acquired minority stakes in the company for a combined $125 Mn. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain pinelabs.com --statement all --period-type all --limit 8
radar get-company-funding --domain pinelabs.com
radar news-overview --company pinelabs.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "pinelabs.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "pinelabs.com"}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`get_company_funding`, `get_financials`, `news_overview`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.
- EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies.
- Part of the news index is temporarily offline; this answer uses about 86% of indexed articles, so counts are lower bounds.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- News, events and funding are separate populations and must not be added together. Topic search checks article text for news, event descriptions for events and deal descriptions for funding; an explicit match mode uses source articles.

## Related use cases

- [Country Delight Revenue](country-delight-revenue.md)
- [Licious Revenue](licious-revenue.md)
- [Makemytrip Revenue](makemytrip-revenue.md)
- [Revolut Revenue](revolut-revenue.md)
