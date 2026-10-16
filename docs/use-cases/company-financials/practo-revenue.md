# Practo Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “practo revenue” · 320/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [practo-revenue.json](../../examples/use-cases/practo-revenue.json).

**Question.** What revenue and profit has Practo reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `practo.com` |
| Fiscal periods with figures | 5 |
| Summary | Latest reported FY2025: revenue $28.8M, net income $—. YoY -40.0% (0.6× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $28.8M | $-2M | — | — | news report |
| FY2024 | $48M | $-2M | $2M | — | news report |
| FY2022 | $24.2M | — | — | — | news report |
| FY2017 | $25.2M | $-22.9M ⚠ | — | — | news report |
| FY2015 | $3.6M | $-1.5M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

⚠ marks a figure more than eight times this company's typical value for that metric, usually a unit or currency slip in the source report. Verify it before use.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2021-05-11 | Debt | $7.2M | Bengaluru-based telemedicine and mobile health startup ﻿Practo﻿ is looking to raise about Rs 60 crore in debt funding from Trifecta… |
| 2021-01-05 | Series D | $32M | Practo ($32 million raised in Series D round) |
| 2020-08-17 | Series E | $32M | Online healthcare portal Practo has raised $32 million (Rs 240 crore) in a new round of funding led by Chinese life insurance conglomerate… |
| 2019-07-29 | Equity | $8.4M | The funding in the online grocer comes close on the heels of Trifecta Capital’s Rs 70 crore investment in health-tech firm Practo… |
| 2017-06-30 | Equity | $55M | Practi raised $55 million in a Series-D funding led by China's Tencent Holdings in January earlier this year, and which, reportedly,… |
| 2017-04-12 | Funding round | $180M | Practo has raised around $180 million from investors, including a recent $55 million Series D led by Chinese internet giant Tencent, to… |
| 2017-01-16 | Series D | $55M | India-based Practo, a startup that helps consumers locate doctors and healthcare information, has closed a $55 million Series D funding… |
| 2015-12-04 | Funding round | $120M | Tencent invested $120 million |
| 2015-08-06 | Series C | $90M | Chinese Internet giant Tencent is getting its tentacles into India’s healthcare space after it led a $90 million Series C round for… |
| 2015-06-09 | Funding round | $48M | Practo, healthcare technology startup, might see investments to the tune of Rs 400 crore by Russian billionaire Yuri Milner and Google… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain practo.com --statement all --period-type all --limit 8
radar get-company-funding --domain practo.com
radar news-overview --company practo.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "practo.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "practo.com"}, timeout=120)
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

- [Dream11 Revenue](dream11-revenue.md)
- [Upgrad Revenue](upgrad-revenue.md)
- [Acko Revenue](acko-revenue.md)
- [Ather Energy Financials](ather-energy-financials.md)
