# Crypto News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “crypto news” · 49,500/month India · 165,000/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [crypto-news.json](../../examples/use-cases/crypto-news.json).

**Question.** How much news did crypto receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 61,116 |
| Negative · neutral · positive | 33% · 1.2% · 65% |
| Critical (priority 7–9) | 59% (36,164 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (18,777 articles) |
| Negative-to-positive vs all news | 0.69× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 3,016 | 59% | 622 | 2,355 | ███ |
| Sep 2025 | 14,157 | 59% | 2,684 | 11,325 | ███████████████ |
| Oct 2025 | 15,806 | 63% | 3,871 | 11,801 | █████████████████ |
| Nov 2025 | 15,538 | 64% | 4,691 | 10,691 | █████████████████ |
| Dec 2025 | 14,351 | 62% | 3,883 | 10,327 | ███████████████ |
| Jan 2026 | 11,089 | 59% | 2,882 | 8,048 | ████████████ |
| Feb 2026 | 17,460 | 53% | 7,281 | 9,980 | ███████████████████ |
| Mar 2026 | 13,790 | 61% | 4,315 | 9,293 | ███████████████ |
| Apr 2026 | 18,777 | 64% | 5,868 | 12,656 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 13 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 18 Apr 2026 | [France Face Rising Crypto Kidnapping After Multiple Ransom Case](https://bitcoinethereumnews.com/crypto/france-face-rising-crypto-kidnapping-after-multiple-ransom-case/) | bitcoinethereumnews.com | 9 | negative |
| 16 Apr 2026 | [French Police Rescue Mother and Child After $400K Crypto Ransom Kidnapping](https://www.yahoo.com/news/articles/french-police-rescue-mother-child-144638689.html) | yahoo.com | 9 | negative |
| 15 Apr 2026 | [Market Crash? Do THIS Instead! shorts](https://cryptocurrency.com.tr/market-crash-do-this-instead-shorts-266607) | cryptocurrency.com.tr | 9 | negative |
| 9 Apr 2026 | [Iran’s Strait of Hormuz Crypto Toll Plan: Why Tehran’s $1-Per-Barrel Proposal Is Shaking Global Oil Markets…](https://thelogicstick.com/rans-strait-of-hormuz-crypto-toll-plan/) | thelogicstick.com | 9 | negative |
| 9 Apr 2026 | [Why the Hormuz Crisis Is Still Crippling Global Shipping](https://serrarigroup.com/why-the-hormuz-crisis-is-still-crippling-global-shipping/) ⚠ | serrarigroup.com | 9 | negative |
| 8 Apr 2026 | [Bitcoin Rises, Oil Falls as US–Iran Ceasefire Eases Fears](https://bitcoinethereumnews.com/bitcoin/bitcoin-rises-oil-falls-as-us-iran-ceasefire-eases-fears/) | bitcoinethereumnews.com | 9 | negative |
| 7 Apr 2026 | [Trump plays roulette with Iran as oil and Bitcoin hold their breath](https://crypto.news/trump-plays-roulette-with-iran-as-oil-and-bitcoin-hold-their-breath/) | crypto.news | 9 | negative |
| 27 Mar 2026 | [Bitcoin Plunges 3% And ETFs Bleed $171M After Ukraine Destroys Russian Oil Ports](https://www.benzinga.com/crypto/cryptocurrency/26/03/51510607/bitcoin-plunges-3-and-etfs-bleed-171m-after-ukraine-destroys-russian-oil-ports) | benzinga.com | 9 | negative |
| 17 Feb 2026 | [$600K USDT Lost in Sophisticated Address Poisoning Attack](https://bitcoinethereumnews.com/tech/600k-usdt-lost-in-sophisticated-address-poisoning-attack/) | bitcoinethereumnews.com | 9 | negative |
| 10 Feb 2026 | [Daren Li Flees Ankle Monitor, Sentenced in Absentia for Global Cryptocurrency Scam](https://thenewscrypto.com/daren-li-flees-ankle-monitor-sentenced-in-absentia-for-global-cryptocurrency-scam/) | thenewscrypto.com | 9 | negative |
| 2 Feb 2026 | [$41M in Losses as Crypto Wrench Attacks Hit Record High in 2025](https://www.yahoo.com/news/articles/41m-losses-crypto-wrench-attacks-140102565.html) | yahoo.com | 9 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q crypto --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q crypto --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q crypto --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q crypto --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "crypto", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "crypto", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Stock Market News](stock-market-news.md)
- [GST News](gst-news.md)
- [Gold Price News](gold-price-news.md)
