# Dow Jones News Today: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “dow jones news today” · 1,300/month India · 8,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [dow-jones-news-today.json](../../examples/use-cases/dow-jones-news-today.json).

**Question.** How much news did dow jones receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 9,385 |
| Negative · neutral · positive | 56% · 3.5% · 40% |
| Critical (priority 7–9) | 48% (4,528 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,269 articles) |
| Negative-to-positive vs all news | 1.87× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 483 | 53% | 206 | 266 | ███ |
| Sep 2025 | 2,034 | 46% | 859 | 1,081 | ████████████ |
| Oct 2025 | 1,665 | 62% | 770 | 875 | ██████████ |
| Nov 2025 | 1,478 | 57% | 717 | 732 | █████████ |
| Dec 2025 | 1,408 | 44% | 631 | 734 | █████████ |
| Jan 2026 | 1,311 | 46% | 603 | 667 | ████████ |
| Feb 2026 | 2,469 | 45% | 1,226 | 1,184 | ███████████████ |
| Mar 2026 | 2,336 | 56% | 1,576 | 708 | ██████████████ |
| Apr 2026 | 3,269 | 46% | 1,851 | 1,239 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 13 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 14 Apr 2026 | [Asian stocks rally, crude drops on lingering hope for a peace deal](https://www.digitaljournal.com/world/asian-stocks-rally-crude-drops-on-lingering-hope-for-a-peace-deal/article) ⚠ | digitaljournal.com | 9 | negative |
| 9 Apr 2026 | [Oil price surges towards $100 as Middle East ceasefire begins to unravel](https://bmmagazine.co.uk/news/oil-price-rises-iran-ceasefire-cracks-strait-hormuz/) ⚠ | bmmagazine.co.uk | 9 | negative |
| 7 Apr 2026 | [Evening digest: Trump’s Iran deadline nears, oil surge shakes markets](https://www.bitcoininsider.org/article/301413/evening-digest-trumps-iran-deadline-nears-oil-surge-shakes-markets) ⚠ | bitcoininsider.org | 9 | negative |
| 7 Apr 2026 | [How the Iran war may be stopping a different full-scale conflict \| Mint](https://www.livemint.com/global/how-the-iran-war-may-be-stopping-a-different-full-scale-conflict-11775551697611.html) ⚠ | livemint.com | 9 | negative |
| 22 Mar 2026 | [Will gas prices reach $2.00 per litre?](https://kitchener.citynews.ca/2026/03/22/will-gas-prices-reach-2-00-per-litre/) ⚠ | kitchener.citynews.ca | 9 | negative |
| 30 Apr 2026 | [S&P 500 Edges Higher Amid Mixed Mega-Cap Earnings; Dow Leads Market Indexes Overall \| The Motley Fool](https://www.fool.com/investing/2026/04/30/sp-500-edges-higher-amid-mixed-mega-cap-earnings-d/) | fool.com | 8 | positive |
| 30 Apr 2026 | ["Magnificent Seven" Companies Microsoft, Amazon, Alphabet, and Meta Just Reported Earnings. Here Are the…](https://www.fool.com/investing/2026/04/30/magnificent-seven-companies-microsoft-amazon-alpha/) | fool.com | 8 | positive |
| 30 Apr 2026 | [US Tech Stocks Decline as OpenAI Revenue Concerns Trigger Selloff](https://www.harianbasis.co/en/tech-stocks-decline-openai-concerns) | harianbasis.co | 8 | negative |
| 30 Apr 2026 | [Dow Jones boosted by Caterpillar as S&P 500 closes above 7,200 for first time](https://www.proactiveinvestors.com/companies/news/1091518/dow-jones-boosted-by-caterpillar-as-s-p-500-closes-above-7-200-for-first-time-1091518.html) | proactiveinvestors.com | 8 | positive |
| 29 Apr 2026 | [The Morning Catch-Up: ASX set to fall as oil surge and Fed split rattle market confidence](https://au.finance.yahoo.com/news/morning-catch-asx-set-fall-234200526.html) | au.finance.yahoo.com | 8 | negative |
| 29 Apr 2026 | [Wall Street recule, la Fed temporise, le pétrole flambe !](https://boursier.com/indices/actualites/news/wall-street-recule-la-fed-temporise-le-petrole-flambe-984479.html) | boursier.com | 8 | negative |
| 29 Apr 2026 | [Dow Jones Today: Why the Blue-Chip Index Is Sliding Before Powell, Big Tech and the Oil Shock](https://ts2.tech/en/dow-jones-today-why-the-blue-chip-index-is-sliding-before-powell-big-tech-and-the-oil-shock/) | ts2.tech | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "dow jones" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "dow jones" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "dow jones" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "dow jones" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "dow jones", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "dow jones", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Mortgage Rates News](mortgage-rates-news.md)
- [Silver Price News](silver-price-news.md)
- [Interest Rates News](interest-rates-news.md)
- [S&P 500 News Today](s-p-500-news-today.md)
