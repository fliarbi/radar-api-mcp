# Blinkit Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “blinkit revenue” · 1,000/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [blinkit-revenue.json](../../examples/use-cases/blinkit-revenue.json).

**Question.** What revenue and profit has Blinkit reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `blinkit.com` |
| Fiscal periods with figures | 20 |
| Summary | Latest reported Q4 FY2026: revenue $1.59B. YoY +674.3% (7.74× prior period). Growth has been erratic across reported periods. Recent signals: Record revenue,… |
| Recorded funding events | 7 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q4 FY2026 | $1.6B | — | $4.4M | — | news report |
| Q3 FY2026 | $1.5B | $480k | $480k | $24.2M | news report |
| Q2 FY2026 | $11.9B ⚠ | $600k | $-18.7M | — | news report |
| Q1 FY2026 | $288M | $3M | $-18M | — | news report |
| Q4 FY2025 | $205.1M | — | $-21.4M | $-21.4M | news report |
| Q3 FY2025 | $167.9M | $-12.4M ⚠ | $960k | — | news report |
| Q2 FY2025 | $138.7M | — | $-960k | — | news report |
| Q1 FY2025 | $113M | $-360k | $-360k | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

⚠ marks a figure more than eight times this company's typical value for that metric, usually a unit or currency slip in the source report. Verify it before use.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-03-12 | Rights Issue | $54M | Eternal, the parent company of Blinkit, has infused Rs 450 crore into its quick commerce subsidiary through a rights issue, reinforcing… |
| 2025-11-26 | Equity | $72M | Eternal — the parent entity of quick commerce market leader Blinkit — has infused Rs 600 crore into the quick-commerce platform, according… |
| 2025-01-17 | Equity | $60M | Food tech giant Zomato has invested Rs 500 crore (nearly $60 million) in its quick commerce subsidiary, Blinkit, bringing its total… |
| 2024-06-11 | Equity | $36M | Zomato is set to infuse INR 300 crore of fresh capital into its quick commerce venture, Blinkit, as per a regulatory filing submitted to… |
| 2024-04-02 | Funding round | $240M | Zomato has invested around $240 million in Blinkit over the past one year. |
| 2023-10-26 | Funding round | $150M | Indian startup Blinkit – an app-based instant grocery delivery service – received an injection of $150M, before being acquired by… |
| 2022-01-21 | Funding round | $100M | BlinkIt had raised $100 million from Zomato. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain blinkit.com --statement all --period-type all --limit 8
radar get-company-funding --domain blinkit.com
radar news-overview --company blinkit.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "blinkit.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "blinkit.com"}, timeout=120)
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

- [Zerodha Revenue](zerodha-revenue.md)
- [Swiggy Revenue](swiggy-revenue.md)
- [Urban Company Revenue](urban-company-revenue.md)
- [Cred Revenue](cred-revenue.md)
