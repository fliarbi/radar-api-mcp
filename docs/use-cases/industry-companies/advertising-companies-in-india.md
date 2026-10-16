# Advertising Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “advertising companies in india” · 1,900/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [advertising-companies-in-india.json](../../examples/use-cases/advertising-companies-in-india.json).

**Question.** Which Advertising companies are based in India, how large and how old are they, and who competes in the Advertising market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Advertising” |
| Companies returned (India, first page) | 20 |

## Advertising companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| GreedyGame Media (greedygame.com) | Bengaluru | 2013 | 11-50 | Provider of all in one solutions for all app growth and app monetization requirement |
| Entropik (entropik.io) | Bengaluru | 2016 | 51-200 | AI powered consumer behavior analysis platform |
| Moby (mobyads.in) | Gurugram | 2017 | — | Platform for near store omnichannel advertising |
| PLAKC (plakc.com) | Mumbai | 2014 | — | In-game advertising and marketing platform |
| Crooze (crooze.app) | Ahmedabad | 2021 | — | Provider of a reward-based community app for cyclists |
| Opa (opareviews.com) | Mumbai | 2019 | 1-10 | Mouth marketer and influencer community platform |
| AduClick (aduclick.in) | Delhi | 2018 | — | Platform offering ad network solution |
| Alist.club (alist.club) | Delhi | 2020 | — | Provider of influencer marketing services to brands |
| Eventsdo (eventsdo.com) | Thiruvananthapuram | 2017 | — | Cloud-based event vendor and venue listing platform proivder |
| vHub.ai (vhub.ai) | Bengaluru | 2021 | — | AI based influencer marketing solutions for brands |
| Airavat (airavatbusiness.com) | Ahmedabad | 2022 | — | Provider of branding, web & app development, IoT, and data networking services |
| Cheggout (cheggout.com) | Bengaluru | 2017 | — | Provider of marketing platform connecting brands with banking application users |
| CityBazarOnline (citybazaronline.com) | Indore | 2019 | — | Platform offering local shopkeepers marketplace |
| Hector (hectorai.live) | Mumbai | 2022 | — | Provider of Amazon advertising platform with optimization and automation capabilities |
| Payzo (payzopartner.com) | Visakhapatnam | 2023 | — | Provider of instant cashback points for payments at partner stores |
| Programmatic India (programmaticindia.com) | Mumbai | 2019 | — | Platform offering dsp solution |
| Troak (troak.club) | Bengaluru | 2023 | — | In game advertising platform |
| Vmerg (vmerg.com) | Bengaluru | 2021 | — | Platform offering influencer marketing software |
| ADNUE (adnue.com) | Jaipur | 2020 | — | Provider of cross device ad network |
| adzip (adzip.in) | — | 2021 | — | Provider of collaborative social media ad campaign management platform |

## Competitive set: “advertising” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Advertising --filters.locations India --limit 20
radar find-competitors --market advertising --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Advertising"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "advertising", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Gaming Companies in India](gaming-companies-in-india.md)
- [Electronics Companies in India](electronics-companies-in-india.md)
- [Cybersecurity Companies in India](cybersecurity-companies-in-india.md)
- [Robotics Companies in India](robotics-companies-in-india.md)
