# Yen News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “yen news” · 210/month India · 1,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [yen-news.json](../../examples/use-cases/yen-news.json).

**Question.** How much news did yen receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 10,383 |
| Negative · neutral · positive | 39% · 2.1% · 59% |
| Critical (priority 7–9) | 50% (5,183 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,908 articles) |
| Negative-to-positive vs all news | 0.88× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 569 | 60% | 276 | 278 | ████ |
| Sep 2025 | 2,058 | 61% | 993 | 1,003 | ██████████████ |
| Oct 2025 | 1,848 | 54% | 684 | 1,134 | █████████████ |
| Nov 2025 | 1,904 | 48% | 731 | 1,159 | █████████████ |
| Dec 2025 | 2,005 | 52% | 868 | 1,082 | ██████████████ |
| Jan 2026 | 2,377 | 54% | 1,034 | 1,301 | ████████████████ |
| Feb 2026 | 2,649 | 54% | 1,030 | 1,561 | ██████████████████ |
| Mar 2026 | 2,449 | 46% | 904 | 1,493 | █████████████████ |
| Apr 2026 | 2,908 | 45% | 1,049 | 1,793 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 15 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 9 Mar 2026 | [‘Spillover’: Iran energy shockwaves hit Europe](https://www.politico.eu/article/spillover-iran-energy-shockwaves-hit-europe/) ⚠ | politico.eu | 9 | negative |
| 30 Apr 2026 | [Bonds, stocks climb on oil's pullback; yen jumps after Japan's currency intervention](https://uk.finance.yahoo.com/news/tech-shares-rise-asia-bonds-015615873.html) | uk.finance.yahoo.com | 8 | negative |
| 30 Apr 2026 | [USD/JPY Caves in On Aggressive BoJ Posture. But Will It Last?](https://www.investingcube.com/forex/usd-jpy-caves-in-on-aggressive-boj-posture-but-will-it-last/) | investingcube.com | 8 | negative |
| 30 Apr 2026 | [The sources, one government and another a market source, spoke on condition of anonymity as they were not…](https://www.yarrawongachronicle.com.au/aap-finance/japan-intervenes-to-counter-currency-weakness-sources/) | yarrawongachronicle.com.au | 8 | negative |
| 30 Apr 2026 | [Dollar drops versus yen as Japanese officials signal possible intervention](https://www.zawya.com/en/economy/global/dollar-drops-versus-yen-as-japanese-officials-signal-possible-intervention-vfyga57j) | zawya.com | 8 | negative |
| 30 Apr 2026 | [Yen crosses key threshold, but don’t count on intervention just yet \| Mint](https://www.livemint.com/global/yen-crosses-key-threshold-but-don-t-count-on-intervention-just-yet-11777540086587.html) | livemint.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q yen --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q yen --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q yen --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q yen --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "yen", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "yen", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Retirement News](retirement-news.md)
- [Treasury Yields News](treasury-yields-news.md)
- [Market Crash News](market-crash-news.md)
- [Tax News Today](tax-news-today.md)
