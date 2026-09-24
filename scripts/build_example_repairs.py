#!/usr/bin/env python3
"""Publish actual replacement captures and explain unresolved empty examples."""
import json
from pathlib import Path

from audit_examples import content_check
from build_endpoint_docs import digest, encoded, excerpt
from capture_example_replacements import CASES

ROOT = Path(__file__).resolve().parents[1]
NOTES = {
    "yext-products.json": ("Yext: populated product names", "The source returns three product names. These are the recorded labels, not independently verified current commercial offerings. This is a companion to the observed-empty Razorpay and Swiggy products captures; their company-specific files remain unchanged."),
    "yext-activity.json": ("Yext: populated stored business activity", "This selected activity field returns three dated source records: one event-marketing item and two product-launch items. It is a stored company field, not the account-limited recent timeline from get_company_events. The source's event associations have not been independently verified; the July marketing item in particular requires review before describing it as a Yext corporate event."),
    "mastech-annual-income.json": ("Mastech Digital: a second populated annual income example", "FY2025 revenue is USD 191,371,000 and net income is USD -609,000, with news_report provenance. Negative profit is retained. This smaller-company capture provides another real annual response; it does not establish filing-only, balance-sheet or cash-flow availability."),
}


def main():
    raw = {r["file"]: r for r in json.loads((ROOT / "qa/private/example-replacements.json").read_text())}
    folder = ROOT / "docs/examples/additional"
    folder.mkdir(exist_ok=True)
    text = """# Empty example review and smaller-company replacements

Reviewed every saved response capture on 2026-09-24, including selected company,
app and investor fields, scenarios, endpoint examples and contact fixtures.
The [complete audit](EXAMPLE_AUDIT.md) lists each file, date, status and whether
the requested data is populated. Capture timestamps remain individual; reviewing
all saved examples does not imply every source was queried again today.

## What changed

| Previous example | Current documented result | Interpretation |
|---|---|---|
| Microsoft annual income returned no periods | [electroCore FY2024](scenarios/14-annual-income.md): revenue, net income, EBITDA and EPS | Populated annual income, with news provenance and negative values preserved |
| Microsoft quarterly income | [electroCore quarterly income](scenarios/16-quarterly-income.md) | Two accessible quarters, each with revenue and EPS |
| Microsoft positive-profit screen returned no matches | [Qualys annual profit/revenue screen](scenarios/19-precise-profit-screen.md) | One match; the sample threshold explicitly changed from USD 1B to USD 100M |
| Microsoft/Python structured-skills job query returned no rows | [Connvertex Python role-title query](scenarios/39-company-skill-jobs.md) | Two records; a title search does not assert structured skill coverage |
| Razorpay/Swiggy product fields were empty | [Yext products](examples/additional/yext-products.json) below | Three actual source labels; original company-specific coverage cases retained |
| Razorpay activity field was absent | [Yext activity](examples/additional/yext-activity.json) below | Three stored dated activity rows, distinct from the recent timeline endpoint |
| Only large-company financial examples | [Mastech Digital annual income](examples/additional/mastech-annual-income.json) below | Revenue and net income with source provenance |

Original scenario requests and responses remain in each baseline. Sample changes
are labeled `sample_replacement`; they do not masquerade as fixes to identical
business predicates. The original under-$10,000 US AdTech request is preserved.

## Balance sheets and cash flow are still blocked

[Scenario 13](scenarios/13-balance-sheet.md) now uses electroCore rather than
Microsoft. It returns a FY2024 label but **no balance-sheet metrics**.
[Scenario 15](scenarios/15-annual-cash-flow.md) likewise contains no cash-flow metrics.
Both pages are clearly marked blocked coverage examples, not successful tutorials.

Strict read-only checks on 2026-09-24 found that the financial filings and
company-resolution stores failed on an unreachable shard (connection/socket
timeouts). Six live company probes returned news-derived income or no periods;
none returned official balance-sheet or cash-flow metrics. Available cached source
snapshots were expired and were not substituted into live responses. The upstream
can return HTTP 200 income-only data when its filing read fails. This is an
upstream observability gap: the response alone cannot distinguish a failed filing
read from a missing statement. The connection must be repaired and these exact
requests recaptured before claiming that those examples yield usable statements.
No database write, service restart or entitlement bypass was performed.

For a working annual-income request, use [scenario 14](scenarios/14-annual-income.md).
For balance sheets, require numeric `total_assets`, `total_liabilities` or
`stockholders_equity` in `periods[].metrics`; for cash flow, require a cash-flow
metric. Period labels, `has_data=true`, archive counts and company assessments are
not substitutes. A known zero or negative metric is still valid data.

## Other empty examples and the appropriate next step

| Coverage case | What to do |
|---|---|
| [US AdTech below USD 10K](scenarios/03-usa-adtech-under-10k.md) | Keep the original threshold; unknown annual evidence is not a match. Page through bounded candidates. [Scenario 04](scenarios/04-usa-adtech-over-1m.md) is a separately labeled positive screen. |
| [Indian seed USD 10K–100K shortlist](scenarios/11-seed-small-round.md) | The strict page excluded expanded candidates. Follow continuation when available; do not weaken country, stage or round filters silently. |
| [Normalized Shine internships](scenarios/38-normalized-interns.md) | No rows, including a broader internship-type recheck. Use the separate [internship corpus example](scenarios/41-remote-part-time-interns.md) for populated observed listings. |
| [Recent company events](reference/get_company_events.md) | The source account's effective window can be shorter than requested; a 365-day electroCore probe was also empty. Yext's stored activity field below is a distinct operation, not a replacement timeline. |
| Selected innovation fields | All three saved company examples are absent; a bounded native lookup found no positive patent-family row. No fabricated patent sample or stale snapshot was substituted. |
| [Founder professional lookup](examples/contacts/founder-professional.json) | The exact name-plus-company query was empty. [Contact guidance](CONTACTS.md) retains the populated separate lookup and conflicting source affiliations; it does not invent an identity match. |
| Location and News errors | Genuine upstream/coverage failures remain visible. Historical successful News captures retain dates and are not proof of current availability. |
| Contact denials and empty contact fixtures | Expected default-key scope denials and deliberately empty selected contact types; successful contact wire shapes are labeled synthetic fixtures. |

## Complete populated companion responses

These are actual authenticated gateway responses with every returned business row
retained. Identified source prose may be omitted under the same projection rules
as the endpoint reference; every omission and response hash is in the JSON file.
These endpoints require your configured base URL and API key. MCP uses the same
operation name with the JSON body in `arguments.request`.
"""
    for filename, operation, request in CASES:
        row = raw[filename]
        assert row["operation"] == operation and row["request"] == request
        assert content_check(operation, request, row["http_status"], row["response"])["state"] == "populated", filename
        response, omitted = excerpt(operation, row["response"])
        capture = {**{k: v for k, v in row.items() if k != "file"}, "response": response,
                   "omitted_paths": omitted, "credential_redactions": [],
                   "hash_basis": "Parsed sorted JSON; every business row retained after explicit source prose omissions",
                   "original_response_sha256": digest(row["response"]), "response_excerpt_sha256": digest(response)}
        (folder / filename).write_text(encoded(capture))
        title, note = NOTES[filename]
        text += f"\n### {title}\n\n{note}\n\n**POST `{row['path']}`** · MCP `{operation}` · HTTP {row['http_status']} · captured {row['captured_at']}.\n\n"
        text += f"<!-- replacement-request: {filename} -->\n```json\n{encoded(request).rstrip()}\n```\n\n"
        text += f"<!-- replacement-response: {filename} -->\n```json\n{encoded(response).rstrip()}\n```\n\n[Full capture and provenance](examples/additional/{filename}).\n"
    text += "\n## Reproduce the review\n\nIn an operator-configured environment, `scripts/capture_example_replacements.py` recaptures the three companion examples. `scripts/stress_scenarios.py --round examples-20260924 --only 13-balance-sheet 14-annual-income 15-annual-cash-flow 16-quarterly-income 19-precise-profit-screen 39-company-skill-jobs` recaptures the six changed scenarios. Render with `scripts/build_example_repairs.py`, `scripts/build_scenario_docs.py` and `scripts/build_endpoint_docs.py`, then run `scripts/check_docs.py`. Raw captures and credentials remain ignored. The checker rejects empty positive samples, stale response hashes and rewritten baseline requests.\n"
    (ROOT / "docs/EXAMPLE_REPAIRS.md").write_text(text)


if __name__ == "__main__":
    main()
