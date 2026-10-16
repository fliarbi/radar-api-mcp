# Phonepe Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “phonepe revenue” · 480/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [phonepe-revenue.json](../../examples/use-cases/phonepe-revenue.json).

**Question.** What revenue and profit has Phonepe reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `phonepe.com` |
| Fiscal periods with figures | 11 |
| Summary | Latest reported FY2025: revenue $853.8M, net income $—. YoY +40.5% (1.41× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $853.8M | $-206.4M ⚠ | — | — | news report |
| Q2 FY2024 | $302.2M | — | — | — | news report |
| FY2024 | $607.7M | $23.6M | — | — | news report |
| FY2023 | $349.7M | $23.6M | $19.1M | $-210.6M | news report |
| FY2022 | $197.5M | — | $80.5M | — | news report |
| FY2021 | $690M | — | — | $106.6M | news report |
| FY2020 | $51.2M | — | — | — | news report |
| FY2019 | $29.5M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

⚠ marks a figure more than eight times this company's typical value for that metric, usually a unit or currency slip in the source report. Verify it before use.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-10-30 | Secondary Transaction | $600M | General Atlantic has invested about $600 million in PhonePe through a secondary transaction |
| 2024-10-22 | Funding round | $336M | PhonePe has invested more than Rs 2,800 crore in infrastructure capital expenditure, focusing on servers and data centers across various… |
| 2024-02-08 | Series D | $623M | Reportedly, PhonePe and Udaan secured the highest funding in 2023, raising $623 million and $377 million in Series D and Series E funding… |
| 2023-09-03 | Equity | $700M | During the first half of 2023, Flipkart received $700 million related to new rounds of equity funding for its subsidiary PhonePe, said the… |
| 2023-01-20 | Equity | $350M | Fintech company PhonePe raised $350 million at a pre-money valuation of $12 billion from private equity firm General Atlantic with… |
| 2021-08-21 | Funding round | $350M | Phonepe on Thursday said it has raised USD 350 million at a valuation of USD 12 billion in a funding round led by private equity firm… |
| 2021-03-29 | Equity | — | Established mobile payment firms including PhonePe, Viva Republica and Voyager Innovations, which owns PayMaya in the Philippines, closed… |
| 2021-01-26 | Funding round | $807M | Startups that attracted maximum funding in 2020 include Zomato (USD 1.02 billion), Byju’s (USD 922 million), Phonepe (USD 807 million),… |
| 2020-04-28 | Equity | $60M | In February, the Walmart-controlled digital payments firm had received about $60 million (nearly Rs 430 crore) from the entity. |
| 2019-12-10 | Funding round | $70.3M | Flipkart-owned digital payments company PhonePe received fresh funding of about Rs 585.66 crore from its parent firm, according to… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain phonepe.com --statement all --period-type all --limit 8
radar get-company-funding --domain phonepe.com
radar news-overview --company phonepe.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "phonepe.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "phonepe.com"}, timeout=120)
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

- [Klarna Revenue](klarna-revenue.md)
- [Ola Revenue](ola-revenue.md)
- [Indiamart Revenue](indiamart-revenue.md)
- [Ola Electric Revenue](ola-electric-revenue.md)
