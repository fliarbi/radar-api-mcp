#!/usr/bin/env python3
"""Report failed, empty, limited and fixture-backed examples without hiding them."""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def assess(record):
    name = record["operation"]
    payload = record["response"]
    data = payload.get("data") or {}
    notes = []
    if record["http_status"] >= 400:
        prefix = "Expected default-key contact denial: " if record["http_status"] == 403 and name in {"get_company_contacts", "get_person_contacts"} else "Unsuccessful: "
        notes.append(prefix + payload.get("error", {}).get("kind", "HTTP error"))
    elif isinstance(data, dict):
        if payload.get("meta", {}).get("partial") or data.get("partial") or data.get("partial_timeout"):
            notes.append("Partial response")
        for key in ("companies", "jobs", "people", "items", "events", "matches"):
            if key in data and isinstance(data[key], list):
                notes.append(f"{len(data[key])} {key}" + ("; empty result" if not data[key] else ""))
        if name == "find_competitors":
            notes.append(f"{sum(len(rows) for rows in data.get('companies', {}).values())} peer cards across stages")
        if name == "get_job" and data.get("job"):
            notes.append("Resolved listing ID; salary can be missing")
        if name == "get_company_field":
            notes.append("Requested field: " + str(data.get("field")) + "; " + str(data.get("status")))
        if name == "get_company":
            notes.append("Profile depth: " + data.get("profile_depth", "unspecified"))
        if name == "get_investor_page" and not (data.get("portfolio") or data.get("investors")):
            notes.append("Metadata only; source roster access boundary")
        if name == "company_brief":
            sections = data.get("sections", {})
            notes.append(f"{sum(bool(v.get('available')) for v in sections.values())}/{len(sections)} sections available")
            for section, value in sections.items():
                if value.get("error"):
                    notes.append(section + ": " + value["error"].get("kind", "unavailable"))
        if name == "salary_benchmark":
            notes.append(f"{data.get('count', 0)} salary observations; " + ("sparse" if data.get("sparse") else str(data.get("currency"))))
        if data.get("access_limited"):
            notes.append("Financial archive access limited")
        if data.get("truncated"):
            notes.append("Source history/result window truncated")
        if data.get("total_capped"):
            notes.append("Count or aggregation capped")
        if data.get("has_data") is False:
            notes.append("No data supplied")
        if isinstance(data.get("companies"), list) and any(
            c.get("name", "").lower() in {"anon", "anonymous"} or c.get("domain") == "linkedin.com"
            for c in data["companies"]):
            notes.append("Ambiguous investor identity present; review source association")
        if name == "market_pulse":
            year = int(record["captured_at"][:4])
            serialized = json.dumps(data.get("recent_fundings", []))
            if any(int(y) > year for y in re.findall(r'"(20\d\d)-\d\d-\d\d', serialized)):
                notes.append("Future-dated funding candidate; not verified recent activity")
            if '"latest_deal_amount": -1' in serialized:
                notes.append("Unknown funding amount sentinel -1")
        if data.get("amount_approx"):
            notes.append("Approximate reported funding")
        if payload.get("window", {}).get("freshness"):
            notes.append("Source freshness qualification applies")
    if record["capture_kind"] == "local_account_fixture":
        notes.append("Synthetic identity/payment fixture; no production activation verified")
    elif record["capture_kind"] == "live_data_integration":
        notes.append("Real data with isolated News identity/quota; no deployed News connection verified")
    if not notes:
        notes.append("Captured response; source accuracy and completeness not independently audited")
    return {"operation": name, "http_status": record["http_status"], "capture_kind": record["capture_kind"],
            "captured_at": record["captured_at"], "response_sha256": record["response_excerpt_sha256"],
            "observations": notes}


def report():
    manifest = json.loads((ROOT / "docs/examples/index.json").read_text())
    rows = [assess(json.loads((ROOT / "docs/examples" / (r["operation"] + ".json")).read_text())) for r in manifest]
    return {"scope": "All checked-in endpoint examples; capture dates and methods remain per operation",
            "operations": len(rows), "http_status_counts": dict(sorted(Counter(str(r["http_status"]) for r in rows).items())),
            "capture_methods": dict(sorted(Counter(r["capture_kind"] for r in rows).items())), "examples": rows}


def build():
    result = report()
    (ROOT / "docs/EXAMPLE_AUDIT.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    text = """# Endpoint example audit: errors, empty results and coverage limits

This report checks every published JSON endpoint example, including HTTP 200
responses that are empty, partial, restricted or produced with test identities.
Each row links to its request, actual response and field explanations. Capture
dates below are the dates of that operation's evidence; this audit does not imply
that every endpoint was retested on the same day or that a public service exists.

The 2026-09-21 review replaced the empty job-search, hiring-company and salary
examples with narrower successful requests; job detail now uses a returned real
ID. A Payments query supplies populated competitor groups. Investor search was
recaptured successfully, and the Stripe brief now contains a successful News
section using the documented isolated News integration identity.

The compact-profile revision adds separate field retrieval, filter discovery,
selected listing columns and scoped contact lookups. The default key is correctly
denied contact access; paid contact response shapes are tested with synthetic data.

**Remaining limitations:** location intelligence still returns a real upstream
failure. The investor-page source intentionally returns metadata only. The company
event example has an empty account-limited recent window. Market pulse contains
future dates and an unknown-amount sentinel. Successful investor search also
contains an ambiguous anonymous identity. These conditions remain visible; they
are not replaced with invented statistics or unrestricted records.

The [machine-readable audit](EXAMPLE_AUDIT.json) records response fingerprints;
the documentation validator rejects stale audit output. See [data quality](DATA_QUALITY.md)
and [verification](VERIFICATION.md) for source and deployment boundaries.

| Operation | HTTP | Observed data and qualifications | Capture date | Method |
|---|---:|---|---|---|
"""
    for row in result["examples"]:
        name = row["operation"]
        notes = "; ".join(row["observations"]).replace("|", "&#124;")
        text += f"| [{name}](reference/{name}.md) | {row['http_status']} | {notes} | {row['captured_at'][:10]} | `{row['capture_kind']}` |\n"
    (ROOT / "docs/EXAMPLE_AUDIT.md").write_text(text)
    print(f"Audited {result['operations']} endpoint examples: {result['http_status_counts']}")


if __name__ == "__main__":
    build()
