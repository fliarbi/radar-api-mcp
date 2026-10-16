# Dividend News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “dividend news” · 1,000/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [dividend-news.json](../../examples/use-cases/dividend-news.json).

**Question.** How much news did dividend receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 17,654 |
| Negative · neutral · positive | 11% · 5.3% · 84% |
| Critical (priority 7–9) | 24% (4,213 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (7,215 articles) |
| Negative-to-positive vs all news | 0.18× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 607 | 27% | 45 | 533 | ██ |
| Sep 2025 | 2,314 | 25% | 176 | 2,032 | ██████ |
| Oct 2025 | 1,645 | 34% | 158 | 1,431 | █████ |
| Nov 2025 | 2,487 | 44% | 462 | 1,943 | ███████ |
| Dec 2025 | 2,358 | 29% | 306 | 1,964 | ███████ |
| Jan 2026 | 2,270 | 22% | 242 | 1,944 | ██████ |
| Feb 2026 | 4,287 | 32% | 511 | 3,577 | ████████████ |
| Mar 2026 | 3,882 | 28% | 474 | 3,195 | ███████████ |
| Apr 2026 | 7,215 | 17% | 718 | 6,053 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 15 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Stock Market Today, April 30: Meta Falls as Higher AI Capex Outlook Overshadows Strong Q1 Results \| The…](https://www.fool.com/coverage/stock-market-today/2026/04/30/stock-market-today-april-30-meta-falls-as-higher-ai-capex-outlook-overshadows-strong-q1-results/) | fool.com | 8 | negative |
| 30 Apr 2026 | [Indiaâs demographic dividend at risk as jobs, skills gap persist - The Economic Times](https://economictimes.indiatimes.com/opinion/et-commentary/indias-demographic-dividend-at-risk-as-jobs-skills-gap-persist/articleshow/130646608.cms) | economictimes.indiatimes.com | 8 | negative |
| 29 Apr 2026 | [Indian Bank Q4 profit rises 5% to Rs 3,103 crore on sharp fall in bad loans](https://www.thehindubusinessline.com/money-and-banking/indian-bank-q4-profit-rises-5-to-rs-3103-crore-on-lower-npas/article70920294.ece) ⚠ | thehindubusinessline.com | 8 | positive |
| 29 Apr 2026 | [Indian Bank Q4 Results: ₹308 crore provision for West Asia crisis; Board approves fund raise - CNBC TV18](https://www.cnbctv18.com/market/indian-bank-q4-results-rs-308-crore-provision-for-west-asia-crisis-board-approves-fund-raise-ws-l-19895741.htm) | cnbctv18.com | 8 | positive |
| 29 Apr 2026 | [Nagarro SE \| Nagarro releases audited financial statements and annual report for FY 2025, reaffirms the…](https://www.webdisclosure.com/press-release/nagarro-releases-audited-financial-statements-and-annual-report-for-fy-2025-reaffirms-the-preliminary-numbers-vhzZNjnajjw) | webdisclosure.com | 8 | positive |
| 29 Apr 2026 | [Weichai Power 2025 Annual Report: Business Performance, Innovations, Financials, and Strategic Growth](https://www.minichart.com.sg/2026/04/29/weichai-power-2025-annual-report-business-performance-innovations-financials-and-strategic-growth/) | minichart.com.sg | 8 | positive |
| 28 Apr 2026 | [Maruti Suzuki announces Rs 140/share dividend, fixes record date. Check details](https://economictimes.indiatimes.com/markets/stocks/earnings/maruti-suzuki-announces-rs-140/share-dividend-fixes-record-date-check-details/articleshow/130575397.cms) | economictimes.indiatimes.com | 8 | positive |
| 28 Apr 2026 | [NGX: Investors dump banking stocks, losing N1.3 trillion on dividend concerns](https://nairametrics.com/2026/04/28/ngx-investors-dump-banking-stocks-losing-n1-3-trillion-on-dividend-concerns/) | nairametrics.com | 8 | negative |
| 28 Apr 2026 | [Rs 240 Dividend: This cement maker announces quarterly results, recommends special dividend - Details here](https://www.indiatvnews.com/business/markets/ultratech-cement-dividend-amount-rs-240-q4-results-check-full-details-here-2026-04-28-1039178) | indiatvnews.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q dividend --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q dividend --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q dividend --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q dividend --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "dividend", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "dividend", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Credit Card News](credit-card-news.md)
- [Hedge Fund News](hedge-fund-news.md)
- [Unemployment News](unemployment-news.md)
- [Retirement News](retirement-news.md)
