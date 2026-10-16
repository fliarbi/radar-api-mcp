# IMF News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “imf news” · 320/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [imf-news.json](../../examples/use-cases/imf-news.json).

**Question.** How much news did imf receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 10,917 |
| Negative · neutral · positive | 60% · 3.8% · 36% |
| Critical (priority 7–9) | 82% (8,958 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (5,879 articles) |
| Negative-to-positive vs all news | 2.29× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 393 | 77% | 225 | 148 | █ |
| Sep 2025 | 1,565 | 76% | 827 | 693 | █████ |
| Oct 2025 | 3,048 | 74% | 1,405 | 1,574 | ██████████ |
| Nov 2025 | 1,487 | 85% | 743 | 711 | █████ |
| Dec 2025 | 1,503 | 83% | 758 | 710 | █████ |
| Jan 2026 | 1,820 | 84% | 859 | 925 | ██████ |
| Feb 2026 | 1,737 | 83% | 895 | 787 | ██████ |
| Mar 2026 | 1,481 | 83% | 925 | 525 | █████ |
| Apr 2026 | 5,879 | 81% | 3,916 | 1,656 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 11 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Oil crisis: Lessons from global crises and Bangladesh’s blueprint for energy security](https://tbsnews.net/features/big-picture/oil-crisis-lessons-global-crises-and-bangladeshs-blueprint-energy-security) ⚠ | tbsnews.net | 9 | negative |
| 23 Apr 2026 | [Air war in Iran gives way to crippling stalemate in Hormuz \| Mint](https://www.livemint.com/global/air-war-in-iran-gives-way-to-crippling-stalemate-in-hormuz-11776908046721.html) ⚠ | livemint.com | 9 | negative |
| 22 Apr 2026 | [A New Oil Crisis Stress-Tests the Global Energy Transition](https://www.newsecuritybeat.org/2026/04/a-new-oil-crisis-stress-tests-the-global-energy-transition/) ⚠ | newsecuritybeat.org | 9 | negative |
| 22 Apr 2026 | [The bold lie of the Americans is over... an](https://www.bankingnews.gr/diethni/articles/870170/the-bold-lie-of-the-americans-is-over-an-acid-storm-is-coming-from-the-gulf-set-to-ignite-a-global-crash) ⚠ | bankingnews.gr | 9 | negative |
| 22 Apr 2026 | [War-linked energy shock pushing inflation higher in Europe: IMF expert](https://www.fibre2fashion.com/news/economics/war-linked-energy-shock-pushing-inflation-higher-in-europe-imf-expert-309803-newsdetails.htm) | fibre2fashion.com | 9 | negative |
| 20 Apr 2026 | [The Stranglehold at the Strait: How a Distant War Is Quietly Breaking Southeast Asia's Economy Heaptalk](https://heaptalk.com/insight/the-stranglehold-at-the-strait-how-a-distant-war-is-quietly-breaking-southeast-asias-economy/) ⚠ | heaptalk.com | 9 | negative |
| 20 Apr 2026 | [John FitzGerald: Ireland faces a possible winter recession yet has plundered its war chest](https://irishtimes.com/business/economy/2026/04/20/john-fitzgerald-ireland-faces-a-possible-winter-recession-yet-has-plundered-its-war-chest/) ⚠ | irishtimes.com | 9 | negative |
| 17 Apr 2026 | [The real cost of war: Economies don’t bounce back easily](https://www.indiatoday.in/diu/story/west-asia-conflict-economic-impact-imf-warns-of-long-term-damage-2897811-2026-04-17) ⚠ | indiatoday.in | 9 | negative |
| 17 Apr 2026 | [Chancellor says ‘no issue’ with fuel supply after energy boss's six-week warning](https://travelweekly.co.uk/news/europe-has-maybe-six-weeks-of-jet-fuel-left-warns-energy-boss) | travelweekly.co.uk | 9 | negative |
| 16 Apr 2026 | [International Energy Agency warns Europe has six weeks of jet fuel left - Time News](https://time.news/international-energy-agency-warns-europe-has-six-weeks-of-jet-fuel-left/) ⚠ | time.news | 9 | negative |
| 15 Apr 2026 | [Pierrakakis on CNBC: Possibly the largest energy crisis in history](https://sofokleous10.gr/2026/04/15/pierrakakis-on-cnbc-possibly-the-largest-energy-crisis-in-history/) ⚠ | sofokleous10.gr | 9 | negative |
| 15 Apr 2026 | [Iran war escalation could push global economy to brink of recession, IMF warns - Türkiye Today](https://www.turkiyetoday.com/business/iran-war-escalation-could-push-global-economy-to-brink-of-recession-imf-warns-3218153) | turkiyetoday.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q IMF --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q IMF --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q IMF --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q IMF --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "IMF", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "IMF", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Market Crash News](market-crash-news.md)
- [Tax News Today](tax-news-today.md)
- [NBFC News](nbfc-news.md)
- [Wealth Management News](wealth-management-news.md)
