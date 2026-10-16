# Commercial Real Estate News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “commercial real estate news” · 50/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [commercial-real-estate-news.json](../../examples/use-cases/commercial-real-estate-news.json).

**Question.** How much news did commercial real estate receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,418 |
| Negative · neutral · positive | 12% · 2.3% · 86% |
| Critical (priority 7–9) | 26% (1,156 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (1,293 articles) |
| Negative-to-positive vs all news | 0.19× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 148 | 23% | 21 | 127 | ██ |
| Sep 2025 | 692 | 24% | 82 | 593 | ███████████ |
| Oct 2025 | 700 | 29% | 78 | 606 | ███████████ |
| Nov 2025 | 579 | 28% | 66 | 496 | █████████ |
| Dec 2025 | 729 | 31% | 96 | 612 | ███████████ |
| Jan 2026 | 740 | 23% | 75 | 638 | ███████████ |
| Feb 2026 | 1,142 | 33% | 165 | 957 | ██████████████████ |
| Mar 2026 | 1,243 | 24% | 137 | 1,075 | ███████████████████ |
| Apr 2026 | 1,293 | 24% | 142 | 1,124 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 18 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 17 Apr 2026 | [Big Banks Are Still Shedding Real Estate Debt](https://www.bisnow.com/national/news/capital-markets/big-banks-still-shedding-real-estate-debt-and-thats-a-good-thing-134177) | bisnow.com | 8 | negative |
| 10 Apr 2026 | [Consumer Sentiment Sours Over Inflation Concerns](https://www.bisnow.com/national/news/economy/weak-consumer-sentiment-inflation-concerns-pressure-economy-134081) ⚠ | bisnow.com | 8 | negative |
| 7 Apr 2026 | [Iran war: Energy supply disruption threatens malls, office projects- Moneycontrol.com](https://www.moneycontrol.com/news/business/real-estate/iran-war-energy-supply-disruption-threatens-malls-office-projects-13882352.html) | moneycontrol.com | 8 | negative |
| 31 Mar 2026 | [Signature Global, RMZ JV for Gurugram Project](https://money.rediff.com/news/market/signature-global-rmz-jv-for-gurugram-project/44493720260331) | money.rediff.com | 8 | positive |
| 30 Mar 2026 | [Credit growth at 13.9% y-o-y; deposit growth dips to 10.8% as on mid-March](https://www.financialexpress.com/business/banking-finance-credit-growth-at-13-9-y-o-y-deposit-growth-dips-to-108-as-on-mid-march-4189781/) | financialexpress.com | 8 | positive |
| 30 Mar 2026 | [Hyderabad Leads India GCC Expansion Wave](https://urbanacres.in/hyderabad-leads-india-gcc-expansion-wave/) | urbanacres.in | 8 | positive |
| 23 Mar 2026 | [Affordable housing is possible, if we stop ignoring the obvious \| Opinion](https://www.usatoday.com/story/opinion/2026/03/23/affordable-housing-vacant-offices-remote-work/89085433007/) | usatoday.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "commercial real estate" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "commercial real estate" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "commercial real estate" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "commercial real estate" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "commercial real estate", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "commercial real estate", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Pension News](pension-news.md)
- [Repo Rate News](repo-rate-news.md)
- [Rupee News](rupee-news.md)
- [ECB News Today](ecb-news-today.md)
