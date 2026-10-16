# Sensex News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “sensex news” · 6,600/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [sensex-news.json](../../examples/use-cases/sensex-news.json).

**Question.** How much news did sensex receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 11,088 |
| Negative · neutral · positive | 47% · 0.8% · 52% |
| Critical (priority 7–9) | 41% (4,556 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,520 articles) |
| Negative-to-positive vs all news | 1.21× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 684 | 49% | 331 | 345 | ████ |
| Sep 2025 | 2,675 | 40% | 869 | 1,768 | ███████████████ |
| Oct 2025 | 1,749 | 27% | 362 | 1,379 | ██████████ |
| Nov 2025 | 1,766 | 29% | 563 | 1,200 | ██████████ |
| Dec 2025 | 1,840 | 30% | 747 | 1,081 | ██████████ |
| Jan 2026 | 1,911 | 44% | 948 | 951 | ███████████ |
| Feb 2026 | 2,854 | 30% | 941 | 1,871 | ████████████████ |
| Mar 2026 | 2,803 | 49% | 1,812 | 986 | ████████████████ |
| Apr 2026 | 3,520 | 42% | 1,492 | 2,000 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 14 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 8 Apr 2026 | [Oil Prices Plunge After Iran Ceasefire Announcement - IndiaWest News](https://indiawest.com/oil-prices-plunge-after-iran-ceasefire-announcement/) ⚠ | indiawest.com | 9 | negative |
| 23 Mar 2026 | [Investor panic deepens stocks crash, bear markets loom](https://www.forbesindia.com/article/upfront/take-one-big-story-of-the-day/investor-panic-deepens-stocks-crash-bear-markets-loom/2992386/1) ⚠ | forbesindia.com | 9 | negative |
| 30 Apr 2026 | [Sensex, Nifty end 7 per cent higher in April](https://www.thehindubusinessline.com/markets/stock-markets/sensex-nifty-end-7-per-cent-higher-in-april/article70926006.ece) | thehindubusinessline.com | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty fall amid FII selling and surge in crude oil prices](https://www.newindianexpress.com/business/2026/Apr/30/sensex-nifty-fall-amid-fii-selling-and-surge-in-crude-oil-prices) | newindianexpress.com | 8 | negative |
| 30 Apr 2026 | [Indian Bank Sees Sharp Open Interest Surge Amidst Weak Price Action](https://www.marketsmojo.com/news/stocks-in-action/indian-bank-sees-sharp-open-interest-surge-amidst-weak-price-action-3970315) ⚠ | marketsmojo.com | 8 | positive |
| 30 Apr 2026 | [Asia Intelligence Brief for Thursday, April 30, 2026](https://www.riotimesonline.com/asia-pulse-brent-samsung-boj-india-april-30-2026/) ⚠ | riotimesonline.com | 8 | negative |
| 30 Apr 2026 | [Rupee falls 14 paise to close near all-time low level at 94.82 against US dollar](https://www.dtnext.in/news/business/biz-rupee-close-27) ⚠ | dtnext.in | 8 | negative |
| 30 Apr 2026 | [Markets end lower as crude stays high, rupee hits record low](https://www.indiatoday.in/business/market/story/sensex-nifty-fall-as-crude-oil-stays-high-and-rupee-hits-record-low-2903762-2026-04-30) | indiatoday.in | 8 | negative |
| 30 Apr 2026 | [Why market fell today? Sensex slumps 583 pts, Nifty below 24,000; 7 key triggers - The Economic Times](https://economictimes.indiatimes.com/markets/stocks/news/why-market-fell-today-sensex-slumps-583-pts-nifty-below-24000-7-key-triggers/printarticle/130630192.cms) | economictimes.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [Rupee falls to record low of 95.3 against US dollars as oil prices surge](https://scroll.in/latest/1092497/rupee-falls-to-record-low-of-95-3-against-us-dollars-as-oil-prices-surge) ⚠ | scroll.in | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty Fall Nearly 1% Today: Oil Price Surge Weighs on Sentiment - Business League](https://www.businessleague.in/sensex-nifty-fall-nearly-1-today-oil-price-surge-weighs-on-sentiment/) | businessleague.in | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q sensex --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q sensex --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q sensex --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q sensex --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "sensex", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "sensex", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [SEBI News](sebi-news.md)
- [Income Tax News](income-tax-news.md)
- [Inflation News](inflation-news.md)
- [Venture Capital News Today](venture-capital-news-today.md)
