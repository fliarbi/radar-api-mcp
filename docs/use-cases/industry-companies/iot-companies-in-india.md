# IOT Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “iot companies in india” · 480/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [iot-companies-in-india.json](../../examples/use-cases/iot-companies-in-india.json).

**Question.** Which IOT companies are based in India, how large and how old are they, and who competes in the IOT market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Internet of Things” |
| Companies returned (India, first page) | 20 |

## IOT companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Atoll Solutions (atollsolutions.com) | Bengaluru | 2014 | 11-50 | Provider of real-time location intelligence platform for IoT applications |
| Pococare (pococare.com) | Bengaluru | 2021 | — | Online platform offering medical emergency services |
| Six Sense Mobility (sixsensemobility.com) | Delhi | 2020 | — | End-to-End fleet management solutions for fleet operators |
| SNAS IoT Laboratories (snasiotlab.com) | Pune | 2015 | — | Provider of IoT services |
| Viliso Technologies (viliso.in) | Mumbai | 2019 | — | IoT based environment monitoring product |
| AB Circuits and Research Labs (abcrlabs.com) | Bengaluru | 2019 | — | Developer of automotive electronics, semiconductors, and tire monitoring solutions |
| Aidio (aidio.in) | Bengaluru | 2016 | 11-50 | Provider digital signage solutions for enterprises |
| HeadFox (headfox.in) | Jaipur | 2017 | — | Smart bluetooth helmets, offering features like easy navigation and long battery life |
| Hivericks (hivericks.com) | Chennai | 2018 | — | Developer of IoT-based solutions for home automation |
| Troncart Solutions (troncartsolutions.com) | Thiruvananthapuram | 2018 | — | Develops smart metering and irrigation system |
| Xeeed IO (xeeed.io) | Hyderabad | 2021 | — | Developer of IoT-integrated asset monitoring systems |
| Deep Facts (deepfacts.io) | Hyderabad | 2020 | — | Developer of wearable device for continuous vital monitoring and predictive cardiac screening |
| Gyrfalcon IntelliEdge Solutions India (gyrfalconintelliedge.com) | Bengaluru | 2022 | — | Provider of IoT solutions for digitization, digitalization, and automation services |
| MLworkX (mlworkx.com) | Noida | 2020 | — | Provider of production process management system with machine vision capabilities for… |
| Qualivon Technologies (qualivontechnologies.com) | Bhubaneswar | 2020 | — | Developer of silicon photonics-based gas sensors for environmental and industrial monitoring |
| Tuchware (tuchware.com) | Indore | 2016 | — | Manufacturer of electronic & RFID locks |
| BOLA (trafobola.com) | Mumbai | 2021 | 201-500 | Provides IoT based solutions for remote monitoring of transformers |
| AICAN (aican.co.in) | Mumbai | 2021 | — | Provider of industrial automation and data analytics services |
| Arion Tech-Sol (ariontechsol.com) | Ahmedabad | 2016 | — | Provider of IoT-based wireless smart water management solutions |
| DyoCense (dyocense.com) | Bengaluru | 2018 | 1-10 | Provider of IoT platform and devices |

## Competitive set: “iot” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Internet of Things" --filters.locations India --limit 20
radar find-competitors --market iot --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Internet of Things"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "iot", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Bpo Companies in India](bpo-companies-in-india.md)
- [Jewellery Companies in India](jewellery-companies-in-india.md)
- [Healthtech Companies in India](healthtech-companies-in-india.md)
- [Music Companies in India](music-companies-in-india.md)
