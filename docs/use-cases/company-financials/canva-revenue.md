# Canva Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “canva revenue” · 320/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [canva-revenue.json](../../examples/use-cases/canva-revenue.json).

**Question.** What revenue and profit has Canva reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `canva.com` |
| Fiscal periods with figures | 2 |
| Summary | Latest reported FY2021: revenue $500M. Recent signals: Record revenue. |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2021 | $500M | — | — | — | news report |
| FY2019 | $187.5M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-08-22 | Employee share sale | — | The latest funding round was led by existing investor Fidelity Management & Research Co. and new investors J.P. Morgan Asset Management… |
| 2024-05-01 | Funding round | $8M | Stack Capital Group Inc. (TSX:STCK and STCK.WT) (‘Stack Capital’) an investment holding company that invests in some of the world’s most… |
| 2024-01-21 | Share Sale | $1.5B | Australian software company Canva is close to completing a share sale that’s set to raise more than $US1.5 billion ($2.3b), according to… |
| 2023-11-20 | Developer Innovation Fund | $50M | Visual communication platform Canva on Monday announced the opening of applications for its $50 million Developers Innovation Fund to… |
| 2023-08-08 | Equity | — | Canva has two new investors in San Francisco-headquartered ICONIQ Capital and Coatue Management, another US firm, with the sale confirming… |
| 2022-04-26 | Equity | $18.7M | In Canva’s latest round of venture capital raising, Franklin Templeton’s Growth Opportunities Fund purchased thousands of shares in the… |
| 2022-01-24 | Raise | $273M | They included Canva’s $273 million raise, which valued the business at $55 billion; |
| 2021-09-14 | Funding round | $200M | Canva, the global visual communications platform, today announced a USD $40 billion valuation after a USD $200 million funding round led… |
| 2021-04-06 | Funding round | — | The investment round of $US71 million came from existing investors Australian venture capital firm Blackbird Ventures and Scott Farquhar… |
| 2021-02-04 | Funding round | $300M | Canva employs around 1,000 people and has raised around USD 300 million from various investors. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain canva.com --statement all --period-type all --limit 8
radar get-company-funding --domain canva.com
radar news-overview --company canva.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "canva.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "canva.com"}, timeout=120)
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

- [Groww Revenue](groww-revenue.md)
- [Oyo Revenue](oyo-revenue.md)
- [Mamaearth Revenue](mamaearth-revenue.md)
- [Rapido Revenue](rapido-revenue.md)
