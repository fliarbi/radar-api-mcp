# Crude Oil Price News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “crude oil price news” · 3,600/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [crude-oil-price-news.json](../../examples/use-cases/crude-oil-price-news.json).

**Question.** How much news did crude oil price receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 377 |
| Negative · neutral · positive | 90% · 0.8% · 8.8% |
| Critical (priority 7–9) | 52% (196 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (162 articles) |
| Negative-to-positive vs all news | 13.98× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 8 | 0.0% | 7 | 1 | █ |
| Sep 2025 | 27 | 18% | 26 | 1 | ███ |
| Oct 2025 | 27 | 11% | 20 | 7 | ███ |
| Nov 2025 | 21 | 4.8% | 21 | 0 | ███ |
| Dec 2025 | 37 | 19% | 32 | 3 | █████ |
| Jan 2026 | 35 | 8.6% | 33 | 2 | ████ |
| Feb 2026 | 24 | 50% | 24 | 0 | ███ |
| Mar 2026 | 162 | 60% | 150 | 12 | ████████████████████ |
| Apr 2026 | 156 | 53% | 134 | 19 | ███████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 14 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Rupee falls 14 paise to close near all-time low level at 94.82 against US dollar](https://www.dtnext.in/news/business/biz-rupee-close-27) | dtnext.in | 8 | negative |
| 29 Apr 2026 | [Oil soars, stocks dip on Iran worries, earnings in focus after Fed](https://virginiabusiness.com/oil-prices-soar-iran-conflict-fed-rates-steady/) | virginiabusiness.com | 8 | neutral |
| 29 Apr 2026 | [Rupee falls 14 paise to close near all-time low level at 94.82 against US dollar - OrissaPOST](https://www.orissapost.com/rupee-falls-14-paise-to-close-near-all-time-low-level-at-94-82-against-us-dollar/) | orissapost.com | 8 | negative |
| 29 Apr 2026 | [UAE Exits OPEC Amid West Asia Conflict: How Will It Impact Oil Prices? - Outlook Money](https://outlookmoney.com/invest/uae-exits-opec-amid-west-asia-conflict-how-will-it-impact-oil-prices) | outlookmoney.com | 8 | negative |
| 29 Apr 2026 | [Crude Oil Price Today - April 29: Brent Crude Crosses $111 Per Barrel; Check Latest Rates of WTI, Murban](https://www.oneindia.com/india/crude-oil-price-today-april-29-brent-crude-crosses-111-per-barrel-check-latest-rates-of-wti-mu-8072617.html) | oneindia.com | 8 | negative |
| 28 Apr 2026 | [UAE to exit Opec amid continued disruption at Strait of Hormuz](https://article.wn.com/view/2026/04/28/UAE_to_exit_Opec_amid_continued_disruption_at_Strait_of_Horm/) ⚠ | article.wn.com | 8 | negative |
| 23 Apr 2026 | [Crude shock! Petrol, diesel prices may rise by ₹25-28 per litre after elections, says Kotak Institutional…](https://www.livemint.com/market/stock-market-news/petrol-diesel-prices-may-rise-by-rs-25-28-per-litre-after-elections-says-kotak-institutional-equities-11776920085220.html) | livemint.com | 8 | negative |
| 22 Apr 2026 | [WTI drifts lower to mid-$88.00s; US-Iran tensions limit downside](https://bitcoinethereumnews.com/finance/wti-drifts-lower-to-mid-88-00s-us-iran-tensions-limit-downside/) | bitcoinethereumnews.com | 8 | negative |
| 21 Apr 2026 | [US-Iran talks ease oil price concerns, odds of $90 crude drop](https://bitcoinethereumnews.com/tech/us-iran-talks-ease-oil-price-concerns-odds-of-90-crude-drop/) | bitcoinethereumnews.com | 8 | negative |
| 20 Apr 2026 | [Crude Oil Price: Brent at $94.57 as Hormuz Freezes](https://bitcoinethereumnews.com/tech/crude-oil-price-brent-at-94-57-as-hormuz-freezes/) | bitcoinethereumnews.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "crude oil price" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "crude oil price" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "crude oil price" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "crude oil price" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "crude oil price", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "crude oil price", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Bank of Japan News](bank-of-japan-news.md)
- [US Dollar News](us-dollar-news.md)
- [Fintech News](fintech-news.md)
- [Mutual Fund News](mutual-fund-news.md)
