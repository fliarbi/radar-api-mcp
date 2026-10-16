# Repo Rate News: Radar API example with live data

[Financial news research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “repo rate news” · 2,900/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [repo-rate-news.json](../../examples/use-cases/repo-rate-news.json).

**Question.** How much news did repo rate receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?

## At a glance

| Measure | Value |
| --- | ---: |
| Matching articles, 1 Jan – 30 Apr 2026 | 904 |
| Negative · neutral · positive | 26% · 17% · 57% |
| Critical (priority 7–9) | 75% (679 articles) |
| Busiest month, May 2025 – Apr 2026 | Dec 2025 (458 articles) |
| Negative-to-positive vs all news | 0.61× |

## Twelve months of coverage

Monthly matching articles (`news_trends`, `granularity=monthly`).

| Month | Articles | Critical | Negative | Positive |  |
| --- | ---: | ---: | ---: | ---: | --- |
| Aug 2025 (partial) | 28 | 64% | 7 | 20 | █ |
| Sep 2025 | 123 | 65% | 40 | 48 | █████ |
| Oct 2025 | 227 | 70% | 47 | 149 | ██████████ |
| Nov 2025 | 96 | 76% | 48 | 29 | ████ |
| Dec 2025 | 458 | 76% | 161 | 250 | ████████████████████ |
| Jan 2026 | 97 | 78% | 37 | 54 | ████ |
| Feb 2026 | 344 | 72% | 58 | 213 | ███████████████ |
| Mar 2026 | 71 | 70% | 29 | 33 | ███ |
| Apr 2026 | 392 | 78% | 109 | 215 | █████████████████ |

## Critical headlines

Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown). 15 matching articles were temporarily unavailable from the article store at capture time.

| Date | Headline | Publisher | Priority | Tone |
| --- | --- | --- | --- | ---: |
| 23 Apr 2026 | [RBI Maintains Repo Rate at 5.25% Amid Global Economic Uncertainty](https://currentaffairs.adda247.com/rbi-maintains-repo-rate-at-5-25-amid-global-economic-uncertainty/) | currentaffairs.adda247.com | 8 | positive |
| 22 Apr 2026 | [MPC members flag supply-driven external shock for holding the repo rate](https://www.thehindubusinessline.com/money-and-banking/mpc-members-flag-supply-driven-external-shock-for-holding-the-repo-rate/article70893538.ece) | thehindubusinessline.com | 8 | positive |
| 21 Apr 2026 | [West Asia war’s second round effects the real concern, RBI in wait-and-watch mode: Governor Sanjay Malhotra](https://indianexpress.com/article/business/west-asia-wars-second-round-effects-the-real-concern-rbi-in-wait-and-watch-mode-governor-sanjay-malhotra-10647213/) ⚠ | indianexpress.com | 8 | negative |
| 20 Apr 2026 | [Top investment options in 2026: Compare FD, PPF, Mutual Funds, ELSS and gold — which asset class is right…](https://www.livemint.com/money/personal-finance/top-investment-options-in-2026-compare-fd-ppf-mutual-funds-elss-and-gold-which-asset-class-is-right-for-you-11776692753947.html) | livemint.com | 8 | negative |
| 15 Apr 2026 | [G-secs yields cross 7%: Should you invest in fixed income?](https://www.hindustantimes.com/business/gsecs-yields-cross-7-should-you-invest-in-fixed-income-101776235678209.html) | hindustantimes.com | 8 | positive |
| 13 Apr 2026 | [New Delhi [India] April 12 (ANI): Punjab National Bank Managing Director and CEO Ashok Chandra on Sunday…](https://bfsi.economictimes.indiatimes.com/news/articles/no-increase-in-interest-rates-125-bps-repo-cut-benefit-passed-to-customers-pnb-ceo/130223749) | bfsi.economictimes.indiatimes.com | 8 | positive |
| 11 Apr 2026 | [RBI rate pause signals hard trade-offs for Indian economy \| Policy Circle](https://www.policycircle.org/economy/rbi-monetary-policy-inflation-2/) | policycircle.org | 8 | positive |
| 9 Apr 2026 | [India Inc CFOs back RBI’s rate hold, flag Q1 pressure amid West Asia uncertainty](https://cfo.economictimes.indiatimes.com/news/economy/india-inc-cfos-back-rbis-rate-hold-flag-q1-pressure-amid-west-asia-uncertainty/130128077) | cfo.economictimes.indiatimes.com | 8 | positive |
| 9 Apr 2026 | [RBI Repo Rate April 2026: MPC Keeps Rate at 5.25% Amid Ceasefire - Business League](https://www.businessleague.in/rbi-repo-rate-april-2026-mpc-keeps-rate-at-5-25-amid-ceasefire/) | businessleague.in | 8 | negative |
| 9 Apr 2026 | [RBI holds the line: Stability signal amid global storm, growth engine intact](https://navjeevanexpress.com/rbi-holds-the-line-stability-signal-amid-global-storm-growth-engine-intact/) | navjeevanexpress.com | 8 | positive |

⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar news-overview --q "repo rate" --date-from 2026-01-01 --date-to 2026-04-30
radar news-trends --q "repo rate" --date-from 2025-05-01 --date-to 2026-04-30 --granularity monthly
radar news-sentiment --q "repo rate" --date-from 2026-01-01 --date-to 2026-04-30 --granularity monthly
radar search-business-news --q "repo rate" --date-from 2026-01-01 --date-to 2026-04-30 --priority-min 6 --sort priority --limit 25
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/news/overview" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"q": "repo rate", "date_from": "2026-01-01", "date_to": "2026-04-30"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/news/trends", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"q": "repo rate", "date_from": "2025-05-01", "date_to": "2026-04-30", "granularity": "monthly"}, timeout=120)
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

- [Private Equity News](private-equity-news.md)
- [Pension News](pension-news.md)
- [Commercial Real Estate News](commercial-real-estate-news.md)
- [Rupee News](rupee-news.md)
