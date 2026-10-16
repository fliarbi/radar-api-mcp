# Inmobi Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “inmobi revenue” · 260/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [inmobi-revenue.json](../../examples/use-cases/inmobi-revenue.json).

**Question.** What revenue and profit has Inmobi reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `inmobi.com` |
| Fiscal periods with figures | 4 |
| Summary | Latest reported FY2020: revenue $51.79M, net income $—. YoY +12.3% (1.12× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2020 | $51.8M | $-9.2M | — | $49.4M | news report |
| FY2019 | $46.1M | $-6.5M | — | — | news report |
| Q4 FY2016 | $300M | — | — | — | news report |
| FY2016 | $300M | $-53M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures.

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-01-22 | Series E | $400M | Bengaluru-based adtech unicorn InMobi is in advanced discussions to raise $400 million in a Series E funding round at a post-money… |
| 2024-09-10 | Debt Financing | $10M | Adtech startup InMobi has raised $100 million in debt financing as the profitable Indian firm looks to “significantly deepen” its… |
| 2024-07-24 | Funding round | $250M | InMobi Pte., a mobile content provider, is currently in advanced discussions to obtain a fundraising round of up to $250 million. |
| 2022-02-14 | Funding round | $4.5B | The US search giant invested US$4.5 billion in the company alongside Meta Platforms in 2020. |
| 2019-02-25 | Debt Financing | $100M | In Sept 2015, it raised its last funding of $100 million from a Debt Financing round. |
| 2015-09-29 | Debt | $10M | Mobile adtech company InMobi has raised $100 million in new debt from a consortium of lenders led by US-based Tennenbaum Capital Partners. |
| 2014-12-02 | Funding round | $5M | Mobile ad network InMobi has raised $5 million (Rs 31 crore) from its high-profile investor SoftBank |
| 2012-11-18 | Funding round | — | First venture capital funding from Kleiner Perkins Caufield and Byers and Ram Shriram’s Sherpalo Investments in 2008. |
| 2012-07-10 | Equity | $200M | InMobi, a technology provider for mobile advertising that raised $200 million from Japan's Softbank late last year |
| 2011-09-14 | Funding round | $200M | In what appears to be the largest investment in the mobile advertising space, InMobi has raised a whooping $200 million from Softbank, a… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain inmobi.com --statement all --period-type all --limit 8
radar get-company-funding --domain inmobi.com
radar news-overview --company inmobi.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "inmobi.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "inmobi.com"}, timeout=120)
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

- [Acko Revenue](acko-revenue.md)
- [Ather Energy Financials](ather-energy-financials.md)
- [Shiprocket Revenue](shiprocket-revenue.md)
- [Spinny Revenue](spinny-revenue.md)
