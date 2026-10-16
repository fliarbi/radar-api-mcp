# Aerospace Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “aerospace companies in india” · 2,400/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [aerospace-companies-in-india.json](../../examples/use-cases/aerospace-companies-in-india.json).

**Question.** Which Aerospace companies are based in India, how large and how old are they, and who competes in the Aerospace market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Aeronautics Aerospace & Defence” |
| Companies returned (India, first page) | 20 |

## Aerospace companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| SpaceFields (spacefields.in) | Bengaluru | 2021 | 11-50 | Developer of custom solid propulsion systems for aerospace and defense |
| EtherealX (etherealx.space) | Bengaluru | 2022 | 11-50 | Developer of reusable medium-lift launch vehicles and related propulsion systems |
| Zepco Technologies (zepcotek.com) | Bengaluru | 2022 | 11-50 | Platform offering power electronics products |
| Vyomik Drones (vyomikdrones.com) | Hyderabad | 2020 | — | Manufacturer of unmanned aerial vehicles and provider of related services |
| ZMotion Autonomous Systems (zmotion.in) | Bengaluru | 2018 | 51-200 | Manufacturer of drones and accessories for defense applications |
| Aerosys Aviation (aerosysaviation.com) | Noida | 2020 | — | Provider of DGCA-certified drone solutions for surveying, mapping, and surveillance |
| Astromeda (astromeda.in) | Bengaluru | 2018 | — | Developer of wearable e-fabric health monitors and real-time health monitoring |
| AVision Systems (avisionsystems.com) | Hyderabad | 2020 | 51-200 | Manufacturer of loitering munition systems for precision military strike operations |
| AxialAero (axial.aero) | Hyderabad | 2020 | — | Developer of flight simulator technology and aeronautical, aerospace products and services |
| DefSpace (defspace.com) | Mumbai | 2020 | — | Platform offering a one-stop digital marketplace for defence, space, and aerospace sectors |
| Smart-Waves (smart-waves.com) | Hyderabad | 2016 | — | Manufacturer of electronic hardware and provider of product engineering services |
| Tunga Aerospace Industries (tungasystems.com) | Chennai | 2020 | — | Manufacturer of unmanned aerial vehicles for defense, commercial, and environmental use |
| CHIRAG Technologies (chiragtechnologies.com) | Noida | 2022 | — | Provider of drone design and agricultural technology solutions |
| Hyoristic (hyoristic.com) | Chennai | 2017 | — | Company provides solutions for space debris detection |
| Misochain (misochain.in) | Bengaluru | 2019 | — | Design and build indigenous, flight‑critical aircraft components for the defence and civil… |
| Octaflyte (octaflyte.com) | Udhampur | 2020 | — | Developer of software products for geographic information system data handling |
| Drone Destination (thedronedestination.com) | Delhi | 2019 | 51-200 | Provider of drone-as-a-service solutions |
| Thermovac Aerospace (thermovacaerospace.com) | Bengaluru | 2016 | 51-200 | Developer and manufacturer of thermal solutions for the aerospace industry |
| Vikra Ocean Tech (vikraoceantech.com) | Chennai | 2018 | — | Developer of autonomous underwater vehicles and marine technology solutions |
| Vyomastra Technologies (vyomastra.in) | Bengaluru | 2020 | — | Developer of drone technology for surveying and inspection |

## Competitive set: “aerospace” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Aeronautics Aerospace & Defence" --filters.locations India --limit 20
radar find-competitors --market aerospace --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Aeronautics Aerospace & Defence"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "aerospace", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Construction Companies in India](construction-companies-in-india.md)
- [Toy Companies in India](toy-companies-in-india.md)
- [Web Development Companies in India](web-development-companies-in-india.md)
- [Legal Companies in India](legal-companies-in-india.md)
