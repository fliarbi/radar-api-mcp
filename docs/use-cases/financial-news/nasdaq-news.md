# Nasdaq News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “nasdaq news” · 1,600/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [nasdaq-news.json](../../examples/use-cases/nasdaq-news.json).

**Question.** How much news did nasdaq receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 145,799 |
| Negative · neutral · positive | 18% · 2.5% · 79% |
| Critical (priority 7–9) | 33% (48,345 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (51,663 articles) |
| Negative-to-positive vs all news | 0.32× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 4,971 | 44% | 754 | 4,160 | ██ |
| Sep 2025 | 23,677 | 43% | 3,550 | 19,735 | █████████ |
| Oct 2025 | 20,316 | 52% | 4,134 | 14,837 | ████████ |
| Nov 2025 | 20,815 | 55% | 4,970 | 15,239 | ████████ |
| Dec 2025 | 19,553 | 50% | 4,214 | 14,401 | ████████ |
| Jan 2026 | 29,528 | 31% | 4,292 | 24,540 | ███████████ |
| Feb 2026 | 34,117 | 35% | 5,657 | 27,680 | █████████████ |
| Mar 2026 | 30,491 | 41% | 7,143 | 22,549 | ████████████ |
| Apr 2026 | 51,663 | 28% | 9,858 | 40,338 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 15 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 17 Apr 2026 | [Markets Shatter Records As Trump Unlocks The Strait of Hormuz - APA (NASDAQ:APA)](https://benzinga.com/markets/equities/26/04/51898649/markets-records-trump-iran-strait-hormuz-week-wall-street) | benzinga.com | 9 | negative |
| 16 Apr 2026 | [Energy chief warns Europe only has six weeks of fuel left](https://finance.yahoo.com/sectors/energy/articles/energy-chief-warns-europe-only-182300136.html) ⚠ | finance.yahoo.com | 9 | negative |
| 9 Apr 2026 | [Petrol and diesel prices rise again as concerns grow over ceasefire](https://www.capitalfm.co.ke/business/2026/04/petrol-and-diesel-prices-rise-again-as-concerns-grow-over-ceasefire/) ⚠ | capitalfm.co.ke | 9 | negative |
| 9 Apr 2026 | [Asian Markets Retreat as Gulf Crisis Fuels Oil Surge and Inflation Fears - EconoTimes](https://econotimes.com/Asian-Markets-Retreat-as-Gulf-Crisis-Fuels-Oil-Surge-and-Inflation-Fears-1738517) ⚠ | econotimes.com | 9 | negative |
| 8 Apr 2026 | [Bitcoin Rises, Oil Falls as US–Iran Ceasefire Eases Fears](https://bitcoinethereumnews.com/bitcoin/bitcoin-rises-oil-falls-as-us-iran-ceasefire-eases-fears/) ⚠ | bitcoinethereumnews.com | 9 | negative |
| 1 Apr 2026 | [Trump declares 'job done,' says U.S. forces to leave Iran in 2-3 weeks](https://www.yahoo.com/news/articles/trump-declares-job-done-says-110838829.html) ⚠ | yahoo.com | 9 | negative |
| 31 Mar 2026 | [The Latest: Iran strikes a fully loaded oil tanker off Dubai coast as gas reaches $4 a gallon in US \| 1010…](https://www.audacy.com/1010wins/news/world/ap-ml-iran-us-the-latest-40th-ld-writethru) ⚠ | audacy.com | 9 | negative |
| 31 Mar 2026 | [The Latest: Iran strikes a fully loaded oil tanker off Dubai coast as gas reaches $4 a gallon in US \| KNX…](https://www.audacy.com/knxnews/news/world/ap-ml-iran-us-the-latest-38th-ld-writethru) ⚠ | audacy.com | 9 | negative |
| 31 Mar 2026 | [The Latest: Iran strikes a fully loaded oil tanker off Dubai coast as gas reaches $4 a gallon in US \| KYW…](https://www.audacy.com/kywnewsradio/news/world/ap-ml-iran-us-the-latest-38th-ld-writethru) ⚠ | audacy.com | 9 | negative |
| 27 Mar 2026 | [Markets lose faith with Donald Trump as we approach Easter Week](https://www.xtb.com/en/market-analysis/markets-lose-faith-with-donald-trump-as-we-approach-easter-week) ⚠ | xtb.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q nasdaq --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q nasdaq --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q nasdaq --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q nasdaq --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "nasdaq", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "nasdaq", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Inflation News](inflation-news.md)
- [Venture Capital News Today](venture-capital-news-today.md)
- [Recession News](recession-news.md)
- [Bank of Japan News](bank-of-japan-news.md)
