# Bank of Japan News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “bank of japan news” · 880/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [bank-of-japan-news.json](../../examples/use-cases/bank-of-japan-news.json).

**Question.** How much news did bank of japan receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,566 |
| Negative · neutral · positive | 71% · 4.4% · 24% |
| Critical (priority 7–9) | 77% (1,207 articles) |
| Busiest month, May 2025 – Apr 2026 | Dec 2025 (941 articles) |
| Negative-to-positive vs all news | 4.01× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 54 | 89% | 32 | 22 | █ |
| Sep 2025 | 256 | 75% | 162 | 76 | █████ |
| Oct 2025 | 297 | 82% | 174 | 115 | ██████ |
| Nov 2025 | 240 | 80% | 182 | 57 | █████ |
| Dec 2025 | 941 | 74% | 652 | 277 | ████████████████████ |
| Jan 2026 | 252 | 76% | 181 | 66 | █████ |
| Feb 2026 | 322 | 78% | 220 | 95 | ███████ |
| Mar 2026 | 439 | 80% | 323 | 91 | █████████ |
| Apr 2026 | 553 | 75% | 395 | 126 | ████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 18 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Japan needs a new framework for a post-deflation economy - OMFIF](https://www.omfif.org/2026/04/japan-needs-a-new-framework-for-a-post-deflation-economy/) | omfif.org | 8 | negative |
| 29 Apr 2026 | [Dollar Surges as U.S.-Iran Tensions Push Traders Into Safe Haven \| The Currency analytics](https://thecurrencyanalytics.com/finance/dollar-surges-as-u-s-iran-tensions-push-traders-into-safe-haven-255339) ⚠ | thecurrencyanalytics.com | 8 | negative |
| 28 Apr 2026 | [US stocks edge up to more records, while oil prices rise ahead of a blockbuster week for Wall Street - WTVQ](https://www.wtvq.com/us-stocks-edge-up-to-more-records-while-oil-prices-rise-ahead-of-a-blockbuster-week-for-wall-street/) ⚠ | wtvq.com | 8 | positive |
| 28 Apr 2026 | [The BoJ will continue raising rates in Japan, but the pace is highly uncertain](https://www.oxfordeconomics.com/resource/the-boj-will-continue-raising-rates-in-japan-but-the-pace-is-highly-uncertain/) | oxfordeconomics.com | 8 | positive |
| 28 Apr 2026 | [USD/JPY steadies after hawkish BoJ as Middle East tensions lift Dollar](https://bitcoinethereumnews.com/finance/usd-jpy-steadies-after-hawkish-boj-as-middle-east-tensions-lift-dollar/) | bitcoinethereumnews.com | 8 | negative |
| 28 Apr 2026 | [BOJ: Gradual tightening with higher inflation risks – UOB](https://bitcoinethereumnews.com/finance/boj-gradual-tightening-with-higher-inflation-risks-uob/) | bitcoinethereumnews.com | 8 | neutral |
| 28 Apr 2026 | [USD/JPY: BoJ split vote lifts normalization risks – BNY](https://bitcoinethereumnews.com/finance/usd-jpy-boj-split-vote-lifts-normalization-risks-bny/) | bitcoinethereumnews.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "bank of japan" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "bank of japan" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "bank of japan" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "bank of japan" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "bank of japan", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "bank of japan", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Nasdaq News](nasdaq-news.md)
- [Recession News](recession-news.md)
- [US Dollar News](us-dollar-news.md)
- [Crude Oil Price News](crude-oil-price-news.md)
