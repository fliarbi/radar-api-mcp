# Databricks Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “databricks revenue” · 390/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [databricks-revenue.json](../../examples/use-cases/databricks-revenue.json).

**Question.** What revenue and profit has Databricks reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `databricks.com` |
| Fiscal periods with figures | 3 |
| Summary | Latest reported Q4 FY2025: revenue $5.4B. YoY +80.0% (1.8× prior period). Recent signals: Record revenue. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q4 FY2025 | $5.4B | — | — | — | news report |
| Q4 FY2024 | $3B | — | — | — | news report |
| FY2024 | $1.6B | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-12-16 | Series L | $4B | Databricks has announced a significant $4 billion Series L funding round, elevating its valuation to $134 billion. |
| 2025-08-25 | Series K | $1B | It is nearing a funding round of more than $1-billion from existing investors including Thrive Capital, Insight Partners and Andreessen… |
| 2024-12-17 | Series J | $10B | Databricks, the data analytics platform, has raised $10 billion in a funding round that values the company at $62 billion (up from $43… |
| 2024-08-22 | Funding round | $6B | Databricks, a data analytics platform, has secured $6 billion to accelerate its growth and strengthen its position in the data analytics… |
| 2024-04-23 | Funding round | $7B | Further megadeals involved Anthropic (30 billion), Waymo (16 billion), xAI (7.5 billion in equity and 12.5 billion in debt), Databricks (7… |
| 2023-09-14 | Series I | $500M | Databricks on Thursday raised $500 million in new financing |
| 2021-12-11 | Venture Capital | — | Its first fund, the Lakehouse Fund, will focus on early- and growth-stage companies extending the lakehouse ecosystem or using the… |
| 2021-08-31 | Funding round | $1.6B | his eight-year-old startup plans to use its new $1.6 billion in funding to supercharge its 'data lakehouse' strategy |
| 2021-02-01 | Funding round | $1B | The latest funding round of US$1 billion was led by the investment firm Franklin Templeton and includes Amazon Web Services, the Google… |
| 2020-02-18 | Equity | $400M | US$400m each raised by Databricks |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain databricks.com --statement all --period-type all --limit 8
radar get-company-funding --domain databricks.com
radar news-overview --company databricks.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "databricks.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "databricks.com"}, timeout=120)
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

- [Boat Revenue](boat-revenue.md)
- [Lenskart Revenue](lenskart-revenue.md)
- [Flipkart Revenue](flipkart-revenue.md)
- [Stripe Revenue](stripe-revenue.md)
