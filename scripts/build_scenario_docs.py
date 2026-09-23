#!/usr/bin/env python3
"""Render the fixed scenario audit from captured evidence, never synthetic success."""
from collections import Counter
import json
from pathlib import Path
from build_endpoint_docs import digest, encoded, excerpt
from scenario_cases import CASES
from stress_scenarios import assess

ROOT = Path(__file__).resolve().parents[1]

INTERPRET = {
    "company_filter_options": "Use the returned values only in the requested filter field. Industry, sector, market and location vocabularies are distinct. The option limit bounds suggestions, not the searchable company population.",
    "search_companies": "Read each match_tier and the matching/excluded_candidates count before accepting the shortlist. Strict is the source's label, not an independent verification of every company attribute. Financial bands refer to source summary fields, not a selected fiscal year; retrieve financial evidence separately. Advance source pages even if strict filtering leaves an empty page with a continuation hint.",
    "screen_company_financials": "Read all evaluated rows, not just matches. Numeric conditions use the same latest accessible fiscal period. Unknown means missing or disallowed evidence; unavailable means a failed read. Neither becomes zero. This is a bounded candidate screen with source gates, not an exhaustive company database query. Its per-metric checks preserve currency, source type and inclusive/exclusive bounds.",
    "get_financials": "Preserve fiscal year, fiscal period, statement family, source type and available dates. Empty annual rows with access_limited do not prove the archive has no annual statements. No annual values are synthesized by adding quarters, and a filing date is not substituted for an absent period end.",
    "get_company_funding": "These are reported whole-round amounts and associations, not sales revenue or a particular investor's cheque. Reconcile approximate values, recipient identity and repeated announcements before totaling capital raised.",
    "get_company_columns": "Columns contain formatted display values. Empty display values do not establish zero; source formatting can suppress zero or negative numbers. For exact financial comparisons use dated numeric financials.",
    "financial_filter_catalog": "Legacy source revenue bands have open boundaries and exclude zero. Use exact numeric constraints when the threshold matters. The catalogue documents accepted predicates, not whether a particular company has enough financial evidence to evaluate them.",
    "get_company_team": "Founders and key people are company records; professionals are source profile cards filtered to an exact recorded company domain. Neither is a verified current employee roster. Keep update dates, excluded affiliations and partial flags. Highest career seniority can differ from a current role, and card count is not headcount.",
    "search_people": "Source people cards retain skills, education, experience and professional rankings. Skills and CV arrays are bounded source summaries; an omitted skill can be elsewhere in a full source profile. Highest seniority is a career attribute. Company-name/domain search is prefix-based; use get_company_team for an exact-domain affiliation check. Contact values require a separate scoped endpoint.",
    "company_apps": "Company association uses the exact normalized developer website host. It can miss products with a different developer or parent-company domain; it must not accept a lookalike suffix. Store observations are dated and not verified current listings.",
    "search_apps": "The rating and install predicates are checked against captured structured app values. Keep category, observation date and developer identity. Installs are not active users, revenue or paying customers.",
    "get_app_field": "Retain the selected field's source structure and observation date. Install history counts stored rows, including duplicates, rather than unique dates. Growth uses dated measurements and the actual interval; ratings and monetization are observations, not forecasts or revenue estimates.",
    "search_jobs": "Job listings are observed recruitment records. Preserve role, location, skills, source dates and absent salary/domain values. Employment-type aliases are normalized by the gateway. An advertised vacancy does not prove a hire or a currently open position.",
    "salary_benchmark": "Read count, sparse, currency and filter_echo alongside the distribution. The source aggregates salary midpoints. Do not invent a monthly or annual pay period that the response does not supply.",
    "search_internships": "The source explicitly selects internship records. Remote means supporting source evidence, not an assumption from a city name. Preserve stipend currency and its unknown pay period. Expired or far-future deadlines do not establish a current opening; current_opening_verified stays false.",
    "companies_offering_internships": "Employers are grouped by exact source name, not a verified corporate domain. Counts describe observed internship records, including old postings. Use sample IDs to inspect listings; do not call the count verified current vacancies.",
    "get_investor_field": "This is a dated published research snapshot. Keep data_through, release and cohort definitions. Portfolio amounts are whole-round amounts, sectors can overlap, and a co-investor relationship is not proof of a current partnership or investment mandate.",
    "get_company_field": "Only the requested detail field is returned. Preserve field_status, source update date, nested business structures and array coverage. Missing observations do not become zero or proof that the company lacks a technology, market or traffic source.",
    "search_business_news": "This run uses actual News application queries and live data with an isolated test identity and quota dependencies. It does not verify a production News connection. The current upstream failure remains an error example; older successful captures are not substituted into this run.",
}
SPECIAL = {
    "03-usa-adtech-under-10k": "The three observed domains were adster.tech, markopolo.ai and topsort.com. All three lacked accessible annual periods, so this run established no below-$10,000 match. Startup is explicitly defined by founded_year_from=2021, not inferred from company size.",
    "04-usa-adtech-over-1m": "The source reported FY2025 revenue of USD 86,000,000 for Inuvo and USD 282,900,000 for PubMatic; both metric sources are news_report, not filing. The third candidate was unresolved. The captured values are reproduced as API evidence, not independently audited financial claims.",
    "05-india-profitable": "The baseline included sep.com in the United States despite an India filter. Its semantic expansion label had been dropped by the gateway. Strict mode now excludes that candidate and retains the two source-labelled strict Indian rows.",
    "11-seed-small-round": "The baseline returned expanded candidates, including a US company. The repaired strict page is empty because its three source candidates were expanded. Do not change the seed/deal filters merely to produce an attractive example; the empty qualified result is part of the finding.",
    "24-microsoft-team": "One retained source card says Researcher Emeritus (ret), and experience data includes an inverted year range. This is evidence of source staleness/inconsistency, so recorded affiliation must not be described as verified present employment.",
    "34-app-history-page": "This page has five identical observed dates and values. The source explicitly reports deduplicated=false and source_total=15. These are stored rows, not five new install measurements.",
    "40-salary-benchmark": "The captured source distribution has 206 observations and a USD 124,000 median. Its absence of an explicit pay period prevents claiming that number is an annual salary solely from this response.",
    "50-company-news": "Default configuration returned 503 in the baseline. The isolated live-data integration returned 502 after an upstream connection timeout. These are different findings: service not connected versus connected query path unable to reach its data source. No source restart or production configuration change was made.",
}


def capture_record(raw, case):
    response, omitted = excerpt(case["operation"], raw["response"])
    return {"captured_at": raw["captured_at"], "capture_kind": raw["capture_kind"] if raw.get("path") else "registry_check",
            "http_executed": bool(raw.get("path")),
            "status_note": "Actual HTTP response" if raw.get("path") else "Operation absent from registry; 404 is an audit sentinel, not an executed HTTP response",
            "http_status": raw["http_status"], "elapsed_seconds": raw["elapsed_seconds"],
            "response": response, "omitted_paths": omitted, "credential_redactions": [],
            "original_response_sha256": digest(raw["response"]), "response_excerpt_sha256": digest(response),
            "assessment": assess(case, raw["http_status"], raw["response"])}


def main():
    baseline = json.loads((ROOT / "qa/private/scenarios-baseline.json").read_text())
    latest = json.loads((ROOT / "qa/private/scenarios-repair2.json").read_text())
    before = {r["id"]: r for r in baseline["results"]}
    after = {r["id"]: r for r in latest["results"]}
    assert set(before) == set(after) == {c["id"] for c in CASES}
    pages, outputs = ROOT / "docs/scenarios", ROOT / "docs/examples/scenarios"
    pages.mkdir(exist_ok=True)
    outputs.mkdir(exist_ok=True)
    records, index = [], []
    for c in CASES:
        assert before[c["id"]]["request"] == after[c["id"]]["request"] == c["request"]
        current, old = capture_record(after[c["id"]], c), capture_record(before[c["id"]], c)
        record = {**c, "method": "POST", "path": after[c["id"]]["path"],
                  "hash_basis": "Parsed sorted JSON; source prose omissions listed explicitly. All returned business fields and array rows preserved.",
                  "provenance": "Local authenticated gateway with live configured read-only sources" if current["capture_kind"] == "live_gateway" else "Actual News application and live query path; isolated test identity/quota; no production connection claim",
                  "baseline": old, "current": current}
        (outputs / (c["id"] + ".json")).write_text(encoded(record))
        records.append(record)
        findings = "; ".join(current["assessment"]["findings"])
        old_findings = "; ".join(old["assessment"]["findings"])
        baseline_label = f"HTTP {old['http_status']}" if old["http_executed"] else "an unavailable operation registry check (no HTTP request)"
        interpretation = INTERPRET[c["operation"]] + ("\n\n" + SPECIAL[c["id"]] if c["id"] in SPECIAL else "")
        page = f'''# {c["question"]}

[All 50 scenarios](README.md) · [Workflow guide](../guides/{c["guide"]}.md) · [Endpoint reference](../reference/{c["operation"]}.md)

**POST `{record["path"]}`** · MCP tool **`{c["operation"]}`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: {c["id"]} -->
```json
{encoded(c["request"]).rstrip()}
```

## Observed result and interpretation

Captured {current["captured_at"]}; HTTP **{current["http_status"]}**;
**{current["assessment"]["outcome"]}**, {current["elapsed_seconds"]} seconds.
{record["provenance"]}.

{findings}.

{interpretation}

The baseline was {baseline_label}, **{old["assessment"]["outcome"]}**:
{old_findings}. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: {c["id"]} -->
```json
{encoded(current["response"]).rstrip()}
```

[Download the current and baseline JSON](../examples/scenarios/{c["id"]}.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
'''
        (pages / (c["id"] + ".md")).write_text(page)
        index.append({k: record[k] for k in ("id", "question", "operation", "guide", "path")})
        index[-1].update(http_status=current["http_status"], outcome=current["assessment"]["outcome"],
                          baseline_outcome=old["assessment"]["outcome"], elapsed_seconds=current["elapsed_seconds"])
    (outputs / "index.json").write_text(encoded(index))
    table = "\n".join(f'| [{r["id"]}]({r["id"]}.md) | {r["question"]} | {r["http_status"]} | {r["outcome"]} |' for r in index)
    (pages / "README.md").write_text('''# 50 executed Radar API questions and full response examples

Each page has an exact REST/MCP request, captured output, baseline comparison and
interpretation. These are bounded read-only tests, not a production capacity or
independent data-accuracy benchmark. Requests were fixed before repairs.

Read the [filter analysis](../FILTER_AUDIT.md) and [feedback and results](../SCENARIO_AUDIT.md).
**Observed** means contract and declared checks passed. **Qualified** means an
explicit source, coverage, freshness or completeness limitation remains.
**Failed** means a tested semantic condition was violated. **Unavailable** means
the operation did not successfully return data. None means all source truth was verified.

| Scenario | Business question | HTTP | Assessment |
|---|---|---:|---|
''' + table + '\n')
    for guide in sorted({c['guide'] for c in CASES}):
        p = ROOT / 'docs/guides' / (guide + '.md')
        s = p.read_text()
        base, marker, tail = s.partition('<!-- captured-workflow -->')
        base = base.split('<!-- scenario-links -->')[0].rstrip()
        links = '\n'.join(f'- [{c["id"]}: {c["question"]}](../scenarios/{c["id"]}.md)' for c in CASES if c['guide'] == guide)
        p.write_text(base + '\n\n<!-- scenario-links -->\n## Executed scenarios for this workflow\n\n' + links + '\n\n' + marker + tail)
    def counts(key):
        return dict(Counter(r[key]['assessment']['outcome'] for r in records))
    times = sorted(r['current']['elapsed_seconds'] for r in records)
    report = {"scenarios": 50, "round": latest['round'], "started_at": latest['started_at'], "finished_at": latest['finished_at'],
              "baseline": counts('baseline'), "current": counts('current'), "concurrency": 2,
              "latency_seconds": {"p50": times[24], "p95": times[47], "max": times[-1]},
              "scope": latest['scope'], "cases": index}
    (ROOT / 'docs/SCENARIO_AUDIT.json').write_text(encoded(report))
    (ROOT / 'docs/SCENARIO_AUDIT.md').write_text(f'''# Radar API and documentation: 50-scenario feedback audit

Executed **50 fixed business questions**, baseline → repair → re-test, on
{latest['finished_at']}. This is a semantic/coverage stress test under bounded read
load, **not a production throughput benchmark**. Maximum scenario concurrency was
2; a financial screen separately limits its reads to 3. No production accounts,
source data or source services were mutated.

| Assessment | Baseline, re-evaluated with the same checks | After repair |
|---|---:|---:|
''' + '\n'.join(f'| {k} | {counts("baseline").get(k,0)} | {counts("current").get(k,0)} |' for k in ('observed','qualified','failed','unavailable')) + f'''

HTTP 200 is not the pass criterion: {sum(r['current']['http_status']==200 for r in records)} requests returned 200, but coverage,
source staleness, missing periods and access gates remain separately qualified.
Observed elapsed times were p50 {times[24]}s, p95 {times[47]}s and maximum {times[-1]}s;
these include local gateway/source latency and caches and do not establish an SLA.

The baseline unavailable count includes ten missing-operation registry checks and
one actual HTTP 503 News response. Registry checks made no HTTP request; their JSON
records mark the stored 404 as an audit sentinel. The repair round executed all
50 HTTP requests. Baseline outcomes were re-evaluated using the same final semantic
checks without altering the original response payloads.

## Feedback that changed the implementation

1. **Wrong industry vocabulary:** AdTech was a valid source dropdown value but the
   gateway queried another industry taxonomy. Suggestions now use the actual Radar
   industry list. The same AdTech request now returns AdTech.
2. **Silent search expansion:** India filters returned US-based sep.com because
   source tier labels were dropped. Structured search now defaults to strict source
   labels, exposes sanitised tier/count metadata, and excludes expanded or unverified
   rows. Explicit expanded mode preserves labels. Stripped filters cannot yield a
   strict shortlist. Tests cover mixed tiers, absent metadata and continued pagination.
3. **No exact revenue workflow:** added the financial filter catalogue and a bounded
   dated-metric screen with inclusive/exclusive bounds, source qualification, consistent
   fiscal periods, unknown/error separation, fan-out limits and settled credit refunds.
4. **No separate team workflow:** added founders, key people and professional groups,
   exact-domain affiliation checks, group-specific filters and separate contact access.
   Incorrect 500-record team retrieval was caught locally and corrected to the existing
   100-record source field limit; professional search pages are independent.
5. **Documentation could not answer concrete questions:** added dedicated financial,
   team and technology/traffic guides plus 50 request/output pages. Guide requests are
   validated against live code models; every scenario is linked from its workflow guide.
   The documentation checker validates request identity, output hashes, full retained
   arrays, source projections and displayed response equality.

## Findings that remain open or qualified

- Under-$10,000 US AdTech startup screening found three unknown annual observations,
  not three qualifying companies. It is not a global exhaustive financial index.
- The positive AdTech screen uses reported annual revenue; its two matches are labelled
  news_report. A filing-only screen may yield different results.
- Preview financial access returned quarterly periods but no annual rows in the Microsoft
  statement scenarios. The API does not bypass the source entitlement.
- People records include retired-role and inconsistent-date evidence. Team affiliation
  means the recorded domain, not verified current employment or employee headcount.
- App history has duplicate stored observations. Internship listings include expired
  deadlines and unresolved employer domains. Investor research retains its dated cutoff.
- News was unconnected in the baseline (503). The isolated live-data query integration
  reached an upstream connection failure (502) in this run. Older successful examples
  remain historical evidence; this run does not claim current News availability.

## Reproduce and inspect

[All 50 request/output pages](scenarios/README.md) and the
[machine-readable audit](SCENARIO_AUDIT.json) retain the exact business questions.
`scripts/scenario_cases.py` defines the fixed matrix. `scripts/stress_scenarios.py`
executes authenticated, bounded read requests in an operator-configured environment.
`scripts/build_scenario_docs.py` renders the captured baseline and repair evidence;
`scripts/check_docs.py` verifies the checked-in result without requiring live data.
Private runtime configuration and raw capture files are not published with these docs.

The suite checks response envelopes, selected-field identity, country/founded-year
predicates visible in company cards, exact financial constraints, fiscal-period
bounds, exact team affiliation, app rating/install/category/domain predicates and
internship work-mode/stipend assertions. Other classifications remain source predicates;
we do not claim independent validation where returned cards lack supporting fields.
''')
    print(json.dumps({"baseline": counts('baseline'), "current": counts('current'), "scenarios": 50}))


if __name__ == '__main__':
    main()
