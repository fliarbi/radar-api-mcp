# Investor portfolio, co-investor, follow-on analysis and funding news API

[All endpoints](README.md) · [Workflow guide](../guides/investor-data-api.md)

Request one rich investor field or one market-directory field with complete business attributes. Portfolio and shortlist arrays are paginated; analysis objects retain their full structure.

## Route, authentication and credits

**`POST /v1/investors/field`** · MCP tool **`get_investor_field`** · key scope **`investors`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `slug` | required | string; min characters: `1`; max characters: `180`; pattern: `^[a-z0-9]+(?:-[a-z0-9]+)*$` |
| `field` | required | string; one of `portfolio`, `undated_portfolio`, `sectors`, `stages`, `activity`, `follow_on`, `co_investors`, `news`, `analysis`, `related`, `investors`, `recent_rounds`, `themes`, `research`, `geography`, `selection` |
| `limit` | default `20` | integer; minimum: `1`; maximum: `100` |
| `offset` | default `0` | integer; minimum: `0`; maximum: `100000` |
| `q` | default `null` | string or null; min characters: `2`; max characters: `500` |
| `sector` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `stage` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `city` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `country` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `kind` | default `null` | string or null; one of `angel`, `firm` |
| `sort_by` | default `"source"` | string; one of `source`, `name`, `latest`, `companies` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/investors/field" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"slug":"anupam-mittal","field":"portfolio","limit":5}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_investor_field -->
```json
{
  "name": "get_investor_field",
  "arguments": {
    "request": {
      "slug": "anupam-mittal",
      "field": "portfolio",
      "limit": 5
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_investor_field -->
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
        "domain": "lickcious.com",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=lickcious.com",
        "name": "Lickcious",
        "url": "/company/lickcious/2ylzom93uz/",
        "description": "Online retailer of oral sprays, lubes, intimate washes, and perfumes",
        "city": "",
        "country": "India",
        "sectors": [
          "B2C E-Commerce",
          "Beauty E-Commerce",
          "Beauty Tech",
          "Internet First Brands",
          "Retail Tech"
        ],
        "stage": "Angel",
        "entry": "2026-03-28",
        "last": "2026-03-28",
        "entry_amount": 52845,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 0,
        "repeat": false,
        "repeat_date": null,
        "next_date": null,
        "next_days": null,
        "mature_24m": false,
        "funded_24m": false,
        "repeat_24m": false
      },
      {
        "domain": "circato.in",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=circato.in",
        "name": "Circato",
        "url": "/company/circato/2s08ott0kw/",
        "description": "Manufacturer of recycled plastic wall panels for net zero construction",
        "city": "Bengaluru",
        "country": "India",
        "sectors": [
          "Green Buildings"
        ],
        "stage": "Angel",
        "entry": "2026-03-17",
        "last": "2026-03-17",
        "entry_amount": 97444,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 0,
        "repeat": false,
        "repeat_date": null,
        "next_date": null,
        "next_days": null,
        "mature_24m": false,
        "funded_24m": false,
        "repeat_24m": false
      },
      {
        "domain": "ctruh.com",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=ctruh.com",
        "name": "Ctruh",
        "url": "/company/ctruh/17y2slqltk/",
        "description": "Provider of a no-code content creation platform for the metaverse",
        "city": "Bengaluru",
        "country": "India",
        "sectors": [
          "Augmented Reality",
          "Augmented Reality Development Tools",
          "Blockchain",
          "Metaverse",
          "Spatial Computing",
          "Virtual Reality"
        ],
        "stage": "Angel",
        "entry": "2026-03-12",
        "last": "2026-03-12",
        "entry_amount": 108603,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 1,
        "repeat": false,
        "repeat_date": null,
        "next_date": "2026-04-28",
        "next_days": 47,
        "mature_24m": false,
        "funded_24m": true,
        "repeat_24m": false
      },
      {
        "domain": "landofcakesbakery.com",
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=landofcakesbakery.com",
        "name": "Land of Cakes",
        "url": "/company/land-of-cakes/3crk6yenfz/",
        "description": "Retailer of cakes, cheesecakes, tarts, brownies, and ice cream desserts",
        "city": "Kolkata",
        "country": "India",
        "sectors": [
          "Food & Beverage Products"
        ],
        "stage": "Angel",
        "entry": "2026-03-03",
        "last": "2026-03-03",
        "entry_amount": 109292,
        "rounds": 1,
        "lead_entry": false,
        "other_backers": 0,
        "repeat": false,
        "repeat_date": null,
        "next_date": null,
        "next_days": null,
        "mature_24m": false,
        "funded_24m": false,
        "repeat_24m": false
      },
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
      }
    ],
    "pagination": {
      "source_total": 268,
      "matched_total": 268,
      "offset": 0,
      "limit": 5,
      "returned": 5,
      "next_offset": 5
    }
  },
  "window": {
    "data_through": "2026-05-22"
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:55.048045+00:00",
    "partial": false,
    "notes": [
      "Investor metrics use the dated, verified Atlas snapshot. Retrieval time is not data freshness. Use available_fields for separate detail requests."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T06:47:55.048255+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_investor_field.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Anupam Mittal portfolio capture returns five complete company rows from 268 dated companies. Separate captures expose all ten available profile fields and nine FinTech/Bengaluru directory fields. Live pagination traversed all 268 portfolio rows and all 1,199 selected directory investors.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.value` | The selected data only. Portfolio rows retain identity, sector/stage, entry and latest dates, amounts, round counts, lead flags, syndicate size and later-financing outcomes. |
| `data.pagination` | Stored source_total, filtered matched_total, returned count, offset, limit and next_offset. Present on array fields; nested row attributes are retained. |
| `data.coverage` | Source cutoff and computation date, separate from retrieval time. |
| `data.definitions` | Non-additive sectors, whole-round USD amounts and cohort eligibility definitions. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Use available_fields from get_investor_page. Request portfolio to examine named investments, follow_on for measured 24-month outcomes, co_investors for syndicate relationships, news for dated source-linked reporting, or investors for a directory shortlist. Advance pagination.next_offset until null.

Directory shortlists are selected subsets, not the full investor universe. Offsets page top-level arrays; portfolio filters accept q, sector, stage, city and country, while directory investors accept q, stage, city, country and kind. LinkedIn reveals, emails, phone numbers and internal source identifiers are excluded.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/investor-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
