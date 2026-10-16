# Data Analytics Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “data analytics companies in india” · 320/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [data-analytics-companies-in-india.json](../../examples/use-cases/data-analytics-companies-in-india.json).

**Question.** Which Data Analytics companies are based in India, how large and how old are they, and who competes in the Data Analytics market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Data Analytics” |
| Companies returned (India, first page) | 20 |

## Data Analytics companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| RecoSense (recosenselabs.com) | Bengaluru | 2014 | 11-50 | AI enabled customer data intelligence and content personalization platform for businesses |
| SetuServ (setuserv.com) | Hyderabad | 2012 | 11-50 | AI powered platform offering consumer insights |
| Staqu (staqu.com) | Gurugram | 2015 | 51-200 | Developer of video and audio analytics platform for multiple industries |
| AllGoVision (allgovision.com) | Bengaluru | 2010 | 51-200 | Provider of an AI and cloud-based video analytics platform for smart cities |
| Almug Technologies (almug.ai) | Bengaluru | 2015 | 11-50 | AI enabled data analytics & data management solutions provider |
| Awiros (awiros.com) | Gurugram | 2015 | 51-200 | Developer of computer vision software for real time video analytics |
| Capital Quant Solutions (capquant.com) | Delhi | 2015 | 1-10 | Data analytics platform for financial market |
| Cerrid Solutions (cerridsolutions.com) | Bengaluru | 2007 | 1-10 | Big data analytics platform |
| Constems-AI (constems-ai.com) | Noida | 2015 | 11-50 | Provider of computer vision powered solutions for surveillance and video analytics |
| Egnify (egnify.com) | Bengaluru | 2015 | 51-200 | Provider of ai based student performance analytics solutions |
| MarketsMojo (marketsmojo.com) | Mumbai | 2015 | 11-50 | Provider of a platform for stock and mutual fund analysis |
| Stride (stride.ai) | Bengaluru | 2015 | 11-50 | AI based platform for building intelligent automation workflows |
| Trendlyne (trendlyne.com) | Bengaluru | 2014 | 11-50 | Data analytics platform for stock investments |
| Zeliot (zeliot.in) | Bengaluru | 2018 | 51-200 | Developer of a platform for building and managing real-time data pipelines |
| Agrex.ai (agrexai.com) | Gurugram | 2016 | 1-10 | AI-based video analytics platform for offline retailers |
| Byteprophecy.com (byteprophecy.com) | Ahmedabad | 2011 | 11-50 | AI powered decision support and analytics platform |
| Ignitarium (ignitarium.com) | Bengaluru | 2012 | 501-1000 | Provider of AI-powered semiconductor and embedded system design platform |
| Infilect (infilect.com) | Bengaluru | 2018 | 51-200 | Provider of image recognition and AI-powered analytics for retail execution |
| Pattern Effects Labs (patterneffects.com) | Bengaluru | 2017 | 11-50 | Provider of AI and IT solutions for government and enterprises |
| Report Bee (reportbee.com) | Chennai | 2010 | 11-50 | Educational data recording and analytics |

## Competitive set: “data analytics” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Data Analytics" --filters.locations India --limit 20
radar find-competitors --market "data analytics" --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Data Analytics"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "data analytics", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Healthtech Companies in India](healthtech-companies-in-india.md)
- [Music Companies in India](music-companies-in-india.md)
- [Quantum Computing Companies in India](quantum-computing-companies-in-india.md)
- [Hotel Companies in India](hotel-companies-in-india.md)
