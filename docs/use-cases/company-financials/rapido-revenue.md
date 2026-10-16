# Rapido Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “rapido revenue” · 720/month India · 20/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [rapido-revenue.json](../../examples/use-cases/rapido-revenue.json).

**Question.** What revenue and profit has Rapido reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `rapido.bike` |
| Fiscal periods with figures | 4 |
| Summary | Latest reported FY2025: revenue $112.08M, net income $—. YoY +44.1% (1.44× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $112.1M | $-31M | $-12.5M | $-12.5M | news report |
| FY2024 | $77.8M | $-44.5M | — | — | news report |
| FY2023 | $59.7M | — | — | — | news report |
| FY2022 | $17.4M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-09-24 | Funding round | $223M | Prosus will acquire Rapido shares worth $223 million (Rs 1,968 crore) following Swiggy’s complete exit from the startup. |
| 2025-06-09 | Funding round | $15M | Nexus Venture Partners will invest Rs 125 crore (around $15 million) in Rapido as a part of a larger financing round last year that valued… |
| 2025-02-07 | Series E | $30M | Mobility Firm Rapido To Raise Rs 250Cr in Series E Funding Round. |
| 2024-07-29 | Funding round | $120M | Ride-hailing startup Rapido has reportedly bagged a funding of $120 Mn (about INR 1,000 Cr) from existing investor WestBridge Capital at a… |
| 2024-04-23 | Funding | $100M | Bengaluru‑based Rapido is seeking around $100 million in new funding. |
| 2022-04-15 | Series D | $180M | Bike taxi platform Rapido, has raised $180 million in its latest Series D round. |
| 2021-12-22 | Funding round | $200M | "The terms of the deal have been finalised wherein Swiggy would lead a $200 million round in Rapido. It’s likely to invest around $100… |
| 2021-08-15 | Funding round | $52M | Bike-taxi platform Rapido on Monday said it has secured $52 million in fresh funding at a time when the mobility sector is clocking a… |
| 2021-05-08 | Funding round | $43.4M | Bike taxi platform Rapido has raised $43.4 million in a round led by WestBridge Capital. |
| 2020-03-03 | Series B | $54.6M | In August last year, the Roppen Transportation Services Pvt. Ltd-operated Rapido raised Rs 391 crore (around $54.6 million) in its Series… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain rapido.bike --statement all --period-type all --limit 8
radar get-company-funding --domain rapido.bike
radar news-overview --company rapido.bike --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "rapido.bike", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "rapido.bike"}, timeout=120)
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

- [Canva Revenue](canva-revenue.md)
- [Mamaearth Revenue](mamaearth-revenue.md)
- [Paytm Revenue](paytm-revenue.md)
- [Razorpay Revenue](razorpay-revenue.md)
