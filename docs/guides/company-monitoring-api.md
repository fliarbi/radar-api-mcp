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
