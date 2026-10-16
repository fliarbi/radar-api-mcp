# Openai Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “openai revenue” · 1,300/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [openai-revenue.json](../../examples/use-cases/openai-revenue.json).

**Question.** What revenue and profit has Openai reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `openai.com` |
| Fiscal periods with figures | 5 |
| Summary | Latest reported FY2025: revenue $12.7B. YoY +243.2% (3.43× prior period). Growth has been erratic across reported periods. Recent signals: Raised guidance,… |
| Recorded funding events | 9 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| FY2025 | $12.7B | — | — | — | news report |
| 1H FY2025 | $4.3B | — | — | — | news report |
| FY2024 | $3.7B | — | — | — | news report |
| FY2023 | $1.3B | — | — | — | news report |
| FY2022 | $28M | — | — | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2025-01-28 | Funding round | $41B | Masayoshi Son-led SoftBank in 2025 completed a $41 billion investment in OpenAI, marking one of the largest private funding rounds on… |
| 2024-03-10 | Funding round | $6.6B | The hottest AI startup, OpenAI, recently raised $6.6 billion at a valuation of $157 billion. |
| 2023-10-28 | Funding round | $13B | OpenAI, which has garnered a whopping $13 billion in funding from Microsoft since 2019 |
| 2023-03-16 | Funding round | $1.5B | Musk’s comments come after OpenAI announced its latest funding round, which raised $1.5 billion at a valuation of $30 billion. The funding… |
| 2023-01-10 | Funding round | $10B | Microsoft Corp is in talks to invest $10 billion in ChatGPT-owner OpenAI as part of funding that will value the firm at $29 billion,… |
| 2022-01-27 | Investment | $1B | In July 2019, Microsoft backed OpenAI with $1 billion. |
| 2021-05-27 | Venture Capital | $100M | OpenAI startup fund announced it is investing $100 million in AI companies. |
| 2019-07-26 | Equity | $1B | the $1 billion investment OpenAI received from Microsoft. |
| 2015-12-12 | Funding round | $1B | In total, these funders have committed $1 billion. |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain openai.com --statement all --period-type all --limit 8
radar get-company-funding --domain openai.com
radar news-overview --company openai.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "openai.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "openai.com"}, timeout=120)
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

- [Anthropic Revenue](anthropic-revenue.md)
- [Zoho Revenue](zoho-revenue.md)
