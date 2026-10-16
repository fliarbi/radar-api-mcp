# Pension News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “pension news” · 1,900/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [pension-news.json](../../examples/use-cases/pension-news.json).

**Question.** How much news did pension receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 12,138 |
| Negative · neutral · positive | 42% · 6.6% · 51% |
| Critical (priority 7–9) | 58% (7,093 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,680 articles) |
| Negative-to-positive vs all news | 1.11× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 805 | 60% | 389 | 346 | ████ |
| Sep 2025 | 3,367 | 58% | 1,338 | 1,804 | ██████████████████ |
| Oct 2025 | 2,922 | 61% | 1,356 | 1,331 | ████████████████ |
| Nov 2025 | 3,138 | 61% | 1,611 | 1,305 | █████████████████ |
| Dec 2025 | 2,644 | 58% | 1,178 | 1,253 | ██████████████ |
| Jan 2026 | 2,684 | 56% | 1,018 | 1,550 | ███████████████ |
| Feb 2026 | 2,994 | 57% | 1,242 | 1,544 | ████████████████ |
| Mar 2026 | 2,780 | 61% | 1,205 | 1,356 | ███████████████ |
| Apr 2026 | 3,680 | 59% | 1,625 | 1,769 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 16 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [£400bn LGPS: What pooling means for private credit investments](https://alternativecreditinvestor.com/2026/04/30/400bn-lgps-what-pooling-means-for-private-credit-investments/) | alternativecreditinvestor.com | 8 | positive |
| 29 Apr 2026 | [Fisco, Cgil alarm: 730 at risk for errors on incomes. The Inland Revenue: pre-filled forms already updated](https://en.ilsole24ore.com/art/fisco-l-allarme-cgil-730-risk-of-errors-single-income-certifications-AIPP47lC) | en.ilsole24ore.com | 8 | negative |
| 29 Apr 2026 | [Your clients’ retirement portfolios took a hit as global slump impacts institutional returns](https://www.investmentnews.com/retirement-planning/your-clients-retirement-portfolios-took-a-hit-as-global-slump-impacts-intuitional-returns/266356) | investmentnews.com | 8 | negative |
| 29 Apr 2026 | [PenCom to employers: Obey CPS rules or face sanctions](https://thesun.ng/pencom-to-employers-obey-cps-rules-or-face-sanctions-2/) | thesun.ng | 8 | negative |
| 28 Apr 2026 | [Iran War-Related Volatility Wiped Out $233B in Public Pension Funding \| PLANSPONSOR](https://www.plansponsor.com/iran-war-related-volatility-wiped-out-233b-in-public-pension-funding/) | plansponsor.com | 8 | negative |
| 28 Apr 2026 | [Temasek, Canadian pension fund among investors looking to sell stakes in India’s NSE IPO: sources](https://www.businesstimes.com.sg/companies-markets/temasek-canadian-pension-fund-among-investors-looking-sell-stakes-indias-nse-ipo-sources) | businesstimes.com.sg | 8 | positive |
| 28 Apr 2026 | [Temasek, CPPIB Among Investors Eyeing Stake Sale in NSE’s $2.75 Billion IPO \| Unique Times Magazine](https://uniquetimes.org/temasek-cppib-among-investors-eyeing-stake-sale-in-nses-2-75-billion-ipo/) | uniquetimes.org | 8 | positive |
| 27 Apr 2026 | [Nirmala Sitharaman Confirms IDBI Bank Privatisation to Continue Despite Failed Bids](https://studycafe.in/nirmala-sitharaman-confirms-idbi-bank-privatisation-to-continue-despite-failed-bids-418277.html) ⚠ | studycafe.in | 8 | negative |
| 27 Apr 2026 | [Government is not lacking in nuclear ambition – so why is nothing happening?](https://www.cityam.com/government-is-not-lacking-in-nuclear-ambition-so-why-is-nothing-happening/) ⚠ | cityam.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q pension --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q pension --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q pension --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q pension --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "pension", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "pension", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Mergers and Acquisitions News](mergers-and-acquisitions-news.md)
- [Private Equity News](private-equity-news.md)
- [Repo Rate News](repo-rate-news.md)
- [Commercial Real Estate News](commercial-real-estate-news.md)
