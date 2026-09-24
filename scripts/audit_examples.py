#!/usr/bin/env python3
"""Report failed, empty, limited and fixture-backed examples without hiding them."""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def content_check(operation, request, status, response):
    """Distinguish useful requested data from a successful response envelope."""
    if status >= 400 or response.get("ok") is False:
        expected = status == 403 and operation in {"get_company_contacts", "get_person_contacts"}
        return {"state": "expected_denial" if expected else "unavailable", "reason": response.get("error", {}).get("kind", str(status))}
    data = response.get("data")
    if operation == "get_financials":
        families = {
            "income": {"revenue", "gross_profit", "operating_income", "net_income", "ebitda", "eps"},
            "balance_sheet": {"total_assets", "total_liabilities", "stockholders_equity", "cash", "long_term_debt"},
            "cash_flow": {"operating_cash_flow", "investing_cash_flow", "financing_cash_flow", "free_cash_flow", "capex"},
        }
        allowed = families.get((request or {}).get("statement"), set().union(*families.values()))
        count = sum(
            any(k in allowed and isinstance(v, dict) and isinstance(v.get("value"), (int, float))
                and not isinstance(v["value"], bool) for k, v in p.get("metrics", {}).items())
            for p in (data or {}).get("periods", [])
        )
        return {"state": "populated" if count else "empty", "reason": f"{count} periods with numeric metrics in the requested statement family"}
    if isinstance(data, dict):
        if operation in {"get_company_contacts", "get_person_contacts"}:
            requested = (request or {}).get("fields", ["emails", "phones"])
            count = sum(len(data.get(field) or []) for field in requested)
            return {"state": "populated" if count else "empty", "reason": f"{count} values in requested contact types; fixture provenance remains separate"}
        if operation in {"get_company_field", "get_investor_field", "get_app_field"}:
            value = data.get("value")
            present = value is not None and value != [] and value != {} and value != ""
            return {"state": "populated" if present else "empty", "reason": "Selected field " + str(data.get("field")) + (" contains data" if present else " has no returned value")}
        row_keys = {
            "search_companies": "companies", "search_people": "people", "get_company_team": "people",
            "search_jobs": "jobs", "get_company_events": "events", "screen_company_financials": "matches",
            "search_apps": "apps", "company_apps": "apps", "search_internships": "internships",
            "companies_offering_internships": "companies", "company_filter_options": "options",
            "search_news": "items", "search_business_news": "items", "search_business_events": "items",
        }
        key = row_keys.get(operation)
        if key and isinstance(data.get(key), list):
            count = len(data[key])
            return {"state": "populated" if count else "empty", "reason": f"{count} {key}; totals and context do not substitute for requested rows"}
        if operation == "salary_benchmark":
            count = data.get("count") or 0
            return {"state": "populated" if count else "empty", "reason": f"{count} salary observations"}
        if data.get("has_data") is False or data.get("profile_depth") == "not_found":
            return {"state": "empty", "reason": "Source reports no accessible data"}
    return {"state": "populated" if data or "data" not in response else "empty", "reason": "Response content present" if data or "data" not in response else "No response data"}


def all_captures():
    """Include fields, scenario current results, investor/app/contact and extra captures."""
    rows = []
    for path in sorted((ROOT / "docs/examples").rglob("*.json")):
        record = json.loads(path.read_text())
        if not isinstance(record, dict):
            continue
        capture = record.get("current", record)
        if not isinstance(capture.get("response"), dict) or "http_status" not in capture:
            continue
        operation = record.get("operation") or capture["response"].get("feature")
        if not operation:
            continue
        check = content_check(operation, record.get("request"), capture["http_status"], capture["response"])
        kind = capture.get("capture_kind", record.get("capture_kind"))
        data = capture["response"].get("data") or {}
        empty_arrays = [key for key, value in data.items() if value == []] if isinstance(data, dict) else []
        rows.append({"file": str(path.relative_to(ROOT / "docs")), "operation": operation,
                     "http_status": capture["http_status"], "captured_at": capture["captured_at"],
                     "capture_kind": kind, "synthetic_fixture": "fixture" in (kind or ""),
                     "empty_top_level_arrays": empty_arrays,
                     "response_sha256": capture["response_excerpt_sha256"], **check})
    return rows


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
        for key in ("companies", "jobs", "people", "items", "events", "matches", "apps", "internships"):
            if key in data and isinstance(data[key], list):
                notes.append(f"{len(data[key])} {key}" + ("; empty result" if not data[key] else ""))
        if name == "find_competitors":
            notes.append(f"{sum(len(rows) for rows in data.get('companies', {}).values())} peer cards across stages")
        if name in {"search_internships", "companies_offering_internships", "get_internship"}:
            notes.append("Observed internship records; current openings are unverified and deadlines can be expired or placeholders")
        if name in {"search_apps", "company_apps", "get_app", "get_app_field"}:
            notes.append("Dated Google Play observations; not a current store check")
        if name == "get_app":
            notes.append(str(data.get("history_points", 0)) + " stored history rows; source duplicates can repeat dates")
        if name == "search_opportunities":
            notes.append("Explicit " + data.get("preset", "") + " screen with " + str(len(data.get("evidence", []))) + " evidence rows; no predicted returns or verified purchase intent")
        if name == "get_job" and data.get("job"):
            notes.append("Resolved listing ID; salary can be missing")
        if name == "get_company_field":
            notes.append("Requested field: " + str(data.get("field")) + "; " + str(data.get("status")))
        if name == "get_company":
            notes.append("Profile depth: " + data.get("profile_depth", "unspecified"))
        if name == "get_investor_page":
            notes.append("Investor depth: " + data.get("profile_depth", "unspecified"))
            notes.append(str(len(data.get("available_fields", []))) + " available detail fields")
        if name == "get_investor_field":
            page = data.get("pagination", {})
            notes.append(str(page.get("returned", "object")) + " returned; " + str(page.get("source_total", "n/a")) + " stored rows")
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
    captures = all_captures()
    return {"scope": "All checked-in response captures, including current scenarios and selected fields; historical baselines retained separately. This is a saved-output audit, not a claim of simultaneous live availability.",
            "operations": len(rows), "http_status_counts": dict(sorted(Counter(str(r["http_status"]) for r in rows).items())),
            "capture_methods": dict(sorted(Counter(r["capture_kind"] for r in rows).items())), "examples": rows,
            "capture_count": len(captures), "content_counts": dict(sorted(Counter(r["state"] for r in captures).items())),
            "all_captures": captures}


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
failure. Investor profiles now expose measured summaries and separate verified detail fields. The company
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
    text += f"\n## All saved response captures\n\nChecked **{result['capture_count']}** captures across every example folder. "
    text += "; ".join(f"**{n} {state}**" for state, n in result["content_counts"].items()) + ".\n\n"
    text += "A financial example needs a numeric metric in the requested statement family. A period label, archive count or company summary alone does not qualify. Zero and negative values do qualify as data. Empty matches are retained as coverage cases, never advertised as positive results. Synthetic contact/account examples retain their fixture labels. See [sample replacements and source failures](EXAMPLE_REPAIRS.md).\n\n"
    text += "| Capture | Requested output | Content | Detail | Evidence date | Method |\n|---|---|---|---|---|---|\n"
    for row in result["all_captures"]:
        detail = row['reason'] + ("; empty arrays: " + ", ".join(row['empty_top_level_arrays']) if row['empty_top_level_arrays'] else "")
        text += f"| [{row['file']}]({row['file']}) | `{row['operation']}` | {row['state']} | {detail} | {row['captured_at'][:10]} | `{row['capture_kind']}` |\n"
    (ROOT / "docs/EXAMPLE_AUDIT.md").write_text(text)
    print(f"Audited {result['operations']} endpoint examples: {result['http_status_counts']}")


if __name__ == "__main__":
    build()
