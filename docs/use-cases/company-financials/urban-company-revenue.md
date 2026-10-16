# Urban Company Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “urban company revenue” · 720/month India · 20/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [urban-company-revenue.json](../../examples/use-cases/urban-company-revenue.json).

**Question.** What revenue and profit has Urban Company reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `urbancompany.com` |
| Fiscal periods with figures | 13 |
| Summary | Latest reported Q3 FY2026: revenue $45.92M, net income $—. YoY +0.7% (1.01× prior period). Growth pattern is consistent across reported periods. Recent… |
| Recorded funding events | 8 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q3 FY2026 | $45.9M | $-2.6M | $-2M | — | news report |
| Q2 FY2026 | $45.6M | $-7.1M | $-4.2M | — | news report |
| Q3 FY2025 | $45.6M | $-7.1M | $-4.3M | — | news report |
| Q2 FY2025 | $33.8M | $832.8k | — | — | news report |
| Q1 FY2025 | $11.5M | — | — | — | news report |
| FY2025 | $137.3M | $28.8M | — | $137.6M | news report |
| Q1 FY2024 | $33.7M | $1.4M | — | $1.4M | news report |
| FY2024 | $99.2M | $-11.2M | $13.9M | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-12-25 | IPO | $215M | Through the IPO, it raised around $215 million, listing at a 57% premium to its issue price of ₹103. |
| 2025-08-26 | Funding round | $22.8M | The Urban Company IPO has been in the news for its high grey market premium and strong investor demand. The share price has increased from… |
| 2025-04-12 | IPO | $63.4M | Urban Company’s board approved a primary fundraise of ₹528 crore via an upcoming IPO. |
| 2024-08-05 | Funding round | $50M | Last month, when Dharana Capital invested $50 million in Urban Company |
| 2021-12-12 | ESOP Sale | $7.3M | Urban Company recently concluded its fourth and largest ESOP sale programme worth USD 7.3 million. |
| 2021-08-17 | Funding round | $376M | Urban Company has raised $376M in funding from investors like Accel , Elevation Capital and Bessemer Venture Partners. |
| 2021-06-01 | Series F | $255M | Home services marketplace Urban Company said on Wednesday it has raised $255 million in a new financing round and confirmed a valuation of… |
| 2020-03-25 | Funding round | $180k | Urban Company, its founders, investors and employees have committed Rs 1.5 crore towards this fund till date. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain urbancompany.com --statement all --period-type all --limit 8
radar get-company-funding --domain urbancompany.com
radar news-overview --company urbancompany.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "urbancompany.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "urbancompany.com"}, timeout=120)
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

- [Swiggy Revenue](swiggy-revenue.md)
- [Blinkit Revenue](blinkit-revenue.md)
- [Cred Revenue](cred-revenue.md)
- [Physicswallah Revenue](physicswallah-revenue.md)
