# Physicswallah Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “physicswallah revenue” · 1,000/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [physicswallah-revenue.json](../../examples/use-cases/physicswallah-revenue.json).

**Question.** What revenue and profit has Physicswallah reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `pw.live` |
| Fiscal periods with figures | 3 |
| Summary | Latest reported FY2024: revenue $232.85M, net income $—. YoY +143.2% (2.43× prior period). Recent signals: Reported a loss, Record revenue, Profitable. |
| Recorded funding events | 7 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2024 | $232.8M | $-135.7M | — | — | news report |
| FY2023 | $95.8M | — | $15.2M | $92.6M | news report |
| FY2022 | $28.1M | $11.7M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures.

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-02-24 | Venture Capital | $210 | investment firm led Physics Wallah (PW) $210 Mn Series B funding round last year. |
| 2024-12-16 | Funding round | — | Companies like Physics Wallah and Eruditus managed to secure significant capitals in the mega funding rounds. |
| 2024-09-19 | Series B | $210M | Physics Wallah said on Friday the Series B round was led by the hedge fund Hornbill Capital, a venture between China’s Orchid Asia and… |
| 2023-10-23 | Series A | $100M | The company raised $100 million in Series A funding from Westbridge and GSV Ventures at a valuation of $1.1 billion in 2022. |
| 2023-05-09 | Funding round | $12M | With an eye on strengthening its portfolio, edtech startup Physics Wallah (PW) plans to invest INR 100 Cr to further scale up its UPSC… |
| 2023-03-23 | Funding round | $10M | In June last year, PhysicsWallah became India’s 101st unicorn after raising $100 million in its first round of funding from WestBridge… |
| 2022-06-08 | Funding round | $100M | Last evening, Physics Wallah, Pandey’s ed-tech startup, raised $100 million (Rs. 750 crore) in its first formal funding round. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain pw.live --statement all --period-type all --limit 8
radar get-company-funding --domain pw.live
radar news-overview --company pw.live --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "pw.live", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "pw.live"}, timeout=120)
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

- [Urban Company Revenue](urban-company-revenue.md)
- [Cred Revenue](cred-revenue.md)
- [Groww Revenue](groww-revenue.md)
- [Oyo Revenue](oyo-revenue.md)
