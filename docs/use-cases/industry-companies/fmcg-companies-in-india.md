# FMCG Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “fmcg companies in india” · 5,400/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [fmcg-companies-in-india.json](../../examples/use-cases/fmcg-companies-in-india.json).

**Question.** Which FMCG companies are based in India, how large and how old are they, and who competes in the FMCG market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “FMCG” |
| Companies returned (India, first page) | 20 |

## FMCG companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Sara Suole (saragroup.in) | Bengaluru | 2001 | 11-50 | Brand of shoes and leather products |
| VVF (vvfltd.com) | Mumbai | 2010 | 501-1000 | Manufactures consumer goods and processed food products |
| Indfrag Biosciences (indfragbiosciences.com) | Bengaluru | 1989 | 51-200 | Manufacturer of botanical extracts and flavor ingredients for beauty and food |
| JHS Svendgaard Laboratories (svendgaard.com) | Delhi | 1997 | 51-200 | Manufacturer of oral care and FMCG products offering contract manufacturing |
| Primacy Industries (primacyind.com) | Mangaluru | 2005 | 501-1000 | Contract manufacturer of scented candles, air & personal care, and hygiene products |
| Galaxy Surfactants (galaxysurfactants.com) | Mumbai | 1980 | 1001-5000 | Manufacturer of surfactants and specialty care ingredients for the home and personal care industry |
| HFL (hindustanfoodslimited.com) | Mumbai | 1984 | 501-1000 | Manufacturer of convenience foods and personal care products |
| Nanoclean (nanoclean.store) | Delhi | 2017 | 1-10 | Offering multiple category smoking products |
| Pontika Aerotech (pontikaaerotech.com) | Paonta Sahib | 2017 | 501-1000 | Contract manufacturer of formulations |
| Sarvotham Care (sarvothamcare.com) | Hyderabad | 1996 | 51-200 | Contract manufacturer of liquid orals, tablets, ointments, creams, cosmetics, home and health care… |
| Uniclan (uniclan.in) | Mumbai | 2015 | 51-200 | Manufacturer of hygiene products |
| Vedic Cosmeceuticals (vedicskincare.com) | Noida | 2002 | 51-200 | Contract manufacturer of personal care products |
| Clarion (clarionindia.in) | Chennai | 1993 | 201-500 | Contract manufacturer of cosmetics and personal care products |
| Ramesh Flowers (rameshflowers.com) | Thoothukudi | 1982 | 1001-5000 | Contract based manufacturer of fragrances |
| Stella Indusstries (stella-indusstries.com) | Gurugram | 1983 | 51-200 | Manufacturer of personal care products such as Aerosol and Cosmetics |
| Cheryl Laboratories (cheryllaboratories.com) | Mumbai | 1987 | 11-50 | Manufacturer beauty & personal care products |
| Concept Hygiene (conceptshygiene.com) | Ahmedabad | 2012 | 51-200 | Contract manufacturer of house & laundry, and professional cleaning & hygiene products |
| HCP Wellness (hcpwellness.in) | Ahmedabad | 2017 | 11-50 | Manufacturer of Skin Care and Hair Care & Oral Care Products |
| VFSL (vfslsnacks.com) | Thane | 1986 | 51-200 | Contract manufacturer of snacks |
| Daffy Group (daffygroup.com) | Bengaluru | 1996 | 11-50 | Provider of contract-manufacturing services for cosmetics and personal care products |

## Competitive set: “fmcg” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries FMCG --filters.locations India --limit 20
radar find-competitors --market fmcg --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["FMCG"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "fmcg", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [It Companies in India](it-companies-in-india.md)
- [Insurance Companies in India](insurance-companies-in-india.md)
- [App Development Companies in India](app-development-companies-in-india.md)
- [Fintech Companies in India](fintech-companies-in-india.md)
