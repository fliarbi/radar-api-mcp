# Venture Capital Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “venture capital companies in india” · 3,600/month India · 260/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [venture-capital-companies-in-india.json](../../examples/use-cases/venture-capital-companies-in-india.json).

**Question.** Which Venture Capital companies are based in India, how large and how old are they, and who competes in the Venture Capital market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Venture Capital & Private Equity” |
| Companies returned (India, first page) | 20 |

## Venture Capital companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Mensa Brands (mensabrands.com) | Bengaluru | 2021 | 201-500 | Online platform acquiring e-commerce brands and businesses |
| BizdateUp (bizdateup.com) | Mumbai | 2020 | — | Angel Investment platform which connects investors to curated startup investment opportunities |
| Venture Intelligence (ventureintelligence.com) | Chennai | 2002 | 11-50 | Database of private market datasets |
| Brick Eagle (brickeagle.com) | Mumbai | 2011 | 1-10 | Real estate capital investment company focused on affordable housing projects |
| SanchiConnect (sanchiconnect.com) | Mumbai | 2022 | — | Network of resources enabling deep technology startup growth and investment |
| Bitkemy Technologies (bitkemy.com) | Hyderabad | 2012 | 11-50 | Incubators and VC firm tech based investing primarily in India |
| IvyCamp (ivycamp.in) | Mumbai | 2014 | 11-50 | Platform to network with entrepreneurs, mentors, incubators, and investors |
| PedalStart (pedalstart.com) | Gurugram | 2022 | 11-50 | Network of mentors and investors providing startup accelerator program |
| AdvantEdge (advantedge.vc) | Delhi | 2015 | — | Tech focused early stage incubator & VC firm investing primarily in India |
| CIBA (ciba.org.in) | Salcete | 2012 | — | Business accelerator and incubator backed by Nstedb Division Department of Science and Technology |
| GoMassive (gomassive.in) | Noida | 2017 | — | Startup incubator focusing on environmental sector |
| Hyderabad Angels (hyderabadangels.in) | Hyderabad | 2010 | — | Network of investors providing capital to early and growth-stage companies |
| Indiaco (indiaco.com) | Pune | 1983 | 11-50 | Private equity & venture capital firm |
| Nativelead (nativelead.org) | Madurai | 2012 | 11-50 | Online fundraising platform for location-based native users and entrepreneurs |
| Stirring Minds (stirringminds.com) | Delhi | 2013 | 11-50 | Provider of managed co-working spaces, and mentorship services |
| Lemon Ideas (lemonideas.in) | Nagpur | 2013 | 11-50 | Startup incubator |
| PedalStart (pedalinvest.com) | Gurugram | 2021 | — | Online founder community-driven fundraising platform for early-stage companies |
| Airavat Capital (airavatcap.com) | Bengaluru | 2016 | — | Private equity investment firm |
| Bestvantage Investments (bestvantageinvestments.com) | Mumbai | 2019 | — | Connects startups with investors and mentors |
| BlackHorse Capital (blackhorsecapital.co) | Jaipur | 2019 | — | Provider of investment banking advisory services for capital and corporate structure |

## Competitive set: “venture capital” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Venture Capital & Private Equity" --filters.locations India --limit 20
radar find-competitors --market "venture capital" --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Venture Capital & Private Equity"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "venture capital", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [App Development Companies in India](app-development-companies-in-india.md)
- [Fintech Companies in India](fintech-companies-in-india.md)
- [Logistics Companies in India](logistics-companies-in-india.md)
- [Construction Companies in India](construction-companies-in-india.md)
