# Music Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “music companies in india” · 390/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [music-companies-in-india.json](../../examples/use-cases/music-companies-in-india.json).

**Question.** Which Music companies are based in India, how large and how old are they, and who competes in the Music market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Music” |
| Companies returned (India, first page) | 20 |

## Music companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Jukebox Studio (thejukeboxstudio.com) | Mumbai | 2014 | 1-10 | Music jukebox application for venues |
| Artium Academy (artiumacademy.com) | Mumbai | 2021 | 51-200 | Provider of live, one-on-one online classes for music and instruments |
| Furtados School of Music (furtadosschoolofmusic.com) | Mumbai | 2011 | 51-200 | Provider of music education programs for schools and individuals |
| Muzigal (muzigal.com) | Hyderabad | 2020 | 11-50 | Online platform offering music tutoring solutions |
| Only Much Louder (oml.in) | Mumbai | 2001 | 51-200 | Provider of talent management, content creation, live events, and brand solutions |
| Riyaz (riyazapp.com) | Bengaluru | 2017 | 11-50 | App-based platform offering solutions for practising singing |
| Sensibol (sensibol.com) | Mumbai | 2011 | 11-50 | Online singing platform and technology for auditioning and personal training |
| SkillBox (skillboxes.com) | Gurugram | 2016 | 11-50 | Community platform for artists to collaborate with each other |
| Taaqademy (taaqademy.com) | Bengaluru | 2010 | 1-10 | Chain of instituions offering music courses |
| Bajaao (bajaao.com) | Mumbai | 2005 | 51-200 | Online retailer of music instruments |
| Beatoven.ai (beatoven.ai) | Bengaluru | 2021 | 11-50 | Developer of an AI platform generating royalty-free music and sound effects |
| Moojic (moojic.com) | Mumbai | 2013 | — | In-store radio service and jukebox for retail stores |
| Rhapsody (rhapsodymusic.in) | Chennai | 2013 | 51-200 | Operator of k-12 schools |
| Choira (choira.io) | Mumbai | 2021 | 1-10 | Provider of digital studio for music creation |
| Flutin (flutin.com) | Noida | 2015 | 11-50 | Peronalized playlist music streaming platform provider |
| Guitaa (guitaa.com) | Jaipur | 2018 | 1-10 | Online music learning platform |
| humit (humit.app) | Bengaluru | 2019 | 1-10 | Social platform for music discovery |
| Spardha School of Music (spardhaschoolofmusic.com) | Pune | 2016 | 51-200 | Online music and dance classes for all ages |
| allround (allroundclub.com) | Bengaluru | 2020 | 11-50 | Provider of online co-curricular learning programs for children |
| FanTiger (fantiger.com) | Noida | 2022 | 11-50 | Platform enabling users to invest in songs and trade music cards |

## Competitive set: “music” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Music --filters.locations India --limit 20
radar find-competitors --market music --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Music"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "music", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [IOT Companies in India](iot-companies-in-india.md)
- [Healthtech Companies in India](healthtech-companies-in-india.md)
- [Data Analytics Companies in India](data-analytics-companies-in-india.md)
- [Quantum Computing Companies in India](quantum-computing-companies-in-india.md)
