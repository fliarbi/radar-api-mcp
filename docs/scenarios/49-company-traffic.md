# Retrieve Swiggy traffic and geography observations.

[All 50 scenarios](README.md) · [Workflow guide](../guides/technology-traffic-data-api.md) · [Endpoint reference](../reference/get_company_field.md)

**POST `/v1/companies/field`** · MCP tool **`get_company_field`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** Selected field traffic contains data.

## Exact executed request

<!-- scenario-request: 49-company-traffic -->
```json
{
  "domain": "swiggy.com",
  "field": "traffic",
  "item_limit": 100
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.715647+00:00; HTTP **200**;
**observed**, 0.007 seconds.
Local authenticated gateway with live configured read-only sources.

Response contract and declared scenario checks passed; source truth not independently certified.

Only the requested detail field is returned. Preserve field_status, source update date, nested business structures and array coverage. Missing observations do not become zero or proof that the company lacks a technology, market or traffic source.

The baseline was HTTP 200, **observed**:
Response contract and declared scenario checks passed; source truth not independently certified. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 49-company-traffic -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "swiggy.com",
    "company_id": "tiwgsjxo90",
    "field": "traffic",
    "value": {
      "authority": 83,
      "global_rank": 3127,
      "country_rank": 187,
      "country": "India",
      "visits": 16549799,
      "visits_date": "2026-05-01",
      "bounce": 0.6869,
      "ppv": 3.4375,
      "keywords": [
        {
          "k": "swiggy",
          "pos": 1,
          "vol": 2240000
        },
        {
          "k": "restaurants",
          "pos": 2,
          "vol": 11100000
        },
        {
          "k": "instamart",
          "pos": 1,
          "vol": 1000000
        }
      ],
      "audience": [
        {
          "cc": "IN",
          "country": "India",
          "share": 0.9678,
          "visits": 16017135
        },
        {
          "cc": "US",
          "country": "United States",
          "share": 0.01,
          "visits": 165660
        },
        {
          "cc": "GB",
          "country": "United Kingdom",
          "share": 0.006,
          "visits": 99162
        },
        {
          "cc": "KR",
          "country": "South Korea",
          "share": 0.0017,
          "visits": 27820
        },
        {
          "cc": "CA",
          "country": "Canada",
          "share": 0.0016,
          "visits": 26613
        }
      ]
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "traffic": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/keywords": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/audience": {
          "available": 5,
          "returned": 5,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.715527+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/49-company-traffic.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
