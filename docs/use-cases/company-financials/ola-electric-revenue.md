# Ola Electric Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “ola electric revenue” · 260/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [ola-electric-revenue.json](../../examples/use-cases/ola-electric-revenue.json).

**Question.** What revenue and profit has Ola Electric reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `olaelectric.com` |
| Fiscal periods with figures | 20 |
| Summary | Latest reported FY2026: revenue $270.36M, net income $—, EPS $-4.16. YoY -50.1% (0.5× prior period). Growth has been erratic across reported periods. Recent… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q4 FY2026 | $31.8M | — | $-9.9M | — | news report |
| Q3 FY2026 | $56.4M | — | $-32.5M | — | news report |
| Q2 FY2026 | $82.8M | $-50.2M | $-24.4M | $-24.4M | news report |
| Q1 FY2026 | $99.4M | $-51.4M | $-28.4M | — | news report |
| FY2026 | $270.4M | $-220M | — | — | news report |
| Q4 FY2025 | $73.3M | — | — | $60.5M | news report |
| Q3 FY2025 | $128.3M | $-67.7M | $-55.2M | — | news report |
| Q2 FY2025 | $145.7M | $-59.4M | $-41.4M | $-16M | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-06-02 | Qualified Institutional Placement (QIP) | $60M | The company is looking at raising funds up to ₹500 crore, with a possible upsize option, people in the know told CNBC-TV18. |
| 2026-03-16 | Initial Public Offering | $660M | In August 2024, Ola Electric Mobility raised Rs 5,500 crore through its initial public offering (IPO). |
| 2025-12-26 | Government Grant | $44M | Ola Electric Mobility Limited has received a ₹366.78 crore incentive under the Government of India’s Production Linked Incentive Scheme… |
| 2025-10-01 | Funding round | $10.5M | Ola Electric share price: The company said in a stock exchange filing that the Board and Shareholders of OET have approved a group’s own… |
| 2025-05-23 | Funding round | — | The Board of Directors of Ola Electric Mobility Limited, at its meeting held today, Thursday, May 22, 2025, has inter-alia, considered and… |
| 2024-04-01 | Debt | $50M | Reports confirm that the company has successfully raised $50 million in debt funding from EvolutionX Debt Capital, a renowned debt… |
| 2023-10-26 | Funding round | $384M | Ola Electric has raised Rs 3,200 crore (around $384.4 million) in a mix of equity and debt, in its latest funding round. |
| 2023-06-09 | Funding round | $300M | During the current funding round, Ola Electric has set a target of raising $300 million, leaving approximately $50 million available for… |
| 2023-02-19 | Equity | $613.7M | Of the Rs 7,614 crores, as much as Rs 5,114 crore will go into the cell manufacturing plant |
| 2022-12-23 | Funding round | $500M | Ola Electric will also invest a $500 million in battery innovation and indigenous research and development (R&D). |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain olaelectric.com --statement all --period-type all --limit 8
radar get-company-funding --domain olaelectric.com
radar news-overview --company olaelectric.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "olaelectric.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "olaelectric.com"}, timeout=120)
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

- [Phonepe Revenue](phonepe-revenue.md)
- [Indiamart Revenue](indiamart-revenue.md)
- [Unacademy Revenue](unacademy-revenue.md)
- [Freshworks Revenue](freshworks-revenue.md)
