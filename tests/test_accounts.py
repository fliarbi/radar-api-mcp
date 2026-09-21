from __future__ import annotations

import hashlib
import hmac
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from types import SimpleNamespace

import httpx
import pytest
from cryptography.fernet import Fernet
from fastapi.testclient import TestClient
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

from radar_api.accounts import Accounts, NewKey
from radar_api.auth import CURRENT
from radar_api.config import Settings
from radar_api.errors import RadarError
from radar_api.models import Company
from radar_api.server import create_app
from radar_api.service import Service
from radar_api.upstream import Upstream

from conftest import payload_for
from test_mcp import served


@pytest.fixture
def managed(tmp_path):
    state = {"plan": "business", "verified": True, "blocked": False, "identity_failure": False,
             "data_failure": False, "api_feature": True}

    def respond(request):
        if request.url.path == "/auth/me":
            if state["identity_failure"]:
                return httpx.Response(503)
            token = request.headers.get("X-Auth-Token", "")
            if token not in {"session-a", "session-b"}:
                return httpx.Response(401)
            return httpx.Response(200, json={"user": {"_id": token[-1], "email_verified": state["verified"],
                "suspended": state["blocked"]}, "plan": state["plan"], "plan_details": {
                    "features": ["api_access"] if state["api_feature"] else [], "searches_per_month": 5000,
                    "company_tracking": 1000}})
        if state["data_failure"] or request.url.path.startswith("/v1/"):
            return httpx.Response(503)
        return httpx.Response(200, json=payload_for(request.url.path))

    def payment(request):
        assert request.url.host == "api.razorpay.com"
        data = json.loads(request.content)
        return httpx.Response(200, json={"id": "order_test123", "amount": data["amount"], "currency": "INR"})

    settings = Settings(accounts_enabled=True, accounts_db=str(tmp_path / "accounts.db"),
        encryption_key=Fernet.generate_key().decode(), radar_url="http://radar.local",
        allowed_hosts=("testserver", "127.0.0.1", "localhost"), credit_price_paise=10,
        razorpay_key_id="rzp_test_fixture", razorpay_key_secret="test-secret", razorpay_webhook_secret="test-hook")
    transport = httpx.MockTransport(respond)
    accounts = Accounts(settings, transport, httpx.MockTransport(payment))
    app = create_app(settings, Upstream(settings, transport), accounts)
    with TestClient(app) as client:
        yield client, accounts, state, settings


def create(client, token="session-a", **extra):
    r = client.post("/account/keys", headers={"X-Auth-Token": token}, json={"name": "My app", **extra})
    assert r.status_code == 200, r.text
    return r.json()["data"]


def auth(key):
    return {"X-API-Key": key["api_key"]}


def test_issue_reveal_once_encrypt_and_revoke(managed):
    client, accounts, _, _ = managed
    key = create(client)
    listing = client.get("/account/keys", headers={"X-Auth-Token": "session-a"})
    assert key["api_key"] not in listing.text
    assert "hash" not in listing.text and "session-a" not in listing.text
    with accounts.db() as db:
        assert db.execute("SELECT token FROM accounts").fetchone()[0] != "session-a"
        assert db.execute("SELECT hash FROM api_keys").fetchone()[0] == hashlib.sha256(key["api_key"].encode()).hexdigest()
    assert accounts.path.stat().st_mode & 0o077 == 0
    assert client.post("/v1/companies/profile", headers=auth(key), json={"domain": "example.com"}).status_code == 200
    client.delete("/account/keys/" + key["id"], headers={"X-Auth-Token": "session-b"})
    assert client.get("/v1/capabilities", headers=auth(key)).status_code == 200
    client.delete("/account/keys/" + key["id"], headers={"X-Auth-Token": "session-a"})
    assert client.get("/v1/capabilities", headers=auth(key)).status_code == 401


@pytest.mark.parametrize("change,status", [({"verified": False}, 403), ({"blocked": True}, 403), ({"identity_failure": True}, 503)])
def test_account_rechecked_on_every_call(managed, change, status):
    client, _, state, _ = managed
    key = create(client)
    state.update(change)
    assert client.get("/v1/capabilities", headers=auth(key)).status_code == status


def test_management_requires_session_and_static_keys_cannot_bypass(managed):
    client, _, _, _ = managed
    key = create(client)
    assert client.get("/account/keys", headers=auth(key)).status_code == 401
    assert client.post("/account/keys", json={"name": "bad", "account_id": "a"}).status_code == 422
    assert client.get("/v1/capabilities", headers={"X-API-Key": "rdr_" + "1" * 64}).status_code == 401


def test_scopes_partial_refund_and_upstream_error(managed):
    client, accounts, state, _ = managed
    key = create(client, scopes=["companies"])
    assert client.post("/v1/news/search", headers=auth(key), json={"q": "software"}).status_code == 403
    assert client.post("/v1/companies/brief", headers=auth(key), json={"domain": "example.com"}).status_code == 403
    # No linked News key: six successful Radar sections charge six, seventh is refunded.
    full = create(client)
    r = client.post("/v1/companies/brief", headers=auth(full), json={"domain": "example.com"})
    assert r.status_code == 200
    assert r.json()["meta"]["billing"]["credits"] == 6
    state["data_failure"] = True
    assert client.post("/v1/companies/profile", headers=auth(full), json={"domain": "example.com"}).status_code == 502
    with accounts.db() as db:
        assert db.execute("SELECT included FROM usage").fetchone()[0] == 6
        assert db.execute("SELECT COUNT(*) FROM requests WHERE state='pending'").fetchone()[0] == 0


def test_included_usage_shared_across_keys_and_downgrade(managed):
    client, accounts, state, _ = managed
    one, two = create(client), create(client)
    month = datetime.now(timezone.utc).strftime("%Y-%m")
    with accounts.db() as db:
        db.execute("INSERT INTO usage VALUES (?,?,4999,0)", ("a", month))
    assert client.post("/v1/companies/profile", headers=auth(one), json={"domain": "example.com"}).status_code == 200
    assert client.post("/v1/companies/profile", headers=auth(two), json={"domain": "example.com"}).status_code == 402
    with accounts.db() as db:
        db.execute("UPDATE usage SET included=0")
    state["api_feature"] = False
    assert client.post("/v1/companies/profile", headers=auth(two), json={"domain": "example.com"}).status_code == 402
    state["api_feature"], state["plan"] = True, "free"
    assert client.post("/v1/companies/profile", headers=auth(two), json={"domain": "example.com"}).status_code == 402


@pytest.mark.asyncio
async def test_atomic_reservations_across_workers_and_crash_recovery(managed):
    _, accounts, _, settings = managed
    user = await accounts.identity("session-a")
    key = accounts.create_key(user, NewKey(name="Worker"))
    principal = await accounts.authenticate(key["api_key"])
    other = Accounts(settings, accounts.transport)
    def reserve(i):
        try:
            return (accounts if i % 2 else other).reserve(principal, "get_company", "companies", 1)
        except RadarError as e:
            return e.kind
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(reserve, range(8)))
    assert results.count("concurrency_limited") == 5
    with accounts.db() as db:
        assert db.execute("SELECT included FROM usage").fetchone()[0] == 3
        db.execute("UPDATE requests SET created=0")
    rid = other.reserve(principal, "get_company", "companies", 1)
    other.settle(rid, 0)
    with accounts.db() as db:
        assert db.execute("SELECT included FROM usage").fetchone()[0] == 0


@pytest.mark.asyncio
async def test_service_entry_used_by_stdio_is_metered(managed):
    _, accounts, _, settings = managed
    user = await accounts.identity("session-a")
    key = accounts.create_key(user, NewKey(name="MCP"))
    token = CURRENT.set(await accounts.authenticate(key["api_key"]))
    try:
        r = await Service(Upstream(settings, accounts.transport), accounts).run("get_company", Company(domain="example.com"))
        assert r["meta"]["billing"]["credits"] == 1
        assert accounts.usage(user)["included_used_or_reserved"] == 1
    finally:
        CURRENT.reset(token)


def test_payment_amount_signature_replay_spend_and_reversal(managed):
    client, accounts, state, settings = managed
    state["plan"] = "free"
    key = create(client)
    session = {"X-Auth-Token": "session-a"}
    order = client.post("/account/topups", headers=session, json={"credits": 100})
    assert order.status_code == 200
    assert order.json()["data"]["amount"] == 1000
    event = {"event": "payment.captured", "payload": {"payment": {"entity": {
        "id": "pay_test123", "order_id": "order_test123", "status": "captured", "amount": 999, "currency": "INR"}}}}
    def deliver(event, signature=None):
        raw = json.dumps(event).encode()
        sign = hmac.new(settings.razorpay_webhook_secret.encode(), raw, hashlib.sha256).hexdigest()
        return client.post("/billing/webhook", content=raw, headers={"X-Razorpay-Signature": signature or sign})
    assert deliver(event, "bad").status_code == 401
    assert deliver(event).status_code == 400
    event["payload"]["payment"]["entity"]["amount"] = 1000
    assert deliver(event).status_code == 200
    assert deliver(event).status_code == 200
    assert client.get("/account/usage", headers=session).json()["data"]["wallet_credits"] == 100
    assert client.post("/v1/companies/profile", headers=auth(key), json={"domain": "example.com"}).status_code == 402
    client.put("/account/spending", headers=session, json={"monthly_credit_limit": 1})
    assert client.post("/v1/companies/profile", headers=auth(key), json={"domain": "example.com"}).status_code == 200
    assert client.post("/v1/companies/profile", headers=auth(key), json={"domain": "example.com"}).status_code == 402
    assert client.get("/account/usage", headers=session).json()["data"]["wallet_credits"] == 99
    reverse = {"event": "refund.processed", "payload": {"refund": {"entity": {"payment_id": "pay_test123"}}}}
    assert deliver(reverse).status_code == 200
    assert deliver(reverse).status_code == 200
    assert client.get("/v1/capabilities", headers=auth(key)).status_code == 401
    with accounts.db() as db:
        assert db.execute("SELECT wallet,enabled FROM accounts").fetchone()[:] == (0, 0)


def test_following_owned_idempotent_and_plan_limited(managed):
    client, _, state, _ = managed
    a, b = {"X-Auth-Token": "session-a"}, {"X-Auth-Token": "session-b"}
    for _ in range(2):
        assert client.put("/account/following", headers=a, json={"domain": "www.example.com"}).status_code == 200
    assert client.get("/account/following", headers=a).json()["data"]["count"] == 1
    assert client.get("/account/following", headers=b).json()["data"]["count"] == 0
    state["plan"] = "free"
    assert client.put("/account/following", headers=a, json={"domain": "other.com"}).status_code == 402
    assert client.delete("/account/following/example.com", headers=a).status_code == 200


def test_request_size_origins_and_forwarded_ip_do_not_bypass(managed, monkeypatch):
    client, accounts, _, _ = managed
    # Keep quota setup and the HTTP assertion in one minute. A wall-clock rollover
    # used to reset the real bucket mid-test and make this assertion intermittent.
    now = [int(datetime.now(timezone.utc).timestamp()) // 60 * 60 + 10]
    monkeypatch.setattr("radar_api.accounts.time", SimpleNamespace(time=lambda: now[0]))
    assert client.post("/account/keys", content=b"x" * 262145).status_code == 413
    assert client.get("/account/usage", headers={"Origin": "https://evil.example"}).status_code == 403
    for _ in range(60):
        accounts.throttle_account("a")
    assert client.get("/account/usage", headers={"X-Auth-Token": "session-a", "X-Forwarded-For": "1.2.3.4"}).status_code == 429
    now[0] += 60
    assert client.get("/account/usage", headers={"X-Auth-Token": "session-a"}).status_code == 200


def test_checkout_disabled_without_rate(tmp_path):
    settings = Settings(accounts_enabled=True, accounts_db=str(tmp_path / "db"), encryption_key=Fernet.generate_key().decode())
    accounts = Accounts(settings)
    assert accounts.catalog()["credit_price_paise"] is None
    assert not accounts.checkout_enabled()
    with pytest.raises(RadarError) as exc:
        accounts.webhook(b"{}", "")
    assert exc.value.status == 503


def test_detailed_profile_uses_company_scope_and_shared_credit_budget(managed):
    from radar_api.profiles import ProfileStore
    from test_profiles import StoreClient, record
    client, _, _, settings = managed
    client.app.state.service.profiles = ProfileStore(settings, StoreClient([record()]))
    news_only = create(client, scopes=["news"])
    body = {"domain": "example.com", "field": "technology", "item_limit": 100}
    assert client.post("/v1/companies/field", headers=auth(news_only), json=body).status_code == 403
    company_key = create(client, scopes=["companies"])
    result = client.post("/v1/companies/field", headers=auth(company_key), json=body)
    assert result.status_code == 200
    assert result.json()["meta"]["billing"]["credits"] == 1
    assert len(result.json()["data"]["value"]["website_stack"]) == 70
    usage = client.get("/account/usage", headers={"X-Auth-Token": "session-a"}).json()["data"]
    assert usage["included_used_or_reserved"] == 1


@pytest.mark.asyncio
async def test_prepaid_cannot_overdraw_across_workers(managed):
    _, accounts, state, settings = managed
    state["plan"] = "free"
    user = await accounts.identity("session-a")
    key = accounts.create_key(user, NewKey(name="Metered"))
    principal = await accounts.authenticate(key["api_key"])
    with accounts.db() as db:
        db.execute("UPDATE accounts SET wallet=1,spend_limit=1")
    other = Accounts(settings, accounts.transport)
    def reserve(i):
        try:
            return (accounts if i % 2 else other).reserve(principal, "get_company", "companies", 1)
        except RadarError as e:
            return e.kind
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(reserve, range(8)))
    assert results.count("credits_required") == 7
    with accounts.db() as db:
        assert db.execute("SELECT wallet FROM accounts").fetchone()[0] == 0
        assert db.execute("SELECT prepaid FROM usage").fetchone()[0] == 1


@pytest.mark.asyncio
async def test_real_managed_http_mcp_and_rest_share_usage(managed):
    client, accounts, _, settings = managed
    key = create(client)
    client.post("/v1/companies/profile", headers=auth(key), json={"domain": "example.com"})
    with served(create_app(settings, Upstream(settings, accounts.transport), accounts)) as base:
        async with httpx.AsyncClient(headers=auth(key)) as http_client, \
                streamable_http_client(base + "/mcp", http_client=http_client) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                response = await session.call_tool("get_company", {"request": {"domain": "example.com"}})
                assert not response.isError
                assert response.structuredContent["meta"]["billing"]["credits"] == 1
    assert client.get("/account/usage", headers={"X-Auth-Token": "session-a"}).json()["data"]["included_used_or_reserved"] == 2


def test_key_rotation_creation_limit_and_expiry(managed):
    client, accounts, state, _ = managed
    state["plan"] = "free"
    keys = [create(client) for _ in range(3)]
    headers = {"X-Auth-Token": "session-a"}
    assert client.post("/account/keys", headers=headers, json={"name": "extra"}).status_code == 409
    for key in keys:
        client.delete("/account/keys/" + key["id"], headers=headers)
    for _ in range(7):
        key = create(client)
        client.delete("/account/keys/" + key["id"], headers=headers)
    assert client.post("/account/keys", headers=headers, json={"name": "extra"}).status_code == 429
    other = create(client, token="session-b")
    with accounts.db() as db:
        db.execute("UPDATE api_keys SET expires=0 WHERE account='b'")
    assert client.get("/v1/capabilities", headers=auth(other)).status_code == 401


def test_console_shell_contains_no_account_data_and_schema_security(managed):
    client, _, _, _ = managed
    response = client.get("/developer")
    assert response.status_code == 200 and response.headers["x-robots-tag"] == "noindex, nofollow"
    assert "frame-ancestors 'none'" in response.headers["content-security-policy"]
    assert "session-a" not in response.text
    key = create(client)
    schema = client.get("/v1/openapi.json", headers=auth(key)).json()
    assert schema["paths"]["/account/keys"]["post"]["security"] == [{"RadarSession": []}]
    assert schema["paths"]["/billing/webhook"]["post"]["security"] == [{"PaymentSignature": []}]


def test_contact_scope_and_billing_in_account_mode(managed):
    client, accounts, _, _ = managed
    default = create(client)
    assert client.post("/v1/contacts/company", headers=auth(default), json={"domain": "example.com", "fields": ["emails"]}).status_code == 403
    scoped = create(client, scopes=["contacts"])
    response = client.post("/v1/contacts/company", headers=auth(scoped), json={"domain": "example.com", "fields": ["emails"]})
    assert response.status_code == 200 and response.json()["meta"]["billing"]["credits"] == 1
    with accounts.db() as db:
        assert db.execute("SELECT SUM(included+prepaid) FROM requests").fetchone()[0] == 1
        assert db.execute("SELECT scopes FROM api_keys WHERE hash=?", (hashlib.sha256(scoped["api_key"].encode()).hexdigest(),)).fetchone()[0] == '["contacts"]'


def test_contact_account_counter_is_shared_across_workers(managed, monkeypatch):
    _, accounts, _, settings = managed
    monkeypatch.setattr("radar_api.accounts.time.time", lambda: 1800000001)
    other = Accounts(settings, accounts.transport)
    for _ in range(5):
        accounts.rate("contacts:account-a", 10, 60)
        other.rate("contacts:account-a", 10, 60)
    with pytest.raises(RadarError) as exc:
        other.rate("contacts:account-a", 10, 60)
    assert exc.value.status == 429
