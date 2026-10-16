# Zoho Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “zoho revenue” · 1,900/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [zoho-revenue.json](../../examples/use-cases/zoho-revenue.json).

**Question.** What revenue and profit has Zoho reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `zoho.com` |
| Fiscal periods with figures | 6 |
| Summary | Latest reported FY2025: revenue $1.48B, net income $382.92M. YoY +17.8% (1.18× prior period). Growth pattern is consistent across reported periods. Recent… |
| Recorded funding events | 3 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $1.5B | $382.9M | — | — | news report |
| FY2023 | $1.1B | $340.3M | $489.6M | — | news report |
| FY2022 | $805.3M | $329.9M | — | — | news report |
| FY2021 | $627.6M | $230.2M | $320.6M | — | news report |
| FY2020 | $513M | $96.1M | — | — | news report |
| FY2019 | $397M | $61.9M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures.

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2024-05-16 | Funding round | — | Sources said Zoho had submitted a proposal for a semiconductor manufacturing unit to be set up in its headquarters state of Tamil Nadu… |
| 2022-12-14 | Funding round | $10M | Zoho, a technology company, plans to invest US$10 million in its Queretaro operations center over the next five years. |
| 2016-07-27 | Funding round | $360M | The company has already invested about Rs 450 crore in its facility in Chennai and drawn up a total investment plan of Rs 3,000 crore to… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain zoho.com --statement all --period-type all --limit 8
radar get-company-funding --domain zoho.com
radar news-overview --company zoho.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "zoho.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "zoho.com"}, timeout=120)
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

- [Openai Revenue](openai-revenue.md)
- [Anthropic Revenue](anthropic-revenue.md)
- [Zomato Revenue](zomato-revenue.md)
- [Boat Revenue](boat-revenue.md)
