# Freshworks Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “freshworks revenue” · 320/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [freshworks-revenue.json](../../examples/use-cases/freshworks-revenue.json).

**Question.** What revenue and profit has Freshworks reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `freshworks.com` |
| Fiscal periods with figures | 20 |
| Summary | Latest reported Q1 FY2026: revenue $222.74M, EPS $0.14. YoY +13.5% (1.13× prior period). Growth pattern is consistent across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q1 FY2026 | $222.7M | — | — | — | news report |
| Q4 FY2025 | $222.7M | — | — | $39.7M | news report |
| Q3 FY2025 | $215.1M | $-4.7M | — | $-7.5M | news report |
| Q2 FY2025 | $204.7M | — | — | $-8.7M | news report |
| Q1 FY2025 | $196.3M | $-1.3M | — | $46.4M | news report |
| FY2025 | $838.8M | $183.7M ⚠ | — | $13.2M | news report |
| Q4 FY2024 | $26.9M | $-21.9M | — | $-23.8M | news report |
| Q3 FY2024 | $1.9B ⚠ | $-25.9M | — | $-38.9M | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

⚠ marks a figure more than eight times this company's typical value for that metric, usually a unit or currency slip in the source report. Verify it before use.

## Recorded funding events

`get_company_funding`; amounts are reported figures.

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2024-04-06 | Equity | — | Freshworks listed on Nasdaq at a valuation of $13.5 billion. |
| 2024-02-06 | Funding round | $484M | Freshworks Total Funding: $484 Mn Sector: Enterprisetech |
| 2023-05-17 | Funding round | $200M | WestBridge Capital, which appears to be retuning its investment strategy with bigger and bolder bets against its historical stance of… |
| 2021-09-23 | IPO | $1B | The IPO was led by Morgan Stanley, JPMorgan Chase & Co. and Bank of America Corp. |
| 2020-10-28 | Funding round | $399M | Freshworks, which builds a customer management platform that has hooked customers like Honda, Cisco, and American Express, has raised a… |
| 2020-07-28 | Funding round | $85M | Freshworks (formerly, Freshdesk) on Monday announced that it has raised $85 million from Steadview Capital, a London-based alternative… |
| 2019-11-13 | Series H | $150M | Freshworks, a company that makes a variety of business software tools, from CRM to help-desk software, announced a $150 million Series H… |
| 2019-07-17 | Funding round | $100M | Freshworks bagged the unicorn tag with $100 million round followed by Druva that recently picked up $130 million from US-based hedge fund… |
| 2019-02-28 | Funding round | $544M | Chennai, home to software-as-a-service (SaaS) unicorn Freshworks, received $544 million in funding. |
| 2018-07-31 | Funding round | $100M | Freshworks, a company that offers a variety of business software tools ranging from IT management to CRM for sales and customer support… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain freshworks.com --statement all --period-type all --limit 8
radar get-company-funding --domain freshworks.com
radar news-overview --company freshworks.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "freshworks.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "freshworks.com"}, timeout=120)
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

- [Ola Electric Revenue](ola-electric-revenue.md)
- [Unacademy Revenue](unacademy-revenue.md)
- [Delhivery Revenue](delhivery-revenue.md)
- [Nykaa Revenue](nykaa-revenue.md)
