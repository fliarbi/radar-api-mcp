#!/usr/bin/env python3
"""Check local documentation links and validate guide examples against API models."""
import json
from scenario_cases import CASES
from company_depth_examples import EXAMPLES as COMPANY_DEPTH_EXAMPLES
from stress_scenarios import assess as assess_scenario
from radar_api.models import CompanyFilters
import hashlib
import re
from pathlib import Path

from radar_api import accounts
from radar_api.models import Company, CompanyProfile, CompanyProfileEnvelope, CompanyField, PROFILE_SECTIONS, Envelope
from radar_api.service import BY_NAME
from audit_examples import report as example_audit
from audit_data_depth import audit as depth_audit
from guide_expansions import GUIDES
from contact_workflow_notes import VARIANTS, CONTACT_EVIDENCE, GUIDE_EVIDENCE

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = {
    "founder-contact-data-api": ["get_company_team", "search_people", "get_person_contacts", "get_company_team"],
    "company-email-phone-api": ["get_company", "get_company_contacts", "get_company_team"],
    "linkedin-social-data-api": ["get_company_field", "search_people"],
    "financial-filters-data-api": ["screen_company_financials"] * 2 + ["get_financials"] * 2,
    "teams-people-data-api": ["get_company_team"] * 4 + ["search_people"],
    "technology-traffic-data-api": ["get_company_field"] * 4,
    "b2b-data-api": ["search_companies", "company_brief"],
    "company-search-api": ["search_companies", "semantic_company_search"],
    "company-enrichment-api": ["get_company_enrichment"],
    "financial-data-api": ["get_financials"],
    "company-financial-statements-api": ["get_financials"] * 3,
    "financial-news-api": ["search_business_news"],
    "funding-news-api": ["search_funding_news"],
    "startup-funding-data-api": ["get_company_funding", "market_pulse"],
    "investor-data-api": ["search_investors", "investor_directory"],
    "company-monitoring-api": [None, "get_company_events"],
    "competitor-intelligence-api": ["find_competitors", "compare_companies"],
    "hiring-signals-jobs-api": ["search_jobs", "salary_benchmark", "job_filter_options", "search_jobs"],
    "apps-data-api": ["search_apps", "company_apps", "get_app", "get_app_field"],
    "internships-companies-api": ["search_internships", "companies_offering_internships", "get_internship"],
    "potential-company-data-api": ["search_opportunities"],
    "company-intelligence-mcp-server": ["get_financials"],
}
def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def unchanged_projection(actual, original, path=""):
    assert type(actual) is type(original), f"Changed type at {path}"
    if isinstance(actual, dict):
        for key, value in actual.items():
            assert key in original, f"Invented field at {path}/{key}"
            unchanged_projection(value, original[key], path + "/" + key)
    elif isinstance(actual, list):
        assert len(actual) == len(original), f"Dropped or invented array rows at {path}"
        for i, value in enumerate(actual):
            unchanged_projection(value, original[i], f"{path}/{i}")
    else:
        assert actual == original, f"Changed captured value at {path}"


manifest = json.loads((ROOT / "docs/examples/index.json").read_text())
output_audit = json.loads((ROOT / 'docs/research/endpoint-output-audit.json').read_text())
assert {r['operation'] for r in output_audit['operations']} == set(BY_NAME), 'Output audit misses an operation'
assert output_audit['data_operations'] == len(BY_NAME)
for row in output_audit['operations']:
    feature = BY_NAME[row['operation']]
    feature.model.model_validate(row['live_probe']['request'])
    assert row['path'] == '/v1/' + feature.path
for row in output_audit['source_files']:
    assert hashlib.sha256((ROOT / row['path']).read_bytes()).hexdigest() == row['sha256'], 'Output source review needs refresh: ' + row['path']
conservation = json.loads((ROOT / 'docs/research/selected-field-conservation.json').read_text())
assert len(conservation['captures']) == conservation['checked_captures'] == 61
assert sum(not r['existing_value_differences'] for r in conservation['captures']) == conservation['unchanged_existing_values']
for row in conservation['captures']:
    capture = json.loads((ROOT / row['file']).read_text())
    assert digest(capture['response']) == row['current_response_sha256'], 'Refresh field conservation: ' + row['file']
    assert row['request'] == capture['request']
    if row['existing_value_differences']:
        assert row['difference_classification'] == 'Confirmed current native source projection, not adapter field loss'
records = {r["operation"]: json.loads((ROOT / "docs/examples" / (r["operation"] + ".json")).read_text()) for r in manifest}
assert len(records) == len(manifest), "Duplicate example operation"
assert set(BY_NAME) <= records.keys(), "Missing data endpoint capture"
account_schema = json.loads((ROOT / "docs/account-openapi.json").read_text())
captured_routes = set()
for name, record in records.items():
    assert record["response_excerpt_sha256"] == digest(record["response"]), f"Changed response: {name}"
    path = record["path"]
    if name == "account_revoke_key":
        path = "/account/keys/{key_id}"
    if name == "account_unfollow":
        path = "/account/following/{domain}"
    method = record["method"].lower()
    captured_routes.add((path, method))
    if name in BY_NAME:
        BY_NAME[name].model.model_validate(record["request"])
        assert path == "/v1/" + BY_NAME[name].path and method == "post"
        assert record["capture_kind"] in {"live_gateway", "live_data_integration"}
        if record["capture_kind"] == "live_data_integration":
            assert BY_NAME[name].source != "radar" or name == "company_brief"
            assert "test identity" in record["provenance"] and "live data" in record["provenance"]
    else:
        schema = account_schema["paths"].get(path, {}).get(method, {}).get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema", {})
        if "$ref" in schema:
            model_name = schema["$ref"].split("/")[-1]
            getattr(accounts, model_name).model_validate(record["request"])
    if name not in {"health", "openapi"}:
        Envelope.model_validate(record["response"])
        assert record["response"]["ok"] == (record["http_status"] < 400)
    assert (ROOT / "docs/reference" / (name + ".md")).exists()

expected_routes = {(path, method) for path, methods in account_schema["paths"].items()
                   for method in methods if method in {"get", "post", "put", "delete", "patch"}}
assert captured_routes == expected_routes | {("/v1/openapi.json", "get")}, "HTTP operation coverage differs from schema"

# CI validates checked-in records; local runs additionally compare private originals.
raw_checked = 0
for filename in ("endpoint-live.json", "endpoint-accounts.json"):
    path = ROOT / "qa/private" / filename
    if path.exists():
        raw = json.loads(path.read_text())
        for name, value in raw["operations"].items():
            record = records[name]
            assert record["original_response_sha256"] == digest(value["response"]), name
            assert record["request"] == value.get("request"), name
            assert record["http_status"] == value["http_status"], name
            assert record["provenance"] == value["provenance"], name
            if value.get("capture_kind"):
                assert record["capture_kind"] == value["capture_kind"], name
            unchanged_projection(record["response"], value["response"], name)
            raw_checked += 1

workflow_examples = {
    "COMPANY_DATA_DEPTH.md": [CompanyProfile, CompanyField],
    "FILTERS_AND_LISTINGS.md": [BY_NAME[name].model for name in ("company_filter_options", "search_companies", "get_company_columns")],
}
for file, models in workflow_examples.items():
    workflow_text = (ROOT / "docs" / file).read_text().split("<!-- company-depth-examples -->")[0]
    blocks = re.findall(r"```json\n(.*?)\n```", workflow_text, re.S)
    assert len(blocks) == len(models), "Unmapped workflow example: " + file
    for block, model in zip(blocks, models):
        value = json.loads(block)
        if model:
            model.model_validate(value)

links = examples = responses = mcp_requests = 0
for path in [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]:
    text = path.read_text()
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        target = target.split("#", 1)[0]
        if target:
            assert (path.parent / target).exists(), f"Broken link in {path.name}: {target}"
            links += 1
    for name, block in re.findall(r"<!-- response-example: (\w+) -->\n```json\n(.*?)\n```", text, re.S):
        assert json.loads(block) == records[name]["response"], f"Stale displayed response: {path} {name}"
        responses += 1
    for name, block in re.findall(r"<!-- captured-request: (\w+) -->\n```json\n(.*?)\n```", text, re.S):
        assert json.loads(block) == records[name]["request"], f"Stale captured request: {path} {name}"
        examples += 1
    for name, block in re.findall(r"<!-- mcp-request: (\w+) -->\n```json\n(.*?)\n```", text, re.S):
        call = json.loads(block)
        assert call["name"] == name
        BY_NAME[name].model.model_validate(call["arguments"]["request"])
        assert call["arguments"]["request"] == records[name]["request"]
        mcp_requests += 1
    if path.parent.name == "guides":
        original = text.split("<!-- captured-workflow -->")[0].split("<!-- contact-evidence -->")[0]
        blocks = re.findall(r"```json\n(.*?)\n```", original, re.S)
        operations = EXAMPLES.get(path.stem, [])
        assert len(blocks) == len(operations), f"Unmapped example in {path.name}"
        for block, operation in zip(blocks, operations):
            data = json.loads(block)
            data = data.get("request", data)
            (BY_NAME[operation].model if operation else Company).model_validate(data)
            examples += 1
        # Validate the JSON body of shell examples too.
        for body in re.findall(r"-d '(\{[^\n]+\})'", text):
            Company.model_validate_json(body)
            examples += 1
assert mcp_requests == len(BY_NAME), "Every data reference must show its MCP request"
assert responses == len(records) + len(GUIDES), "Every endpoint and guide must show captured output"
transport = json.loads((ROOT / "docs/examples/transports.json").read_text())
assert {t["name"] for t in transport["tools"]} == set(BY_NAME)
Envelope.model_validate(transport["result"]["structuredContent"])
assert all(row["status"] == 200 for row in transport["browser_routes"])
for domain in ("razorpay.com", "stripe.com", "swiggy.com"):
    item = json.loads((ROOT / "docs/examples/profiles" / (domain + ".json")).read_text())
    CompanyProfile.model_validate(item["request"])
    CompanyProfileEnvelope.model_validate(item["response"])
    assert digest(item["response"]) == item["response_excerpt_sha256"]
    assert not any(path.endswith(":" ) for path in item["omitted_paths"]), "Profile documentation must not truncate arrays"
    original = ROOT / "qa/private" / ("profile-" + domain + ".json")
    if original.exists():
        raw = json.loads(original.read_text())
        assert digest(raw) == item["original_response_sha256"]
        unchanged_projection(item["response"], raw)
for domain in ("razorpay.com", "stripe.com", "swiggy.com"):
    for field in PROFILE_SECTIONS:
        item = json.loads((ROOT / "docs/examples/fields" / (domain + "-" + field + ".json")).read_text())
        CompanyField.model_validate(item["request"])
        Envelope.model_validate(item["response"])
        assert item["response"]["data"]["field"] == field
        assert "company" not in item["response"]["data"]
        assert digest(item["response"]) == item["response_excerpt_sha256"]
        original = ROOT / "qa/private" / ("field-" + domain + "-" + field + ".json")
        if original.exists():
            raw = json.loads(original.read_text())
            assert raw["request"] == item["request"]
            assert digest(raw["response"]) == item["original_response_sha256"]
            unchanged_projection(item["response"], raw["response"])
CompanyProfileEnvelope.model_validate(json.loads((ROOT / "radar_api/static/company-profile-example.json").read_text()))
assert json.loads((ROOT / "radar_api/static/company-profile-example.json").read_text()) == json.loads(
    (ROOT / "docs/examples/profiles/razorpay.com.json").read_text())["response"]
assert account_schema["paths"]["/v1/companies/profile"]["post"]["responses"]["200"]["content"]["application/json"]["examples"]["compact_company"]["value"]["data"]["profile_depth"] == "summary"
print(f"Checked {links} local links, {examples} guide requests, {responses} displayed responses, "
      f"{len(records)} endpoint captures, {mcp_requests} MCP calls, {raw_checked} private-original projections, "
      "3 compact company examples and 54 separate field captures, Swagger profile output and transport output")
assert json.loads((ROOT / "docs/EXAMPLE_AUDIT.json").read_text()) == example_audit(), "Stale example audit"
print("Verified the complete endpoint example audit against current response fingerprints")

assert json.loads((ROOT / "docs/DATA_DEPTH_AUDIT.json").read_text()) == depth_audit(), "Stale depth audit"

# Investor supplemental captures prove actual detail and preserve original structure.
investor_manifest = json.loads((ROOT / "docs/examples/investors/index.json").read_text())
assert len(investor_manifest) == 21
for row in investor_manifest:
    capture = json.loads((ROOT / "docs/examples/investors" / row["file"]).read_text())
    BY_NAME[capture["operation"]].model.model_validate(capture["request"])
    assert capture["http_status"] == 200
    assert digest(capture["response"]) == capture["response_excerpt_sha256"] == row["response_sha256"]
    original = ROOT / "qa/private" / ("investor-" + row["file"])
    if original.exists():
        original = json.loads(original.read_text())
        assert digest(original["response"]) == capture["original_response_sha256"]
        unchanged_projection(capture["response"], original["response"])
print("Verified 21 investor captures and all retained array lengths")


# Every separately selected app field is a real capture with original array lengths.
app_manifest = json.loads((ROOT / "docs/examples/apps/index.json").read_text())
assert {row["field"] for row in app_manifest} == {"listing", "ratings", "monetization", "release", "developer", "growth", "install_history"}
app_records = {}
for row in app_manifest:
    capture = json.loads((ROOT / "docs/examples/apps" / row["file"]).read_text())
    BY_NAME["get_app_field"].model.model_validate(capture["request"])
    assert capture["http_status"] == 200
    Envelope.model_validate(capture["response"])
    assert digest(capture["response"]) == capture["response_excerpt_sha256"] == row["response_sha256"]
    original = ROOT / "qa/private" / ("app-" + row["file"])
    if original.exists():
        raw = json.loads(original.read_text())
        assert digest(raw["response"]) == capture["original_response_sha256"]
        unchanged_projection(capture["response"], raw["response"])
    app_records[row["field"]] = capture
for field, block in re.findall(r"<!-- app-field-response: (\w+) -->\n```json\n(.*?)\n```", (ROOT / "docs/APP_DATA_DEPTH.md").read_text(), re.S):
    assert json.loads(block) == app_records[field]["response"]
print("Verified all seven app field captures and displayed outputs")


opportunity_manifest = json.loads((ROOT / "docs/examples/opportunities/index.json").read_text())
assert {row["preset"] for row in opportunity_manifest} == {"profitable_growth", "hiring_expansion"}
opportunity_records = {}
for row in opportunity_manifest:
    capture = json.loads((ROOT / "docs/examples/opportunities" / row["file"]).read_text())
    BY_NAME["search_opportunities"].model.model_validate(capture["request"])
    assert capture["http_status"] == 200
    Envelope.model_validate(capture["response"])
    assert digest(capture["response"]) == capture["response_excerpt_sha256"] == row["response_sha256"]
    original = ROOT / "qa/private" / ("opportunity-" + row["file"])
    if original.exists():
        raw = json.loads(original.read_text())
        assert digest(raw["response"]) == capture["original_response_sha256"]
        unchanged_projection(capture["response"], raw["response"])
    opportunity_records[row["preset"]] = capture
blocks = re.findall(r"<!-- opportunity-response: (\w+) -->\n```json\n(.*?)\n```", (ROOT / "docs/POTENTIAL_DATA_EXAMPLES.md").read_text(), re.S)
assert len(blocks) == 2
for preset, block in blocks:
    assert json.loads(block) == opportunity_records[preset]["response"]
print("Verified both additional growth/investment and sales-prospect captures")

# Every fixed business question has a valid request, a full response projection,
# displayed output, and a two-way link to its workflow guide.
scenario_index = json.loads((ROOT / "docs/examples/scenarios/index.json").read_text())
assert len(scenario_index) == len(CASES) == 50
assert {r["id"] for r in scenario_index} == {c["id"] for c in CASES}
for case in CASES:
    record = json.loads((ROOT / "docs/examples/scenarios" / (case["id"] + ".json")).read_text())
    assert record["request"] == case["request"] and record["operation"] == case["operation"]
    BY_NAME[case["operation"]].model.model_validate(record["request"])
    assert record["path"] == "/v1/" + BY_NAME[case["operation"]].path
    for stage, source in (("baseline", "baseline"), ("current", "repair2")):
        captured = record[stage]
        assert digest(captured["response"]) == captured["response_excerpt_sha256"]
        assert assess_scenario(case, captured["http_status"], captured["response"]) == captured["assessment"]
        original = ROOT / "qa/private" / ("scenarios-" + source + ".json")
        if original.exists():
            raw = next(r for r in json.loads(original.read_text())["results"] if r["id"] == case["id"])
            assert raw["request"] == record["request"]
            assert digest(raw["response"]) == captured["original_response_sha256"]
            unchanged_projection(captured["response"], raw["response"])
    page = (ROOT / "docs/scenarios" / (case["id"] + ".md")).read_text()
    request_block = re.search(r"<!-- scenario-request: .*? -->\n```json\n(.*?)\n```", page, re.S)
    response_block = re.search(r"<!-- scenario-response: .*? -->\n```json\n(.*?)\n```", page, re.S)
    assert json.loads(request_block[1]) == record["request"]
    assert json.loads(response_block[1]) == record["current"]["response"]
    guide = (ROOT / "docs/guides" / (case["guide"] + ".md")).read_text()
    assert case["id"] + ".md" in guide and case["guide"] + ".md" in page
filter_audit = json.loads((ROOT / "docs/FILTER_AUDIT.json").read_text())
assert {r["field"] for r in filter_audit["fields"]} == set(CompanyFilters.model_fields)
print("Validated 50 scenario requests, baseline/current outputs, displayed examples and guide links; 43 filter fields inventoried")

# New depth walkthroughs must display each saved response verbatim, not a thinner
# hand-written approximation, and their requests must still match the API schema.
depth_text = (ROOT / "docs/COMPANY_DATA_DEPTH.md").read_text()
expected_depth_sources = {row[2] for row in COMPANY_DEPTH_EXAMPLES}
for kind in ("request", "response"):
    blocks = re.findall(r"<!-- company-depth-" + kind + r": ([^ ]+) -->\n```json\n(.*?)\n```", depth_text, re.S)
    assert len(blocks) == len(expected_depth_sources)
    assert {source for source, _ in blocks} == expected_depth_sources
    for source, block in blocks:
        record = json.loads((ROOT / "docs/examples" / source).read_text())
        capture = record.get("current", record)
        expected = record["request"] if kind == "request" else capture["response"]
        assert json.loads(block) == expected, "Stale or shortened company-depth " + kind + ": " + source
        assert digest(capture["response"]) == capture["response_excerpt_sha256"]
        assert record["path"] == "/v1/" + BY_NAME[record["operation"]].path
        BY_NAME[record["operation"]].model.model_validate(record["request"])
        Envelope.model_validate(capture["response"])
print(f"Verified {len(expected_depth_sources)} inline company-depth requests and complete saved responses")

# Contact documentation has distinct live-discovery and synthetic-contact evidence.
# Never substitute fictional success payloads for a real person's contact result.
contact_pages = {"CONTACTS.md": CONTACT_EVIDENCE,
                 **{"guides/" + name + ".md": entries for name, entries in GUIDE_EVIDENCE.items()}}
contact_requests = contact_responses = 0
for relative, entries in contact_pages.items():
    text = (ROOT / "docs" / relative).read_text()
    base = text.split("<!-- contact-evidence -->")[0]
    authored = re.findall(r"<!-- contact-request: (\w+) -->\n```json\n(.*?)\n```", base, re.S)
    assert len(authored) == len(re.findall(r"```json\n", base)), "Unmapped contact recipe: " + relative
    for operation, block in authored:
        model = accounts.NewKey if operation == "account_create_key" else BY_NAME[operation].model
        model.model_validate_json(block)
        contact_requests += 1
    sources = [source for _, source in entries]
    for kind in ("request", "response"):
        blocks = re.findall(r"<!-- contact-captured-" + kind + r": ([^ ]+) -->\n```json\n(.*?)\n```", text, re.S)
        assert [source for source, _ in blocks] == sources, "Missing or reordered contact evidence: " + relative
        for source, block in blocks:
            capture = json.loads((ROOT / "docs/examples" / source).read_text())
            assert json.loads(block) == capture[kind], "Stale or shortened contact evidence: " + source
            BY_NAME[capture["operation"]].model.model_validate(capture["request"])
            assert capture["path"] == "/v1/" + BY_NAME[capture["operation"]].path
            Envelope.model_validate(capture["response"])
            assert digest(capture["response"]) == capture["response_excerpt_sha256"]
            if kind == "response":
                contact_responses += 1

recipes = json.loads((ROOT / "docs/examples/contacts/requests.json").read_text())
assert len(recipes) == len(VARIANTS) == 24
for recipe, variant in zip(recipes, VARIANTS):
    feature = BY_NAME[variant["operation"]]
    assert recipe == {**variant, "method": "POST", "path": "/v1/" + feature.path}
    feature.model.model_validate(recipe["request"])
recipe_text = (ROOT / "docs/CONTACT_REQUEST_RECIPES.md").read_text()
recipe_blocks = re.findall(r"<!-- contact-recipe: ([^ ]+) -->\n```json\n(.*?)\n```", recipe_text, re.S)
assert [key for key, _ in recipe_blocks] == [v["id"] for v in VARIANTS]
for (_, block), variant in zip(recipe_blocks, VARIANTS):
    assert json.loads(block) == variant["request"], "Stale displayed contact recipe: " + variant["id"]

contact_dir = ROOT / "docs/examples/contacts"
contact_manifest = json.loads((contact_dir / "index.json").read_text())
assert len(contact_manifest) == 11
assert {row["file"] for row in contact_manifest} == {
    p.name for p in contact_dir.glob("*.json") if p.name not in {"index.json", "requests.json"}}
contact_captures = {}
for row in contact_manifest:
    capture = json.loads((contact_dir / row["file"]).read_text())
    contact_captures[row["file"]] = capture
    assert row == {**{k: capture[k] for k in row if k != "file"}, "file": row["file"]}
    assert capture["method"] == "POST"
    assert capture["path"] == "/v1/" + BY_NAME[capture["operation"]].path
    BY_NAME[capture["operation"]].model.model_validate(capture["request"])
    Envelope.model_validate(capture["response"])
    assert capture["response"]["ok"] == (capture["http_status"] < 400)
    assert digest(capture["response"]) == capture["response_excerpt_sha256"]
    assert not any(p.endswith(":") for p in capture["omitted_paths"]), "Contact evidence must retain array rows"
    if capture["capture_kind"] == "live_gateway":
        assert capture["operation"] in {"search_people", "get_company_team"}
    else:
        assert capture["capture_kind"] == "local_contact_fixture"
        assert capture["operation"] in {"get_company_contacts", "get_person_contacts"}
        assert capture["request"].get("domain", "example.com") == "example.com"
        assert capture["request"].get("person_id", "example-founder") == "example-founder"
        assert "synthetic" in capture["provenance"] and "fictional" in capture["provenance"]
    original = ROOT / "qa/private" / ("contact-workflow-" + row["file"])
    if original.exists():
        raw = json.loads(original.read_text())
        for key in ("request", "operation", "capture_kind", "http_status", "provenance"):
            assert raw[key] == capture[key]
        assert digest(raw["response"]) == capture["original_response_sha256"]
        unchanged_projection(capture["response"], raw["response"])
assert sum(c["capture_kind"] == "local_contact_fixture" for c in contact_captures.values()) == 8

research = json.loads((ROOT / "docs/research/contact-workflow-evidence.json").read_text())
assert len(research["evidence"]) == len(contact_manifest)
assert {r["file"] for r in research["evidence"]} == {"../examples/contacts/" + r["file"] for r in contact_manifest}
for row in research["evidence"]:
    capture = contact_captures[Path(row["file"]).name]
    for key in ("operation", "capture_kind", "http_status", "response_excerpt_sha256"):
        assert row[key] == capture[key], "Stale research evidence: " + row["file"]
for label, filename in (("named_shashank_results", "founder-shashank.json"),
                        ("named_harshil_results", "founder-professional.json"),
                        ("professional_founder_role_results", "founder-team.json")):
    assert research["discovery_findings"][label] == [r["name"] for r in contact_captures[filename]["response"]["data"]["people"]]
assert not research["live_paid_contact_retrieval_verified"]
assert not research["production_account_mutations"] and not research["messages_sent"]
print(f"Verified {contact_requests} authored contact requests, {contact_responses} complete displayed outputs, "
      "24 typed recipes, 3 live discovery captures, 8 synthetic fixtures and the research evidence manifest")

social_evidence = json.loads((ROOT / 'docs/research/linkedin-social-evidence.json').read_text())
assert {row['domain'] for row in social_evidence['evidence']} == {'razorpay.com', 'stripe.com', 'swiggy.com'}
for row in social_evidence['evidence']:
    capture = json.loads((ROOT / 'docs/research' / row['file']).read_text())
    assert row['response_excerpt_sha256'] == digest(capture['response'])
    assert row['http_status'] == capture['http_status'] == 200
    assert row['captured_at'] == capture['captured_at']
    linkedin = capture['response']['data']['value']['linkedin']
    assert row['profile_snapshots'] == len(linkedin['profile_history'])
    assert row['distinct_posts'] == len(linkedin['recent_posts'])
    assert row['latest_profile'] == linkedin['profile']
    assert len({post['post_id'] for post in linkedin['recent_posts']}) == row['distinct_posts']
    for name in ('profile_history', 'recent_posts'):
        assert linkedin['coverage'][name]['status'] == 'available'
        coverage = capture['response']['data']['coverage']['arrays']['/value/linkedin/' + name]
        assert coverage['available'] == coverage['returned'] == len(linkedin[name]) and not coverage['truncated']
print('Verified all 3 LinkedIn profile captures and 21 distinct stored posts with source dates and coverage')
