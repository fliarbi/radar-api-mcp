# Chemical Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “chemical companies in india” · 1,000/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [chemical-companies-in-india.json](../../examples/use-cases/chemical-companies-in-india.json).

**Question.** Which Chemical companies are based in India, how large and how old are they, and who competes in the Chemical market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Chemicals” |
| Companies returned (India, first page) | 20 |

## Chemical companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| GSP Crop Science (gspcrop.in) | Ahmedabad | 1985 | 501-1000 | Manufactures fertilizers, insecticides, fungicides, herbicides. |
| Laxmi (laxmi.com) | Mumbai | 1992 | 501-1000 | Manufacturer of diversified chemicals |
| Privi (privi.com) | Mumbai | 1992 | 501-1000 | Manufacturer of aroma and fragrance chemicals |
| Best Value Chem (bestvaluechem.com) | Vadodara | 1996 | 201-500 | Manufacturer of flavors and fragrances ingredients |
| Crystal Crop Protection (crystalcropprotection.com) | Delhi | 1994 | 1001-5000 | Manufacturer of agrochemicals for crop protection |
| Himadri Chemicals and Industries (himadri.com) | Kolkata | 1987 | 501-1000 | Manufactures coal tar and basic industrial chemicals. |
| Inventys (inventys.in) | Mumbai | 2005 | 51-200 | Custom based manufacturer of actives, crop protection, advanced intermediates, and specialty… |
| VVF (vvfltd.com) | Mumbai | 2010 | 501-1000 | Manufactures consumer goods and processed food products |
| Keva (keva.co.in) | Mumbai | 1922 | 501-1000 | Manufacturer of flavours and fragrances |
| Aarti Industries (aarti-industries.com) | Mumbai | 1984 | 5001-10000 | Manufacturer of specialty chemicals, pharmaceutical products, and surfactants |
| Aether (aether.co.in) | Surat | 2013 | 501-1000 | Manufacturer of advanced intermediates and active ingredients for multiple industries |
| Ascent Finechem (ascentfinechem.com) | Ahmedabad | 2004 | 51-200 | Manufacturer of specialty and fine chemicals for various industrial applications |
| Calibre Chemicals (calibrechem.com) | Mumbai | 1984 | 51-200 | Manufacturer of iodine, selenium, cobalt and peroxygens |
| Carbanio (carbanio.com) | Hyderabad | 2015 | 11-50 | Provider of a marketplace for chemicals |
| Cilicant (cilicant.com) | Pune | 2011 | 51-200 | Manufacturer and supplier of drugs for biopharma sector |
| Dhanuka Agritech (dhanuka.com) | Gurugram | 1980 | 1001-5000 | Leading Indian agrochemical company empowering agriculture with innovative crop protection solutions |
| Elchemy (elchemy.com) | Mumbai | 2021 | 11-50 | Provider of chemical distribution, custom manufacturing, and regulatory compliance services |
| Elkay Chemicals (elkaysilicones.com) | Pune | 1990 | 51-200 | Manufactures silicone products and emulsions. |
| Eternis (eternis.com) | Mumbai | 1988 | 501-1000 | Manufacturer of aroma chemicals and esters |
| Malladi (malladi.com) | Chennai | 1980 | 501-1000 | Manufacturer of chiral building blocks and specialty chemicals |

## Competitive set: “chemical” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Chemicals --filters.locations India --limit 20
radar find-competitors --market chemical --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Chemicals"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "chemical", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Textile Companies in India](textile-companies-in-india.md)
- [Waste Management Companies in India](waste-management-companies-in-india.md)
- [Market Research Companies in India](market-research-companies-in-india.md)
- [Cloud Companies in India](cloud-companies-in-india.md)
