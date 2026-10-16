# Market Crash News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “market crash news” · 880/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [market-crash-news.json](../../examples/use-cases/market-crash-news.json).

**Question.** How much news did market crash receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 545 |
| Negative · neutral · positive | 76% · 0.2% · 24% |
| Critical (priority 7–9) | 73% (397 articles) |
| Busiest month, May 2025 – Apr 2026 | Oct 2025 (301 articles) |
| Negative-to-positive vs all news | 4.27× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 18 | 83% | 12 | 6 | █ |
| Sep 2025 | 37 | 73% | 26 | 11 | ██ |
| Oct 2025 | 301 | 77% | 204 | 96 | ████████████████████ |
| Nov 2025 | 177 | 83% | 125 | 52 | ████████████ |
| Dec 2025 | 67 | 57% | 57 | 10 | ████ |
| Jan 2026 | 86 | 70% | 63 | 22 | ██████ |
| Feb 2026 | 199 | 75% | 142 | 57 | █████████████ |
| Mar 2026 | 166 | 70% | 139 | 27 | ███████████ |
| Apr 2026 | 94 | 76% | 69 | 25 | ██████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 14 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Why RBI Cancelled Paytm Payments Bank Licence: Vijay Shekhar Sharma Exit And Fintech Shake-Up Explained](https://www.newsx.com/business/why-rbi-cancelled-paytm-payments-bank-licence-vijay-shekhar-sharma-exit-and-fintech-shake-up-explained-207198/) ⚠ | newsx.com | 8 | negative |
| 24 Apr 2026 | [Stock market crash fears soar as Bank of England boss issues dire warning](https://www.express.co.uk/finance/city/2197827/stock-market-crash-bank-of-england-rachel-reeves) | express.co.uk | 8 | negative |
| 22 Apr 2026 | [Lessons Worth Learning About How Much Does a 20000 Mile Service Cost— What Changed in 2026](https://www.thedetroitbureau.com/www-news/lessons-worth-learning-about-how-much-does-a-20000-mile-service-cost-what-changed-in-2026-dhzfr92zjkot) | thedetroitbureau.com | 8 | positive |
| 17 Apr 2026 | [Crypto Fear and Greed Index falls back down to 'extreme fear' levels](https://cryptocurrency.com.tr/crypto-fear-and-greed-index-falls-back-down-to-extreme-fear-levels-274216) | cryptocurrency.com.tr | 8 | negative |
| 15 Apr 2026 | [News And Updates on Cryptocurrency, AI, Gaming and Regulation \| Cryptopolitan](https://www.cryptopolitan.com/binance-us-challenges-secs-proposed-restraining-order/) | cryptopolitan.com | 8 | negative |
| 13 Apr 2026 | [Stock Market Crash Today (13 April 2026): Cigarette Stocks Hit, Top 6 Stocks To Watch Today Amid Market…](https://www.newsx.com/business/stock-market-crash-cigarette-stocks-hit-top-6-stocks-to-watch-today-amid-market-bloodbath-as-failed-us-iran-talks-spark-global-selloff-198279/) | newsx.com | 8 | negative |
| 13 Apr 2026 | [Stock Market Slump Today: Sensex Crashes 1,100 Points, Nifty 50 Falls Under 23,750; 7 Factors Explained](https://www.thehansindia.com/business/hans-invest/stock-market-slump-today-sensex-crashes-1100-points-nifty-50-falls-under-23750-7-factors-explained-1065198) | thehansindia.com | 8 | negative |
| 13 Apr 2026 | [Forget Tariffs: 2 Other Reasons a Stock Market Crash Could Occur Under President Trump](https://cryptocurrency.com.tr/forget-tariffs-2-other-reasons-a-stock-market-crash-could-occur-under-president-trump-274205) | cryptocurrency.com.tr | 8 | negative |
| 9 Apr 2026 | [Several interconnected factors can lead to a sudden and severe stock market crash. These causes often build…](https://www.bajajfinservmarkets.in/discover/understanding-stock-market-crashes) | bajajfinservmarkets.in | 8 | negative |
| 9 Apr 2026 | [आज शेयर मार्केट क्रैश होने के क्या हैं 5 कारण? अभी एक दिन पहले आई थी तूफानी तेजी](https://www.livehindustan.com/business/what-are-the-5-reasons-behind-stock-market-crash-today-just-a-day-ago-it-witnessed-a-massive-surge-201775713613916.html) | livehindustan.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "market crash" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "market crash" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "market crash" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "market crash" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "market crash", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "market crash", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Treasury Yields News](treasury-yields-news.md)
- [Yen News](yen-news.md)
- [Tax News Today](tax-news-today.md)
- [IMF News](imf-news.md)
