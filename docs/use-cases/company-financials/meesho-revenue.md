# Meesho Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “meesho revenue” · 880/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [meesho-revenue.json](../../examples/use-cases/meesho-revenue.json).

**Question.** What revenue and profit has Meesho reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `meesho.com` |
| Fiscal periods with figures | 13 |
| Summary | Latest reported Q3 FY2026: revenue $422.11M, net income $—. YoY +31.0% (1.31× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q3 FY2026 | $422.1M | $-58.9M | $-57.5M | — | news report |
| Q1 FY2026 | $300.5M | — | — | — | news report |
| FY2025 | $1.1B | $-469.8M | — | — | news report |
| Q2 FY2024 | $4.2B | $-169.2M | $-8M | — | news report |
| FY2024 | $913.8M | $-6.4M | — | — | news report |
| 1H FY2024 | $422.5M | $-16.9M | — | — | news report |
| Q4 FY2023 | $403.1M | $-389.7M | — | — | news report |
| FY2023 | $688.2M | $-201M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-10-19 | Equity | $510M | Bengaluru-based online marketplace Meesho has filed its updated draft red herring prospectus (UDRHP) with the SEBI to raise up to ₹4,250… |
| 2025-03-18 | Undisclosed | — | In January, ecommerce major Meesho reportedly closed a $250-270 Mn funding round with participation from new investors including Tiger… |
| 2024-05-09 | Funding round | $275M | Meesho, a leading e-commerce startup in India with about 150 million transacting users, has secured $275 million in a new funding round,… |
| 2022-09-29 | Funding round | $192M | Internet commerce firm Meesho, operated by Fashnear Technologies, has received $192 million from its parent entity, Meesho Inc. |
| 2021-09-30 | Funding round | $570M | Meesho, India’s fastest growing internet commerce platform, today, announced its latest round of funding of USD 570 Million led by… |
| 2021-06-04 | Funding round | $300M | and led a USD 300 million (about Rs 2,201.7 crore) funding round in Meesho earlier this year. |
| 2021-04-04 | Funding round | $300M | Social commerce platform Meesho on Monday said it has raised USD 300 million (about Rs 2,201.7 crore) in a funding round led by SoftBank… |
| 2021-02-12 | Funding round | $250M | SoftBank has given the term sheet and if nothing goes wrong from here then the funding will be announced in a few weeks from now. |
| 2020-12-08 | Funding round | $150M | Social commerce major Meesho is in advanced talks to raise up to $150 million in a fresh round, said three people aware of the details of… |
| 2020-04-21 | Investment | $15M | Facebook has invested around $15 million each in these two startups. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain meesho.com --statement all --period-type all --limit 8
radar get-company-funding --domain meesho.com
radar news-overview --company meesho.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "meesho.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "meesho.com"}, timeout=120)
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

- [Flipkart Revenue](flipkart-revenue.md)
- [Stripe Revenue](stripe-revenue.md)
- [Zerodha Revenue](zerodha-revenue.md)
- [Swiggy Revenue](swiggy-revenue.md)
