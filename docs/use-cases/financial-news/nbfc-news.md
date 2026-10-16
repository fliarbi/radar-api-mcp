# NBFC News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “nbfc news” · 720/month India · 20/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [nbfc-news.json](../../examples/use-cases/nbfc-news.json).

**Question.** How much news did nbfc receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 2,537 |
| Negative · neutral · positive | 13% · 1.6% · 85% |
| Critical (priority 7–9) | 72% (1,818 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (862 articles) |
| Negative-to-positive vs all news | 0.2× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 195 | 68% | 27 | 168 | █████ |
| Sep 2025 | 647 | 69% | 68 | 571 | ███████████████ |
| Oct 2025 | 686 | 70% | 87 | 594 | ████████████████ |
| Nov 2025 | 519 | 74% | 58 | 460 | ████████████ |
| Dec 2025 | 563 | 79% | 55 | 421 | █████████████ |
| Jan 2026 | 487 | 77% | 47 | 431 | ███████████ |
| Feb 2026 | 706 | 73% | 63 | 635 | ████████████████ |
| Mar 2026 | 482 | 76% | 67 | 409 | ███████████ |
| Apr 2026 | 862 | 65% | 151 | 693 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 16 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [First-time borrowers climb to 4.4 crore despite tighter lending norms: Report](https://economictimes.indiatimes.com/industry/banking/finance/first-time-borrowers-climb-to-4-4-crore-despite-tighter-lending-norms-report/articleshow/130629571.cms) ⚠ | economictimes.indiatimes.com | 8 | positive |
| 30 Apr 2026 | [Top stocks in news: Bajaj Finance, Vedanta, L&T, Indegene, Schaeffler, MOIL, HindZinc, HUL - BusinessToday](https://www.businesstoday.in/markets/stocks/story/top-stocks-in-news-bajaj-finance-vedanta-lt-indegene-schaeffler-moil-hindzinc-hul-528123-2026-04-30) ⚠ | businesstoday.in | 8 | positive |
| 29 Apr 2026 | [PIB fact check labels viral fuel price hike report as fake, urges citizens to verify](https://www.financialexpress.com/shorts/india-news/pib-fact-check-labels-viral-fuel-price-hike-report-as-fake-urges-citizens-to-verify-through-official-sources-4221905/) ⚠ | financialexpress.com | 8 | negative |
| 28 Apr 2026 | [India’s banking system turns sluggish amid loan recovery delays and legal hurdles: CII report](https://bfsi.economictimes.indiatimes.com/news/articles/indias-banking-system-turns-sluggish-amid-loan-recovery-delays-and-legal-hurdles-cii-report/130567628) ⚠ | bfsi.economictimes.indiatimes.com | 8 | positive |
| 28 Apr 2026 | [Manappuram Finance Limited Discloses SEBI Warning Against CMD in Personal Capacity](https://studycafe.in/manappuram-finance-limited-discloses-sebi-warning-against-cmd-in-personal-capacity-418379.html) | studycafe.in | 8 | negative |
| 27 Apr 2026 | [L&T Finance Records Highest Ever Consolidated Annual PAT of Rs. 3,003 Cr. (before effect of Labour Code…](https://india-press-release.com/lt-finance-records-highest-ever-consolidated-annual-pat-of-rs-3003-cr-before-effect-of-labour-code-considered-in-q3fy26-in-fy26-up-14-yoy/) ⚠ | india-press-release.com | 8 | positive |
| 27 Apr 2026 | [L&T Finance Records Highest Ever Consolidated Annual PAT of Rs. 3,003 Cr. (before effect of Labour Code…](https://www.tribuneindia.com/news/business/lt-finance-records-highest-ever-consolidated-annual-pat-of-rs-3003-cr-before-effect-of-labour-code-considered-in-q3fy26-in-fy26-up-14-yoy-2-2) ⚠ | tribuneindia.com | 8 | positive |
| 27 Apr 2026 | [Aye Finance posts 110% jump in Q4 profit; stock hits 52-week high](https://www.thehindubusinessline.com/markets/stock-markets/aye-finance-posts-110-jump-in-q4-profit-stock-hits-52-week-high/article70911268.ece) ⚠ | thehindubusinessline.com | 8 | positive |
| 26 Apr 2026 | [RBI Cancels Paytm Payments Bank Licence As ₹800 Crore In Customer Deposits Remain Frozen Two Years After…](https://techstory.in/rbi-cancels-paytm-payments-bank-licence-as-%e2%82%b9800-crore-in-customer-deposits-remain-frozen-two-years-after-shutdown/) ⚠ | techstory.in | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q NBFC --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q NBFC --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q NBFC --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q NBFC --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "NBFC", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "NBFC", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Tax News Today](tax-news-today.md)
- [IMF News](imf-news.md)
- [Wealth Management News](wealth-management-news.md)
