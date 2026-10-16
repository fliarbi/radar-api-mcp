# Food Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “food companies in india” · 1,300/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [food-companies-in-india.json](../../examples/use-cases/food-companies-in-india.json).

**Question.** Which Food companies are based in India, how large and how old are they, and who competes in the Food market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Food & Beverages” |
| Companies returned (India, first page) | 20 |

## Food companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Allied Blenders and Distillers (abdindia.com) | Mumbai | 1986 | 501-1000 | Manufacturer of alcoholic beverages |
| Aibono (aibono.com) | Bengaluru | 2014 | 51-200 | Provider of AI-powered fresh food aggregator platform |
| Blue Tokai Coffee Roasters (bluetokaicoffee.com) | Gurugram | 2013 | 1001-5000 | Retailer of freshly roasted coffee beans |
| Crofarm (crofarm.com) | Gurugram | 2016 | 201-500 | B2B supply chain for fresh farm produce |
| FreshMenu (freshmenu.com) | Bengaluru | 2014 | 501-1000 | Online platform offering on-demand meals |
| Hangyo (hangyo.in) | Mangaluru | 2002 | 501-1000 | Brand of ice creams |
| Open Secret (opensecret.in) | Mumbai | 2019 | 51-200 | Retailer of healthy snacks and food products |
| Suminter (suminterindiaorganics.com) | Mumbai | 2004 | 201-500 | Provider of certified organic and natural food, fibers, and materials |
| 99 Pancakes (99pancakes.in) | Mumbai | 2017 | 51-200 | Chains providing pancakes, waffles, cakes, crepes, pastries, and related desserts |
| Aadvik Foods (aadvikfoods.com) | Delhi | 2015 | 11-50 | Online brand offering camel, goat and donkey milk products |
| Adinath Agro (adinathagro.com) | Pune | 1995 | 201-500 | Manufacturing of food pulp, ketchup, jam, pickles in India |
| Bikaji (bikaji.com) | Bikaner | 1987 | 1001-5000 | Brand of extruded snacks |
| Bonhomia (bonhomiaworld.com) | Bengaluru | 2013 | 11-50 | Internet-first brand offering coffee products |
| Captain Fresh (captainfresh.in) | Bengaluru | 2019 | 201-500 | Digital first seafood supply chain platform |
| Coolberg (coolberg.in) | Mumbai | 2016 | 51-200 | Private label brand of non-alcoholic beer |
| Delight Foods (delightfoods.com) | Bengaluru | 2015 | 1-10 | Online delivery of selected branded food across India |
| FarMart (farmart.co) | Gurugram | 2015 | 201-500 | Provider of digital infrastructure, market linkages, and financial capital for food enterprises |
| Foodcloud (foodcloud.in) | Delhi | 2013 | 11-50 | Online marketplace for home-cooked food |
| Food Memories (foodmemories.com) | Ahmedabad | 2016 | 51-200 | Online platform for ordering food products |
| The Global Green Company (globalgreengroup.com) | Bengaluru | 1992 | 501-1000 | Producer of processed fruits and vegetables |

## Competitive set: “food” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Food & Beverages" --filters.locations India --limit 20
radar find-competitors --market food --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Food & Beverages"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "food", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Robotics Companies in India](robotics-companies-in-india.md)
- [Biotech Companies in India](biotech-companies-in-india.md)
- [Textile Companies in India](textile-companies-in-india.md)
- [Waste Management Companies in India](waste-management-companies-in-india.md)
