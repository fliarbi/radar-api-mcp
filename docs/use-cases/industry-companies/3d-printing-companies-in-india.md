# 3d Printing Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “3d printing companies in india” · 260/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [3d-printing-companies-in-india.json](../../examples/use-cases/3d-printing-companies-in-india.json).

**Question.** Which 3d Printing companies are based in India, how large and how old are they, and who competes in the 3d Printing market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “3D Printing” |
| Companies returned (India, first page) | 20 |
| Competitive set for “3d printing” (worldwide) | 44 |

## 3d Printing companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Fracktal Works (fracktal.in) | Udupi | 2013 | 11-50 | Manufacturer of 3D printers and provider of 3D printing services |
| Objectify Technologies (objectify.co.in) | Kanpur | 2013 | 51-200 | Manufacturer of on-demand industrial 3D printing services |
| Shapecrunch (shapecrunch.com) | Delhi | 2015 | 11-50 | 3D printed custom insoles for shoes |
| VelvetCase (velvetcase.com) | Mumbai | 2013 | 1-10 | Internet first brand offering customized precious jewelry |
| Renderwise (renderwise.in) | Delhi | 2017 | 51-200 | Provider of 3D printing services and clear aligner manufacturing |
| Anatomiz3D (anatomiz3d.com) | Mumbai | 2016 | — | Provider of medical 3D printing solutions and surgical implants |
| Chizel (chizel.io) | Pune | 2014 | 11-50 | Provider of additive manufacturing services for the industrial applications |
| Global 3D Labs (global3dlabs.com) | Bengaluru | 2014 | 1-10 | Manufacturer of 3D printers |
| Imaginarium (imaginarium.io) | Mumbai | 2009 | 201-500 | Provider of additive manufacturing, CNC machining, and reverse engineering services |
| Tvasta (tvasta.construction) | Chennai | 2016 | 51-200 | Online platform for providing end to end solutions for construction 3D printing |
| Intech (intechadditive.com) | Bengaluru | 2012 | 51-200 | Manufacturer of metal 3D printers and related software solutions |
| ThinkMetal (thinkmetal.in) | Chennai | 2021 | 1-10 | Manufacturer of desktop 3D printers |
| Kloneworld (kloneworld.com) | Kolkata | 2013 | 1-10 | 3D Printed figurines manufacturer |
| MiCoB (micob.in) | Gandhinagar | 2018 | 11-50 | Provider of 3D concrete printing solutions for construction |
| Ornativa (ornativa.com) | Hyderabad | 2014 | — | Online brand of fast fashion jewelry |
| 3DPD (3dpd.net) | Bengaluru | 2001 | 51-200 | 3D Printing services |
| Stpl3D (stpl3d.com) | Surat | 2017 | 501-1000 | Provider of industrial three-dimensional printing services using various printing technologies |
| 3D Print World (3dprintworld.co.in) | Mumbai | 2015 | — | 3D Printing services |
| Carbine Systems (carbine3d.com) | Belgaum | 2023 | — | Provider of AI and ML-based machines to revolutionize the production process in industries such as… |
| Ex3DP (excelling3dp.com) | Pune | 2017 | — | 3D printers and printing services |

## Competitive set: “3d printing” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage. Countries: United States 22, China 8, Germany 3, Israel 2, Japan 2, Belgium 1.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |
| Public | KEYENCE | Itasca | Manufacturer of factory automation sensors, measuring instruments, and vision systems |
| Public | Shibuya Kogyo | Kanazawa | Technology for biological 3D printing |
| Public | ABIST | Tokyo | Provider of 3D modelling and printing services |
| Seed | Toybox | Oakland | Manufacturer of 3D printers, printer food, and related digital content |
| Seed | Cad Crowd | Calgary | On-demand 3D modelling, 3D design & CAD drafting services |
| Seed | MyMiniFactory | London | 3D model online repository with pre-tested designs |
| Series A | Farsoon Technologies | Changsha | Developer of sintering 3D printers for building plastic and metal products |
| Series A | MatterHackers | Lake | Online retailer of 3D printers, materials, and digital fabrication supplies |
| Series A | 9T Labs | Zurich | Provider of diversified 3D printing equipment |
| Series B | Elegoo | Shenzhen | Manufacturer of consumer-level three-dimensional printers, materials, STEM kits, and accessories |
| Series B | Ultimaker | Geldermalsen | Manufacturer of professional-grade 3D printers and materials |
| Series B | Chamlion | Nanjing | Provider of 3D printers and 3D printing services |
| Series C | ICON | Austin | Developer of a 3D printer supplier for the building industry |
| Series C | Arris Composites | Berkeley | Manufacturer of carbon fiber composites for multiple industrial applications |
| Series C | Sakuu | San Jose | Provider of AI-enabled desktop 3D battery printers for automotive applications |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "3D Printing" --filters.locations India --limit 20
radar find-competitors --market "3d printing" --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["3D Printing"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "3d printing", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Microfinance Companies in India](microfinance-companies-in-india.md)
- [Media Companies in India](media-companies-in-india.md)
- [Erp Companies in India](erp-companies-in-india.md)
- [Coworking Companies in India](coworking-companies-in-india.md)
