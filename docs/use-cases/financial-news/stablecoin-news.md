# Stablecoin News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “stablecoin news” · 170/month India · 1,900/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [stablecoin-news.json](../../examples/use-cases/stablecoin-news.json).

**Question.** How much news did stablecoin receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 9,420 |
| Negative · neutral · positive | 19% · 1.1% · 80% |
| Critical (priority 7–9) | 76% (7,145 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (3,068 articles) |
| Negative-to-positive vs all news | 0.31× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 387 | 79% | 55 | 332 | ███ |
| Sep 2025 | 2,288 | 77% | 214 | 2,055 | ███████████████ |
| Oct 2025 | 2,309 | 79% | 343 | 1,951 | ███████████████ |
| Nov 2025 | 2,409 | 78% | 478 | 1,914 | ████████████████ |
| Dec 2025 | 2,404 | 78% | 373 | 2,007 | ████████████████ |
| Jan 2026 | 1,794 | 74% | 267 | 1,506 | ████████████ |
| Feb 2026 | 2,308 | 75% | 473 | 1,801 | ███████████████ |
| Mar 2026 | 2,250 | 76% | 453 | 1,768 | ███████████████ |
| Apr 2026 | 3,068 | 78% | 560 | 2,491 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 17 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [Legora Raises $600M, Hits $5.6B Valuation in AI Boom](https://ventureburn.com/legora-raises-600m-hits-5-6b-valuation-in-ai-boom/) ⚠ | ventureburn.com | 8 | positive |
| 29 Apr 2026 | [Hong Kong Issues Stablecoin Fraud Alert Over Fake HSBC,](https://www.tronweekly.com/hong-kong-issues-stablecoin-fraud-alert-over/) | tronweekly.com | 8 | negative |
| 29 Apr 2026 | [Aftermath Finance Exploit Drains $1.1M in USDC](https://coincu.com/aftermath-finance-exploit-1-1m-usdc-stolen/) ⚠ | coincu.com | 8 | negative |
| 28 Apr 2026 | [CertiK Finds AML Now Top Crypto Risk, Eclipsing SEC Cases](https://beincrypto.com/certik-report-aml-crypto-regulatory-risk/) ⚠ | beincrypto.com | 8 | negative |
| 28 Apr 2026 | [Is Binance Stablecoin Inflows Putting Bitcoin’s $79K Test in Focus?](https://www.analyticsinsight.net/news/is-binance-stablecoin-inflows-putting-bitcoins-79k-test-in-focus) | analyticsinsight.net | 8 | negative |
| 28 Apr 2026 | [A digital shekel is here: Israel approves its first-ever regulated stablecoin](https://www.coindesk.com/policy/2026/04/28/a-digital-shekel-is-here-israel-approves-its-first-regulated-stablecoin) | coindesk.com | 8 | negative |
| 28 Apr 2026 | [ADA Price Prediction: Pepeto Outpaces Cardano and Ethereum in the Presale Returns Game](https://www.openpr.com/news/4491685/ada-price-prediction-pepeto-outpaces-cardano-and-ethereum) | openpr.com | 8 | negative |
| 28 Apr 2026 | [AML Fines Eclipse SEC Cases as Top Crypto Risk: Report](https://www.cointelegraph.com/news/aml-crackdown-eclipses-securities-enforcement-crypto-report) ⚠ | cointelegraph.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q stablecoin --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q stablecoin --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q stablecoin --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q stablecoin --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "stablecoin", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "stablecoin", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Rupee News](rupee-news.md)
- [ECB News Today](ecb-news-today.md)
- [ETF News](etf-news.md)
- [GDP News](gdp-news.md)
