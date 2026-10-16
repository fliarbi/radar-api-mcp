# Nykaa Revenue: Radar API example with live data

[Company financials research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “nykaa revenue” · 390/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [nykaa-revenue.json](../../examples/use-cases/nykaa-revenue.json).

**Question.** What revenue and profit has Nykaa reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?

## At a glance

| Measure | Value |
| --- | ---: |
| Company domain | `nykaa.com` |
| Fiscal periods with figures | 20 |
| Summary | Latest reported Q3 FY2026: revenue $344.79M, net income $7.6M, EPS $0.22. YoY +26.7% (1.27× prior period). Growth has been erratic across reported periods.… |
| Recorded funding events | 10 |

## Reported figures by fiscal period

`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.

| Period | Revenue | Net income | EBITDA | Operating income | Source |
| --- | ---: | ---: | ---: | ---: | --- |
| Q3 FY2026 | $344.8M | $7.6M | $27.6M | $13.2M | news report |
| Q2 FY2026 | $2.8B ⚠ | $4.1M | $19M | $19M | news report |
| Q1 FY2026 | $258.6M | $2.9M | — | $16.9M | news report |
| Q4 FY2025 | $247.4M | $1.9M | $16M | — | news report |
| Q3 FY2025 | $272M | $3.2M | $16.9M | — | news report |
| Q2 FY2025 | $228.2M | $3.3M | $14M | — | news report |
| Q1 FY2025 | $258.6M | $2.9M | — | — | news report |
| FY2025 | $954M | $8.6M | $56.9M | — | news report |

“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.

⚠ marks a figure more than eight times this company's typical value for that metric, usually a unit or currency slip in the source report. Verify it before use.

## Recorded funding events

`get_company_funding`; amounts are reported figures (approximate).

| Date | Round | Amount (USD) | Evidence |
| --- | --- | ---: | --- |
| 2024-07-24 | Debt | $15M | Nykaa, a marketplace for beauty and personal care products, has announced its plan to raise Rs 125 crore through non-convertible… |
| 2021-10-26 | Initial Public Offering | $287.5M | FSN E-Commerce Ventures Ltd, which runs online marketplace for beauty and wellness products Nykaa, on Wednesday said it has raised Rs… |
| 2020-11-26 | Primary | $19.9M | Earlier this year, in March, the company had also raised Rs 166 crore from Steadview Capital through a primary transaction, which led to a… |
| 2020-05-09 | Funding round | $8M | Mumbai-based Nykaa has raised INR 67 Cr from its existing investor Asia-focused hedge fund Steadview Capital. |
| 2020-01-13 | Fresh Round | $12M | beauty e-tailer Nykaa raised Rs 100 crore in a fresh round of funding from US-based private equity firm TPG Growth. |
| 2019-04-01 | Funding round | $14.4M | Online beauty brand Nykaa has raised $14.4 million from private equity firm TPG Growth Capital. |
| 2018-10-29 | Funding round | $13.6M | In September, VCCircle reported that the fund inked its second deal, investing Rs 113 crore to acquire a stake in beauty retailer Nykaa… |
| 2018-07-06 | Equity | $24.4M | The company, which owns 33% of the online beauty market, raised $24.45 Mn (INR 165 Cr) in a Series D funding. |
| 2018-04-23 | Funding round | $12M | The company has earlier raised capital in 2016, when it received a fund infusion to the tune of Rs. 100 crore from Max Ventures and… |
| 2017-09-29 | Series B | $9.5M | India’s fastest growing online beauty and wellness retailer, Nykaa.com, has recently announced the completion of US$ 9.5 million equity… |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-financials --domain nykaa.com --statement all --period-type all --limit 8
radar get-company-funding --domain nykaa.com
radar news-overview --company nykaa.com --date-from 2026-01-01 --date-to 2026-04-30
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "nykaa.com", "statement": "all", "period_type": "all", "limit": 8}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/funding", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "nykaa.com"}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`get_company_funding`, `get_financials`, `news_overview`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.
- EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies.
- Part of the news index is temporarily offline; this answer uses about 86% of indexed articles, so counts are lower bounds.
- Article filters require a matching source article in the same window; records without a matching article are excluded. Each deal still counts once.
- Dates refer to source publication dates, not necessarily the date an event or deal occurred.
- News, events and funding are separate populations and must not be added together. Topic search checks article text for news, event descriptions for events and deal descriptions for funding; an explicit match mode uses source articles.

## Related use cases

- [Freshworks Revenue](freshworks-revenue.md)
- [Delhivery Revenue](delhivery-revenue.md)
- [Country Delight Revenue](country-delight-revenue.md)
- [Licious Revenue](licious-revenue.md)
