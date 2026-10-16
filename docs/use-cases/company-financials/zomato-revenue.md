# Zomato Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “zomato revenue” · 1,900/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [zomato-revenue.json](../../examples/use-cases/zomato-revenue.json).

**Question.** What revenue and profit has Zomato reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `zomato.com` |
| Fiscal periods with figures | 20 |
| Summary | Latest reported Q4 FY2026: revenue $375M, net income $20.88M. YoY +29.7% (1.3× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q4 FY2026 | $375M | $20.9M | — | — | news report |
| Q3 FY2026 | $321.1M | — | — | $65.6M | news report |
| Q2 FY2026 | $298.2M | $62.2M | $26.9M | — | news report |
| Q1 FY2026 | $801.9M | $3.7M | $15.6M | — | news report |
| 1H FY2026 | $25.8B ⚠ | $10.8M | — | — | news report |
| Q4 FY2025 | $289.1M | $4.7M | $51.4M | — | news report |
| Q3 FY2025 | $689.5M | $7.1M | $34.2M | — | news report |
| Q2 FY2025 | $578.6M | $36.7M | $4.2M | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

⚠ marks a figure more than eight times this company's typical value for that metric, usually a unit or currency slip in the source report. Verify it before use.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-06-03 | Primary fund raise | $210M | A regulatory filing by Info Edge (India) states “Zomato has signed a definitive agreement to undertake a primary fund raise of… |
| 2024-10-22 | QIP | $1B | Food and grocery platform Zomato ’s board has approved its plan to raise Rs 8,500 crore through qualified institutional placement ( QIP ) |
| 2024-06-11 | Equity | $12M | Apart from Blinkit, Zomato plans to inject INR 100 crore into its subsidiary Zomato Entertainment Pvt Ltd, which oversees the company’s… |
| 2022-11-25 | Public Offering | — | Other corporations that went for large equity fundraising through fresh issues of shares include food delivery major Zomato. It raised a |
| 2022-05-07 | ESOP proceeds donation | $90M | Online food delivery platform Zomato's Founder and CEO Deepinder Goyal will be donating around USD 90 million (nearly Rs 700 crore) from… |
| 2021-11-15 | Equity | $1B | Foodtech major Zomato has revealed an ambitious plan to invest $1 billion in fresh capital into start‑ups that will help it build adjacent… |
| 2021-08-20 | Equity | $500M | Zomato’s capital raising of around USD 500 million |
| 2020-09-03 | Funding round | $250M | Zomato has roped in two new investors - Tiger Global and Kora Capital - in an ongoing funding round valuing the food ordering and… |
| 2020-04-06 | Funding round | $5M | The company has raised an additional $5 million since — a spokesperson did not respond to a request for comment. |
| 2020-01-11 | Funding round | $15M | India’s foodtech giant Zomato on Friday announced about its latest funding of $150 million from Ant Financial which is a sub-organisation… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain zomato.com --statement all --period-type all --limit 8
radar get-company-funding --domain zomato.com
radar news-overview --company zomato.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "zomato.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "zomato.com"}, timeout=120)
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

- [Anthropic Revenue](anthropic-revenue.md)
- [Zoho Revenue](zoho-revenue.md)
- [Boat Revenue](boat-revenue.md)
- [Lenskart Revenue](lenskart-revenue.md)
