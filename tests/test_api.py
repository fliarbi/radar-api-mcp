from __future__ import annotations

import json

import httpx
import pytest
from fastapi.testclient import TestClient

from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.service import FEATURES
from radar_api.upstream import Upstream

from conftest import KEY, KEY2, SAMPLES, payload_for


@pytest.mark.parametrize("feature", FEATURES, ids=lambda f: f.name)
def test_every_capability(harness, feature):
    client, calls, app = harness
    if feature.name in {"get_company_field", "get_company_team"}:
        from radar_api.profiles import ProfileStore
        from test_profiles import StoreClient, record
        app.state.service.profiles = ProfileStore(Settings(), StoreClient([record()]))
    response = client.post("/v1/" + feature.path, json=SAMPLES[feature.name])
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["ok"] and body["feature"] == feature.name
    assert {"data", "window", "meta"} <= body.keys()
    assert "must-not-leak" not in response.text
    assert "SELECT secret" not in response.text
    assert "session-one" not in response.text
    assert "entity_resolution" not in response.text
    assert response.headers["cache-control"] == "no-store"


def test_catalog_matches_openapi_and_registry(harness):
    client, _, _ = harness
    catalog = client.get("/v1/capabilities").json()["data"]["features"]
    schema = client.get("/v1/openapi.json").json()
    assert len(catalog) == len(FEATURES) == 53
    for feature in catalog:
        assert feature["path"] in schema["paths"]
        assert feature["input_schema"]["additionalProperties"] is False
        assert schema["paths"][feature["path"]]["post"]["security"]


@pytest.mark.parametrize("path", ["/v1/companies/profile", "/v1/capabilities", "/docs", "/v1/openapi.json", "/mcp"])
def test_no_unauthenticated_surface(harness, path):
    client, calls, _ = harness
    client.headers.pop("X-API-Key")
    response = client.get(path)
    assert response.status_code == 401
    assert response.headers["www-authenticate"] == "Bearer"
    assert not calls


def test_health_is_liveness_only(harness):
    client, calls, _ = harness
    client.headers.pop("X-API-Key")
    assert client.get("/healthz").json()["visibility"] == "public"
    assert not calls


def test_credentials_are_isolated(harness):
    client, calls, _ = harness
    for key, token, news in [(KEY, "session-one", "news-one"), (KEY2, "session-two", "news-two")]:
        response = client.post("/v1/companies/events", json={"domain": "example.com"}, headers={"X-API-Key": key})
        assert response.status_code == 200
        assert calls[-1].headers["X-Auth-Token"] == token
        assert json.loads(calls[-1].content)["auth_sign"] == token
        client.post("/v1/news/search", json={"company": "example.com"}, headers={"X-API-Key": key})
        assert calls[-1].headers["X-API-Key"] == news
        assert "X-Auth-Token" not in calls[-1].headers
        assert "authorization" not in calls[-1].headers
    response = client.get("/v1/capabilities", headers={"Authorization": "Bearer " + KEY2})
    assert response.status_code == 401  # Conflicting keys cannot change the linked principal.


@pytest.mark.parametrize("payload", [
    {"filters": {"_internal_skip_caps": True}}, {"filters": {"company_names": ["x' OR 1=1"]}},
    {"filters": {"industries": {"$ne": None}}}, {"limit": 101}, {"page": 999999},
    {"filters": {"revenue_bands": ["under1m", "1b+"]}}, {"auth_sign": "inject-token"},
])
def test_unsafe_requests_never_reach_radar(harness, payload):
    client, calls, _ = harness
    response = client.post("/v1/companies/search", json=payload)
    assert response.status_code == 422
    assert not calls
    assert "inject-token" not in response.text


@pytest.mark.parametrize("domain", ["http://example.com", "127.0.0.1", "localhost", "example.com/path", "a.com:80", "x.com'", "a..com"])
def test_domain_validation(harness, domain):
    client, calls, _ = harness
    assert client.post("/v1/companies/profile", json={"domain": domain}).status_code == 422
    assert not calls


def test_news_uses_company_scope_dates_and_cursor(harness):
    client, calls, _ = harness
    response = client.post("/v1/news/search", json={"company": "example.com", "date_from": "2026-01-01",
                           "date_to": "2026-08-01", "cursor": "next_page"})
    assert response.status_code == 200
    request = calls[-1]
    assert str(request.url).startswith("http://business.local/v1/business/headlines")
    assert request.url.params["since"] == "2026-01-01"
    assert request.url.params["until"] == "2026-08-01"
    assert request.url.params["limit"] == "100"
    assert request.url.params["cursor"] == "next_page"
    assert "date_from" not in request.url.params
    assert response.json()["window"]["data_through"] == "2026-08-01"


def test_invalid_date_window(harness):
    client, calls, _ = harness
    assert client.post("/v1/news/search", json={"q": "software", "date_from": "2026-08-01", "date_to": "2026-01-01"}).status_code == 422
    assert not calls


def test_job_company_name_is_not_rejected_as_a_domain(harness):
    client, calls, _ = harness
    response = client.post("/v1/jobs/search", json={"company": "Optimal Inc.", "limit": 3})
    assert response.status_code == 200
    assert json.loads(calls[-1].content)["filters"]["company"] == "Optimal Inc."
    calls.clear()
    assert client.post("/v1/jobs/search", json={"company": {"$ne": None}}).status_code == 422
    assert not calls


@pytest.mark.parametrize("level, value, expected", [
    ("city", "Delhi", {"location": "delhi", "location_type": "location"}),
    ("state", "Karnataka", {"location": "karnataka", "location_type": "state"}),
    ("country", "India", {"location": "india", "location_type": "country"}),
    # The source's cc mode fails on its own lookup, so codes are sent as country names.
    ("cc", "IN", {"location": "india", "location_type": "country"}),
    ("cc", "gb", {"location": "united kingdom", "location_type": "country"}),
])
def test_location_level_uses_upstream_geographic_predicate(harness, level, value, expected):
    client, calls, _ = harness
    response = client.post("/v1/locations/intelligence", json={"location": value, "location_type": level})
    assert response.status_code == 200
    # Stored names are lowercase and matched exactly; "India" used to return empty aggregates.
    assert json.loads(calls[-1].content)["final_data"] == expected


def test_unknown_country_code_is_rejected_before_the_source(harness):
    client, calls, _ = harness
    before = len(calls)
    response = client.post("/v1/locations/intelligence", json={"location": "zz", "location_type": "cc"})
    assert response.status_code == 422 and len(calls) == before


def test_financial_provenance_and_zero_values(harness):
    client, _, _ = harness
    body = client.post("/v1/companies/financials", json={"domain": "example.com", "period_type": "annual"}).json()
    data = body["data"]
    assert data["access_limited"] and data["available_period_count"] == 12
    period = data["periods"][0]
    assert period["period_end"] == "2025-12-31"
    assert period["metrics"]["net_income"]["value"] == 0
    assert period["metrics"]["revenue"]["currency"] == "USD"
    assert period["metrics"]["revenue"]["native_currency"] == "INR"
    assert period["metrics"]["revenue"]["native_value"] == 10000
    assert period["metrics"]["revenue"]["source_type"] == "filing"
    assert period["metrics"]["eps"]["source_type"] == "news_report"
    assert period["metrics"]["eps"]["currency"] is None


def test_statement_and_year_filters(harness):
    client, _, _ = harness
    data = client.post("/v1/companies/financials", json={"domain": "example.com", "statement": "balance_sheet", "year_to": 2025}).json()["data"]
    assert set(data["periods"][0]["metrics"]) == {"total_assets"}
    data = client.post("/v1/companies/financials", json={"domain": "example.com", "year_from": 2026}).json()["data"]
    assert data["periods"][0]["metrics"]["net_income"]["value"] == -2
    assert data["periods"][0]["period_end"] is None


def test_window_reports_effective_limits(harness):
    client, _, _ = harness
    body = client.post("/v1/companies/events", json={"domain": "example.com", "days": 365}).json()
    assert body["window"]["requested_days"] == 365
    assert body["window"]["effective_days"] == 30
    assert body["data"]["truncated"] is True


def test_origin_host_and_body_limits(harness):
    client, calls, _ = harness
    assert client.get("/v1/capabilities", headers={"Origin": "https://evil.example"}).status_code == 403
    assert client.get("/v1/capabilities", headers={"Host": "evil.example"}).status_code == 400
    assert client.post("/v1/companies/profile", content=b"x" * 262145).status_code == 413
    assert not calls


@pytest.mark.parametrize("mode,status,kind", [
    ("http_error", 429, "rate_limited"), ("legacy_error", 429, "rate_limited"),
    ("malformed", 502, "invalid_upstream_response"), ("timeout", 504, "upstream_timeout"),
    ("redirect", 502, "upstream_unavailable"), ("oversize", 502, "response_too_large"),
])
def test_upstream_failures(keyfile, mode, status, kind):
    def respond(request):
        if mode == "http_error":
            return httpx.Response(429, headers={"Retry-After": "23"}, text="private diagnostics")
        if mode == "legacy_error":
            return httpx.Response(200, json={"error": True, "errorCode": 429, "msg": "private diagnostics"})
        if mode == "malformed":
            return httpx.Response(200, text="<html>private diagnostics</html>")
        if mode == "timeout":
            raise httpx.ReadTimeout("private diagnostics")
        if mode == "redirect":
            return httpx.Response(302, headers={"Location": "https://untrusted.example"})
        return httpx.Response(200, content=b"x" * 2048)
    settings = Settings(keys_file=str(keyfile), max_response_bytes=1024, allowed_hosts=("testserver",))
    with TestClient(create_app(settings, Upstream(settings, httpx.MockTransport(respond)))) as client:
        response = client.post("/v1/companies/profile", headers={"X-API-Key": KEY}, json={"domain": "example.com"})
        assert response.status_code == status
        assert response.json()["error"]["kind"] == kind
        assert "private diagnostics" not in response.text
        if mode == "http_error":
            assert response.headers["Retry-After"] == "23"


def test_partial_brief_preserves_error(keyfile):
    def respond(request):
        if request.url.path == "/company_intel/":
            return httpx.Response(503, text="private diagnostics")
        return httpx.Response(200, json=payload_for(request.url.path))
    settings = Settings(keys_file=str(keyfile), allowed_hosts=("testserver",))
    with TestClient(create_app(settings, Upstream(settings, httpx.MockTransport(respond)))) as client:
        body = client.post("/v1/companies/brief", headers={"X-API-Key": KEY}, json={"domain": "example.com"}).json()
        assert body["ok"] and body["meta"]["partial"]
        assert body["data"]["sections"]["financials"]["error"]["kind"] == "upstream_unavailable"
        assert body["data"]["sections"]["news"]["error"]["kind"] == "service_unavailable"


def test_partial_search_is_visible(keyfile):
    settings = Settings(keys_file=str(keyfile), allowed_hosts=("testserver",))
    transport = httpx.MockTransport(lambda r: httpx.Response(200, json={"people": [], "_partial_timeout": True, "_total_capped": True}))
    with TestClient(create_app(settings, Upstream(settings, transport))) as client:
        body = client.post("/v1/people/search", headers={"X-API-Key": KEY}, json={}).json()
        assert body["meta"]["partial"]
        assert body["data"]["total_capped"]


def test_news_evidence_and_coverage_survive_briefs(keyfile):
    article = "Example: SELECT * FROM news. Connect locally to 127.0.0.1."

    def respond(request):
        if request.url.path.startswith("/v1/"):
            return httpx.Response(200, json={"ok": True, "data": {"text": article, "items": [{"headline": article}]}, "meta": {
                "coverage": {"available": False}, "plan": "free", "quota": {"remaining": 12}}})
        return httpx.Response(200, json=payload_for(request.url.path))

    settings = Settings(keys_file=str(keyfile), news_url="http://news.local", business_news_url="http://news.local", allowed_hosts=("testserver",))
    with TestClient(create_app(settings, Upstream(settings, httpx.MockTransport(respond)))) as client:
        body = client.post("/v1/companies/brief", headers={"X-API-Key": KEY}, json={"domain": "example.com"}).json()
        result = body["data"]["sections"]["news"]["result"]
        assert "text" not in result["data"]
        assert result["data"]["items"][0]["headline"] == article
        assert result["meta"]["quota"] == {"remaining": 12}
        assert result["meta"]["partial"] and body["meta"]["partial"]


def test_immediate_revocation_expiry_permissions_and_rate_limit(harness, keyfile):
    client, _, _ = harness
    records = json.loads(keyfile.read_text())
    records["keys"][0]["rate_per_minute"] = 1
    keyfile.write_text(json.dumps(records))
    assert client.get("/v1/capabilities").status_code == 200
    assert client.get("/v1/capabilities").status_code == 429
    records["keys"][0]["active"] = False
    keyfile.write_text(json.dumps(records))
    assert client.get("/v1/capabilities").status_code == 401
    records["keys"][0].update(active=True, expires_at="2020-01-01T00:00:00Z")
    keyfile.write_text(json.dumps(records))
    assert client.get("/v1/capabilities").status_code == 401
    keyfile.chmod(0o644)
    assert client.get("/v1/capabilities").status_code == 503
