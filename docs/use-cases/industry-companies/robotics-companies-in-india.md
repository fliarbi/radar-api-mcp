# Robotics Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “robotics companies in india” · 1,300/month India · 70/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [robotics-companies-in-india.json](../../examples/use-cases/robotics-companies-in-india.json).

**Question.** Which Robotics companies are based in India, how large and how old are they, and who competes in the Robotics market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Robotics” |
| Companies returned (India, first page) | 20 |

## Robotics companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Jay Robotix (jayrobotix.co.in) | — | 2010 | 11-50 | Provider of robotic equipment for industrial automation |
| Accio Robotics (acciorobotics.com) | Bengaluru | 2019 | 11-50 | Developer of warehouse automation robots focused on order picking processes |
| Ati Motors (atimotors.com) | Bengaluru | 2017 | 51-200 | Manufacturer of autonomous mobile robots for material movement and productivity |
| Gridbots (gridbots.com) | Ahmedabad | 2007 | 1-10 | Robotics manufacturing solutions for industrial use |
| Hachidori Robotics (hachidorirobotics.com) | Bengaluru | 2019 | 51-200 | Manufacturer of autonomous mobile robots for material movement in industries |
| Inker Robotics (inkerrobotics.com) | Thrissur | 2018 | 1-10 | Provider of robotics education, robotic kits, and technology-based research services |
| SP Robotic Works (sproboticworks.com) | Bengaluru | 2012 | 1-10 | Provider of robotics, coding, and STEM education kits and classes |
| STEM Robo (stemrobo.com) | Noida | 2012 | 51-200 | Developer of STEM and robotics DIY kits |
| Systemantics (systemantics.com) | Bengaluru | 1995 | 11-50 | Manufacturer of collaborative robots for industrial automation |
| ThinkLink (thinklink-scs.com) | Gurugram | 2006 | 1-10 | Provider of warehouse automation solutions |
| Unbox Robotics (unboxrobotics.com) | Pune | 2019 | 51-200 | Provider of software-defined robotics system for warehouse operations |
| Addverb (addverb.com) | Noida | 2016 | 501-1000 | Provider of automated warehouse solutions using robotics and software |
| Asimov Robotics (asimovrobotics.com) | Kollam | 2012 | 11-50 | Provider of robotics manufacturing and distribution |
| Makebot (makebot.in) | Mumbai | 2010 | 11-50 | Provider of STEAM education programs for students |
| Pari Robotics (parirobotics.com) | Pune | 1990 | 1001-5000 | Manufacturer of precision automation and robotics products and technologies |
| Seven Robotics (sevenrobotics.in) | Hyderabad | 2018 | 1-10 | Manufacturer of AI and web enabled robotic solution for logistics |
| Ace Robotics (acerobotics.in) | Chennai | 2019 | 11-50 | Manufacturer of arm-based industrial robots for multiple purposes |
| ANSCER (anscer.com) | Bengaluru | 2020 | 1-10 | Manufacturer of autonomous mobile robots and related fleet management software |
| Endless Robotics (endlessrobotics.com) | Hyderabad | 2015 | 11-50 | Robotic solutions for decorative painting industry |
| iFuture Robotics (ifuturerobotics.com) | Bengaluru | 2016 | 1-10 | Developer of warehouse management software and industrial robots for automation |

## Competitive set: “robotics” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Robotics --filters.locations India --limit 20
radar find-competitors --market robotics --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Robotics"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "robotics", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Advertising Companies in India](advertising-companies-in-india.md)
- [Cybersecurity Companies in India](cybersecurity-companies-in-india.md)
- [Biotech Companies in India](biotech-companies-in-india.md)
- [Food Companies in India](food-companies-in-india.md)
