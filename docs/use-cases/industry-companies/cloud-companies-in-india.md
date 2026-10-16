# Cloud Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “cloud companies in india” · 880/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [cloud-companies-in-india.json](../../examples/use-cases/cloud-companies-in-india.json).

**Question.** Which Cloud companies are based in India, how large and how old are they, and who competes in the Cloud market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Cloud” |
| Companies returned (India, first page) | 20 |

## Cloud companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| ESDS (esds.co.in) | Nashik | 2005 | 1001-5000 | Provider of cloud and data centre infrastructure solutions |
| Blazeclan (blazeclan.com) | Pune | 2010 | 501-1000 | Provider of cloud consulting, DevOps, and digital transformation services |
| Cloudxchange.io (cloudxchange.io) | Mumbai | 2018 | 1001-5000 | Provider of cloud services |
| G7 CR Technologies (g7cr.com) | Bengaluru | 2008 | 201-500 | Provider of cloud implementation and microsoft services |
| Suyati Technologies (suyati.com) | Kochi | 2009 | 201-500 | CRM, CMS, mobile and web development services |
| Feuji (feuji.com) | Hyderabad | 2014 | 51-200 | Provider of digital transformation, AI and IT services |
| smartData Enterprise (smartdatainc.com) | Sahibzada Ajit Singh Nagar | 1998 | 201-500 | Software Development Outsourcing Company |
| GlobalOutlook (globaloutlook.com) | Hyderabad | 2007 | 11-50 | Office Communication and Collaboration Software |
| VXL Instruments (vxl.net) | Bengaluru | 1986 | 11-50 | Thin-Client and Cloud-Client Devices Provider |
| Applied Cloud Computing (appliedcloudcomputing.com) | Thane | 2013 | 201-500 | Cloud-based solutions provider |
| Cirrologix (cirrologix.com) | Bengaluru | 2010 | 11-50 | Cloud Services Provider |
| Cloud Analogy (cloudanalogy.com) | Noida | 2015 | 201-500 | Provider of customer relationship management consulting, full stack development, and digital… |
| CloudThat (cloudthat.com) | Bengaluru | 2012 | 201-500 | Cloud consulting and training services provider |
| DCirrus (dcirrus.com) | Delhi | 2015 | 1-10 | Provider of a virtual data room - VDR |
| Softcell (softcell.com) | Mumbai | 1989 | 501-1000 | Provider of cloud management and IT security services |
| Umbrella (umbrellainfocare.com) | Noida | 2013 | 51-200 | Provider of managed cloud services |
| CloudJournee (cloudjournee.com) | Bengaluru | 2016 | 11-50 | Services related to the adoption of cloud infrastructure for enterprises |
| Ace Cloud Hosting (acecloudhosting.com) | Delhi | 2004 | 51-200 | Provider of cloud migration services |
| Prismberry (prismberry.com) | Noida | 2018 | 11-50 | Provider of cloud application development and cloud migration services |
| Aditi (aditi.com) | Bengaluru | 1994 | 1001-5000 | Aditi Technologies Now HARMAN, is outsourced product development company offering services to ISVs |

## Competitive set: “cloud” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Cloud --filters.locations India --limit 20
radar find-competitors --market cloud --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Cloud"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "cloud", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Chemical Companies in India](chemical-companies-in-india.md)
- [Market Research Companies in India](market-research-companies-in-india.md)
- [Furniture Companies in India](furniture-companies-in-india.md)
- [Retail Companies in India](retail-companies-in-india.md)
