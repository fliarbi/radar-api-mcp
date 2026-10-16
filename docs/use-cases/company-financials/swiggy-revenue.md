# Swiggy Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “swiggy revenue” · 880/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [swiggy-revenue.json](../../examples/use-cases/swiggy-revenue.json).

**Question.** What revenue and profit has Swiggy reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `swiggy.com` |
| Fiscal periods with figures | 20 |
| Summary | Latest reported FY2027: revenue $1.06B. YoY +18.0% (1.18× prior period). Recent signals: Reported a loss, Record revenue, Beat estimates. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2027 | $1.1B | — | — | — | news report |
| Q4 FY2026 | $786.6M | $-97.8M | $-81.1M | — | news report |
| Q3 FY2026 | $737.9M | $-127.8M | $-85.4M | — | news report |
| Q2 FY2026 | $667.3M | $-131M | $-83.4M | $-95.9M | news report |
| Q1 FY2026 | $595.3M | $-143.6M | — | — | news report |
| Q4 FY2025 | $529.2M | $-129.7M | $25.4M | — | news report |
| Q3 FY2025 | $479.2M | $-95.9M | $22.1M | $-87.1M | news report |
| Q2 FY2025 | $442.3M | $-75M | $-40.9M | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-11-19 | QIP | $1.2B | Swiggy has recently cleared a fundraising plan of up to Rs 10,000 crore, through a combination of public or private offerings to shore up… |
| 2024-11-06 | Equity | $539.9M | Swiggy plans to raise Rs 4,499 crore in primary capital, while shares worth Rs 6,828 crore are being put up on offer for sale by existing… |
| 2022-04-19 | Venture | $1.3B | Bangalore-based Swiggy is a food delivery platform that brings food from neighborhood restaurants directly to customers’ doors. |
| 2022-01-31 | Series-K | $700M | Food delivery platform, Swiggy, headlined this month’s funding news as it raised $700 Mn in Series-K funding round led by US asset manager… |
| 2021-12-02 | Funding round | $8.4M | Swiggy said on Thursday that she will invest $70 crore (closed Rs 5,250 crore) in her grocery goods supply unit instamart. |
| 2021-10-07 | Equity | $600M | According to multiple media reports, the company is in talks with Invesco to raise up to $600 million as a part of a fresh funding round,… |
| 2021-07-19 | Funding round | $1.2B | Swiggy on Tuesday said it has closed a fundraise of $1.25 billion (Rs 9,344 crore) led by new investor SoftBank Vision Fund 2 and existing… |
| 2021-04-05 | Funding round | $800M | Food delivery platform Swiggy has raised around $800 million (about Rs 5,863 crore) in a new funding round. |
| 2021-02-12 | Unicorn Fundraising | — | Restaurant aggregator Swiggy is in advanced talks to raise $700-$800 million funding round led by sovereign wealth funds Qatar Investment… |
| 2020-09-10 | Funding round | $1.6B | Swiggy, India’s largest online food ordering and delivery platform, has received about $1.64 billion from investors. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain swiggy.com --statement all --period-type all --limit 8
radar get-company-funding --domain swiggy.com
radar news-overview --company swiggy.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "swiggy.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "swiggy.com"}, timeout=120)
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

- [Meesho Revenue](meesho-revenue.md)
- [Zerodha Revenue](zerodha-revenue.md)
- [Blinkit Revenue](blinkit-revenue.md)
- [Urban Company Revenue](urban-company-revenue.md)
