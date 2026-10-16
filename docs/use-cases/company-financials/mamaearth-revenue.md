# Mamaearth Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “mamaearth revenue” · 720/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [mamaearth-revenue.json](../../examples/use-cases/mamaearth-revenue.json).

**Question.** What revenue and profit has Mamaearth reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `mamaearth.in` |
| Fiscal periods with figures | 9 |
| Summary | Latest reported Q1 FY2025: revenue $66.48M, net income $3.66M. YoY +19.3% (1.19× prior period). Growth has been erratic across reported periods. Recent… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q1 FY2025 | $66.5M | $3.7M | — | — | news report |
| Q3 FY2024 | $59.9M | $3.1M | $5.5M | — | news report |
| Q2 FY2024 | $59.5M | $3.5M | $4.8M | — | news report |
| 1H FY2024 | $115.3M | $6.5M | — | — | news report |
| FY2023 | $181.8M | $-18.1M | — | — | news report |
| FY2022 | $114.3M | $2.4M | — | — | news report |
| FY2021 | $55.3M | $3M | — | — | news report |
| FY2020 | $13.4M | $-708k | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2024-06-08 | Funding round | $720k | She invested another INR 6 Cr in the D2C unicorn in September 2022. |
| 2023-11-04 | Growth stage | $91M | D2C brand Mamaearth led the pack with $91 million in funding |
| 2022-03-29 | Funding round | $38M | This year also saw beauty brand, Mamaearth, become the first brand of the year to enter the coveted unicorn club after raising $38 Mn from… |
| 2022-01-01 | Funding round | $52M | MamaEarth: Baby and mother care brand Mamaearth has raised close to $52 million in a new round at unicorn valuation led by Sequoia. |
| 2021-07-26 | Funding round | $50M | Personal care brand Mamaearth has raised $50 million from European investment firm Sofina Ventures SA and Sequoia Capital. |
| 2021-05-13 | Funding round | $80M | European investment firm Sofina is in advanced talks to lead a new round of funding in personal care brand Mamaearth at a valuation of… |
| 2020-01-08 | Funding round | $15.6M | Personal care brand Mamaearth on Wednesday said it has raised Rs 130 crore in funding led by Sequoia India. |
| 2019-07-10 | Series B | $20M | Mamaearth, an online retailer specialising in baby and toddler products, is in talks to raise up to $20 million (about Rs 137 crore at… |
| 2018-09-11 | Series A | $4M | Honasa Consumer Pvt. Ltd, which owns and operates babycare products startup Mamaearth, has raised $4 million (Rs 28 crore) in its Series A… |
| 2018-04-19 | Funding round | $250k | Bollywood actress Shilpa Shetty Kundra has invested $250,000 in MamaEarth--an online baby care products startup. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain mamaearth.in --statement all --period-type all --limit 8
radar get-company-funding --domain mamaearth.in
radar news-overview --company mamaearth.in --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "mamaearth.in", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "mamaearth.in"}, timeout=120)
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

- [Oyo Revenue](oyo-revenue.md)
- [Canva Revenue](canva-revenue.md)
- [Rapido Revenue](rapido-revenue.md)
- [Paytm Revenue](paytm-revenue.md)
