# Mutual Fund News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “mutual fund news” · 3,600/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [mutual-fund-news.json](../../examples/use-cases/mutual-fund-news.json).

**Question.** How much news did mutual fund receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 12,130 |
| Negative · neutral · positive | 8.8% · 2.5% · 89% |
| Critical (priority 7–9) | 14% (1,667 articles) |
| Busiest month, May 2025 – Apr 2026 | Feb 2026 (6,944 articles) |
| Negative-to-positive vs all news | 0.13× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 170 | 25% | 19 | 145 | █ |
| Sep 2025 | 2,231 | 18% | 100 | 2,111 | ██████ |
| Oct 2025 | 820 | 40% | 72 | 728 | ██ |
| Nov 2025 | 647 | 42% | 58 | 578 | ██ |
| Dec 2025 | 894 | 45% | 74 | 724 | ███ |
| Jan 2026 | 1,292 | 19% | 77 | 1,191 | ████ |
| Feb 2026 | 6,944 | 11% | 762 | 5,946 | ████████████████████ |
| Mar 2026 | 2,168 | 16% | 116 | 2,026 | ██████ |
| Apr 2026 | 1,726 | 18% | 108 | 1,580 | █████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 16 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 22 Apr 2026 | [Indian investors are buying the dip and doing it smarter than ever: Sandipan Roy](https://economictimes.indiatimes.com/markets/expert-view/indian-investors-are-buying-the-dip-and-doing-it-smarter-than-ever-sandipan-roy/articleshow/130438738.cms) | economictimes.indiatimes.com | 8 | positive |
| 22 Apr 2026 | [Why smallcap funds are still a buy: A long-term strategy from Aditya Khemani - The Economic Times](https://economictimes.indiatimes.com/markets/expert-view/why-smallcap-funds-are-still-a-buy-a-long-term-strategy-from-aditya-khemani/printarticle/130416796.cms) | economictimes.indiatimes.com | 8 | positive |
| 21 Apr 2026 | [India's Nuclear Energy Push: Report Highlights Path to 100 GW](https://www.newkerala.com/news/a/indias-nuclear-push-needs-parallel-power-play-hit-451.htm) | newkerala.com | 8 | positive |
| 21 Apr 2026 | [FIIs dump $19 billion, But retail keeps buying-can retail SIPs hold the line? Kotak explains](https://www.financialexpress.com/market/fiis-dump-19-billion-but-retail-keeps-buying-can-retail-sips-hold-the-line-kotak-explains-4213668/) ⚠ | financialexpress.com | 8 | negative |
| 21 Apr 2026 | [The Gold Edge: ETF net inflows up 4.5x in FY26](https://economictimes.indiatimes.com/mf/mf-news/the-gold-edge-etf-net-inflows-up-4-5x-in-fy26/articleshow/130404928.cms) | economictimes.indiatimes.com | 8 | positive |
| 19 Apr 2026 | [Defence stocks: What MFs bought and sold at peak of US Iran war - BusinessToday](https://www.businesstoday.in/markets/stocks/story/defence-stocks-what-mfs-bought-and-sold-at-peak-of-us-iran-war-526188-2026-04-19) | businesstoday.in | 8 | positive |
| 16 Apr 2026 | [Daily Indian Funding Roundup & Key News - 16 April 2026: The Hosteller Bags ₹150 Cr Series B, Snabbit…](https://www.startuptalky.com/news/daily-indian-funding-roundup-key-news-16-april-2026/) | startuptalky.com | 8 | positive |
| 16 Apr 2026 | [Equity mutual funds’ average AUM rises 17% in FY26; flexi cap funds lead growth: Abakkus MF - CNBC TV18](https://www.cnbctv18.com/personal-finance/equity-mutual-funds-aum-17-pc-up-fy26-flexi-cap-funds-lead-abakkus-mf-ws-el-19887930.htm) | cnbctv18.com | 8 | positive |
| 16 Apr 2026 | [Why Aditya Birla Sun Life MF's Balasubramanian sees a 10-year bull market beyond the dip \| Mint](https://www.livemint.com/money/why-aditya-birla-sun-life-mfs-balasubramanian-sees-10-year-bull-market-beyond-dip-11776315504452.html) | livemint.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "mutual fund" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "mutual fund" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "mutual fund" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "mutual fund" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "mutual fund", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "mutual fund", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Crude Oil Price News](crude-oil-price-news.md)
- [Fintech News](fintech-news.md)
- [Mergers and Acquisitions News](mergers-and-acquisitions-news.md)
- [Private Equity News](private-equity-news.md)
