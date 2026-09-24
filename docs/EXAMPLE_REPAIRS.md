# Empty example review and smaller-company replacements

Reviewed every saved response capture on 2026-09-24, including selected company,
app and investor fields, scenarios, endpoint examples and contact fixtures.
The [complete audit](EXAMPLE_AUDIT.md) lists each file, date, status and whether
the requested data is populated. Capture timestamps remain individual; reviewing
all saved examples does not imply every source was queried again today.

## What changed

| Previous example | Current documented result | Interpretation |
|---|---|---|
| Microsoft annual income returned no periods | [electroCore FY2024](scenarios/14-annual-income.md): revenue, net income, EBITDA and EPS | Populated annual income, with news provenance and negative values preserved |
| Microsoft quarterly income | [electroCore quarterly income](scenarios/16-quarterly-income.md) | Two accessible quarters, each with revenue and EPS |
| Microsoft positive-profit screen returned no matches | [Qualys annual profit/revenue screen](scenarios/19-precise-profit-screen.md) | One match; the sample threshold explicitly changed from USD 1B to USD 100M |
| Microsoft/Python structured-skills job query returned no rows | [Connvertex Python role-title query](scenarios/39-company-skill-jobs.md) | Two records; a title search does not assert structured skill coverage |
| Razorpay/Swiggy product fields were empty | [Yext products](examples/additional/yext-products.json) below | Three actual source labels; original company-specific coverage cases retained |
| Razorpay activity field was absent | [Yext activity](examples/additional/yext-activity.json) below | Three stored dated activity rows, distinct from the recent timeline endpoint |
| Only large-company financial examples | [Mastech Digital annual income](examples/additional/mastech-annual-income.json) below | Revenue and net income with source provenance |

Original scenario requests and responses remain in each baseline. Sample changes
are labeled `sample_replacement`; they do not masquerade as fixes to identical
business predicates. The original under-$10,000 US AdTech request is preserved.

## Balance sheets and cash flow are still blocked

[Scenario 13](scenarios/13-balance-sheet.md) now uses electroCore rather than
Microsoft. It returns a FY2024 label but **no balance-sheet metrics**.
[Scenario 15](scenarios/15-annual-cash-flow.md) likewise contains no cash-flow metrics.
Both pages are clearly marked blocked coverage examples, not successful tutorials.

Strict read-only checks on 2026-09-24 found that the financial filings and
company-resolution stores failed on an unreachable shard (connection/socket
timeouts). Six live company probes returned news-derived income or no periods;
none returned official balance-sheet or cash-flow metrics. Available cached source
snapshots were expired and were not substituted into live responses. The upstream
can return HTTP 200 income-only data when its filing read fails. This is an
upstream observability gap: the response alone cannot distinguish a failed filing
read from a missing statement. The connection must be repaired and these exact
requests recaptured before claiming that those examples yield usable statements.
No database write, service restart or entitlement bypass was performed.

For a working annual-income request, use [scenario 14](scenarios/14-annual-income.md).
For balance sheets, require numeric `total_assets`, `total_liabilities` or
`stockholders_equity` in `periods[].metrics`; for cash flow, require a cash-flow
metric. Period labels, `has_data=true`, archive counts and company assessments are
not substitutes. A known zero or negative metric is still valid data.

## Other empty examples and the appropriate next step

| Coverage case | What to do |
|---|---|
| [US AdTech below USD 10K](scenarios/03-usa-adtech-under-10k.md) | Keep the original threshold; unknown annual evidence is not a match. Page through bounded candidates. [Scenario 04](scenarios/04-usa-adtech-over-1m.md) is a separately labeled positive screen. |
| [Indian seed USD 10K–100K shortlist](scenarios/11-seed-small-round.md) | The strict page excluded expanded candidates. Follow continuation when available; do not weaken country, stage or round filters silently. |
| [Normalized Shine internships](scenarios/38-normalized-interns.md) | No rows, including a broader internship-type recheck. Use the separate [internship corpus example](scenarios/41-remote-part-time-interns.md) for populated observed listings. |
| [Recent company events](reference/get_company_events.md) | The source account's effective window can be shorter than requested; a 365-day electroCore probe was also empty. Yext's stored activity field below is a distinct operation, not a replacement timeline. |
| Selected innovation fields | All three saved company examples are absent; a bounded native lookup found no positive patent-family row. No fabricated patent sample or stale snapshot was substituted. |
| [Founder professional lookup](examples/contacts/founder-professional.json) | The exact name-plus-company query was empty. [Contact guidance](CONTACTS.md) retains the populated separate lookup and conflicting source affiliations; it does not invent an identity match. |
| Location and News errors | Genuine upstream/coverage failures remain visible. Historical successful News captures retain dates and are not proof of current availability. |
| Contact denials and empty contact fixtures | Expected default-key scope denials and deliberately empty selected contact types; successful contact wire shapes are labeled synthetic fixtures. |

## Complete populated companion responses

These are actual authenticated gateway responses with every returned business row
retained. Identified source prose may be omitted under the same projection rules
as the endpoint reference; every omission and response hash is in the JSON file.
These endpoints require your configured base URL and API key. MCP uses the same
operation name with the JSON body in `arguments.request`.

### Yext: populated product names

The source returns three product names. These are the recorded labels, not independently verified current commercial offerings. This is a companion to the observed-empty Razorpay and Swiggy products captures; their company-specific files remain unchanged.

**POST `/v1/companies/field`** · MCP `get_company_field` · HTTP 200 · captured 2026-09-24T06:58:30.326479+00:00.

<!-- replacement-request: yext-products.json -->
```json
{
  "domain": "yext.com",
  "field": "products",
  "item_limit": 10
}
```

<!-- replacement-response: yext-products.json -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "yext.com",
    "company_id": "2l14u9i09o",
    "field": "products",
    "value": [
      "Yext Digital Experience Platform",
      "Yext Content Management System",
      "Yext Solutions"
    ],
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "products": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value": {
          "available": 3,
          "returned": 3,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-24T06:58:30.326326+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

[Full capture and provenance](examples/additional/yext-products.json).

### Yext: populated stored business activity

This selected activity field returns three dated source records: one event-marketing item and two product-launch items. It is a stored company field, not the account-limited recent timeline from get_company_events. The source's event associations have not been independently verified; the July marketing item in particular requires review before describing it as a Yext corporate event.

**POST `/v1/companies/field`** · MCP `get_company_field` · HTTP 200 · captured 2026-09-24T06:58:30.328110+00:00.

<!-- replacement-request: yext-activity.json -->
```json
{
  "domain": "yext.com",
  "field": "activity",
  "item_limit": 10
}
```

<!-- replacement-response: yext-activity.json -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "yext.com",
    "company_id": "2l14u9i09o",
    "field": "activity",
    "value": [
      {
        "d": "2026-07-02",
        "type": "event_marketing",
        "label": "Event",
        "detail": "Qdoba Live Walkthrough on Mexican food catering near me"
      },
      {
        "d": "2026-06-26",
        "type": "product_launch",
        "label": "Product launch",
        "detail": "Scout"
      },
      {
        "d": "2026-06-25",
        "type": "product_launch",
        "label": "Product launch",
        "detail": "Yext MCP"
      }
    ],
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "activity": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value": {
          "available": 3,
          "returned": 3,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-24T06:58:30.327979+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

[Full capture and provenance](examples/additional/yext-activity.json).

### Mastech Digital: a second populated annual income example

FY2025 revenue is USD 191,371,000 and net income is USD -609,000, with news_report provenance. Negative profit is retained. This smaller-company capture provides another real annual response; it does not establish filing-only, balance-sheet or cash-flow availability.

**POST `/v1/companies/financials`** · MCP `get_financials` · HTTP 200 · captured 2026-09-24T06:58:34.404631+00:00.

<!-- replacement-request: mastech-annual-income.json -->
```json
{
  "domain": "mastechdigital.com",
  "statement": "income",
  "period_type": "annual",
  "limit": 3
}
```

<!-- replacement-response: mastech-annual-income.json -->
```json
{
  "ok": true,
  "feature": "get_financials",
  "data": {
    "domain": "mastechdigital.com",
    "statement": "income",
    "has_data": true,
    "periods": [
      {
        "period": "FY2025",
        "fiscal_year": 2025,
        "fiscal_period": "FY",
        "period_end": null,
        "reported_date": "2026-02-19",
        "filed_date": null,
        "form_type": null,
        "metrics": {
          "net_income": {
            "value": -609000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          },
          "revenue": {
            "value": 191371000,
            "currency": "USD",
            "unit": "absolute",
            "source_type": "news_report",
            "native_value": null,
            "native_currency": null
          }
        },
        "article_ids": [
          "69bc45eedded76ae100ea280"
        ],
        "currency_conversion": null,
        "evidence": {
          "coverage_count": 1,
          "quality_signals": [
            "Reported a loss"
          ],
          "has_official": false,
          "period_has_official": false
        },
        "operating_context": {
          "employees": null,
          "revenue_growth_pct": -1.1,
          "net_income_growth_pct": -82.1,
          "guidance_revenue": null,
          "beat_or_miss": null
        }
      }
    ],
    "returned": 1,
    "truncated": false,
    "access_limited": true,
    "available_period_count": 17,
    "coverage": {
      "accessible_periods_before_filters": 3,
      "matching_periods": 1,
      "returned_periods_with_metrics": 1,
      "requested_metrics": [
        "ebitda",
        "eps",
        "gross_profit",
        "net_income",
        "operating_income",
        "revenue"
      ],
      "note": "Only entitled upstream periods are evaluated. A period can lack metrics for the selected statement; missing is not zero. Growth, guidance and evidence are source observations, not independently verified forecasts."
    },
    "computed_at": "2026-09-24T06:58:34.398000Z",
    "summary": {
      "narrative": "Latest reported FY2025: revenue $191.37M, net income $—. YoY -3.8% (0.96× prior period). Growth pattern is consistent across reported periods. Recent signals: Reported a loss, Profitable, Beat estimates.",
      "assessment": {
        "score": 53,
        "growth_consistency": 92,
        "yoy_pct": -3.8,
        "yoy_multiple": 0.96,
        "yoy_basis": "numeric",
        "quality_signals_aggregate": [
          "Reported a loss",
          "Profitable",
          "Beat estimates"
        ]
      },
      "comparison_periods": {
        "latest": {
          "period_label": "FY2025",
          "period_year": 2025,
          "period_qtr": "FY",
          "date": "2026-02-19"
        },
        "prior": {
          "period_label": "FY2024",
          "period_year": 2024,
          "period_qtr": "FY",
          "date": "2025-02-20"
        }
      },
      "source_coverage": {
        "bi_periods": 17,
        "currencies": [],
        "form_types": [],
        "fx_converted": false,
        "official_periods": 0
      },
      "note": "Summary assessments describe the upstream company window, not the filtered statement rows. Source coverage may count observations beyond the entitled archive. Guidance currency and horizon are not supplied; do not compare it with USD actuals without checking the article."
    }
  },
  "window": {
    "data_through": "2026-02-19"
  },
  "meta": {
    "retrieved_at": "2026-09-24T06:58:34.404471+00:00",
    "partial": false,
    "notes": [
      "Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
      "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies.",
      "The linked Radar account exposes only part of the financial archive."
    ],
    "provider": "Fliar BI"
  }
}
```

[Full capture and provenance](examples/additional/mastech-annual-income.json).

## Reproduce the review

In an operator-configured environment, `scripts/capture_example_replacements.py` recaptures the three companion examples. `scripts/stress_scenarios.py --round examples-20260924 --only 13-balance-sheet 14-annual-income 15-annual-cash-flow 16-quarterly-income 19-precise-profit-screen 39-company-skill-jobs` recaptures the six changed scenarios. Render with `scripts/build_example_repairs.py`, `scripts/build_scenario_docs.py` and `scripts/build_endpoint_docs.py`, then run `scripts/check_docs.py`. Raw captures and credentials remain ignored. The checker rejects empty positive samples, stale response hashes and rewritten baseline requests.
