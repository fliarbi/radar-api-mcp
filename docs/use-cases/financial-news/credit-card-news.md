# Credit Card News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “credit card news” · 480/month India · 1,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [credit-card-news.json](../../examples/use-cases/credit-card-news.json).

**Question.** How much news did credit card receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 7,882 |
| Negative · neutral · positive | 33% · 4.9% · 62% |
| Critical (priority 7–9) | 35% (2,729 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (2,160 articles) |
| Negative-to-positive vs all news | 0.73× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 565 | 30% | 160 | 394 | █████ |
| Sep 2025 | 2,075 | 33% | 702 | 1,322 | ███████████████████ |
| Oct 2025 | 1,765 | 28% | 486 | 1,240 | ████████████████ |
| Nov 2025 | 1,554 | 30% | 467 | 1,052 | ██████████████ |
| Dec 2025 | 1,509 | 32% | 457 | 985 | ██████████████ |
| Jan 2026 | 1,806 | 43% | 685 | 1,047 | █████████████████ |
| Feb 2026 | 1,929 | 29% | 574 | 1,203 | ██████████████████ |
| Mar 2026 | 1,987 | 29% | 580 | 1,305 | ██████████████████ |
| Apr 2026 | 2,160 | 38% | 784 | 1,296 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 14 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Haryana women's panel chief visits suicide-hit NIT Kurukshetra, cites 'online gambling, credit card debt'](https://theprint.in/india/education/haryana-womens-panel-chief-visits-suicide-hit-nit-kurukshetra-cites-online-gambling-credit-card-debt/2917297/) | theprint.in | 8 | negative |
| 28 Apr 2026 | [Acquirers Hold Payment Tokens Hostage. Here Are The Real Rules of Negotiation](https://reformingretail.com/index.php/2026/04/28/acquirers-hold-payment-tokens-hostage-here-are-the-real-rules-of-negotiation/) ⚠ | reformingretail.com | 8 | negative |
| 28 Apr 2026 | [Credit card spends jump to ₹2.19 lakh crore in March; HDFC hits record share, SBI Card outperforms -…](https://www.businesstoday.in/personal-finance/banking/story/credit-card-spends-jump-to-rs219-lakh-crore-in-march-hdfc-hits-record-share-sbi-outperforms-527779-2026-04-28) | businesstoday.in | 8 | positive |
| 25 Apr 2026 | [Tax alert: Credit card spending can invite notices — How to avoid penalties - BusinessToday](https://www.businesstoday.in/personal-finance/tax/story/tax-alert-credit-card-spending-can-invite-notices-how-to-avoid-penalties-527454-2026-04-25) | businesstoday.in | 8 | negative |
| 24 Apr 2026 | [Why RBI cancelled Paytm Payments Bank’s banking licence](https://indianexpress.com/article/explained/explained-economics/why-rbi-cancelled-paytm-payments-banks-banking-licence-10654383/) ⚠ | indianexpress.com | 8 | negative |
| 23 Apr 2026 | [Ledger Users Think They're Safe – Wait Until You See BMIC's Quantum-Safe Wallet, Crypto Presale Live -…](https://insidebitcoins.com/press-releases/ledger-users-think-theyre-safe-wait-until-you-see-bmics-quantum-safe-wallet-crypto-presale-live) ⚠ | insidebitcoins.com | 8 | positive |
| 21 Apr 2026 | [Shivraj Singh Chouhan calls for overhaul of rural credit system, citing \"ordeal\" for farmers](https://www.dailyexcelsior.com/shivraj-singh-chouhan-calls-for-overhaul-of-rural-credit-system-citing-ordeal-for-farmers/) | dailyexcelsior.com | 8 | negative |
| 19 Apr 2026 | [SEC Charges Bitcoin Latinum Founder Donald Basile With $16 Million Investor Fraud](https://bitcoinethereumnews.com/bitcoin/sec-charges-bitcoin-latinum-founder-donald-basile-with-16-million-investor-fraud/) | bitcoinethereumnews.com | 8 | negative |
| 18 Apr 2026 | [JPMorgan Chase, Citi and Wells Fargo Lose $5,606,000,000 to Bad Loans in Just Three Months - The Daily Hodl](https://dailyhodl.com/2026/04/18/jpmorgan-chase-citi-and-wells-fargo-lose-5606000000-to-bad-loans-in-just-three-months/) | dailyhodl.com | 8 | negative |
| 17 Apr 2026 | [Mastercard explores sale of payments unit it bought from Nets in 2019, FT reports \| M & A Critique â…](https://www.magzter.com/de/stories/business/M-A-Critique/MASTERCARD-EXPLORES-SALE-OF-PAYMENTS-UNIT-IT-BOUGHT-FROM-NETS-IN-2019-FT-REPORTS) | magzter.com | 8 | positive |
| 17 Apr 2026 | [{Ø§ÙØ¹ÙÙØ§Ù: Ø³ÙØ³ÙØ©} \| {Ø§Ø³Ù Ø§ÙÙ ØºÙØ§Ø·ÙØ³: Ø³ÙØ³ÙØ©} - {Ø§ÙÙØ¦Ø©: Ø³ÙØ³ÙØ©} - Ø§ÙØ±Ø£…](https://www.magzter.com/ar/stories/business/M-A-Critique/MASTERCARD-EXPLORES-SALE-OF-PAYMENTS-UNIT-IT-BOUGHT-FROM-NETS-IN-2019-FT-REPORTS) | magzter.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "credit card" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "credit card" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "credit card" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "credit card" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "credit card", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "credit card", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [ETF News](etf-news.md)
- [GDP News](gdp-news.md)
- [Hedge Fund News](hedge-fund-news.md)
- [Dividend News](dividend-news.md)
