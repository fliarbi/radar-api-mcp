# Lenskart Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “lenskart revenue” · 1,300/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [lenskart-revenue.json](../../examples/use-cases/lenskart-revenue.json).

**Question.** What revenue and profit has Lenskart reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `lenskart.com` |
| Fiscal periods with figures | 17 |
| Summary | Latest reported Q4 FY2026: revenue $301.88M, net income $24.43M. YoY +46.0% (1.46× prior period). Recent signals: Profitable, Record revenue. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q4 FY2026 | $301.9M | $24.4M | — | — | news report |
| Q3 FY2026 | $276.8M | $15.9M | — | — | news report |
| Q2 FY2026 | $250.9M | $12.4M | $51.1M | — | news report |
| Q1 FY2026 | $227.3M | $7.3M | $40.4M | — | news report |
| 1H FY2026 | $501.5M | $23.2M | $94.9M | — | news report |
| Q3 FY2025 | $276.9M | $15.9M | — | — | news report |
| Q2 FY2025 | $251.5M | $12.3M | $49.7M | — | news report |
| FY2025 | $755M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-08-26 | Funding round | $26.4M | Lenskart, a popular eyewear provider co‑founded by Peyush Bansal, has filed for an IPO to raise Rs 2,200 crore through a fresh issue and… |
| 2024-12-08 | Equity | $180M | Lenskart is investing Rs 1,500 crore for this factory that is formed in Telangana. |
| 2024-06-03 | Funding round | $200M | Indian eyewear retailer Lenskart has raised $200 million from Singapore state investment firm Temasek and Fidelity Management and Research… |
| 2023-10-03 | Equity | $600M | This was followed by eyewear brand Lenskart, which raised $600 million. |
| 2023-06-15 | Funding round | $100M | Private equity fund Chryscapital on Thursday announced a USD 100 million (over Rs 819 crore) investment in eyewear company Lenskart. |
| 2023-04-11 | Series J | $500M | Lenskart raised $500 million in Series J round led by a wholly-owned subsidiary of Abu Dhabi Investment Authority (ADIA) at a valuation of… |
| 2022-12-12 | Funding round | $39.6M | Last month, Lenskart raised $39.6 million from Chiratae Ventures, DSP India Fund and Axis Growth Avenues AIF-I in its fifth fundraising… |
| 2022-08-28 | Equity | $100M | it has so far raised 165 million this year, including a $100 million round from Alpha Wave Ventures (previously Falcon Edge). |
| 2022-04-11 | Funding round | $100M | Multi-channel eyewear brand Lenskart has raised Rs 760 crore or $100 million in a new round from Alpha Wave Incubation (Previously Falcon… |
| 2021-11-11 | Venture Capital | — | Lenskart floated its Vision Fund of $20 million to invest in ancillary businesses. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain lenskart.com --statement all --period-type all --limit 8
radar get-company-funding --domain lenskart.com
radar news-overview --company lenskart.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "lenskart.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "lenskart.com"}, timeout=120)
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

- [Zomato Revenue](zomato-revenue.md)
- [Boat Revenue](boat-revenue.md)
- [Databricks Revenue](databricks-revenue.md)
- [Flipkart Revenue](flipkart-revenue.md)
