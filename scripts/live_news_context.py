"""Explicit local integration context; real News queries, isolated test auth/quota."""

from contextlib import asynccontextmanager
from dataclasses import replace
from pathlib import Path
import json
import logging
import os
import secrets
import sys
import tempfile
from unittest.mock import patch
import httpx


@asynccontextmanager
async def connect(settings):
    sys.path[:0] = [os.environ["RADAR_NEWS_APP_DIR"], os.environ["RADAR_BUSINESS_NEWS_APP_DIR"]]
    from prism_news_api import auth, config, quota
    from prism_news_api.main import create_app as news_app
    from prism_news_api.routers import metered, unmetered
    from prism_business_api.main import create_app as business_app

    logging.getLogger().setLevel(logging.ERROR)
    user = auth.Principal(
        user_id="0" * 24,
        key_id="1" * 24,
        key_prefix="integration",
        key_name="scenario integration",
        email=None,
        plan="free",
        plan_cfg=config.plan_cfg("free"),
        source="integration",
        expired=False,
        expires=None,
        account_flag=None,
    )
    apps = {"news.integration": news_app(), "business.integration": business_app()}
    for app in apps.values():
        app.dependency_overrides[metered] = lambda: user
        app.dependency_overrides[unmetered] = lambda: user
    transports = {
        host: httpx.ASGITransport(app=app, raise_app_exceptions=False) for host, app in apps.items()
    }
    network = httpx.AsyncHTTPTransport(retries=0)

    class Transport(httpx.AsyncBaseTransport):
        async def handle_async_request(self, request):
            return await transports.get(request.url.host, network).handle_async_request(request)

    with tempfile.TemporaryDirectory() as directory:
        keys = json.loads(Path(settings.keys_file).read_text())
        for row in keys["keys"]:
            row["news_key"] = "pna_" + secrets.token_hex(20)
        target = Path(directory) / "keys.json"
        target.write_text(json.dumps(keys))
        target.chmod(0o600)
        configured = replace(
            settings,
            keys_file=str(target),
            news_url="http://news.integration",
            business_news_url="http://business.integration",
        )
        with (
            patch.object(quota, "record_daily", lambda *a, **k: None),
            patch.object(quota, "reserve_exports", lambda user, key, n, limit: n),
            patch.object(quota, "refund_exports", lambda *a, **k: None),
            patch.object(quota, "exports_remaining", lambda *a, **k: 100),
        ):
            yield configured, Transport()
        await network.aclose()
