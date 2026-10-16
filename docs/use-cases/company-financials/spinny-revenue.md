# Spinny Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “spinny revenue” · 260/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [spinny-revenue.json](../../examples/use-cases/spinny-revenue.json).

**Question.** What revenue and profit has Spinny reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `spinny.com` |
| Fiscal periods with figures | 4 |
| Summary | Latest reported FY2025: revenue $558.84M, net income $—. YoY +25.0% (1.25× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $558.8M | $-50.9M | — | $-45.7M | news report |
| FY2024 | $447M | $-70.8M | — | — | news report |
| FY2023 | $391.4M | — | — | — | news report |
| FY2022 | $21.6M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-04-20 | Series F | — | Valuedrive Technologies Private Limited, dba Spinny, has raised approximately $340 million across its Series F and its Series G fundraises. |
| 2025-12-11 | Funding round | $165M | Spinny, an India-based used-car retailer, is set to raise up to $165 million in a funding round, Entrackr reports. |
| 2025-06-13 | Series F | $170M | Used car marketplace Spinny has secured $30 million in primary capital from investment firm WestBridge Capital, as part of an extension to… |
| 2025-04-01 | Funding round | $131M | Used-car sales platform Spinny has raised $131 million (Rs 1,120 crore) in a funding round led by US-based Accel Leaders Fund at a flat… |
| 2025-01-23 | Funding round | $120M | Spinny could raise up to $120 million from internal investors including Elevation Capital, Abu Dhabi Growth Fund, General Catalyst and… |
| 2021-11-24 | Series E | $285M | Online used car marketplace Spinny has raised $285 million in its Series E funding round, led by Abu Dhabi-based ADQ and New York-based… |
| 2021-07-09 | Series D | $105M | Full-stack used car retailing platform Spinny has raised over $100 million in its Series D round led by Tiger Global. |
| 2021-04-07 | Series C | $65M | Spinny has raised $65 million in its Series C financing round, the five-year-old Indian startup said. |
| 2020-03-02 | Series B | $43.7M | Pre‑owned cars platform Spinny has raised $43.7 million (around 316.46 crore at current exchange rates) in its Series B funding led by the… |
| 2019-09-27 | Series B | $50M | Spinny has closed about $50 million in a Series B round led by an American investor. New investors from India, including Nandan Nilekani’s… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain spinny.com --statement all --period-type all --limit 8
radar get-company-funding --domain spinny.com
radar news-overview --company spinny.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "spinny.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "spinny.com"}, timeout=120)
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

- [Inmobi Revenue](inmobi-revenue.md)
- [Shiprocket Revenue](shiprocket-revenue.md)
- [Darwinbox Revenue](darwinbox-revenue.md)
- [Rebel Foods Revenue](rebel-foods-revenue.md)
