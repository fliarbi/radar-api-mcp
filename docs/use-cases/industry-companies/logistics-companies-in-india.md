# Logistics Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “logistics companies in india” · 3,600/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [logistics-companies-in-india.json](../../examples/use-cases/logistics-companies-in-india.json).

**Question.** Which Logistics companies are based in India, how large and how old are they, and who competes in the Logistics market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Logistics” |
| Companies returned (India, first page) | 20 |

## Logistics companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| LogiNext (loginextsolutions.com) | Mumbai | 2014 | 1-10 | Cloud based end-to-end transportation management software |
| Mahindra Logistics (mahindralogistics.com) | Mumbai | 2009 | 1001-5000 | Provider of integrated supply chain and mobility solutions |
| ElasticRun (elastic.run) | Pune | 2014 | 1001-5000 | Platform offering rural B2B E-commerce and logistics |
| Peel-Works (peel-works.com) | Mumbai | 2010 | 501-1000 | Provider of CRM software for grocery retailers |
| Prozo (prozo.com) | Gurugram | 2014 | 201-500 | Online platform offering wholesale and business-focused e-commerce solutions |
| Ripplr (ripplr.in) | Bengaluru | 2019 | 201-500 | Provider of distribution and logistics services for multiple industry verticals |
| ShopKirana (shopkirana.com) | Indore | 2015 | 501-1000 | Provider of B2B procurement platform for grocery retailers |
| WhistleDrive (whistledrive.com) | Hyderabad | 2016 | 51-200 | Online platform offering transportation and fleet management services |
| 72 Networks (72networks.com) | Gurugram | 2014 | 11-50 | Provider of web-based last-mile logistics services |
| Accio Robotics (acciorobotics.com) | Bengaluru | 2019 | 11-50 | Developer of warehouse automation robots focused on order picking processes |
| AgriGator (agrigator.co) | Bhopal | 2019 | 11-50 | Digital platform offering logistics and transportation management solutions for the agricultural… |
| ClickPost (clickpost.ai) | Bengaluru | 2015 | 51-200 | Provider of post-purchase platform for ecommerce, including shipping, tracking, returns |
| Creando (creando.in) | Delhi | 2014 | 11-50 | Retailer of FMCG products and brand & e-commerce management services |
| Exprs (exprs.com) | Hyderabad | 2018 | 1-10 | Last-mile delivery solutions for e-commerce brands and communities |
| Hachidori Robotics (hachidorirobotics.com) | Bengaluru | 2019 | 51-200 | Manufacturer of autonomous mobile robots for material movement in industries |
| Redwing (redwinglabs.in) | Bengaluru | 2018 | 11-50 | Developer of autonomous drones for logistics and delivery services |
| Skye Air (skyeair.tech) | Gurugram | 2019 | 51-200 | Platform offers drone‑based last‑mile delivery services |
| Stackbox (stackbox.xyz) | Bengaluru | 2016 | 51-200 | Provider of cloud-based supply chain automation solutions |
| Techeagle (techeagle.in) | Gurugram | 2015 | 51-200 | Developer of autonomous drone infrastructure for logistics, public safety, and defence |
| ThinkLink (thinklink-scs.com) | Gurugram | 2006 | 1-10 | Provider of warehouse automation solutions |

## Competitive set: “logistics” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Logistics --filters.locations India --limit 20
radar find-competitors --market logistics --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Logistics"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "logistics", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Fintech Companies in India](fintech-companies-in-india.md)
- [Venture Capital Companies in India](venture-capital-companies-in-india.md)
- [Construction Companies in India](construction-companies-in-india.md)
- [Toy Companies in India](toy-companies-in-india.md)
