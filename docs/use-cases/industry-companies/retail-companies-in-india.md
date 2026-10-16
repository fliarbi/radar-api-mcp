# Retail Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “retail companies in india” · 880/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [retail-companies-in-india.json](../../examples/use-cases/retail-companies-in-india.json).

**Question.** Which Retail companies are based in India, how large and how old are they, and who competes in the Retail market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Retail” |
| Companies returned (India, first page) | 20 |

## Retail companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| FirstCry (firstcry.com) | Pune | 2010 | 5001-10000 | Online retailer offering a range of baby, kids, and maternity products |
| Holisol (holisollogistics.com) | Delhi | 2009 | 1001-5000 | Platform offering end-to-end supply chain, fulfilment, and IT solutions |
| IndiaMART (indiamart.com) | Noida | 1999 | 1001-5000 | B2B marketplace platform connecting buyers and suppliers offering diverse industrial products |
| W (wforwoman.com) | Delhi | 2003 | 1001-5000 | Designer and retailer of womens fusion wear |
| 6Degree (6degree.co) | Bengaluru | 2014 | 51-200 | Growth enablement platform providing end-to-end e-commerce solutions |
| AapkaPainter (aapkapainter.com) | Bengaluru | 2012 | 51-200 | Online closed marketplace for booking painting services |
| Aibono (aibono.com) | Bengaluru | 2014 | 51-200 | Provider of AI-powered fresh food aggregator platform |
| Arzooo (arzooo.com) | Bengaluru | 2016 | 51-200 | Provider of a technology platform for retail business management and growth |
| Baazar Kolkata (baazarkolkata.com) | Kolkata | 2002 | 1001-5000 | Large format fashion and accessories retailer. |
| BabyChakra (babychakra.com) | Mumbai | 2014 | 11-50 | Online parenting platform for pregnancy and childcare |
| Baby Destination (babydestination.com) | Delhi | 2017 | 1-10 | Provider of a community platform with content and support for mothers |
| BlueStone (bluestone.com) | Bengaluru | 2011 | 1001-5000 | Retailer of gold diamond platinum and gemstone jewellery and coins |
| Bombay Shaving (bombayshavingcompany.com) | Gurugram | 2015 | 51-200 | Online brand offering grooming and personal care products for mens |
| Browntape (browntape.com) | Aradi Socorro | 2012 | 11-50 | Provider of eCommerce software solution for Amazon and Flipkart sellers |
| Cafe Coffee Day (cafecoffeeday.com) | Bengaluru | 1993 | 1001-5000 | Restaurant chain serving coffee |
| Candere (candere.com) | Mumbai | 2012 | 51-200 | Online retailer of gold and diamond jewellery for various occasions |
| ConvertCart (convertcart.com) | Bengaluru | 2013 | 51-200 | eCommerce platform provider enhancing conversion rates and email marketing revenue |
| Craftsvilla (craftsvilla.com) | Mumbai | 2011 | 11-50 | Online marketplace offering multi-category consumer products |
| Crofarm (crofarm.com) | Gurugram | 2016 | 201-500 | B2B supply chain for fresh farm produce |
| CustomFurnish (customfurnish.com) | Hyderabad | 2013 | 51-200 | Provider of customized home interior design and modular furniture solutions |

## Competitive set: “retail” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries Retail --filters.locations India --limit 20
radar find-competitors --market retail --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Retail"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "retail", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Cloud Companies in India](cloud-companies-in-india.md)
- [Furniture Companies in India](furniture-companies-in-india.md)
- [SAAS Companies in India](saas-companies-in-india.md)
- [Fashion Companies in India](fashion-companies-in-india.md)
