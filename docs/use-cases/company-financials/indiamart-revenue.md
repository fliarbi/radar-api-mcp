# Indiamart Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “indiamart revenue” · 480/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [indiamart-revenue.json](../../examples/use-cases/indiamart-revenue.json).

**Question.** What revenue and profit has Indiamart reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `indiamart.com` |
| Fiscal periods with figures | 20 |
| Summary | Latest reported FY2026: revenue $188.28M. YoY +13.0% (1.13× prior period). Recent signals: Beat estimates, Profitable. |
| Recorded funding events | 2 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q1 FY2026 | $44.6M | $18.5M | $16.2M | — | news report |
| FY2026 | $188.3M | — | $62.4M | — | news report |
| Q4 FY2025 | $48.5M | $6M | $15.9M | — | news report |
| Q3 FY2025 | $42.5M | $14.5M | $17.3M | $19.1M | news report |
| Q2 FY2025 | $41.7M | $16.2M | $16.2M | — | news report |
| Q1 FY2025 | $39.8M | $13.7M | $14M | — | news report |
| FY2025 | $166.6M | $66.1M | — | — | news report |
| Q4 FY2024 | $37.8M | $12M | $10.8M | $10.8M | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2021-03-01 | Qualified Institutions Placement | — | Shardul Amarchand Mangaldas & Co. advised IndiaMART InterMESH Limited on its qualified institutions placement. The deal was valued at ₹… |
| 2016-03-09 | Funding round | $18M | Ecommerce player IndiaMART has raised an estimated Rs 150 crore in a new round of financing led by Amadeus Capital Partners to scale up… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain indiamart.com --statement all --period-type all --limit 8
radar get-company-funding --domain indiamart.com
radar news-overview --company indiamart.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "indiamart.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "indiamart.com"}, timeout=120)
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

- [Ola Revenue](ola-revenue.md)
- [Phonepe Revenue](phonepe-revenue.md)
- [Ola Electric Revenue](ola-electric-revenue.md)
- [Unacademy Revenue](unacademy-revenue.md)
