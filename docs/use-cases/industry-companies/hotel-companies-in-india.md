# Hotel Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “hotel companies in india” · 320/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [hotel-companies-in-india.json](../../examples/use-cases/hotel-companies-in-india.json).

**Question.** Which Hotel companies are based in India, how large and how old are they, and who competes in the Hotel market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Hotel” |
| Companies returned (India, first page) | 20 |

## Hotel companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| BookingJini (bookingjini.com) | Bhubaneswar | 2015 | 11-50 | Provider of hotel booking engine, channel manager, and property management |
| Djubo (djubo.com) | Noida | 2015 | 51-200 | Provider of cloud-based software suite for hotel management and operations |
| Maximojo (maximojo.com) | Pune | 2011 | 11-50 | Cloud-based distribution & revenue management solutions for hotels |
| OYO (oyorooms.com) | Gurugram | 2012 | 51-200 | Chains providing hotel and home booking services with free cancellation |
| Simplotel (simplotel.com) | Bengaluru | 2013 | 51-200 | Cloud platform to develop website and booking engine for hotels |
| Treebo (treebo.com) | Bengaluru | 2015 | 501-1000 | Operator of a network providing accommodations across multiple brands and tiers |
| Humming Bird Digital (hummingbirdindia.com) | Bengaluru | 2006 | 11-50 | AI-enabled hotel booking tool for corporate travelers |
| ICanStay (icanstay.com) | Gurugram | 2015 | 1-10 | Online platform to book luxury hotel stays |
| IDS Next (idsnext.com) | Bengaluru | 1987 | 201-500 | Provider of cloud-based enterprise resource planning software for hospitality businesses |
| Mistay (mistay.in) | Gurugram | 2016 | 11-50 | Online hotel booking platform that allows users to book hotel rooms based on time slots |
| RezNext (reznext.com) | Bengaluru | 2012 | 11-50 | Real time distribution management solution provider |
| Bag2Bag (bag2bag.in) | Bengaluru | 2019 | 11-50 | Online retailer of hourly, overnight, and extended stay accommodation options |
| NightStay (nightstay.in) | Noida | 2014 | 1-10 | App-based platform for last minute hotel booking |
| QikStay (qikstay.com) | Gurugram | 2015 | 11-50 | Asset light chain of budget hotels |
| Quoality (quoality.com) | Gurugram | 2020 | 11-50 | Provider of a platform for managing in-room ancillary services |
| V Resorts (vresorts.in) | Noida | 2010 | 51-200 | Online hotel booking platform |
| BreviStay (brevistay.com) | Noida | 2016 | 51-200 | App-based platform to book hotels on an hourly basis |
| InnkeyPMS (innkeypms.net) | Ahmedabad | 2011 | 51-200 | Cloud based ERP and property management software for hotels |
| Roomoncall (roomoncall.in) | Gurugram | 2015 | 11-50 | Online branded budget hotel chain |
| RoomsTonite (roomstonite.com) | Bengaluru | 2014 | 11-50 | Last-minute hotel booking mobile app |

## Competitive set: “hotel” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Hotel --filters.locations India --limit 20
radar find-competitors --market hotel --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Hotel"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "hotel", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Data Analytics Companies in India](data-analytics-companies-in-india.md)
- [Quantum Computing Companies in India](quantum-computing-companies-in-india.md)
- [Sports Companies in India](sports-companies-in-india.md)
- [Microfinance Companies in India](microfinance-companies-in-india.md)
