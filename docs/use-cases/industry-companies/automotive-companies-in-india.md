# Automotive Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “automotive companies in india” · 14,800/month India · 480/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [automotive-companies-in-india.json](../../examples/use-cases/automotive-companies-in-india.json).

**Question.** Which Automotive companies are based in India, how large and how old are they, and who competes in the Automotive market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Automotive” |
| Companies returned (India, first page) | 20 |

## Automotive companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Uniparts India (unipartsgroup.com) | Noida | 1984 | 1001-5000 | Manufacturer of engineered systems and components for off-highway vehicles |
| CarTrade (cartrade.com) | Navi Mumbai | 2006 | 1001-5000 | App-based used cars listing platform |
| CarWale (carwale.com) | Mumbai | 2003 | 501-1000 | Online listing platforms that facilitate the sale of second-hand cars |
| CredR (credr.com) | Bengaluru | 2015 | 51-200 | Online marketplace for second-hand bikes |
| CarIQ (mycariq.com) | Pune | 2013 | 501-1000 | Saas-based platform for vehicle diagnostics solutions |
| Ola Electric (olaelectric.com) | Bengaluru | 2017 | 1001-5000 | Manufacturer of electric scooters, motorcycles, and energy storage solutions |
| Pureev.in (pureev.in) | — | 2019 | 51-200 | Manufacturer of energy storage products and electric vehicles with lithium batteries |
| Sansera Engineering (sanseraindia.com) | Bengaluru | 1981 | 5001-10000 | Manufacturer of vehicles, engines, bodies, and components for the automotive sector |
| SEDEMAC (sedemac.com) | Mumbai | 2007 | 201-500 | Manufacturer of motor vehicle parts |
| SparesHub (spareshub.com) | Pune | 2013 | 11-50 | Retailer of automotive service and replacement parts via online platform |
| Advanced Structures (advancedstructures.in) | Bengaluru | 2014 | 51-200 | Manufacturer and supplier of auto components |
| Altigreen (altigreen.com) | Bengaluru | 2013 | 201-500 | Manufacturer of electric three-wheel vehicles for cargo and passenger transport |
| Ather Energy (atherenergy.com) | Bengaluru | 2013 | 1001-5000 | Manufacturer of electric scooters, charging infrastructure, smart helmets, and accessories |
| AutoNxt Automation (autonxt.in) | Thane | 2016 | 11-50 | Manufacturer of electric tractors for agriculture, industry, and defense applications |
| Battery Smart (batterysmart.in) | Delhi | 2019 | 201-500 | Platform offering operator of battery-swapping network for electric vehicles and related services |
| Belrise Industries (belriseindustries.com) | Pune | 1988 | 1001-5000 | Manufacturer of components for automotive and white goods industries |
| BlueBinaries (bluebinaries.com) | Chennai | 2017 | 201-500 | Provider of engineering solutions for software-driven vehicles and E/E architecture |
| CarDekho (cardekho.com) | Jaipur | 2008 | 1001-5000 | App based platform offering car buying, selling, and comparison services |
| Cars24 (cars24.com) | Gurugram | 2015 | 1001-5000 | Retailer of used vehicles, new vehicle information, loans, and related services |
| Demyto.com (demyto.com) | Pune | 2014 | 11-50 | Online garage aggregator for automotive repair & maintenance services |

## Competitive set: “automotive” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Automotive --filters.locations India --limit 20
radar find-competitors --market automotive --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Automotive"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "automotive", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [AI Companies in India](ai-companies-in-india.md)
- [Digital Marketing Companies in India](digital-marketing-companies-in-india.md)
