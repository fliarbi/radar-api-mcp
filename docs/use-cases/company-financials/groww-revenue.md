# Groww Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “groww revenue” · 590/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [groww-revenue.json](../../examples/use-cases/groww-revenue.json).

**Question.** What revenue and profit has Groww reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `groww.in` |
| Fiscal periods with figures | 10 |
| Summary | Latest reported FY2026: revenue $557.35M, net income $249.96M. YoY +19.0% (1.19× prior period). Growth has been erratic across reported periods. Recent… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q4 FY2026 | $180.6M | $82.4M | $112.6M | — | news report |
| Q3 FY2026 | $145.9M | $65.6M | $89M | $53M | news report |
| Q2 FY2026 | $122.2M | $56.6M | — | — | news report |
| FY2026 | $557.4M | $250M | — | — | news report |
| Q2 FY2025 | $122.2M | $56.6M | — | — | news report |
| FY2024 | $348M | $35.8M | — | $64.2M | news report |
| FY2023 | $82.5M | $36M | — | — | news report |
| FY2022 | $41.8M | $816k | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-02-05 | Funding round | $202M | Zepto, Groww, and Jumbotail were among the major fundraisers, with Zepto securing $300 million, Groww raising $202 million, and Jumbotail… |
| 2025-11-03 | IPO | $795.8M | Groww's ₹6,632 crore IPO will open for subscription on Tuesday, November 4, with the issue priced between ₹95 per share to ₹100 per share. |
| 2025-07-01 | Equity | $202M | Groww’s $202 Mn equity raise in the run-up to its IPO |
| 2021-10-24 | Series E | $251M | Iconiq Growth led the Bangalore-based startup’s $251 million Series E financing round. Alkeon, Lone Pine Capital and Steadfast as well as… |
| 2021-04-07 | Series D | $83M | Investment platform Groww has vaulted to the unicorn club after raising $83 million (Rs 618 crore) in its Series D round led by Tiger… |
| 2020-09-10 | Series C | $30M | NextBillion Technology Pvt Ltd, which operates online investment platform Groww, has raised $30 million (Rs 220) in a Series C funding… |
| 2019-09-19 | Series B | $21.4M | Groww, an online investment platform that sells mutual fund products, has raised $21.4 million (Rs 152.5 crore at current exchange rate)… |
| 2019-01-23 | Series A | $6.2M | Groww, an online platform which sells mutual funds, has raised $6.2 million (Rs 44 crore) in a Series A round led by Sequoia Capital India. |
| 2018-12-07 | Series A | $6M | Online direct mutual funds investment platform Groww is in talks with Sequoia Capital to raise around $6 million (about Rs 42.5 crore),… |
| 2018-07-09 | pre-series A | $1.6M | Online investment startup Groww has raised $1.6 million in a pre-series A funding round from Insignia Venture Partners, America’s… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain groww.in --statement all --period-type all --limit 8
radar get-company-funding --domain groww.in
radar news-overview --company groww.in --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "groww.in", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "groww.in"}, timeout=120)
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

- [Cred Revenue](cred-revenue.md)
- [Physicswallah Revenue](physicswallah-revenue.md)
- [Oyo Revenue](oyo-revenue.md)
- [Canva Revenue](canva-revenue.md)
