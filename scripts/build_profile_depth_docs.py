#!/usr/bin/env python3
"""Build separate profile summaries and measured one-field examples."""
import json
from pathlib import Path
from build_endpoint_docs import digest, encoded, excerpt
from radar_api.models import PROFILE_SECTIONS
from company_depth_examples import render_examples

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ("razorpay.com", "stripe.com", "swiggy.com")


def record(operation, path, request, response):
    public, omitted = excerpt(operation, response)
    return {"operation": operation, "method": "POST", "path": path, "request": request,
            "http_status": 200, "captured_at": response["meta"]["retrieved_at"],
            "capture_kind": "live_gateway", "provenance": "Executed authenticated gateway request using the live company field store",
            "response": public, "omitted_paths": omitted, "original_response_sha256": digest(response),
            "response_excerpt_sha256": digest(public)}


def build():
    profiles, fields = ROOT / "docs/examples/profiles", ROOT / "docs/examples/fields"
    profiles.mkdir(parents=True, exist_ok=True)
    fields.mkdir(parents=True, exist_ok=True)
    summaries = {}
    for domain in DOMAINS:
        raw = json.loads((ROOT / "qa/private" / ("profile-" + domain + ".json")).read_text())
        item = record("get_company", "/v1/companies/profile", {"domain": domain}, raw)
        (profiles / (domain + ".json")).write_text(encoded(item))
        summaries[domain] = item
        for field in PROFILE_SECTIONS:
            raw = json.loads((ROOT / "qa/private" / ("field-" + domain + "-" + field + ".json")).read_text())
            item = record("get_company_field", "/v1/companies/field", raw["request"], raw["response"])
            (fields / (domain + "-" + field + ".json")).write_text(encoded(item))
    (ROOT / "radar_api/static/company-profile-example.json").write_text(encoded(summaries["razorpay.com"]["response"]))
    text = """# Company data examples: financials, founders, apps, LinkedIn, business data and events

Start with a compact company profile. It returns identity, a short description,
founding year, employee count, a Radar image URL and the names of available fields.
Rich values require a separate JSON POST selecting one field. Availability checks
do not return email addresses, phone numbers, technology arrays or founder records.

[Jump to 13 worked examples with complete saved responses](#worked-examples-with-actual-requests-and-outputs),
including [financials](#financial-statements), [founders](#founders-and-background),
[apps](#apps-roster), [LinkedIn-associated profiles](#linkedin-professional),
[business classifications](#business-classification) and [events](#business-events).

## 1. Discover the company and its available fields

```json
{"domain": "razorpay.com"}
```

Send this to `POST /v1/companies/profile`, or MCP `get_company`. Read
`available_fields`, `field_status` and `contacts.availability`. These report stored
coverage. They do not promise current accuracy, email deliverability or paid access.
An unconnected field store returns `profile_depth=card` and unavailable field status.
The normal connected response is `profile_depth=summary`.

## 2. Retrieve one field

```json
{"domain": "razorpay.com", "field": "technology", "item_limit": 100}
```

Send this to `POST /v1/companies/field`, or MCP `get_company_field`. Only `value`
contains the requested field. `item_limit` defaults to 50 and is capped at 100 per
array. Every array reports available/returned/truncated counts in `coverage.arrays`.
No all-fields selector exists. The old `sections` and `item_limit` parameters on
`get_company` are rejected with HTTP 422; move those detail reads to the field endpoint.
Each successful field request costs one operation credit in account mode.

## Real, separate captures

The following JSON files come from authenticated local gateway calls against the
live company store. Most were captured on 2026-09-21; the three social fields were
refreshed on 2026-09-23 with LinkedIn profile logs and stored posts. Each includes its request, response, timestamp,
checksums and explicit documentation omission paths. The values are source
observations; they have not been independently verified as current facts.

| Compact company | Available detail fields | Summary JSON |
|---|---:|---|
"""
    for domain, item in summaries.items():
        d = item["response"]["data"]
        text += f"| {d['company']['name']} | {len(d['available_fields'])} | [{domain}](examples/profiles/{domain}.json) |\n"
    text += "\n| Field request | Razorpay | Stripe | Swiggy |\n|---|---|---|---|\n"
    for field in PROFILE_SECTIONS:
        text += "| `" + field + "` | " + " | ".join(f"[JSON](examples/fields/{domain}-{field}.json)" for domain in DOMAINS) + " |\n"
    text += """
## What the fields mean

- `overview`: alternate names, other domains and the longer description.
- `classification`: sectors, primary and other feeds, industries, business/revenue models and source flags.
- `people`: named key people and founders selected by the source designation. These are professional records; contact values require their own endpoint.
- `technology` and `web_presence`: merged stack, observed technologies and crawl dates versus web performance, SEO and derived digital scores.
- `traffic`: visits, observation date, country shares, keywords and engagement. Visits are not unique customers, and fractions remain fractions.
- `apps`: aggregate app count, downloads and rating. This is not an app roster; downloads are not monthly active users.
- `products`, `geography`, `social`, `lifecycle`, `legal`, `assessments`: separately requested business context. Scores are derived assessments; legal associations may need review.
- `social` includes platform links plus `linkedin.profile`, bounded `profile_history` and distinct `recent_posts` when its read connection is configured. LinkedIn observations carry their own dates and per-source coverage.
- `hiring`, `innovation`, `activity`, `reputation`, `share_of_voice`: separate enrichment observations with source coverage and date limitations.

`available` means the field was observed, including an empty list or numeric zero.
`not_observed` means no stored observation; `unavailable` means the store failed;
`partial` and array truncation remain explicit. Missing values never become zero.

## Contacts, financials and briefs

Request company emails or phone numbers with `get_company_contacts`; request a
professional's contact using a person ID returned by `search_people` and
`get_person_contacts`. Both require the explicit `contacts` key scope and the
linked Radar account's paid-plan check. Company-domain fallback is labeled and
must not be treated as a verified personal contact. See [contact retrieval](CONTACTS.md).

Financial history remains in `get_financials` with period, currency, source and
access-limit metadata. `company_brief` now returns concise section summaries and
separate detail requests, rather than embedding the complete profile and archives.
The image URL uses Radar's first-party image route; that route can fall back to a
favicon. Stored provider CDN logo URLs are not passed through.

See [profile reference](reference/get_company.md), [field reference](reference/get_company_field.md),
[filters and listings](FILTERS_AND_LISTINGS.md), [source review](RADAR_SOURCE_REVIEW.md)
and [data quality](DATA_QUALITY.md).
"""
    text += render_examples()
    (ROOT / "docs/COMPANY_DATA_DEPTH.md").write_text(text)


if __name__ == "__main__":
    build()
