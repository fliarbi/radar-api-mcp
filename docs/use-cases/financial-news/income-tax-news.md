# Income Tax News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “income tax news” · 8,100/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [income-tax-news.json](../../examples/use-cases/income-tax-news.json).

**Question.** How much news did income tax receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 9,333 |
| Negative · neutral · positive | 40% · 15% · 45% |
| Critical (priority 7–9) | 61% (5,645 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,957 articles) |
| Negative-to-positive vs all news | 1.2× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 505 | 52% | 172 | 234 | ███ |
| Sep 2025 | 2,169 | 60% | 857 | 993 | ███████████████ |
| Oct 2025 | 1,253 | 54% | 569 | 486 | ████████ |
| Nov 2025 | 1,691 | 66% | 909 | 577 | ███████████ |
| Dec 2025 | 1,387 | 63% | 642 | 545 | █████████ |
| Jan 2026 | 1,559 | 61% | 664 | 719 | ███████████ |
| Feb 2026 | 2,268 | 66% | 928 | 1,040 | ███████████████ |
| Mar 2026 | 2,549 | 59% | 919 | 1,155 | █████████████████ |
| Apr 2026 | 2,957 | 58% | 1,208 | 1,271 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 13 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Ford Expects $1.3 Billion in Tariff Refunds After SCOTUS Ruling](http://autoweek.com/news/a71177860/ford-expects-13-billion-tariff-refunds/) | autoweek.com | 8 | negative |
| 30 Apr 2026 | [Meesho to appeal $1.5m tax demand in India](https://www.startupnews.fyi/ecommerce/meesho-to-appeal-1-5m-tax-demand-in-india) | startupnews.fyi | 8 | negative |
| 30 Apr 2026 | [Clean Max Enviro Energy Solutions Receives Income Tax Order for AY 2023-24 with Rs 6.78 Cr Demand](https://studycafe.in/clean-max-enviro-energy-solutions-receives-income-tax-order-for-ay-2023-24-with-rs-6-78-cr-demand-418729.html) | studycafe.in | 8 | negative |
| 30 Apr 2026 | [Income Tax Department grants stay to NDTV on Rs 420.36 Crore Income Tax Liability](https://studycafe.in/income-tax-department-grants-stay-to-ndtv-on-rs-420-36-crore-income-tax-liability-418766.html) | studycafe.in | 8 | negative |
| 30 Apr 2026 | [NDTV gets stay on ₹420.36 crore tax demand; subject to review](http://storyboard18.com/brand-marketing/ndtv-gets-stay-on-%e2%82%b9420-36-crore-tax-demand-subject-to-review-96767.htm) | storyboard18.com | 8 | negative |
| 29 Apr 2026 | [Federal Bank Q4 Profit Jumps 22%](https://money.rediff.com/news/market/federal-bank-q4-profit-jumps-22/46158920260429) ⚠ | money.rediff.com | 8 | positive |
| 29 Apr 2026 | [Number of top rate taxpayers surges as frozen thresholds squeeze Brits](https://www.cityam.com/number-of-top-rate-taxpayers-surges-as-frozen-thresholds-squeeze-brits/) | cityam.com | 8 | negative |
| 29 Apr 2026 | [Income tax refund rules change from April 2026: Check these 2 important updates for Tax Year 2026-27 - The…](https://economictimes.indiatimes.com/wealth/tax/income-tax-refund-rules-change-from-april-2026-check-these-2-important-updates-for-tax-year-2026-27/articleshow/130595920.cms) | economictimes.indiatimes.com | 8 | positive |
| 29 Apr 2026 | [HRA Alert: Income Tax Dept Using AI to Spot Fake Rent Claims](https://studycafe.in/hra-alert-income-tax-dept-using-ai-to-spot-fake-rent-claims-418529.html) | studycafe.in | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "income tax" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "income tax" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "income tax" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "income tax" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "income tax", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "income tax", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Budget News](budget-news.md)
- [SEBI News](sebi-news.md)
- [Sensex News](sensex-news.md)
- [Inflation News](inflation-news.md)
