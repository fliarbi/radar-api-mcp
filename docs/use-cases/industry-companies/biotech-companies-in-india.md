# Biotech Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “biotech companies in india” · 1,300/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [biotech-companies-in-india.json](../../examples/use-cases/biotech-companies-in-india.json).

**Question.** Which Biotech companies are based in India, how large and how old are they, and who competes in the Biotech market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Biotechnology” |
| Companies returned (India, first page) | 20 |

## Biotech companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Concord Biotech (concordbiotech.com) | Ahmedabad | 2000 | 1001-5000 | CDMO focused on manufacturing API |
| Datar Genetics (datarpgx.com) | Nashik | 1992 | 51-200 | Provider of liquid biopsy-based cancer diagnostic test |
| String Bio (stringbio.com) | Bengaluru | 2013 | 51-200 | Provider of sustainable manufacturing through gas fermentation technology |
| Yashraj Biotechnology (yashraj.com) | Mumbai | 1999 | 201-500 | Provider of recombinant antigens and antibodies for diagnostic and research |
| Zumutor (zumutor.com) | Bengaluru | 2013 | 11-50 | Developer of novel immunotherapy and monoclonal antibody therapeutics |
| 4baseCare (4basecare.com) | Bengaluru | 2018 | 11-50 | Provider of precision oncology solutions, including genomic testing and digital health |
| Anthem Biosciences (anthembio.com) | Bengaluru | 2006 | 1001-5000 | Developer of integrated contract research development and manufacturing services |
| Avesthagen (avesthagen.com) | Bengaluru | 1998 | 51-200 | Life science company operating at the intersection of food, pharma, and agri-technologies |
| Bugworks Research (bugworksresearch.com) | Bengaluru | 2014 | 11-50 | Developer of drugs for antibiotic-resistant bacterial infections and cancer |
| FibroHeal (fibroheal.com) | Bengaluru | 2017 | 11-50 | Developer of silk proteins as biomaterials for wound healing |
| GeneTech (genetech.co.in) | Hyderabad | 1998 | 51-200 | Provider of biomedical genetics, prenatal test, and avian genetic test |
| Intron Life Sciences (intronlifesciences.com) | Hyderabad | 2018 | 51-200 | Manufacturer and supplier of probiotics and biotech products |
| Kan Biosys (kanbiosys.com) | Pune | 2005 | 201-500 | Provider of microbes-based diversified crop biological solutions |
| Leucine Rich Bio (leucinerichbio.com) | Bengaluru | 2014 | 11-50 | Provider of the genomics-based platform to analyze microbiome |
| MedGenome (medgenome.com) | Bengaluru | 2013 | 501-1000 | Provider of DNA sequencing, bioinformatics, and multiomics services |
| Piltover Technologies (piltovertechnologies.com) | Bengaluru | 2015 | 1-10 | Provider of artificial limbs for disable person |
| Sayre Therapeutics (sayretherapeutics.com) | Bengaluru | 2015 | 11-50 | Provider of access to innovative therapies for rare and life-threatening diseases |
| Shilps Sciences (shilpsciences.com) | Bengaluru | 2013 | 11-50 | Developer of microfluidic devices for imaging and characterization at the nano and micro scale |
| Tropical Animal Genetics (taggnx.com) | Gurugram | 2014 | 11-50 | Provider of assisted reproductive technologies and superior genetics for livestock |
| Mahyco (mahyco.com) | Jalna | 1964 | 501-1000 | Provider of research, production, processing, and marketing of agricultural seeds |

## Competitive set: “biotech” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Biotechnology --filters.locations India --limit 20
radar find-competitors --market biotech --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Biotechnology"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "biotech", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Cybersecurity Companies in India](cybersecurity-companies-in-india.md)
- [Robotics Companies in India](robotics-companies-in-india.md)
- [Food Companies in India](food-companies-in-india.md)
- [Textile Companies in India](textile-companies-in-india.md)
