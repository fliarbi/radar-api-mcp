# Nifty News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “nifty news” · 14,800/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [nifty-news.json](../../examples/use-cases/nifty-news.json).

**Question.** How much news did nifty receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 15,321 |
| Negative · neutral · positive | 38% · 1.1% · 61% |
| Critical (priority 7–9) | 34% (5,204 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (5,711 articles) |
| Negative-to-positive vs all news | 0.83× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 761 | 41% | 308 | 440 | ███ |
| Sep 2025 | 3,614 | 31% | 891 | 2,685 | █████████████ |
| Oct 2025 | 2,152 | 26% | 393 | 1,745 | ████████ |
| Nov 2025 | 2,164 | 29% | 592 | 1,547 | ████████ |
| Dec 2025 | 2,166 | 30% | 734 | 1,414 | ████████ |
| Jan 2026 | 2,380 | 38% | 926 | 1,417 | ████████ |
| Feb 2026 | 5,711 | 21% | 1,489 | 4,110 | ████████████████████ |
| Mar 2026 | 3,379 | 46% | 1,883 | 1,482 | ████████████ |
| Apr 2026 | 3,851 | 39% | 1,449 | 2,380 | █████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 16 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Mar 2026 | [Investor panic deepens stocks crash, bear markets loom](https://www.forbesindia.com/article/upfront/take-one-big-story-of-the-day/investor-panic-deepens-stocks-crash-bear-markets-loom/2992386/1) ⚠ | forbesindia.com | 9 | negative |
| 30 Apr 2026 | [Sensex, Nifty end 7 per cent higher in April](https://www.thehindubusinessline.com/markets/stock-markets/sensex-nifty-end-7-per-cent-higher-in-april/article70926006.ece) | thehindubusinessline.com | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty fall amid FII selling and surge in crude oil prices](https://www.newindianexpress.com/business/2026/Apr/30/sensex-nifty-fall-amid-fii-selling-and-surge-in-crude-oil-prices) | newindianexpress.com | 8 | negative |
| 30 Apr 2026 | [Markets end lower as crude stays high, rupee hits record low](https://www.indiatoday.in/business/market/story/sensex-nifty-fall-as-crude-oil-stays-high-and-rupee-hits-record-low-2903762-2026-04-30) | indiatoday.in | 8 | negative |
| 30 Apr 2026 | [Why market fell today? Sensex slumps 583 pts, Nifty below 24,000; 7 key triggers - The Economic Times](https://economictimes.indiatimes.com/markets/stocks/news/why-market-fell-today-sensex-slumps-583-pts-nifty-below-24000-7-key-triggers/printarticle/130630192.cms) | economictimes.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty Fall Nearly 1% Today: Oil Price Surge Weighs on Sentiment - Business League](https://www.businessleague.in/sensex-nifty-fall-nearly-1-today-oil-price-surge-weighs-on-sentiment/) | businessleague.in | 8 | negative |
| 30 Apr 2026 | [Record High Oil, All-Time Low Rupee Batters Sensex, Nifty; IndiGo, Eternal Top Losers Chart](https://www.freepressjournal.in/business/record-high-oil-rupee-plunge-batter-sensex-nifty-indigo-eternal-top-losers-chart) | freepressjournal.in | 8 | negative |
| 30 Apr 2026 | [6 reasons why markets are falling today: Sensex nosedives 1,100 points, Crude spikes to $125](https://www.financialexpress.com/market/6-reasons-why-markets-are-falling-today-sensex-nosedives-1100-points-nifty-plunges-to-23900-4222994/) | financialexpress.com | 8 | negative |
| 30 Apr 2026 | [Stocks to buy: Nagaraj Shetti recommends Time Technoplast, Gujarat Ambuja Exports shares to buy \| Stock…](https://www.livemint.com/market/stock-market-news/stocks-to-buy-nagaraj-shetti-recommends-time-technoplast-gujarat-ambuja-exports-shares-to-buy-11777528414947.html) | livemint.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q nifty --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q nifty --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q nifty --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q nifty --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "nifty", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "nifty", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [IPO News](ipo-news.md)
- [RBI News](rbi-news.md)
- [Federal Reserve News Today](federal-reserve-news-today.md)
- [Mortgage Rates News](mortgage-rates-news.md)
