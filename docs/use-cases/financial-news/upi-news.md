# UPI News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “upi news” · 2,400/month India · 9,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [upi-news.json](../../examples/use-cases/upi-news.json).

**Question.** How much news did upi receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 15,757 |
| Negative · neutral · positive | 34% · 1.9% · 64% |
| Critical (priority 7–9) | 55% (8,652 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (4,589 articles) |
| Negative-to-positive vs all news | 0.71× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 668 | 62% | 220 | 431 | ███ |
| Sep 2025 | 2,812 | 61% | 856 | 1,896 | ████████████ |
| Oct 2025 | 2,826 | 63% | 862 | 1,905 | ████████████ |
| Nov 2025 | 2,761 | 50% | 807 | 1,907 | ████████████ |
| Dec 2025 | 2,719 | 56% | 988 | 1,683 | ████████████ |
| Jan 2026 | 3,176 | 49% | 1,016 | 2,117 | ██████████████ |
| Feb 2026 | 4,289 | 55% | 1,164 | 3,068 | ███████████████████ |
| Mar 2026 | 3,703 | 56% | 1,461 | 2,146 | ████████████████ |
| Apr 2026 | 4,589 | 58% | 1,682 | 2,777 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 18 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 24 Apr 2026 | [A global jet fuel crisis is closer than the world knows - UPI.com](https://www.upi.com/Voices/2026/04/24/perspectives-global-jet-fuel-crisis/9591777035708/) | upi.com | 9 | negative |
| 1 Apr 2026 | [Trump declares 'job done,' says U.S. forces to leave Iran in 2-3 weeks](https://www.yahoo.com/news/articles/trump-declares-job-done-says-110838829.html) | yahoo.com | 9 | negative |
| 12 Jan 2026 | [Britain to develop new ground-launched missiles for Ukraine - UPI.com](https://www.upi.com/Top_News/World-News/2026/01/12/Britain-supply-Ukraine-new-missiles/9121768192455/) | upi.com | 9 | negative |
| 30 Apr 2026 | [Triple holiday on 1 May 2026: What is open and what is closed in India](https://english.mathrubhumi.com/news/india/may-1-2026-holiday-india-status-feodtxmf) ⚠ | english.mathrubhumi.com | 8 | negative |
| 30 Apr 2026 | [Big Tech Challenges PhonePe and Google Pay Dominance in India](http://ibtimes.sg/amazon-pay-whatsapp-cred-challenge-phonepe-google-pay-dominance-india-seek-level-playing-net-85931) ⚠ | ibtimes.sg | 8 | positive |
| 30 Apr 2026 | [Is Mizoram’s famed healthcare scheme already on life support?](https://eastmojo.com/premium/2026/04/30/is-mizorams-famed-healthcare-scheme-already-on-life-support/) ⚠ | eastmojo.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q UPI --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q UPI --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q UPI --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q UPI --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "UPI", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "UPI", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Interest Rates News](interest-rates-news.md)
- [S&P 500 News Today](s-p-500-news-today.md)
- [Budget News](budget-news.md)
- [SEBI News](sebi-news.md)
