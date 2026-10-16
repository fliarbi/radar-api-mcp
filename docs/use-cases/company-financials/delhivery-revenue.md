# Delhivery Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “delhivery revenue” · 390/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [delhivery-revenue.json](../../examples/use-cases/delhivery-revenue.json).

**Question.** What revenue and profit has Delhivery reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `delhivery.com` |
| Fiscal periods with figures | 20 |
| Summary | Latest reported Q3 FY2026: revenue $345.84M, net income $4.8M. YoY +21.2% (1.21× prior period). Growth has been erratic across reported periods. Recent… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q3 FY2026 | $345.8M | $4.8M | $17.6M | — | news report |
| Q2 FY2026 | $307.1M | $-60.5M ⚠ | $81.8M | — | news report |
| Q1 FY2026 | $275.3M | $109.2M ⚠ | $17.9M | — | news report |
| Q4 FY2025 | $276.4M | $8.7M | $14.3M | — | news report |
| Q3 FY2025 | $285.4M | $4.9M | $12.2M | — | news report |
| Q2 FY2025 | $262.8M | $1.2M | $6.8M | — | news report |
| Q1 FY2025 | $273.8M | $6.2M | $11.6M | — | news report |
| Q4 FY2024 | $263.3M | $1.4M | $720k | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

⚠ marks a figure more than eight times this company's typical value for that metric, usually a unit or currency slip in the source report. Verify it before use.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-04-21 | Acquisition | $168M | Delhivery Ltd and Ecom Express have sought the Competition Commission of India’s approval for their ₹ 1,400-crore deal. Under the deal… |
| 2022-07-07 | Equity | $304M | "Delhivery (USD 304 million- Series J)" |
| 2021-06-02 | Funding round | $277M | IPO-bound Delhivery raked in a $277 million round. |
| 2020-12-14 | Secondary | $25M | Steadview has bought shares worth $25 million (Rs 184 crore) in Delhivery from one of its early backers, as per a press statement. |
| 2020-08-24 | Funding round | $36M | Delhivery is looking at investing up to Rs 300 crore in the next 18-24 months for expansion. |
| 2020-06-10 | Funding round | $260M | Following the round, Delhivery had raised an approximation of $260 million. And their investors include the Carlyle Group, Chinese… |
| 2019-12-27 | Funding round | $350M | The company raised $350 million from SoftBank Group alone. |
| 2019-10-24 | Equity | $115M | Among the top funding rounds, last month include Delhivery ($115 Mn), Lenskart ($55 Mn), Spinny ($50 Mn) and Glance ($45 Mn). |
| 2019-03-06 | Funding round | $400M | Encouraged by Delhivery’s near ten-fold growth in about four years, and the e-retailing boom in India, investors led by SoftBank have… |
| 2018-11-21 | Funding round | $350M | SoftBank, through its Vision Fund, may invest an estimated $350 Mn as fresh capital in Delhivery. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain delhivery.com --statement all --period-type all --limit 8
radar get-company-funding --domain delhivery.com
radar news-overview --company delhivery.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "delhivery.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "delhivery.com"}, timeout=120)
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

- [Unacademy Revenue](unacademy-revenue.md)
- [Freshworks Revenue](freshworks-revenue.md)
- [Nykaa Revenue](nykaa-revenue.md)
- [Country Delight Revenue](country-delight-revenue.md)
