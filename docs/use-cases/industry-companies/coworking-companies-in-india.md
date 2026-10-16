# Coworking Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “coworking companies in india” · 140/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [coworking-companies-in-india.json](../../examples/use-cases/coworking-companies-in-india.json).

**Question.** Which Coworking companies are based in India, how large and how old are they, and who competes in the Coworking market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Coworking Spaces” |
| Companies returned (India, first page) | 5 |

## Coworking companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Novel Office (noveloffice.in) | Bengaluru/bangalore | 1993 | 51-200 | Novel Office provides business centers, commercial office space on rent, office spaces and startup… |
| co brew ventures (cobrewventures.com) | Chandigarh | 2022 | — | Co Brew Ventures is a leading platform collaborating startups, founders, and investors in one place. |
| Gurgaon IT Hub (gurgaonithub.com) | Gurgaon | 2005 | 51-200 | If People, Performance, Project Management is your forte, we have the Place for you. |
| Sharal CoWork (sharal.com) | — | — | — |  |
| GoHive (gohive.space) | — | 2017 | — |  |

## Competitive set: “coworking” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Coworking Spaces" --filters.locations India --limit 20
radar find-competitors --market coworking --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Coworking Spaces"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "coworking", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [3d Printing Companies in India](3d-printing-companies-in-india.md)
- [Erp Companies in India](erp-companies-in-india.md)
