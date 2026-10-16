# Flipkart Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “flipkart revenue” · 1,600/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [flipkart-revenue.json](../../examples/use-cases/flipkart-revenue.json).

**Question.** What revenue and profit has Flipkart reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `flipkart.com` |
| Fiscal periods with figures | 13 |
| Summary | Latest reported FY2025: revenue $9.93B, net income $—. YoY +17.4% (1.17× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $9.9B | $-622.7M | — | — | news report |
| FY2024 | $8.5B | $-509.8M | — | — | news report |
| FY2023 | $1.8B | — | — | — | news report |
| FY2022 | $1.3B | $-523.4M | $-471M | $-471M | news report |
| FY2021 | $5.2B | $-2.9B | — | — | news report |
| FY2020 | $41.5B | $-378M | — | — | news report |
| FY2019 | $5.2B | $-2.1B | — | — | news report |
| FY2018 | $4.6B | $-600M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-04-20 | pre-IPO | $2.2B | E-commerce major Flipkart is exploring a $2-2.5 billion (around Rs 18,570-23,213 crore) pre-IPO fundraise, while private‑equity firm KKR… |
| 2025-08-01 | Funding round | — | Bengaluru’s company will try to raise $1.5 billion. |
| 2025-05-30 | Equity | $26.7M | As part of this strategic focus, Flipkart’s Indian marketplace entity recently received a capital infusion of ₹2,225 crore (approximately… |
| 2025-04-02 | Funding round | $281.4M | In the past year alone, Flipkart received maximum funding from Singapore-based entities—totaling Rs 2,345 crore |
| 2024-07-03 | Late-Stage | $350M | Late-stage companies such as Zepto, Flipkart, PharmEasy and Lenskart topped with $665 million, $350 million, $216 million, and $200… |
| 2023-12-22 | Equity | $600M | The homegrown ecommerce company Flipkart continues to receive financial support from its parent firm Walmart with a $600 million infusion. |
| 2023-09-03 | Acquisition | $3.5B | Walmart, the US retail major has raised its stake in Flipkart as it paid $3.5 billion (around ₹28,953 crore) to acquire shares from its… |
| 2023-01-11 | Private Equity | $90 | Flipkart Internet, the marketplace arm of ecommerce firm Flipkart, has received a cash infusion of close to $90 million (Rs 722 crore)… |
| 2022-10-26 | Series (or unspecified) | $3B | Retail giant Walmart is reportedly raising up to $3 billion for its e-commerce giant Flipkart to further expand its operations in the… |
| 2022-01-05 | Funding round | $233M | Walmart-backed Indian ecommerce giant Flipkart has received fresh investment of $233 Mn (INR 1,736 Cr) from its Singapore holding company. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain flipkart.com --statement all --period-type all --limit 8
radar get-company-funding --domain flipkart.com
radar news-overview --company flipkart.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "flipkart.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "flipkart.com"}, timeout=120)
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

- [Lenskart Revenue](lenskart-revenue.md)
- [Databricks Revenue](databricks-revenue.md)
- [Stripe Revenue](stripe-revenue.md)
- [Meesho Revenue](meesho-revenue.md)
