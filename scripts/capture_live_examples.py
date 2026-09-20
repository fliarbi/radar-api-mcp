#!/usr/bin/env python3
"""Capture bounded, authenticated gateway responses for documentation review.

Raw captures stay in owner-only ignored QA files. This does not publish anything,
mint production credentials, activate accounts, or start upstream services.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import time
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

import httpx

from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.service import FEATURES

CASES = {
    "search_companies": {"filters": {"industries": ["Software"], "locations": ["India"]}, "limit": 2},
    "semantic_company_search": {"q": "enterprise software companies in India", "limit": 2},
    "get_company": {"domain": "microsoft.com"},
    "get_company_intelligence": {"domain": "microsoft.com"},
    "get_financials": {"domain": "microsoft.com", "limit": 2},
    "get_company_events": {"domain": "microsoft.com", "days": 30, "limit": 2},
    "get_company_funding": {"domain": "openai.com"},
    "get_company_enrichment": {"domain": "microsoft.com"},
    "find_competitors": {"market": "Software", "per_stage": 3},
    "company_brief": {"domain": "microsoft.com", "include_news": True, "news_limit": 2, "event_days": 30},
    "compare_companies": {"domains": ["microsoft.com", "salesforce.com"]},
    "search_investors": {"filters": {"locations": ["India"]}, "limit": 2},
    "investor_directory": {},
    "get_investor_page": {"slug": "unavailable-example"},
    "market_pulse": {"days": 30, "limit": 2},
    "location_intelligence": {"location": "India", "location_type": "country"},
    "discover_industries": {"q": "software", "limit": 3},
    "search_jobs": {"q": "engineer", "limit": 2},
    "companies_hiring": {"q": "engineer", "limit": 2},
    "get_job": {"id": "unavailable-example"},
    "salary_benchmark": {"title": "engineer", "country": "India", "currency": "INR"},
    "search_people": {"name": "Satya Nadella", "limit": 1},
    "search_news": {"q": "software earnings", "limit": 2},
    "search_business_news": {"company": "microsoft.com", "limit": 2},
    "news_overview": {"q": "software earnings"},
    "news_trends": {"q": "software earnings", "granularity": "weekly"},
    "news_sentiment": {"company": "microsoft.com", "granularity": "weekly"},
    "search_business_events": {"company": "microsoft.com", "limit": 2},
    "search_funding_news": {"q": "startup funding", "limit": 2},
    "get_article": {"article_id": "000000000000000000000000"},
}


async def capture(args):
    logging.getLogger("httpx").setLevel(logging.WARNING)
    key = os.getenv("RADAR_API_KEY") or Path(args.key_file).read_text().strip()
    settings = replace(Settings.from_env(), timeout_seconds=20, allowed_hosts=("capture.local",))
    app = create_app(settings)
    report = {"captured_at": datetime.now(timezone.utc).isoformat(),
              "transport": "local ASGI gateway with live configured upstream HTTP services",
              "account_mode": settings.accounts_enabled,
              "news_configured": bool(settings.news_url),
              "business_news_configured": bool(settings.business_news_url), "operations": {}}
    output = Path(args.output)
    output.parent.mkdir(mode=0o700, parents=True, exist_ok=True)

    def save():
        fd = os.open(output, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0o600)
        with os.fdopen(fd, "w") as handle:
            os.fchmod(handle.fileno(), 0o600)
            json.dump(report, handle, indent=2)
            handle.write("\n")

    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://capture.local",
                                 headers={"X-API-Key": key}, timeout=90) as client:
        for feature in FEATURES:
            name, body = feature.name, dict(CASES[feature.name])
            if name == "get_investor_page":
                directory = report["operations"].get("investor_directory", {}).get("response", {}).get("data") or {}
                rows = directory.get("top_profiles", []) or directory.get("top_lists", [])
                if rows and rows[0].get("slug"):
                    body["slug"] = rows[0]["slug"]
            if name == "get_job":
                jobs = report["operations"].get("search_jobs", {}).get("response", {}).get("data") or {}
                rows = jobs.get("jobs", []) or jobs.get("items", [])
                if rows and (rows[0].get("id") or rows[0].get("job_id")):
                    body["id"] = rows[0].get("id") or rows[0]["job_id"]
            if name == "get_article":
                data = report["operations"].get("get_financials", {}).get("response", {}).get("data") or {}
                ids = [i for p in data.get("periods", []) for i in p.get("article_ids", [])]
                if ids:
                    body["article_id"] = ids[0]
            feature.model.model_validate(body)
            started = time.monotonic()
            try:
                async with asyncio.timeout(90):
                    response = await client.post("/v1/" + feature.path, json=body)
                payload = response.json()
                row = {"method": "POST", "path": "/v1/" + feature.path, "request": body,
                       "http_status": response.status_code, "response": payload,
                       "elapsed_seconds": round(time.monotonic() - started, 3),
                       "provenance": "live gateway capture"}
            except Exception as exc:
                row = {"method": "POST", "path": "/v1/" + feature.path, "request": body,
                       "capture_error": type(exc).__name__, "provenance": "capture did not complete"}
            report["operations"][name] = row
            save()
            print(name, row.get("http_status", row.get("capture_error")),
                  row.get("response", {}).get("error", {}).get("kind", "ok"), flush=True)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--key-file", default="secrets/client-key.txt")
    parser.add_argument("--output", default="qa/private/endpoint-live.json")
    asyncio.run(capture(parser.parse_args()))
