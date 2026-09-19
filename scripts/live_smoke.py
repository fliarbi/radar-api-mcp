#!/usr/bin/env python3
"""Opt-in live reads. Record status/count metadata, never upstream payloads or keys."""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from fastapi.testclient import TestClient

from radar_api.config import Settings
from radar_api.server import create_app


CASES = [
    ("profile", "companies/profile", {"domain": "microsoft.com"}),
    ("financials", "companies/financials", {"domain": "microsoft.com"}),
    ("events", "companies/events", {"domain": "microsoft.com", "days": 30, "limit": 5}),
    ("funding", "companies/funding", {"domain": "openai.com"}),
    ("enrichment", "companies/enrichment", {"domain": "microsoft.com"}),
    ("investor_directory", "investors/directory", {}),
    ("jobs", "jobs/search", {"company": "microsoft.com", "limit": 2}),
    ("people", "people/search", {"name": "Satya Nadella", "limit": 2}),
    ("company_news", "news/business", {"company": "microsoft.com", "limit": 2}),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="qa/live-smoke.json")
    parser.add_argument("--key-file", default="secrets/client-key.txt")
    args = parser.parse_args()
    key = os.environ.get("RADAR_API_KEY") or Path(args.key_file).read_text().strip()
    configured = Settings.from_env()
    from dataclasses import replace
    settings = replace(configured, allowed_hosts=(*configured.allowed_hosts, "testserver"))
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "transport": "local ASGI gateway to live upstreams",
              "cases": [], "note": "Only response status and counts are stored. No public service is deployed."}
    with TestClient(create_app(settings)) as client:
        for name, path, body in CASES:
            response = client.post("/v1/" + path, json=body, headers={"X-API-Key": key})
            payload = response.json()
            result = {"name": name, "http_status": response.status_code, "ok": payload.get("ok", False),
                      "partial": payload.get("meta", {}).get("partial", False)}
            data = payload.get("data")
            if isinstance(data, dict):
                result["list_counts"] = {k: len(v) for k, v in data.items() if isinstance(v, list)}
                for field in ("access_limited", "returned", "has_data", "truncated", "total_capped"):
                    if field in data:
                        result[field] = data[field]
            if not result["ok"]:
                result["error_kind"] = payload.get("error", {}).get("kind")
            report["cases"].append(result)
            print(name, response.status_code, "ok" if result["ok"] else result.get("error_kind"))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    return 0 if all(case["ok"] for case in report["cases"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
