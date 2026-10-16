# Media Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “media companies in india” · 260/month India · 20/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [media-companies-in-india.json](../../examples/use-cases/media-companies-in-india.json).

**Question.** Which Media companies are based in India, how large and how old are they, and who competes in the Media market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Media & Entertainment” |
| Companies returned (India, first page) | 20 |

## Media companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Spyne.ai (spyne.ai) | Gurugram | 2018 | 51-200 | Platform offering AI-powered imaging for vehicle photography |
| Amagi (amagi.com) | Bengaluru | 2008 | 501-1000 | Provider of cloud-based solutions for broadcast, streaming, and CTV advertising |
| Baby Destination (babydestination.com) | Delhi | 2017 | 1-10 | Provider of a community platform with content and support for mothers |
| CLIRNET (clirnet.com) | Mumbai | 2015 | 51-200 | Digital continuing medical education and doctor-generated content platform |
| Corpus (corpus.com) | Hyderabad | 1999 | 51-200 | Media delivery solutions provider for OTT platforms |
| Hurix Digital (hurix.com) | Mumbai | 2000 | 501-1000 | Provider of digital learning, publishing solutions, and AI-powered data services |
| Ittiam (ittiam.com) | Bengaluru | 2001 | 11-50 | Provider of video encoding and transcoding solutions for various applications |
| Magnaquest (magnaquest.com) | Hyderabad | 1997 | 51-200 | Provider of a subscription billing management platform |
| Nazara (nazara.com) | Mumbai | 1999 | 51-200 | Provider of diversified gaming and sports media platform |
| Rediff.com (rediff.com) | Mumbai | 1996 | 201-500 | Provider of news, email services, stock quotes, and online expert advice |
| Talentrack (talentrack.in) | Delhi | 2015 | 51-200 | Online marketplace to hire acting professionals |
| UFO Moviez (ufomoviez.com) | Mumbai | 2005 | 501-1000 | Network providing cinema advertising, film distribution, and cinema technology services |
| Venera Tech (veneratech.com) | Noida | 2003 | 1001-5000 | Video solutions and digital media company |
| AFK Gaming (afkgaming.com) | Noida | 2012 | 11-50 | Online platform offering esports news |
| AlmaBay (almabay.com) | Zirakpur | 2015 | 1-10 | Alumni engagement platform for higher educational institutes |
| AlmaConnect (almaconnect.com) | Gurugram | 2011 | 11-50 | Offers a web-based platform to create socio-professional alumni networks |
| Balaji Telefilms (balajitelefilms.com) | Mumbai | 1994 | 51-200 | Producer of films and TV shows |
| Bar & Bench (barandbench.com) | Delhi | 2009 | 11-50 | Provider of legal news portal |
| Canvera (canvera.com) | Bengaluru | 2007 | 51-200 | Photo-based products provider & photographers marketplace |
| Convosight (convosight.com) | Delhi | 2017 | 51-200 | Platform connecting creators with brands for content collaboration and monetization |

## Competitive set: “media” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Media & Entertainment" --filters.locations India --limit 20
radar find-competitors --market media --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Media & Entertainment"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "media", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Sports Companies in India](sports-companies-in-india.md)
- [Microfinance Companies in India](microfinance-companies-in-india.md)
- [3d Printing Companies in India](3d-printing-companies-in-india.md)
- [Erp Companies in India](erp-companies-in-india.md)
