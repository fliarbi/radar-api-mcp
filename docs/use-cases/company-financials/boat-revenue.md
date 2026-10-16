# Boat Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “boat revenue” · 1,600/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [boat-revenue.json](../../examples/use-cases/boat-revenue.json).

**Question.** What revenue and profit has Boat reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `boat-lifestyle.com` |
| Fiscal periods with figures | 6 |
| Summary | Latest reported FY2025: revenue $371.76M, net income $7.2M. YoY -0.8% (0.99× prior period). Recent signals: Profitable, Reported a loss, Record revenue. |
| Recorded funding events | 9 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $371.8M | $7.2M | $17M | — | news report |
| FY2024 | $374.6M | $-6.4M | — | — | news report |
| FY2023 | $480M | — | — | — | news report |
| FY2022 | $344.8M | $8.2M | — | — | news report |
| FY2021 | $183.7M | $9.4M | $15.3M | $15.3M | news report |
| FY2020 | $84.1M | $5.9M | $9M | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2024-02-02 | Funding round | $177M | To date, investors including Qualcomm Ventures, Warburg Pincus, InnoVen Capital, Navi Technologies, and Fireside Ventures have contributed… |
| 2022-10-28 | Private Placement | $60M | Wearables startup boAt on Friday deferred its public share sale plans and raised $60 million ( ₹500 crore) from private investors instead. |
| 2021-06-18 | Venture | $100M | Some of the major Indian D2C startups to raise funding in Q1 2021 include consumer electronics tech startup boAt, which raised $100 Mn in… |
| 2021-04-16 | Funding round | $6.7M | the amount of investment is speculated to be Rs 50 crores (~$6.7 million). |
| 2021-01-06 | Funding round | $100M | Consumer tech products brand boAt on Wednesday said it has raised USD 100 million (about Rs 731.6 crore) in funding from an affiliate of… |
| 2020-09-01 | Debt | $2.4M | Before that, boAt had raised INR 20 Cr (around $2.9 Mn) in venture debt from Sachin Bansal’s BAC Acquisitions. |
| 2019-07-17 | Venture Debt | $2.4M | Flipkart co-founder Sachin Bansal, after making multiple investments in venture debt post his exit from Flipkart after acquisition by… |
| 2019-01-29 | Equity | $7.2M | We invested ₹6 crore in Boat, a consumer electronics start-up, which notched up ₹100 crore in revenue as of March 2018 and was profitable… |
| 2018-05-03 | Funding round | $720k | Audio products maker boAt today said it has raised Rs 6 crore from Fireside Ventures and will use the funds towards marketing and product… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain boat-lifestyle.com --statement all --period-type all --limit 8
radar get-company-funding --domain boat-lifestyle.com
radar news-overview --company boat-lifestyle.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "boat-lifestyle.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "boat-lifestyle.com"}, timeout=120)
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

- [Zoho Revenue](zoho-revenue.md)
- [Zomato Revenue](zomato-revenue.md)
- [Lenskart Revenue](lenskart-revenue.md)
- [Databricks Revenue](databricks-revenue.md)
