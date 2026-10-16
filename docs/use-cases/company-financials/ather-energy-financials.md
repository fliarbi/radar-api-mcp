# Ather Energy Financials: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “ather energy financials” · 170/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [ather-energy-financials.json](../../examples/use-cases/ather-energy-financials.json).

**Question.** What revenue and profit has Ather Energy reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `atherenergy.com` |
| Fiscal periods with figures | 16 |
| Summary | Latest reported FY2026: revenue $440.61M, net income $—. YoY +62.8% (1.63× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q4 FY2026 | $145.7M | $-12M | $-3.6M | $-3.6M | news report |
| Q3 FY2026 | $119.5M | $-10.2M | $-3.6M | $-3.6M | news report |
| Q2 FY2026 | $107.9M | $-18.5M | $10.8M | — | news report |
| Q1 FY2026 | $77.4M | $-21.4M | — | — | news report |
| FY2026 | $440.6M | $-62.1M | $-30.8M | $-3.6M | news report |
| Q4 FY2025 | $81.1M | $-28.1M | $-20.7M | — | news report |
| Q2 FY2025 | $112.9M | $-18.5M | $-15.6M | — | news report |
| Q1 FY2025 | $81.1M | $28.1M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-11-12 | Block Deal | $66.1M | National Investment and Infrastructure Fund II is likely to sell up to 2.34% of its existing total equity stake in Ather Energy Ltd… |
| 2025-04-26 | IPO | $315.1M | The public offering, which will open on April 28th, will include a fresh issue of Rs 2,626 crore and an offer for sale of up to 1.1 crore… |
| 2025-01-11 | Funding round | $630M | Ather Energy has secured approximately $630 million in total funding through various rounds. |
| 2024-06-26 | Funding round | $240M | The investment will be more than ₹2,000 crore, generating around 4000 jobs, Fadnavis says in a post on X. |
| 2024-02-02 | Equity Investment | $16.8M | Pawan Munjal-led Hero MotoCorp will buy an additional 3% stake in Bengaluru-based EV startup Ather Energy for up to INR 140 Cr ($16.8 Mn). |
| 2023-12-16 | Funding round | $16.8M |  |
| 2023-09-06 | Rights Issue | $108M | India's Ather Energy has raised Rs 9oo crore ($108.27 million) from its shareholders Hero MotoCorp and Singapore's GIC through a rights… |
| 2023-06-28 | Funding round | $103.8M | Ather Energy, a prominent Indian electric scooter manufacturer, has confirmed a staggering Rs 865 crore investment in the Shendra phase of… |
| 2023-05-08 | Funding round | $33M | Ather is set to receive about Rs 275 crore. |
| 2023-01-08 | Funding round | $170M | We’ve raised a total of $170-180 million in the recently-concluded funding round and raised $50 million last October. With this, our… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain atherenergy.com --statement all --period-type all --limit 8
radar get-company-funding --domain atherenergy.com
radar news-overview --company atherenergy.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "atherenergy.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "atherenergy.com"}, timeout=120)
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

- [Practo Revenue](practo-revenue.md)
- [Acko Revenue](acko-revenue.md)
- [Inmobi Revenue](inmobi-revenue.md)
- [Shiprocket Revenue](shiprocket-revenue.md)
