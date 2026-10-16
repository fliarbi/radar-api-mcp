# Pharmaceutical Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “pharmaceutical companies in india” · 9,900/month India · 170/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [pharmaceutical-companies-in-india.json](../../examples/use-cases/pharmaceutical-companies-in-india.json).

**Question.** Which Pharmaceutical companies are based in India, how large and how old are they, and who competes in the Pharmaceutical market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Pharmaceuticals” |
| Companies returned (India, first page) | 20 |

## Pharmaceutical companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Rubicon (rubicon.co.in) | Mumbai | 2000 | 201-500 | CDMO offering drug development services through its proprietary drug delivery technologies |
| Ascent Health & Wellness Solutions (ahwspl.com) | Mumbai | 2012 | 1001-5000 | Provider of pharmaceutical supply chain solutions |
| Akums (akums.in) | Delhi | 2004 | 1001-5000 | CDMO focusing on spectrum of dosage forms and therapeutic segments |
| Amanta Healthcare (amanta.co.in) | Ahmedabad | 1997 | 501-1000 | Manufacturer of sterile liquid parenterals using Aseptic BFS & ISBM technology |
| BDR Pharmaceuticals (bdrpharma.com) | Mumbai | 2003 | 1001-5000 | Developer and manufacturer of APIs as well as finished products |
| Celon Laboratories (celonlabs.com) | Hyderabad | 2007 | 501-1000 | Manufacturer of oncology-based products |
| Corona Remedies (coronaremedies.com) | Ahmedabad | 2004 | 1001-5000 | Manufacturer of pharmaceutical products focused on women's health, cardio-diabetology, pain… |
| Emcure (emcure.com) | Pune | 1983 | 5001-10000 | Developer, manufacturer, and markets a broad range of pharmaceutical products |
| Fermenta Biotech (fermentabiotech.com) | Thane | 1986 | 201-500 | Manufacturer of Vitamin D3, enzymes, and environmental solutions |
| La Renon (larenon.com) | Ahmedabad | 2007 | 1001-5000 | Provider of pharmaceutical products |
| Laurus Labs (lauruslabs.com) | Hyderabad | 2005 | 5001-10000 | Pharmaceutical and biotechnology company |
| Mankind Pharma (mankindpharma.com) | Delhi | 1991 | 1001-5000 | Pharmaceutical company engaged in developing, manufacturing, and marketing a diverse range of… |
| Nectar Lifesciences (neclife.com) | Chandigarh | 1995 | 1001-5000 | Manufacturer of cephalosporin APIs and generic formulations |
| Sai Life Sciences (sailife.com) | Hyderabad | 1999 | 1001-5000 | Provider of drug discovery, developing, and manufacturing of complex small molecules |
| Siro Clinpharm (siroclinpharm.com) | Thane | 2000 | 51-200 | Company offering clinical development services |
| Akumentis Healthcare (akumentishealthcare.com) | Thane | 2010 | 1001-5000 | Manufacturer of pharmaceutical products across multiple therapeutic areas |
| Baroque Pharmaceuticals (baroquepharma.com) | Khambhat | 1994 | 201-500 | Manufacturer of affordable pharmaceutical products |
| Eurolife Healthcare (eurolifehealthcare.com) | Mumbai | 2001 | 51-200 | Manufacturer and distributor of healthcare formulations |
| Globela Pharma (globelapharma.com) | Surat | 1996 | 51-200 | Manufacturer of tablets, capsules, syrup, and injectables |
| Hexagon Nutrition (hexagonnutrition.com) | Mumbai | 1991 | 201-500 | Manufacturer of micronutrient premixes, clinical nutrition products, and therapeutic food |

## Competitive set: “pharmaceutical” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Pharmaceuticals --filters.locations India --limit 20
radar find-competitors --market pharmaceutical --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Pharmaceuticals"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "pharmaceutical", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [AI Companies in India](ai-companies-in-india.md)
- [Digital Marketing Companies in India](digital-marketing-companies-in-india.md)
- [It Companies in India](it-companies-in-india.md)
- [Insurance Companies in India](insurance-companies-in-india.md)
