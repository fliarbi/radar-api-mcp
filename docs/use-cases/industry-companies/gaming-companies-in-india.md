# Gaming Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “gaming companies in india” · 1,900/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [gaming-companies-in-india.json](../../examples/use-cases/gaming-companies-in-india.json).

**Question.** Which Gaming companies are based in India, how large and how old are they, and who competes in the Gaming market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Gaming” |
| Companies returned (India, first page) | 20 |

## Gaming companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| GreedyGame Media (greedygame.com) | Bengaluru | 2013 | 11-50 | Provider of all in one solutions for all app growth and app monetization requirement |
| Games2win Media (games2winmedia.com) | Mumbai | 2005 | 51-200 | Developer of mobile-based multi-genre games |
| Moonfrog Labs (moonfroglabs.com) | Bengaluru | 2013 | 51-200 | Mobile game development studio |
| Nazara (nazara.com) | Mumbai | 1999 | 51-200 | Provider of diversified gaming and sports media platform |
| 99Games (99games.in) | Udupi | 2008 | 51-200 | Developer of mobile games with focus on cooking and restaurant themes |
| Ability Games (abilitygames.in) | Kolkata | 2011 | 11-50 | Casino-based gaming platform for browser devices |
| AFK Gaming (afkgaming.com) | Noida | 2012 | 11-50 | Online platform offering esports news |
| Games24x7 (games24x7.com) | Mumbai | 2006 | 501-1000 | Operator of a platform providing Rummy, Fantasy Sports, and Ludo |
| Gamezop (gamezop.com) | Gurugram | 2015 | 51-200 | Operator of a platform providing instant-play games across multiple categories |
| Hike (hike.in) | Delhi | 2012 | 201-500 | Provider of blockchain based mobile gaming platform |
| JetSynthesys (jetsynthesys.com) | Pune | 2010 | 51-200 | Provider of digital entertainment experiences across gaming, esports, music, and sports |
| Junglee Games (jungleegames.com) | Delhi | 2010 | 501-1000 | Developer of online skill-based games across multiple platforms and genres |
| NODWIN Gaming (nodwingaming.com) | Gurugram | 2015 | 51-200 | Provider of gaming, esports, and youth entertainment intellectual properties and services |
| Tamasha (tamasha.live) | Bengaluru | 2020 | 11-50 | Developer of social applications facilitating interactive contests, audio experiences, and… |
| WinZO (winzogames.com) | Delhi | 2018 | 51-200 | Digital platform offering a wide range of online games with monetization options and social features |
| Baazi Games (baazigames.com) | Delhi | 2014 | 51-200 | Operator of online poker and sports prediction gaming solutions |
| Brandscale Innovations (business-standard.com) | Mumbai | 2021 | 51-200 | Manufacturer of gaming accessories |
| Creative Monkey Games (creativemonkeygames.com) | Coimbatore | 2014 | 11-50 | Mobile game developer and publisher |
| GameEon (gameeon.in) | Mumbai | 2013 | 1-10 | Developer of mobile games and provider of game development services |
| Gamerji (gamerji.com) | Ahmedabad | 2019 | 11-50 | Real money based gaming platform |

## Competitive set: “gaming” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Gaming --filters.locations India --limit 20
radar find-competitors --market gaming --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Gaming"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "gaming", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Consulting Companies in India](consulting-companies-in-india.md)
- [Telecom Companies in India](telecom-companies-in-india.md)
- [Electronics Companies in India](electronics-companies-in-india.md)
- [Advertising Companies in India](advertising-companies-in-india.md)
