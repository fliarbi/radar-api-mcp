# Bpo Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “bpo companies in india” · 590/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [bpo-companies-in-india.json](../../examples/use-cases/bpo-companies-in-india.json).

**Question.** Which Bpo companies are based in India, how large and how old are they, and who competes in the Bpo market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “BPO” |
| Companies returned (India, first page) | 20 |

## Bpo companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| AGS (agshealth.com) | Chennai | 2011 | 1-10 | Healthcare revenue cycle management services provider |
| Global Healthcare Billing Partner (ghcbp.com) | Chennai | 2016 | 1001-5000 | Provider of revenue cycle management services to medical billing companies |
| Dvara Holdings (dvara.com) | Chennai | 2008 | 11-50 | Provider of financial services and investment in early-stage financial ventures |
| Access Healthcare (accesshealthcare.com) | Chennai | 2011 | 10000+ | Provider of revenue cycle management, BPO, IT, and finance and accounting services |
| Knack Global (knackglobal.com) | Sahibzada Ajit Singh Nagar | 2007 | 1001-5000 | Provider of revenue cycle management software to healthcare professionals |
| Aditya Birla Health (adityabirlahealth.com) | Mumbai | 2015 | 501-1000 | Provider of health insurance and claim processing services |
| e-care India (ecareindia.com) | Chennai | 2000 | 501-1000 | Provider of medical billing and coding services for the healthcare sector |
| Medryte (medryte.com) | Nagercoil | 2012 | 11-50 | Provider of medical billing & coding services |
| Paul Merchants Finance (paulmerchants.net) | Chandigarh | 2010 | 201-500 | Provider of forex, money transfer, travel, and gold loan services |
| Visionary RCM (visionaryrcm.com) | Chennai | 2006 | 1001-5000 | Provider of medical billing, coding, and revenue cycle management outsourcing services |
| Ascent Business Solutions (ascent-group.com) | Nagpur | 1998 | 51-200 | Provider of BPO services for healthcare |
| CIPHER Healthcare (cipherhealthcare.com) | Hyderabad | 2012 | 51-200 | Provider of a communication paltform for patient management at healthcare organisations |
| Health Prime (hpiinc.com) | — | 1988 | 1001-5000 | Provider of hospital revenue cycle management services |
| ISYS (isyssoftech.in) | Jaipur | 2000 | 51-200 | Provide of medical staffing services |
| RxPrism (rxprism.com) | Bengaluru | 2013 | 201-500 | Provider of digital healthcare marketing services |
| Universal Consulting (universalconsulting.com) | Mumbai | 1994 | 51-200 | Provider of strategy, organisation, operations, and implementation consulting services |
| VIAANTE (viaante.com) | Mumbai | 2011 | 501-1000 | Provider of healthcare payer, call center, data management & IT services |
| Acurus Solutions Abc (acurussolutions.com) | Chennai | 1999 | 201-500 | Provider of BPO services for healthcare |
| Annova Solutions (annovasolutions.com) | Indore | 2016 | 501-1000 | Provider of healthcare, AI/ML operations, and end to end HR services |
| Fedora (ifedora.com) | Ahmedabad | 2004 | 501-1000 | Provider of revenue cycle management services for the healthcare industry |

## Competitive set: “bpo” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries BPO --filters.locations India --limit 20
radar find-competitors --market bpo --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["BPO"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "bpo", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Event Management Companies in India](event-management-companies-in-india.md)
- [Water Companies in India](water-companies-in-india.md)
- [Jewellery Companies in India](jewellery-companies-in-india.md)
- [IOT Companies in India](iot-companies-in-india.md)
