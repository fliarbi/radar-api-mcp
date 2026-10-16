# Telecom Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “telecom companies in india” · 2,400/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [telecom-companies-in-india.json](../../examples/use-cases/telecom-companies-in-india.json).

**Question.** Which Telecom companies are based in India, how large and how old are they, and who competes in the Telecom market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Telecommunications” |
| Companies returned (India, first page) | 20 |

## Telecom companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Futwork (futwork.com) | Mumbai | 2016 | 11-50 | Provider of AI-powered contact center solutions |
| Subex (subex.com) | Bengaluru | 1992 | 501-1000 | Telecom business and operations support systems provider |
| Matrix Cellular Services (matrix.in) | Delhi | 2005 | 11-50 | SIM cards, Forex cards and travel insurance |
| Prodapt (prodapt.com) | Chennai | 1999 | 1001-5000 | Provider of IT services for businesses |
| Repaireasy.in (repaireasy.in) | Pune | 2013 | 1-10 | Provider of electronic repair services |
| Route Mobile (routemobile.com) | Mumbai | 2004 | 201-500 | Provider of cloud communication platform as a service (CPaaS) solutions |
| Tanla Platforms (tanla.com) | Hyderabad | 1999 | 11-50 | VAS messaging, IoT and cloud telephony solutions provider |
| VMukti (vmukti.com) | Ahmedabad | 2007 | 11-50 | Cloud based video streaming surveillance and meeting platform |
| Waybeo (waybeo.com) | Thiruvananthapuram | 2009 | 11-50 | Artificial intelligence based platform offering conversational analytics software solutions |
| ACL (aclmobile.com) | Noida | 2000 | 501-1000 | Omnichannel customer communication management solutions |
| ACT (actcorp.in) | Bengaluru | 2000 | 5001-10000 | Provider of fibre optic broadband, WiFi network, and television services |
| Aksh Optifibre (akshoptifibre.com) | Delhi | 1986 | 51-200 | Manufacturer of plastic-based optical fibers |
| Altruist Technologies (altruistindia.com) | Panchkula | 2005 | 1001-5000 | Provider of mobile value added services |
| Apalya (apalya.com) | Hyderabad | 2005 | 201-500 | End-to-end video management and delivery solutions provider |
| Ascend Telecom (ascendtele.com) | Bengaluru | 2002 | 11-50 | Provider of telecom infrastructure and allied services |
| Bharti Infratel (bharti-infratel.com) | Gurugram | 2006 | 1001-5000 | Online platform for tower infrastructure and services |
| Bharat Sanchar Nigam (bsnl.co.in) | Delhi | 2000 | 10000+ | Provider of international roaming, telephone, wifi, and broadband services |
| Eagle Photonics (eaglephotonics.com) | Bengaluru | 2002 | 1-10 | Provider of fiber optic products, training, and consultancy services. It offers a comprehensive… |
| Exotel (exotel.com) | Bengaluru | 2011 | 201-500 | Provider of cloud-based communication platform offering AI-powered customer engagement solutions |
| HFCL (hfcl.com) | Delhi | 1987 | 1001-5000 | Provider of telecom equipment and fiber cables |

## Competitive set: “telecom” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Telecommunications --filters.locations India --limit 20
radar find-competitors --market telecom --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Telecommunications"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "telecom", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Legal Companies in India](legal-companies-in-india.md)
- [Consulting Companies in India](consulting-companies-in-india.md)
- [Gaming Companies in India](gaming-companies-in-india.md)
- [Electronics Companies in India](electronics-companies-in-india.md)
