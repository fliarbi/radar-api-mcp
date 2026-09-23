# Retrieve Microsoft business news for April 2026 and retain dates and source links.

[All 50 scenarios](README.md) · [Workflow guide](../guides/financial-news-api.md) · [Endpoint reference](../reference/search_business_news.md)

**POST `/v1/news/business`** · MCP tool **`search_business_news`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 50-company-news -->
```json
{
  "company": "microsoft.com",
  "date_from": "2026-04-01",
  "date_to": "2026-04-30",
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:37.824929+00:00; HTTP **502**;
**unavailable**, 4.111 seconds.
Actual News application and live query path; isolated test identity/quota; no production connection claim.

upstream_unavailable.

This run uses actual News application queries and live data with an isolated test identity and quota dependencies. It does not verify a production News connection. The current upstream failure remains an error example; older successful captures are not substituted into this run.

Default configuration returned 503 in the baseline. The isolated live-data integration returned 502 after an upstream connection timeout. These are different findings: service not connected versus connected query path unable to reach its data source. No source restart or production configuration change was made.

The baseline was HTTP 503, **unavailable**:
service_unavailable. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 50-company-news -->
```json
{
  "ok": false,
  "feature": "search_business_news",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:37.824809+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  },
  "error": {
    "kind": "upstream_unavailable",
    "message": "The data service could not complete this request"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/50-company-news.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
