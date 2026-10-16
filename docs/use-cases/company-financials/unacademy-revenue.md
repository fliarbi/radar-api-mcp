# Unacademy Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “unacademy revenue” · 480/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [unacademy-revenue.json](../../examples/use-cases/unacademy-revenue.json).

**Question.** What revenue and profit has Unacademy reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `unacademy.com` |
| Fiscal periods with figures | 7 |
| Summary | Latest reported FY2025: revenue $99.16M, net income $—. YoY -16.4% (0.84× prior period). Recent signals: Reported a loss, Record revenue. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $99.2M | $-52.3M | — | — | news report |
| FY2024 | $118.6M | $-75.7M | $-58.7M | — | news report |
| FY2023 | $150M | — | — | — | news report |
| FY2022 | $86.3M | — | — | — | news report |
| FY2021 | $47.7M | — | — | — | news report |
| FY2020 | $103.2M | $-36M | — | — | news report |
| FY2019 | $1.4M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2021-08-01 | Series H | $440M | Indian online learning platform Unacademy has raised $440 million in a new financing round as investors double down on the South Asian… |
| 2021-04-20 | Secondary | $50M | Tiger, Dragoneer, Steadview and General Atlantic had acquired $50 million worth of shares from existing investors at the same valuation ~… |
| 2020-09-02 | Series F | $150M | Bengaluru based education startup-Unacademy, is one of them as it now sits at a $1.5 billion valuation, after receiving $150 million in a… |
| 2020-06-05 | Funding round | $150M | Unacademy is expected to raise up to $150 million (about Rs 1,130 crore at current exchange rate), but the amount could be higher… |
| 2020-02-19 | Funding round | $110M | Seven months after raising $50 million in a Series D round led by Steadview, Unacademy has now scored $110 million in a fresh round led by… |
| 2019-06-26 | Series D | $50M | Unacademy which is an Education Technology startup has now secured $50 Million in the funding round of Series D led by the Hong Kong-based… |
| 2019-04-13 | Funding round | $300k | Unacademy: Flipkart CEO Kalyan Krishnamurthy has invested $0.3 million in edtech startup Unacademy. |
| 2018-07-16 | Series C | $21M | Edtech startup Unacademy has raised $21 million Series C round led by Sequoia Capital, Nexus Ventures, SAIF Partners. The round was also… |
| 2018-05-05 | Funding | $570k | Unacademy has raised $0.57 million from existing investors - Sequoia Capital, Saif Partners, Nexus Venture Partners, and Blume Ventures. |
| 2017-09-13 | Series B | $11.5M | Online learning platform Unacademy has raised $11.5 million in a Series B financing led by Sequoia Capital India and SAIF Partners. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain unacademy.com --statement all --period-type all --limit 8
radar get-company-funding --domain unacademy.com
radar news-overview --company unacademy.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "unacademy.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "unacademy.com"}, timeout=120)
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

- [Indiamart Revenue](indiamart-revenue.md)
- [Ola Electric Revenue](ola-electric-revenue.md)
- [Freshworks Revenue](freshworks-revenue.md)
- [Delhivery Revenue](delhivery-revenue.md)
