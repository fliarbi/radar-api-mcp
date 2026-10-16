# IPO News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “ipo news” · 14,800/month India · 2,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [ipo-news.json](../../examples/use-cases/ipo-news.json).

**Question.** How much news did ipo receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 37,426 |
| Negative · neutral · positive | 26% · 2.1% · 72% |
| Critical (priority 7–9) | 67% (24,942 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (12,478 articles) |
| Negative-to-positive vs all news | 0.49× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 1,842 | 58% | 282 | 1,525 | ███ |
| Sep 2025 | 12,478 | 70% | 2,357 | 9,942 | ████████████████████ |
| Oct 2025 | 6,726 | 64% | 939 | 5,694 | ███████████ |
| Nov 2025 | 6,951 | 64% | 1,094 | 5,697 | ███████████ |
| Dec 2025 | 8,209 | 60% | 1,077 | 6,948 | █████████████ |
| Jan 2026 | 6,507 | 65% | 896 | 5,479 | ██████████ |
| Feb 2026 | 12,005 | 73% | 4,962 | 6,848 | ███████████████████ |
| Mar 2026 | 8,290 | 63% | 1,672 | 6,408 | █████████████ |
| Apr 2026 | 10,624 | 64% | 2,210 | 8,161 | █████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 15 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Feb 2026 | [Elon Musk Allows To 'Use Starlink For Anything To Help Ukraine,' But What Do Prediction Markets Say?](https://www.benzinga.com/markets/prediction-markets/26/02/50939711/elon-musk-allows-to-use-starlink-for-anything-to-help-ukraine-but-what-do-prediction-markets-say) ⚠ | benzinga.com | 9 | negative |
| 30 Apr 2026 | [SoftBank Eyes $100bn AI Infrastructure Spin-Off as Masayoshi Son Doubles Down on America’s Data Center Boom…](https://www.tekedia.com/softbank-eyes-100bn-ai-infrastructure-spin-off-as-masayoshi-son-doubles-down-on-americas-data-center-boom/) ⚠ | tekedia.com | 8 | positive |
| 30 Apr 2026 | [Zeta Global RevenueGrowth Accelerates to 50% and “Beats and Raises” for its 19th Consecutive Quarter on the…](https://zetaglobal.com/news/zeta-global-revenuegrowth-accelerates-to-50-and-beats-and-raises-for-its-19th-consecutive-quarter-on-the-he/) ⚠ | zetaglobal.com | 8 | positive |
| 30 Apr 2026 | [Big Tech is about to spend $700 billion on AI this year. No one knows where the buildout ends. \| Fortune](https://www.fortune.com/2026/04/30/big-tech-hyperscalers-will-spend-700-billion-on-ai-infrastructure-this-year-with-no-clear-end-in-sight-eye-on-ai/) ⚠ | fortune.com | 8 | positive |
| 30 Apr 2026 | [SpaceX sale a bolsa: la OPI más grande de la historia podría valer $2 billones](https://elplaneta.com/2026/04/30/nacionales/spacex-sale-a-bolsa-la-opi-mas-grande-de-la-historia-podria-valer-2-billones/) ⚠ | elplaneta.com | 8 | positive |
| 30 Apr 2026 | [NYSE Content Update: NASA's Jared Isaacman Celebrates Artemis II Success at NYSE](https://www.newswire.ca/news-releases/nyse-content-update-nasa-s-jared-isaacman-celebrates-artemis-ii-success-at-nyse-864991476.html) ⚠ | newswire.ca | 8 | positive |
| 30 Apr 2026 | [Meesho to appeal $1.5m tax demand in India](https://www.startupnews.fyi/ecommerce/meesho-to-appeal-1-5m-tax-demand-in-india) ⚠ | startupnews.fyi | 8 | negative |
| 30 Apr 2026 | [PA Daily News \| Tether leads $14 million Series A funding round for Belo; Squads completes $18 million…](https://www.panewslab.com/en/articles/019ddda0-c24c-77ca-9afc-8ccd6c719cc3) ⚠ | panewslab.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q IPO --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q IPO --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q IPO --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q IPO --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "IPO", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "IPO", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Gold Price News](gold-price-news.md)
- [Housing Market News](housing-market-news.md)
- [RBI News](rbi-news.md)
- [Nifty News](nifty-news.md)
