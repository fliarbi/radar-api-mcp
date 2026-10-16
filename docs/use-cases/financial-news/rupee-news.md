# Rupee News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “rupee news” · 2,400/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [rupee-news.json](../../examples/use-cases/rupee-news.json).

**Question.** How much news did rupee receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,291 |
| Negative · neutral · positive | 70% · 1.0% · 29% |
| Critical (priority 7–9) | 63% (3,931 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,619 articles) |
| Negative-to-positive vs all news | 3.23× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 283 | 62% | 191 | 85 | ██ |
| Sep 2025 | 1,083 | 62% | 672 | 392 | ████████ |
| Oct 2025 | 645 | 55% | 321 | 317 | █████ |
| Nov 2025 | 715 | 52% | 446 | 264 | █████ |
| Dec 2025 | 1,656 | 64% | 1,118 | 502 | █████████████ |
| Jan 2026 | 995 | 66% | 672 | 312 | ████████ |
| Feb 2026 | 888 | 56% | 378 | 496 | ███████ |
| Mar 2026 | 1,789 | 74% | 1,374 | 397 | ██████████████ |
| Apr 2026 | 2,619 | 55% | 1,962 | 633 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 12 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [UPSC Key: Internationalisation of the Rupee, Panchayat Advancement Index and E-PRAAPTI](https://indianexpress.com/article/upsc-current-affairs/upsc-key-internationalisation-of-the-rupee-panchayat-advancement-index-and-e-praapti-10664476/) | indianexpress.com | 8 | positive |
| 30 Apr 2026 | [Indian Rupee Plunges to a Historic Low Against US Dollar At ₹95.20 Sparks Economic Concerns - PUNE PULSE](https://www.mypunepulse.com/indian-rupee-plunges-to-a-historic-low-against-us-dollar-at-%e2%82%b995-20-sparks-economic-concerns/) | mypunepulse.com | 8 | negative |
| 30 Apr 2026 | [Castrol India bets on pricing actions, cost efficiency as crude, FX volatility persists: CFO Srinivasan](https://cfo.economictimes.indiatimes.com/news/strategy-operations/castrol-india-plans-to-tackle-crude-and-currency-volatility-with-price-hikes-and-cost-cuts/130611130) ⚠ | cfo.economictimes.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [Rupee Sinks to Record Low 95.23: Oil Price Spike and Fed Stance Crush INR - Business League](https://www.businessleague.in/rupee-sinks-to-record-low-95-23-oil-price-spike-and-fed-stance-crush-inr/) | businessleague.in | 8 | negative |
| 30 Apr 2026 | [Rupee plumbs record low of 95.34, closes at 95.91 as crude tops $126/barrel](https://www.newindianexpress.com/business/2026/Apr/30/rupee-plumbs-record-low-of-9534-closes-at-9591-as-crude-tops-126barrel) | newindianexpress.com | 8 | negative |
| 30 Apr 2026 | [Rupee falls 14 paise to close near all-time low level at 94.82 against US dollar](https://www.dtnext.in/news/business/biz-rupee-close-27) | dtnext.in | 8 | negative |
| 30 Apr 2026 | [India’s rupee defence faces tough test as capital flows stall](https://bfsi.economictimes.indiatimes.com/news/industry/indias-rupee-defence-faces-tough-test-as-capital-flows-stall/130624302) | bfsi.economictimes.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [Markets end lower as crude stays high, rupee hits record low](https://www.indiatoday.in/business/market/story/sensex-nifty-fall-as-crude-oil-stays-high-and-rupee-hits-record-low-2903762-2026-04-30) | indiatoday.in | 8 | negative |
| 30 Apr 2026 | [Why market fell today? Sensex slumps 583 pts, Nifty below 24,000; 7 key triggers - The Economic Times](https://economictimes.indiatimes.com/markets/stocks/news/why-market-fell-today-sensex-slumps-583-pts-nifty-below-24000-7-key-triggers/printarticle/130630192.cms) | economictimes.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [Rupee record fall explained: What's weighing the currency and where is it headed? - The Economic Times](https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-record-fall-explained-whats-weighing-the-currency-and-where-is-it-headed/printarticle/130630734.cms) | economictimes.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [Rupee record fall explained: What's weighing the currency and where is it headed?](https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-record-fall-explained-whats-weighing-the-currency-and-where-is-it-headed/articleshow/130630734.cms) | economictimes.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [Rupee's slide to a record low of 95.33 puts RBI back on the defensive](https://www.thehindubusinessline.com/markets/forex/rupees-slide-to-record-low-of-9533-puts-rbi-back-on-the-defensive/article70924238.ece) | thehindubusinessline.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q rupee --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q rupee --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q rupee --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q rupee --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "rupee", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "rupee", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Repo Rate News](repo-rate-news.md)
- [Commercial Real Estate News](commercial-real-estate-news.md)
- [ECB News Today](ecb-news-today.md)
- [Stablecoin News](stablecoin-news.md)
