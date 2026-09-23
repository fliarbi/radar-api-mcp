# Company intelligence API: scores, risks and business context

[All endpoints](README.md) · [Workflow guide](../guides/competitor-intelligence-api.md)

Retrieve Radar's computed view of a company's market position, innovation, management signals, financial trajectory, risk and investment readiness. This endpoint is useful for deciding which evidence to investigate next. Its scores and narratives are derived assessments and should remain separate from financial statement facts.

## Route, authentication and credits

**`POST /v1/companies/intelligence`** · MCP tool **`get_company_intelligence`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/intelligence" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_intelligence -->
```json
{
  "name": "get_company_intelligence",
  "arguments": {
    "request": {
      "domain": "microsoft.com"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_company_intelligence -->
```json
{
  "ok": true,
  "feature": "get_company_intelligence",
  "data": {
    "domain": "microsoft.com",
    "intel": {
      "company_meta": {
        "country": "united states",
        "current_stage": "Unfunded",
        "estimated_revenue": null,
        "progress_label": "",
        "size_label": "",
        "markets": [
          "business intelligence"
        ],
        "total_funding": null,
        "valuation": null
      },
      "computed_at": "2026-09-23T03:22:51Z",
      "earnings": {
        "balance_sheet": null,
        "estimated_revenue_usd": null,
        "gated": true,
        "growth_consistency": 22,
        "has_data": true,
        "history": [
          {
            "beat_or_miss": "Beat",
            "cash_usd": null,
            "coverage_count": 4,
            "currency_native": "",
            "date": "2026-04-29",
            "ebitda_usd": null,
            "employees": null,
            "eps": 4.27,
            "article_id": "69e99ba475f157062cafcd91",
            "metric_sources": {
              "eps": "news_report",
              "net_income_usd": "news_report",
              "operating_income_usd": "news_report",
              "revenue_usd": "news_report"
            },
            "filed_date": null,
            "form_type": "",
            "fx_source": "",
            "gross_profit_usd": null,
            "guidance_revenue": 81296200000,
            "has_official": false,
            "long_term_debt_usd": null,
            "native": {},
            "net_income_growth_pct": 23.0,
            "net_income_usd": 31800000000,
            "operating_cash_flow_usd": null,
            "operating_income_usd": 38400000000,
            "period_has_official": false,
            "period_label": "Q3 FY2026",
            "period_qtr": "Q3",
            "period_sort": 20263,
            "period_year": 2026,
            "source_type": "news_report",
            "quality_signals": [
              "Beat estimates",
              "Profitable"
            ],
            "revenue_growth_pct": 18.0,
            "revenue_usd": 82890000000,
            "article_ids": [
              "69e99ba475f157062cafcd91",
              "69f87f9d43843dd771ce0936",
              "69f8a61b43843dd771d24172",
              "69f9d902713680636eef61bb"
            ],
            "stockholders_equity_usd": null,
            "total_assets_usd": null,
            "total_liabilities_usd": null
          },
          {
            "beat_or_miss": "Beat",
            "cash_usd": null,
            "coverage_count": 15,
            "currency_native": "",
            "date": "2026-01-29",
            "ebitda_usd": null,
            "employees": null,
            "eps": 3.23,
            "article_id": "67b306a368916ca487deb3b6",
            "metric_sources": {
              "eps": "news_report",
              "net_income_usd": "news_report",
              "operating_income_usd": "news_report",
              "revenue_usd": "news_report"
            },
            "filed_date": null,
            "form_type": "",
            "fx_source": "",
            "gross_profit_usd": null,
            "guidance_revenue": 73790000000,
            "has_official": false,
            "headline": "The company reported net income for the quarter of $24.1 billion, or $3.23 per share, beating Wall Street expectations of $3.11 per share.",
            "long_term_debt_usd": null,
            "native": {},
            "net_income_growth_pct": 10.0,
            "net_income_usd": 24100000000,
            "operating_cash_flow_usd": null,
            "operating_income_usd": 34300000000,
            "period_has_official": false,
            "period_label": "Q4 FY2025",
            "period_qtr": "Q4",
            "period_sort": 20254,
            "period_year": 2025,
            "source_type": "news_report",
            "quality_signals": [
              "Beat estimates",
              "Profitable"
            ],
            "revenue_growth_pct": 12.0,
            "revenue_usd": 69600000000,
            "article_ids": [
              "67b306a368916ca487deb3b6",
              "6898cd8a2f01d48cd3008d26",
              "68a176573ff75e010c29decf",
              "68a176633ff75e010c2cc764",
              "68d0eb54b4da52a1072b8017",
              "6986b9749438ce100b18811d",
              "6988ab058fb0ea95e97759ff",
              "69bb154def75d924655a684d",
              "69c9c4daeff444794ed8070e",
              "69dfb1fef2a6294de7f764a0",
              "69dfb24286bd23245a9134fc",
              "69dfb6f5c1e955063e150b93",
              "69dfb7893dd0a4354393b0fa",
              "69e886f27bb1410d4c8b1893",
              "69efabfa727212302c5ff193"
            ],
            "stockholders_equity_usd": null,
            "total_assets_usd": null,
            "total_liabilities_usd": null
          },
          {
            "beat_or_miss": "Beat",
            "cash_usd": null,
            "coverage_count": 8,
            "currency_native": "",
            "date": "2025-12-31",
            "ebitda_usd": null,
            "employees": null,
            "eps": 5.16,
            "article_id": "6988a7773757765ee826377c",
            "metric_sources": {
              "eps": "news_report",
              "operating_income_usd": "news_report",
              "revenue_usd": "news_report"
            },
            "filed_date": null,
            "form_type": "",
            "fx_source": "",
            "gross_profit_usd": null,
            "guidance_revenue": 80230000000,
            "has_official": false,
            "headline": "The Zacks Consensus Estimate for revenues is pegged at $80.23 billion, indicating growth of 15.22% from the figure reported in the year-ago quarter.",
            "long_term_debt_usd": null,
            "native": {},
            "net_income_growth_pct": 20.12,
            "net_income_usd": null,
            "operating_cash_flow_usd": null,
            "operating_income_usd": 38300000000,
            "period_has_official": false,
            "period_label": "Q2 FY2026",
            "period_qtr": "Q2",
            "period_sort": 20262,
            "period_year": 2026,
            "source_type": "news_report",
            "quality_signals": [
              "Beat estimates"
            ],
            "revenue_growth_pct": 15.22,
            "revenue_usd": 77670000000,
            "article_ids": [
              "6988a7773757765ee826377c",
              "698e37498d29a990b6e524d5",
              "69bbe6aba75fc0dcb02055d5",
              "69bce327a7b1648247b810ef",
              "69c42f5b7c4635ab38e80104",
              "69cc188adcf7c26bbed60f05",
              "69dfb24286bd23245a9134fc",
              "69dfb6f5c1e955063e150b93"
            ],
            "stockholders_equity_usd": null,
            "total_assets_usd": null,
            "total_liabilities_usd": null
          }
        ],
        "history_public_count": 3,
        "history_total_count": 20,
        "latest": {
          "beat_or_miss": "Beat",
          "cash_usd": null,
          "coverage_count": 4,
          "currency_native": "",
          "date": "2026-04-29",
          "ebitda_usd": null,
          "employees": null,
          "eps": 4.27,
          "article_id": "69e99ba475f157062cafcd91",
          "metric_sources": {
            "eps": "news_report",
            "net_income_usd": "news_report",
            "operating_income_usd": "news_report",
            "revenue_usd": "news_report"
          },
          "filed_date": null,
          "form_type": "",
          "fx_source": "",
          "gross_profit_usd": null,
          "guidance_revenue": 81296200000,
          "has_official": false,
          "long_term_debt_usd": null,
          "native": {},
          "net_income_growth_pct": 23.0,
          "net_income_usd": 31800000000,
          "operating_cash_flow_usd": null,
          "operating_income_usd": 38400000000,
          "period_has_official": false,
          "period_label": "Q3 FY2026",
          "period_qtr": "Q3",
          "period_sort": 20263,
          "period_year": 2026,
          "source_type": "news_report",
          "quality_signals": [
            "Beat estimates",
            "Profitable"
          ],
          "revenue_growth_pct": 18.0,
          "revenue_usd": 82890000000,
          "article_ids": [
            "69e99ba475f157062cafcd91",
            "69f87f9d43843dd771ce0936",
            "69f8a61b43843dd771d24172",
            "69f9d902713680636eef61bb"
          ],
          "stockholders_equity_usd": null,
          "total_assets_usd": null,
          "total_liabilities_usd": null
        },
        "narrative": "Latest reported Q3 FY2026: revenue $82.89B, net income $31.8B, EPS $4.27. YoY +34.0% (1.34× prior period). Growth has been erratic across reported periods. Recent signals: Raised guidance, Beat estimates, Profitable.",
        "official_coverage": {
          "bi_periods": 108,
          "currencies": [],
          "form_types": [],
          "fx_converted": false,
          "official_periods": 0
        },
        "prior": {
          "beat_or_miss": "Beat",
          "cash_usd": null,
          "coverage_count": 11,
          "currency_native": "",
          "date": "2025-03-31",
          "ebitda_usd": null,
          "employees": null,
          "eps": 3.22,
          "article_id": "6843078b210ca338ebf3ec5f",
          "metric_sources": {
            "eps": "news_report",
            "net_income_usd": "news_report",
            "operating_income_usd": "news_report",
            "revenue_usd": "news_report"
          },
          "filed_date": null,
          "form_type": "",
          "fx_source": "",
          "gross_profit_usd": null,
          "guidance_revenue": 68420000000,
          "has_official": false,
          "headline": "Earnings per share: $3.22 vs. $3.23 in Q2 Revenue: $68.42 billion vs. $69.63 billion in Q2",
          "long_term_debt_usd": null,
          "native": {},
          "net_income_growth_pct": 18.0,
          "net_income_usd": 21940000000,
          "operating_cash_flow_usd": null,
          "operating_income_usd": 32000000000,
          "period_has_official": false,
          "period_label": "Q3 FY2025",
          "period_qtr": "Q3",
          "period_sort": 20253,
          "period_year": 2025,
          "source_type": "news_report",
          "quality_signals": [
            "Beat estimates",
            "Profitable"
          ],
          "revenue_growth_pct": 13.0,
          "revenue_usd": 61860000000,
          "article_ids": [
            "6843078b210ca338ebf3ec5f",
            "685cca85e6fd25cb9e70d484",
            "686410448882abb7e3e5fadd",
            "6864104c8882abb7e3e7f7a0",
            "693145c6222f79889af21778",
            "69653eacc82797245566b667",
            "69863cc7dac7b0ca9c5f0074",
            "698943e994d3f481f3e274f1",
            "6989483794d3f481f3e2ce4f",
            "69e882355cfa3e5ba504a95f",
            "69f88520bbf1d3145598ec22"
          ],
          "stockholders_equity_usd": null,
          "total_assets_usd": null,
          "total_liabilities_usd": null
        },
        "quality_signals_aggregate": [
          "Raised guidance",
          "Beat estimates",
          "Profitable"
        ],
        "score": 77,
        "source": "earnings_table",
        "source_count": 1373,
        "yoy_basis": "numeric",
        "yoy_multiple": 1.34,
        "yoy_pct": 34.0
      },
      "events_by_role": {
        "acquirer": 820,
        "client": 315,
        "contractor": 327,
        "defendant": 459,
        "plaintiff": 124,
        "primary": 5555,
        "seller": 32,
        "target": 50
      },
      "events_by_type": {
        "asset_acquisition": 250,
        "board_updates": 45,
        "buyback": 31,
        "capital_infusion": 66,
        "company_announcement": 690,
        "contracts": 642,
        "earnings": 1379,
        "funding_rounds": 3,
        "funds_raising": 4,
        "incorporation": 2,
        "ipo": 5,
        "job_creation": 111,
        "key_people": 1908,
        "lawsuit": 583,
        "layoffs": 209,
        "ma": 652,
        "new_product": 472,
        "regulatory": 630
      },
      "events_by_year": {
        "2010": 238,
        "2011": 313,
        "2012": 278,
        "2013": 448,
        "2014": 557,
        "2015": 380,
        "2016": 358,
        "2017": 261,
        "2018": 176,
        "2019": 272,
        "2020": 449,
        "2021": 477,
        "2022": 445,
        "2023": 1145,
        "2024": 791,
        "2025": 789,
        "2026": 305
      },
      "financial_trajectory": {
        "buyback_events": 31,
        "funding_events_360d": 9,
        "funding_events_lifetime": 73,
        "highest_stage": "Public",
        "highest_stage_rank": 12,
        "ipo_events": 5,
        "narrative": "Strong financial trajectory: 73 funding events lifetime reaching Public; 9 in last 12 months.",
        "score": 100,
        "stage_pace_years": 0.2
      },
      "innovation_index": {
        "announcements_360d": 59,
        "fda_approvals": 0,
        "narrative": "Moderate innovation signal — 29 products, 59 announcements in 12 months.",
        "new_products_360d": 29,
        "new_products_lifetime": 472,
        "score": 54,
        "velocity_change_pct": -27.5
      },
      "investment_readiness": {
        "breakdown": {
          "earnings": 77,
          "financial_trajectory": 100,
          "innovation": 54,
          "management": 55,
          "market_position": 100,
          "risk": 60
        },
        "label": "Moderate",
        "private_equity_score": 53,
        "public_shares_score": 54,
        "recommendation": "Mixed signals; tilt depends on whether the upside or risk drivers matter more for your thesis. Note: 2 CEO/MD transitions recently — watch leadership continuity.",
        "score": 54
      },
      "management_quality": {
        "board_updates_360d": 0,
        "ceo_cfo_change_signals_90d": 0,
        "ceo_transition_window_years": 4,
        "ceo_transitions": [
          {
            "date": "2023-11-20"
          },
          {
            "date": "2025-08-29",
            "headline": "Microsoft has been searching for a new managing director since Steven Worrall decided to join Telstra InfraCo as its CEO back in May."
          }
        ],
        "ceo_transitions_count": 2,
        "churn_penalty": 16,
        "key_people_events_360d": 186,
        "key_people_events_all": 1908,
        "leadership_churn": true,
        "leadership_churn_level": "elevated",
        "narrative": "Management instability: 2 CEO/MD transitions in the last 4 years — repeated top-seat turnover is a governance risk, not momentum. Investors should diligence succession stability before treating leadership news as a positive.",
        "score": 55,
        "warning_flags": [
          "Leadership turnover"
        ]
      },
      "market_position": {
        "asset_acquisitions": 250,
        "asset_roles": {
          "acquirer": 218,
          "seller": 32
        },
        "contracts_360d": 81,
        "contracts_all": 642,
        "ma_involvement": {
          "acquirer": 602,
          "target": 50
        },
        "ma_total": 652,
        "narrative": "Strong market position: 81 contracts in 12 months, 652 M&A engagements, 250 partnerships lifetime.",
        "partnerships_all": 250,
        "score": 100
      },
      "peer_comparison": {
        "cohort_size": 123,
        "country": "united states",
        "event_count_percentile": 95,
        "event_count_quantiles": {
          "p25": 1,
          "p50": 2,
          "p75": 6,
          "p90": 14,
          "p95": 37
        },
        "market": "business intelligence",
        "innovation_percentile": 95,
        "innovation_quantiles": {
          "p50": 0,
          "p90": 6,
          "p95": 13
        },
        "risk_percentile": 95,
        "risk_quantiles": {
          "p50": 0,
          "p90": 1,
          "p95": 2
        },
        "this_company": {
          "event_count": 518,
          "innovation": 88,
          "risk": 51
        }
      },
      "raw_event_count": 7682,
      "risk_profile": {
        "bankruptcy_events": 0,
        "lawsuits_360d": 24,
        "lawsuits_all": 583,
        "lawsuits_as_defendant": 459,
        "layoffs_180d": 5,
        "narrative": "Elevated risk: 459 cases as defendant, 12 regulatory hits, 5 layoff events recently.",
        "regulatory_360d": 12,
        "score": 60,
        "warning_flags": [
          "Recent Layoffs",
          "Active Litigation",
          "Regulatory Heat",
          "Repeat Defendant"
        ]
      }
    },
    "computed_at": "2026-09-23T03:22:51.284000Z"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:27.830848+00:00",
    "partial": false,
    "notes": [
      "Scores and narratives are derived assessments. Financial metrics are retrieved evidence."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:27.831117+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_intelligence.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live Microsoft response included all available intelligence components and an earnings archive with gated history. The example now retains the full captured intelligence object, rather than selecting a few scores. Archive gates remain source-controlled.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.domain / computed_at` | The requested company and the source computation time, distinct from gateway retrieval time. |
| `data.intel.company_meta` | Available size, stage, market and other company context. |
| `data.intel.investment_readiness` | Derived labels and scores, not a recommendation issued by this gateway. |
| `data.intel.risk_profile` | Derived risk indicators and component counts when supplied. |
| `data.intel.earnings` | Source earnings context; use get_financials for normalized metric provenance. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Read the computation date and the component you need, then retrieve the supporting company events or financial metrics separately. Build a research view that labels a risk score as derived and a filing-sourced revenue value as retrieved financial evidence. Preserve a gap when a component is absent.

Do not sum unrelated score families, treat a score as a probability, or label a computed assessment as an audited financial value. The gateway does not establish the source scoring model's calibration.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/competitor-intelligence-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
