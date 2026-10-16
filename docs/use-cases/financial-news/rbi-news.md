# RBI News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “rbi news” · 14,800/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [rbi-news.json](../../examples/use-cases/rbi-news.json).

**Question.** How much news did rbi receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 41,069 |
| Negative · neutral · positive | 33% · 3.5% · 63% |
| Critical (priority 7–9) | 50% (20,554 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (16,077 articles) |
| Negative-to-positive vs all news | 0.71× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 2,745 | 57% | 869 | 1,749 | ███ |
| Sep 2025 | 9,771 | 53% | 3,599 | 5,755 | ████████████ |
| Oct 2025 | 7,843 | 59% | 2,570 | 5,034 | ██████████ |
| Nov 2025 | 6,863 | 57% | 2,234 | 4,445 | █████████ |
| Dec 2025 | 7,522 | 63% | 2,697 | 4,578 | █████████ |
| Jan 2026 | 5,699 | 58% | 1,860 | 3,693 | ███████ |
| Feb 2026 | 9,097 | 53% | 2,163 | 6,609 | ███████████ |
| Mar 2026 | 10,196 | 49% | 3,545 | 6,268 | █████████████ |
| Apr 2026 | 16,077 | 46% | 6,019 | 9,395 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 17 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [J&K records historic Rs 5,824 Cr investments in FY 25-26 - Northlines](https://thenorthlines.com/jk-records-historic-rs-5824-cr-investments-in-fy-25-26/) ⚠ | thenorthlines.com | 8 | positive |
| 30 Apr 2026 | [Gold loans surge five time in two years](https://economictimes.indiatimes.com/industry/cons-products/fashion-/-cosmetics-/-jewellery/gold-loans-surge-five-time-in-two-years/articleshow/130643260.cms) ⚠ | economictimes.indiatimes.com | 8 | positive |
| 30 Apr 2026 | [Triple holiday on 1 May 2026: What is open and what is closed in India](https://english.mathrubhumi.com/news/india/may-1-2026-holiday-india-status-feodtxmf) ⚠ | english.mathrubhumi.com | 8 | negative |
| 30 Apr 2026 | [UPSC Key: Internationalisation of the Rupee, Panchayat Advancement Index and E-PRAAPTI](https://indianexpress.com/article/upsc-current-affairs/upsc-key-internationalisation-of-the-rupee-panchayat-advancement-index-and-e-praapti-10664476/) ⚠ | indianexpress.com | 8 | positive |
| 30 Apr 2026 | [Centre reviews Hyderabad Police’s Operation Octopus, pushes anti-fraud AI tool](https://www.siasat.com/centre-reviews-hyderabad-polices-operation-octopus-pushes-anti-fraud-ai-tool-3462916/) | siasat.com | 8 | positive |
| 30 Apr 2026 | [Asia Intelligence Brief for Thursday, April 30, 2026](https://www.riotimesonline.com/asia-pulse-brent-samsung-boj-india-april-30-2026/) ⚠ | riotimesonline.com | 8 | negative |
| 30 Apr 2026 | [India imports 37 lakh tonne urea amid West Asia Crisis: Domestic output stable as Kharif stock at 50%](https://www.financialexpress.com/business/news-india-imports-37-lakh-tonne-urea-amid-west-asia-crisis-domestic-production-at-37-49-lakh-tonne-4223348/) ⚠ | financialexpress.com | 8 | negative |
| 30 Apr 2026 | [Rupee Sinks to Record Low 95.23: Oil Price Spike and Fed Stance Crush INR - Business League](https://www.businessleague.in/rupee-sinks-to-record-low-95-23-oil-price-spike-and-fed-stance-crush-inr/) ⚠ | businessleague.in | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q RBI --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q RBI --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q RBI --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q RBI --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "RBI", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "RBI", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Housing Market News](housing-market-news.md)
- [IPO News](ipo-news.md)
- [Nifty News](nifty-news.md)
- [Federal Reserve News Today](federal-reserve-news-today.md)
