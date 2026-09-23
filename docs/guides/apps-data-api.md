# Mobile app data API: Android apps, downloads, ratings and company app intelligence

Use Radar’s app data API and MCP tools to discover Google Play apps, connect apps
to a company website, inspect ratings and monetization, and retrieve dated install
history. The API exposes individual app records, not only a company's aggregate
mobile-download count. App intelligence can support competitive research,
developer discovery, product comparisons and company-growth analysis.

## Find apps and categories

`POST /v1/apps/search` / `search_apps`:

```json
{"category":"Food & Drink","min_installs":1000000,"min_score":4,"free":true,"sort_by":"installs","limit":20,"page":0}
```

Supported filters are q (app-name substring), developer (name substring), exact
website domain, exact category label, min_installs, min_score and free. At least
q, developer, domain, category or min_installs is required. Sort choices are
installs, rating, observed and name. Pages start at zero, with limits of 1–100;
keep the same filters and ordering and continue while has_more is true. There is
no inferred total. Use `app_filter_options` to discover observed category labels.

For company apps, use `POST /v1/companies/apps` / `company_apps`:

```json
{"domain":"swiggy.com","limit":10,"page":0}
```

The developer website host must match exactly after lowercasing and removing
www. The captured result contains four apps. The delivery-partner app uses
ride.swiggy.com, so it requires that explicit domain or a broader app search.
A clone vendor's URL path mentioning Swiggy does not establish a company match.
An exact developer-host match is still an observed association, not a verified
legal ownership statement.

## Keep the profile compact; select the needed detail

`POST /v1/apps/profile` / `get_app`:

```json
{"app_id":"in.swiggy.android"}
```

The profile returns name, summary, category, developer website, store URL,
recorded installs, rating, rating count and UTC observation date. Its
available_fields list tells you which groups can be requested. A group can
contain unknown individual values. The captured Swiggy profile has seven groups
and 15 stored install-history rows. The live audit found only two distinct
observations among those rows; duplicates are retained and disclosed, not counted
as additional dates. Deduplicate identical date/install/band tuples if your analysis
requires unique measurements.

`POST /v1/apps/field` / `get_app_field`:

```json
{"app_id":"in.swiggy.android","field":"install_history","limit":5,"offset":0}
```

| Field | Available detail |
|---|---|
| listing | Summary, description, categories, content rating, screenshots, privacy-policy URL and source availability |
| ratings | Score, rating count, review count and complete rating histogram |
| monetization | Price, currency, free/paid, in-app purchases, ads and Play Pass flag |
| release | Release text, update timestamp, version, Android requirements, preregistration and early-access flags |
| developer | Name, store developer ID, website and recorded legal name |
| growth | Two dated install counts, gap days, observed and annualized change, reliability and release-date flags |
| install_history | Dated install observations and minimum-install band, with offset pagination |

Follow pagination.next_offset for install history until null. Offsets are rejected
for other fields. Developer email, phone and address are excluded from these
app fields; contacts have their own scope and entitlement checks.

## Interpret mobile growth correctly

The Swiggy capture reports 281,013,619 cumulative installs at its June 2026
observation. The earlier observation is 223,179,065 installs, 360 days earlier.
The source calculates 25.91% observed change and 26.32% annualized change and
marks this comparison reliable. These are stored measurements, not current
active users, revenue, retention or predicted future growth. A null rating differs
from a recorded zero. A release-date-suspect flag limits age-based velocity claims.

Current coverage is Google Play / Android. No Apple App Store source is connected.
A successful retrieval does not refresh a store listing. `observed_at` timestamps
are UTC; release strings retain source formatting and updated is a Unix timestamp.

Use `apps` key scope for `/v1/apps/*` and `companies` for company app discovery.
Each successful request costs one credit in account mode; normal shared rate,
concurrency and spending limits apply. An unconfigured app connection returns 503.

See [seven real field outputs](../APP_DATA_DEPTH.md), [app search reference](../reference/search_apps.md),
[company potential research](potential-company-data-api.md) and [API keys](api-keys-authentication.md).

<!-- scenario-links -->
## Executed scenarios for this workflow

- [31-company-apps: Which Google Play apps have swiggy.com as the developer website host?](../scenarios/31-company-apps.md)
- [32-food-apps: Find Food & Drink apps with at least one million installs and rating at least four.](../scenarios/32-food-apps.md)
- [33-app-growth: Retrieve Swiggy app growth together with the dated measurements and reliability flag.](../scenarios/33-app-growth.md)
- [34-app-history-page: Retrieve the second page of Swiggy install observations while retaining source duplicates.](../scenarios/34-app-history-page.md)
- [35-app-monetization: Does Swiggy’s app record show ads, purchases, currency and paid/free status?](../scenarios/35-app-monetization.md)
- [36-app-ratings: Retrieve Swiggy’s rating histogram and review counts.](../scenarios/36-app-ratings.md)

<!-- captured-workflow -->
## Read the inputs behind mobile-app growth

The example preserves both dated install measurements, the 360-day interval and source reliability flags. See [all seven app field captures](../APP_DATA_DEPTH.md) for listing, ratings, monetization, release, developer and install-history output. The exact-host company lookup and title search deliberately return different app sets; the match method is part of the evidence.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/apps/field`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_app_field -->
```json
{
  "app_id": "in.swiggy.android",
  "field": "growth"
}
```

<!-- response-example: get_app_field -->
```json
{
  "ok": true,
  "feature": "get_app_field",
  "data": {
    "app_id": "in.swiggy.android",
    "store": "google_play",
    "observed_at": "2026-06-07T03:54:55Z",
    "coverage": {
      "live_store_verified": false,
      "source": "radar_app_records"
    },
    "field": "growth",
    "value": {
      "install_change": {
        "current_observed_at": "2026-06-07T03:54:55Z",
        "current_installs": 281013619,
        "previous_installs": 223179065,
        "previous_observed_at": "2025-06-11T18:30:00Z",
        "gap_days": 360,
        "observed_change_pct": 25.91,
        "annualized_change_pct": 26.32,
        "reliable": 1
      },
      "velocity": {
        "age_years": 11,
        "avg_installs_per_year": 25551462,
        "release_date_suspect": 0,
        "young_fast_riser": 0
      },
      "note": "Annualized growth is derived from the measured gap, not necessarily a full-year observation. Retain reliable and suspect-date flags; this is not a forecast."
    },
    "status": "available"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T10:48:30.099630+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T10:48:30.099775+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_app_field.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The captured growth comparison spans 360 days: 223,179,065 to 281,013,619 installs, 25.91% observed change and 26.32% annualized change. The source reliable flag is 1. All seven separate field outputs are linked from the app depth walkthrough.

See the [complete get_app_field endpoint reference](../reference/get_app_field.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
