# Retrieve three investors from the reviewed Bengaluru FinTech directory.

[All 50 scenarios](README.md) · [Workflow guide](../guides/investor-data-api.md) · [Endpoint reference](../reference/get_investor_field.md)

**POST `/v1/investors/field`** · MCP tool **`get_investor_field`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 46-investor-directory -->
```json
{
  "slug": "fintech-investors-in-bengaluru",
  "field": "investors",
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.692474+00:00; HTTP **200**;
**qualified**, 0.018 seconds.
Local authenticated gateway with live configured read-only sources.

Dated published research snapshot; not current investment activity.

This is a dated published research snapshot. Keep data_through, release and cohort definitions. Portfolio amounts are whole-round amounts, sectors can overlap, and a co-investor relationship is not proof of a current partnership or investment mandate.

The baseline was HTTP 200, **qualified**:
Dated published research snapshot; not current investment activity. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 46-investor-directory -->
```json
{
  "ok": true,
  "feature": "get_investor_field",
  "data": {
    "slug": "fintech-investors-in-bengaluru",
    "kind": "investor_list",
    "family": "investors",
    "coverage": {
      "data_through": "2026-05-22",
      "computed_on": "2026-09-14",
      "last_investment": "2026-05-20",
      "first_investment": null,
      "recent_window_start": "2024-05-22",
      "previous_window_start": "2022-05-22",
      "release": "atlas-20260914-v1",
      "snapshot_sha256": "d5cfdcd78bed3ed7ebfbb35b0f78a446f25fa02b3d42f1484cfa77a6ba133b5e",
      "partial": false,
      "source": "verified_published_atlas_snapshot"
    },
    "field": "investors",
    "status": "available",
    "definitions": {
      "portfolio": "Dated equity investments; undated companies are retrieved separately. Debt and grants are excluded.",
      "amounts": "USD whole-round amounts, not the investor's cheque, fund size, assets under management or investment returns.",
      "follow_on": "Another investor's later financing and this investor's repeat backing are distinct. Only entries with a full 24-month observation window enter the cohort.",
      "sectors": "Historical company tags can overlap; their counts are not additive and do not establish a current investment mandate.",
      "directory": "A directory's stored shortlist is a selected subset of its measured investor universe, not every investor in the database."
    },
    "value": [
      {
        "name": "Kunal Naresh Shah",
        "kind": "angel",
        "slug": "kunal-naresh-shah",
        "domain": "",
        "url": "/investor/kunal-naresh-shah/",
        "city": "Bengaluru",
        "country": "India",
        "companies": 44,
        "rounds": 48,
        "recent": 2,
        "active": true,
        "last": "2025-05-28",
        "repeat_companies": 4,
        "lead_entries": 2,
        "portfolio_total": 277,
        "focus_pct": 15.9,
        "stages": {
          "Seed": 30,
          "Series A": 9,
          "Angel": 1,
          "Series B": 3,
          "Series E+": 1
        },
        "entry_sizes": {
          "n": 44,
          "q1": 1045669.25,
          "median": 2500000.0,
          "q3": 4775000.0
        },
        "examples": [
          {
            "name": "Spense",
            "domain": "",
            "url": "/company/spense/3d68w1v2rm/",
            "date": "2025-05-28",
            "stage": "Seed",
            "amount": 1850000,
            "logo_url": null
          },
          {
            "name": "Prosperr",
            "domain": "prosperr.io",
            "url": "/company/prosperr/2iu4wrru6r/",
            "date": "2024-06-17",
            "stage": "Seed",
            "amount": 1550000,
            "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=prosperr.io"
          },
          {
            "name": "OnFinance AI",
            "domain": "onfinance.ai",
            "url": "/company/onfinance-ai/3doam0b5ad/",
            "date": "2023-11-07",
            "stage": "Seed",
            "amount": 1050000,
            "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=onfinance.ai"
          }
        ],
        "stage_sizes": {
          "Seed": {
            "n": 30,
            "q1": 649424.5,
            "median": 1925000.0,
            "q3": 3000000.0
          },
          "Series A": {
            "n": 9,
            "q1": 4000000.0,
            "median": 6600000.0,
            "q3": 15700000.0
          },
          "Angel": {
            "n": 1,
            "q1": 500000.0,
            "median": 500000.0,
            "q3": 500000.0
          },
          "Series B": {
            "n": 3,
            "q1": 13000000.0,
            "median": 14000000.0,
            "q3": 22500000.0
          },
          "Series E+": {
            "n": 1,
            "q1": 50000000.0,
            "median": 50000000.0,
            "q3": 50000000.0
          }
        },
        "local": true,
        "image_url": null,
        "themes": {
          "alternative-lending": 11,
          "payments": 7,
          "investment-tech": 11,
          "banking-tech": 7,
          "embedded-finance": 6,
          "cfo-stack": 6,
          "insurtech": 5,
          "regtech": 2,
          "financial-ai": 1,
          "blockchain-finance": 3
        }
      },
      {
        "name": "Y Combinator",
        "kind": "firm",
        "slug": "y-combinator",
        "domain": "ycombinator.com",
        "url": null,
        "city": "Mountain View",
        "country": "United States",
        "companies": 42,
        "rounds": 68,
        "recent": 1,
        "active": true,
        "last": "2025-09-28",
        "repeat_companies": 16,
        "lead_entries": 35,
        "portfolio_total": 5648,
        "focus_pct": 0.7,
        "stages": {
          "Seed": 42
        },
        "entry_sizes": {
          "n": 39,
          "q1": 125000.0,
          "median": 125000.0,
          "q3": 500000.0
        },
        "examples": [
          {
            "name": "EnrichVideo",
            "domain": "enrichvideo.com",
            "url": "/company/enrichvideo/1wy20bm0ox/",
            "date": "2025-09-28",
            "stage": "Seed",
            "amount": 500000,
            "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=enrichvideo.com"
          },
          {
            "name": "Infinity",
            "domain": "infinityapp.in",
            "url": "/company/infinity/3xosilfjuj/",
            "date": "2024-04-03",
            "stage": "Seed",
            "amount": 1900000,
            "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=infinityapp.in"
          },
          {
            "name": "Yenmo",
            "domain": "yenmo.in",
            "url": "/company/yenmo/12noqalbwt/",
            "date": "2024-03-22",
            "stage": "Seed",
            "amount": 500000,
            "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=yenmo.in"
          }
        ],
        "stage_sizes": {
          "Seed": {
            "n": 39,
            "q1": 125000.0,
            "median": 125000.0,
            "q3": 500000.0
          }
        },
        "local": false,
        "image_url": "https://in-api-radar.fliarbi.com/company_logo?domain=ycombinator.com",
        "themes": {
          "alternative-lending": 4,
          "payments": 12,
          "investment-tech": 9,
          "banking-tech": 8,
          "embedded-finance": 2,
          "cfo-stack": 9,
          "insurtech": 4,
          "regtech": 1,
          "blockchain-finance": 3
        }
      },
      {
        "name": "Angel List",
        "kind": "firm",
        "slug": "angel-list",
        "domain": "angellist.com",
        "url": null,
        "city": "San Francisco",
        "country": "United States",
        "companies": 39,
        "rounds": 49,
        "recent": 4,
        "active": true,
        "last": "2025-09-04",
        "repeat_companies": 9,
        "lead_entries": 8,
        "portfolio_total": 466,
        "focus_pct": 8.4,
        "stages": {
          "Seed": 35,
          "Series A": 3,
          "Series B": 1
        },
        "entry_sizes": {
          "n": 39,
          "q1": 440503.5,
          "median": 1099552.0,
          "q3": 3050000.0
        },
        "examples": [
          {
            "name": "OnFinance AI",
            "domain": "onfinance.ai",
            "url": "/company/onfinance-ai/3doam0b5ad/",
            "date": "2025-09-04",
            "stage": "Seed",
            "amount": 4200000,
            "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=onfinance.ai"
          },
          {
            "name": "Grey Sky Capital",
            "domain": "greysky.capital",
            "url": "/company/grey-sky-capital/3mdlvefgn5/",
            "date": "2025-06-19",
            "stage": "Seed",
            "amount": 1099552,
            "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=greysky.capital"
          },
          {
            "name": "GreenStitch",
            "domain": "greenstitch.io",
            "url": "/company/greenstitch/3egjankjy9/",
            "date": "2024-12-28",
            "stage": "Seed",
            "amount": 1200000,
            "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=greenstitch.io"
          }
        ],
        "stage_sizes": {
          "Seed": {
            "n": 35,
            "q1": 420246.5,
            "median": 1000000.0,
            "q3": 2238548.5
          },
          "Series A": {
            "n": 3,
            "q1": 6197632.0,
            "median": 7495264.0,
            "q3": 13348684.0
          },
          "Series B": {
            "n": 1,
            "q1": 30000000.0,
            "median": 30000000.0,
            "q3": 30000000.0
          }
        },
        "local": false,
        "image_url": "https://in-api-radar.fliarbi.com/company_logo?domain=angellist.com",
        "themes": {
          "alternative-lending": 10,
          "payments": 7,
          "investment-tech": 9,
          "banking-tech": 8,
          "embedded-finance": 3,
          "cfo-stack": 10,
          "insurtech": 5,
          "regtech": 2,
          "financial-ai": 2
        }
      }
    ],
    "pagination": {
      "source_total": 1199,
      "matched_total": 1199,
      "offset": 0,
      "limit": 3,
      "returned": 3,
      "next_offset": 3
    }
  },
  "window": {
    "data_through": "2026-05-22"
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.692224+00:00",
    "partial": false,
    "notes": [
      "Investor metrics use the dated, verified Atlas snapshot. Retrieval time is not data freshness. Use available_fields for separate detail requests."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/46-investor-directory.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
