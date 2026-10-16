# Digital Marketing Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “digital marketing companies in india” · 9,900/month India · 590/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [digital-marketing-companies-in-india.json](../../examples/use-cases/digital-marketing-companies-in-india.json).

**Question.** Which Digital Marketing companies are based in India, how large and how old are they, and who competes in the Digital Marketing market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Digital Marketing” |
| Companies returned (India, first page) | 20 |

## Digital Marketing companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Digital Vidya (digitalvidya.com) | Delhi | 2009 | 1-10 | Provider of professional training and certification programs in digital marketing. |
| RepUp (repup.co) | Gurugram | 2012 | 11-50 | Web based reputation and guest experience data management platform for hotels |
| Digiperform (digiperform.com) | Delhi | 2014 | 11-50 | Chains providing digital marketing and data science training courses |
| Kraftshala (kraftshala.com) | Delhi | 2016 | 11-50 | Online courses in sales and marketing for graduates and professionals |
| BizzO (bizzo.in) | Mumbai | 2017 | 11-50 | SaaS-driven white-label apps to digitalize travel, tourism & hospitality industries |
| IIDE (iide.co) | Mumbai | 2016 | 51-200 | Provider of digital marketing and AI education |
| Digiaccel (digiaccel.in) | Gurugram | 2021 | 11-50 | Online platform offering digital marketing and e-commerce courses |
| Digitalacademy360 (digitalacademy360.com) | Bengaluru | 2015 | 201-500 | Provider of online and offline digital marketing training programs |
| Delhi School of Internet Marketing (dsim.in) | Delhi | 2011 | 1-10 | Training provider for digital marketing |
| ThinkWhy (thinkwhy.co) | Ahmedabad | 2016 | 11-50 | Provider of e-commerce support services |
| Uppskill (uppskill.com) | Noida | 2017 | 1-10 | Provider of online digital marketing training programs |
| Brance (brance.ai) | Delhi | 2022 | — | AI-powered chatbot service platform |
| NuvoRetail (nuvoretail.com) | Delhi | 2017 | 51-200 | Provider of ecommerce management services |
| Digital Academy India (digitalacademyindia.com) | Delhi | 2012 | — | Online training programs on digital marketing |
| Xpert (xpert.chat) | Kolkata | 2007 | — | Platform offering AI-driven brands marketing |
| Aapka Apna Bazar (aapkaapnabazar.com) | Mumbai | 2020 | — | Provider of advertising services |
| eZee iFeedback (ezeeifeedback.com) | Surat | 2004 | 201-500 | Guest feedback management software |
| Allindia (allindia.com) | Kolkata | 1996 | 51-200 | Communication agency offering digital marketing services for brands |
| IIOL (iiol.online) | Aligarh | 2024 | — | Provider of online digital marketing course |
| Rankkeywords (rankkeywords.com) | — | 2017 | — | Provider of digital marketing and website development services |

## Competitive set: “digital marketing” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Digital Marketing" --filters.locations India --limit 20
radar find-competitors --market "digital marketing" --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Digital Marketing"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "digital marketing", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Automotive Companies in India](automotive-companies-in-india.md)
- [AI Companies in India](ai-companies-in-india.md)
- [Pharmaceutical Companies in India](pharmaceutical-companies-in-india.md)
- [It Companies in India](it-companies-in-india.md)
