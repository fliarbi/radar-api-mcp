# Insurance Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “insurance companies in india” · 8,100/month India · 140/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [insurance-companies-in-india.json](../../examples/use-cases/insurance-companies-in-india.json).

**Question.** Which Insurance companies are based in India, how large and how old are they, and who competes in the Insurance market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Insurance” |
| Companies returned (India, first page) | 20 |

## Insurance companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| Star Health and Allied Insurance (starhealth.in) | Chennai | 2006 | 10000+ | Provider of health insurance services |
| C2L BIZ (c2lbiz.com) | Mumbai | 2007 | 201-500 | Software suite for the insurance industry |
| CarIQ (mycariq.com) | Pune | 2013 | 501-1000 | Saas-based platform for vehicle diagnostics solutions |
| ACKO (acko.com) | Bengaluru | 2016 | 1001-5000 | Provider of car, bike, health, life, and travel insurance policies |
| Assurekit (assurekit.com) | Mumbai | 2019 | 11-50 | Insurance processing and distribution management solution for the insurance industry |
| Digit Insurance (godigit.com) | Bengaluru | 2016 | 501-1000 | Provider of general and life insurance products across various categories |
| IndiaFirst Life (indiafirstlife.com) | Mumbai | 2009 | 1001-5000 | Provider of life & health insurance services to individuals and families |
| Infinity Assurance Solutions (infinityassurance.com) | Delhi | 2013 | 11-50 | Warranty Management Service provider |
| InsuringIndia (insuringindia.com) | Mumbai | 2010 | 11-50 | Online insurance aggregator for individuals |
| Medi Assist (mediassist.in) | Bengaluru | 2002 | 51-200 | Provider of benefits administration, international private medical insurance, and self-funded plans |
| Niva Bupa (nivabupa.com) | Delhi | 2008 | 10000+ | Online platform offering multiple insurance service |
| QuickInsure (quickinsure.co.in) | Pune | 2016 | 51-200 | Provider of platform to compare and buy insurance policies online |
| Remedinet Technologies (remedinet.com) | Bengaluru | 2006 | 51-200 | Provider of healthcare payer-provider network solutions |
| Toffee (toffeeinsurance.com) | Gurugram | 2017 | 11-50 | Online platform for health and property and casualty insurances |
| Vidal Healthcare (vidalhealthtpa.com) | Bengaluru | 2010 | 51-200 | Provider of third-party administrator services for health insurance |
| Alliance (allianceinsurance.in) | Mumbai | 2003 | 201-500 | Provider of insurance brokerage services |
| Beacon (beacon.co.in) | Vadodara | 2005 | 501-1000 | Provider of insurance broking services for direct and reinsurance business |
| Coverfox Insurance (coverfox.com) | Mumbai | 2013 | 51-200 | Provider of platform to compare and purchase various insurance policies online |
| Easypolicy (easypolicy.com) | Noida | 2011 | 1-10 | Online comparison platform for life and non-life insurance |
| ENSUREDIT (ensuredit.com) | Bengaluru | 2019 | 51-200 | Provider of insurance technology solutions for digital distribution and analytics |

## Competitive set: “insurance” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Insurance --filters.locations India --limit 20
radar find-competitors --market insurance --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Insurance"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "insurance", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Pharmaceutical Companies in India](pharmaceutical-companies-in-india.md)
- [It Companies in India](it-companies-in-india.md)
- [FMCG Companies in India](fmcg-companies-in-india.md)
- [App Development Companies in India](app-development-companies-in-india.md)
