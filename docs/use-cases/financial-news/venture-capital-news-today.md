# Venture Capital News Today: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “venture capital news today” · 20/month India · 4,400/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [venture-capital-news-today.json](../../examples/use-cases/venture-capital-news-today.json).

**Question.** How much news did venture capital receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 18,074 |
| Negative · neutral · positive | 12% · 1.9% · 86% |
| Critical (priority 7–9) | 56% (10,138 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (5,140 articles) |
| Negative-to-positive vs all news | 0.19× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 877 | 54% | 88 | 775 | ███ |
| Sep 2025 | 3,838 | 61% | 408 | 3,348 | ███████████████ |
| Oct 2025 | 3,399 | 59% | 383 | 2,963 | █████████████ |
| Nov 2025 | 3,293 | 60% | 315 | 2,885 | █████████████ |
| Dec 2025 | 3,117 | 57% | 315 | 2,716 | ████████████ |
| Jan 2026 | 3,438 | 57% | 369 | 2,994 | █████████████ |
| Feb 2026 | 5,140 | 60% | 677 | 4,353 | ████████████████████ |
| Mar 2026 | 4,698 | 50% | 543 | 4,082 | ██████████████████ |
| Apr 2026 | 4,798 | 57% | 609 | 4,101 | ███████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 14 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [SoftBank Eyes $100bn AI Infrastructure Spin-Off as Masayoshi Son Doubles Down on America’s Data Center Boom…](https://www.tekedia.com/softbank-eyes-100bn-ai-infrastructure-spin-off-as-masayoshi-son-doubles-down-on-americas-data-center-boom/) ⚠ | tekedia.com | 8 | positive |
| 30 Apr 2026 | [Legal AI startup Legora hits $5.6B valuation and its battle with Harvey just got hotter \| TechCrunch](https://techcrunch.com/2026/04/30/legal-ai-startup-legora-hits-5-6-valuation-and-its-battle-with-harvey-just-got-hotter/) ⚠ | techcrunch.com | 8 | positive |
| 30 Apr 2026 | [CryptoRank Reveals: Just Six ICOs Closed in 2026 as Market Activity Dries Up - Crypto Economy](https://crypto-economy.com/cryptorank-reveals-just-six-icos-closed-in-2026-as-market-activity-dries-up/) | crypto-economy.com | 8 | negative |
| 30 Apr 2026 | [India's AI Funding Leaderboard for Q1 2026](https://www.analyticsinsight.net/photo/indias-ai-funding-leaderboard-for-q1-2026) | analyticsinsight.net | 8 | positive |
| 30 Apr 2026 | [Navarre: Apple is dead, SaaS is next, you have 18 months.](https://panewslab.com/en/articles/019ddcb5-f99c-731d-b0d4-a6f0fa40b259) ⚠ | panewslab.com | 8 | negative |
| 30 Apr 2026 | [Tether Treasury mints an additional 1 billion USDT on the Tron network.](https://www.panewslab.com/articles/019ddd5b-6398-714b-a517-c34f7040dc46) | panewslab.com | 8 | positive |
| 30 Apr 2026 | [Snabbit’s $56 Mn Series D backs leadership bid in India’s $60 Bn quick home services market](http://chennaipatrika.com/post/snabbits-56-mn-series-d-backs-leadership-bid-in-indias-60-bn-quick-home-services-market) | chennaipatrika.com | 8 | positive |
| 29 Apr 2026 | [Aidoc Secures $150M to Accelerate Enterprise-Scale Clinical AI](https://hitconsultant.net/2026/04/29/aidoc-series-e-funding-clinical-ai-foundation-model/) | hitconsultant.net | 8 | positive |
| 29 Apr 2026 | [How AI’s impact on software is pushing VCs from Bits to Atoms \| VC Cafe](https://www.vccafe.com/how-ais-impact-on-software-is-pushing-vcs-from-bits-to-atoms/) | vccafe.com | 8 | positive |
| 29 Apr 2026 | [A senior Iranian official stated that Iran will respond to US "piracy" with "unprecedented military action."](https://panewslab.com/en/articles/019dd943-3bef-76bf-9e2a-25d93c44ca95) | panewslab.com | 8 | positive |
| 29 Apr 2026 | [Prince Charles to Jeff Bezos, Tim Cook, Jensen Huang: Tell us your problem with British startups - The Times…](https://timesofindia.indiatimes.com/technology/tech-news/prince-charles-to-jeff-bezos-tim-cook-jensen-huang-tell-us-your-problem-with-british-startups/articleshow/130603673.cms) ⚠ | timesofindia.indiatimes.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "venture capital" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "venture capital" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "venture capital" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "venture capital" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "venture capital", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "venture capital", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Sensex News](sensex-news.md)
- [Inflation News](inflation-news.md)
- [Nasdaq News](nasdaq-news.md)
- [Recession News](recession-news.md)
