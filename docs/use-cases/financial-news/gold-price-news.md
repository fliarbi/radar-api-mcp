# Gold Price News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “gold price news” · 22,200/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [gold-price-news.json](../../examples/use-cases/gold-price-news.json).

**Question.** How much news did gold price receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,236 |
| Negative · neutral · positive | 39% · 2.1% · 59% |
| Critical (priority 7–9) | 14% (319 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (681 articles) |
| Negative-to-positive vs all news | 0.91× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 75 | 32% | 27 | 46 | ██ |
| Sep 2025 | 445 | 17% | 83 | 358 | █████████████ |
| Oct 2025 | 603 | 18% | 194 | 384 | ██████████████████ |
| Nov 2025 | 314 | 20% | 106 | 198 | █████████ |
| Dec 2025 | 346 | 15% | 99 | 243 | ██████████ |
| Jan 2026 | 482 | 13% | 158 | 318 | ██████████████ |
| Feb 2026 | 527 | 15% | 172 | 347 | ███████████████ |
| Mar 2026 | 546 | 16% | 261 | 274 | ████████████████ |
| Apr 2026 | 681 | 13% | 288 | 370 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 14 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Gold price today: Rates lacklustre on MCX ahead of US Fed policy outcome; experts highlight key levels to…](https://www.livemint.com/market/commodities/gold-price-today-rates-lacklustre-on-mcx-ahead-of-us-fed-policy-outcome-experts-highlight-key-levels-to-watch-11777432566435.html) | livemint.com | 8 | negative |
| 28 Apr 2026 | [Gold prices volatile on MCX as strong dollar, high oil prices weigh; US Fed policy outcome in focus \| Stock…](https://www.livemint.com/market/commodities/gold-price-today-gold-rate-volatile-on-mcx-as-strong-dollar-high-oil-prices-weigh-us-fed-policy-outcome-in-focus-11777347637884.html) | livemint.com | 8 | negative |
| 22 Apr 2026 | [Gold Price Surge: Trump’s Iran Ceasefire Extension Sparks Market Uncertainty Amid Stalled Peace Talks](https://bitcoinworld.co.in/gold-price-surge-trump-iran-ceasefire/) | bitcoinworld.co.in | 8 | positive |
| 17 Apr 2026 | [After five weeks, forex reserves reclaim $700-billion mark](https://www.newindianexpress.com/business/2026/Apr/17/after-five-weeks-forex-reserves-reclaim-700-billion-mark) | newindianexpress.com | 8 | negative |
| 17 Apr 2026 | [Ripple’s Global Payments Expansion Strengthens XRP’s Institutional Role](https://cryptocurrency.com.tr/ripple-s-global-payments-expansion-strengthens-xrp-s-institutional-role-274236) | cryptocurrency.com.tr | 8 | negative |
| 15 Apr 2026 | [Gold Price Today 15 April 2026: Yellow Metal Retraces from One-Month High as US-Iran Peace Talks Loom -…](https://www.businessleague.in/gold-price-today-15-april-2026-yellow-metal-retraces-from-one-month-high-as-us-iran-peace-talks-loom/) | businessleague.in | 8 | negative |
| 13 Apr 2026 | [US Judge Throws out Lawsuit Against Binance and CZ Over Claims of Funding Linked to Violent Attacks](https://cryptocurrency.com.tr/us-judge-throws-out-lawsuit-against-binance-and-cz-over-claims-of-funding-linked-to-violent-attacks-274234) | cryptocurrency.com.tr | 8 | negative |
| 6 Apr 2026 | [Gold price today: Why is gold rate down? Check latest gold price prediction for 2026](http://economictimes.indiatimes.com/news/international/us/gold-price-today-why-is-gold-rate-down-check-latest-gold-price-prediction-for-2026/articleshow/130048847.cms) | economictimes.indiatimes.com | 8 | negative |
| 5 Apr 2026 | [Gold & Silver Rates Today Live: RBI Rates Decision Next Week Will Decide Fate Of Precious Metals?](https://www.goodreturns.in/news/gold-rates-silver-rates-today-live-mcx-gold-silver-price-24k-22k-18k-gold-prices-predictions-april-6-1500461.html) | goodreturns.in | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "gold price" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "gold price" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "gold price" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "gold price" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "gold price", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "gold price", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Crypto News](crypto-news.md)
- [GST News](gst-news.md)
- [Housing Market News](housing-market-news.md)
- [IPO News](ipo-news.md)
