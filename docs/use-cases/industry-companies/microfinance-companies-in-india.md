# Microfinance Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “microfinance companies in india” · 320/month India  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [microfinance-companies-in-india.json](../../examples/use-cases/microfinance-companies-in-india.json).

**Question.** Which Microfinance companies are based in India, how large and how old are they, and who competes in the Microfinance market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Microfinance” |
| Companies returned (India, first page) | 20 |
| Competitive set for “microfinance” (worldwide) | 41 |

## Microfinance companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Arohan (arohan.in) | Kolkata | 2006 | 10000+ | Non-banking financial company focuses on providing financial services to low-income individuals… |
| Saija (saija.in) | Patna | 2007 | 1-10 | Micro Loans in Bihar |
| Satin Creditcare (satincreditcare.com) | Gurugram | 1990 | 10000+ | NBFC offering micro loans to businesses |
| CreditAccess Grameen (creditaccessgrameen.in) | Bengaluru | 1999 | 10000+ | Provider of microcredit services |
| Muthoot Microfin (muthootmicrofin.com) | Ernakulam | 2010 | 10000+ | Provider of microfinance financial support and loans to low-income earning women entrepreneurs |
| Sonata Finance (sonataindia.com) | Lucknow | 2006 | 1001-5000 | Micro loans in UP and North India |
| Svatantra Microfinance (svatantramicrofin.com) | Mumbai | 2012 | 10000+ | Provider of microcredit services |
| Vedika Credit Capital (teamvedika.com) | Ranchi | 1995 | 1001-5000 | NBFC-MFI offering individual and group loan products |
| Ujjivan (ujjivan.com) | Bengaluru | 2005 | 10000+ | Financial services company primarily focused on serving the urban poor through microfinance and… |
| Annapurna Finance (annapurnafinance.in) | Bhubaneswar | 2009 | 10000+ | Provider of microfinance services for economic empowerment |
| Basix (basixindia.com) | Hyderabad | 1996 | 1-10 | Provider of financial, business, and institutional development services |
| Belstar (belstar.in) | Chennai | 1988 | 10000+ | Micro Loans for setting up of micro enterprises based on a SHG model |
| Bharat Financial Inclusion (bfil.co.in) | Secunderabad | 1997 | 10000+ | Provider of micro-credit & insurance for low income income individuals and women |
| Chaitanya India Fin Credit (chaitanyaindia.in) | Bengaluru | 2004 | 5001-10000 | Provider of micro-credit financing for low-income individuals and businesses |
| Mitrata Inclusive Financial Services (mitrata.in) | Gurugram | 1985 | 501-1000 | Provider of microfinance services |
| Satyamicrocapital (satyamicrocapital.com) | Delhi | 2016 | 5001-10000 | Microfinance operations |
| SHARE Microfin (sharemicrofin.com) | Hyderabad | 1999 | 1001-5000 | Micro Loans under joint liability group lending model |
| Svasti (svasti.in) | Chennai | 2010 | 1001-5000 | Microfinance Institution catering to the urban poor |
| Arman Financial Services (armanindia.com) | Ahmedabad | 1992 | 1001-5000 | Auto loans provider |
| Asirvad Microfinance (asirvadmicrofinance.co.in) | Chennai | 2009 | 10000+ | Provider of micro loans for consumers |

## Competitive set: “microfinance” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage. Countries: India 24, China 2, Mexico 2, Peru 2, Egypt 1, Indonesia 1.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |
| Public | CreditAccess Grameen | India | CreditAccess Grameen Limited is a leading Indian micro-finance institution headquartered in… |
| Public | Fusion Microfinance | Delhi | Fusion Microfinance is a New Delhi-based micro-lending startup aiming to provide underprivileged… |
| Public | Ujjivan | Bengaluru | Financial services company primarily focused on serving the urban poor through microfinance and… |
| Seed | Advans | Paris | Cooperative providing microcredit and savings for the low-income individuals |
| Seed | Digamber Finance | Jaipur | Provider of microfinance solutions |
| Seed | Vector Finance | Bhubaneswar | Provider of microcredit services |
| Series A | Financiera Confianza | San Isidro | Provider of micro credit services |
| Series A | Letshego | Gaborone | Provider of microfinance services |
| Series A | Midland Microfin | Jalandhar | Micro Loans in Punjab |
| Series B | Light Microfinance | Ahmedabad | Microloans for empowering small households |
| Series B | SV Creditline | Gurugram | Micro Loans in UP, MP and Rajasthan |
| Series B | Avanti | Bengaluru | Provider of financial services focused on livelihood advancement for underserved communities |
| Series C | Satyamicrocapital | Delhi | Microfinance operations |
| Series C | Pahal Financial Services | Ahmedabad | Provider of microfinance services to low-income households |
| Series C | Svasti | Chennai | Microfinance Institution catering to the urban poor |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Microfinance --filters.locations India --limit 20
radar find-competitors --market microfinance --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Microfinance"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "microfinance", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Hotel Companies in India](hotel-companies-in-india.md)
- [Sports Companies in India](sports-companies-in-india.md)
- [Media Companies in India](media-companies-in-india.md)
- [3d Printing Companies in India](3d-printing-companies-in-india.md)
