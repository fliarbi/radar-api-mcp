# Paytm Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “paytm revenue” · 590/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [paytm-revenue.json](../../examples/use-cases/paytm-revenue.json).

**Question.** What revenue and profit has Paytm reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `paytm.com` |
| Fiscal periods with figures | 20 |
| Summary | Latest reported Q3 FY2026: revenue $263.28M, net income $27M. YoY +20.0% (1.2× prior period). Recent signals: Profitable, Beat estimates, Reported a loss. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q3 FY2026 | $263.3M | $27M | $18.7M | — | news report |
| Q2 FY2026 | $247.3M | $2.5M | — | — | news report |
| Q1 FY2026 | $230.2M | $14.7M | $8.6M | $-22.2M | news report |
| Q4 FY2025 | $256.2M | $-65.4M | $9.7M | — | news report |
| Q3 FY2025 | $219.4M | $-42.1M | $-4.9M | — | news report |
| Q2 FY2025 | $194M | $-79.2M | $22.3M | $-37.2M | news report |
| Q1 FY2025 | $196.7M | $-100.8M | $8.6M | $8.6M | news report |
| FY2025 | $915M | $-79.6M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-06-03 | Series Funding | $1B | Digital payments major Paytm is looking at raising another round of funding of $1 billion, and is in discussion with multiple investors,… |
| 2025-07-01 | Secondary Share Sale | $248.4M | In Paytm, Antfin (Netherlands) Holding, one of the early investors in the digital payments solutions pioneers in India, is selling shares… |
| 2021-11-04 | Anchor Round | $988.2M | Paytm’s parent company One97 Communications has raised Rs 8,235 crore from anchor investors. |
| 2021-07-17 | Primary fundraise | $996M | Paytm will raise Rs 8,300 crore from a primary fundraise, and the remaining Rs 8,300 crore from a secondary sale of shares by its existing… |
| 2020-12-03 | Funding round | $8.2M | T Rowe Price Communications and Technology Fund has valued its investment in One97 Communications (operates under brand name Paytm) at USD… |
| 2020-04-27 | Series G | $100M | Paytm is looking to add an extended $100 million to its series-G round worth $1 billion, which was announced last year. |
| 2019-11-24 | Series G | $1B | Paytm said on Monday it has raised $1 billion in a new financing round as the Noida-headquartered firm, which once dominated the local… |
| 2019-03-28 | Funding round | $2B | Paytm is raising up to $2 billion from its major existing investors counting Masayoshi Son led SoftBank Vision Fund and Jack Ma’s Ant… |
| 2018-12-03 | Unspecified | $100M | I realized we needed marketing money and a 100 million dollars simply slipped in. |
| 2018-10-03 | Equity | $300M | The other significant deals were Paytm’s $300 million, |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain paytm.com --statement all --period-type all --limit 8
radar get-company-funding --domain paytm.com
radar news-overview --company paytm.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "paytm.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "paytm.com"}, timeout=120)
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

- [Mamaearth Revenue](mamaearth-revenue.md)
- [Rapido Revenue](rapido-revenue.md)
- [Razorpay Revenue](razorpay-revenue.md)
- [Myntra Revenue](myntra-revenue.md)
