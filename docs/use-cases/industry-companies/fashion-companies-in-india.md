# Fashion Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “fashion companies in india” · 720/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [fashion-companies-in-india.json](../../examples/use-cases/fashion-companies-in-india.json).

**Question.** Which Fashion companies are based in India, how large and how old are they, and who competes in the Fashion market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Fashion” |
| Companies returned (India, first page) | 20 |

## Fashion companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| 1-India Family Mart (1indiafamilymart.com) | Delhi | 2012 | 501-1000 | Offline retail chain for multi-category products |
| Ben Franklin (benfranklin.in) | Hyderabad | 2008 | 1001-5000 | Chain of optical retail stores |
| Bijnis (bijnis.com) | Delhi | 2015 | 501-1000 | Online platform offering B2B sourcing and trading solutions |
| Eastman Exports (eastmanexports.com) | Tiruppur | 2003 | 1001-5000 | Contract manufacturer of apparel products |
| Ethos Watch (ethoswatches.com) | Chandigarh | 2003 | 501-1000 | Retail chain of luxury watches |
| Fashinza (fashinza.com) | Gurugram | 2020 | 1-10 | Platform offering AI-enabled production solutions for the fashion industry |
| Specsmakers (specsmakers.in) | Chennai | 2007 | 501-1000 | Internet first brand of eyeglasses, sunglasses, contact lenses, and related accessories |
| VastraApp (vastraapp.com) | Ahmedabad | 2018 | 11-50 | Cloud-based software suite solutions for fashion retailers |
| Wholesalebox (wholesalebox.in) | Jaipur | 2015 | 1-10 | Online wholesale distribution platform for fashion products |
| Shoppers Stop (shoppersstop.com) | Mumbai | 1991 | 5001-10000 | Retailer of large format fashion and lifestyle products |
| Bigthinx (bigthinx.com) | Bengaluru | 2015 | 11-50 | Platform offering AI‑driven 3D solutions for fashion and gaming |
| Celebrity Fashions (celebritygroup.com) | Chennai | 1988 | 1001-5000 | Contract manufacturer of garments |
| Diamond India (diamondindia.net) | Mumbai | 2002 | 11-50 | Wholesaler of luxury good and jewelry |
| Ed-a-Mamma (edamamma.com) | Mumbai | 2020 | 11-50 | Internet first brand offering eco-friendly apparel for kids and mom |
| Fibre2Fashion (fibre2fashion.com) | Ahmedabad | 2000 | 51-200 | B2B marketplace for textile and fashion industry |
| Future Lifestyle Fashions (futurelifestyle.in) | Mumbai | 2012 | 1001-5000 | Retail chain of fashion and clothing products |
| Gokaldas Exports (gokaldasexports.com) | Bengaluru | 1979 | 1001-5000 | Contract manufacturer and exporter of apparel and clothing |
| House of Brands (houseofbrands.company) | Bengaluru | 2021 | 11-50 | Designer and manufacturer of premium direct-to-consumer apparel and accessories |
| Kalyan Jewellers (kalyanjewellers.net) | Thrissur | 1993 | 10000+ | Retail chain of jewellery |
| Khadim's (khadims.com) | Kolkata | 1965 | 501-1000 | Retailer of footwear for men, women, and children through online channels |

## Competitive set: “fashion” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Fashion --filters.locations India --limit 20
radar find-competitors --market fashion --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Fashion"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "fashion", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Retail Companies in India](retail-companies-in-india.md)
- [SAAS Companies in India](saas-companies-in-india.md)
- [Event Management Companies in India](event-management-companies-in-india.md)
- [Water Companies in India](water-companies-in-india.md)
