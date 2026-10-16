# Toy Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “toy companies in india” · 2,900/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [toy-companies-in-india.json](../../examples/use-cases/toy-companies-in-india.json).

**Question.** Which Toy companies are based in India, how large and how old are they, and who competes in the Toy market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Toys and Games” |
| Companies returned (India, first page) | 20 |

## Toy companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Terra (letsterra.com) | Bengaluru | 2023 | 51-200 | Online gaming, socializing and learning metaverse based platform for kids |
| Rainmaker (rainmaker.win) | Mumbai | 2021 | — | App-based stocks and cryptocurrency gaming platform |
| Toyflix (toyflix.in) | Bengaluru | 2022 | — | Platform for toy access and play subscriptions |
| ilearnngrow (ilearnngrow.com) | Indore | 2020 | — | Internet first brand offering toys for kids |
| Neosphere Interactive (neosphereinteractive.com) | Mumbai | 2016 | — | Developer of video games |
| Candid Creeda (candidcreeda.com) | Bengaluru | 2021 | — | Internet first brand offering language learning activity boxes for kids |
| ITOYS (itoys.co.in) | Sonipat | 2012 | 501-1000 | Manufacturer of kids toys |
| KALAKARAM (kalakaram.com) | Gurugram | 2022 | — | Provider of DIY kits for all ages |
| Rawky Studios (rawky-studios.com) | Mumbai | 2018 | — | Developer and publisher of mobile and PC-based AR games |
| The Talking Canvas (thetalkingcanvas.com) | Bengaluru | 2018 | — | Internet-first brand of kids apparel |
| GamingAkhada (gamingakhada.com) | Kanpur | 2019 | — | Real money based gaming platform |
| Sellet (sellet.in) | — | 2021 | — | Contract based manufacturer of toys |
| DIOSC Gaming (dioscgaming.com) | Silchar | 2020 | — | Game development company |
| ToyMahal (toymahal.in) | Ahmedabad | 2014 | — | Subscription-based platform to rent toys |
| Bumpy Rides (bumpyrides.in) | Coimbatore | 2019 | — | Online shopping platform offering multi-category toys for babies |
| Gaming Gone Epic (gamingonepic.com) | Delhi | 2020 | — | Online platform offering esports tournaments |
| Gurucool Fun (gurucool.fun) | Chennai | 2021 | — | Operator of k-12 schools |
| StockTry (stocktry.com) | Ahmedabad | 2020 | — | Game based stock trading platform |
| Toycel (toycel.com) | Bengaluru | 2019 | — | Online retailer offering toys for kids |
| Uptot (uptot.in) | Mumbai | 2021 | — | Online marketplace for multi-category second-hand products |

## Competitive set: “toy” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Toys and Games" --filters.locations India --limit 20
radar find-competitors --market toy --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Toys and Games"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "toy", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Logistics Companies in India](logistics-companies-in-india.md)
- [Construction Companies in India](construction-companies-in-india.md)
- [Aerospace Companies in India](aerospace-companies-in-india.md)
- [Web Development Companies in India](web-development-companies-in-india.md)
