# Recession News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “recession news” · 1,900/month India · 4,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [recession-news.json](../../examples/use-cases/recession-news.json).

**Question.** How much news did recession receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,342 |
| Negative · neutral · positive | 67% · 4.5% · 28% |
| Critical (priority 7–9) | 65% (2,822 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,633 articles) |
| Negative-to-positive vs all news | 3.21× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 284 | 70% | 194 | 77 | ███ |
| Sep 2025 | 906 | 68% | 590 | 283 | ███████████ |
| Oct 2025 | 828 | 62% | 552 | 229 | ██████████ |
| Nov 2025 | 719 | 62% | 448 | 238 | █████████ |
| Dec 2025 | 711 | 56% | 411 | 267 | █████████ |
| Jan 2026 | 578 | 54% | 331 | 208 | ███████ |
| Feb 2026 | 841 | 56% | 480 | 318 | ██████████ |
| Mar 2026 | 1,290 | 70% | 971 | 272 | ████████████████ |
| Apr 2026 | 1,633 | 69% | 1,134 | 431 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 14 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [War-linked energy shock pushing inflation higher in Europe: IMF expert](https://www.fibre2fashion.com/news/economics/war-linked-energy-shock-pushing-inflation-higher-in-europe-imf-expert-309803-newsdetails.htm) ⚠ | fibre2fashion.com | 9 | negative |
| 21 Apr 2026 | [Top oil traders, including those from South-East Asia, warn worst of demand hit from the war is yet to come](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/04/21/top-oil-traders-including-those-from-south-east-asia-warn-worst-of-demand-hit-from-the-war-is-yet-to-come) ⚠ | thestar.com.my | 9 | negative |
| 21 Apr 2026 | [Top Oil Traders Say Worst of Demand Hit Is Yet to Come - TT](https://www.transporttopics.com/index%2ephp/articles/top-oil-traders-demand-worst) ⚠ | transporttopics.com | 9 | negative |
| 15 Apr 2026 | [Iran war escalation could push global economy to brink of recession, IMF warns - Türkiye Today](https://www.turkiyetoday.com/business/iran-war-escalation-could-push-global-economy-to-brink-of-recession-imf-warns-3218153) | turkiyetoday.com | 9 | negative |
| 15 Apr 2026 | [La creciente factura de la guerra contra Irán](https://www.expansion.com/opinion/2026/04/15/69df6d47e5fdeac33b8b4581.html) ⚠ | expansion.com | 9 | negative |
| 14 Apr 2026 | [IMF slashes UK economic growth forecasts as Iran war risks global recession](https://www.thenational.scot/news/26020925.imf-says-iran-war-risks-global-recession-growth-forecasts-slashed/) | thenational.scot | 9 | negative |
| 14 Apr 2026 | [Iran war wreaks havoc on global economy and could spark recession, says IMF](http://www.middleeasteye.net/news/iran-war-wreaks-havoc-global-economy-and-could-spark-recession-says-imf) | middleeasteye.net | 9 | negative |
| 14 Apr 2026 | [UK economic growth forecasts slashed as IMF says Iran war risks global recession](https://www.edp24.co.uk/news/national/26020326.uk-economic-growth-forecasts-slashed-imf-says-iran-war-risks-global-recession/) | edp24.co.uk | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q recession --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q recession --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q recession --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q recession --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "recession", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "recession", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Venture Capital News Today](venture-capital-news-today.md)
- [Nasdaq News](nasdaq-news.md)
- [Bank of Japan News](bank-of-japan-news.md)
- [US Dollar News](us-dollar-news.md)
