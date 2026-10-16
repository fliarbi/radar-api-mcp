# Legal Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “legal companies in india” · 2,400/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [legal-companies-in-india.json](../../examples/use-cases/legal-companies-in-india.json).

**Question.** Which Legal companies are based in India, how large and how old are they, and who competes in the Legal market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Legal Services” |
| Companies returned (India, first page) | 20 |

## Legal companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Mindcrest (mindcrest.com) | Pune | 2001 | 201-500 | Provider of contract management and legal research & analytics services |
| Alaya Legal (alayalegal.com) | Delhi | 2003 | 11-50 | Provider of legal services in dispute resolution, corporate, and transactional matters |
| Constellation Blu (constellationblu.com) | Mumbai | 2012 | 11-50 | Provider of finance, accounting, and auditing services |
| FastInfo (fastinfo.com) | Kolkata | 2019 | 501-1000 | Provider of business incorporation, right to information and compliance legal services |
| Metayage IP Strategy Consulting (metayage.com) | Bengaluru | 2006 | 11-50 | Provider of intellectual property protection and strategy services |
| QuisLex (quislex.com) | Hyderabad | 2013 | 201-500 | Provider of financing and legal services |
| Accuprosys (accuprosys.com) | Hyderabad | 2008 | — | Provides application development, HR consulting, electrical maintenance, and digital marketing… |
| AZB & Partners (azbpartners.com) | Mumbai | 2004 | 201-500 | Provider of tax and legal advisory services |
| BananaIP (bananaip.com) | Bengaluru | 2003 | 11-50 | Provider of IP management, advisory and consulting services |
| CorpSeed (corpseed.com) | Noida | 2018 | 51-200 | Provider of regulatory, environmental, and business setup compliance services |
| Dhruva Advisors (dhruvaadvisors.com) | Mumbai | 2014 | 51-200 | Provider of tax and regulatory advisory services |
| ezyLegal (ezylegal.in) | Gurugram | 2021 | — | Provider of legal advisory services |
| King Stubb & Kasiva (ksandk.com) | Delhi | 2004 | 51-200 | Provider of full-service corporate legal services |
| Nishith Desai Associates (nishithdesai.com) | Mumbai | 1989 | 201-500 | Provider of strategic legal, regulatory, and tax advisory services |
| SciTech Patent Art (patent-art.com) | Hyderabad | 2002 | 51-200 | Provider of personal, business, and employee benefits insurance |
| Vahura (vahura.com) | Mumbai | 2007 | 51-200 | Provider of consulting and recruitment services to legal and business sector |
| Wider World Immigration (widerworld.in) | Delhi | 2019 | 11-50 | Provider of immigration services |
| WillJini (willjini.com) | Mumbai | 2014 | — | Provider of online will writing and estate succession planning services |
| Y-Axis (y-axis.com) | Hyderabad | 1999 | 501-1000 | Provider of immigration and visa consultancy services |
| EbizFiling (ebizfiling.com) | Ahmedabad | 2016 | 11-50 | Provides company reistration services |

## Competitive set: “legal” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Legal Services" --filters.locations India --limit 20
radar find-competitors --market legal --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Legal Services"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "legal", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Aerospace Companies in India](aerospace-companies-in-india.md)
- [Web Development Companies in India](web-development-companies-in-india.md)
- [Consulting Companies in India](consulting-companies-in-india.md)
- [Telecom Companies in India](telecom-companies-in-india.md)
