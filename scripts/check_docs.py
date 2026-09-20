#!/usr/bin/env python3
"""Check local documentation links and validate guide examples against API models."""
import json
import hashlib
import re
from pathlib import Path

from radar_api import accounts
from radar_api.models import Company, CompanyProfile, CompanyProfileEnvelope, Envelope
from radar_api.service import BY_NAME

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = {
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
    "hiring-signals-jobs-api": ["search_jobs", "salary_benchmark"],
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
        assert len(actual) <= len(original), f"Invented array rows at {path}"
        for i, value in enumerate(actual):
            unchanged_projection(value, original[i], f"{path}/{i}")
    else:
        assert actual == original, f"Changed captured value at {path}"


manifest = json.loads((ROOT / "docs/examples/index.json").read_text())
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
            assert BY_NAME[name].source != "radar"
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
        original = text.split("<!-- captured-workflow -->")[0]
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
assert responses == len(records) + 16, "Every endpoint and guide must show captured output"
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
CompanyProfileEnvelope.model_validate(json.loads((ROOT / "radar_api/static/company-profile-example.json").read_text()))
assert json.loads((ROOT / "radar_api/static/company-profile-example.json").read_text()) == json.loads(
    (ROOT / "docs/examples/profiles/razorpay.com.json").read_text())["response"]
assert account_schema["paths"]["/v1/companies/profile"]["post"]["responses"]["200"]["content"]["application/json"]["examples"]["detailed_company"]["value"]["data"]["profile_depth"] == "detailed"
print(f"Checked {links} local links, {examples} guide requests, {responses} displayed responses, "
      f"{len(records)} endpoint captures, {mcp_requests} MCP calls, {raw_checked} private-original projections, "
      "3 deep company examples, Swagger profile output and transport output")
