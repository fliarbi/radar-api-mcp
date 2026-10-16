# Inflation News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “inflation news” · 590/month India · 6,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [inflation-news.json](../../examples/use-cases/inflation-news.json).

**Question.** How much news did inflation receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 82,249 |
| Negative · neutral · positive | 67% · 4.1% · 29% |
| Critical (priority 7–9) | 68% (56,306 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (28,308 articles) |
| Negative-to-positive vs all news | 3.15× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 3,407 | 68% | 2,122 | 1,136 | ██ |
| Sep 2025 | 14,485 | 65% | 8,148 | 5,697 | ██████████ |
| Oct 2025 | 12,432 | 68% | 7,200 | 4,803 | █████████ |
| Nov 2025 | 11,495 | 68% | 6,676 | 4,370 | ████████ |
| Dec 2025 | 13,974 | 65% | 7,813 | 5,525 | ██████████ |
| Jan 2026 | 12,823 | 68% | 7,265 | 5,053 | █████████ |
| Feb 2026 | 16,151 | 67% | 9,749 | 5,622 | ███████████ |
| Mar 2026 | 24,967 | 72% | 18,608 | 5,421 | ██████████████████ |
| Apr 2026 | 28,308 | 67% | 19,497 | 7,578 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 9 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 27 Apr 2026 | [World Bank Warns Middle East Conflict Could Push 2.4 Million Kenyans Into Poverty](https://businesstoday.co.ke/iran-could-push-kenyans-into-poverty/) ⚠ | businesstoday.co.ke | 9 | negative |
| 23 Apr 2026 | [Oil crisis: Lessons from global crises and Bangladesh’s blueprint for energy security](https://tbsnews.net/features/big-picture/oil-crisis-lessons-global-crises-and-bangladeshs-blueprint-energy-security) ⚠ | tbsnews.net | 9 | negative |
| 23 Apr 2026 | [Hormuz closure wipes out 13M bpd, further reserve releases won’t fix crisis: IEA - Türkiye Today](https://www.turkiyetoday.com/business/hormuz-closure-wipes-out-13m-bpd-further-reserve-releases-wont-fix-crisis-iea-3218662) ⚠ | turkiyetoday.com | 9 | negative |
| 23 Apr 2026 | [Air war in Iran gives way to crippling stalemate in Hormuz \| Mint](https://www.livemint.com/global/air-war-in-iran-gives-way-to-crippling-stalemate-in-hormuz-11776908046721.html) ⚠ | livemint.com | 9 | negative |
| 22 Apr 2026 | [War-linked energy shock pushing inflation higher in Europe: IMF expert](https://www.fibre2fashion.com/news/economics/war-linked-energy-shock-pushing-inflation-higher-in-europe-imf-expert-309803-newsdetails.htm) | fibre2fashion.com | 9 | negative |
| 19 Apr 2026 | [Europe has 'maybe 6 weeks of jet fuel left,' energy agency head tells AP - Breitbart](https://www.breitbart.com/news/europe-has-maybe-6-weeks-of-jet-fuel-left-energy-agency-head-tells-ap/) ⚠ | breitbart.com | 9 | negative |
| 17 Apr 2026 | [Markets Shatter Records As Trump Unlocks The Strait of Hormuz - APA (NASDAQ:APA)](https://benzinga.com/markets/equities/26/04/51898649/markets-records-trump-iran-strait-hormuz-week-wall-street) | benzinga.com | 9 | negative |
| 17 Apr 2026 | [Trouble for Irish tourists this summer as Europe has 'maybe 6 weeks of jet fuel left'](https://www.rsvplive.ie/news/uk-world-news/trouble-irish-tourists-summer-europe-37030380) ⚠ | rsvplive.ie | 9 | negative |
| 17 Apr 2026 | [Europe has 'six weeks of jet fuel left,' energy boss warns](https://www.9news.com.au/world/europe-has-six-weeks-of-jet-fuel-left/732ad6e2-c4a9-4ed5-b4ec-5e995496cc7a) ⚠ | 9news.com.au | 9 | negative |
| 16 Apr 2026 | [Europe could run out of jet fuel in 6 weeks — throwing flights into chaos in time for summer](https://nypost.com/2026/04/16/world-news/europe-could-run-out-of-jet-fuel-in-6-weeks-throwing-flights-into-chaos/) ⚠ | nypost.com | 9 | negative |
| 16 Apr 2026 | [Europe has 'maybe 6 weeks' of jet fuel left amid Hormuz blockade, energy agency chief says](https://www.foxbusiness.com/politics/europe-has-maybe-6-weeks-oil-left-amid-hormuz-blockade-energy-agency-chief-says) ⚠ | foxbusiness.com | 9 | negative |
| 16 Apr 2026 | [Strait of Hormuz Impact: IEA Chief Warns Flights May Get Hit As Jet Fuel Stocks Run Low \| LatestLY](https://www.latestly.com/uk/strait-of-hormuz-impact-iea-chief-warns-flights-may-get-hit-as-jet-fuel-stocks-run-low-7395956.html) ⚠ | latestly.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q inflation --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q inflation --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q inflation --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q inflation --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "inflation", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "inflation", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Income Tax News](income-tax-news.md)
- [Sensex News](sensex-news.md)
- [Venture Capital News Today](venture-capital-news-today.md)
- [Nasdaq News](nasdaq-news.md)
