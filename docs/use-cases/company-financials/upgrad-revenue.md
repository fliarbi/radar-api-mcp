# Upgrad Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “upgrad revenue” · 320/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [upgrad-revenue.json](../../examples/use-cases/upgrad-revenue.json).

**Question.** What revenue and profit has Upgrad reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `upgrad.com` |
| Fiscal periods with figures | 8 |
| Summary | Latest reported FY2025: revenue $233.16M, net income $32.88M. YoY +3.6% (1.04× prior period). Growth has been erratic across reported periods. Recent signals:… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $233.2M | $32.9M | $1.8M | — | news report |
| FY2024 | $225.1M | $-67.2M | $-34.2M | $-34.2M | news report |
| FY2023 | $14.3M | $-13.7M | — | — | news report |
| FY2022 | $81.8M | $-75.2M | — | — | news report |
| FY2021 | $144M | — | — | — | news report |
| 1H FY2021 | $210M | — | — | — | news report |
| FY2020 | $19.5M | $-9.5M | — | — | news report |
| FY2019 | $14.5M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-02-26 | Funding round | $258M | The move follows upGrad's announcement in Davos of creating an AI center of excellence with investment of Rs 2,150 crore in collaboration… |
| 2024-10-25 | Funding round | $60M | Mumbai-based edtech unicorn Upgrad led the week’s funding with a $60 million infusion from Singapore’s sovereign wealth fund Temasek. |
| 2024-06-27 | Debt | $34.5M | Edtech unicorn upGrad has raised Rs 287.5 crore (approximately $35 million) from EvolutionX. |
| 2023-03-29 | Rights Issue | $36M | New Delhi: Edtech firm Upgrad has raised Rs 300 crore in a right issue led by co-founder and chairperson of the company Ronnie Screwvala,… |
| 2023-01-11 | Equity | $600M | UpGrad, founded by Ronnie Screwvala, Mayank Kumar and Phalgun Kompalli, has raised over $600 million from Temasek, Bharti Enterprises and… |
| 2022-08-08 | Funding round | $210M | Upskilling unicorn upGrad on Monday said it has secured $210 million (around Rs 1,638 crore) in a fresh round of funding from a clutch of… |
| 2022-03-11 | Funding round | $180M | upGrad raised $180 Mn from IFC, Temasek and IIFL increasing its valuation to $1.2 Bn in August 2021. |
| 2021-11-22 | Unicorn | $185M | In August, the Mumbai-based edtech giant became India’s fourth edtech startup to enter the celebrated unicorn club after closing $185 Mn… |
| 2021-04-25 | Funding round | $120M | Edtech startup upGrad has raised $120 Million (Rs 900 crores) from Singapore's sovereign fund Temasek in its first external fundraising. |
| 2021-01-31 | Funding round | $45M | Online tutor upGrad will raise around $45 million from International Finance Corporation (IFC) to expand its services, said the two sides. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain upgrad.com --statement all --period-type all --limit 8
radar get-company-funding --domain upgrad.com
radar news-overview --company upgrad.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "upgrad.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "upgrad.com"}, timeout=120)
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

- [Firstcry Revenue](firstcry-revenue.md)
- [Dream11 Revenue](dream11-revenue.md)
- [Practo Revenue](practo-revenue.md)
- [Acko Revenue](acko-revenue.md)
