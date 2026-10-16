# Acko Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “acko revenue” · 260/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [acko-revenue.json](../../examples/use-cases/acko-revenue.json).

**Question.** What revenue and profit has Acko reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `acko.com` |
| Fiscal periods with figures | 5 |
| Summary | Latest reported FY2025: revenue $340.44M. YoY +31.3% (1.31× prior period). Growth pattern is consistent across reported periods. Recent signals: Record… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $340.4M | — | — | — | news report |
| FY2024 | $259.2M | — | — | — | news report |
| FY2023 | $211.1M | $-88.6M | — | — | news report |
| Q1 FY2022 | $9.7M | — | — | — | news report |
| FY2022 | $130.5M | $-45.9M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-02-27 | Funding round | $598M | ACKO has raised $598 million — the highest among all funded InsurTech companies in India as of January 2026. |
| 2025-07-30 | Secondary Transaction | — | The family office of cricketer MS Dhoni has invested in insurtech unicorn Acko, participating in a secondary transaction. |
| 2023-07-17 | Funding round | $450M | The platform has raised $450 million from Amazon, Accel Partners, Catamaran Ventures, Elevation Capital, RPS Ventures, and Binny Bansal. |
| 2022-10-19 | Funding round | $100M | The New York-headquartered growth equity investor is positioning to lead a new financing round of about $100 million in the Indian startup. |
| 2022-03-30 | Funding round | $319.2M |  |
| 2021-10-27 | Series D | $255M | Indian digital insurance provider Acko has raised $255 million as a part of its Series D round led by private equity firms General… |
| 2021-05-12 | Funding round | $200M | The Amazon.com Inc.-backed startup is looking to raise about $200 million in the round |
| 2020-09-16 | Series D | $60M | Digital insurance provider Acko has secured $60 million in its Series D funding round led by Munich Re Ventures along with the… |
| 2020-01-21 | Funding round | $20M | In November last year, it raised $20 million (around Rs 143.50 crore) in funding from Binny Bansal, taking the Flipkart co-founder’s total… |
| 2019-11-30 | Funding round | $16M | Bengaluru-based online insurance startup Acko has raised $16 Mn funding of from Ascent Capital. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain acko.com --statement all --period-type all --limit 8
radar get-company-funding --domain acko.com
radar news-overview --company acko.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "acko.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "acko.com"}, timeout=120)
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

- [Upgrad Revenue](upgrad-revenue.md)
- [Practo Revenue](practo-revenue.md)
- [Ather Energy Financials](ather-energy-financials.md)
- [Inmobi Revenue](inmobi-revenue.md)
