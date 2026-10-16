# S&P 500 News Today: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “s&p 500 news today” · 390/month India · 9,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [s-p-500-news-today.json](../../examples/use-cases/s-p-500-news-today.json).

**Question.** How much news did s&p 500 receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 22,472 |
| Negative · neutral · positive | 47% · 1.7% · 51% |
| Critical (priority 7–9) | 49% (11,039 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (7,479 articles) |
| Negative-to-positive vs all news | 1.25× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 1,361 | 48% | 408 | 945 | ████ |
| Sep 2025 | 4,750 | 47% | 1,441 | 3,218 | █████████████ |
| Oct 2025 | 6,305 | 46% | 2,499 | 3,220 | █████████████████ |
| Nov 2025 | 5,041 | 47% | 2,197 | 2,702 | █████████████ |
| Dec 2025 | 4,915 | 40% | 1,870 | 2,841 | █████████████ |
| Jan 2026 | 3,700 | 46% | 1,265 | 2,355 | ██████████ |
| Feb 2026 | 6,167 | 43% | 3,217 | 2,871 | ████████████████ |
| Mar 2026 | 5,126 | 57% | 3,012 | 2,043 | ██████████████ |
| Apr 2026 | 7,479 | 50% | 3,099 | 4,212 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 15 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 16 Apr 2026 | [Energy chief warns Europe only has six weeks of fuel left](https://finance.yahoo.com/sectors/energy/articles/energy-chief-warns-europe-only-182300136.html) | finance.yahoo.com | 9 | negative |
| 13 Apr 2026 | [Cost of crude oil races higher as Donald Trump pledges to block Iranian ports](https://www.independent.co.uk/news/business/donald-trump-strait-of-hormuz-keir-starmer-airlines-failure-b2956375.html) | independent.co.uk | 9 | negative |
| 9 Apr 2026 | [Asian Markets Retreat as Gulf Crisis Fuels Oil Surge and Inflation Fears - EconoTimes](https://econotimes.com/Asian-Markets-Retreat-as-Gulf-Crisis-Fuels-Oil-Surge-and-Inflation-Fears-1738517) | econotimes.com | 9 | negative |
| 8 Apr 2026 | [Stocks surge, oil dives below $100 as Iran ceasefire sparks relief rally- Moneycontrol.com](https://www.moneycontrol.com/news/business/stocks-surge-oil-dives-below-100-as-iran-ceasefire-sparks-relief-rally-13884100.html) | moneycontrol.com | 9 | negative |
| 7 Apr 2026 | [Oil Prices Dive, Stocks Surge as Trump Agrees to Middle East Ceasefire](https://globalbankingandfinance.com/oil-dives-stocks-surge-trump-agrees-two-week-ceasefire/) | globalbankingandfinance.com | 9 | negative |
| 7 Apr 2026 | [Evening digest: Trump’s Iran deadline nears, oil surge shakes markets](https://www.bitcoininsider.org/article/301413/evening-digest-trumps-iran-deadline-nears-oil-surge-shakes-markets) | bitcoininsider.org | 9 | negative |
| 23 Mar 2026 | [Oil prices rise after Trump issues ultimatum](http://www.ghanaweb.com/GhanaHomePage/NewsArchive/Oil-prices-rise-after-Trump-issues-ultimatum-2026999) | ghanaweb.com | 9 | negative |
| 30 Apr 2026 | [Bonds, stocks climb on oil's pullback; yen jumps after Japan's currency intervention](https://uk.finance.yahoo.com/news/tech-shares-rise-asia-bonds-015615873.html) | uk.finance.yahoo.com | 8 | negative |
| 30 Apr 2026 | [U.S. stocks rally to the finish of their best month since 2020, even as oil prices whipsaw](https://www.bnnbloomberg.ca/markets/oil/2026/04/30/soaring-oil-prices-ease-and-markets-rise-as-big-tech-sends-mixed-signals/) | bnnbloomberg.ca | 8 | positive |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "S&P 500" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "S&P 500" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "S&P 500" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "S&P 500" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "S&P 500", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "S&P 500", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Dow Jones News Today](dow-jones-news-today.md)
- [Interest Rates News](interest-rates-news.md)
- [UPI News](upi-news.md)
- [Budget News](budget-news.md)
