# Hedge Fund News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “hedge fund news” · 390/month India · 1,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [hedge-fund-news.json](../../examples/use-cases/hedge-fund-news.json).

**Question.** How much news did hedge fund receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,538 |
| Negative · neutral · positive | 27% · 0.9% · 72% |
| Critical (priority 7–9) | 69% (2,424 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,138 articles) |
| Negative-to-positive vs all news | 0.5× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 127 | 61% | 21 | 102 | █ |
| Sep 2025 | 385 | 63% | 149 | 229 | ████ |
| Oct 2025 | 297 | 61% | 86 | 205 | ███ |
| Nov 2025 | 417 | 67% | 169 | 247 | ████ |
| Dec 2025 | 256 | 62% | 81 | 170 | ██ |
| Jan 2026 | 348 | 49% | 104 | 241 | ███ |
| Feb 2026 | 507 | 64% | 177 | 320 | █████ |
| Mar 2026 | 545 | 63% | 151 | 385 | █████ |
| Apr 2026 | 2,138 | 74% | 518 | 1,607 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 13 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Bill Ackman's Pershing Square USA tumbles 18% in its stock-market debut](https://www.businessinsider.com/bill-ackman-ps-psus-pershing-square-usa-ipo-trading-investing-2026-4) | businessinsider.com | 8 | negative |
| 28 Apr 2026 | [Michael Burry Bets Against Red-Hot Chip Stocks — Says They 'Will Return To Earth'](https://ibtimes.co.uk/michael-burry-bets-against-ai-semiconductor-surge-1794051) | ibtimes.co.uk | 8 | negative |
| 27 Apr 2026 | [Impax Environmental Markets: Three important questions – starting with "How exactly did Saba end up with…](https://quoteddata.com/2026/04/impax-environmental-markets-three-important-questions-starting-with-how-exactly-did-saba-end-up-with-29-9/) | quoteddata.com | 8 | negative |
| 23 Apr 2026 | [Alibaba, Tencent Eye Major Investment in DeepSeek: Report - Techstrong.ai](https://techstrong.ai/articles/alibaba-tencent-eye-major-investment-in-deepseek-report/) | techstrong.ai | 8 | negative |
| 23 Apr 2026 | [Deepseek ‘In Talks’ to Raise Funds at $20 Bn Valuation](https://aidatainsider.com/news/deepseek-in-talks-to-raise-funds-at-20-bn-valuation/) | aidatainsider.com | 8 | positive |
| 23 Apr 2026 | [Bitcoin Nears $80,000 But Hedge Fund Founder Says It's Still In 'No-Trade Zone'](https://ibtimes.co.uk/bitcoin-surges-past-79000-us-iran-ceasefire-1793245) | ibtimes.co.uk | 8 | positive |
| 22 Apr 2026 | [Is DeepSeek Raising Funds at $20 Billion Valuation? \| Analytics India Magazine](https://analyticsindiamag.com/ai-news/deepseek-in-talks-to-raise-funds-at-20-billion-valuation) | analyticsindiamag.com | 8 | positive |
| 22 Apr 2026 | [DeepSeek isn’t short of cash: so why has it decided to raise funds anyway?](https://www.scmp.com/tech/article/3351004/why-chinas-cash-rich-ai-firm-deepseek-still-shopping-funding-sources) | scmp.com | 8 | negative |
| 20 Apr 2026 | [Austin-based hedge fund manager pleads guilty to tax evasion](https://www.yahoo.com/news/articles/austin-based-hedge-fund-manager-210726197.html) | yahoo.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "hedge fund" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "hedge fund" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "hedge fund" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "hedge fund" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "hedge fund", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "hedge fund", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`news_overview`, `news_sentiment`, `news_trends`, `search_business_news`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Window: 1 Jan – 30 Apr 2026 for counts, tone and headlines; May 2025 – Apr 2026 for the monthly series. News intake thins after May 2026.
- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Part of the news index is temporarily offline; this answer uses about 86% of indexed articles, so counts are lower bounds.
- Tone shares use articles with a recognized sentiment; critical share uses articles with a priority rating.
- since 2025-05-01 is earlier than the plan's history_days (365); clamped to 2025-08-24
- zero-count periods are included; partial_period marks buckets the window only partly covers
- shares divide by articles carrying a sentiment label (one label per article: the top-scoring one)

## Related use cases

- [GDP News](gdp-news.md)
- [Credit Card News](credit-card-news.md)
- [Dividend News](dividend-news.md)
- [Unemployment News](unemployment-news.md)
