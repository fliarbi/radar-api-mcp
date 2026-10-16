# Silver Price News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “silver price news” · 9,900/month India · 3,600/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [silver-price-news.json](../../examples/use-cases/silver-price-news.json).

**Question.** How much news did silver price receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 1,325 |
| Negative · neutral · positive | 49% · 0.8% · 50% |
| Critical (priority 7–9) | 10% (137 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (427 articles) |
| Negative-to-positive vs all news | 1.3× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 29 | 14% | 3 | 26 | █ |
| Sep 2025 | 158 | 6.3% | 33 | 124 | ███████ |
| Oct 2025 | 222 | 11% | 72 | 145 | ██████████ |
| Nov 2025 | 120 | 14% | 43 | 72 | ██████ |
| Dec 2025 | 220 | 4.5% | 65 | 152 | ██████████ |
| Jan 2026 | 251 | 8.8% | 82 | 169 | ████████████ |
| Feb 2026 | 327 | 10% | 182 | 143 | ███████████████ |
| Mar 2026 | 320 | 9.4% | 164 | 154 | ███████████████ |
| Apr 2026 | 427 | 12% | 217 | 203 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 10 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 29 Apr 2026 | [Silver Rate Today 29th April 2026: Silver is up by 0.42%; check prices in Mumbai, Bengaluru, Hyderabad,…](https://www.financialexpress.com/market/silver/silver-rate-today-on-29th-april-2026-check-1gm-10gm-1kg-silver-price-today-in-mumbai-bengaluru-hyderabad-delhi-ahmedabad/4221521/) | financialexpress.com | 8 | positive |
| 23 Apr 2026 | [Elon Musk Is Wrong: AI Won’t Create Wealth, It Will Fuel Inflation - Rafi Farber \| Economy \| Before It's News](https://beforeitsnews.com/economy/2026/04/elon-musk-is-wrong-ai-wont-create-wealth-it-will-fuel-inflation-rafi-farber-3163444.html) | beforeitsnews.com | 8 | negative |
| 23 Apr 2026 | [Gold Rates & Silver Rates Today (23 April, 2026) Live Updates: MCX Gold Falls, Silver Price Crashes By 2%](https://www.goodreturns.in/news/gold-rates-silver-rates-today-21-april-2026-live-mcx-gold-silver-price-crash-24k-22k-18k-gold-prices-1503995.html) | goodreturns.in | 8 | negative |
| 20 Apr 2026 | [Gold and Silver Price in India on 20 April 2026: Gold Crashes ₹500 to ₹1,55,290/10g on Akshaya Tritiya,…](https://startuptalky.com/news/gold-silver-price-india-today-20-april-2026/) | startuptalky.com | 8 | negative |
| 17 Apr 2026 | [Ripple’s Global Payments Expansion Strengthens XRP’s Institutional Role](https://cryptocurrency.com.tr/ripple-s-global-payments-expansion-strengthens-xrp-s-institutional-role-274236) | cryptocurrency.com.tr | 8 | negative |
| 13 Apr 2026 | [Silver Rate Today 13th April 2026: Silver is down by 2.08%; check prices in Mumbai, Bengaluru, Hyderabad,…](https://www.financialexpress.com/market/silver/silver-rate-today-on-13th-april-2026-check-1gm-10gm-1kg-silver-price-today-in-mumbai-bengaluru-hyderabad-delhi-ahmedabad/4205457/) | financialexpress.com | 8 | negative |
| 13 Apr 2026 | [US Judge Throws out Lawsuit Against Binance and CZ Over Claims of Funding Linked to Violent Attacks](https://cryptocurrency.com.tr/us-judge-throws-out-lawsuit-against-binance-and-cz-over-claims-of-funding-linked-to-violent-attacks-274234) | cryptocurrency.com.tr | 8 | negative |
| 7 Apr 2026 | [Silver futures decline ₹1,479 to ₹2.31 lakh/kg as geopolitical risks lift inflation outlook](https://www.thehindubusinessline.com/markets/commodities/silver-futures-decline-1479-to-231-lakhkg-as-geopolitical-risks-lift-inflation-outlook/article70833851.ece) | thehindubusinessline.com | 8 | negative |
| 7 Apr 2026 | [XAG/USD trades almost flat above $72 as Trump’s Iran deadline is in focus](https://bitcoinethereumnews.com/finance/xag-usd-trades-almost-flat-above-72-as-trumps-iran-deadline-is-in-focus/) | bitcoinethereumnews.com | 8 | negative |
| 7 Apr 2026 | [Gold Rates & Silver Rates Big Update: Will Gold & Silver Prices Rise Or Crash After RBI's Rate Decision ?](https://www.goodreturns.in/news/gold-rates-in-india-silver-rates-will-gold-silver-prices-rise-or-crash-after-rbis-repo-rate-decision-1500741.html) | goodreturns.in | 8 | negative |
| 1 Apr 2026 | [XAG/USD holds losses near $74.00 on Middle East peace hopes](https://bitcoinethereumnews.com/finance/xag-usd-holds-losses-near-74-00-on-middle-east-peace-hopes/) | bitcoinethereumnews.com | 8 | negative |
| 26 Mar 2026 | [Silber: Ausverkauf wegen Zinsangst](https://www.boerse-express.com/news/articles/silber-ausverkauf-wegen-zinsangst-883861) | boerse-express.com | 8 | negative |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "silver price" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "silver price" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "silver price" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "silver price" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "silver price", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "silver price", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Federal Reserve News Today](federal-reserve-news-today.md)
- [Mortgage Rates News](mortgage-rates-news.md)
- [Dow Jones News Today](dow-jones-news-today.md)
- [Interest Rates News](interest-rates-news.md)
