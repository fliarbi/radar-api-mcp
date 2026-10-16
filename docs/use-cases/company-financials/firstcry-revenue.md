# Firstcry Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “firstcry revenue” · 320/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [firstcry-revenue.json](../../examples/use-cases/firstcry-revenue.json).

**Question.** What revenue and profit has Firstcry reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `firstcry.com` |
| Fiscal periods with figures | 13 |
| Summary | Latest reported Q3 FY2026: revenue $297.6M, net income $—. YoY +11.9% (1.12× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q3 FY2026 | $297.6M | $-4.6M | — | — | news report |
| Q2 FY2026 | $251.9M | — | — | — | news report |
| Q1 FY2026 | $223.5M | — | — | — | news report |
| Q3 FY2025 | $266M | $-1.8M | $18.2M | — | news report |
| Q2 FY2025 | $234.5M | $-7.5M | $9.6M | — | news report |
| Q1 FY2025 | $198.2M | $-90.8M | $89.2M | — | news report |
| FY2024 | $789M | $-38.6M | — | — | news report |
| FY2023 | $675.8M | $-58.3M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2023-12-29 | Equity | $500M | On December 28, FirstCry filed its draft IPO papers for an estimated $500 million IPO. |
| 2023-10-01 | Equity | $52.2M | In August, three family investment office funds collectively acquired a stake worth about ₹435 crore in IPO-bound online kids and baby… |
| 2022-04-02 | Secondary Share Sale | $315M | FirstCry had conducted a $315-million secondary share sale in March last year. |
| 2022-02-03 | Secondary | $240M | it led a $240-million secondary funding round in Mahindra-backed, baby products e-commerce firm FirstCry |
| 2021-06-29 | Seed | $75M | Besides these companies, FirstCry is in the last leg to raise $75 million from SoftBank, TPG Capital, ChrysCapital and Premji Invest to… |
| 2021-04-29 | Equity | $75M | Pune-based kidswear ecommerce unicorn FirstCry is set to launch India’s largest Thrasio-style investment venture for D2C brands and online… |
| 2021-01-08 | Secondary Transaction | $180M | FirstCry’s early investors such as Chiratae Ventures, Vertex Ventures and Elevation Capital could sell their stake in the company for $180… |
| 2020-04-01 | Equity | $296M | The mega funding rounds in OYO ($807 Mn), ReNew Power ($450 Mn), FirstCry ($296 Mn) and others uplifted the overall value of capital… |
| 2020-02-10 | Series E | $296M | Pune-based baby products marketplace FirstCry has raised $296 Mn (INR 2120 Cr) Series E funding from Japan-based marquee investor… |
| 2019-01-25 | Funding round | $150M | The Japanese conglomerate’s Vision Fund has committed a total of $400 million to the omnichannel retailer, of which $150 million was… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain firstcry.com --statement all --period-type all --limit 8
radar get-company-funding --domain firstcry.com
radar news-overview --company firstcry.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "firstcry.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "firstcry.com"}, timeout=120)
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

- [Revolut Revenue](revolut-revenue.md)
- [Cars24 Revenue](cars24-revenue.md)
- [Dream11 Revenue](dream11-revenue.md)
- [Upgrad Revenue](upgrad-revenue.md)
