# Waste Management Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “waste management companies in india” · 1,000/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [waste-management-companies-in-india.json](../../examples/use-cases/waste-management-companies-in-india.json).

**Question.** Which Waste Management companies are based in India, how large and how old are they, and who competes in the Waste Management market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Waste Management” |
| Companies returned (India, first page) | 20 |

## Waste Management companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| EcoCentric Management (ecocentric.co.in) | Mumbai | 2012 | 11-50 | Provider of electronic waste recycling services |
| Ganesha Ecosphere (ganeshaecosphere.com) | Kanpur | 1987 | 201-500 | Provider of plastic waste recycling services |
| Rubamin (rubamin.com) | Vadodara | 1981 | 501-1000 | Provider of recycling solutions for industrial waste and end-of-life products |
| Bintix (bintix.com) | Hyderabad | 2005 | 1-10 | Platform utilizing technology to collect, tag, and analyze household dry waste for recycling… |
| Citizengage (citizengage.co) | Bengaluru | 2015 | 1-10 | IoT-based software platform for waste producers & service providers |
| Century Metal Recycling (cmr.co.in) | Faridabad | 2006 | 1001-5000 | Producer of secondary aluminum and zinc alloys |
| Daily Dump (dailydump.org) | Bengaluru | 2006 | 11-50 | Provider of composting products and services intended to decentralize waste management |
| Hasiru Dala Innovations (hasirudalainnovations.com) | Bengaluru | 2015 | 51-200 | Provider of waste management and circular economy services |
| KAM-AVIDA (kamavida.com) | Pune | 1994 | 51-200 | Manufacturer of waste handling equipment |
| Solwearth Ecotech (solwearth.com) | Kochi | 2014 | 11-50 | Provider of food waste recycling machines |
| The Kabadiwala (thekabadiwala.com) | Bhopal | 2013 | 11-50 | Digital platform offering door to door scrap collection and recycling services |
| Zigma (zigma.in) | Erode | 2006 | 1001-5000 | Provider of smart cleaning equipments |
| Antony Waste Handling (antony-waste.com) | Mumbai | 2001 | 201-500 | Provider of waste processing, treatment, and collection services |
| Elrhino Eco Industries (elrhinopaper.com) | Guwahati | 2014 | 1-10 | Provider of organic waste recycling services to produce paper |
| Greenscape (greenscape-eco.com) | Delhi | 2007 | 51-200 | Provider of recycling electronic waste services and end-of-life IT products |
| Pashupati Group (pashupatigrp.com) | Kashipur | 2008 | 11-50 | Provider of waste plastic recycling and environmental services |
| Polygenta (polygenta.com) | Nashik | 1981 | 201-500 | Provider of chemical recycling of PET bottles to produce yarns and chips |
| Sampurn(e)arth (sampurnearth.com) | Mumbai | 2012 | 11-50 | Provider of garbage processing, recycling, and other waste managemment services |
| Tara Machines (taramachines.com) | Delhi | 2008 | 1-10 | Provider of waste treatment technology based services |
| Binbag (binbag.in) | Bengaluru | 2014 | 1-10 | Online portal for e-waste collection |

## Competitive set: “waste management” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Waste Management" --filters.locations India --limit 20
radar find-competitors --market "waste management" --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Waste Management"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "waste management", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Food Companies in India](food-companies-in-india.md)
- [Textile Companies in India](textile-companies-in-india.md)
- [Chemical Companies in India](chemical-companies-in-india.md)
- [Market Research Companies in India](market-research-companies-in-india.md)
