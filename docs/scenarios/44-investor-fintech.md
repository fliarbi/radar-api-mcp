# Retrieve Anupam Mittal’s recorded FinTech portfolio entries.

[All 50 scenarios](README.md) · [Workflow guide](../guides/investor-data-api.md) · [Endpoint reference](../reference/get_investor_field.md)

**POST `/v1/investors/field`** · MCP tool **`get_investor_field`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 44-investor-fintech -->
```json
{
  "slug": "anupam-mittal",
  "field": "portfolio",
  "sector": "FinTech",
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.661876+00:00; HTTP **200**;
**qualified**, 0.008 seconds.
Local authenticated gateway with live configured read-only sources.

Dated published research snapshot; not current investment activity.

This is a dated published research snapshot. Keep data_through, release and cohort definitions. Portfolio amounts are whole-round amounts, sectors can overlap, and a co-investor relationship is not proof of a current partnership or investment mandate.

The baseline was HTTP 200, **qualified**:
Dated published research snapshot; not current investment activity. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 44-investor-fintech -->
```json
{
  "ok": true,
  "feature": "get_investor_field",
  "data": {
    "slug": "anupam-mittal",
    "kind": "investor_profile",
    "family": "investor",
    "coverage": {
      "data_through": "2026-05-22",
      "computed_on": "2026-09-14",
      "last_investment": "2026-03-28",
      "first_investment": "2011-04-21",
      "recent_window_start": "2024-05-22",
      "previous_window_start": "2022-05-22",
      "release": "atlas-20260914-v1",
      "snapshot_sha256": "ce205691ab49871ec3e14f25ea4fabc89c1b8a75c4d8053ae755453869946979",
      "partial": false,
      "source": "verified_published_atlas_snapshot"
    },
    "field": "portfolio",
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
        "domain": "cotopay.in",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=cotopay.in",
        "name": "CotoPay",
        "url": "/company/cotopay/13zqy88k0j/",
        "description": "Provider of UPI voucher platform for business expense management solutions",
        "city": "Delhi",
        "country": "India",
        "sectors": [
          "CFO Stack",
          "Expense Analytics Software",
          "FinTech",
          "Finance & Accounting Tech"
        ],
        "stage": "Angel",
        "entry": "2026-02-11",
        "last": "2026-02-11",
        "entry_amount": 82770,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 1,
        "repeat": false,
        "repeat_date": null,
        "next_date": null,
        "next_days": null,
        "mature_24m": false,
        "funded_24m": false,
        "repeat_24m": false
      },
      {
        "domain": "savesage.club",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=savesage.club",
        "name": "SaveSage",
        "url": "/company/savesage/19egy2b9f8/",
        "description": "Platform that offers strategies for saving money along with credit card rewards and loyalty programs",
        "city": "Gurugram",
        "country": "India",
        "sectors": [
          "FinTech",
          "Payments"
        ],
        "stage": "Angel",
        "entry": "2026-01-09",
        "last": "2026-01-09",
        "entry_amount": 444820,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 3,
        "repeat": false,
        "repeat_date": null,
        "next_date": null,
        "next_days": null,
        "mature_24m": false,
        "funded_24m": false,
        "repeat_24m": false
      },
      {
        "domain": "mitigata.com",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=mitigata.com",
        "name": "Mitigata",
        "url": "/company/mitigata/1cxc6esmlf/",
        "description": "Provider of cyber insurance products and digital security monitoring services",
        "city": "Bengaluru",
        "country": "India",
        "sectors": [
          "Cyber Insurance",
          "Cybersecurity",
          "FinTech",
          "FinTech SaaS",
          "InsurTech",
          "InsurTech SaaS",
          "Insurance IT",
          "Insurance Underwriting and Risk Management",
          "Internet First Insurance Platforms",
          "Internet First Insurers",
          "Security Analytics",
          "Usage Based Insurance",
          "Vulnerability Assessment"
        ],
        "stage": "Seed",
        "entry": "2024-01-12",
        "last": "2024-01-12",
        "entry_amount": 961925,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 11,
        "repeat": false,
        "repeat_date": null,
        "next_date": "2025-07-22",
        "next_days": 557,
        "mature_24m": true,
        "funded_24m": true,
        "repeat_24m": false
      }
    ],
    "pagination": {
      "source_total": 268,
      "matched_total": 29,
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
    "retrieved_at": "2026-09-23T03:35:33.661688+00:00",
    "partial": false,
    "notes": [
      "Investor metrics use the dated, verified Atlas snapshot. Retrieval time is not data freshness. Use available_fields for separate detail requests."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/44-investor-fintech.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
