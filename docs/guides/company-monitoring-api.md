# Company monitoring API: follow companies, events and associated news

Company monitoring combines a list of businesses with repeatable retrieval of
their activity. Radar's private account mode provides an API watchlist, and the
data API retrieves company events, funding history and associated business news.
Use these pieces to build an internal company-monitoring dashboard or research feed.

Following a company does not automatically start background API requests, send
email alerts or incur usage charges. Your application decides when to retrieve
updates and remains subject to account rate, concurrency and credit limits.

## Follow a company in your API watchlist

The developer console at `/developer` includes a Following section. The equivalent
account operation is `PUT /account/following`, authenticated with a Radar session
in `X-Auth-Token`:

```json
{"domain":"microsoft.com"}
```

Repeatedly following the same normalized domain is idempotent. Use
`GET /account/following` to list companies and
`DELETE /account/following/microsoft.com` to remove one. These are account actions,
so they are deliberately absent from the read-only MCP tool list.

The API watchlist is stored separately from Radar's existing dashboard watchlist;
there is no automatic synchronization. Its capacity follows the current plan:
Free 0, Pro 100, Business 1,000, and the Market.ai bundled grant 0. Downgrading does
not delete existing follows; removal is still possible and additions obey the
new limit. Prepaid credits do not expand watchlist capacity.

## Retrieve company events

`get_company_events` maps to `POST /v1/companies/events`:

```json
{"domain":"microsoft.com","days":90,"limit":50}
```

Inspect the effective date window and truncation/access flags. Requesting 90 days
does not guarantee that your account exposes 90 days. Keep stable returned event
identifiers where available and deduplicate your own feed before showing repeated
results as new activity.

## Add news and funding context

Retrieve [financial news](financial-news-api.md) for a company when the News
connection is available. Use [funding history](startup-funding-data-api.md) for
structured rounds and [funding news](funding-news-api.md) for announcements. Each
successful data request is metered independently; a follow itself is not a paid
data operation.

There is no event-push subscription, automatic email delivery or freshness SLA in
this preview. Store the response retrieval time and source dates separately so a
monitoring page can explain how current its evidence is.

Related: [API keys](api-keys-authentication.md), [pricing and usage](pricing-pay-per-use.md),
[company enrichment](company-enrichment-api.md), [capability reference](../CAPABILITIES.md).

<!-- captured-workflow -->
## Turn an API watchlist into an application-controlled monitor

Following a company stores a domain in the account's API watchlist. It does not
create a background polling job, send an email or mirror the Radar dashboard's
saved list. Your application chooses when to fetch events, stores the last
successful retrieval and compares stable event/article identifiers. Each successful
data fetch consumes its normal credit allocation; adding the domain itself does
not reserve future polling credits.

Choose polling frequency from the required freshness and your budget. Ten companies
polled once each day through one single-credit event operation would require 300
successful-operation credits in a thirty-day month, before any extra news or brief
calls. This is arithmetic illustrating the credit model, not a promise of thirty
new observations per company. Keep prepaid spending caps enabled according to the
account owner's intended usage.

In the captured thirty-day Microsoft timeline, `events` is empty while `truncated`
is true and broader pulse fields describe a longer history. Preserve the response
window and source freshness instead of announcing “no company activity.” After a
failed or partial poll, keep the last complete checkpoint so a later retry does
not accidentally skip records or erase previously known events.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/events`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_company_events -->
```json
{
  "domain": "microsoft.com",
  "days": 30,
  "limit": 2
}
```

<!-- response-example: get_company_events -->
```json
{
  "ok": true,
  "feature": "get_company_events",
  "data": {
    "freshness": {
      "future_rows_count": 0,
      "future_rows_filtered": false,
      "latest_event_date": "2026-05-04",
      "latest_inserted_at": "2026-09-20T05:30:00+05:30"
    },
    "truncated": true,
    "buckets_by_month": {},
    "domain": "microsoft.com",
    "events": [],
    "plan": "free",
    "pulse": {
      "badges": [
        "Leadership Turnover"
      ],
      "ceo_transitions": 2,
      "churn_penalty": 10,
      "days_since_latest": 999,
      "event_variety_360d": 6,
      "events_30d_fresh": 0,
      "events_360d": 345,
      "events_prev_360d": 425,
      "label": "Quiet",
      "leadership_churn": true,
      "leadership_churn_level": "elevated",
      "momentum_pct": -18.8,
      "opportunity_score": 0,
      "risk_score": 0,
      "score": 36,
      "top_drivers": [
        {
          "count": 186,
          "event_type": "key_people",
          "label": "Key People Movement"
        },
        {
          "count": 74,
          "event_type": "earnings",
          "label": "Earnings Release"
        },
        {
          "count": 61,
          "event_type": "company_announcement",
          "label": "Company Announcement"
        }
      ],
      "window_days": 360
    },
    "totals_by_type": {},
    "window_days": 30
  },
  "window": {
    "data_through": "2026-05-04",
    "effective_days": 30,
    "requested_days": 30
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:46.111118+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_events.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The captured thirty-day Microsoft request returned events=[] and truncated=true. Its source freshness pointed to an older latest event date, and its pulse included broader historical activity. An empty thirty-day list therefore cannot establish that the company has never had any relevant events.

See the [complete get_company_events endpoint reference](../reference/get_company_events.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 66 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
