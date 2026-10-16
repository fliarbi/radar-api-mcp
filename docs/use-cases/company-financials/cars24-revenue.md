# Cars24 Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “cars24 revenue” · 320/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [cars24-revenue.json](../../examples/use-cases/cars24-revenue.json).

**Question.** What revenue and profit has Cars24 reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `cars24.com` |
| Fiscal periods with figures | 6 |
| Summary | Latest reported FY2025: revenue $747.96M, net income $—. YoY -9.9% (0.9× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $748M | $-65.2M | $-64.8M | — | news report |
| FY2024 | $830M | $-59.8M | $38.3M | — | news report |
| FY2023 | $664.2M | $-55.2M | — | — | news report |
| FY2022 | $61 | — | — | — | news report |
| FY2020 | $366.7M | — | — | — | news report |
| FY2018 | $92M | $-11M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-06-02 | Corporate Investment | $20M | Cars24 is making a significant and strategic pivot, pouring $20 million into a groundbreaking new artificial intelligence initiative… |
| 2024-07-27 | Funding round | $30.1M | Auto marketplace Cars24 has bagged INR 250 Cr ($29.8 Mn) funding from its Singapore-based parent entity Global Car Group Limited. |
| 2021-09-19 | Series F | $450M | The used car market is getting another major infusion of venture capital today, with one of the faster scaling startups out of India… |
| 2020-11-24 | Series E | $200M | Online used car marketplace Cars24 has secured $200 million in Series E financing led by existing investor DST Global at a post-money… |
| 2020-06-03 | Funding round | $100M | Cars24 had raised $100 million led by Unbound and KCK Global in October. |
| 2020-03-17 | Funding round | — | In August 2019, Dhoni also backed Gurugram-based Cars24, an online marketplace for buying and selling used cars. |
| 2019-10-17 | Series D | $100M | Tech-enabled used car marketplace CARS24 has announced that it has raised fresh capital of $100 million in their Series D round of funding. |
| 2019-04-03 | Funding round | $9.3M | Gurugram-based Cars24, online marketplace for buying and selling used cars, raised funding of Rs 77.58 crore from its Singapore parent… |
| 2018-10-14 | Funding round | $50M | Cars24 raising USD 50 million |
| 2018-06-07 | Funding round | $50M | So far, the used car buying platform has raised $49.95 million from 16 investors, including Apoletto Asia, Venture Highway along with a… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain cars24.com --statement all --period-type all --limit 8
radar get-company-funding --domain cars24.com
radar news-overview --company cars24.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "cars24.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "cars24.com"}, timeout=120)
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

- [Makemytrip Revenue](makemytrip-revenue.md)
- [Revolut Revenue](revolut-revenue.md)
- [Firstcry Revenue](firstcry-revenue.md)
- [Dream11 Revenue](dream11-revenue.md)
