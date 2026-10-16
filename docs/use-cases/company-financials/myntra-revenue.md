# Myntra Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “myntra revenue” · 590/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [myntra-revenue.json](../../examples/use-cases/myntra-revenue.json).

**Question.** What revenue and profit has Myntra reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `myntra.com` |
| Fiscal periods with figures | 14 |
| Summary | Latest reported FY2025: revenue $725.12M, net income $65.8M. YoY +16.8% (1.17× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $725.1M | $65.8M | — | $38.3M | news report |
| FY2024 | $620.8M | $37.1M | $17.1M | — | news report |
| Q4 FY2023 | $525M | $-93.8M | — | — | news report |
| FY2023 | $541.1M | $-93.9M | — | — | news report |
| FY2022 | $420.1M | $-71.6M | — | — | news report |
| FY2021 | $28 | $-5 | — | — | news report |
| FY2020 | $206.3M | $-89.3M | — | — | news report |
| FY2019 | $124.9M | $-64.7M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-05-28 | Funding round | $125M | Fashion ecommerce platform Myntra has secured Rs 1,062.5 crore ($125 million) from its Singapore-based parent company FK Myntra Holdings. |
| 2025-02-07 | Equity | $81M | Indian online fashion retailer, Myntra, has secured a substantial US $ 81 million investment from its parent company, Flipkart, as per a… |
| 2024-03-02 | Funding round | $54M | Parent company Flipkart provided $54 million in funding to fashion e-commerce company Myntra. |
| 2018-10-19 | Funding round | $16B | After sealing a $16-billion investment deal with the US-based retail giant, Flipkart’s fashion unit has started to leverage the company's… |
| 2018-03-06 | Equity | $176M | Prior to this, FK Myntra Holdings had infused $176 million in Myntra. |
| 2017-10-22 | Funding round | $6M | Myntra: Flipkart-owned fashion e-tailer Myntra business-to-business (B2B) retail arm, Myntra Jabong India Pvt. Ltd has got a working… |
| 2017-06-02 | Funding round | $130M | Funds raised: About $130 million |
| 2016-09-20 | Funding round | $5M | 2008 - $5 million, NEA-IndoUS Ventures, IDG Ventures |
| 2016-03-12 | Investment | $50M | Recently, Flipkart infused over $50 Mn (INR 338 Cr) in its online fashion portal Myntra, to boost its position in the fashion segment. |
| 2014-07-03 | Equity | $100M | Flipkart is also expected to pump $100 million into Myntra over the next few quarters. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain myntra.com --statement all --period-type all --limit 8
radar get-company-funding --domain myntra.com
radar news-overview --company myntra.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "myntra.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "myntra.com"}, timeout=120)
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

- [Paytm Revenue](paytm-revenue.md)
- [Razorpay Revenue](razorpay-revenue.md)
- [Klarna Revenue](klarna-revenue.md)
- [Ola Revenue](ola-revenue.md)
