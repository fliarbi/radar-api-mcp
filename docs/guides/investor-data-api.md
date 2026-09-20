# Investor data API for venture capital and investment research

Radar's investor data API supports investor discovery, a directory of published
investor pages and retrieval of those pages by slug. Use it to explore investors
associated with a sector or geography and then connect the research to company
funding data or funding news.

Investor search and company funding history answer different questions. Search
discovers investor entities; a funding record supplies reported associations with
a particular company or round. Neither alone establishes an investor's current
mandate, available capital or intention to fund a new deal.

## Search for investors

`search_investors` maps to `POST /v1/investors/search`:

```json
{"filters":{"locations":["India"],"industries":["Software"]},"limit":20,"page":0}
```

The filter vocabulary follows the company search model. Radar interprets relevant
investor filters through its existing headquarters and portfolio classifications.
Check account access metadata because the linked plan can restrict filters or
result counts.

## Discover published investor profiles

Call `investor_directory` (`POST /v1/investors/directory`) with an empty body:

```json
{}
```

Choose a returned slug and pass it to `get_investor_page`
(`POST /v1/investors/page`). For example, the body shape is
`{"slug":"slug-returned-by-directory"}`. Do not invent slugs from names and assume
they exist. Some published pages provide metadata while a detailed roster remains
behind another access gate; the API does not bypass that gate.

## Turn investor discovery into a research workflow

Start with a sector or location, review investor identity, then retrieve relevant
company funding histories. Use [funding news](funding-news-api.md) to examine
reported announcements involving an investor, keeping article dates and source
links. Review the evidence before inferring a pattern in stage or sector preference.

A directory page is not a promise of an up-to-date fund size or a verified contact
address. These read-only APIs do not send messages, create introductions or expose
contact-reveal actions. Investor shortlists should remain research artifacts until
you validate current information through appropriate sources.

Related: [startup funding data](startup-funding-data-api.md), [B2B company search](company-search-api.md),
[company monitoring](company-monitoring-api.md), [MCP integration](company-intelligence-mcp-server.md).

<!-- captured-workflow -->
## Discover an investor slug before requesting a profile

The live directory returned the slug `anupam-mittal`; the successful profile request
below uses that exact value. This is more reliable than guessing a URL slug from
a person's displayed name. Retain `kind` and `family` when navigating the directory
because an investor profile, an angel list and a city list are different page types.

The response contains page metadata only: slug, kind, family, heading and edition.
It does not expose an unrestricted portfolio, contact list or current investment
mandate. An application should show the available profile heading and distinguish
additional authorized research links from data already present in the response.
Directory counts describe published categories and can overlap; adding profile,
angel-list and city-list counts does not yield a unique-investor population.

The filter-based India investor search timed out in this same capture. That failure
does not invalidate the independently successful directory and page requests,
nor does it prove there are no investors in India. If your workflow needs a filtered
investor roster, narrow the source query and handle timeout explicitly. If it only
needs a navigable published profile, use the successful directory-to-slug workflow
and preserve its actual metadata-only coverage.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/investors/page`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_investor_page -->
```json
{
  "slug": "anupam-mittal"
}
```

<!-- response-example: get_investor_page -->
```json
{
  "ok": true,
  "feature": "get_investor_page",
  "data": {
    "slug": "anupam-mittal",
    "kind": "investor_profile",
    "family": "investor",
    "h1": "Anupam Mittal",
    "edition": "founder-atlas"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:59:07.195786+00:00",
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
The [downloadable JSON example](../examples/get_investor_page.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

Using the directory's anupam-mittal slug returned HTTP 200 with investor_profile, investor and the heading Anupam Mittal. The captured response was metadata only. It contained no unrestricted portfolio or contact roster.

See the [complete get_investor_page endpoint reference](../reference/get_investor_page.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
