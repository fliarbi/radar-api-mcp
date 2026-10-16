# Furniture Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “furniture companies in india” · 880/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [furniture-companies-in-india.json](../../examples/use-cases/furniture-companies-in-india.json).

**Question.** Which Furniture companies are based in India, how large and how old are they, and who competes in the Furniture market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Lifestyle” |
| Companies returned (India, first page) | 20 |

## Furniture companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Baby Destination (babydestination.com) | Delhi | 2017 | 1-10 | Provider of a community platform with content and support for mothers |
| AFK Gaming (afkgaming.com) | Noida | 2012 | 11-50 | Online platform offering esports news |
| IncNut Digital (incnut.com) | Hyderabad | 2011 | 51-200 | Online platform offering content related to beauty and wellness |
| Kidsstoppress (kidsstoppress.com) | Mumbai | 2012 | 11-50 | Parenting content platform |
| MissMalini (missmalini.com) | Mumbai | 2008 | 11-50 | Online platform publishing content focusing on lifestyle and entertainment |
| POPxo (popxo.com) | Gurugram | 2013 | 51-200 | Provides content platform for lifestyle/fashion, beauty, and health topics |
| Sepalika (sepalika.com) | Mumbai | 2016 | 1-10 | Healthcare content platform offering research based content |
| Beingtheparent (beingtheparent.com) | Bengaluru | 2013 | 1-10 | Platform for parenting needs |
| Cinestaan (cinestaan.com) | Mumbai | 2013 | 1-10 | Entertainment-focused digital media platform |
| Glamrs (glamrs.com) | Mumbai | 2012 | 11-50 | Online platform providing news on women lifestyle |
| IWMBuzz (iwmbuzz.com) | Mumbai | 2017 | 11-50 | App-based media portal focused on entertainment news |
| MensXP (mensxp.com) | Gurugram | 2007 | 11-50 | Online destination providing lifestyle content for men, covering fashion and wellness |
| Peepul Tree (peepultree.world) | Bengaluru | 2020 | 11-50 | Online platform offering handcrafted products from local artisans |
| CafeMarathi (cafemarathi.com) | Mumbai | 2016 | 1-10 | Online platform providing news on films and TV |
| Medindia (medindia.net) | Chennai | 1995 | 1-10 | Digital platform providing information focused on health |
| Momspresso (momspresso.com) | Gurugram | 2010 | 51-200 | Information portal for parents |
| Bitoodle (bitoodlebooks.com) | Noida | 2017 | 51-200 | E-commerce platform for school supplies |
| E-Reasoning (ereasoning.com) | Hyderabad | 2019 | 1-10 | Online news portal focused on gambling |
| ParentCircle (parentcircle.com) | Chennai | 2010 | 11-50 | Digital content sharing platform for parents and a magazine in print. |
| Pink Villa (pinkvilla.com) | Mumbai | 2007 | 51-200 | Entertainment content publishing on digital platform. |

## Competitive set: “furniture” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Lifestyle --filters.locations India --limit 20
radar find-competitors --market furniture --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Lifestyle"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "furniture", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Market Research Companies in India](market-research-companies-in-india.md)
- [Cloud Companies in India](cloud-companies-in-india.md)
- [Retail Companies in India](retail-companies-in-india.md)
- [SAAS Companies in India](saas-companies-in-india.md)
