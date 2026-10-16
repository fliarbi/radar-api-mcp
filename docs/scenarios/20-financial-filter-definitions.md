# Discover exact financial thresholds, growth meanings and screening limits.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-filters-data-api.md) · [Endpoint reference](../reference/financial_filter_catalog.md)

**POST `/v1/companies/financials/filters`** · MCP tool **`financial_filter_catalog`**.
Use `https://radar-api.fliarbi.com` (`RADAR_API_URL`) and your API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** Response content present.

## Exact executed request

<!-- scenario-request: 20-financial-filter-definitions -->
```json
{}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.190232+00:00; HTTP **200**;
**qualified**, 0.003 seconds.
Local authenticated gateway with live configured read-only sources.

Coverage is explicitly bounded.

Legacy source revenue bands have open boundaries and exclude zero. Use exact numeric constraints when the threshold matters. The catalogue documents accepted predicates, not whether a particular company has enough financial evidence to evaluate them.

The baseline was an unavailable operation registry check (no HTTP request), **unavailable**:
not_implemented. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 20-financial-filter-definitions -->
```json
{
  "ok": true,
  "feature": "financial_filter_catalog",
  "data": {
    "currency": "USD",
    "numeric_screen": {
      "$defs": {
        "CompanyFilters": {
          "additionalProperties": false,
          "properties": {
            "company_names": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Company Names",
              "type": "array"
            },
            "industries": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Industries",
              "type": "array"
            },
            "sectors": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Sectors",
              "type": "array"
            },
            "markets": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Markets",
              "type": "array"
            },
            "business_models": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Business Models",
              "type": "array"
            },
            "locations": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Locations",
              "type": "array"
            },
            "sizes": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Sizes",
              "type": "array"
            },
            "stages": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Stages",
              "type": "array"
            },
            "technologies": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Technologies",
              "type": "array"
            },
            "products": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Products",
              "type": "array"
            },
            "skills": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Skills",
              "type": "array"
            },
            "event_types": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Event Types",
              "type": "array"
            },
            "financing_status": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Financing Status",
              "type": "array"
            },
            "ownership_status": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Ownership Status",
              "type": "array"
            },
            "revenue_bands": {
              "items": {
                "enum": [
                  "under1m",
                  "1m-10m",
                  "10m-100m",
                  "100m-1b",
                  "1b+"
                ],
                "type": "string"
              },
              "maxItems": 1,
              "title": "Revenue Bands",
              "type": "array"
            },
            "revenue_growth": {
              "items": {
                "enum": [
                  "declining",
                  "flat",
                  "growing",
                  "high",
                  "hyper"
                ],
                "type": "string"
              },
              "maxItems": 1,
              "title": "Revenue Growth",
              "type": "array"
            },
            "profitability": {
              "items": {
                "enum": [
                  "profitable",
                  "loss"
                ],
                "type": "string"
              },
              "maxItems": 1,
              "title": "Profitability",
              "type": "array"
            },
            "entity_type": {
              "default": "all",
              "enum": [
                "all",
                "investor",
                "incubator"
              ],
              "title": "Entity Type",
              "type": "string"
            },
            "revenue_models": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Revenue Models",
              "type": "array"
            },
            "business_approaches": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Business Approaches",
              "type": "array"
            },
            "scalability": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Scalability",
              "type": "array"
            },
            "growth_stages": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Growth Stages",
              "type": "array"
            },
            "operating_status": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Operating Status",
              "type": "array"
            },
            "organization_types": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Organization Types",
              "type": "array"
            },
            "deal_sizes": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Deal Sizes",
              "type": "array"
            },
            "ages": {
              "items": {
                "enum": [
                  "Most Recent",
                  "< 5y",
                  "5-10y",
                  "10-25y",
                  "25+y"
                ],
                "type": "string"
              },
              "maxItems": 1,
              "title": "Ages",
              "type": "array"
            },
            "founded_year_from": {
              "anyOf": [
                {
                  "maximum": 2100,
                  "minimum": 1800,
                  "type": "integer"
                },
                {
                  "type": "null"
                }
              ],
              "default": null,
              "title": "Founded Year From"
            },
            "founded_year_to": {
              "anyOf": [
                {
                  "maximum": 2100,
                  "minimum": 1800,
                  "type": "integer"
                },
                {
                  "type": "null"
                }
              ],
              "default": null,
              "title": "Founded Year To"
            },
            "positions": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Positions",
              "type": "array"
            },
            "verticals": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Verticals",
              "type": "array"
            },
            "industrial_applications": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Industrial Applications",
              "type": "array"
            },
            "founders_background": {
              "items": {
                "enum": [
                  "serial_entrepreneur",
                  "first_time_founder",
                  "founder_with_exit",
                  "top_ranked_founder",
                  "top_tier_university",
                  "elite_alumni",
                  "technical_founder",
                  "ex_notable_employer",
                  "c_level_exec",
                  "seasoned_15y"
                ],
                "type": "string"
              },
              "maxItems": 10,
              "title": "Founders Background",
              "type": "array"
            },
            "web_popularity": {
              "items": {
                "enum": [
                  "high",
                  "medium",
                  "low"
                ],
                "type": "string"
              },
              "maxItems": 3,
              "title": "Web Popularity",
              "type": "array"
            },
            "web_cwv": {
              "items": {
                "enum": [
                  "pass",
                  "needs_improvement",
                  "poor"
                ],
                "type": "string"
              },
              "maxItems": 3,
              "title": "Web Cwv",
              "type": "array"
            },
            "web_speed": {
              "items": {
                "enum": [
                  "fast",
                  "average",
                  "slow"
                ],
                "type": "string"
              },
              "maxItems": 3,
              "title": "Web Speed",
              "type": "array"
            },
            "web_seo_maturity": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Web Seo Maturity",
              "type": "array"
            },
            "web_sd_maturity": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Web Sd Maturity",
              "type": "array"
            },
            "web_business_hints": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Web Business Hints",
              "type": "array"
            },
            "web_score": {
              "items": {
                "enum": [
                  "80+",
                  "60-80",
                  "40-60",
                  "<40"
                ],
                "type": "string"
              },
              "maxItems": 1,
              "title": "Web Score",
              "type": "array"
            },
            "mobile_downloads": {
              "items": {
                "enum": [
                  "1k+",
                  "100k+",
                  "1m+",
                  "10m+"
                ],
                "type": "string"
              },
              "maxItems": 1,
              "title": "Mobile Downloads",
              "type": "array"
            },
            "mobile_growth": {
              "items": {
                "enum": [
                  "declining",
                  "flat",
                  "growing",
                  "high",
                  "hyper"
                ],
                "type": "string"
              },
              "maxItems": 1,
              "title": "Mobile Growth",
              "type": "array"
            },
            "hiring": {
              "anyOf": [
                {
                  "$ref": "#/$defs/HiringFilter"
                },
                {
                  "type": "null"
                }
              ],
              "default": null
            },
            "radius_km": {
              "anyOf": [
                {
                  "maximum": 250,
                  "minimum": 21,
                  "type": "integer"
                },
                {
                  "type": "null"
                }
              ],
              "default": null,
              "description": "Explicit radius expansion around the selected location; source matching tiers apply",
              "title": "Radius Km"
            }
          },
          "title": "CompanyFilters",
          "type": "object"
        },
        "FinancialConstraint": {
          "additionalProperties": false,
          "properties": {
            "metric": {
              "enum": [
                "revenue",
                "net_income",
                "operating_income",
                "gross_profit",
                "ebitda",
                "total_assets",
                "total_liabilities",
                "stockholders_equity",
                "cash",
                "long_term_debt",
                "operating_cash_flow",
                "investing_cash_flow",
                "financing_cash_flow",
                "free_cash_flow",
                "capex"
              ],
              "title": "Metric",
              "type": "string"
            },
            "gt": {
              "anyOf": [
                {
                  "maximum": 1000000000000000,
                  "minimum": -1000000000000000,
                  "type": "number"
                },
                {
                  "type": "null"
                }
              ],
              "default": null,
              "title": "Gt"
            },
            "gte": {
              "anyOf": [
                {
                  "maximum": 1000000000000000,
                  "minimum": -1000000000000000,
                  "type": "number"
                },
                {
                  "type": "null"
                }
              ],
              "default": null,
              "title": "Gte"
            },
            "lt": {
              "anyOf": [
                {
                  "maximum": 1000000000000000,
                  "minimum": -1000000000000000,
                  "type": "number"
                },
                {
                  "type": "null"
                }
              ],
              "default": null,
              "title": "Lt"
            },
            "lte": {
              "anyOf": [
                {
                  "maximum": 1000000000000000,
                  "minimum": -1000000000000000,
                  "type": "number"
                },
                {
                  "type": "null"
                }
              ],
              "default": null,
              "title": "Lte"
            }
          },
          "required": [
            "metric"
          ],
          "title": "FinancialConstraint",
          "type": "object"
        },
        "HiringFilter": {
          "additionalProperties": false,
          "properties": {
            "is_hiring": {
              "default": true,
              "title": "Is Hiring",
              "type": "boolean"
            },
            "min_open_roles": {
              "default": 1,
              "maximum": 100000,
              "minimum": 1,
              "title": "Min Open Roles",
              "type": "integer"
            },
            "roles": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Roles",
              "type": "array"
            },
            "cities": {
              "items": {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              "maxItems": 20,
              "title": "Cities",
              "type": "array"
            },
            "recency_days": {
              "default": 30,
              "maximum": 365,
              "minimum": 1,
              "title": "Recency Days",
              "type": "integer"
            }
          },
          "title": "HiringFilter",
          "type": "object"
        }
      },
      "additionalProperties": false,
      "properties": {
        "filters": {
          "$ref": "#/$defs/CompanyFilters"
        },
        "domains": {
          "items": {
            "type": "string"
          },
          "maxItems": 10,
          "title": "Domains",
          "type": "array"
        },
        "constraints": {
          "items": {
            "$ref": "#/$defs/FinancialConstraint"
          },
          "maxItems": 5,
          "minItems": 1,
          "title": "Constraints",
          "type": "array"
        },
        "period_type": {
          "enum": [
            "annual",
            "quarterly"
          ],
          "title": "Period Type",
          "type": "string"
        },
        "year_from": {
          "anyOf": [
            {
              "maximum": 2100,
              "minimum": 1900,
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Year From"
        },
        "year_to": {
          "anyOf": [
            {
              "maximum": 2100,
              "minimum": 1900,
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Year To"
        },
        "source_type": {
          "default": "any",
          "enum": [
            "any",
            "filing",
            "news_report"
          ],
          "title": "Source Type",
          "type": "string"
        },
        "page": {
          "default": 0,
          "maximum": 200,
          "minimum": 0,
          "title": "Page",
          "type": "integer"
        },
        "candidate_limit": {
          "default": 5,
          "maximum": 10,
          "minimum": 1,
          "title": "Candidate Limit",
          "type": "integer"
        }
      },
      "required": [
        "constraints",
        "period_type"
      ],
      "title": "FinancialScreen",
      "type": "object"
    },
    "period_selection": "Latest accessible period of the requested annual/quarterly type and year window. All constraints use the same period. Never fall back to an older period to manufacture a match.",
    "revenue_bands": {
      "under1m": "0 < revenue < 1000000",
      "1m-10m": "1000000 < revenue < 10000000",
      "10m-100m": "10000000 < revenue < 100000000",
      "100m-1b": "100000000 < revenue < 1000000000",
      "1b+": "revenue > 1000000000"
    },
    "source_band_boundary_note": "Radar legacy bands exclude exact boundary values and zero. They refer to source financial summary fields, not a selected fiscal period.",
    "growth_bands_pct": {
      "declining": "<0",
      "flat": ">=0 and <10",
      "growing": ">=10 and <30",
      "high": ">=30 and <100",
      "hyper": ">=100"
    },
    "profitability": {
      "profitable": "net profit > 0",
      "loss": "net profit < 0"
    },
    "distinctions": [
      "Revenue models describe how a business earns money.",
      "Deal-size filters select funding rounds, not revenue.",
      "Display columns and estimated-revenue sorts are not verified financial statements.",
      "Unknown financial values do not satisfy a numeric filter, including zero."
    ],
    "billing": "Reserve 1 + candidate_limit credits (or 1 + number of domains); settle one screen credit plus successful financial reads. Unused/failed reads are refunded.",
    "coverage": {
      "complete": false,
      "note": "A bounded screen over a source candidate page or explicit domains, not an exhaustive database-wide financial query. Source gates remain authoritative."
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:32.190000+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/20-financial-filter-definitions.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
