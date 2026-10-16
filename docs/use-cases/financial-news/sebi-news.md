# SEBI News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “sebi news” · 9,900/month India · 110/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [sebi-news.json](../../examples/use-cases/sebi-news.json).

**Question.** How much news did sebi receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 4,807 |
| Negative · neutral · positive | 23% · 5.4% · 72% |
| Critical (priority 7–9) | 70% (3,380 articles) |
| Busiest month, May 2025 – Apr 2026 | Sep 2025 (1,723 articles) |
| Negative-to-positive vs all news | 0.43× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 310 | 71% | 75 | 221 | ████ |
| Sep 2025 | 1,723 | 78% | 566 | 1,104 | ████████████████████ |
| Oct 2025 | 973 | 75% | 248 | 703 | ███████████ |
| Nov 2025 | 1,022 | 78% | 324 | 679 | ████████████ |
| Dec 2025 | 1,203 | 77% | 300 | 860 | ██████████████ |
| Jan 2026 | 954 | 74% | 202 | 701 | ███████████ |
| Feb 2026 | 1,163 | 63% | 212 | 864 | █████████████ |
| Mar 2026 | 1,482 | 72% | 396 | 1,006 | █████████████████ |
| Apr 2026 | 1,208 | 72% | 286 | 874 | ██████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 14 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 30 Apr 2026 | [NCLT to hear class action suit against Jindal Poly on May 7](https://www.financialexpress.com/business/news/nclt-to-hear-class-action-suit-against-jindal-poly-on-may-7/4223512/) ⚠ | financialexpress.com | 8 | negative |
| 30 Apr 2026 | [Amazon Now’s India orders growing 25% every month: CEO Andy Jassy \| Company Business News](https://www.livemint.com/companies/news/amazon-now-amazon-prime-india-ceo-andy-jassy-quick-commerce-11777531511884.html) ⚠ | livemint.com | 8 | positive |
| 30 Apr 2026 | [Sebi nod to change in RBL Bank control \| Mint Bangalore - newspaper - Lee esta historia en Magzter.com](https://www.magzter.com/es/stories/newspaper/Mint-Bangalore/SEBI-NOD-TO-CHANGE-IN-RBL-BANK-CONTROL) | magzter.com | 8 | negative |
| 28 Apr 2026 | [Punjab & Sind Bank plans ₹3,000-cr share sale this fiscal](https://www.thehindubusinessline.com/money-and-banking/punjab-sind-bank-plans-3000-cr-share-sale-this-fiscal/article70916322.ece) | thehindubusinessline.com | 8 | positive |
| 28 Apr 2026 | [IPO Launches Slow Amid Geopolitical Uncertainty; 222 Companies Wait in Pipeline - Outlook Money](https://www.outlookmoney.com/invest/ipo-launches-slow-amid-geopolitical-uncertainty-222-companies-wait-in-pipeline) ⚠ | outlookmoney.com | 8 | positive |
| 28 Apr 2026 | [Temasek, Canadian pension fund among investors looking to sell stakes in India’s NSE IPO: sources](https://www.businesstimes.com.sg/companies-markets/temasek-canadian-pension-fund-among-investors-looking-sell-stakes-indias-nse-ipo-sources) ⚠ | businesstimes.com.sg | 8 | positive |
| 28 Apr 2026 | [SEBI bans 8 including Ashok Maheshwari in front-running case](https://www.thehindubusinessline.com/money-and-banking/sebi-bars-ashok-maheshwari-7-others-in-front-running-case/article70914985.ece) | thehindubusinessline.com | 8 | negative |
| 28 Apr 2026 | [Manappuram Finance Limited Discloses SEBI Warning Against CMD in Personal Capacity](https://studycafe.in/manappuram-finance-limited-discloses-sebi-warning-against-cmd-in-personal-capacity-418379.html) | studycafe.in | 8 | negative |
| 27 Apr 2026 | [NSE Sells Stake in Indian Gas Exchange (IGX)](https://money.rediff.com/news/market/nse-sells-stake-in-indian-gas-exchange-igx/46009220260427) ⚠ | money.rediff.com | 8 | positive |
| 27 Apr 2026 | [Support measures to offset the impact of the Iran war? Here’s what FM Sitharaman said - BusinessToday](https://www.businesstoday.in/latest/economy/story/support-measures-to-offset-the-impact-of-the-iran-war-heres-what-fm-sitharaman-said-527542-2026-04-27) ⚠ | businesstoday.in | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q SEBI --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q SEBI --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q SEBI --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q SEBI --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "SEBI", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "SEBI", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [UPI News](upi-news.md)
- [Budget News](budget-news.md)
- [Income Tax News](income-tax-news.md)
- [Sensex News](sensex-news.md)
