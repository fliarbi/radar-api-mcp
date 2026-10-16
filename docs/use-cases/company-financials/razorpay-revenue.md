# Razorpay Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “razorpay revenue” · 590/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [razorpay-revenue.json](../../examples/use-cases/razorpay-revenue.json).

**Question.** What revenue and profit has Razorpay reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `razorpay.com` |
| Fiscal periods with figures | 7 |
| Summary | Latest reported FY2025: revenue $453.96M, net income $—. YoY +82.9% (1.83× prior period). Recent signals: Reported a loss, Record revenue, Profitable. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $454M | $-145.1M ⚠ | — | — | news report |
| FY2024 | $248.2M | $4.2M | — | — | news report |
| FY2023 | $273.5M | $8.6M ⚠ | — | — | news report |
| FY2022 | $177.7M | $876k | — | — | news report |
| FY2021 | $101.3M | $840k | — | — | news report |
| FY2020 | $61.1M | $-738k | — | — | news report |
| FY2019 | $24.3M | $-391.2k | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

⚠ marks a figure more than eight times this company's typical value for that metric, usually a unit or currency slip in the source report. Verify it before use.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2022-11-14 | Funding round | $535M | Razorpay, which raised over $535 million last year |
| 2022-05-10 | Liquidity Program (ESOP) | $75M | Fintech Unicorn Razorpay with Bengaluru headquarters announced the fourth and largest liquidity program for the employee stock ownership… |
| 2022-02-07 | Funding round | $535M | Razorpay Software Pvt Ltd drew in $535 million from three investment rounds. |
| 2021-12-19 | Series F | $375M | Business-focused payment gateway and neo banking platform Razorpay has raised $375 million in its Series F round led by Lone Pine Capital,… |
| 2021-09-20 | Strategic investment | — | Razorpay said on Monday it has received a “strategic investment” from the venture arm of the American enterprise giant. |
| 2021-04-18 | Series E | $160M | Razorpay said on Monday it has raised $160 million in its Series E financing round that valued the startup at $3 billion, up from “a… |
| 2021-02-25 | Funding round | $200M | digital payments startup Razorpay is in talks with several investors, including existing investor GIC, to raise up to $200 million (about… |
| 2020-10-11 | Series D | $100M | Bangalore-headquartered Razorpay, one of a handful of Indian fintech startups that has demonstrated accelerated growth in recent years,… |
| 2020-08-05 | Funding round | $80M | Also, payments startup Razorpay is in talks to raise up to $80 million (Rs 600 crore) in a round of funding co-led by existing investor… |
| 2020-01-08 | Equity | $75M | Bengalurubased B2B payment service provider Razorpay raised $75 million earlier this year from Ribbit Capital and Sequoia Capital. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain razorpay.com --statement all --period-type all --limit 8
radar get-company-funding --domain razorpay.com
radar news-overview --company razorpay.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "razorpay.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "razorpay.com"}, timeout=120)
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

- [Rapido Revenue](rapido-revenue.md)
- [Paytm Revenue](paytm-revenue.md)
- [Myntra Revenue](myntra-revenue.md)
- [Klarna Revenue](klarna-revenue.md)
