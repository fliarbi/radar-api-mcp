# Cred Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “cred revenue” · 720/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [cred-revenue.json](../../examples/use-cases/cred-revenue.json).

**Question.** What revenue and profit has Cred reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `cred.club` |
| Fiscal periods with figures | 6 |
| Summary | Latest reported FY2025: revenue $328.2M. YoY +10.6% (1.11× prior period). Growth has been erratic across reported periods. Recent signals: Reported a loss,… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $328.2M | — | — | $-35.8M | news report |
| FY2024 | $296.8M | $-73.1M | — | $-73.1M | news report |
| FY2023 | $155.6M | — | — | — | news report |
| FY2022 | $50.7M | — | — | — | news report |
| FY2021 | $13M | — | — | — | news report |
| FY2020 | $62.4k | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-01-07 | Equity | $72M | CRED also saw a capital infusion of $72 Mn |
| 2025-06-09 | Funding round | $72M | Fintech unicorn CRED has received Rs 617 crore ($72 million) from multiple investors, including Lathe Investment, RTP Global, Sofina… |
| 2023-05-02 | Equity | $74M | GIC led a Rs 617-crore (about $80 million) fundraising round in the fintech business last year, which included a mix of main and secondary… |
| 2022-06-08 | Series F | $140M | Kunal Shah-led fintech unicorn Cred is raising $140 million in a Series F round led by GIC and existing investors, the company said in a… |
| 2021-10-18 | Series E | $251M | Indian fintech CRED said on Tuesday it has raised $251 million in a new financing round, its third funding this year, at a valuation of… |
| 2021-03-15 | Series D | $200M | Two-year-old CRED is in advanced stages of talks to raise about $200 million at about $2 billion valuation, three sources familiar with… |
| 2020-10-13 | Funding round | $100M | According to the reports from Moneycontrol, the funding will be led by Sequoia Capital, Tiger Global Management and Hillhouse Capital. |
| 2019-07-26 | Series B | $120M | Amidst finalising a $120 million fresh round from existing and new investors, the company has raised Rs 27.55 Crore ($4 million) from… |
| 2019-04-16 | Series A | $212.4M | Cred has till now raised approximately Rs 177 crore as part of its ongoing Series A round. |
| 2018-11-05 | Funding round | $30M | Earlier this year, Kunal raised $30 million for his new venture from a group of investors led by Sequoia Capital. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain cred.club --statement all --period-type all --limit 8
radar get-company-funding --domain cred.club
radar news-overview --company cred.club --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "cred.club", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "cred.club"}, timeout=120)
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

- [Blinkit Revenue](blinkit-revenue.md)
- [Urban Company Revenue](urban-company-revenue.md)
- [Physicswallah Revenue](physicswallah-revenue.md)
- [Groww Revenue](groww-revenue.md)
