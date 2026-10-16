# GST News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “gst news” · 49,500/month India · 210/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [gst-news.json](../../examples/use-cases/gst-news.json).

**Question.** How much news did gst receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 21,844 |
| Negative · neutral · positive | 49% · 1.6% · 50% |
| Critical (priority 7–9) | 40% (8,665 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (14,317 articles) |
| Negative-to-positive vs all news | 1.32× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 1,810 | 60% | 655 | 1,103 | ███ |
| Sep 2025 | 14,317 | 54% | 3,938 | 9,966 | ████████████████████ |
| Oct 2025 | 5,616 | 47% | 1,289 | 4,232 | ████████ |
| Nov 2025 | 4,440 | 48% | 1,095 | 3,285 | ██████ |
| Dec 2025 | 4,381 | 53% | 1,232 | 3,031 | ██████ |
| Jan 2026 | 4,503 | 53% | 1,935 | 2,490 | ██████ |
| Feb 2026 | 5,754 | 36% | 3,019 | 2,658 | ████████ |
| Mar 2026 | 5,489 | 36% | 2,997 | 2,404 | ████████ |
| Apr 2026 | 6,098 | 37% | 2,658 | 3,313 | █████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 16 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Not TACO, Wall Street Coins 'NACHO' Acronym As Hormuz Crisis Fuels Oil Rally](https://www.ibtimes.sg/not-taco-wall-street-coins-nacho-acronym-hormuz-crisis-fuels-oil-rally-85936) ⚠ | ibtimes.sg | 8 | negative |
| 30 Apr 2026 | [Mere GST Deposit not payment until debited and appropriated to Government: High Court](https://studycafe.in/mere-gst-deposit-not-payment-until-debited-and-appropriated-to-government-high-court-418476.html) | studycafe.in | 8 | negative |
| 30 Apr 2026 | [Meesho to appeal $1.5m tax demand in India](https://www.startupnews.fyi/ecommerce/meesho-to-appeal-1-5m-tax-demand-in-india) ⚠ | startupnews.fyi | 8 | negative |
| 29 Apr 2026 | [Can Alphabet, Meta, and Amazon justify the sky-high spend as earnings report release today?](https://www.financialexpress.com/market/global-markets/can-alphabet-meta-and-amazon-justify-the-sky-high-spend-as-earnings-report-release-today/4222396/) ⚠ | financialexpress.com | 8 | positive |
| 29 Apr 2026 | [Electrification can slash 1.2 billion tonne CO₂, cut energy 22%, save 7.9 lakh lives a year](https://www.financialexpress.com/policy/economy/electrification-can-slash-1-2-billion-tonne-co-cut-energy-22-save-79-lakh-lives-a-year/4222162/) ⚠ | financialexpress.com | 8 | negative |
| 28 Apr 2026 | [Liberals target affordability to meet era of uncertainty in spring fiscal update](https://cheknews.ca/liberals-target-affordability-to-meet-era-of-uncertainty-in-spring-fiscal-update-1321487/) ⚠ | cheknews.ca | 8 | negative |
| 28 Apr 2026 | [Nine highlights from the spring economic update](https://www.theglobeandmail.com/politics/article-spring-economic-update-highlights-cpp-sports-defence-april-28/) ⚠ | theglobeandmail.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q GST --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q GST --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q GST --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q GST --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "GST", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "GST", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Stock Market News](stock-market-news.md)
- [Crypto News](crypto-news.md)
- [Gold Price News](gold-price-news.md)
- [Housing Market News](housing-market-news.md)
