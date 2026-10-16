# Anthropic Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “anthropic revenue” · 1,000/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [anthropic-revenue.json](../../examples/use-cases/anthropic-revenue.json).

**Question.** What revenue and profit has Anthropic reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `anthropic.com` |
| Fiscal periods with figures | 2 |
| Summary | Latest reported FY2026: revenue $30B. YoY +233.3% (3.33× prior period). |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2026 | $30B | — | — | — | news report |
| FY2025 | $9B | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2026-02-12 | Equity | $30B | Anthropic announced on Thursday the close of a $30 billion funding round at a $380 billion post-money valuation |
| 2025-02-13 | Funding round | $3.5B | Anthropic has raised $3.5 billion at a $61.5 billion post-money valuation. |
| 2024-08-29 | Funding round | $6B | Amazon and Google have jointly invested $6 billion in Anthropic. |
| 2024-07-08 | Funding round | $50M | DAMAC Group announced notable investments in leading AI companies including a $50 million in the AI startup, Anthropic |
| 2024-04-23 | Series G | $30B | US AI unicorn Anthropic, the scaleup founded by Italian-Americans Dario and Daniela Amodei has raised another 30 billion dollars in a… |
| 2023-12-21 | Funding round | $750M | Artificial intelligence (AI) startup Anthropic is in discussions to raise $750 million in a funding round led by Menlo Ventures, a source… |
| 2023-09-24 | Funding round | $4B | Amazon is pledging to invest up to $4 billion in artificial intelligence (AI) startup Anthropic. |
| 2022-07-28 | Series B | $704M | Total equity funding raised: $704.0M |
| 2022-05-02 | Series B | $580M | Anthropic, a San Francisco, California-based Artificial intelligence research company, announced that it raised $580 million in a Series B… |
| 2022-01-23 | Series C | $450M | Anthropic has raised $450 million in Series C funding led by Spark Capital with participation from Google, Salesforce Ventures, Sound… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain anthropic.com --statement all --period-type all --limit 8
radar get-company-funding --domain anthropic.com
radar news-overview --company anthropic.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "anthropic.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "anthropic.com"}, timeout=120)
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

- [Openai Revenue](openai-revenue.md)
- [Zoho Revenue](zoho-revenue.md)
- [Zomato Revenue](zomato-revenue.md)
