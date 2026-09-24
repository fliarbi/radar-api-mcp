#!/usr/bin/env python3
"""Capture bounded smaller-company examples using operator-configured read-only sources."""
import asyncio
from dataclasses import replace
from datetime import datetime, timezone
import json
import logging
from pathlib import Path

import httpx

from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.service import BY_NAME

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    ("yext-products.json", "get_company_field", {"domain": "yext.com", "field": "products", "item_limit": 10}),
    ("yext-activity.json", "get_company_field", {"domain": "yext.com", "field": "activity", "item_limit": 10}),
    ("mastech-annual-income.json", "get_financials", {"domain": "mastechdigital.com", "statement": "income", "period_type": "annual", "limit": 3}),
]


async def main():
    logging.getLogger("httpx").setLevel(logging.WARNING)
    app = create_app(replace(Settings.from_env(), allowed_hosts=("capture.local",), timeout_seconds=30))
    key = (ROOT / "secrets/client-key.txt").read_text().strip()
    rows = []
    try:
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://capture.local", headers={"X-API-Key": key}) as client:
            for filename, operation, request in CASES:
                path = "/v1/" + BY_NAME[operation].path
                response = await client.post(path, json=request)
                rows.append({"file": filename, "operation": operation, "request": request,
                             "path": path, "method": "POST", "http_status": response.status_code,
                             "response": response.json(), "capture_kind": "live_gateway",
                             "captured_at": datetime.now(timezone.utc).isoformat(), "provenance": "live gateway capture"})
                print(filename, response.status_code, flush=True)
        target = ROOT / "qa/private/example-replacements.json"
        target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        target.touch(mode=0o600)
        target.chmod(0o600)
        target.write_text(json.dumps(rows, indent=2) + "\n")
    finally:
        if app.state.service.profiles:
            app.state.service.profiles.close()
        if app.state.service.internships:
            app.state.service.internships.close()


if __name__ == "__main__":
    asyncio.run(main())
