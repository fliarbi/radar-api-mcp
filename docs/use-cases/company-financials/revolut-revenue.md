# Revolut Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “revolut revenue” · 170/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [revolut-revenue.json](../../examples/use-cases/revolut-revenue.json).

**Question.** What revenue and profit has Revolut reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `revolut.com` |
| Fiscal periods with figures | 8 |
| Summary | Latest reported FY2025: revenue $6B, net income $1.7B. YoY +52.4% (1.52× prior period). Recent signals: Beat estimates, Profitable, Record revenue. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $6B | $1.7B ⚠ | — | — | news report |
| FY2024 | $3.9B | $1.3B ⚠ | — | — | news report |
| FY2023 | $2.3B | $556.3M | — | — | news report |
| FY2022 | $1.1B | $7M | $28M | — | news report |
| FY2021 | $769M | $31M | $127.4M | $75.1M | news report |
| FY2019 | $206.6M | $-135.9M | — | — | news report |
| FY2018 | $73.7M | $-41.9M | — | — | news report |
| FY2017 | $16.3M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

⚠ marks a figure more than eight times this company's typical value for that metric, usually a unit or currency slip in the source report. Verify it before use.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-01-28 | Equity | $100M | Revolut has allocated more than $100m in capital for its Mexican bank |
| 2025-10-13 | Funding round | $2B | Revolut’s landmark $2 billion raise |
| 2025-07-09 | Funding round | $1B | The U.K.-based company is reportedly in talks to raise around $1 billion by issuing new shares and selling existing ones. The U.S.-based… |
| 2025-05-19 | Funding round | $1.1B | Revolut, the London-based FinTech giant, has unveiled plans to invest over €1 billion in France over the next three years |
| 2024-08-16 | Secondary Share Sale | — | The firm announced on Friday that Coatue, D1 Capital Partners and Tiger Global were among the institutional investors who participated in… |
| 2024-05-14 | Series A | $66M | In fact, one of the biggest in the UK was from FinTech Revolut, which raised $66 million in its Series A round in 2017, a move that… |
| 2022-01-28 | Equity Crowdfunding | $1.3M | Revolut raised just over £1 million (€1.2 million) from 433 investors via equity-based crowdfunding platform Crowdcube in July 2016. |
| 2021-07-15 | Funding round | $800M | Revolut, the London-based digital banking startup founded just six years ago by Russian-born founder Nikolay Storonsky, raised $800… |
| 2021-04-19 | Funding round | $15M | Revolut launched 2015 and by 2016 had 100,000 personal customers and in its first found raised $15 million, according to its website. |
| 2021-03-02 | Funding round | $917M | Revolut ($917M funding raised, $5.5B valuation). |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain revolut.com --statement all --period-type all --limit 8
radar get-company-funding --domain revolut.com
radar news-overview --company revolut.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "revolut.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "revolut.com"}, timeout=120)
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

- [Pine Labs Revenue](pine-labs-revenue.md)
- [Makemytrip Revenue](makemytrip-revenue.md)
- [Cars24 Revenue](cars24-revenue.md)
- [Firstcry Revenue](firstcry-revenue.md)
