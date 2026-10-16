# Oyo Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “oyo revenue” · 590/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [oyo-revenue.json](../../examples/use-cases/oyo-revenue.json).

**Question.** What revenue and profit has Oyo reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `oyorooms.com` |
| Fiscal periods with figures | 18 |
| Summary | Latest reported Q1 FY2026: revenue $242.28M, net income $24M. YoY +47.0% (1.47× prior period). Growth has been erratic across reported periods. Recent… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q1 FY2026 | $242.3M | $24M | — | — | news report |
| Q4 FY2025 | $252M | $132M | $240M | — | news report |
| Q3 FY2025 | $203.4M | $19.9M | $29.9M | $29.9M | news report |
| Q2 FY2025 | $189.4M | $19M | $31.9M | — | news report |
| FY2025 | $775.6M | $132M | $135.8M | — | news report |
| FY2024 | $27.5M | — | — | — | news report |
| 1H FY2024 | $336M | — | $22.2M | — | news report |
| Q1 FY2023 | $175.1M | $-49.7M | $840k | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-01-04 | Equity | $65M | Oyo, one of the leading hospitality companies, has managed to raise ₹550 crore or $65 million from Redsprig Innovation Partners, an entity… |
| 2024-08-12 | Series G | $174.8M | Oyo, a leading company in the hospitality industry, has successfully secured Rs 1,457 crore (about $175 million) in a Series G funding… |
| 2024-03-12 | Credit Facility | $24M | JP Morgan has provided a credit facility of Rs 200 crore to Oyo, aimed at fueling the expansion of Oyo's Accelerator Programme. |
| 2024-01-25 | Preliminary Funding Round | $400M | IPO-bound hospitality chain OYO , operated by Oravel Stays Pvt Ltd, is in talks with Malaysian sovereign wealth fund Khazanah Nasional… |
| 2021-07-16 | term loan B | $660M | India-based hotel company Oyo Rooms has raised $660 million from global institutional investors in term loan B funding, the company… |
| 2021-05-20 | Term Loan B | $600M | Hospitality firm OYO is looking to raise USD 600 million (over Rs 4,380 crore) in debt from the US institutional investors to service its… |
| 2021-01-05 | Series F1 | $6.5M | OYO has raised Rs 54 crore in Series F1 round of financing from Hindustan Media Ventures. |
| 2020-03-17 | Series F | $807M | Online hospitality firm Oyo has raised $807 million as part of its $1.5 billion fundraise from SoftBank and RA Hospitality which was… |
| 2019-12-28 | Series F | $1.5B | Among the top equity rounds of the year include OYO Rooms ($1.5 billion – Series F), Paytm ($1 million – Series G) and Udaan ($585 million… |
| 2018-09-25 | Funding round | $1B | Start-up OYO, budget hotel aggregator , is raising $1 billion to fund expansion into China and other global regions. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain oyorooms.com --statement all --period-type all --limit 8
radar get-company-funding --domain oyorooms.com
radar news-overview --company oyorooms.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "oyorooms.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "oyorooms.com"}, timeout=120)
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

- [Physicswallah Revenue](physicswallah-revenue.md)
- [Groww Revenue](groww-revenue.md)
- [Canva Revenue](canva-revenue.md)
- [Mamaearth Revenue](mamaearth-revenue.md)
