# Rebel Foods Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “rebel foods revenue” · 260/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [rebel-foods-revenue.json](../../examples/use-cases/rebel-foods-revenue.json).

**Question.** What revenue and profit has Rebel Foods reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `rebelfoods.com` |
| Fiscal periods with figures | 6 |
| Summary | Latest reported FY2025: revenue $194.09M, net income $—. YoY +13.9% (1.14× prior period). Recent signals: Reported a loss, Record revenue. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $194.1M | $-40.4M | $-15.3M | — | news report |
| FY2024 | $170.4M | $-45.4M | — | — | news report |
| FY2023 | $151M | $-78.8M | — | — | news report |
| FY2022 | $103M | $-67.8M | — | — | news report |
| FY2021 | $48.6M | — | — | — | news report |
| FY2019 | $36.6M | $-15.7M | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-09-18 | Equity | $25M | This debt round follows closely on the heels of a $25 million equity investment from the Qatar Investment Authority earlier this year. |
| 2025-03-12 | Equity | — | Rebel Foods plans to invest Rs 100-150 crore to help American burger chain Wendy’s expand its footprint in India to 500 stores by 2028. |
| 2024-12-12 | Series G | $210M | has raised $210 million (nearly Rs 1,800 crore) in its Series G funding round in a mix of primary and secondary share sales. |
| 2024-08-26 | Funding round | $120M | Rebel Foods, the Mumbai-based cloud kitchen startup behind popular brands such as Faasos, Oven Story, and Behrouz Biryani, is in advanced… |
| 2024-05-29 | Debt | $13.2M | Cloud kitchen brand Rebel Foods has raised Rs 110 crore ($13.2 million) in debt from Alteria and InnoVen Capital. |
| 2023-04-25 | Debt | $9M | The board at Rebel Foods has passed a special resolution to issue 7,500 Series F non-convertible debentures at an issue price of Rs… |
| 2022-12-29 | Debt | $6.6M | Cloud kitchen brand Rebel Foods has raised Rs 55 crore in a debt round from InnoVen Capital and Trifecta Capital. |
| 2022-11-01 | Debt funding round | $12.5M | Foodtech unicorn Rebel Foods has raised $12.5 Mn (INR 100 Cr) in a debt funding round from InnoVen Capital and Trifecta Capital. |
| 2022-03-28 | Funding round | $10M | Rebel Foods , which operates a network of cloud kitchens and digital brands, on Friday announced a $10 million employee stock ownership… |
| 2021-10-07 | Series F | $175M | Rebel Foods Pvt Ltd, the owner of online kitchen brands including Faasos and Behrouz Biryani, has raised $175 million (Rs 1,308 crore) in… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain rebelfoods.com --statement all --period-type all --limit 8
radar get-company-funding --domain rebelfoods.com
radar news-overview --company rebelfoods.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "rebelfoods.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "rebelfoods.com"}, timeout=120)
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

- [Spinny Revenue](spinny-revenue.md)
- [Darwinbox Revenue](darwinbox-revenue.md)
