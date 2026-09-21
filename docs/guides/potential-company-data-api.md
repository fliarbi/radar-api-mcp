# Company potential data API: growth signals, investment research and B2B sales prospects

Use company potential data to build an explainable shortlist for investment
research or B2B sales prospecting. Radar combines company filters with measured
financial, funding, hiring, technology and mobile-app evidence. Every screen has
visible criteria; its result is a research candidate, not a purchase probability,
fundraising mandate or prediction of investment returns.

## Choose an explicit opportunity screen

`POST /v1/companies/opportunities/presets` / `opportunity_presets` accepts `{}`.

| Preset | What selects a company | Suggested research use |
|---|---|---|
| high_growth | Scaling Super Fast or Aggressively Scaling source labels | Check financial periods, team size and hiring to investigate expansion |
| profitable_growth | Profitable and growing revenue source bands | Inspect profitability and cash flow across dated statements |
| early_stage | Under-five-year age band and Seed stage | Research young companies and their investors; verify latest round dates |
| hiring_expansion | Recorded hiring with at least one role in a 90-day window | Prioritize recruiting, training or related B2B account research |
| technology_modernization | Aggressively Scaling plus PHP/MySQL technology filters | Study stack/service fit; these technologies do not imply technical problems |
| mobile_scale | At least one million aggregate mobile downloads | Research mobile products, app performance and related services |

The catalog returns exact filter values, default sort, requested evidence columns
and an interpretation for each preset. Multi-value filters retain Radar's source
matching behavior; they are not a hidden scoring model.

`POST /v1/companies/opportunities/search` / `search_opportunities`:

```json
{"preset":"mobile_scale","filters":{"locations":["India"],"markets":["Payments"]},"limit":2,"page":0}
```

You can add typed company filters and choose a sort, but cannot replace a preset's
defining criteria. Pages contain at most 20 candidates so that supporting evidence
remains bounded. effective_filters records what was submitted to Radar. Read
access.restricted_filters, access plan and matching metadata as well: the source
can restrict a requested filter or relax a match. Do not interpret submitted
criteria as independent proof that every returned company satisfies them.

## Retrieve the evidence needed for your decision

For growth or investment research, start with a candidate domain, request a compact
company profile, then select the needed financial, funding, founders, investors,
hiring, technology, traffic or app fields. Financial responses preserve periods,
currency and provenance. Investor detail adds portfolio and co-investor context.
News and company events add dated evidence without replacing the measured figures.

For sales prospects, use recorded hiring demand, app scale or a specific technology
as reasons to investigate account fit. Add geography, sector, employee band or
other accepted company filters. Read a job's actual skills and a company's detailed
technology fields before assuming it needs your service. Contact retrieval is a
separate request with explicit contacts scope and paid linked Radar access; the
opportunity search neither reveals private contact values nor sends outreach.

The captured mobile-scale search returns Paytm and Paisabazaar with aggregate app
download display values of 825.0M and 30.0M and app-growth values 15 and 24. Those
columns can come from different observations than individual app records. Follow
company_apps and get_app_field for dates and calculation inputs. Employee values
were null in this capture and remain null in the example.

Additional live examples cover [profitable growth and hiring-based prospects](../POTENTIAL_DATA_EXAMPLES.md).
The hiring preset accepts added nested role/city filters, for example a hiring
roles list containing engineer, while retaining is_hiring=true, min_open_roles=1
and recency_days=90. These defining values remain visible in effective_filters.
Changing them through an extra filter is rejected.

## Handle partial evidence and charges

A result contains candidate cards plus evidence rows keyed by domain. Missing
columns remain null; failed evidence retrieval sets coverage.partial and
meta.partial instead of inventing numbers. Display columns can suppress zero or
negative source values. Retrieve detailed financials before interpreting a blank
cell as no revenue, no loss or no activity.

One successful search costs one credit in account mode, including its bounded
evidence lookup. It uses companies scope and shares rate, concurrency and spending
limits with other REST/MCP calls. Individual follow-up detail requests are separate
operations. Unavailable evidence, source access gates and snapshot dates remain
part of the client-visible result.

See [preset reference](../reference/opportunity_presets.md), [financial data](financial-data-api.md),
[app data](apps-data-api.md), [hiring signals](hiring-signals-jobs-api.md),
[company filters](../FILTERS_AND_LISTINGS.md) and [contact access](../CONTACTS.md).

<!-- captured-workflow -->
## Follow the company shortlist to its supporting evidence

The worked screen combines Payments, India and a million-install minimum. It returns Paytm and Paisabazaar alongside measured display columns. For investment research, verify financial periods and app observations. For sales prospecting, use those same signals to prioritize research while keeping budget and purchase intent unknown until separately established.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/opportunities/search`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: search_opportunities -->
```json
{
  "preset": "mobile_scale",
  "filters": {
    "locations": [
      "India"
    ],
    "markets": [
      "Payments"
    ]
  },
  "limit": 2
}
```

<!-- response-example: search_opportunities -->
```json
{
  "ok": true,
  "feature": "search_opportunities",
  "data": {
    "companies": [
      {
        "founded": "2000",
        "tagline": "Digital payment platform offering financial services, recharges and more",
        "size": "10000+",
        "company_id": "1lnxl8v10w",
        "hq": "noida",
        "has_phone": false,
        "has_email": false,
        "description": "Digital payment platform offering financial services, recharges and more",
        "location": {
          "c": "india",
          "rg": "uttar pradesh",
          "l": "noida",
          "lc": "noida, uttar pradesh, india",
          "hq": "noida",
          "cc": "in",
          "coord": [
            77.33,
            28.58
          ],
          "g": "28.58,77.33"
        },
        "flags": [],
        "linkedin_slug": "paytm-mobile-solutions-pvt-ltd-",
        "name": "Paytm",
        "slug": "paytm",
        "domain": "paytm.com",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=paytm.com"
      },
      {
        "founded": "2014",
        "tagline": "Online financial marketplace that offers a range of personal loan and credit card options to consumers",
        "size": "5001-10000",
        "company_id": "2inawol0hl",
        "hq": "gurugram",
        "has_phone": false,
        "has_email": false,
        "description": "Online financial marketplace that offers a range of personal loan and credit card options to consumers",
        "location": {
          "c": "india",
          "rg": "haryana",
          "l": "gurugram",
          "lc": "gurugram, haryana, india",
          "hq": "gurugram",
          "cc": "in",
          "coord": [
            77.02635,
            28.4601
          ],
          "g": "28.4601,77.02635"
        },
        "flags": [
          [
            "Large Enterprise",
            "size"
          ]
        ],
        "linkedin_slug": "paisabazaar",
        "name": "Paisabazaar",
        "slug": "paisabazaar",
        "domain": "paisabazaar.com",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=paisabazaar.com"
      }
    ],
    "page": 0,
    "requested_limit": 2,
    "returned": 2,
    "total": null,
    "access": {
      "plan": "free",
      "results_capped": false,
      "searches_remaining": 50
    },
    "partial_timeout": false,
    "matching": {},
    "pagination": "Increment page; account caps can apply. No total is inferred from a page.",
    "preset": "mobile_scale",
    "effective_filters": {
      "markets": [
        "Payments"
      ],
      "locations": [
        "India"
      ],
      "mobile_downloads": [
        "1m+"
      ]
    },
    "sort_by": "employees",
    "evidence": [
      {
        "domain": "paytm.com",
        "columns": {
          "mobile_downloads": {
            "label": "App Downloads",
            "value": "825.0M"
          },
          "mobile_growth": {
            "label": "App Growth %",
            "value": "15"
          },
          "employees": null
        },
        "status": "available"
      },
      {
        "domain": "paisabazaar.com",
        "columns": {
          "mobile_downloads": {
            "label": "App Downloads",
            "value": "30.0M"
          },
          "mobile_growth": {
            "label": "App Growth %",
            "value": "24"
          },
          "employees": null
        },
        "status": "available"
      }
    ],
    "interpretation": "Historical cumulative install bands; inspect individual apps and observation dates before estimating momentum.",
    "coverage": {
      "partial": false,
      "evidence_available": true
    },
    "note": "These are source-filtered candidates, not verified opportunities. Inspect access/restricted_filters and matching metadata; display columns may suppress zero or negative values. Retrieve exact financials and detail fields separately."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T10:48:29.878400+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T10:48:29.878570+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_opportunities.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The India/Payments/mobile_scale capture returns Paytm and Paisabazaar. Recorded aggregate app-download values are 825.0M and 30.0M, with app growth display values 15 and 24. Employee values are null rather than invented.

See the [complete search_opportunities endpoint reference](../reference/search_opportunities.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 66 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
