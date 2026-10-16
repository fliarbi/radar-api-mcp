# Darwinbox Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “darwinbox revenue” · 260/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [darwinbox-revenue.json](../../examples/use-cases/darwinbox-revenue.json).

**Question.** What revenue and profit has Darwinbox reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `darwinbox.com` |
| Fiscal periods with figures | 4 |
| Summary | Latest reported FY2025: revenue $64.07M. YoY +35.9% (1.36× prior period). Growth pattern is consistent across reported periods. Recent signals: Record… |
| Recorded funding events | 9 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $64.1M | — | — | — | news report |
| FY2024 | $47.2M | — | — | — | news report |
| FY2023 | $26.4M | $-18M | — | — | news report |
| FY2022 | $14M | $-8M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-08-14 | Funding round | $40M | HRTech startup Darwinbox has raised US$40 million (approx. Rs 350 crore) from Teachers’ Venture Growth (TVG), which is the late‑stage… |
| 2025-03-05 | Funding round | $140M | Enterprise HR technology platform Darwinbox, has raised $140 million (about INR 1,218.1 Cr) funding in an undisclosed round co-led by… |
| 2024-03-04 | Funding round | $115.9M |  |
| 2023-01-04 | Series D | $4.9M | Hyderabad-based HR tech firm ﻿Darwinbox﻿ has raised around $4.9 million from the State Bank of India (SBI) in an extended Series D round. |
| 2022-11-03 | Series D | $4M | Microsoft Corp. has invested $4 million U.S. in India-based HRTech startup Darwinbox |
| 2022-01-25 | Funding round | $72M | The technology-based human resource company Darwinbox said on Tuesday that he has raised $7.2 crore from investors and will cross an… |
| 2021-01-19 | Funding round | $15M | Darwinbox, the HR tech startup based out of Hyderabad, has raised $15 million from Salesforce Ventures, the investment arm of global… |
| 2019-09-25 | Series B | $15M | Hyderabad-based Darwinbox, which operates a cloud-based human resource management platform, said on Thursday it has raised $15 million in… |
| 2017-06-19 | Series A | $4M | The company has raised $4 million (Rs 25.79 crore) in its Series A round led by Lightspeed India Partners LLC, |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain darwinbox.com --statement all --period-type all --limit 8
radar get-company-funding --domain darwinbox.com
radar news-overview --company darwinbox.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "darwinbox.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "darwinbox.com"}, timeout=120)
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

- [Shiprocket Revenue](shiprocket-revenue.md)
- [Spinny Revenue](spinny-revenue.md)
- [Rebel Foods Revenue](rebel-foods-revenue.md)
