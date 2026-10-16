# Stripe Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “stripe revenue” · 390/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [stripe-revenue.json](../../examples/use-cases/stripe-revenue.json).

**Question.** What revenue and profit has Stripe reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `stripe.com` |
| Fiscal periods with figures | 4 |
| Summary | Latest reported FY2024: revenue $500M. Growth has been erratic across reported periods. Recent signals: Reported a loss, Record revenue, Profitable. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2024 | $500M | — | — | — | news report |
| FY2022 | $2.8B | — | — | — | news report |
| FY2020 | $7.4B | $-138.2M | — | — | news report |
| FY2019 | $800.4M | $46.9M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-03-26 | Seed | $2M | In 2011, Sequoia Capital invested $2 million in Stripe’s seed round at a valuation of roughly $20 million. |
| 2025-03-12 | Equity | — | Stripe secured funding at a $91.5 billion valuation |
| 2024-08-30 | Series?? | $1.8B | When the funding came together this March, Thrive invested $1.8 billion—the largest check Thrive had ever written and about $1 billion… |
| 2023-08-10 | Equity | $6.8B | despite a $6.8 billion raise by payments processing company Stripe |
| 2023-03-15 | Series I | $6.5B | Digital payments company Stripe announced Wednesday that it raised over $6.5 billion in Series I funding to value the company at $50… |
| 2022-04-12 | Venture Capital | — | The Frontier fund, as it is called, has received funding from some of the world’s largest tech corporations, including Meta Platforms… |
| 2021-08-10 | Raise | $600M | Big deals included a $3.4 billion raise by Robinhood, a $600 million raise by Stripe, and $500 million raises by Better, ServiceTitan, and… |
| 2021-06-14 | Funding round | $1B | According to The Wall Street Journal, Shopify, Capital Group, Sequoia Capital, Silver Lake, and others invested about $1 billion USD in… |
| 2021-03-15 | Series H | $600M | To further accelerate its expansion, Stripe announced today it has raised a whopping $600 million Series H funding round to “invest a ton… |
| 2020-07-29 | Equity | $600M | Payment platform Stripe raised $600 million in April, and grocery delivery service Instacart has raised $325 billion in multiple funding… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain stripe.com --statement all --period-type all --limit 8
radar get-company-funding --domain stripe.com
radar news-overview --company stripe.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "stripe.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "stripe.com"}, timeout=120)
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

- [Databricks Revenue](databricks-revenue.md)
- [Flipkart Revenue](flipkart-revenue.md)
- [Meesho Revenue](meesho-revenue.md)
- [Zerodha Revenue](zerodha-revenue.md)
