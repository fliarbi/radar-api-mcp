# Dream11 Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “dream11 revenue” · 320/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [dream11-revenue.json](../../examples/use-cases/dream11-revenue.json).

**Question.** What revenue and profit has Dream11 reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `dream11.com` |
| Fiscal periods with figures | 4 |
| Summary | Latest reported FY2023: revenue $766.08M, net income $22.56M. YoY +57.0% (1.57× prior period). Recent signals: Profitable, Record revenue. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2023 | $766.1M | $22.6M | — | — | news report |
| FY2022 | $487.8M | $17M | — | — | news report |
| FY2020 | $248.4M | $21.7M | — | — | news report |
| FY2019 | $93M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures.

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2021-11-24 | Funding round | $840M | Fantasy sports platform Dream11 [owned by Dream Sports] has scooped up $840 million in a new round led by Falcon Edge, DST Global, D1… |
| 2021-07-07 | Funding round | $400M | Some of the marquee fundraising deals in the January-June period included those by edtech leader Byju’s ($1 billion), food delivery… |
| 2021-03-25 | Secondary | $400M | Dream Sports, which owns online fantasy sports platform Dream11, has closed a $400-million secondary investment round led by new investors… |
| 2020-08-24 | Funding round | $235M | Also, Dream11, the lead sponsor of the 2020 Indian Premier League (IPL), is in advanced talks with at least four private equity firms to… |
| 2020-03-09 | Round | $500M | Recently, Dream11 was speculated to be raising $500 Mn in funding, which will be led by Tiger Global. |
| 2019-12-04 | Funding round | $60M | Verge Dream11, fantasy sports service, raised $60m. |
| 2019-03-08 | Funding round | — | Tencent's investment in Dream11, |
| 2018-12-07 | Series D | $100M | Following which, last month, Dream11 vaulted into the big league of local mobile gaming startups when it raised $100 million in a Series D… |
| 2018-09-08 | Funding round | $100M | Dream11 has raised around $100 million round from Tencent Holding, said two sources close to the development. |
| 2018-04-20 | Funding round | $10M | Tencent Holdings, the world’s fifth-largest internet company, is in advanced stages of negotiations to invest an estimated $100 million… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain dream11.com --statement all --period-type all --limit 8
radar get-company-funding --domain dream11.com
radar news-overview --company dream11.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "dream11.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "dream11.com"}, timeout=120)
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

- [Cars24 Revenue](cars24-revenue.md)
- [Firstcry Revenue](firstcry-revenue.md)
- [Upgrad Revenue](upgrad-revenue.md)
- [Practo Revenue](practo-revenue.md)
