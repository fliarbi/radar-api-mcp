# SAAS Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “saas companies in india” · 720/month India · 20/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [saas-companies-in-india.json](../../examples/use-cases/saas-companies-in-india.json).

**Question.** Which SAAS companies are based in India, how large and how old are they, and who competes in the SAAS market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Software” |
| Companies returned (India, first page) | 20 |
| Competitive set for “saas” (worldwide) | 22 |

## SAAS companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| E2E Networks (e2enetworks.com) | Delhi | 2009 | 51-200 | Provider of cloud infrastructure for artificial intelligence and machine learning |
| Sun Telematics (suntelematics.com) | Bengaluru | 2013 | 51-200 | Saas-enabled fleet management solutions |
| Amnex (amnex.com) | Ahmedabad | 2008 | 501-1000 | Provider of precision agriculture solutions |
| BlueBinaries (bluebinaries.com) | Chennai | 2017 | 201-500 | Provider of engineering solutions for software-driven vehicles and E/E architecture |
| LetsEndorse (letsendorse.com) | Bengaluru | 2014 | 51-200 | Crowdfunding and donation platform to support social cause projects |
| Megdap (megdap.com) | Pune | 2013 | 11-50 | Data for AI training across voice, text, images & videos |
| SmartVizX (smartvizx.com) | Noida | 2014 | 11-50 | Platform offering VR-based solutions for multiple businesses |
| Foyr (foyr.com) | Hyderabad | 2014 | 11-50 | Provider of cloud-based interior design software platform |
| Sacumen (sacumen.com) | Bengaluru | 2015 | 201-500 | Consulting based security service delivery and management |
| Superpro (superpro.ai) | Bengaluru | 2019 | 11-50 | Online platform to deliver videos directly to consumers |
| BangDB (bangdb.com) | Bengaluru | 2015 | 1-10 | Key Value NoSQL Database |
| Bellplus Media (bellplusmedia.com) | Hyderabad | 2019 | 11-50 | Provider of digital signage solutions |
| BUSINESSNEXT (businessnext.com) | Noida | 2001 | 1001-5000 | Provider of composable platform for CRM, data management, lending, and AI agent solutions |
| Commutec (commutec.in) | Mumbai | 2016 | 51-200 | SaaS-driven route scheduling software solutions for employee transport management |
| Eternal Robotics (eternalrobotics.com) | Hyderabad | 2018 | 11-50 | Provider of AI-powered robotics and computer vision solutions for industrial automation |
| Ignitarium (ignitarium.com) | Bengaluru | 2012 | 501-1000 | Provider of AI-powered semiconductor and embedded system design platform |
| Vyorius (vyorius.com) | Delhi | 2018 | 1-10 | Provider of a cloud-based operation management platform for robots and drones |
| Xwards (xwards.com) | Bengaluru | 2016 | 1-10 | In-transit ad exchange and content management software solution |
| Ajeevi (ajeevi.com) | Noida | 2012 | 51-200 | Cloud-based fleet tracking and management solution |
| AuraML (auraml.com) | Bengaluru | 2022 | 1-10 | Developer of multimodal world model for generative robotics simulations |

## Competitive set: “saas” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage. Countries: United States 10, China 2, France 2, Brazil 1, Canada 1, Denmark 1.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |
| Public | indra | Madrid | Indra provides information technology offerings for finance, insurance, public administration,… |
| Public | shenzhen sunline tech | Shenzhen | Shenzhen Sunline Tech provides financial IT services for banks. |
| Public | Sangfor Technologies | China | Sangfor Technologies Inc is a provider of security and cloud computing solutions and is committed… |
| Seed | DAGsHub | Tel Aviv | Provider of free open source software |
| Seed | Papercups | San Francisco | Provider of free open source software |
| Seed | GetScale | Redwood City | Remote quality control software for factories |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Software --filters.locations India --limit 20
radar find-competitors --market saas --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Software"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "saas", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Furniture Companies in India](furniture-companies-in-india.md)
- [Retail Companies in India](retail-companies-in-india.md)
- [Fashion Companies in India](fashion-companies-in-india.md)
- [Event Management Companies in India](event-management-companies-in-india.md)
