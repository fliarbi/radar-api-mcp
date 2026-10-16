# AI Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “ai companies in india” · 8,100/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [ai-companies-in-india.json](../../examples/use-cases/ai-companies-in-india.json).

**Question.** Which AI companies are based in India, how large and how old are they, and who competes in the AI market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “AI” |
| Companies returned (India, first page) | 20 |

## AI companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Bigthinx (bigthinx.com) | Bengaluru | 2015 | 11-50 | Platform offering AI‑driven 3D solutions for fashion and gaming |
| Orbo (orbo.ai) | Mumbai | 2016 | 11-50 | AI-powered visual intelligence solutions for the beauty and personal care sector |
| Coitor (coitor.com) | Coimbatore | 2013 | 11-50 | AR technology based virtual apparel look trials at offline retails |
| CogniQuest (cogniquest.ai) | Bengaluru | 2022 | 11-50 | Developer of AI-driven intelligent document processing and automation platform |
| ConsInt (consint.ai) | Noida | 2020 | 11-50 | Provider of AI-driven solutions for healthcare claims, fraud detection, and automation |
| Intozi (intozi.io) | Gurugram | 2019 | 11-50 | Provider of video analytics platform for safety, security and operational efficiency |
| Tryndbuy (tryndbuy.com) | Delhi | 2018 | 11-50 | Developer of an AI platform for virtual try-on and media |
| AIDoings (aidoings.ai) | Bengaluru | 2018 | 1-10 | Provider of learning resources for students with dyslexia |
| Arcturus Business Solutions (arcturusbusiness.in) | Noida | 2019 | — | Provider of AI-powered monitoring and analytics solutions for industrial safety and asset security |
| Dailyhunt (dailyhunt.in) | Bengaluru | 2009 | 201-500 | Provider of personalized news content aggregated in multiple Indian languages |
| Fabulyst (fabulyst.com) | Bengaluru | 2016 | — | AI-enabled personal stylist tool for online retailers |
| JustAct (justact.co.in) | Chennai | 2019 | — | AI powered dispute resolution platform |
| augurai (theaugurai.com) | Tiruchirappalli | 2022 | 11-50 | Provider of AI and SaaS-based automated machine vision systems |
| uniQin.ai (uniqin.ai) | Bengaluru | 2021 | — | SaaS-based platform offering pricing solution for small to large-sized enterprises |
| Epitome (epitome.ai) | Bengaluru | 2020 | — | Provider of a unified platform for student, recruiter, and training institution interactions |
| Medvolt (medvolt.ai) | Pune | 2021 | — | Developer of an AI platform for drug discovery and repurposing |
| Optimum Data Analytics (optimumdataanalytics.com) | Pune | 2017 | 11-50 | Tech company providing AI solutions |
| bhk.ai (bhk.ai) | Bengaluru | 2022 | — | Provider of a web-enabled real estate listing analytics solutions |
| Consuma (consuma.ai) | Bengaluru | 2021 | — | AI-powered market research and intelligence platform |
| Loomiz (loomiz.in) | Gurugram | 2024 | — | Provider of apparel manufacturing platform with design and supply chain tools |

## Competitive set: “ai” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries AI --filters.locations India --limit 20
radar find-competitors --market ai --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["AI"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "ai", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Automotive Companies in India](automotive-companies-in-india.md)
- [Digital Marketing Companies in India](digital-marketing-companies-in-india.md)
- [Pharmaceutical Companies in India](pharmaceutical-companies-in-india.md)
