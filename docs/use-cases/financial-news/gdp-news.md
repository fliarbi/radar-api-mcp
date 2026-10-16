# GDP News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “gdp news” · 1,000/month India · 720/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [gdp-news.json](../../examples/use-cases/gdp-news.json).

**Question.** How much news did gdp receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 11,649 |
| Negative · neutral · positive | 40% · 2.8% · 57% |
| Critical (priority 7–9) | 71% (8,313 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,928 articles) |
| Negative-to-positive vs all news | 0.94× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 887 | 81% | 334 | 518 | █████ |
| Sep 2025 | 2,484 | 76% | 990 | 1,428 | █████████████ |
| Oct 2025 | 2,025 | 76% | 911 | 1,058 | ██████████ |
| Nov 2025 | 1,916 | 78% | 739 | 1,125 | ██████████ |
| Dec 2025 | 2,506 | 72% | 958 | 1,441 | █████████████ |
| Jan 2026 | 2,406 | 78% | 844 | 1,506 | ████████████ |
| Feb 2026 | 3,065 | 80% | 1,212 | 1,770 | ████████████████ |
| Mar 2026 | 2,250 | 76% | 1,093 | 1,067 | ███████████ |
| Apr 2026 | 3,928 | 58% | 1,487 | 2,340 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 11 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 15 Apr 2026 | [La creciente factura de la guerra contra Irán](https://www.expansion.com/opinion/2026/04/15/69df6d47e5fdeac33b8b4581.html) | expansion.com | 9 | negative |
| 30 Apr 2026 | [Growing GDP, thank GPT](https://www.marketplace.org/episode/2026/04/30/growing-gdp-thank-gpt) | marketplace.org | 8 | positive |
| 30 Apr 2026 | [GDP improves to start 2026, driven by AI investment](https://www.marketplace.org/story/2026/04/30/gdp-improves-to-start-2026-driven-by-ai-investment) | marketplace.org | 8 | positive |
| 30 Apr 2026 | [US national debt surpasses size of the economy for first time since World War II](https://www.foxbusiness.com/economy/us-national-debt-surpasses-size-economy-first-time-since-world-war-ii-data-shows) ⚠ | foxbusiness.com | 8 | negative |
| 30 Apr 2026 | [AI investments helped U.S. economy rebound in Q1](https://finance-commerce.com/2026/04/us-gdp-growth-inflation-ai-investment-outlook/) | finance-commerce.com | 8 | positive |
| 30 Apr 2026 | [Ghana’s international reserves hit $14.5bn: Majority caucus commends BoG for economic stabilisation efforts](https://www.graphic.com.gh/business/business-news/ghanas-international-reserves-hit-14-5bn-majority-caucus-commends-bog-for-economic-stabilisation-efforts.html) ⚠ | graphic.com.gh | 8 | negative |
| 30 Apr 2026 | [India’s textile output shrinks in March as Iran war fuels input costs, hits - The Economic Times](https://economictimes.indiatimes.com/industry/cons-products/garments-/-textiles/indias-textile-output-shrinks-in-march-as-iran-war-fuels-input-costs-hits/printarticle/130648148.cms) ⚠ | economictimes.indiatimes.com | 8 | negative |
| 30 Apr 2026 | [The AI economy: Business investment overtakes consumer spending as the biggest driver of GDP growth](https://malaysia.news.yahoo.com/the-ai-economy-business-investment-overtakes-consumer-spending-as-the-biggest-driver-of-gdp-growth-181709229.html) | malaysia.news.yahoo.com | 8 | positive |
| 30 Apr 2026 | [Canada’s economy stuck in low gear: Bank of Canada projects slow GDP growth well below 2% for 2026 and 2027](https://thehub.ca/2026/04/30/canadas-economy-stuck-in-low-gear-bank-of-canada-projects-slow-gdp-growth-well-below-2-for-2026-and-2027/) | thehub.ca | 8 | positive |
| 30 Apr 2026 | [Why Is Opendoor Technologies Stock Sliding On Thursday? - Opendoor Technologies (NASDAQ:OPEN)](https://www.benzinga.com/trading-ideas/movers/26/04/52186563/why-is-opendoor-technologies-stock-sliding-on-thursday) ⚠ | benzinga.com | 8 | negative |
| 30 Apr 2026 | [U.S. national debt headed into uncharted territory](https://www.deseret.com/business/2026/04/30/inflation-gas-prices-gdp-national-debt-iran-war-consumer-spending-stock-markets/) | deseret.com | 8 | negative |
| 30 Apr 2026 | [Mexico Economy Contracts for First Time Since Pandemic in Q1](https://www.riotimesonline.com/mexico-gdp-q1-2026-contraction-inegi/) | riotimesonline.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q GDP --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q GDP --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q GDP --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q GDP --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "GDP", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "GDP", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Stablecoin News](stablecoin-news.md)
- [ETF News](etf-news.md)
- [Credit Card News](credit-card-news.md)
- [Hedge Fund News](hedge-fund-news.md)
