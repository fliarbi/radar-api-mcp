# Interest Rates News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “interest rates news” · 260/month India · 12,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [interest-rates-news.json](../../examples/use-cases/interest-rates-news.json).

**Question.** How much news did interest rates receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 26,322 |
| Negative · neutral · positive | 55% · 6.3% · 39% |
| Critical (priority 7–9) | 61% (16,114 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (8,147 articles) |
| Negative-to-positive vs all news | 1.94× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 1,881 | 69% | 1,136 | 681 | █████ |
| Sep 2025 | 7,737 | 67% | 4,187 | 3,133 | ███████████████████ |
| Oct 2025 | 4,899 | 65% | 2,521 | 2,173 | ████████████ |
| Nov 2025 | 4,991 | 62% | 2,653 | 2,127 | ████████████ |
| Dec 2025 | 7,257 | 58% | 3,360 | 3,367 | ██████████████████ |
| Jan 2026 | 5,749 | 67% | 2,971 | 2,449 | ██████████████ |
| Feb 2026 | 5,676 | 58% | 2,849 | 2,491 | ██████████████ |
| Mar 2026 | 6,750 | 62% | 4,206 | 2,151 | █████████████████ |
| Apr 2026 | 8,147 | 59% | 4,492 | 3,039 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 10 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 14 Apr 2026 | [Oil surges past $100 as Trump’s Hormuz blockade raises global economic risks](https://iol.co.za/business-report/economy/2026-04-14-oil-surges-past-100-as-trumps-hormuz-blockade-raises-global-economic-risks/) ⚠ | iol.co.za | 9 | negative |
| 30 Apr 2026 | [FxWirePro: EUR/AUD dips after ECB rate decision , eyes 1.6150 level - EconoTimes](https://econotimes.com/FxWirePro-EUR-AUD-dips-after-ECB-rate-decision-eyes-16150-level-1740555) | econotimes.com | 8 | negative |
| 30 Apr 2026 | [Analyst who predicted 2021 crash says 'markets were better off with Powell'](https://finance.yahoo.com/markets/crypto/articles/analyst-predicted-2021-crash-says-234943672.html) | finance.yahoo.com | 8 | negative |
| 30 Apr 2026 | [‘Progress’: ANZ profits surge 9 per cent](https://www.goldcoastbulletin.com.au/business/work/leaders-companies/anz-halfyear-profits-surge-9-per-cent-to-365bn/news-story/79f487943b70c46a4b0b0d6e15d59338) | goldcoastbulletin.com.au | 8 | negative |
| 30 Apr 2026 | [Treasuries Draw Buyers After Selloff as Oil Surge Stalls \| Stock Market News](https://www.livemint.com/market/treasuries-draw-buyers-after-selloff-as-oil-surge-stalls-11777580292964.html) ⚠ | livemint.com | 8 | positive |
| 30 Apr 2026 | [Colombia Holds Interest Rates Steady in May and June](https://colombiaone.com/2026/04/30/colombia-holds-interest-rates-steady-in-may-and-june/) | colombiaone.com | 8 | positive |
| 30 Apr 2026 | [3 mortgage rate questions borrowers should ask after the Fed rate pause](https://cbsnews.com/news/mortgage-rate-questions-borrowers-fed-rate-pause/) ⚠ | cbsnews.com | 8 | negative |
| 30 Apr 2026 | [Stagflation Concerns and the Fed’s Growth vs Inflation Call](https://fintech.tv/stagflation-concerns-balancing-growth-and-inflation-in-todays-economy/) ⚠ | fintech.tv | 8 | negative |
| 30 Apr 2026 | [Gas prices soar to record highs amid war in Iran](https://www.yahoo.com/news/articles/arizona-gas-prices-soar-record-173013746.html) ⚠ | yahoo.com | 8 | negative |
| 30 Apr 2026 | [Treasuries draw buyers after selloff as oil surge stalls](https://asreport.americanbanker.com/articles/treasuries-draw-buyers-after-selloff-as-oil-surge-stalls) ⚠ | asreport.americanbanker.com | 8 | positive |
| 30 Apr 2026 | [World Liberty Financial (WLFI) Plunges to New ATL: Has Trump's Family Ruined Crypto?](https://cryptopotato.com/world-liberty-financial-wlfi-plunges-to-new-atl-has-trumps-family-ruined-crypto/) | cryptopotato.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "interest rates" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "interest rates" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "interest rates" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "interest rates" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "interest rates", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "interest rates", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Silver Price News](silver-price-news.md)
- [Dow Jones News Today](dow-jones-news-today.md)
- [S&P 500 News Today](s-p-500-news-today.md)
- [UPI News](upi-news.md)
