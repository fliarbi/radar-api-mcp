# US Dollar News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “us dollar news” · 1,900/month India · 2,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [us-dollar-news.json](../../examples/use-cases/us-dollar-news.json).

**Question.** How much news did us dollar receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 12,990 |
| Negative · neutral · positive | 63% · 3.4% · 33% |
| Critical (priority 7–9) | 44% (5,710 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (5,327 articles) |
| Negative-to-positive vs all news | 2.57× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 471 | 51% | 270 | 186 | ██ |
| Sep 2025 | 1,782 | 48% | 853 | 865 | ███████ |
| Oct 2025 | 2,423 | 38% | 956 | 1,433 | █████████ |
| Nov 2025 | 1,863 | 49% | 1,015 | 798 | ███████ |
| Dec 2025 | 1,914 | 58% | 1,147 | 708 | ███████ |
| Jan 2026 | 2,016 | 58% | 1,213 | 744 | ████████ |
| Feb 2026 | 2,625 | 53% | 1,573 | 957 | ██████████ |
| Mar 2026 | 3,022 | 47% | 2,038 | 881 | ███████████ |
| Apr 2026 | 5,327 | 33% | 3,396 | 1,740 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 13 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Mar 2026 | [MEA debunks 'fake' claims on fertiliser unit closures due to LNG shortage - Yes Punjab News](https://yespunjab.com/mea-debunks-fake-claims-on-fertiliser-unit-closures-due-to-lng-shortage/) ⚠ | yespunjab.com | 9 | negative |
| 30 Apr 2026 | [The sources, one government and another a market source, spoke on condition of anonymity as they were not…](https://www.yarrawongachronicle.com.au/aap-finance/japan-intervenes-to-counter-currency-weakness-sources/) | yarrawongachronicle.com.au | 8 | negative |
| 30 Apr 2026 | [Sensex, Nifty end 7 per cent higher in April](https://www.thehindubusinessline.com/markets/stock-markets/sensex-nifty-end-7-per-cent-higher-in-april/article70926006.ece) ⚠ | thehindubusinessline.com | 8 | negative |
| 30 Apr 2026 | [US Seizes $500M in Iran-Linked Crypto Amid Intensified Sanctions](https://thenewscrypto.com/us-seizes-500m-in-iran-linked-crypto-amid-intensified-sanctions/) | thenewscrypto.com | 8 | negative |
| 30 Apr 2026 | [Indian Rupee Plunges to a Historic Low Against US Dollar At ₹95.20 Sparks Economic Concerns - PUNE PULSE](https://www.mypunepulse.com/indian-rupee-plunges-to-a-historic-low-against-us-dollar-at-%e2%82%b995-20-sparks-economic-concerns/) | mypunepulse.com | 8 | negative |
| 30 Apr 2026 | [Rupee Sinks to Record Low 95.23: Oil Price Spike and Fed Stance Crush INR - Business League](https://www.businessleague.in/rupee-sinks-to-record-low-95-23-oil-price-spike-and-fed-stance-crush-inr/) | businessleague.in | 8 | negative |
| 30 Apr 2026 | [Rupee falls 14 paise to close near all-time low level at 94.82 against US dollar](https://www.dtnext.in/news/business/biz-rupee-close-27) | dtnext.in | 8 | negative |
| 30 Apr 2026 | [Rupee falls to record low of 95.3 against US dollars as oil prices surge](https://scroll.in/latest/1092497/rupee-falls-to-record-low-of-95-3-against-us-dollars-as-oil-prices-surge) | scroll.in | 8 | negative |
| 30 Apr 2026 | [Oil Surges to Wartime Highs as Supply Shock Deepens - Comments from Century Financial - Middle East News 247](https://menews247.com/oil-surges-to-wartime-highs-as-supply-shock-deepens-comments-from-century-financial/) | menews247.com | 8 | positive |
| 30 Apr 2026 | [Rupee falls 14 paise amid high crude prices, foreign outflows and West Asia tensions](https://www.mid-day.com/mumbai/mumbai-news/article/rupee-falls-14-paise-amid-high-crude-prices-foreign-outflows-and-west-asia-tensions-23628134) | mid-day.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "us dollar" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "us dollar" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "us dollar" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "us dollar" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "us dollar", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "us dollar", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Recession News](recession-news.md)
- [Bank of Japan News](bank-of-japan-news.md)
- [Crude Oil Price News](crude-oil-price-news.md)
- [Fintech News](fintech-news.md)
