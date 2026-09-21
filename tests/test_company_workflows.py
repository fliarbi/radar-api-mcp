import json

import httpx
from fastapi.testclient import TestClient

from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.upstream import Upstream
from conftest import KEY


def grant(keyfile, scopes, token="linked-session"):
    data = json.loads(keyfile.read_text())
    data["keys"][0].update(scopes=scopes, radar_token=token)
    keyfile.write_text(json.dumps(data))


def test_filter_catalog_sorting_columns_and_numeric_filters(harness):
    client, calls, _ = harness
    catalog = client.post("/v1/companies/filters", json={}).json()["data"]
    assert not calls
    assert {"revenue_models", "founders_background", "web_score", "hiring", "founded_year_from"} <= {f["field"] for f in catalog["filters"]}
    assert "employees" in catalog["sort_options"] and "latest_revenue" in catalog["columns"]
    body = {"filters": {"revenue_models": ["subscription"], "founded_year_from": 2010,
        "founded_year_to": 2020, "locations": ["Delhi, India"], "radius_km": 50,
        "web_score": ["80+"], "mobile_downloads": ["1m+"], "hiring": {"roles": ["engineer"]}},
        "sort_by": "employees", "page": 2, "limit": 5}
    assert client.post("/v1/companies/search", json=body).status_code == 200
    sent = json.loads(calls[-1].content)["final_data"]
    assert sent["sort_by"] == ["no of employees"] and sent["founded_year"] == [2010, 2020]
    assert sent["custom_range"] == 50000 and sent["radius_explicit"] is True
    assert sent["hiring"]["roles"] == ["engineer"] and sent["revenue"] == ["subscription"]
    assert sent["current_page"] == 2 and sent["results_per_page"] == 5
    columns = client.post("/v1/companies/columns", json={"domains": ["example.com"], "columns": ["employees", "latest_revenue"]}).json()["data"]
    assert columns["companies"][0]["columns"]["employees"]["value"] == "51-200"
    assert columns["companies"][0]["columns"]["latest_revenue"] is None


def test_unsupported_filters_and_injection_do_not_reach_source(harness):
    client, calls, _ = harness
    for path, body in [
        ("filter-options", {"field": "private_sql", "q": "anything"}),
        ("columns", {"domains": ["example.com"], "columns": ["emails"]}),
        ("search", {"sort_by": "SELECT secret"}),
        ("search", {"filters": {"founded_year_from": 2020, "founded_year_to": 2010}}),
        ("search", {"filters": {"hiring": {"roles": {"$ne": None}}}}),
        ("search", {"filters": {"radius_km": 50}}),
    ]:
        assert client.post("/v1/companies/" + path, json=body).status_code == 422
    assert not calls


def test_people_extended_filters_use_source_names(harness):
    client, calls, _ = harness
    response = client.post("/v1/people/search", json={"companies": ["Microsoft"], "roles": ["board"],
        "schools": ["Stanford University"], "degrees": ["Computer Science"], "min_seniority": "director", "min_people_rank": 50})
    assert response.status_code == 200
    fd = json.loads(calls[-1].content)["final_data"]
    assert fd["degree"] == ["Computer Science"] and fd["current_company"] == ["Microsoft"]
    assert fd["people_types"] == ["board"] and fd["min_seniority"] == "director"


def test_contacts_require_explicit_scope_and_link_before_source(harness, keyfile):
    client, calls, _ = harness
    grant(keyfile, ["*"])
    response = client.post("/v1/contacts/company", json={"domain": "example.com", "fields": ["emails"]})
    assert response.status_code == 403 and response.json()["error"]["kind"] == "scope_required"
    assert not calls
    grant(keyfile, ["contacts"], "")
    assert client.post("/v1/contacts/person", json={"person_id": "example", "fields": ["phones"]}).status_code == 403
    assert not calls


def test_contact_field_selection_preserves_fallback_and_hides_other_values(harness):
    client, calls, _ = harness
    response = client.post("/v1/contacts/person", json={"person_id": "example", "fields": ["emails"]})
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["emails"] == ["sales@example.com"] and "phones" not in data
    assert data["contact_source"] == "company_domain"
    assert json.loads(calls[-1].content)["id"] == "example"
    assert calls[-1].headers["X-Auth-Token"] == "session-one"
    assert client.post("/v1/contacts/company", json={"domain": "example.com", "fields": ["phones"]}).json()["data"]["phones"] == ["+1-202-555-0123"]


def test_source_contact_gate_cannot_be_bypassed_even_with_values(keyfile):
    grant(keyfile, ["contacts"])
    settings = Settings(keys_file=str(keyfile), allowed_hosts=("testserver",))
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"gated": True, "emails": ["must-not-leak@example.com"]}))
    with TestClient(create_app(settings, Upstream(settings, transport))) as client:
        result = client.post("/v1/contacts/company", headers={"X-API-Key": KEY}, json={"domain": "example.com", "fields": ["emails"]})
        assert result.status_code == 403 and "must-not-leak" not in result.text


def test_contact_rate_limit_stops_before_eleventh_upstream_call(harness):
    client, calls, _ = harness
    for _ in range(10):
        assert client.post("/v1/contacts/company", json={"domain": "example.com", "fields": ["emails"]}).status_code == 200
    result = client.post("/v1/contacts/company", json={"domain": "example.com", "fields": ["emails"]})
    assert result.status_code == 429 and len(calls) == 10
    assert result.headers["retry-after"]


def test_brief_requires_details_to_obtain_bulk_records(harness):
    client, _, _ = harness
    response = client.post("/v1/companies/brief", json={"domain": "example.com"}).json()
    sections = response["data"]["sections"]
    financials = sections["financials"]["result"]["data"]
    assert "periods" not in financials and financials["latest_period"]["fiscal_year"] == 2026
    assert sections["financials"]["detail_request"]["path"] == "/v1/companies/financials"
    assert "events" not in sections["events"]["result"]["data"]
    assert "hiring" not in sections["enrichment"]["result"]["data"]
