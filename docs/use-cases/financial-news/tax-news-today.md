# Tax News Today: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “tax news today” · 720/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [tax-news-today.json](../../examples/use-cases/tax-news-today.json).

**Question.** How much news did tax receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 83,768 |
| Negative · neutral · positive | 43% · 8.3% · 49% |
| Critical (priority 7–9) | 54% (45,559 articles) |
| Busiest month, May 2025 – Apr 2026 | Dec 2025 (28,969 articles) |
| Negative-to-positive vs all news | 1.19× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 4,094 | 60% | 1,961 | 1,782 | ███ |
| Sep 2025 | 18,466 | 59% | 8,094 | 9,049 | █████████████ |
| Oct 2025 | 14,887 | 63% | 7,487 | 6,337 | ██████████ |
| Nov 2025 | 13,543 | 61% | 6,324 | 6,269 | █████████ |
| Dec 2025 | 28,969 | 27% | 6,103 | 21,710 | ████████████████████ |
| Jan 2026 | 13,992 | 58% | 6,001 | 6,889 | ██████████ |
| Feb 2026 | 21,259 | 63% | 9,404 | 10,269 | ███████████████ |
| Mar 2026 | 23,684 | 45% | 8,576 | 13,171 | ████████████████ |
| Apr 2026 | 24,833 | 54% | 11,936 | 10,494 | █████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 18 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 12 Apr 2026 | [Irish PM moves to cut fuel tax](https://www.bostonherald.com/2026/04/12/irish-pm-moves-to-cut-fuel-tax/) | bostonherald.com | 9 | negative |
| 7 Jan 2026 | [The 2025 Los Angeles Wildfires: Lessons and Key Recommendations: Policy Report - Independent Institute](https://www.independent.org/article/2026/01/07/the-2025-los-angeles-wildfires-lessons-and-key-recommendations/) ⚠ | independent.org | 9 | negative |
| 30 Apr 2026 | [Ford Expects $1.3 Billion in Tariff Refunds After SCOTUS Ruling](http://autoweek.com/news/a71177860/ford-expects-13-billion-tariff-refunds/) | autoweek.com | 8 | negative |
| 30 Apr 2026 | [Tax refunds and AI boom have offset some US economic pain from Iran war and high gas prices, so far](https://www.sandiegouniontribune.com/2026/04/30/economy-iran-war/) | sandiegouniontribune.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q tax --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q tax --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q tax --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q tax --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "tax", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "tax", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Yen News](yen-news.md)
- [Market Crash News](market-crash-news.md)
- [IMF News](imf-news.md)
- [NBFC News](nbfc-news.md)
