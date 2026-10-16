# Shiprocket Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “shiprocket revenue” · 260/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [shiprocket-revenue.json](../../examples/use-cases/shiprocket-revenue.json).

**Question.** What revenue and profit has Shiprocket reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `shiprocket.in` |
| Fiscal periods with figures | 5 |
| Summary | Latest reported FY2025: revenue $195.84M, net income $—. YoY +24.0% (1.24× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $195.8M | $-8.9M | $840k | $840k | news report |
| FY2024 | $157.9M | $-71.4M | — | — | news report |
| FY2023 | $130.7M | $-40.9M | — | — | news report |
| FY2022 | $73.3M | $-11.2M | — | — | news report |
| FY2020 | $19.8M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2024-12-28 | Series E (extension) | $26.3M | Shiprocket, a logistics SaaS unicorn, is raising ₹219 crore ( Around $26 million) in an extension of its Series E funding round. The round… |
| 2024-04-25 | Funding round | $11M | Shiprocket had last raised $11 million in funding from McKinsey in October. |
| 2023-10-14 | Bridge Round | $11M | Shiprocket bagged $11 Mn in a Bridge Round |
| 2023-01-16 | Fresh Capital | $31.2M | In the same month, logistics platform Shiprocket entered the much-coveted unicorn club after raising Rs 260 crore in fresh capital by… |
| 2022-10-26 | Funding round | $31.2M | the startup, operated by Bigfoot Retail Solutions Pvt Ltd, has joined the much-coveted unicorn club after raising Rs 260 crore (around $33… |
| 2022-08-17 | Series E2 | $33.5M | Shiprocket raised $33.5 Mn in a Series E2 round fresh funding round led by Lightrock India. |
| 2022-02-14 | Funding round | — | The company has invested US$225 million across Blinkit (formerly Grofers), Shiprocket and Magicpin. |
| 2021-12-10 | Series E | $185M | Logistics aggregator platform Shiprocket has raised $185 million in a Series E round co-led by Zomato, Teamasek and Lightrock India.… |
| 2021-07-08 | Series D1 | $41.3M | BigFoot Retail Solutions Pvt Ltd, which operates ecommerce focused logistics-tech firm Shiprocket, on Thursday said it has raised $41.3… |
| 2021-02-18 | Series C3 | $27M | E-commerce aggregation platform Shiprocket on Thursday announced it has raised $27 million (nearly 200 Crore) in Series C3 funding. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain shiprocket.in --statement all --period-type all --limit 8
radar get-company-funding --domain shiprocket.in
radar news-overview --company shiprocket.in --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "shiprocket.in", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "shiprocket.in"}, timeout=120)
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

- [Ather Energy Financials](ather-energy-financials.md)
- [Inmobi Revenue](inmobi-revenue.md)
- [Spinny Revenue](spinny-revenue.md)
- [Darwinbox Revenue](darwinbox-revenue.md)
