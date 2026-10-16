# Mortgage Rates News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “mortgage rates news” · 50/month India · 12,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [mortgage-rates-news.json](../../examples/use-cases/mortgage-rates-news.json).

**Question.** How much news did mortgage rates receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 3,154 |
| Negative · neutral · positive | 62% · 1.3% · 36% |
| Critical (priority 7–9) | 67% (2,110 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (1,028 articles) |
| Negative-to-positive vs all news | 2.32× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 183 | 75% | 114 | 69 | ████ |
| Sep 2025 | 1,028 | 79% | 649 | 350 | ████████████████████ |
| Oct 2025 | 685 | 59% | 392 | 272 | █████████████ |
| Nov 2025 | 541 | 57% | 289 | 249 | ███████████ |
| Dec 2025 | 924 | 41% | 488 | 276 | ██████████████████ |
| Jan 2026 | 591 | 68% | 369 | 216 | ███████████ |
| Feb 2026 | 693 | 62% | 432 | 251 | █████████████ |
| Mar 2026 | 960 | 66% | 563 | 389 | ███████████████████ |
| Apr 2026 | 910 | 71% | 597 | 290 | ██████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 8 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [3 mortgage rate questions borrowers should ask after the Fed rate pause](https://cbsnews.com/news/mortgage-rate-questions-borrowers-fed-rate-pause/) | cbsnews.com | 8 | negative |
| 30 Apr 2026 | [Rising household costs ‘will be felt hardest by those already struggling’](https://www.irishnews.com/news/uk/rising-household-costs-will-be-felt-hardest-by-those-already-struggling-LTVD6HZ4OFLTLCZGULNORFNJKI/) ⚠ | irishnews.com | 8 | negative |
| 30 Apr 2026 | [Will Mortgage Rates Go Down In May? \| Bankrate](https://www.bankrate.com/mortgages/mortgage-interest-rates-forecast/) | bankrate.com | 8 | positive |
| 30 Apr 2026 | [Bank of England holds interest rates at 3.75%: What it means for you](https://www.thisismoney.co.uk/money/mortgageshome/article-15776071/Bank-England-holds-rates-3-75-means-mortgage-savings.html) | thisismoney.co.uk | 8 | negative |
| 30 Apr 2026 | [Home sellers cut prices less even as U.S. listing prices fall again](https://www.stocktitan.net/news/NWS/spring-housing-market-holds-its-ground-despite-economic-headwinds-9bya0s1zamqe.html) | stocktitan.net | 8 | negative |
| 30 Apr 2026 | [US Mortgage Rates Surge to 6.5 Percent Amid Middle East Tensions](https://www.asatunews.co.id/en/mortgage-rates-surge-iran-tension) | asatunews.co.id | 8 | positive |
| 29 Apr 2026 | [US housing starts surge to highest level since December 2024](https://www.spokesman.com/stories/2026/apr/29/us-housing-starts-surge-to-highest-level-since-dec/) ⚠ | spokesman.com | 8 | positive |
| 29 Apr 2026 | [UAE maintains benchmark interest rate at 3.65% following US Fed decision](https://www.khaleejtimes.com/uae/uae-maintains-benchmark-interest-rate) | khaleejtimes.com | 8 | neutral |
| 29 Apr 2026 | [What the Fed rate pause may mean for mortgage interest rates](https://cbsnews.com/news/what-fed-rate-pause-means-mortgage-interest-rates/) | cbsnews.com | 8 | positive |
| 29 Apr 2026 | [Mortgage Rates Steady as Fed Holds, Despite Global Tensions - NerdWallet](https://www.nerdwallet.com/mortgages/news/fed-holds-mortgage-rates-4-29-26) | nerdwallet.com | 8 | positive |
| 29 Apr 2026 | [Will the Bank of England hold rates again on Thursday?](https://www.sapeople.com/expats/will-the-bank-of-england-hold-rates-again-on-thursday-30-april-2026/) | sapeople.com | 8 | positive |
| 29 Apr 2026 | [The housing market's summer rebound is falling apart](https://www.businessinsider.com/real-estate-market-summer-buyers-mortgate-rates-iran-war-2026-4) ⚠ | businessinsider.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "mortgage rates" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "mortgage rates" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "mortgage rates" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "mortgage rates" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "mortgage rates", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "mortgage rates", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Nifty News](nifty-news.md)
- [Federal Reserve News Today](federal-reserve-news-today.md)
- [Silver Price News](silver-price-news.md)
- [Dow Jones News Today](dow-jones-news-today.md)
