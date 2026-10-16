# Housing Market News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “housing market news” · 40/month India · 18,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [housing-market-news.json](../../examples/use-cases/housing-market-news.json).

**Question.** How much news did housing market receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,376 |
| Negative · neutral · positive | 54% · 1.8% · 44% |
| Critical (priority 7–9) | 56% (3,597 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,926 articles) |
| Negative-to-positive vs all news | 1.65× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 307 | 56% | 149 | 154 | ███ |
| Sep 2025 | 1,304 | 59% | 733 | 563 | ██████████████ |
| Oct 2025 | 1,134 | 62% | 559 | 555 | ████████████ |
| Nov 2025 | 1,295 | 58% | 765 | 521 | █████████████ |
| Dec 2025 | 1,174 | 57% | 553 | 605 | ████████████ |
| Jan 2026 | 1,394 | 58% | 784 | 599 | ██████████████ |
| Feb 2026 | 1,476 | 56% | 772 | 694 | ███████████████ |
| Mar 2026 | 1,580 | 56% | 780 | 736 | ████████████████ |
| Apr 2026 | 1,926 | 55% | 1,095 | 791 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 12 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Will the Iran War crash house prices?](https://www.macrobusiness.com.au/2026/05/will-the-iran-war-crash-house-prices/) ⚠ | macrobusiness.com.au | 8 | negative |
| 30 Apr 2026 | [Sadiq Khan to probe London’s £4,000-a-year service charges](https://www.yahoo.com/news/articles/sadiq-khan-probe-london-4-170500290.html) | yahoo.com | 8 | negative |
| 30 Apr 2026 | [Will Mortgage Rates Go Down In May? \| Bankrate](https://www.bankrate.com/mortgages/mortgage-interest-rates-forecast/) ⚠ | bankrate.com | 8 | positive |
| 30 Apr 2026 | [Home sellers cut prices less even as U.S. listing prices fall again](https://www.stocktitan.net/news/NWS/spring-housing-market-holds-its-ground-despite-economic-headwinds-9bya0s1zamqe.html) | stocktitan.net | 8 | negative |
| 30 Apr 2026 | [Is Florida housing tanking or holding steady? Comparing myths vs. facts](https://www.news-journalonline.com/story/news/state/2026/04/30/housing-market-in-florida-show-positive-picture-despite-reports/89704954007/) | news-journalonline.com | 8 | negative |
| 30 Apr 2026 | ['Five homes affordable': Rental market at breaking point for young South Aussies - News \| InDaily, Inside…](https://www.indailysa.com.au/news/just-in/2026/04/30/five-homes-affordable-rental-market-at-breaking-point-for-young-south-aussies) | indailysa.com.au | 8 | negative |
| 30 Apr 2026 | [‘Can’t afford to live’: Stark housing fears](https://au.finance.yahoo.com/news/t-afford-live-stark-housing-013015014.html) | au.finance.yahoo.com | 8 | negative |
| 30 Apr 2026 | [Dividend history of Quanta Services Inc., Dividend date of Quanta Services Inc., Dividend data of Quanta…](https://www.rttnews.com/Calendar/dividend/9218/quanta-services-inc.aspx) | rttnews.com | 8 | negative |
| 30 Apr 2026 | [LATEST: Bank of England keeps interest rates on hold](https://www.landlordzone.co.uk/news/bank-of-england-keeps-interest-rates-on-hold) ⚠ | landlordzone.co.uk | 8 | negative |
| 29 Apr 2026 | [Housing slump will curb country’s economic growth, Bank of Canada says](http://www.theglobeandmail.com/business/article-housing-slump-will-curb-countrys-economic-growth-bank-of-canada-says/) | theglobeandmail.com | 8 | negative |
| 29 Apr 2026 | [How a plan to fix the housing market may be making it worse - realestate.com.au](https://www.dailytelegraph.com.au/real-estate/national/how-a-plan-to-fix-the-housing-market-may-be-making-it-worse/news-story/bb0c724ab7531d67115aa7e8365a23e9) | dailytelegraph.com.au | 8 | negative |
| 29 Apr 2026 | [Mortgage Rates Steady as Fed Holds, Despite Global Tensions - NerdWallet](https://www.nerdwallet.com/mortgages/news/fed-holds-mortgage-rates-4-29-26) | nerdwallet.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "housing market" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "housing market" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "housing market" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "housing market" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "housing market", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "housing market", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [GST News](gst-news.md)
- [Gold Price News](gold-price-news.md)
- [IPO News](ipo-news.md)
- [RBI News](rbi-news.md)
