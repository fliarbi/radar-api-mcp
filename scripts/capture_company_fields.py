#!/usr/bin/env python3
"""Capture compact profiles and explicit field requests through the authenticated gateway."""
import asyncio
from dataclasses import replace
import json
import logging
import os
from pathlib import Path

import httpx

from radar_api.config import Settings
from radar_api.models import PROFILE_SECTIONS
from radar_api.server import create_app

ROOT = Path(__file__).resolve().parents[1]


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd = os.open(path, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "w") as handle:
        os.fchmod(handle.fileno(), 0o600)
        json.dump(data, handle, indent=2)
        handle.write("\n")


async def capture():
    logging.getLogger("httpx").setLevel(logging.WARNING)
    settings = replace(Settings.from_env(), allowed_hosts=("capture.local",))
    assert settings.profile_mongo_uri, "Configure the detailed profile connection before capturing"
    key = os.getenv("RADAR_API_KEY") or (ROOT / "secrets/client-key.txt").read_text().strip()
    app = create_app(settings)
    try:
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://capture.local", headers={"X-API-Key": key}) as client:
            for domain in ("razorpay.com", "stripe.com", "swiggy.com"):
                response = await client.post("/v1/companies/profile", json={"domain": domain})
                assert response.status_code == 200, (domain, response.status_code)
                save(ROOT / "qa/private" / ("profile-" + domain + ".json"), response.json())
                for field in PROFILE_SECTIONS:
                    body = {"domain": domain, "field": field, "item_limit": 100}
                    response = await client.post("/v1/companies/field", json=body)
                    assert response.status_code == 200, (domain, field, response.status_code)
                    save(ROOT / "qa/private" / ("field-" + domain + "-" + field + ".json"), {"request": body, "response": response.json()})
                print(json.dumps({"domain": domain, "profile": "summary", "field_captures": len(PROFILE_SECTIONS)}), flush=True)
    finally:
        app.state.service.profiles.close()


if __name__ == "__main__":
    asyncio.run(capture())
