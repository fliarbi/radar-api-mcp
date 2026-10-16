# Treasury Yields News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “treasury yields news” · 50/month India · 1,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [treasury-yields-news.json](../../examples/use-cases/treasury-yields-news.json).

**Question.** How much news did treasury yields receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 630 |
| Negative · neutral · positive | 57% · 1.1% · 42% |
| Critical (priority 7–9) | 58% (365 articles) |
| Busiest month, May 2025 – Apr 2026 | Mar 2026 (229 articles) |
| Negative-to-positive vs all news | 1.84× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 32 | 72% | 21 | 11 | ███ |
| Sep 2025 | 181 | 71% | 107 | 74 | ████████████████ |
| Oct 2025 | 100 | 74% | 68 | 31 | █████████ |
| Nov 2025 | 85 | 61% | 48 | 36 | ███████ |
| Dec 2025 | 176 | 68% | 111 | 61 | ███████████████ |
| Jan 2026 | 121 | 74% | 74 | 46 | ███████████ |
| Feb 2026 | 149 | 54% | 69 | 80 | █████████████ |
| Mar 2026 | 229 | 59% | 154 | 71 | ████████████████████ |
| Apr 2026 | 131 | 47% | 62 | 67 | ███████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 17 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [US Mortgage Rates Surge to 6.5 Percent Amid Middle East Tensions](https://www.asatunews.co.id/en/mortgage-rates-surge-iran-tension) ⚠ | asatunews.co.id | 8 | positive |
| 28 Apr 2026 | [Why Is Gold Falling? Gold Price Risk Crash to $3,400](https://www.financemagnates.com/trending/why-is-gold-falling-gold-price-risk-crash-to-3400) | financemagnates.com | 8 | negative |
| 21 Apr 2026 | [S&P 500 Eases, Crude Soars To $90: Stock Market Today - State Street Energy Select Sector SPDR ETF (ARCA:](https://www.benzinga.com/markets/equities/26/04/51951795/sp-500-falls-oil-surges-iran-stalemate-stalls-stocks-markets-tuesday) | benzinga.com | 8 | positive |
| 17 Apr 2026 | [Yields fall as hopes of end to Iran war ease inflation fears \| Stock Market News](https://www.livemint.com/market/yields-fall-as-hopes-of-end-to-iran-war-ease-inflation-fears-11776453342062.html) | livemint.com | 8 | negative |
| 15 Apr 2026 | [Treasury yields plunge, dollar hits key technical targets](https://cryptocurrency.com.tr/treasury-yields-plunge-dollar-hits-key-technical-targets-267303) | cryptocurrency.com.tr | 8 | negative |
| 10 Apr 2026 | [Buying A Home Just Got Harder — US Home Loan Rates Could Stay Near 6% For The Rest Of The Decade](https://www.ibtimes.co.uk/buying-home-just-got-harder-us-home-loan-rates-could-stay-near-6-rest-decade-1791141) ⚠ | ibtimes.co.uk | 8 | negative |
| 9 Apr 2026 | [US bond yields drop as Middle East ceasefire boosts rate-cut expectations](https://www.zawya.com/en/capital-markets/bonds/us-bond-yields-drop-as-middle-east-ceasefire-boosts-rate-cut-expectations-eqkqeo80) | zawya.com | 8 | negative |
| 8 Apr 2026 | [India's 10-year bond yield nears 6.90% on Iran ceasefire, RBI decision awaited](https://economictimes.indiatimes.com/markets/bonds/indias-10-year-bond-yield-nears-6-90-on-iran-ceasefire-rbi-decision-awaited/articleshow/130102572.cms) ⚠ | economictimes.indiatimes.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "treasury yields" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "treasury yields" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "treasury yields" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "treasury yields" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "treasury yields", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "treasury yields", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Unemployment News](unemployment-news.md)
- [Retirement News](retirement-news.md)
- [Yen News](yen-news.md)
- [Market Crash News](market-crash-news.md)
