from __future__ import annotations

import hashlib
import json

import httpx
import pytest
from fastapi.testclient import TestClient

from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.upstream import Upstream

KEY = "rdr_" + "1" * 64
KEY2 = "rdr_" + "2" * 64
ARTICLE = "1234567890abcdef12345678"

EARNINGS = {
    "domain": "example.com", "computed_at": "2026-09-18T00:00:00Z", "intel": {
        "entity_resolution": {"database": "private_store"}, "investment_readiness": {"score": 75},
        "earnings": {"has_data": True, "gated": True, "history_total_count": 12, "history": [
            {"period_year": 2025, "period_qtr": "FY", "period_label": "FY2025", "date": "2026-02-01",
             "period_end": "2025-12-31", "filed_date": "2026-02-01", "form_type": "annual",
             "revenue_usd": 120, "net_income_usd": 0, "total_assets_usd": 250,
             "operating_cash_flow_usd": 15, "eps": 1.2, "currency_native": "INR",
             "native": {"revenue_usd": 10000}, "field_sources": {"revenue_usd": "official", "eps": "bi"},
             "primary_source": "official", "source_target_ids": [ARTICLE], "fx_source": "annual_average"},
            {"period_year": 2026, "period_qtr": "Q1", "period_label": "Q1 FY2026", "date": "2026-04-30",
             "revenue_usd": 35, "net_income_usd": -2, "primary_source": "bi"},
        ]},
    },
}


def payload_for(path):
    if path == "/company_intel/":
        return json.loads(json.dumps(EARNINGS))
    if path in {"/company_search/", "/company_search/shortlist_hydrate", "/semantic_search/"}:
        return {"companies": [{"name": "Example", "w": "example.com", "desc": "Example company",
                 "idx": "public-id", "password": "must-not-leak", "contact_infox": {"email": "private"}}],
                "_plan": "free", "_extras_gated": True, "_entitlements": {"plan": "free"}}
    if path in {"/company_search/contact", "/people_search/contact"}:
        return {"emails": ["sales@example.com"], "phones": ["+1-202-555-0123"], "source": "company_domain"}
    if path == "/company_search/cols":
        return {"example.com": {"employees": {"label": "Employees", "value": "51-200"}}}
    if path == "/people_search/suggest":
        return {"results": ["Python"]}
    if path == "/competitive/":
        return {"companies": {"Seed": [{"name": "Peer", "w": "peer.com"}]}, "summary": {"count": 1}}
    if path == "/company_events/":
        return {"events": [{"headline": "Announced results", "target_id": ARTICLE}], "window_days": 30,
                "_data_freshness": {"latest_event_date": "2026-08-01"}, "_truncated": True}
    if path == "/company_enrichment/":
        return {"has_data": True, "hiring": {"total": 5}}
    if path == "/metas/":
        return {"matched": [["Software", "feeds"], ["Digital Health", "PRACTICE_AREA"]]}
    if path == "/investors/index":
        return {"top_profiles": [{"_id": "example-investor", "h1": "Example Investor"}],
                "sectors": [{"_id": "Software", "pages": 5}]}
    if path.startswith("/v1/"):
        return {"ok": True, "data": {"items": [{"article_id": ARTICLE, "headline": "Results",
                "url": "https://example.com/news"}], "next_cursor": "next_page"},
                "window": {"since": "2026-01-01", "until": "2026-08-01", "data_through": "2026-08-01"},
                "meta": {"notes": ["Coverage is incomplete"]}}
    return {"has_data": True, "items": [], "sql": "SELECT secret FROM hidden"}


SAMPLES = {
    "search_companies": {"filters": {"industries": ["Software"]}},
    "semantic_company_search": {"q": "software companies"},
    "get_company": {"domain": "example.com"},
    "get_company_field": {"domain": "example.com", "field": "technology"},
    "company_filter_catalog": {},
    "company_filter_options": {"field": "sectors", "q": "Fin"},
    "get_company_columns": {"domains": ["example.com"], "columns": ["employees"]},
    "people_filter_options": {"field": "skills", "q": "Py"},
    "get_company_contacts": {"domain": "example.com", "fields": ["emails"]},
    "get_person_contacts": {"person_id": "person-example", "fields": ["phones"]},
    "get_company_intelligence": {"domain": "example.com"},
    "get_financials": {"domain": "example.com"},
    "get_company_events": {"domain": "example.com"},
    "get_company_funding": {"domain": "example.com"},
    "get_company_enrichment": {"domain": "example.com"},
    "find_competitors": {"market": "Software"},
    "company_brief": {"domain": "example.com"},
    "compare_companies": {"domains": ["example.com", "peer.com"]},
    "search_investors": {}, "investor_directory": {},
    "get_investor_page": {"slug": "example-investor"},
    "market_pulse": {}, "location_intelligence": {"location": "India"},
    "discover_industries": {"q": "software"}, "search_jobs": {"company": "example.com"},
    "companies_hiring": {"q": "engineer"}, "get_job": {"id": "job-123"},
    "salary_benchmark": {"title": "engineer", "currency": "USD"},
    "search_people": {"roles": ["founder"]},
    "search_news": {"q": "software"}, "search_business_news": {"company": "example.com"},
    "news_overview": {"q": "software"}, "news_trends": {"q": "software"},
    "news_sentiment": {"company": "example.com"}, "search_business_events": {"company": "example.com"},
    "search_funding_news": {"q": "software", "investor": "Example VC"},
    "get_article": {"article_id": ARTICLE},
}


@pytest.fixture
def keyfile(tmp_path):
    path = tmp_path / "keys.json"
    path.write_text(json.dumps({"keys": [
        {"sha256": hashlib.sha256(key.encode()).hexdigest(), "active": True, "name": "test",
         "radar_token": token, "news_key": news, "rate_per_minute": 600, "scopes": ["*", "contacts"]}
        for key, token, news in [(KEY, "session-one", "news-one"), (KEY2, "session-two", "news-two")]
    ]}))
    path.chmod(0o600)
    return path


@pytest.fixture
def harness(keyfile):
    calls = []

    def respond(request):
        calls.append(request)
        return httpx.Response(200, json=payload_for(request.url.path))

    settings = Settings(radar_url="http://radar.local", news_url="http://news.local",
                        business_news_url="http://business.local", keys_file=str(keyfile),
                        allowed_hosts=("testserver", "127.0.0.1", "localhost"))
    upstream = Upstream(settings, httpx.MockTransport(respond))
    app = create_app(settings, upstream)
    with TestClient(app) as client:
        client.headers["X-API-Key"] = KEY
        yield client, calls, app
