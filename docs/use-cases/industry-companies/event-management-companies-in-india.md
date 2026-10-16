# Event Management Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “event management companies in india” · 720/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [event-management-companies-in-india.json](../../examples/use-cases/event-management-companies-in-india.json).

**Question.** Which Event Management companies are based in India, how large and how old are they, and who competes in the Event Management market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Events” |
| Companies returned (India, first page) | 20 |

## Event Management companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Fusion Foods (fusionfoods.co) | Chennai | 2008 | 1001-5000 | Provider of event catering services |
| Microchip Payments (microchippayments.com) | Hubli | 2017 | 1-10 | Digital payment solutions for diversified event businesses |
| Foodlink (foodlink.in) | Mumbai | 2003 | 501-1000 | Provider of comprehensive catering solutions for diverse events and needs |
| Atomx (atomx.in) | Pune | 2012 | — | Electronic wallet harnessing NFC technology |
| Rozzana (rozzana.com) | Kolkata | 2012 | 1-10 | Offers event catering services |
| WarpBay (warpbay.com) | Pune | 2020 | — | Cloud-based event management software provider |
| ZillOut (zillout.com) | Bengaluru | 2021 | — | App-based discovery platform providing reviews for bars |
| Create (create.wtf) | Mumbai | 2022 | — | Provider of influencer marketing services |
| Rekard (rekard.com) | Bengaluru | 2015 | — | Live streaming services provider |
| SS Hyderabad Biryani (sshyderabadbiryani.com) | Chennai | 1998 | — | Operator of restaurants |
| WedAdvisor (wed-advisor.com) | Delhi | 2020 | 1-10 | Online marketplace for wedding vendor services |
| EventCo (eventco.live) | Kozhikode | 2019 | — | Cloud based event management application provider |
| Goa Sunsplash (goasunsplash.com) | Pernem | 2015 | — | Platform that hosts and organizes music festivals |
| Laasye (laasye.com) | Noida | 2018 | — | Online shopping platform offering a wide range of handcrafted home decor products |
| LeChaat Factory (lechaatfactory.co.in) | Delhi | 2015 | — | Provider of food catering service |
| BlueDove (bluedove.co.in) | Bengaluru | 2023 | — | Chains providing catering and hospitality services |
| Codgrey (codgrey.com) | Bengaluru | 2017 | — | Provides software solutions for events and activations |
| Foodlink Catering (foodlinkcatering.co) | Delhi | 2003 | — | Provider of catering services |
| Indigo Catering & Services (indigoservices.co.in) | Ranchi | 2008 | 11-50 | Provider of catering services |
| Little Food Co (littlefoodco.com) | Mumbai | 2010 | — | Provider of bespoke catering, delivered party food, and kids' menu services |

## Competitive set: “event management” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Events --filters.locations India --limit 20
radar find-competitors --market "event management" --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Events"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "event management", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [SAAS Companies in India](saas-companies-in-india.md)
- [Fashion Companies in India](fashion-companies-in-india.md)
- [Water Companies in India](water-companies-in-india.md)
- [Bpo Companies in India](bpo-companies-in-india.md)
