# Market Research Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “market research companies in india” · 880/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [market-research-companies-in-india.json](../../examples/use-cases/market-research-companies-in-india.json).

**Question.** Which Market Research companies are based in India, how large and how old are they, and who competes in the Market Research market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Market Research” |
| Companies returned (India, first page) | 20 |

## Market Research companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| MarketsandMarkets (marketsandmarkets.com) | Pune | 2009 | 501-1000 | Provider of market research reports and business research insights services |
| redquanta (redquanta.com) | Mumbai | 2010 | 1-10 | Retailers of consumer products |
| Thelightbulb (thelightbulb.ai) | Mumbai | 2021 | 11-50 | Provider of AI tools for market research and consumer insights |
| DelveInsight (delveinsight.com) | Delhi | 2014 | 51-200 | Market research firm focused on life sciences |
| Grand View Research (grandviewresearch.com) | Pune | 2014 | 201-500 | Market research reports and insights provider |
| Tijori (tijorifinance.com) | Bengaluru | 2016 | 11-50 | Provider of investment tracking and research tools for equities |
| Unomer (unomer.com) | Bengaluru | 2015 | 11-50 | Provider of digital consumer insights and market research platform |
| A for Analytics (aforanalytic.com) | Chennai | 2002 | 11-50 | Provider of BI services |
| Azure Knowledge (azureknowledge.com) | Ahmedabad | 2013 | 1001-5000 | Provider of IT suite solutions, Data collection and management, and other services |
| Cybex (cybex.in) | Noida | 2006 | 51-200 | Provider of import–export trade intelligence and global customs data |
| Entropik (entropik.io) | Bengaluru | 2016 | 51-200 | AI powered consumer behavior analysis platform |
| Intech Space (intechspace.com) | Ahmedabad | 2016 | 11-50 | Provider of B2B data intelligence, sales consulting, and CRM administration services. It offers… |
| Ken Research (kenresearch.com) | Gurgaon/gurugram | 2007 | 1-10 | Provider of market research and business intelligence & operational consulting services |
| Stratview Research (stratviewresearch.com) | Raipur | 2015 | 51-200 | Business market research reports and insights |
| AIOCD Pharmasofttech AWACS (aiocdawacs.com) | Chennai | 2007 | 1-10 | Provider of pharma product services |
| Borderless Access (borderlessaccess.com) | Bengaluru | 2008 | 201-500 | Provider of analytics-drive project for management suite |
| Databridge (databridgemarketresearch.com) | Pune | 2014 | 51-200 | Provider of market research and procurement consulting services for multiple industries |
| Fortune Business Insights (fortunebusinessinsights.com) | Pune | 2019 | 51-200 | Provider of market research reports |
| InsightsIO (insightsio.com) | Bengaluru | 2015 | 1-10 | Customer insights and business analytics solutions for enterprises |
| Markelytics (markelytics.com) | Bengaluru | 2003 | 51-200 | Provider of BPO services for market research |

## Competitive set: “market research” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Market Research" --filters.locations India --limit 20
radar find-competitors --market "market research" --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Market Research"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "market research", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Waste Management Companies in India](waste-management-companies-in-india.md)
- [Chemical Companies in India](chemical-companies-in-india.md)
- [Cloud Companies in India](cloud-companies-in-india.md)
- [Furniture Companies in India](furniture-companies-in-india.md)
