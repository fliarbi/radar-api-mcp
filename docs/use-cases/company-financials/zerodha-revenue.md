# Zerodha Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “zerodha revenue” · 1,000/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [zerodha-revenue.json](../../examples/use-cases/zerodha-revenue.json).

**Question.** What revenue and profit has Zerodha reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `zerodha.com` |
| Fiscal periods with figures | 4 |
| Summary | Latest reported FY2024: revenue $1B, net income $564M. YoY +53.3% (1.53× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 4 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2024 | $1B | $564M | — | — | news report |
| FY2023 | $655.1M | $282.5M | — | — | news report |
| FY2022 | $516M | $216M | — | — | news report |
| FY2020 | $131.2M | $53M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures.

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-01-14 | Venture Capital | — | In October 2024, fintech unicorn Zerodha launched FLOSS/fund to support open-source projects globally with annual funding of $1 Mn. |
| 2024-10-17 | Funding round | — | We are excited to announce the launch of a dedicated fund aimed at providing financial assistance to Free/Libre and Open Source Software… |
| 2023-08-10 | Venture Capital | $12 | Zerodha has committed Rs 1,000 crore ($120.9 million) for its startup fund Rainmatter in a structure that will allow it to remain invested… |
| 2020-06-22 | Equity | — | It is expected to pay-out around Rs 60-65 crores to 700 employees. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain zerodha.com --statement all --period-type all --limit 8
radar get-company-funding --domain zerodha.com
radar news-overview --company zerodha.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "zerodha.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "zerodha.com"}, timeout=120)
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

- [Stripe Revenue](stripe-revenue.md)
- [Meesho Revenue](meesho-revenue.md)
- [Swiggy Revenue](swiggy-revenue.md)
- [Blinkit Revenue](blinkit-revenue.md)
