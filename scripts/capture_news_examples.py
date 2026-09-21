#!/usr/bin/env python3
"""Capture real News data through the gateway with isolated integration identities.

Loads the sibling private News applications in process. Only their identity/quota
dependencies are replaced; database queries, coverage gates, article resolution,
filtering, sanitization and the gateway remain real. No listener, customer account,
production key or billable usage is created. This is not deployment verification.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import logging
import os
from pathlib import Path
import secrets
import sys
import tempfile
import time
from dataclasses import replace
from datetime import datetime, timezone
from unittest.mock import patch

import httpx

from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.service import BY_NAME
from radar_api.upstream import Upstream

ROOT = Path(__file__).resolve().parents[1]
PROVENANCE = (
    "Executed authenticated local Radar gateway and actual Prism News application code against live data; "
    "isolated test identity and quota dependencies, with the News Free plan's data limits retained. "
    "No deployed News URL, production News-key authentication or customer billing was verified."
)


async def capture(args):
    os.environ.setdefault("PRISM_LOG_LEVEL", "CRITICAL")
    sys.path[:0] = [str(args.news_source), str(args.business_source)]
    from prism_news_api import auth, config, quota
    from prism_news_api.main import create_app as news_app
    from prism_news_api.routers import metered, unmetered
    from prism_business_api.main import create_app as business_app

    logging.getLogger().setLevel(logging.CRITICAL)
    user = auth.Principal(user_id="0" * 24, key_id="1" * 24, key_prefix="integration",
                          key_name="local documentation integration", email=None, plan="free",
                          plan_cfg=config.plan_cfg("free"), source="integration", expired=False,
                          expires=None, account_flag=None)

    def caller():
        return user

    apps = {"news.integration": news_app(), "business.integration": business_app()}
    for app in apps.values():
        app.dependency_overrides[metered] = caller
        app.dependency_overrides[unmetered] = caller
    transports = {host: httpx.ASGITransport(app=app, raise_app_exceptions=False) for host, app in apps.items()}
    network = httpx.AsyncHTTPTransport(retries=0)

    class NewsTransport(httpx.AsyncBaseTransport):
        async def handle_async_request(self, request):
            if request.url.host in transports:
                return await transports[request.url.host].handle_async_request(request)
            return await network.handle_async_request(request)

    report = json.loads(args.output.read_text()) if args.output.exists() else {"operations": {}}
    cases = {"search_news": {"q": "software earnings", "limit": 5},
             "search_business_news": {"company": "microsoft.com", "limit": 5},
             "news_overview": {"q": "software earnings"},
             "news_trends": {"q": "software earnings", "granularity": "weekly"},
             "news_sentiment": {"company": "microsoft.com", "granularity": "weekly"},
             "search_business_events": {"company": "microsoft.com", "limit": 5},
             "search_funding_news": {"q": "funding", "limit": 5},
             "get_article": {"article_id": "000000000000000000000000"}}
    for name, body in cases.items():
        if name != "get_article":
            body.update(date_from="2026-04-01", date_to="2026-04-30")
    if args.only and "company_brief" in args.only:
        cases["company_brief"] = {"domain": "stripe.com", "include_news": True, "news_limit": 3, "event_days": 30}
    previous_items = (report["operations"].get("search_news", {}).get("response", {}).get("data") or {}).get("items", [])
    article_id = previous_items[0].get("id") if previous_items else None
    with tempfile.TemporaryDirectory() as directory:
        key = "rdr_" + secrets.token_hex(32)
        keys = Path(directory) / "keys.json"
        keys.write_text(json.dumps({"keys": [{"sha256": hashlib.sha256(key.encode()).hexdigest(),
                         "name": "news documentation integration", "active": True,
                         "news_key": "pna_" + secrets.token_hex(20), "rate_per_minute": 60}]}))
        keys.chmod(0o600)
        settings = replace(Settings.from_env(), news_url="http://news.integration", business_news_url="http://business.integration",
                           keys_file=str(keys), accounts_enabled=False, allowed_hosts=("capture.local",), timeout_seconds=90)
        gateway = create_app(settings, Upstream(settings, NewsTransport()))
        with patch.object(quota, "record_daily", lambda *a, **k: None), \
             patch.object(quota, "reserve_exports", lambda user, key, n, limit: n), \
             patch.object(quota, "refund_exports", lambda *a, **k: None), \
             patch.object(quota, "exports_remaining", lambda *a, **k: 100):
            async with httpx.AsyncClient(transport=httpx.ASGITransport(app=gateway), base_url="http://capture.local",
                                         headers={"X-API-Key": key}, timeout=120) as client:
                for name, body in cases.items():
                    if args.only and name not in args.only:
                        continue
                    if name == "get_article":
                        if not article_id:
                            print("get_article skipped: no resolved headline ID", flush=True)
                            continue
                        body = {"article_id": article_id}
                    path = "/v1/" + BY_NAME[name].path
                    started = time.monotonic()
                    response = await client.post(path, json=body)
                    payload = response.json()
                    report["operations"][name] = {
                        "method": "POST", "path": path, "request": body, "http_status": response.status_code,
                        "response": payload, "elapsed_seconds": round(time.monotonic() - started, 3),
                        "captured_at": datetime.now(timezone.utc).isoformat(),
                        "capture_kind": "live_data_integration", "provenance": PROVENANCE + (
                            " Radar sections use the existing live HTTP service with anonymous access and the configured detailed profile store."
                            if name == "company_brief" else "")}
                    args.output.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
                    fd = os.open(args.output, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0o600)
                    with os.fdopen(fd, "w") as handle:
                        os.fchmod(handle.fileno(), 0o600)
                        json.dump(report, handle, ensure_ascii=False, indent=2)
                        handle.write("\n")
                    data = payload.get("data") or {}
                    items = data.get("items", [])
                    if name in {"search_news", "search_business_news"} and items:
                        article_id = items[0].get("id") if name == "search_news" else article_id or items[0].get("id")
                    print(json.dumps({"operation": name, "status": response.status_code,
                                      "seconds": round(time.monotonic() - started, 2),
                                      "returned": data.get("returned", len(items)),
                                      "fields": list(data), "error": payload.get("error")}), flush=True)
        if gateway.state.service.profiles:
            gateway.state.service.profiles.close()
    await network.aclose()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--news-source", type=Path, default=ROOT.parent / "prism-news-api")
    parser.add_argument("--business-source", type=Path, default=ROOT.parent / "prism-business-news-api")
    parser.add_argument("--output", type=Path, default=ROOT / "qa/private/endpoint-live.json")
    parser.add_argument("--only", nargs="+", choices=[name for name, f in BY_NAME.items() if f.source != "radar"] + ["company_brief"])
    asyncio.run(capture(parser.parse_args()))
