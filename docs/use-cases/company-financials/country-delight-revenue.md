# Country Delight Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “country delight revenue” · 390/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [country-delight-revenue.json](../../examples/use-cases/country-delight-revenue.json).

**Question.** What revenue and profit has Country Delight reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `countrydelight.in` |
| Fiscal periods with figures | 3 |
| Summary | Latest reported 1H FY2024: revenue $78M. Recent signals: Record revenue, Reported a loss. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| 1H FY2024 | $78M | — | — | — | news report |
| FY2023 | $108M | — | — | — | news report |
| FY2022 | $65.2M | $-22.3M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-03-26 | Series E | $25.5M | Gurugram-based dairy and daily essential brand Country Delight is raising Rs 212.5 crore (approximately $25 million) in its Series E round… |
| 2024-11-02 | Debt | $24M | Country Delight, a dairy tech startup has closed its INR 200 Cr debt funding round with Alteria Capital. |
| 2024-06-01 | Funding round | $9M | Delhi-NCR based dairytech startup Country Delight is looking to raise $9 Mn (INR 76 Cr) from Alteria Capital in a mix of debt and equity… |
| 2024-01-05 | Series E | $20M | Dairy brand Country Delight has raised $20 million or Rs 164.4 crore in a series E round from new and existing investors. |
| 2023-11-07 | Funding round | $108M | competitor brand Country Delight successfully obtained a significant $108 million in a funding round just last year. |
| 2023-07-17 | Series C | $22.2M | The platform has raised ₹185 crore, in its Series C round of funding led by Elevation Capital. |
| 2022-05-25 | Series D | $108M | Country Delight, a direct-to-consumer (D2C) food essentials brand, has raised $108 million in Series D round taking its valuation to $615… |
| 2022-02-07 | Funding round | — | Country Delight is in talks with private equity funds Temasek, Venturi Partners, and Premji Invest to raise $90-$100 million, esteeming it… |
| 2020-11-22 | Series C | $25M | Bengaluru‑based home food essential brand ﻿Country Delight﻿ has raised $25 million Series C funding led by Elevation Capital (formerly… |
| 2020-07-18 | Debt | $934k | Gurugram-based food production company Country Delight’s parent Beejapuri Dairy Private Limited has raised $934K (INR 7 Cr) in debt from… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain countrydelight.in --statement all --period-type all --limit 8
radar get-company-funding --domain countrydelight.in
radar news-overview --company countrydelight.in --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "countrydelight.in", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "countrydelight.in"}, timeout=120)
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

- [Delhivery Revenue](delhivery-revenue.md)
- [Nykaa Revenue](nykaa-revenue.md)
- [Licious Revenue](licious-revenue.md)
- [Pine Labs Revenue](pine-labs-revenue.md)
