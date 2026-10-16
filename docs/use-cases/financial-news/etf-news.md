# ETF News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “etf news” · 140/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [etf-news.json](../../examples/use-cases/etf-news.json).

**Question.** How much news did etf receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 112,225 |
| Negative · neutral · positive | 20% · 1.3% · 78% |
| Critical (priority 7–9) | 25% (27,517 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (37,206 articles) |
| Negative-to-positive vs all news | 0.35× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 5,702 | 23% | 1,079 | 4,581 | ███ |
| Sep 2025 | 24,285 | 24% | 3,756 | 20,121 | █████████████ |
| Oct 2025 | 20,481 | 31% | 4,470 | 15,786 | ███████████ |
| Nov 2025 | 21,369 | 32% | 4,634 | 16,548 | ███████████ |
| Dec 2025 | 23,590 | 34% | 5,529 | 17,848 | █████████████ |
| Jan 2026 | 22,317 | 22% | 3,888 | 18,071 | ████████████ |
| Feb 2026 | 25,455 | 35% | 6,405 | 18,768 | ██████████████ |
| Mar 2026 | 27,247 | 22% | 5,632 | 21,249 | ███████████████ |
| Apr 2026 | 37,206 | 21% | 6,711 | 29,873 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 13 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 20 Apr 2026 | [Trump’s Iran bomb warning puts oil, Bitcoin and crypto risk back in play](https://bitcoinethereumnews.com/bitcoin/trumps-iran-bomb-warning-puts-oil-bitcoin-and-crypto-risk-back-in-play/) ⚠ | bitcoinethereumnews.com | 9 | negative |
| 9 Apr 2026 | [A Two-Week Iran Ceasefire Crashed Oil 10% and Sent Bitcoin Past $72,000: It Started Unraveling Within Hours](https://bitcoinethereumnews.com/bitcoin/a-two-week-iran-ceasefire-crashed-oil-10-and-sent-bitcoin-past-72000-it-started-unraveling-within-hours/) ⚠ | bitcoinethereumnews.com | 9 | negative |
| 7 Apr 2026 | [Evening digest: Trump’s Iran deadline nears, oil surge shakes markets](https://www.bitcoininsider.org/article/301413/evening-digest-trumps-iran-deadline-nears-oil-surge-shakes-markets) ⚠ | bitcoininsider.org | 9 | negative |
| 27 Mar 2026 | [Bitcoin Plunges 3% And ETFs Bleed $171M After Ukraine Destroys Russian Oil Ports](https://www.benzinga.com/crypto/cryptocurrency/26/03/51510607/bitcoin-plunges-3-and-etfs-bleed-171m-after-ukraine-destroys-russian-oil-ports) | benzinga.com | 9 | negative |
| 27 Mar 2026 | [Ukraine Oil Attack Disrupts Trump's Price Plan, Heightens Bitcoin Macro Risk](https://bitcoinethereumnews.com/bitcoin/ukraine-oil-attack-disrupts-trumps-price-plan-heightens-bitcoin-macro-risk/) ⚠ | bitcoinethereumnews.com | 9 | negative |
| 30 Apr 2026 | [Warner Bros. Discovery CEO David Zaslavâs Pay More Than Tripled in 2025 to a Staggering $165 MillionÂ](https://au.variety.com/2026/biz/news/david-zaslav-warner-bros-discovery-compensation-2025-36094/) ⚠ | au.variety.com | 8 | negative |
| 30 Apr 2026 | [Why Jerome Powell Refuses to Leave the Fed](https://crypto.news/why-jerome-powell-refuses-to-leave-the-fed/) ⚠ | crypto.news | 8 | negative |
| 30 Apr 2026 | [Could Pepeto Be the Next Crypto to Explode as Strategy Loads 818,334 BTC While SOL and BNB Stall](https://www.openpr.com/news/4497376/could-pepeto-be-the-next-crypto-to-explode-as-strategy-loads) ⚠ | openpr.com | 8 | negative |
| 30 Apr 2026 | [David Zaslav's Warner Bros. Discovery Pay Package Skyrocketed In 2025 - SlashFilm](https://www.slashfilm.com/2161269/david-zaslav-2025-warner-bros-discovery-pay-package/) ⚠ | slashfilm.com | 8 | negative |
| 30 Apr 2026 | [Eric Trump Reiterates $1 Million Bitcoin Forecast At](https://www.tronweekly.com/eric-trump-reiterates-1-million-bitcoin/) | tronweekly.com | 8 | positive |
| 30 Apr 2026 | [Alphabet Soars, Meta Sinks As Big Tech Splits — ETFs Let You Pick The Right Side - Alphabet (NASDAQ:GOOGL](https://www.benzinga.com/etfs/sector-etfs/26/04/52178697/alphabet-soars-meta-sinks-as-big-tech-splits-etfs-let-you-pick-the-right-side) | benzinga.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q ETF --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q ETF --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q ETF --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q ETF --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "ETF", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "ETF", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [ECB News Today](ecb-news-today.md)
- [Stablecoin News](stablecoin-news.md)
- [GDP News](gdp-news.md)
- [Credit Card News](credit-card-news.md)
