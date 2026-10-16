# Fintech Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “fintech companies in india” · 3,600/month India · 50/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [fintech-companies-in-india.json](../../examples/use-cases/fintech-companies-in-india.json).

**Question.** Which Fintech companies are based in India, how large and how old are they, and who competes in the Fintech market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “FinTech” |
| Companies returned (India, first page) | 20 |

## Fintech companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Groww (groww.in) | Bengaluru | 2016 | 201-500 | Provider of an online platform for investments and trading services |
| BankBazaar (bankbazaar.com) | Chennai | 2008 | 501-1000 | Online platform providing tools for comparing and applying for financial products |
| BharatPe (bharatpe.com) | Gurugram | 2018 | 501-1000 | Provider of payment solutions, lending, and investment opportunities for businesses |
| C2L BIZ (c2lbiz.com) | Mumbai | 2007 | 201-500 | Software suite for the insurance industry |
| Clari5 (clari5.com) | Bengaluru | 2006 | 51-200 | Provider of financial crime management and fraud prevention technology solutions |
| CredFlow (credflow.in) | Noida | 2019 | 51-200 | Comprehensive cash flow management platform for small and medium-sized enterprises |
| Credit Fair (creditfair.in) | Mumbai | 2018 | 51-200 | Platform offering solar financing solutions |
| CRIF (crifhighmark.com) | Mumbai | 2005 | 51-200 | Provider of a credit scoring solution for businesses |
| Cybrilla (cybrilla.com) | Bengaluru | 2010 | 11-50 | Provider of technology solutions streamlining mutual fund transactions and distribution |
| DemandFarm (demandfarm.com) | Bengaluru | 2012 | 51-200 | Provider of Key account management software tool to make strategic account planning data driven,… |
| Easy Home Finance (easyhomefinance.in) | Mumbai | 2017 | 501-1000 | Provider of home loans and refinancing options |
| Eduvanz (eduvanz.com) | Mumbai | 2016 | 51-200 | Provider of financial assistance for education, career, and skills development |
| Fable Fintech (fablefintech.com) | Mumbai | 1999 | 51-200 | Provider of end-to-end cross border payment solutions for businesses |
| Fino Paytech (finopaytech.com) | Mumbai | 2006 | 11-50 | Provider of technology solutions and services for banking and financial sectors |
| FundsIndia (fundsindia.com) | Chennai | 2008 | 201-500 | Online investment platform for mutual funds and other financial products |
| Kosh (getkosh.com) | Gurugram | 2019 | 51-200 | Provider of community finance products and joint liability loans for businesses |
| Simpl (getsimpl.com) | Bengaluru | 2015 | 51-200 | Provider of an online marketplace platform for purchase financing |
| GyanDhan (gyandhan.com) | Delhi | 2015 | 51-200 | Provider of education loan marketplace and study abroad admission support |
| HostBooks (hostbooks.com) | Gurugram | 2009 | 201-500 | Provider of agentic AI-powered ERP solutions for diverse industries |
| i-exceed (i-exceed.com) | Bengaluru | 2011 | 201-500 | Developer of digital banking platform offering solutions for financial institutions |

## Competitive set: “fintech” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries FinTech --filters.locations India --limit 20
radar find-competitors --market fintech --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["FinTech"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "fintech", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [FMCG Companies in India](fmcg-companies-in-india.md)
- [App Development Companies in India](app-development-companies-in-india.md)
- [Venture Capital Companies in India](venture-capital-companies-in-india.md)
- [Logistics Companies in India](logistics-companies-in-india.md)
