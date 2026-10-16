# It Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “it companies in india” · 8,100/month India · 320/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [it-companies-in-india.json](../../examples/use-cases/it-companies-in-india.json).

**Question.** Which It companies are based in India, how large and how old are they, and who competes in the It market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “IT Services” |
| Companies returned (India, first page) | 20 |

## It companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Canarys (ecanarys.com) | Bengaluru | 1988 | 201-500 | Provider of IT services suite solutions |
| Cyfuture (cyfuture.com) | Noida | 2001 | 1001-5000 | Provider of IT service suite solutions and BPO services |
| Daffodil Software (daffodilsw.com) | Gurugram | 1999 | 51-200 | Provider of a range of IT services |
| Focaloid (focaloid.com) | Bengaluru | 2012 | 51-200 | Custom application development services for enterprises |
| Happiest Minds (happiestminds.com) | Bengaluru | 2011 | 1001-5000 | Provider of IT suite services |
| Neebal (neebal.com) | Mumbai | 2012 | 51-200 | Provider of Industrial IoT solutions and consulting services |
| People10 (people10.com) | Bengaluru | 2011 | 201-500 | Provides horizontal application development services |
| Robosoft (robosoftin.com) | Udupi | 1996 | 501-1000 | Mobile app development company |
| Suventure (suventure.in) | Bengaluru | 2012 | 11-50 | End-to-end IT service provider |
| Gateway Group (thegatewaycorp.com) | Ahmedabad | 1997 | 11-50 | Provider of IT suite services |
| Alletec (alletec.com) | Noida | 2000 | 201-500 | Provider of enterprise business applications and digital services |
| Anantara Solutions (anantsol.com) | Chennai | 2007 | 11-50 | Provider of IT service suite solutions and digital transformation services |
| Blazeclan (blazeclan.com) | Pune | 2010 | 501-1000 | Provider of cloud consulting, DevOps, and digital transformation services |
| Datamatics (datamatics.com) | Mumbai | 1975 | 5001-10000 | Provider of digital technologies, business process management, analytics, and automation services |
| Emproto Technologies (emproto.com) | Bengaluru | 2017 | 11-50 | Provides application development services |
| eNoah (enoahisolution.com) | Chennai | 2006 | 1001-5000 | Provider of web development, data analytics, BPO, ERP, and cloud security services |
| GirnarSOFT (girnarsoft.com) | Jaipur | 2007 | 1001-5000 | Provider of website, web & mobile application development, BI, and digital marketing services |
| GSS Infotech (gssinfotech.com) | Hyderabad | 1999 | 51-200 | Provider of IT services suite solutions |
| Hexaware (hexaware.com) | Mumbai | 1990 | 10000+ | Provider of IT consulting and BPO services |
| iProgrammer (iprogrammer.com) | Pune | 2007 | 201-500 | Provider of web application, mobile app development, cloud management, and robotic process… |

## Competitive set: “it” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "IT Services" --filters.locations India --limit 20
radar find-competitors --market it --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["IT Services"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "it", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Digital Marketing Companies in India](digital-marketing-companies-in-india.md)
- [Pharmaceutical Companies in India](pharmaceutical-companies-in-india.md)
- [Insurance Companies in India](insurance-companies-in-india.md)
- [FMCG Companies in India](fmcg-companies-in-india.md)
