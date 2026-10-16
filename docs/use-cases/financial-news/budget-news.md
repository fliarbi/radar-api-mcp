# Budget News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “budget news” · 6,600/month India · 880/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [budget-news.json](../../examples/use-cases/budget-news.json).

**Question.** How much news did budget receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 100,660 |
| Negative · neutral · positive | 33% · 3.8% · 63% |
| Critical (priority 7–9) | 49% (49,479 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (32,179 articles) |
| Negative-to-positive vs all news | 0.72× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 5,595 | 37% | 1,995 | 3,345 | ███ |
| Sep 2025 | 20,077 | 40% | 7,030 | 12,265 | ████████████ |
| Oct 2025 | 15,506 | 54% | 7,585 | 7,061 | ██████████ |
| Nov 2025 | 25,826 | 40% | 16,125 | 8,830 | ████████████████ |
| Dec 2025 | 18,440 | 43% | 6,384 | 10,919 | ███████████ |
| Jan 2026 | 17,782 | 51% | 5,876 | 10,951 | ███████████ |
| Feb 2026 | 32,179 | 57% | 10,102 | 20,903 | ████████████████████ |
| Mar 2026 | 28,439 | 36% | 7,697 | 19,980 | ██████████████████ |
| Apr 2026 | 22,260 | 53% | 9,818 | 11,416 | ██████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 12 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [Australian Prime Minister Television interview – ABC Afternoon Briefing](https://www.nationaltribune.com.au/australian-prime-minister-television-interview-abc-afternoon-briefing-6/) ⚠ | nationaltribune.com.au | 9 | negative |
| 16 Apr 2026 | [IEA warns Europe has 6 weeks of jet fuel left](https://qz.com/iea-europe-jet-fuel-shortage-flight-cancellations-041626) ⚠ | qz.com | 9 | negative |
| 16 Apr 2026 | [EasyJet boss warns of summer price hike after £25million hit from jet fuel costs](https://www.mirror.co.uk/money/easyjet-boss-warns-summer-price-37025739) | mirror.co.uk | 9 | negative |
| 10 Apr 2026 | [Dazed delegates to IMF spring meetings wait in suspense - OMFIF](https://www.omfif.org/2026/04/delegates-to-imf-spring-meetings-wait-in-suspense/) ⚠ | omfif.org | 9 | negative |
| 7 Apr 2026 | [Singapore Parliament to Discuss Measures Protecting Citizens from Middle East Conflict Impacts](https://world.infonasional.com/singapore-parliament-middle-east-conflict) ⚠ | world.infonasional.com | 9 | negative |
| 3 Apr 2026 | [Trump says US can open Strait of Hormuz with 'a little more time'](http://www.euronews.com/2026/04/03/trump-says-us-can-open-hormuz-with-a-little-more-time-and-asks-congress-for-15tr-for-defen) ⚠ | euronews.com | 9 | negative |
| 1 Apr 2026 | [Russia's Oil Windfall Is a Mirage: Why the US-Iran War Won't Save Moscow's Economy](https://www.ctol.digital/news/russia-oil-windfall-mirage-us-iran-war-wont-save-moscow-economy/) ⚠ | ctol.digital | 9 | negative |
| 25 Mar 2026 | [Philippines Declares State of National Energy Emergency Amid Middle East Crisis \| the deep dive](https://thedeepdive.ca/philippines-declares-state-of-national-energy-emergency-amid-middle-east-crisis/) ⚠ | thedeepdive.ca | 9 | negative |
| 9 Mar 2026 | [Iran war ‘could bring down global economy’ after warning oil could reach $150 a barrel](https://www.aol.com/news/oil-prices-could-reach-100-145013320.html) ⚠ | aol.com | 9 | negative |
| 30 Apr 2026 | [B.C. cancels care home, hospital construction contracts amid budget pressure - Quesnel Cariboo Observer](https://quesnelobserver.com/2026/04/30/b-c-cancels-care-home-hospital-construction-contracts-amid-budget-pressure/) | quesnelobserver.com | 8 | negative |
| 30 Apr 2026 | [B.C. cancels care home, hospital construction contracts amid budget pressure - Abbotsford News](https://abbynews.com/2026/04/30/b-c-cancels-care-home-hospital-construction-contracts-amid-budget-pressure/) | abbynews.com | 8 | negative |
| 30 Apr 2026 | [B.C. cancels care home, hospital construction contracts amid budget pressure - Chemainus Valley Courier](https://chemainusvalleycourier.ca/2026/04/30/b-c-cancels-care-home-hospital-construction-contracts-amid-budget-pressure/) | chemainusvalleycourier.ca | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q budget --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q budget --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q budget --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q budget --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "budget", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "budget", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [S&P 500 News Today](s-p-500-news-today.md)
- [UPI News](upi-news.md)
- [SEBI News](sebi-news.md)
- [Income Tax News](income-tax-news.md)
