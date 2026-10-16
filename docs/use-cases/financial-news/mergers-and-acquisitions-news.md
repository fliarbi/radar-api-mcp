# Mergers and Acquisitions News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “mergers and acquisitions news” · 720/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [mergers-and-acquisitions-news.json](../../examples/use-cases/mergers-and-acquisitions-news.json).

**Question.** How much news did mergers and acquisitions receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 41,175 |
| Negative · neutral · positive | 24% · 4.8% · 72% |
| Critical (priority 7–9) | 48% (19,774 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (11,924 articles) |
| Negative-to-positive vs all news | 0.45× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 1,934 | 46% | 493 | 1,358 | ███ |
| Sep 2025 | 8,235 | 43% | 1,734 | 6,090 | ██████████████ |
| Oct 2025 | 6,871 | 52% | 1,309 | 5,250 | ████████████ |
| Nov 2025 | 6,579 | 53% | 1,443 | 4,819 | ███████████ |
| Dec 2025 | 8,211 | 55% | 1,678 | 6,157 | ██████████████ |
| Jan 2026 | 8,529 | 49% | 1,808 | 6,334 | ██████████████ |
| Feb 2026 | 11,252 | 49% | 2,640 | 8,114 | ███████████████████ |
| Mar 2026 | 9,470 | 46% | 2,188 | 6,743 | ████████████████ |
| Apr 2026 | 11,924 | 48% | 3,119 | 8,236 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 14 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [China blocks tech acquisitions to weaken America. The U.S. shouldn’t follow suit.](https://reason.com/2026/04/30/china-blocks-tech-acquisitions-to-weaken-america-the-u-s-shouldnt-follow-suit/) | reason.com | 8 | negative |
| 30 Apr 2026 | [BB relaxes provisioning rules for funds stuck in merged Islamic banks](https://tbsnews.net/economy/banking/bb-relaxes-provisioning-rules-funds-stuck-merged-islamic-banks-1426511) ⚠ | tbsnews.net | 8 | negative |
| 30 Apr 2026 | [Opec's days of manipulating the market are over \| The National](https://www.thenationalnews.com/opinion/comment/2026/04/30/uae-opec-saudi-arabia-us-russia-oil-iran-war-strait-of-hormuz/) ⚠ | thenationalnews.com | 8 | negative |
| 30 Apr 2026 | [Amazon’s Financial Results Blow Past Wall Street Forecasts](https://www.barchart.com/story/news/1621814/amazons-financial-results-blow-past-wall-street-forecasts) ⚠ | barchart.com | 8 | positive |
| 30 Apr 2026 | [Warner Bros. Discovery Finance Chief Gunnar Wiedenfels Gets New Contract](https://www.hollywoodreporter.com/business/business-news/gunnar-wiedenfels-warner-bros-discovery-1236580848/) ⚠ | hollywoodreporter.com | 8 | positive |
| 30 Apr 2026 | [David Zaslav’s 2025 Pay Levitates To $165 Million On Option Awards](https://deadline.com/2026/04/david-zaslav-2025-pay-surges-massive-option-award-1236876846/) ⚠ | deadline.com | 8 | negative |
| 30 Apr 2026 | [Despite change atop the Fed, investor hopes for rate cuts hit hurdles](https://theglobeandmail.com/investing/article-despite-change-atop-the-fed-investor-hopes-for-rate-cuts-hit-hurdles/) ⚠ | theglobeandmail.com | 8 | positive |
| 30 Apr 2026 | [$4 billion in 2026: 10 stocks where promoters are increasing ownership – Jefferies decodes trend](https://www.financialexpress.com/market/4-billion-in-2026-10-stocks-where-promoters-are-increasing-ownership-jefferies-decodes-trend-4222834/) ⚠ | financialexpress.com | 8 | positive |
| 30 Apr 2026 | [AI spending sets a record, with no end in sight](http://www.straitstimes.com/world/ai-spending-sets-a-record-with-no-end-in-sight) ⚠ | straitstimes.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "mergers and acquisitions" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "mergers and acquisitions" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "mergers and acquisitions" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "mergers and acquisitions" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "mergers and acquisitions", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "mergers and acquisitions", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Fintech News](fintech-news.md)
- [Mutual Fund News](mutual-fund-news.md)
- [Private Equity News](private-equity-news.md)
- [Pension News](pension-news.md)
