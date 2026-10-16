# Textile Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “textile companies in india” · 1,300/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [textile-companies-in-india.json](../../examples/use-cases/textile-companies-in-india.json).

**Question.** Which Textile companies are based in India, how large and how old are they, and who competes in the Textile market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Textile” |
| Companies returned (India, first page) | 20 |

## Textile companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Sidwin Fabrics (sidwinfabrics.com) | Sabarkantha | 2011 | 51-200 | Manufacturer of spun melt, spun bond, and meltblown nonwoven fabrics |
| Canvaloop (canvaloop.com) | Surat | 2020 | 1-10 | Online platform offering sustainable fabrics and materials from agricultural waste |
| Absolute (absolute.ag) | Gurugram | 2015 | 201-500 | Climate-focused deep tech bioscience research institute enabling a sustainable future |
| Flexituff (flexituff.com) | Dhar | 1993 | 1-10 | Online platform for technical textile and irrigation component solutions |
| Pasupati Acrylon (pasupatiacrylon.com) | Delhi | 1990 | 201-500 | Producer of acrylic fiber |
| Rubfila International Limited (rubfila.com) | Palakkad | 1994 | 201-500 | Manufacture of heat resistant latex rubber threads |
| Suryaamba (suryaamba.com) | Nagpur | 1993 | 51-200 | Manufacturer of blended yarns |
| AltMat (altmat.in) | Ahmedabad | 2019 | — | Manufacturer of sustainable material science solutions converting agricultural waste into natural… |
| Greenwear (greenwear.in) | Lucknow | 2018 | 1-10 | Operates retail store of apparel wear for women |
| HIMACHAL FIBRES (himachalfibre.com) | Ludhiana | 1980 | 11-50 | Manufacturer of open end, blended & cotton yarn products |
| Garware Technical Fibres (garwarefibres.com) | Pune | 1976 | 1001-5000 | Developer of technical textiles for multiple industries |
| Sanimo Polymers (sanimoindia.com) | Mumbai | 2000 | 11-50 | Manufacturer of polyester dyed yarn |
| Vortex Flex (vortexflex.com) | Navsari | 2017 | 11-50 | Manufacturer & exporter of leather cloth, PVC products, and other materials |
| Century Enka (centuryenka.com) | Pune | 1965 | 1-10 | Producer of nylon tyre cord fabric and nylon filament yarn |
| Century Textiles and Industries (centurytextind.com) | Mumbai | 1897 | 11-50 | Manufacturer of textile, cement and paper |
| Fabiosys Innovations (fabiosys.com) | Delhi | 2018 | — | Manufacturer of anti-infective surgical supplies for maintaining infection-free surgical… |
| Jasch Industries (jaschindustries.com) | Sonipat | 1985 | 51-200 | Jasch Industries \| Deal in Coated Fabrics, PU Resins, Industrial Gauges |
| MuddleArt (muddleart.com) | Delhi | 2019 | — | Provider of textile waste management services |
| Premier Polyfilm (premierpoly.com) | Delhi | 1992 | 201-500 | Manufacturer of vinyl flooring and related flooring goods |
| Sitaram India (sitaramindia.com) | Bhilwara | 1987 | 11-50 | Manufacturer of fabric products |

## Competitive set: “textile” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Textile --filters.locations India --limit 20
radar find-competitors --market textile --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Textile"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "textile", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Biotech Companies in India](biotech-companies-in-india.md)
- [Food Companies in India](food-companies-in-india.md)
- [Waste Management Companies in India](waste-management-companies-in-india.md)
- [Chemical Companies in India](chemical-companies-in-india.md)
