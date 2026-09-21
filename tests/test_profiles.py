from __future__ import annotations
from copy import deepcopy
import json
from datetime import datetime, timezone
import pytest
from pydantic import ValidationError
from pymongo.errors import ServerSelectionTimeoutError
from radar_api.auth import CURRENT, Principal
from radar_api.config import Settings
from radar_api.errors import RadarError
from radar_api.models import CompanyProfile, CompanyField, CompanyProfileData, PROFILE_SECTIONS
from radar_api.profiles import (
    ProfileStore,
    FIELD_PROJECTIONS,
    SUMMARY_PROJECTION,
    summary_projection,
    profile_payload,
)


def record():
    return {
        "_id": "internal-source-id",
        "identity": {"name": "Example", "domain": "example.com"},
        "descriptive": {"short_description": "A payments business", "founded_year": 2014},
        "classification": {
            "practice_areas": [{"id": "provider-id", "name": "FinTech"}],
            "feeds_primary": [{"name": "Payments"}],
            "feeds_other": [{"name": f"Category {i}"} for i in range(18)],
        },
        "people": {
            "key_people_count": 3,
            "key_people": [
                {
                    "name": "Founder One",
                    "designation": "Co-Founder & CEO",
                    "email": "private@example.com",
                    "id": "internal",
                },
                {"name": "Founder Two", "designation": "Founder", "phone": "private"},
                {"name": "Executive Three", "designation": "CTO"},
            ],
        },
        "enrichment": {
            "website_stacks": [f"Technology {i}" for i in range(70)],
            "finalized_products": ["Payments"],
        },
        "traction": {"mobile_app": {"count": 5, "downloads": 100, "weighted_rating": 0}},
        "web_presence": {"crawl_date": "2026-05-01", "source": "internal-provider", "tech_count": 70},
        "financials": {"employees": 120, "latest_estimated_revenue_usd": 900000000},
        "extras": {"updated_at": datetime(2026, 9, 20, tzinfo=timezone.utc)},
        "contact": {"email": "private@example.com"},
        "scores": {"innovation": 0, "finance_source": "private"},
    }


def lookup(doc, path):
    for key in path.split("."):
        if not isinstance(doc, dict) or key not in doc:
            return None
        doc = doc[key]
    return doc


def project(doc, paths):
    result = {"_id": doc["_id"]}
    for path in paths:
        value = lookup(doc, path)
        if value is None:
            continue
        target = result
        bits = path.split(".")
        for bit in bits[:-1]:
            target = target.setdefault(bit, {})
        target[bits[-1]] = deepcopy(value)
    return result


class Cursor:
    def __init__(self, rows):
        self.rows = rows

    def limit(self, n):
        self.rows = self.rows[:n]
        return self

    def max_time_ms(self, ms):
        return iter(self.rows)


class Collection:
    def __init__(self, rows):
        self.rows, self.queries, self.projections = rows, [], []

    def find(self, query, projection):
        self.queries.append(query)
        self.projections.append(projection)
        return Cursor(
            [
                project(row, projection)
                for row in self.rows
                if all(lookup(row, k) == v for k, v in query.items())
            ]
        )

    def find_one(self, query, projection, **kwargs):
        self.queries.append(query)
        self.projections.append(projection)
        return next(
            (
                project(row, projection)
                for row in self.rows
                if all(lookup(row, k) == v for k, v in query.items())
            ),
            None,
        )

    def aggregate(self, pipeline, **kwargs):
        query, projection = pipeline[0]["$match"], pipeline[-1]["$project"]
        self.queries.append(query)
        self.projections.append(projection)
        rows = [row for row in self.rows if all(lookup(row, k) == v for k, v in query.items())][
            : pipeline[1]["$limit"]
        ]
        out = []
        for row in rows:
            if "field_presence" in projection:
                d = project(row, SUMMARY_PROJECTION)
                d["field_presence"] = {
                    key: any(lookup(row, p) is not None for p in paths)
                    for key, paths in FIELD_PROJECTIONS.items()
                }
                d["contact_presence"] = {
                    key: bool(lookup(row, "contact." + key)) for key in ("emails", "phones")
                }
            else:
                d = {key: row.get(key) is not None for key in projection if key != "_id"}
            out.append(d)
        return out


class StoreClient:
    def __init__(self, docs):
        self.main_data = Collection(docs)
        self.company_pubmap = Collection([{"_id": "public-example", "src": "internal-source-id"}])
        self.company_enrichment = Collection(
            [{"_id": "example.com", "digital": {"visits": 0, "visits_date": "2026-05-01"}}]
        )

    def __getitem__(self, name):
        assert name == "companies_data"
        return self

    def close(self):
        pass


def test_summary_returns_identity_availability_and_no_rich_values_or_contacts():
    doc = record()
    doc["descriptive"]["logo_url"] = "https://s3.amazonaws.com/tracxn-data-image/logo/company/source"
    doc["contact"] = {"emails": ["private@example.com"], "phones": []}
    client = StoreClient([doc])
    store = ProfileStore(Settings(), client)
    result = store._read(CompanyProfile(domain="example.com"))
    CompanyProfileData.model_validate(result)
    assert result["profile_depth"] == "summary"
    assert {"technology", "classification", "people", "traffic", "apps"} <= set(result["available_fields"])
    assert result["contacts"]["availability"] == {"emails": True, "phones": False}
    assert set(result["company"]) == {
        "name",
        "domain",
        "company_id",
        "description",
        "founded",
        "employee_count",
        "logo_url",
    }
    for value in ["Technology 1", "Founder One", "private@example.com", "tracxn", "visits_date", "900000000"]:
        assert value not in json.dumps(result)
    projection = client.main_data.projections[-1]
    assert projection == summary_projection()
    assert "people" not in projection and "classification" not in projection and "contact" not in projection


@pytest.mark.parametrize("field", list(PROFILE_SECTIONS))
def test_field_is_explicit_and_projection_does_not_fetch_other_sections(field):
    client = StoreClient([record()])
    store = ProfileStore(Settings(), client)
    result = store._read(CompanyField(domain="example.com", field=field))
    assert result["field"] == field and "company" not in result and "available_fields" not in result
    assert set(client.main_data.projections[-1]) == {
        "identity.domain",
        "extras.updated_at",
        *FIELD_PROJECTIONS[field],
    }
    assert "private@example.com" not in json.dumps(result)
    assert "900000000" not in json.dumps(result)


def test_field_preserves_zero_founders_and_explicit_array_limits():
    store = ProfileStore(Settings(), StoreClient([record()]))
    tech = store._read(CompanyField(domain="example.com", field="technology", item_limit=7))
    assert len(tech["value"]["website_stack"]) == 7
    assert tech["coverage"]["arrays"]["/value/website_stack"] == {
        "available": 70,
        "returned": 7,
        "truncated": True,
    }
    assert tech["coverage"]["partial"]
    assert store._read(CompanyField(domain="example.com", field="traffic"))["value"]["visits"] == 0
    assert len(store._read(CompanyField(domain="example.com", field="people"))["value"]["founders"]) == 2
    assert store._read(CompanyField(domain="example.com", field="apps"))["value"]["weighted_rating"] == 0


def test_empty_missing_and_failed_fields_are_distinct():
    doc = record()
    doc["enrichment"]["finalized_products"] = []
    req = CompanyField(domain="example.com", field="products")
    assert profile_payload(doc, {}, req, "public")["value"] == []
    req = CompanyField(domain="example.com", field="traffic")
    missing = profile_payload(doc, {}, req, "public")
    failed = profile_payload(doc, {}, req, "public", enrichment_failed=True)
    assert missing["status"] == "not_observed" and missing["value"] is None
    assert failed["status"] == "unavailable" and failed["coverage"]["partial"]


def test_null_source_blocks_do_not_become_available_or_crash():
    doc = {"identity": {"domain": "example.com"}, **{key: None for key in (
        "descriptive", "classification", "people", "web_presence", "enrichment", "financials",
        "traction", "lifecycle", "structure", "scores", "extras")}}
    for field in PROFILE_SECTIONS:
        result = profile_payload(doc, {}, CompanyField(domain="example.com", field=field), "public")
        assert result["status"] == "not_observed" and result["value"] is None


def test_provider_and_malformed_asset_urls_are_not_forwarded():
    from radar_api.public import clean
    source = {"logo_url": "https://s3.amazonaws.com/tracxn-data-image/logo/id", "photo_url": "http://[", "nested": {
        "logo_url": "https://fliarbi.com/logos/by_domain.php?domain=example.com"}}
    result = clean(source)
    assert result["logo_url"] is None and result["photo_url"] is None
    assert result["nested"]["logo_url"] == source["nested"]["logo_url"]


@pytest.mark.asyncio
async def test_store_requires_auth_and_disambiguates_public_id_and_domain():
    first, second = record(), record()
    second["_id"] = "another"
    store = ProfileStore(Settings(), StoreClient([first, second]))
    with pytest.raises(RadarError) as exc:
        await store.get(CompanyProfile(domain="example.com"))
    assert exc.value.status == 401
    token = CURRENT.set(Principal("test", "test"))
    try:
        with pytest.raises(RadarError) as exc:
            await store.get(CompanyProfile(domain="example.com"))
        assert exc.value.kind == "ambiguous_company"
        result = await store.get(CompanyProfile(domain="example.com", company_id="public-example"))
        assert result["company"]["company_id"] == "public-example"
        with pytest.raises(RadarError) as exc:
            await store.get(CompanyField(domain="other.com", company_id="public-example", field="people"))
        assert exc.value.status == 404
    finally:
        CURRENT.reset(token)


@pytest.mark.asyncio
async def test_store_failure_is_sanitized_and_response_budget_applies(monkeypatch):
    store = ProfileStore(Settings(max_response_bytes=1024), StoreClient([record()]))
    token = CURRENT.set(Principal("test", "test"))
    try:
        with pytest.raises(RadarError) as exc:
            await store.get(CompanyProfile(domain="example.com"))
        assert exc.value.kind == "response_too_large"

        def fail(_):
            raise ServerSelectionTimeoutError("mongodb://private-secret@127.0.0.1/internal")

        monkeypatch.setattr(store, "_read", fail)
        with pytest.raises(RadarError) as exc:
            await store.get(CompanyProfile(domain="example.com"))
        assert exc.value.status == 503 and "private-secret" not in exc.value.message
    finally:
        CURRENT.reset(token)


@pytest.mark.parametrize(
    "body",
    [{"domain": "example.com", "sections": ["technology"]}, {"domain": "example.com", "item_limit": 2}],
)
def test_summary_rejects_old_bulk_detail_inputs(body):
    with pytest.raises(ValidationError):
        CompanyProfile.model_validate(body)


@pytest.mark.parametrize(
    "body",
    [
        {"domain": "example.com"},
        {"domain": "example.com", "field": "contact"},
        {"domain": "example.com", "field": "technology", "item_limit": 101},
        {"domain": "example.com", "field": {"$ne": None}},
    ],
)
def test_field_validation_rejects_missing_unknown_or_unbounded_selectors(body):
    with pytest.raises(ValidationError):
        CompanyField.model_validate(body)


@pytest.mark.asyncio
async def test_http_and_mcp_share_one_field_projection(harness):
    from mcp import ClientSession
    from mcp.client.streamable_http import streamable_http_client
    import httpx
    from conftest import KEY
    from test_mcp import served
    from radar_api.server import create_app

    client, _, app = harness
    app.state.service.profiles = ProfileStore(Settings(), StoreClient([record()]))
    body = {"domain": "example.com", "field": "technology", "item_limit": 100}
    rest = client.post("/v1/companies/field", json=body).json()
    assert len(rest["data"]["value"]["website_stack"]) == 70
    server_app = create_app(app.state.service.upstream.settings, app.state.service.upstream)
    server_app.state.service.profiles = ProfileStore(Settings(), StoreClient([record()]))
    with served(server_app) as base:
        async with (
            httpx.AsyncClient(headers={"X-API-Key": KEY}) as http,
            streamable_http_client(base + "/mcp", http_client=http) as streams,
        ):
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                result = await session.call_tool("get_company_field", {"request": body})
                assert not result.isError and result.structuredContent["data"] == rest["data"]
