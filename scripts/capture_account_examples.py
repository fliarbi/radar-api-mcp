#!/usr/bin/env python3
"""Exercise every account endpoint in an isolated local demonstration.

Radar identity and Razorpay are explicit synthetic fixtures. The account API,
SQLite ledger, key hashing, spending checks and signature verification are real.
No network request, production account mutation or payment is performed.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import httpx
from cryptography.fernet import Fernet
from fastapi.testclient import TestClient

from radar_api.accounts import Accounts
from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.upstream import Upstream


def capture():
    def identity(request):
        return httpx.Response(200, json={"user": {"_id": "documentation-account", "email_verified": True},
            "plan": "business", "plan_details": {"features": ["api_access"], "searches_per_month": 5000,
                                                  "company_tracking": 1000}})

    def provider(request):
        body = json.loads(request.content)
        return httpx.Response(200, json={"id": "order_documentation", "amount": body["amount"], "currency": "INR"})

    report = {"captured_at": datetime.now(timezone.utc).isoformat(),
              "provenance": "Executed local account API; synthetic Radar identity and Razorpay responses; no live payment",
              "credential_redaction": "API keys, session tokens, News keys and webhook signatures are not published",
              "operations": {}}
    with tempfile.TemporaryDirectory(prefix="radar-account-docs-") as directory:
        settings = Settings(accounts_enabled=True, accounts_db=str(Path(directory) / "accounts.db"),
                            encryption_key=Fernet.generate_key().decode(), allowed_hosts=("testserver",),
                            radar_url="http://identity-fixture.invalid", credit_price_paise=10,
                            razorpay_key_id="rzp_test_documentation", razorpay_key_secret="fixture-only",
                            razorpay_webhook_secret="fixture-hook-only")
        transport = httpx.MockTransport(identity)
        accounts = Accounts(settings, transport, httpx.MockTransport(provider))
        with TestClient(create_app(settings, Upstream(settings, transport), accounts)) as client:
            client.headers["X-Auth-Token"] = "FIXTURE_RADAR_SESSION"

            def run(name, method, path, body=None, **kwargs):
                response = client.request(method, path, **({"json": body} if body is not None else {}), **kwargs)
                payload = response.json()
                actual = json.loads(json.dumps(payload))
                if name == "account_create_key" and payload.get("ok"):
                    payload["data"]["api_key"] = "REDACTED_COPY_ONCE_API_KEY"
                report["operations"][name] = {"method": method, "path": path, "request": body,
                    "http_status": response.status_code, "response": payload,
                    "provenance": report["provenance"]}
                return actual

            run("health", "GET", "/healthz")
            run("account_session", "POST", "/account/session", {})
            run("account_plans", "GET", "/account/plans")
            created = run("account_create_key", "POST", "/account/keys",
                          {"name": "Research notebook", "scopes": ["companies", "news"], "expires_days": 30})
            key_id, key = created["data"]["id"], created["data"]["api_key"]
            client.headers["X-API-Key"] = key
            run("capabilities", "GET", "/v1/capabilities")
            run("openapi", "GET", "/v1/openapi.json")
            run("account_list_keys", "GET", "/account/keys")
            run("account_link_news", "PUT", "/account/news-key", {"api_key": "REDACTED_NEWS_KEY"})
            run("account_follow", "PUT", "/account/following", {"domain": "microsoft.com"})
            run("account_list_following", "GET", "/account/following")
            run("account_spending", "PUT", "/account/spending", {"monthly_credit_limit": 100})
            run("account_topup", "POST", "/account/topups", {"credits": 100})
            event = {"event": "payment.captured", "payload": {"payment": {"entity": {
                "id": "pay_documentation", "order_id": "order_documentation", "status": "captured",
                "amount": 1000, "currency": "INR"}}}}
            raw = json.dumps(event).encode()
            signature = hmac.new(settings.razorpay_webhook_secret.encode(), raw, hashlib.sha256).hexdigest()
            run("billing_webhook", "POST", "/billing/webhook", content=raw,
                headers={"Content-Type": "application/json", "X-Razorpay-Signature": signature})
            report["operations"]["billing_webhook"]["request"] = event
            run("account_usage", "GET", "/account/usage")
            run("account_unfollow", "DELETE", "/account/following/microsoft.com")
            run("account_revoke_key", "DELETE", "/account/keys/" + key_id)
    path = Path("qa/private/endpoint-accounts.json")
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    fd = os.open(path, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "w") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print(f"Captured {len(report['operations'])} local operations; no live identity or payment calls")


if __name__ == "__main__":
    capture()
