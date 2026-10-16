# Retirement News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “retirement news” · 260/month India · 1,300/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [retirement-news.json](../../examples/use-cases/retirement-news.json).

**Question.** How much news did retirement receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 44,217 |
| Negative · neutral · positive | 36% · 5.3% · 59% |
| Critical (priority 7–9) | 39% (17,327 articles) |
| Busiest month, May 2025 – Apr 2026 | Apr 2026 (14,072 articles) |
| Negative-to-positive vs all news | 0.83× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 2,916 | 34% | 924 | 1,827 | ████ |
| Sep 2025 | 9,617 | 33% | 3,074 | 6,132 | ██████████████ |
| Oct 2025 | 7,630 | 40% | 2,717 | 4,411 | ███████████ |
| Nov 2025 | 7,531 | 38% | 2,587 | 4,484 | ███████████ |
| Dec 2025 | 9,068 | 33% | 2,921 | 5,627 | █████████████ |
| Jan 2026 | 8,312 | 37% | 2,745 | 5,141 | ████████████ |
| Feb 2026 | 10,844 | 39% | 3,831 | 6,449 | ███████████████ |
| Mar 2026 | 10,989 | 41% | 4,043 | 6,302 | ████████████████ |
| Apr 2026 | 14,072 | 39% | 5,192 | 8,034 | ████████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 13 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 10 Jan 2026 | [Elderly Couple Duped Into ‘Helping’ Investigation in $1.3 Million Bitcoin ATM Scam](https://www.benzinga.com/crypto/cryptocurrency/26/01/49830695/elderly-couple-duped-into-helping-investigation-in-1-3-million-bitcoin-atm-scam) | benzinga.com | 9 | negative |
| 30 Apr 2026 | [It's official: Some lower-income workers can get $1,000 in matching retirement savings from Uncle Sam](https://www.businessinsider.com/trump-retirement-plans-401k-ira-work-full-time-2026-4) | businessinsider.com | 8 | positive |
| 30 Apr 2026 | [Trump Signs Executive Order Launching IRA Web Site \| PLANSPONSOR](https://www.plansponsor.com/trump-signs-executive-order-launching-ira-web-site/) | plansponsor.com | 8 | positive |
| 30 Apr 2026 | [Trump signs executive order expanding retirement benefits](https://thehill.com/homenews/administration/5857949-trump-executive-order-retirement-benefits/) | thehill.com | 8 | positive |
| 30 Apr 2026 | [Trump to sign order aimed at retirement plan access ahead of $1,000 federal match](https://thehill.com/homenews/5857607-trump-to-sign-order-aimed-at-retirement-plan-access-ahead-of-1000-federal-match/) | thehill.com | 8 | negative |
| 30 Apr 2026 | [Trump order aims to help more people get retirement savings plans in time for new federal match](https://www.sandiegouniontribune.com/2026/04/30/trump-retirement-accounts/) | sandiegouniontribune.com | 8 | positive |
| 30 Apr 2026 | [Trump To Sign Order To Expand Access To Retirement Plans](https://www.fa-mag.com/news/trump-to-sign-order-to-expand-access-to-retirement-plans-86824.html) | fa-mag.com | 8 | positive |
| 29 Apr 2026 | [‘Pretty grim’: Super crisis for 750k Aussies](https://www.dailytelegraph.com.au/business/australias-retirement-system-not-fit-for-purpose-for-renters-facing-housing-crisis/news-story/8347b49a10d10fffe932400394b88ca4) | dailytelegraph.com.au | 8 | negative |
| 29 Apr 2026 | [Startup Founder Says Rs. 40 Crore Needed for Retirement in India, Sparks Debate](https://www.newsmobile.in/business/startup-founder-says-rs-40-crore-needed-for-retirement-in-india-sparks-debate/) | newsmobile.in | 8 | negative |
| 29 Apr 2026 | [The Pensions Schemes Bill has completed its journey through Parliament following a compromise being reached…](https://www.financialplanningtoday.co.uk/news/pensions-schemes-bill-passes-following-mandate-compromise) ⚠ | financialplanningtoday.co.uk | 8 | positive |
| 29 Apr 2026 | [Your clients’ retirement portfolios took a hit as global slump impacts institutional returns](https://www.investmentnews.com/retirement-planning/your-clients-retirement-portfolios-took-a-hit-as-global-slump-impacts-intuitional-returns/266356) | investmentnews.com | 8 | negative |
| 28 Apr 2026 | [Protesters halt NatWest shareholder meeting as boss defends climate policy](https://www.irishnews.com/news/uk/protesters-halt-natwest-shareholder-meeting-as-boss-defends-climate-policy-XEH6XQYZ6RIJDC26G652YWAA2A/) ⚠ | irishnews.com | 8 | negative |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q retirement --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q retirement --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q retirement --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q retirement --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "retirement", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "retirement", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Dividend News](dividend-news.md)
- [Unemployment News](unemployment-news.md)
- [Treasury Yields News](treasury-yields-news.md)
- [Yen News](yen-news.md)
