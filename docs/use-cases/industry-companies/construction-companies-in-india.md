# Construction Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “construction companies in india” · 2,900/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [construction-companies-in-india.json](../../examples/use-cases/construction-companies-in-india.json).

**Question.** Which Construction companies are based in India, how large and how old are they, and who competes in the Construction market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Construction” |
| Companies returned (India, first page) | 20 |

## Construction companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Infra.Market (infra.market) | Thane | 2016 | 1001-5000 | Provider of diverse building and construction materials for project lifecycles |
| Ace Cranes (ace-cranes.com) | Delhi | 1995 | 1001-5000 | Manufacturer of construction equipment |
| Modulus Housing (modulushousing.com) | Chennai | 2015 | 51-200 | Manufacturer of modular, portable, and reusable infrastructure for various sectors |
| Mtandt (mtandt.com) | Chennai | 2000 | 501-1000 | Aerial Work Platforms & Equipment Rentals \| Buy or Rent |
| Shankara (shankarabuildpro.com) | Bengaluru | 1995 | 501-1000 | Supplier of construction materials, tiles, and wooden flooring products |
| AJAX (ajax-engg.com) | Bengaluru | 1992 | 501-1000 | Manufacturer of concrete production, transport, placement, and paving equipment |
| Apl Apollo Tubes (aplapollo.com) | Noida | 1986 | 1001-5000 | Online platform for manufacturing structural steel tubes, pipes, and related steel solutions |
| BuildNext (buildnext.in) | Ernakulam | 2015 | 51-200 | Tech-enabled construction company building customized homes |
| Capacite Infraproject (capacite.in) | Mumbai | 2012 | 501-1000 | Provider of engineering, procurement, and construction services for building projects |
| Cyber City (cybercity.in) | Hyderabad | 2008 | 51-200 | Provider of residential & commercial real estate development services |
| DB Realty (dbrealty.co.in) | Mumbai | 2007 | 1-10 | Developer of residential, commercial, and gated community real estate projects |
| Dynacon Projects (dynaconprojects.com) | Noida | 1986 | 51-200 | Provider of civil construction and industrial infrastructure development services |
| Gayatri Projects (gayatri.co.in) | Hyderabad | 1989 | 1001-5000 | Provider of construction and infratructure services |
| GPT Infraprojects (gptgroup.co.in) | Kolkata | 1980 | 1001-5000 | Chains providing multispecialty tertiary healthcare, infrastructure construction, and railway… |
| GreenJams (greenjams.org) | Visakhapatnam | 2019 | 11-50 | Manufacturer of carbon-negative building materials |
| G R Infraprojects (grinfra.com) | Udaipur | 1995 | 10000+ | EPC provider for infrastructure projects and manufacturer of related materials |
| HUVIAiR (huviair.com) | Bengaluru | 2016 | 1-10 | Platform offering construction monitoring solutions |
| Karda Construction (kardaconstruction.com) | Nashik | 1994 | 11-50 | Developer of real estate & infrastructure projects |
| MBL (mblinfra.com) | Delhi | 1995 | 201-500 | Provider of engineering services |
| Power Mech Projects (powermechprojects.com) | Hyderabad | 1999 | 10000+ | Provider of engineering and power generation infrastructure construction services |

## Competitive set: “construction” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Construction --filters.locations India --limit 20
radar find-competitors --market construction --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Construction"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "construction", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Venture Capital Companies in India](venture-capital-companies-in-india.md)
- [Logistics Companies in India](logistics-companies-in-india.md)
- [Toy Companies in India](toy-companies-in-india.md)
- [Aerospace Companies in India](aerospace-companies-in-india.md)
