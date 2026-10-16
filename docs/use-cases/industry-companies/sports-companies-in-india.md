# Sports Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “sports companies in india” · 260/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [sports-companies-in-india.json](../../examples/use-cases/sports-companies-in-india.json).

**Question.** Which Sports companies are based in India, how large and how old are they, and who competes in the Sports market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Sports” |
| Companies returned (India, first page) | 20 |

## Sports companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| GreedyGame Media (greedygame.com) | Bengaluru | 2013 | 11-50 | Provider of all in one solutions for all app growth and app monetization requirement |
| Nazara (nazara.com) | Mumbai | 1999 | 51-200 | Provider of diversified gaming and sports media platform |
| SportzVillage (sportzvillage.com) | Bengaluru | 2003 | 51-200 | Provider of sports and physical education for schools |
| Aquasail (aquasailindia.com) | Mumbai | 2006 | 11-50 | Provider of ship designing and engineering services |
| JetSynthesys (jetsynthesys.com) | Pune | 2010 | 51-200 | Provider of digital entertainment experiences across gaming, esports, music, and sports |
| Sporjo (sporjo.com) | Mumbai | 2020 | 1-10 | Provider of recruitment services |
| Dream11 (dream11.com) | Mumbai | 2008 | 1001-5000 | Online sports fantasy platform that allows users to create virtual teams of real players |
| Eventjini (eventjini.com) | Chennai | 2011 | 11-50 | Event listing, promotion and ticketing platform |
| Fantasy Akhada (fantasyakhada.com) | Gurugram | 2020 | 51-200 | App based fantasy sports platform for multi sports |
| Gamerji (gamerji.com) | Ahmedabad | 2019 | 11-50 | Real money based gaming platform |
| HitWicket (hitwicket.com) | Hyderabad | 2012 | 51-200 | Online platform offering mobile-based cricket strategy game and simulation experience |
| Hudle (hudle.in) | Delhi | 2019 | 51-200 | Provider of platform connecting sports enthusiasts with venues and community |
| Kabaddi Adda (kabaddiadda.com) | Bengaluru | 2019 | 11-50 | Provider of an online platform offering news on kabaddi |
| Khel Now (khelnow.com) | Delhi | 2014 | 11-50 | Online platform offering news related to sports |
| MPL (mpl.live) | Bengaluru | 2018 | 201-500 | Operator of an online platform providing real money skill-based gaming |
| Nautilus Mobile (nautilusmobile.com) | Hyderabad | 2013 | 11-50 | Developer of mobile-based sports games |
| Procam International (procam.in) | Mumbai | 1988 | 51-200 | Provider of sports event management and development services |
| SportHood (sporthood.in) | Bengaluru | 2013 | 11-50 | Provider of an online platform for booking courts and coaching classes |
| sportscafe.in (sportscafe.in) | Bengaluru | 2015 | 11-50 | Online platform providing sports news |
| Sports Flashes (sportsflashes.com) | Mumbai | 2016 | 51-200 | Online sports content platform |

## Competitive set: “sports” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Sports --filters.locations India --limit 20
radar find-competitors --market sports --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Sports"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "sports", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Quantum Computing Companies in India](quantum-computing-companies-in-india.md)
- [Hotel Companies in India](hotel-companies-in-india.md)
- [Microfinance Companies in India](microfinance-companies-in-india.md)
- [Media Companies in India](media-companies-in-india.md)
