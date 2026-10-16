# Wealth Management News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “wealth management news” · 30/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [wealth-management-news.json](../../examples/use-cases/wealth-management-news.json).

**Question.** How much news did wealth management receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 10,045 |
| Negative · neutral · positive | 5.7% · 2.5% · 92% |
| Critical (priority 7–9) | 17% (1,663 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (4,094 articles) |
| Negative-to-positive vs all news | 0.08× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 494 | 14% | 41 | 444 | ██ |
| Sep 2025 | 1,549 | 22% | 134 | 1,369 | ████████ |
| Oct 2025 | 918 | 37% | 76 | 822 | ████ |
| Nov 2025 | 738 | 38% | 72 | 651 | ████ |
| Dec 2025 | 750 | 33% | 69 | 662 | ████ |
| Jan 2026 | 2,420 | 18% | 115 | 2,253 | ████████████ |
| Feb 2026 | 1,553 | 25% | 123 | 1,401 | ████████ |
| Mar 2026 | 1,978 | 20% | 169 | 1,764 | ██████████ |
| Apr 2026 | 4,094 | 11% | 162 | 3,806 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 15 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Startup Founder Says Rs. 40 Crore Needed for Retirement in India, Sparks Debate](https://www.newsmobile.in/business/startup-founder-says-rs-40-crore-needed-for-retirement-in-india-sparks-debate/) | newsmobile.in | 8 | negative |
| 28 Apr 2026 | [Bitcoin mining meltdown? Why IREN’s real future is in AI, according to Bernstein](https://www.dlnews.com/articles/markets/bitcoin-mining-meltdown-why-irens-real-future-is-in-ai-says-bernstein/) | dlnews.com | 8 | positive |
| 20 Apr 2026 | [Wealth AI Crosses the Rubicon: 78% of Global Investors Now Use AI for Investment Research, BridgeWise Study…](https://serrarigroup.com/wealth-ai-crosses-the-rubicon-78-of-global-investors-now-use-ai-for-investment-research-bridgewise-study-reveals/) | serrarigroup.com | 8 | positive |
| 20 Apr 2026 | [We are pleased to share the April 2026 Ecosystem Update, highlighting developments in the macro environment,…](https://www.advancedblockchain.com/blogs/ecosystem-update-april-2026) ⚠ | advancedblockchain.com | 8 | positive |
| 17 Apr 2026 | [Market Disconnect as Stocks Rise and Consumers Struggle](https://fintech.tv/markets-at-record-highs-while-consumers-struggle/) | fintech.tv | 8 | negative |
| 16 Apr 2026 | [Hormuz Who? Iran War Volatility Hands Morgan Stanley A Record Q1 - Morgan Stanley (NYSE:MS)](https://www.benzinga.com/markets/earnings/26/04/51863567/hormuz-iran-war-morgan-stanley-record-trading-quarter) ⚠ | benzinga.com | 8 | positive |
| 16 Apr 2026 | [S&P 500 Hits 7,000: Why Markets Are Rising Despite Global Chaos](https://fintech.tv/sp-500-hits-7000-why-markets-are-rising-despite-global-chaos/) | fintech.tv | 8 | positive |
| 15 Apr 2026 | [The Fraser Inflection: Citigroup Shakes Off Decades of Underperformance with Blockbuster Q1](https://markets.financialcontent.com/stocks/article/marketminute-2026-4-15-the-fraser-inflection-citigroup-shakes-off-decades-of-underperformance-with-blockbuster-q1) ⚠ | markets.financialcontent.com | 8 | positive |
| 15 Apr 2026 | [Morgan Stanley Shatters Records in Q1 2026: Wealth Management Surge and AI Innovation Fuel 5.4% Stock Leap](https://markets.financialcontent.com/stocks/article/marketminute-2026-4-15-morgan-stanley-shatters-records-in-q1-2026-wealth-management-surge-and-ai-innovation-fuel-54-stock-leap) | markets.financialcontent.com | 8 | positive |
| 15 Apr 2026 | [Merrill, other BofA wealth units hit record revenue despite asset dip](https://www.financial-planning.com/news/merrill-other-bofa-wealth-units-hit-record-revenue-despite-asset-dip) | financial-planning.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "wealth management" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "wealth management" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "wealth management" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "wealth management" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "wealth management", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "wealth management", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [IMF News](imf-news.md)
- [NBFC News](nbfc-news.md)
