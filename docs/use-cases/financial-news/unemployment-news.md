# Unemployment News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “unemployment news” · 320/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [unemployment-news.json](../../examples/use-cases/unemployment-news.json).

**Question.** How much news did unemployment receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 9,748 |
| Negative · neutral · positive | 66% · 3.3% · 31% |
| Critical (priority 7–9) | 74% (7,223 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,943 articles) |
| Negative-to-positive vs all news | 2.93× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 557 | 73% | 368 | 175 | ████ |
| Sep 2025 | 2,468 | 78% | 1,630 | 765 | █████████████████ |
| Oct 2025 | 1,610 | 77% | 1,074 | 462 | ███████████ |
| Nov 2025 | 1,637 | 75% | 1,021 | 562 | ███████████ |
| Dec 2025 | 2,147 | 78% | 1,392 | 668 | ███████████████ |
| Jan 2026 | 1,711 | 74% | 1,129 | 533 | ████████████ |
| Feb 2026 | 2,688 | 75% | 1,747 | 849 | ██████████████████ |
| Mar 2026 | 2,406 | 76% | 1,691 | 616 | ████████████████ |
| Apr 2026 | 2,943 | 72% | 1,857 | 970 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 14 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 14 Apr 2026 | [IMF slashes UK economic growth forecasts as Iran war risks global recession](https://www.thenational.scot/news/26020925.imf-says-iran-war-risks-global-recession-growth-forecasts-slashed/) ⚠ | thenational.scot | 9 | negative |
| 14 Apr 2026 | [UK economic growth forecasts slashed as IMF says Iran war risks global recession](https://www.edp24.co.uk/news/national/26020326.uk-economic-growth-forecasts-slashed-imf-says-iran-war-risks-global-recession/) ⚠ | edp24.co.uk | 9 | negative |
| 14 Apr 2026 | [Trump’s Iran war could trigger global recession, IMF warns](https://www.independent.co.uk/news/uk/politics/recession-iran-war-trump-imf-b2957233.html) ⚠ | independent.co.uk | 9 | negative |
| 25 Mar 2026 | [Today in History: March 25, coal dust explosion kills 111 miners](https://us.headtopics.com/news/today-in-history-march-25-coal-dust-explosion-kills-111-81426851) ⚠ | us.headtopics.com | 9 | negative |
| 30 Apr 2026 | [Weekly U.S. jobless claims fall to lowest level in more than five decades](https://www.theglobeandmail.com/business/international-business/us-business/article-weekly-us-jobless-claims-week-ending-april-25/) | theglobeandmail.com | 8 | negative |
| 30 Apr 2026 | [Canada's youth unemployment 'a crisis' as numbers rise](https://torontosun.com/news/national/canada-youth-unemployment-numbers-rise) | torontosun.com | 8 | negative |
| 30 Apr 2026 | [ECB holds interest rates but keeps June hike in play as war drags on](https://www.politico.eu/article/eu-ecb-holds-rates-but-keeps-june-hike-play-as-war-drags-on/) | politico.eu | 8 | negative |
| 30 Apr 2026 | [Egyptian unemployment rate drops to 6.3% in 2025 amidst economic reforms](https://www.zawya.com/en/economy/north-africa/egyptian-unemployment-rate-drops-to-63-in-2025-amidst-economic-reforms-yec4xpn4) | zawya.com | 8 | positive |
| 30 Apr 2026 | [For What AI Could Do to Democracies, Look to the Petrostates](https://foreignpolicy.com/2026/04/30/petrostates-ai-democracies/) | foreignpolicy.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q unemployment --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q unemployment --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q unemployment --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q unemployment --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "unemployment", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "unemployment", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Hedge Fund News](hedge-fund-news.md)
- [Dividend News](dividend-news.md)
- [Retirement News](retirement-news.md)
- [Treasury Yields News](treasury-yields-news.md)
