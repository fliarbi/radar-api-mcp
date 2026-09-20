from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone

import pytest
from pydantic import ValidationError
from pymongo.errors import ServerSelectionTimeoutError

from radar_api.auth import CURRENT, Principal
from radar_api.config import Settings
from radar_api.errors import RadarError
from radar_api.models import CompanyProfile, CompanyProfileData
from radar_api.profiles import PROJECTION, ProfileStore, profile_payload
from radar_api.public import company_card


def record():
    return {"_id": "internal-source-id", "identity": {"name": "Example", "domain": "example.com"},
            "descriptive": {"short_description": "A payments business", "founded_year": 2014},
            "classification": {"practice_areas": [{"id": "provider-id", "name": "FinTech"}],
                               "feeds_primary": [{"name": "Payments"}],
                               "feeds_other": [{"name": f"Category {i}"} for i in range(18)]},
            "people": {"key_people_count": 3, "key_people": [
                {"name": "Founder One", "designation": "Co-Founder & CEO", "email": "private@example.com", "id": "internal"},
                {"name": "Founder Two", "designation": "Founder", "phone": "private"},
                {"name": "Executive Three", "designation": "CTO"}]},
            "enrichment": {"website_stacks": [f"Technology {i}" for i in range(70)], "finalized_products": ["Payments"]},
            "traction": {"mobile_app": {"count": 5, "downloads": 100, "weighted_rating": 0}},
            "web_presence": {"crawl_date": "2026-05-01", "source": "internal-provider", "tech_count": 70},
            "financials": {"employees": 120, "latest_estimated_revenue_usd": 900000000},
            "extras": {"updated_at": datetime(2026, 9, 20, tzinfo=timezone.utc)},
            "contact": {"email": "private@example.com"}, "scores": {"innovation": 0, "finance_source": "private"}}


def test_deep_profile_preserves_depth_and_keeps_private_or_gated_fields_out():
    data = profile_payload(record(), {"digital": {"visits": 0, "visits_date": "2026-05-01"}},
                           CompanyProfile(domain="example.com"), "public-example")
    company = data["company"]
    CompanyProfileData.model_validate(data)
    assert len(company["technology"]["website_stack"]) == 70
    assert len(company["classification"]["feeds"]["other"]) == 18
    assert len(company["people"]["founders"]) == 2
    assert len(company["people"]["key_people"]) == 3
    assert company["traffic"]["visits"] == company["apps"]["weighted_rating"] == 0
    assert company["assessments"]["innovation"] == 0
    assert data["updated_at"] == "2026-09-20T00:00:00+00:00"
    assert not data["coverage"]["partial"]
    rendered = str(data)
    for secret in ["private@example.com", "internal-source-id", "provider-id", "latest_estimated_revenue", "900000000", "internal-provider"]:
        assert secret not in rendered
    assert "contact" not in PROJECTION and "financials" not in PROJECTION


def test_requested_sections_and_array_limits_are_explicit():
    result = profile_payload(record(), {}, CompanyProfile(domain="example.com", sections=["technology"], item_limit=7), "public")
    assert len(result["company"]["technology"]["website_stack"]) == 7
    assert "people" not in result["company"]
    assert result["coverage"]["arrays"]["/company/technology/website_stack"] == {
        "available": 70, "returned": 7, "truncated": True}
    assert result["coverage"]["partial"]


def test_missing_and_failed_sections_are_distinct_and_not_zero_filled():
    req = CompanyProfile(domain="example.com", sections=["traffic", "products"])
    missing = profile_payload(record(), {}, req, "public")
    failed = profile_payload(record(), {}, req, "public", enrichment_failed=True)
    assert "traffic" not in missing["company"]
    assert missing["coverage"]["sections"]["traffic"]["status"] == "not_observed"
    assert failed["coverage"]["sections"]["traffic"]["status"] == "unavailable"
    assert failed["coverage"]["partial"]
    doc = record()
    doc["enrichment"]["finalized_products"] = []
    empty = profile_payload(doc, {}, req, "public")
    assert empty["company"]["products"] == []
    assert empty["coverage"]["sections"]["products"]["available"]


@pytest.mark.parametrize("shape", [lambda d: d, lambda d: [d], lambda d: {"0": d}])
def test_legacy_cards_retain_nested_sectors_products_and_entitled_extras(shape):
    value = {"name": "Example", "w": "example.com", "sectors_object": shape({
        "PRACTICE AREA": ["FinTech"], "FEED": ["Payments"], "BUSINESS MODEL": ["Gateway"]}),
        "finalized_products": ["Payments"], "_extras": {"revenue": {"value": "$1M"}},
        "data": {"sk": {"Python": 4}, "private": "do not expose"}}
    out = company_card(value)
    assert out["classification"]["markets"] == ["Payments"]
    assert out["classification"]["sectors"] == ["FinTech"]
    assert out["extras"]["revenue"]["value"] == "$1M"
    assert out["skills"] == {"Python": 4}
    assert "private" not in str(out)


class Cursor:
    def __init__(self, rows):
        self.rows = rows

    def limit(self, n):
        assert n == 2
        self.rows = self.rows[:n]
        return self

    def max_time_ms(self, ms):
        assert ms == 5000
        return iter(self.rows)


class Collection:
    def __init__(self, rows):
        self.rows, self.queries = rows, []

    def find(self, query, projection):
        self.queries.append(query)
        assert projection == PROJECTION
        return Cursor([deepcopy(row) for row in self.rows if row["identity"]["domain"] == query["identity.domain"]
                       and ("_id" not in query or row["_id"] == query["_id"])])

    def find_one(self, query, projection, **kwargs):
        self.queries.append(query)
        assert kwargs["max_time_ms"] == 3000
        return next((row for row in self.rows if all(row.get(k) == v for k, v in query.items())), None)


class StoreClient:
    def __init__(self, docs):
        self.main_data = Collection(docs)
        self.company_pubmap = Collection([{"_id": "public-example", "src": "internal-source-id"}])
        self.company_enrichment = Collection([])

    def __getitem__(self, name):
        assert name == "companies_data"
        return self

    def close(self):
        pass


@pytest.mark.asyncio
async def test_store_requires_auth_and_uses_domain_and_public_id_together():
    client = StoreClient([record()])
    store = ProfileStore(Settings(), client)
    req = CompanyProfile(domain="example.com", company_id="public-example")
    with pytest.raises(RadarError) as exc:
        await store.get(req)
    assert exc.value.status == 401 and not client.main_data.queries
    token = CURRENT.set(Principal("test", "test"))
    try:
        result = await store.get(req)
        assert result["company"]["company_id"] == "public-example"
        assert client.main_data.queries[-1] == {"identity.domain": "example.com", "_id": "internal-source-id"}
        with pytest.raises(RadarError) as exc:
            await store.get(CompanyProfile(domain="other.com", company_id="public-example"))
        assert exc.value.status == 404
    finally:
        CURRENT.reset(token)


def test_ambiguous_domain_never_silently_selects_another_entity():
    first, second = record(), record()
    second["_id"] = "another-entity"
    store = ProfileStore(Settings(), StoreClient([first, second]))
    with pytest.raises(RadarError) as exc:
        store._read(CompanyProfile(domain="example.com"))
    assert exc.value.kind == "ambiguous_company"
    assert store._read(CompanyProfile(domain="example.com", company_id="public-example"))["company"]["name"] == "Example"


@pytest.mark.asyncio
async def test_profile_failure_does_not_leak_driver_details(monkeypatch):
    store = ProfileStore(Settings(), StoreClient([]))
    def fail(_):
        raise ServerSelectionTimeoutError("mongodb://private-secret@127.0.0.1/internal")
    monkeypatch.setattr(store, "_read", fail)
    token = CURRENT.set(Principal("test", "test"))
    try:
        with pytest.raises(RadarError) as exc:
            await store.get(CompanyProfile(domain="example.com"))
        assert exc.value.status == 503 and "private-secret" not in exc.value.message
    finally:
        CURRENT.reset(token)


@pytest.mark.asyncio
async def test_profile_response_budget_and_optional_store_failure(monkeypatch):
    client = StoreClient([record()])
    store = ProfileStore(Settings(max_response_bytes=1024), client)
    def fail(*_, **__):
        raise ServerSelectionTimeoutError("private diagnostics")
    monkeypatch.setattr(client.company_enrichment, "find_one", fail)
    data = store._read(CompanyProfile(domain="example.com", sections=["people", "traffic"]))
    assert data["coverage"]["sections"]["traffic"]["status"] == "unavailable"
    assert data["coverage"]["sections"]["people"]["status"] == "available"
    token = CURRENT.set(Principal("test", "test"))
    try:
        with pytest.raises(RadarError) as exc:
            await store.get(CompanyProfile(domain="example.com"))
        assert exc.value.kind == "response_too_large"
    finally:
        CURRENT.reset(token)


@pytest.mark.parametrize("body", [{"domain": "example.com", "item_limit": 251},
                                  {"domain": "example.com", "sections": ["contact"]},
                                  {"domain": "example.com", "company_id": {"$ne": None}}])
def test_profile_query_bounds_and_no_raw_query_input(body):
    with pytest.raises(ValidationError):
        CompanyProfile.model_validate(body)


@pytest.mark.asyncio
async def test_http_and_mcp_share_deep_profile_fields(harness):
    from mcp import ClientSession
    from mcp.client.streamable_http import streamable_http_client
    import httpx
    from conftest import KEY
    from test_mcp import served
    from radar_api.server import create_app

    client, _, app = harness
    app.state.service.profiles = ProfileStore(Settings(), StoreClient([record()]))
    body = {"domain": "example.com", "sections": ["classification", "people", "technology", "apps"]}
    rest = client.post("/v1/companies/profile", json=body).json()
    assert len(rest["data"]["company"]["classification"]["feeds"]["other"]) == 18
    assert not rest["meta"]["partial"]
    upstream = app.state.service.upstream
    server_app = create_app(upstream.settings, upstream)
    server_app.state.service.profiles = ProfileStore(Settings(), StoreClient([record()]))
    with served(server_app) as base:
        async with httpx.AsyncClient(headers={"X-API-Key": KEY}) as http, streamable_http_client(base + "/mcp", http_client=http) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                result = await session.call_tool("get_company", {"request": body})
                assert not result.isError
                assert result.structuredContent["data"] == rest["data"]
