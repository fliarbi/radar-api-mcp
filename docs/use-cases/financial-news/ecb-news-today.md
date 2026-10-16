# ECB News Today: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “ecb news today” · 20/month India · 1,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [ecb-news-today.json](../../examples/use-cases/ecb-news-today.json).

**Question.** How much news did ecb receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 6,224 |
| Negative · neutral · positive | 56% · 12% · 33% |
| Critical (priority 7–9) | 62% (3,887 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (1,928 articles) |
| Negative-to-positive vs all news | 2.3× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 195 | 52% | 122 | 63 | ██ |
| Sep 2025 | 1,080 | 66% | 537 | 454 | ███████████ |
| Oct 2025 | 885 | 64% | 425 | 413 | █████████ |
| Nov 2025 | 900 | 67% | 470 | 356 | █████████ |
| Dec 2025 | 1,134 | 65% | 572 | 453 | ████████████ |
| Jan 2026 | 931 | 57% | 430 | 367 | ██████████ |
| Feb 2026 | 1,826 | 62% | 866 | 643 | ███████████████████ |
| Mar 2026 | 1,928 | 66% | 1,234 | 550 | ████████████████████ |
| Apr 2026 | 1,539 | 62% | 936 | 475 | ████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 16 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 4 Apr 2026 | [Iran Offers Europe a Hormuz Lifeline — and the Price Could Be the Dollar](https://www.ibtimes.co.uk/iran-strait-hormuz-transit-negotiations-1790190) ⚠ | ibtimes.co.uk | 9 | negative |
| 16 Feb 2026 | [Overcoming structural barriers to the green transition](https://www.ecb.europa.eu/press/economic-bulletin/articles/2026/html/ecb.ebart202601_01~d8ce53e315.en.html) | ecb.europa.eu | 9 | negative |
| 30 Apr 2026 | [FxWirePro: EUR/AUD dips after ECB rate decision , eyes 1.6150 level - EconoTimes](https://econotimes.com/FxWirePro-EUR-AUD-dips-after-ECB-rate-decision-eyes-16150-level-1740555) | econotimes.com | 8 | negative |
| 30 Apr 2026 | [Bank of England warns ‘higher inflation unavoidable’ after holding interest rates](https://www.theguardian.com/business/2026/apr/30/bank-of-england-leaves-interest-rates-on-hold) ⚠ | theguardian.com | 8 | negative |
| 30 Apr 2026 | [ECB holds rates at 2% as inflation rises and eurozone growth slows](https://au.finance.yahoo.com/news/ecb-holds-rates-2-inflation-122126422.html) | au.finance.yahoo.com | 8 | negative |
| 30 Apr 2026 | [Oil strikes 4-year peak, stocks rise](https://www.bangkokpost.com/business/general/3247284/oil-strikes-4year-peak-stocks-rise) ⚠ | bangkokpost.com | 8 | negative |
| 30 Apr 2026 | [ECB Holds the Line: Rates Stay Steady as Geopolitical Energy Risks Loom - EconoTimes](https://econotimes.com/ECB-Holds-the-Line-Rates-Stay-Steady-as-Geopolitical-Energy-Risks-Loom-1740495) | econotimes.com | 8 | positive |
| 30 Apr 2026 | [US growth falls short in Q1 2026; EU, UK hold rates as oil prices rise - Türkiye Today](https://www.turkiyetoday.com/business/us-growth-falls-short-in-q1-2026-eu-uk-hold-rates-as-oil-prices-rise-3219134) | turkiyetoday.com | 8 | negative |
| 30 Apr 2026 | [ECB Maintains Interest Rates Amid Rising Iran Conflict Risks](https://world.infonasional.com/ecb-holds-rates-iran-conflict) | world.infonasional.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q ECB --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q ECB --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q ECB --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q ECB --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "ECB", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "ECB", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Commercial Real Estate News](commercial-real-estate-news.md)
- [Rupee News](rupee-news.md)
- [Stablecoin News](stablecoin-news.md)
- [ETF News](etf-news.md)
