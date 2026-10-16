# Stock Market News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “stock market news” · 74,000/month India · 201,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [stock-market-news.json](../../examples/use-cases/stock-market-news.json).

**Question.** How much news did stock market receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 209,554 |
| Negative · neutral · positive | 26% · 2.7% · 72% |
| Critical (priority 7–9) | 29% (59,809 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (76,341 articles) |
| Negative-to-positive vs all news | 0.49× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 8,853 | 36% | 1,991 | 6,700 | ██ |
| Sep 2025 | 32,558 | 34% | 6,656 | 24,998 | █████████ |
| Oct 2025 | 28,614 | 42% | 7,674 | 19,481 | ███████ |
| Nov 2025 | 28,300 | 44% | 8,384 | 19,045 | ███████ |
| Dec 2025 | 27,648 | 40% | 7,549 | 18,934 | ███████ |
| Jan 2026 | 41,737 | 25% | 8,688 | 31,981 | ███████████ |
| Feb 2026 | 48,370 | 32% | 12,107 | 34,988 | █████████████ |
| Mar 2026 | 43,106 | 35% | 14,675 | 27,102 | ███████████ |
| Apr 2026 | 76,341 | 24% | 18,518 | 55,858 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 10 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Trump Fires Navy Secretary John Phelan During Iran Crisis](https://www.ibtimes.sg/iran-fires-two-ships-hormuz-trump-extends-ceasefire-without-deadline-watch-85650) | ibtimes.sg | 9 | negative |
| 17 Apr 2026 | [Markets Shatter Records As Trump Unlocks The Strait of Hormuz - APA (NASDAQ:APA)](https://benzinga.com/markets/equities/26/04/51898649/markets-records-trump-iran-strait-hormuz-week-wall-street) | benzinga.com | 9 | negative |
| 14 Apr 2026 | [Two-Week Ceasefire Cannot Hide Deep Wounds: Five Logics Support High Oil Prices](https://nai500.com/blog/2026/04/two-week-ceasefire-cannot-hide-deep-wounds-five-logics-support-high-oil-prices/) | nai500.com | 9 | negative |
| 13 Apr 2026 | [Cost of crude oil races higher as Donald Trump pledges to block Iranian ports](https://www.independent.co.uk/news/business/donald-trump-strait-of-hormuz-keir-starmer-airlines-failure-b2956375.html) ⚠ | independent.co.uk | 9 | negative |
| 9 Apr 2026 | [Southeast Asia Faces Energy Reality Check as War Bites](https://www.energyintel.com/0000019d-620b-d7a3-a59d-72af30f30000) | energyintel.com | 9 | negative |
| 9 Apr 2026 | [Oil price surges towards $100 as Middle East ceasefire begins to unravel](https://bmmagazine.co.uk/news/oil-price-rises-iran-ceasefire-cracks-strait-hormuz/) | bmmagazine.co.uk | 9 | negative |
| 9 Apr 2026 | [Trump warns strikes will resume if Iran doesn't agree to his peace terms](https://www.wvxu.org/news-from-npr/2026-04-09/trump-warns-strikes-will-resume-if-iran-doesnt-agree-to-his-peace-terms) ⚠ | wvxu.org | 9 | negative |
| 8 Apr 2026 | [Relief in financial markets after Iran ceasefire – but it is far from absolute \| Richard Partington](https://www.theguardian.com/world/2026/apr/08/relief-financial-markets-iran-ceasefire-far-from-absolute) | theguardian.com | 9 | negative |
| 8 Apr 2026 | [Bitcoin Rises, Oil Falls as US–Iran Ceasefire Eases Fears](https://bitcoinethereumnews.com/bitcoin/bitcoin-rises-oil-falls-as-us-iran-ceasefire-eases-fears/) | bitcoinethereumnews.com | 9 | negative |
| 8 Apr 2026 | [Oil plunges and stocks rally on US-Iran ceasefire](https://www.agbi.com/oil-and-gas/2026/04/oil-slides-below-100-after-trump-announces-two-week-ceasefire/) | agbi.com | 9 | negative |
| 8 Apr 2026 | [Middle East war: global economic fallout](https://www.digitaljournal.com/business/middle-east-war-global-economic-fallout-8/article) | digitaljournal.com | 9 | negative |
| 2 Apr 2026 | [Oil Prices Surge and Global Markets React to Trump's Threats Against Iran](https://www.timesnownews.com/agency-news/oil-prices-surge-and-global-markets-react-to-trumps-threats-against-iran-article-153985214) | timesnownews.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "stock market" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "stock market" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "stock market" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "stock market" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "stock market", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "stock market", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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
