# Makemytrip Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “makemytrip revenue” · 320/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [makemytrip-revenue.json](../../examples/use-cases/makemytrip-revenue.json).

**Question.** What revenue and profit has Makemytrip reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `makemytrip.com` |
| Fiscal periods with figures | 20 |
| Summary | Latest reported Q3 FY2026: revenue $295.7M, net income $7.3M, EPS $0.43. YoY +40.1% (1.4× prior period). Growth has been erratic across reported periods.… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q3 FY2026 | $295.7M | $7.3M | — | $50.7M | news report |
| Q2 FY2026 | $229.3M | $-5.7M | — | — | news report |
| Q1 FY2026 | $268.9M | $25.8M | — | — | news report |
| Q4 FY2025 | $245.5M | $29.2M | — | — | news report |
| Q3 FY2025 | $211M | $17.9M | — | $46M | news report |
| Q2 FY2025 | $211M | $17.9M | — | $47.3M | news report |
| Q1 FY2025 | $254M | $21M | — | $39.1M | news report |
| Q4 FY2024 | $202.9M | $15.2M | — | $44.7M | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-06-17 | Convertible Note | $1.2B | Separately, MakeMyTrip plans to convert senior notes, set at a principal amount of $1.25 billion, with an option for initial purchasers to… |
| 2021-02-06 | Convertible Notes | $200M | The company, in a press statement, revealed that it will be using the capital from the notes for business operations and for employee… |
| 2019-07-04 | Funding round | $4.2M | Gurugram-based MakeMyTrip received an additional Rs 34.68 crore from its Mauritius-based holding entity, according to the RoC filings… |
| 2019-04-12 | Funding round | $12M | Online travel major MakeMyTrip’s Indian arm MakeMyTrip India Pvt Ltd has received Rs 100 crore from the Mauritius-based entity. |
| 2017-06-26 | Funding round | $132M | The group also invested an additional $132 million in MakeMyTrip in May 2017, as part of an equity funding round. |
| 2017-05-03 | Funding round | $330M | Online travel company MakeMyTrip on Wednesday said it was raising $330 million (Rs 2,110 crore) through a share sale to existing investors… |
| 2016-09-20 | Funding round | $13M | 2006 - $13 million Helion Venture Partners, Sierra Partners and SAIF Partners |
| 2016-01-11 | Funding round | $180M | This did not stop MakeMyTrip, one of the earliest Indian dotcom companies that went public in 2010 on the Nasdaq, from raising investment… |
| 2014-09-23 | Venture Capital | — | NASDAQ-listed online travel services firm MakeMyTrip (MMT) has recently floated a $15 million (around Rs 90 crore) innovation fund, which… |
| 2014-03-11 | Public Offering | $75M | MakeMyTrip raising $75 Mn in fresh capital |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain makemytrip.com --statement all --period-type all --limit 8
radar get-company-funding --domain makemytrip.com
radar news-overview --company makemytrip.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "makemytrip.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "makemytrip.com"}, timeout=120)
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

- [Licious Revenue](licious-revenue.md)
- [Pine Labs Revenue](pine-labs-revenue.md)
- [Revolut Revenue](revolut-revenue.md)
- [Cars24 Revenue](cars24-revenue.md)
