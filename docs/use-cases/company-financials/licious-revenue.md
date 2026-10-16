# Licious Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “licious revenue” · 390/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [licious-revenue.json](../../examples/use-cases/licious-revenue.json).

**Question.** What revenue and profit has Licious reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `licious.in` |
| Fiscal periods with figures | 7 |
| Summary | Latest reported FY2026: revenue $139.92M. YoY +40.1% (1.4× prior period). Growth pattern is consistent across reported periods. Recent signals: Raised… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2026 | $139.9M | — | $-22.4M | — | news report |
| FY2025 | $99.9M | $-25.8M | — | — | news report |
| Q1 FY2024 | $22.8M | — | — | — | news report |
| FY2024 | $82.2M | $-35.3M | — | — | news report |
| FY2023 | $84M | $-63.4M | — | — | news report |
| FY2022 | $82M | — | — | — | news report |
| FY2021 | $52.2M | $-44.4M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-06-03 | Debt Investment | — | InnoVen Capital on Thursday announced making a debt investment in Licious with an investment worth Rs. 12 crores. |
| 2025-02-18 | Funding round | $554.2M | It has raised $554.22 Mn in funding so far, and counts the likes of Temasek, 3One4 Capital and IIFL among its marquee investors. |
| 2024-05-21 | Funding round | $490M | It has received total funding, of over $490 million in 12 rounds. |
| 2022-11-21 | Funding round | $390M | Direct-to-consumer (D2C) meat and seafood brand Licious became India’s first unicorn in its space and raised over $390 million across four… |
| 2022-03-14 | Series F2 | $150M | The Series F2 round was led by Singapore-based Amansa Capital, along with Kotak PE and Axis Growth Avenues AIF - I.Zerodha’s founders… |
| 2021-10-04 | Funding round | $52M | The company has raised $5.2 crore on this value in the fresh funding round. |
| 2021-06-11 | Series F | $192M | Updated story: Licious today announced that it has raised $192 million in its Series F funding round led by Temasek and Multiples Private… |
| 2021-04-16 | Funding round | — | Private equity investors Multiples Alternate Asset Management, Premji Invest and Goldman Sachs are looking to together invest $150-200… |
| 2021-01-19 | Funding round | $80M | Gourmet meat startupis eyeing $80 million in funding at a valuation of $800 million , in a round that will see participation from new as… |
| 2020-10-27 | Funding round | $30M | In its latest round in December 2019, Licious received $30 million from Sistema Asia Fund, Vertex Ventures, Bertelsmann and 3one4 Capital. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain licious.in --statement all --period-type all --limit 8
radar get-company-funding --domain licious.in
radar news-overview --company licious.in --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "licious.in", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "licious.in"}, timeout=120)
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

- [Nykaa Revenue](nykaa-revenue.md)
- [Country Delight Revenue](country-delight-revenue.md)
- [Pine Labs Revenue](pine-labs-revenue.md)
- [Makemytrip Revenue](makemytrip-revenue.md)
