# Jewellery Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “jewellery companies in india” · 480/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [jewellery-companies-in-india.json](../../examples/use-cases/jewellery-companies-in-india.json).

**Question.** Which Jewellery companies are based in India, how large and how old are they, and who competes in the Jewellery market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Jewellery” |
| Companies returned (India, first page) | 20 |

## Jewellery companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| BlueStone (bluestone.com) | Bengaluru | 2011 | 1001-5000 | Retailer of gold diamond platinum and gemstone jewellery and coins |
| Candere (candere.com) | Mumbai | 2012 | 51-200 | Online retailer of gold and diamond jewellery for various occasions |
| CaratLane (caratlane.com) | Chennai | 2008 | 1001-5000 | Internet-first brand offering precious jewelry products for men and women |
| Fourseven (fourseven.com) | Gurugram | 2012 | 11-50 | Online platform offering designer jewellery |
| Melorra (melorra.com) | Bengaluru | 2015 | 201-500 | Internet-first brand offering precious jewelry |
| Voylla (voylla.com) | Jaipur | 2013 | 51-200 | Internet-first brand of jewelry and fashion accessories |
| Fiona Diamond (fionadiamonds.com) | Mumbai | 2015 | 11-50 | Brand of lab-grown diamond rings, earrings, pendants, and bracelets |
| GemPundit (gempundit.com) | Gurugram | 2013 | 51-200 | Online retailer of loose gemstones and gemstone-set jewelry pieces |
| GIVA (giva.co) | Bengaluru | 2019 | 1001-5000 | Retailer of silver, gold, and lab-grown diamond jewellery |
| JewelMaze (jewelmaze.com) | Mumbai | 2017 | 11-50 | Online platform providing fashion jewellery |
| Sukkhi Fashion Jewellery (sukkhi.com) | Mumbai | 2012 | 11-50 | Online retailer of Indian ethnic and fashion jewelry |
| Ultrahuman (ultrahuman.com) | Bengaluru | 2019 | 51-200 | Provider of wearable health trackers and metabolic monitoring hardware devices |
| VelvetCase (velvetcase.com) | Mumbai | 2013 | 1-10 | Internet first brand offering customized precious jewelry |
| Amama (amama.in) | Delhi | 2016 | 11-50 | Internet-first brand of handcrafted fast-fashion jewelry for women |
| Aulerth (aulerth.com) | Gurugram | 2021 | 11-50 | Online retailer of semi-precious sustainable jewelry designed in partnership with designers |
| Bempu (bempu.com) | Bengaluru | 2014 | 1-10 | Manufacturer of newborn monitoring devices designed to detect and alert caregivers |
| DiA (diaprecious.com) | Mumbai | 2000 | 11-50 | Retailer offering jewellery pieces, including necklaces, pendants, and earrings |
| eJohri (ejohri.com) | Mumbai | 2015 | 1-10 | Online marketplace offering precious jewelry |
| Gold Setu (goldsetu.co) | Bengaluru | 2021 | 11-50 | Platform offering software suite solutions for jewelry stores |
| I Love Diamonds (ilovediamonds.com) | Chennai | 2000 | 1-10 | Internet first brand offering precious jewelry |

## Competitive set: “jewellery” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Jewellery --filters.locations India --limit 20
radar find-competitors --market jewellery --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Jewellery"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "jewellery", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Water Companies in India](water-companies-in-india.md)
- [Bpo Companies in India](bpo-companies-in-india.md)
- [IOT Companies in India](iot-companies-in-india.md)
- [Healthtech Companies in India](healthtech-companies-in-india.md)
