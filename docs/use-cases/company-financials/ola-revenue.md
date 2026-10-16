# Ola Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “ola revenue” · 480/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [ola-revenue.json](../../examples/use-cases/ola-revenue.json).

**Question.** What revenue and profit has Ola reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `olacabs.com` |
| Fiscal periods with figures | 1 |
| Summary | Latest reported FY2023: revenue $256.2M, net income $—. YoY +58.0% (1.58× prior period). Recent signals: Reported a loss, Record revenue. |
| Recorded funding events | 9 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2023 | $256.2M | $-129.8M | $30M | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures.

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2022-02-22 | Series J | $18M | Ola Cabs has raised Rs 150 crore in its ongoing Series J round from Axis Growth Avenues AIF and Arrow Multi-Asset Fund. |
| 2019-03-19 | Funding round | $300M | South Korean automaker, Hyundai along with Kia Motors, will be investing $300 million (Rs. 2,056 crores) into ride hailing giant Ola Cabs. |
| 2018-01-10 | Funding round | $1.1B | SoftBank Group and Tencent Holdings-led $1.1-billion investment in Bengaluru-based taxi-hailing service provider Ola cabs |
| 2016-10-06 | Funding round | $210M | and a $210 million funding round in taxi-hailing app Ola Cabs. |
| 2015-11-18 | Series F | $500M | Ola Cabs, the ride-hailing company giving Uber a run for its money in India, announced today that it has closed a $500 million Series F… |
| 2015-09-15 | Funding round | $500M | Ola Cabs, the Indian ride-sharing app that shares a major investor with Alibaba, has sealed $225 million USD of a planned $500 million… |
| 2015-03-20 | Funding round | $400M | Indian taxi aggregator, Ola Cabs, who is backed by SoftBank among others, is in talks with Russian Billionaire Yuri Milner’s investment… |
| 2014-10-28 | Funding round | $210M | SoftBank Internet and Media, Inc ('SIMI') and ANI Technologies Pvt Ltd (better known as 'Ola Cabs' or 'Ola') on Monday announced a… |
| 2013-11-15 | Funding round | — | Online taxi aggregator Ola Cabs has raised a second round of funding from Matrix Partners India and existing investor Tiger Global… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain olacabs.com --statement all --period-type all --limit 8
radar get-company-funding --domain olacabs.com
radar news-overview --company olacabs.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "olacabs.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "olacabs.com"}, timeout=120)
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

- [Myntra Revenue](myntra-revenue.md)
- [Klarna Revenue](klarna-revenue.md)
- [Phonepe Revenue](phonepe-revenue.md)
- [Indiamart Revenue](indiamart-revenue.md)
