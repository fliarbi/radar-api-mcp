# Private Equity News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “private equity news” · 140/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [private-equity-news.json](../../examples/use-cases/private-equity-news.json).

**Question.** How much news did private equity receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 11,889 |
| Negative · neutral · positive | 17% · 1.8% · 81% |
| Critical (priority 7–9) | 49% (5,792 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (3,737 articles) |
| Negative-to-positive vs all news | 0.28× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 513 | 47% | 68 | 435 | ███ |
| Sep 2025 | 2,518 | 50% | 317 | 2,133 | █████████████ |
| Oct 2025 | 2,270 | 48% | 286 | 1,934 | ████████████ |
| Nov 2025 | 2,404 | 46% | 302 | 2,053 | █████████████ |
| Dec 2025 | 2,489 | 47% | 329 | 2,098 | █████████████ |
| Jan 2026 | 2,670 | 48% | 332 | 2,288 | ██████████████ |
| Feb 2026 | 3,737 | 51% | 865 | 2,807 | ████████████████████ |
| Mar 2026 | 2,643 | 49% | 385 | 2,205 | ██████████████ |
| Apr 2026 | 2,839 | 46% | 412 | 2,365 | ███████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 12 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Unprecedented- Private Equity Firm Potentially on Hook for Portfolio Company’s Data Breach](https://natlawreview.com/article/unprecedented-private-equity-firm-potentially-hook-portfolio-companys-data-breach) | natlawreview.com | 8 | negative |
| 30 Apr 2026 | [Higher Education Market Size Accelerating at 6.5 % CAGR \| By Key Players: Adobe Systems, Apple, Blackboard,…](https://www.openpr.com/news/4496381/higher-education-market-size-accelerating-at-6-5-cagr-by-key) ⚠ | openpr.com | 8 | negative |
| 30 Apr 2026 | [The New Era in Tech Investing Starts Now](https://www.bain.com/es-es/insights/new-era-in-tech-investing-starts-now/) | bain.com | 8 | positive |
| 29 Apr 2026 | [Digital Therapeutics Market Size Accelerating at 24.8% CAGR \| By Key Players: Pear Therapeutics, Omada…](https://www.openpr.com/news/4494132/digital-therapeutics-market-size-accelerating-at-24-8-cagr) ⚠ | openpr.com | 8 | positive |
| 29 Apr 2026 | [Kyberswap Exploiter Moves 2,900 ETH to Tornado Cash Two Years After $65M Heist](https://cryptocurrency.com.tr/kyberswap-exploiter-moves-2-900-eth-to-tornado-cash-two-years-after-65m-heist-288971) | cryptocurrency.com.tr | 8 | negative |
| 28 Apr 2026 | [India Real Estate: Domestic Capital Dominates at 76%](https://www.newkerala.com/news/a/domestic-capital-drives-76-indias-real-estate-investment-959.htm) ⚠ | newkerala.com | 8 | positive |
| 28 Apr 2026 | [IT firm Virtusa eyes India IPO, could raise over $1 billion](https://www.thehindubusinessline.com/markets/it-firm-virtusa-eyes-india-ipo-could-raise-over-1-billion/article70915980.ece) | thehindubusinessline.com | 8 | positive |
| 28 Apr 2026 | [Why Goldman Sachs still sees $160bn in IPO proceeds despite fewer expected](https://business-news-today.com/why-goldman-sachs-still-sees-160bn-in-ipo-proceeds-despite-fewer-expected-listings/) ⚠ | business-news-today.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "private equity" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "private equity" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "private equity" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "private equity" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "private equity", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "private equity", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Mutual Fund News](mutual-fund-news.md)
- [Mergers and Acquisitions News](mergers-and-acquisitions-news.md)
- [Pension News](pension-news.md)
- [Repo Rate News](repo-rate-news.md)
