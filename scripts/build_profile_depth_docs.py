#!/usr/bin/env python3
"""Publish reviewed rich-profile captures and a concrete field walkthrough."""
import json
from pathlib import Path

from build_endpoint_docs import digest, encoded, excerpt

ROOT = Path(__file__).resolve().parent.parent


def build():
    examples = ROOT / "docs/examples/profiles"
    examples.mkdir(parents=True, exist_ok=True)
    records = {}
    for domain in ("razorpay.com", "stripe.com", "swiggy.com"):
        raw = json.loads((ROOT / "qa/private" / f"profile-{domain}.json").read_text())
        response, omitted = excerpt("get_company", raw)
        record = {"operation": "get_company", "method": "POST", "path": "/v1/companies/profile",
                  "request": {"domain": domain}, "http_status": 200,
                  "captured_at": raw["meta"]["retrieved_at"],
                  "provenance": "Executed authenticated gateway request using the live detailed company store",
                  "response": response, "omitted_paths": omitted,
                  "original_response_sha256": digest(raw), "response_excerpt_sha256": digest(response)}
        (examples / f"{domain}.json").write_text(encoded(record))
        records[domain] = record
    table = []
    for domain, record in records.items():
        c = record["response"]["data"]["company"]
        table.append(f"| [{c['name']}](examples/profiles/{domain}.json) | {len(c['classification']['sectors'])} | "
                     f"{len(c['classification']['feeds']['primary'])} / {len(c['classification']['feeds']['other'])} | "
                     f"{len(c['people']['founders'])} | {len(c['technology']['website_stack'])} | "
                     f"{c['traffic']['visits']:,} | {c['apps']['count']} / {c['apps']['downloads']:,} |")
    razorpay = records["razorpay.com"]["response"]["data"]["company"]
    (ROOT / "radar_api/static/company-profile-example.json").write_text(encoded(records["razorpay.com"]["response"]))
    stripe = records["stripe.com"]["response"]["data"]["company"]
    # Explicit selected blocks in this walkthrough; downloadable records preserve
    # every returned business field and row except documented review snippets.
    featured = {"classification": razorpay["classification"], "people": razorpay["people"],
                "technology": razorpay["technology"], "traffic": razorpay["traffic"], "apps": razorpay["apps"]}
    text = """# Company data depth: real sectors, feeds, founders, technology, traffic and apps

Radar's company profile API now reads the grouped company record and associated
enrichment. The earlier gateway used a shortlist card, and its documentation then
removed fields and cut arrays to two items. Those choices understated the available
data. The API now exposes seventeen selectable sections, and documentation preserves
all captured business fields and all returned array rows.

## Three live examples with meaningful depth

These are measured fields from authenticated local API calls on **2026-09-20**.
They are source observations, not independently audited current company facts.
Traffic dates and website crawl dates are returned separately; downloads are
aggregate source totals, not active users or downloads in a stated recent month.

| Complete captured company JSON | Sectors | Primary / other feeds | Founders | Stack entries | Visits in source observation | Apps / downloads |
|---|---:|---:|---:|---:|---:|---:|
""" + "\n".join(table) + """

Each linked file contains the exact request, response, capture date, omission paths
and checksums. No company array is cut to two entries. The longer review snippets
are omitted from documentation reproduction, with their paths recorded explicitly.
The [profile endpoint reference](reference/get_company.md) shows the complete primary
Razorpay response inline, including sections beyond the five highlighted below.

## Retrieve the data

```bash
curl --fail-with-body "$RADAR_API_URL/v1/companies/profile" \\
  -H "Authorization: Bearer $RADAR_API_KEY" \\
  -H 'Content-Type: application/json' \\
  -d '{"domain":"razorpay.com","item_limit":100}'
```

With the detailed store connected, omitting `sections` requests all seventeen.
For a focused integration, use `sections=["classification","people","technology",
"traffic","apps"]`. This is one `get_company` operation and one successful-operation
credit in account mode. REST and MCP share the same result; MCP wraps this body
in `arguments.request`. `item_limit` defaults to 100 per array and supports 1–250.
Every capped array reports its available and returned count in `coverage.arrays`.
None of the arrays in these three captures needed truncation.

The operator enables this data connection with `RADAR_PROFILE_MONGO_URI`; caller
requests never accept database names, collection names, queries or connection
strings. An unconfigured deployment explicitly returns `profile_depth=card`.
See [private operator setup](OPERATIONS.md); these captures do not represent a
production deployment or public API launch.

## Classification is more than one industry label

`classification.sectors` contains practice-area labels. `markets` preserves the
existing primary-market convention, while `feeds.primary` and `feeds.other` make
the richer feed hierarchy explicit. Business models describe how the company
operates; revenue models describe its monetization categories. Flags retain their
source values such as YES, NO or Untagged instead of turning unknown into false.

Razorpay's full captured classification, founder, technology, traffic and app blocks:

<!-- depth-highlight: razorpay.com -->
```json
""" + encoded(featured).rstrip() + """
```

## Founders and professional context

Razorpay's record names Shashank Kumar as Co-Founder & Managing Director and Harshil
Mathur as Co-Founder & CEO. The `founders` array is selected from key people whose
source designation contains “founder”; it is not an independent current-role audit.
Stripe has four key-person records and two matching founders. Other executive
roles remain in `key_people`, including source labels that explicitly describe
former positions. Professional names and roles are separate from contact reveal.

## Technology, website quality and traffic are different observations

`technology.website_stack` retains the grouped technology list. The observed web
scan can have a different count: Razorpay has 70 merged stack entries and 69 in its
observed-technology array. The API preserves both and the observation date.
`technographics` can separately identify a category and technology, such as an
infrastructure platform. No technology name is inferred from the company's sector.

`web_presence` adds rank, CDN, performance measurements, SEO signals, structured
data, schema types and a derived digital-presence score. `traffic` instead contains
visits, observation date, bounce fraction, pages per visit, search keywords and
country audience shares. A rank is not a visit count, and visits are not unique
customers. Numeric fractions are retained as fractions, not silently multiplied
into percentages or combined into an invented growth rate.

## App metrics have explicit scope

`apps.count`, `downloads` and `weighted_rating` are aggregate source fields. These
records do not expose an app-by-app list, package IDs, store URLs or rating dates;
the API does not invent them. Preserve the full returned numeric rating or round it
only for presentation. Do not interpret a missing rating as zero or total downloads
as monthly active users.

## Products, hiring, patents and social data

Stripe's populated product and social blocks illustrate additional depth:

<!-- depth-highlight: stripe.com -->
```json
""" + encoded({"products": stripe["products"], "social": stripe["social"]}).rstrip() + """
```

The complete Stripe example also contains hiring totals and first/last dates,
monthly/yearly counts, roles and locations; innovation includes patent-family,
grant, citation, year and area observations. Those represent the source's stored
history and aggregates, not a guarantee that every vacancy is still open or that
every patent represents a current commercial product. The detailed profile and
[enrichment endpoint](reference/get_company_enrichment.md) both expose this context.

## Field dictionary and availability

| Section | Content | Important distinction |
|---|---|---|
| `classification` | Sectors, primary/other feeds, business/revenue models, industries, company types, flags | Untagged is not NO |
| `people` | Key people, designations, derived founder subset, background categories | Source role is not a verified current appointment |
| `technology` | Merged stack, observed technologies, technographics, observation date | Merged and observed counts can differ |
| `web_presence` | Rank, CDN, performance, SEO, structured data, score, crawl date | Measurements and derived labels retain separate meanings |
| `traffic` | Visits/date, countries, keywords, bounce and pages per visit | Traffic is not revenue or customer count |
| `apps` | Count, downloads, weighted rating | Aggregates, not a per-app roster |
| `products` | Returned product labels | Empty source list is not proof of no products |
| `geography` | Headquarters, locations, served geographies, coordinates, business addresses | Headquarters and markets served are different |
| `social` | Profile links, followers, engagement, posting cadence and benchmarks | Source dates/denominators may differ |
| `lifecycle` | Stage, financing/ownership status and public/deadpool indicators | Unknown values remain unknown |
| `legal` | Legal names, registration identifiers, registrars and countries | Review entity associations before joining filings |
| `assessments` | Completion, finance, scalability, momentum and other scores | Derived scores are not financial amounts |
| `hiring` | Counts, dates, history, roles and locations | Stored observations do not certify current vacancies |
| `innovation` | Patent families, grants, citations, years, areas and notable items | Patents are not a complete product inventory |
| `activity` | Dated source activity entries | Available history varies by company |
| `reputation` | Source review aggregates and counts | Documentation omits individual review snippets |
| `share_of_voice` | Peers and available audience/review/follower shares | Denominator is the supplied comparison cohort |

`coverage.sections` distinguishes available, not_observed, unavailable and partial.
Empty arrays and numeric zero remain valid source values. Database failures return
503; they do not silently become an empty company. If optional enrichment fails,
the available base profile survives with explicit partial coverage.

Several company records can share a domain. In that case, the detailed lookup
returns **409 `ambiguous_company`** and accepts a public `company_id` alongside
the domain for disambiguation. A wrong ID/domain pair cannot return another entity.
Financial history and estimated-revenue access continue through the existing
entitlement-checked financial endpoint; adding profile depth does not unlock them.

Related: [company lookup](guides/company-data-api.md), [enrichment](guides/company-enrichment-api.md),
[financial data](guides/financial-data-api.md), [all endpoint outputs](reference/README.md).
"""
    (ROOT / "docs/COMPANY_DATA_DEPTH.md").write_text(text)
    print("Rendered three full company examples and the field-depth walkthrough")


if __name__ == "__main__":
    build()
