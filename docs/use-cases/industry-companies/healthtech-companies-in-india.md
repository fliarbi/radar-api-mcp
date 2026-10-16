# Healthtech Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “healthtech companies in india” · 320/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [healthtech-companies-in-india.json](../../examples/use-cases/healthtech-companies-in-india.json).

**Question.** Which Healthtech companies are based in India, how large and how old are they, and who competes in the Healthtech market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Healthcare & Lifesciences” |
| Companies returned (India, first page) | 20 |

## Healthtech companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| FyndHealth (fyndhealth.com) | Bengaluru | 2020 | 1-10 | Provider of children's healthcare and parenting needs |
| LEVEL (level.game) | Mumbai | 2021 | 11-50 | Developer of a mobile app called level supermind for meditation and anxiety relief |
| OrangeCross (orangecross.in) | Bhubaneswar | 2017 | 51-200 | Provider of home care nursing services |
| Aqmen Medtech (aqmen.co.in) | Bengaluru | 2018 | 51-200 | R&D company focused on manufacturing surgical devices for multiple therapeutic areas |
| Bare Body Essentials (barebody.in) | Ahmedabad | 2017 | — | Online platform offering body waxing services and related beauty solutions for individuals |
| Care4Parents (care4parents.in) | Noida | 2015 | — | Provider of health care assistance, analysis, and solutions for health records for the elderly |
| Gyroid Photonics (gyrophint.com) | Bengaluru | 2021 | — | Photonic solutions \| Gyroid Photonics \| Bengaluru |
| Pentavalent (pentavalent.in) | Bengaluru | 2015 | — | Provider of vaccines and research services |
| Ruby's Organics (rubysorganics.in) | Mumbai | 2015 | — | Manufacturer of organic and plant-based makeup products for Indian skin |
| Sekkei Bio (sekkeibio.com) | Chennai | 2017 | — | Developer of drugs and vaccines to treat multiple diseases |
| Sensio (sensio-ai.in) | Bengaluru | 2019 | — | Wearable devices and software for vital signs monitoring |
| Wundrsight (wundrsight.com) | Bengaluru | 2022 | — | Provider of virtual reality and AI-integrated platform for mental healthcare |
| 9M India (9mindia.in) | Raipur | 2020 | — | Manufacturer of pharmaceutical formulations |
| Ace Blend (aceblend.com) | Mumbai | 2018 | — | Manufacturer of plant protein powders and functional health supplement blends |
| DeNovo (denovobioinnovations.com) | Pune | 2020 | — | Company focused on advancing surgical care through innovative medical devices |
| Docuses Healthcare (docuses.com) | Mumbai | 2020 | — | Surgical & medical disposables supplier, offering procurement solutions to healthcare providers |
| East Ocyon Bio (eastocyonbio.com) | Gurugram | 2022 | — | Developer of cell and gene therapies for the treatment of cancer |
| EasyHeals Technologies (easyheals.com) | Pune | 2021 | — | Online marketplace of healthcare service providers offering healthcare services at affordable prices |
| Icareheal (icareheal.com) | Noida | 2020 | — | Provider of practice growth and management solutions for healthcare professionals |
| MediArt Life Sciences (mediartlifesciences.com) | Delhi | 2015 | 51-200 | Manufacturer of renal and critical care medications |

## Competitive set: “healthtech” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Healthcare & Lifesciences" --filters.locations India --limit 20
radar find-competitors --market healthtech --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Healthcare & Lifesciences"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "healthtech", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Jewellery Companies in India](jewellery-companies-in-india.md)
- [IOT Companies in India](iot-companies-in-india.md)
- [Music Companies in India](music-companies-in-india.md)
- [Data Analytics Companies in India](data-analytics-companies-in-india.md)
