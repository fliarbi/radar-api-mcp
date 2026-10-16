# Electronics Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “electronics companies in india” · 1,900/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [electronics-companies-in-india.json](../../examples/use-cases/electronics-companies-in-india.json).

**Question.** Which Electronics companies are based in India, how large and how old are they, and who competes in the Electronics market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Electronics” |
| Companies returned (India, first page) | 20 |

## Electronics companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Amber Enterprises India (ambergroupindia.com) | Gurugram | 1990 | 201-500 | Original equipment manufacturer for white goods companies |
| Dixon Technologies (dixoninfo.com) | Noida | 1993 | 1001-5000 | Provider of electronics manufacturing services |
| Sastra Robotics (sastrarobotics.com) | Ernakulam | 2013 | 11-50 | Manufacturer of consumer and industrial use robots |
| Elecbits (elecbits.in) | Delhi | 2019 | 11-50 | Provider of electronics supply chain, engineering, and manufacturing solutions |
| Epack Durable (epackdurable.com) | Noida | 2003 | 501-1000 | Online platform for OEM/ODM manufacturing of air‑conditioning and home appliances |
| GabbarDeals (gabbardeals.com) | Pune | 2000 | 11-50 | E-commerce platform offering electronic products and accessories |
| Oakter (oakter.com) | Noida | 2015 | 51-200 | Provider of electronic contract manufacturing and designing services |
| PickMe eSolutions India (pickmeindia.com) | Mumbai | 2011 | 1-10 | Service provider for retailers |
| PROFX (profx.com) | Bengaluru | 2000 | 51-200 | Retail chain of speakers, AV receivers, amplifiers, soundbars and headphones |
| Brandworks Technologies (bwtech.in) | Palghar | 2017 | 51-200 | Provider of electronics manufacturing services |
| Mekr Technologies (mekr.in) | Sonipat | 2022 | 1-10 | Manufacturer of kitchen appliances |
| Pai International (paiinternational.in) | Bengaluru | 2000 | 1001-5000 | Retail-chain of consumer electronics and appliances |
| Horivacao (horivacao.com) | Margao | 2015 | 1-10 | Contract manufacturer of lighting & decorative products |
| Sargam India Electronics (sargam.in) | Delhi | 1994 | 51-200 | Retail chain offering consumer electronics products |
| CastNX (castnx.com) | Indore | 2020 | 11-50 | Power electronics manufacturer specializing in design, development, and manufacturing of power… |
| Maven Silicon (maven-silicon.com) | Bengaluru | 2009 | 51-200 | Provider of online VLSI training |
| SATHYA (sathya.in) | Thoothukudi | 1978 | 1001-5000 | Online retailer offering multi-category consumer electronic products |
| Unicorn (unicornstore.in) | Mumbai | 2002 | 501-1000 | Retail chain of electronic products |
| Poojara Telecom (poojaratele.com) | Rajkot | 1994 | 51-200 | Online retail platform offering smart electronics gadgets and accessories |
| Sangeetha Mobiles (sangeethamobiles.com) | Bengaluru | 1974 | 51-200 | Online platform offering mobile devices, electronics, and accessories for purchase and exchange |

## Competitive set: “electronics” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Electronics --filters.locations India --limit 20
radar find-competitors --market electronics --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Electronics"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "electronics", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Telecom Companies in India](telecom-companies-in-india.md)
- [Gaming Companies in India](gaming-companies-in-india.md)
- [Advertising Companies in India](advertising-companies-in-india.md)
- [Cybersecurity Companies in India](cybersecurity-companies-in-india.md)
