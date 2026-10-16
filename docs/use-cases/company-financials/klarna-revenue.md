# Klarna Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “klarna revenue” · 30/month India · 390/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [klarna-revenue.json](../../examples/use-cases/klarna-revenue.json).

**Question.** What revenue and profit has Klarna reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `klarna.com` |
| Fiscal periods with figures | 15 |
| Summary | Latest reported Q4 FY2025: revenue $1.08B, net income $—. YoY +38.0% (1.38× prior period). Recent signals: Beat estimates, Reported a loss, Record revenue,… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q4 FY2025 | $1.1B | $-26M | — | $47M | news report |
| Q3 FY2025 | $903M | $-95M | — | — | news report |
| Q2 FY2025 | $823M | — | — | $29M | news report |
| Q3 FY2024 | $903M | $-95M | — | — | news report |
| Q1 FY2024 | $608M | $-30.7M | — | $21.8M | news report |
| 1H FY2024 | $1.3B | $-31.6M | — | $63.9M | news report |
| Q4 FY2023 | $1.1B | $-26M | — | — | news report |
| Q1 FY2023 | $465.5M | $-123.5M | — | $-47.5M | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-04-02 | Significant Risk Transfer (SRT) | $1.7B | has secured a $1.7 billion funding deal designed to unlock more than $40 billion in loan capacity. |
| 2025-12-23 | Equity | $255M | Recently, Klarna secured €255 million in equity funding and a €1.4 billion structured financing facility with Santander to fuel European… |
| 2025-08-19 | Debt financing / strategic investment | $26B | Swedish fintech giant Klarna has struck a colossal $26 billion funding agreement with U.S.-based lender Nelnet to fuel the expansion of… |
| 2023-01-17 | Series | $800M | Swedish BNPL giant Klarna had a bittersweet 2022. While it raised an impressive $800m in funding, its valuation dropped by 85% to $6.7bn. |
| 2022-07-11 | Funding round | $800M | Klarna is set to announce soon a $800m fundraising at a valuation of almost $6b, following new funding from existing investors and new… |
| 2021-06-10 | Funding round | $567M | In a new financing round of 525 million euros (639 million dollars), the company's assessment increases to 37.5 billion. |
| 2021-02-24 | Funding round | $1B | Swedish fintech scale-up Klarna is looking to raise up $1 billion at a $31 billion valuation. |
| 2020-09-15 | Funding round | $650M | [STOCKHOLM] Payment provider Klarna Bank said on Tuesday it has raised US$650 million at a valuation of US$10.65 billion from investors… |
| 2020-01-29 | Funding round | $200M | Commonwealth Bank has invested an additional $US200 million in European 'buy now pay later' giant Klarna. |
| 2019-11-06 | Venture Capital | — | H&M has spent more than SKr500m ($52m) on stakes in 16 businesses developing more sustainable ways of making clothes, such as dye company… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain klarna.com --statement all --period-type all --limit 8
radar get-company-funding --domain klarna.com
radar news-overview --company klarna.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "klarna.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "klarna.com"}, timeout=120)
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

- [Razorpay Revenue](razorpay-revenue.md)
- [Myntra Revenue](myntra-revenue.md)
- [Ola Revenue](ola-revenue.md)
- [Phonepe Revenue](phonepe-revenue.md)
