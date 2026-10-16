# Federal Reserve News Today: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “federal reserve news today” · 140/month India · 9,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [federal-reserve-news-today.json](../../examples/use-cases/federal-reserve-news-today.json).

**Question.** How much news did federal reserve receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 43,168 |
| Negative · neutral · positive | 62% · 5.2% · 33% |
| Critical (priority 7–9) | 72% (31,162 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (15,433 articles) |
| Negative-to-positive vs all news | 2.57× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 4,615 | 80% | 3,209 | 1,253 | ██████ |
| Sep 2025 | 15,433 | 74% | 8,857 | 5,880 | ████████████████████ |
| Oct 2025 | 9,804 | 72% | 5,418 | 4,052 | █████████████ |
| Nov 2025 | 9,354 | 71% | 5,427 | 3,648 | ████████████ |
| Dec 2025 | 11,859 | 67% | 6,111 | 5,212 | ███████████████ |
| Jan 2026 | 10,389 | 70% | 5,747 | 4,055 | █████████████ |
| Feb 2026 | 10,077 | 68% | 5,932 | 3,721 | █████████████ |
| Mar 2026 | 10,143 | 74% | 7,169 | 2,521 | █████████████ |
| Apr 2026 | 12,559 | 76% | 7,930 | 3,818 | ████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 10 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Air war in Iran gives way to crippling stalemate in Hormuz \| Mint](https://www.livemint.com/global/air-war-in-iran-gives-way-to-crippling-stalemate-in-hormuz-11776908046721.html) ⚠ | livemint.com | 9 | negative |
| 20 Apr 2026 | [Trump’s Iran bomb warning puts oil, Bitcoin and crypto risk back in play](https://bitcoinethereumnews.com/bitcoin/trumps-iran-bomb-warning-puts-oil-bitcoin-and-crypto-risk-back-in-play/) ⚠ | bitcoinethereumnews.com | 9 | negative |
| 9 Apr 2026 | [A Two-Week Iran Ceasefire Crashed Oil 10% and Sent Bitcoin Past $72,000: It Started Unraveling Within Hours](https://bitcoinethereumnews.com/bitcoin/a-two-week-iran-ceasefire-crashed-oil-10-and-sent-bitcoin-past-72000-it-started-unraveling-within-hours/) ⚠ | bitcoinethereumnews.com | 9 | negative |
| 9 Apr 2026 | [Asian Markets Retreat as Gulf Crisis Fuels Oil Surge and Inflation Fears - EconoTimes](https://econotimes.com/Asian-Markets-Retreat-as-Gulf-Crisis-Fuels-Oil-Surge-and-Inflation-Fears-1738517) ⚠ | econotimes.com | 9 | negative |
| 8 Apr 2026 | [Stocks surge, oil dives below $100 as Iran ceasefire sparks relief rally- Moneycontrol.com](https://www.moneycontrol.com/news/business/stocks-surge-oil-dives-below-100-as-iran-ceasefire-sparks-relief-rally-13884100.html) ⚠ | moneycontrol.com | 9 | negative |
| 7 Apr 2026 | [Oil Prices Dive, Stocks Surge as Trump Agrees to Middle East Ceasefire](https://globalbankingandfinance.com/oil-dives-stocks-surge-trump-agrees-two-week-ceasefire/) ⚠ | globalbankingandfinance.com | 9 | negative |
| 27 Mar 2026 | [Ukraine Oil Attack Disrupts Trump's Price Plan, Heightens Bitcoin Macro Risk](https://bitcoinethereumnews.com/bitcoin/ukraine-oil-attack-disrupts-trumps-price-plan-heightens-bitcoin-macro-risk/) ⚠ | bitcoinethereumnews.com | 9 | negative |
| 27 Mar 2026 | [Macro risks mount as Ukraine adds to oil market uncertainty](https://bitcoinethereumnews.com/tech/macro-risks-mount-as-ukraine-adds-to-oil-market-uncertainty/) ⚠ | bitcoinethereumnews.com | 9 | negative |
| 27 Mar 2026 | [Bitcoin (BTC) news: Macro risks mount as Ukraine adds to oil market uncertainty](https://www.coindesk.com/markets/2026/03/27/bitcoin-macro-risks-spike-as-ukraine-throws-a-spanner-in-trump-s-plan-to-stabilize-oil-markets) ⚠ | coindesk.com | 9 | negative |
| 25 Mar 2026 | [ANALYSIS: THE WORLD’S CRITICAL SUPPLY ARCHITECTURE DISRUPTED BY THE U.S. ATTACK ON IRAN](https://www.linkedin.com/pulse/analysis-worlds-critical-supply-architecture-us-attack-scott-ortkiese-ly5lc) ⚠ | linkedin.com | 9 | negative |
| 17 Mar 2026 | [There is Something Worse Than an all-out Collapse Hitting the World \| Alternative \| Before It's News](https://beforeitsnews.com/alternative/2026/03/there-is-something-worse-than-an-all-out-collapse-hitting-the-world-3-3860685.html) ⚠ | beforeitsnews.com | 9 | negative |
| 16 Mar 2026 | [Global Market: Energy market turmoil forces policymakers to reassess inflation outlook - The Economic Times](https://economictimes.indiatimes.com/markets/stocks/news/global-market-energy-market-turmoil-forces-policymakers-to-reassess-inflation-outlook/printarticle/129600660.cms) ⚠ | economictimes.indiatimes.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "federal reserve" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "federal reserve" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "federal reserve" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "federal reserve" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "federal reserve", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "federal reserve", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [RBI News](rbi-news.md)
- [Nifty News](nifty-news.md)
- [Mortgage Rates News](mortgage-rates-news.md)
- [Silver Price News](silver-price-news.md)
