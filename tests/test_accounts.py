from __future__ import annotations

import hashlib
import hmac
import json
import os
import re
import secrets
import sqlite3
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from types import SimpleNamespace
from urllib.parse import urlsplit

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


@pytest.fixture(params=["sqlite", "postgres"])
def ledger_url(request):
    """Empty string selects SQLite; postgres runs when RADAR_TEST_POSTGRES_URL names a server."""
    if request.param == "sqlite":
        yield ""
        return
    base = os.getenv("RADAR_TEST_POSTGRES_URL", "")
    if not base:
        pytest.skip("RADAR_TEST_POSTGRES_URL is not set")
    import psycopg
    name = "radar_test_" + secrets.token_hex(6)
    with psycopg.connect(base, autocommit=True) as admin:
        admin.execute(f"CREATE DATABASE {name}")
    try:
        yield urlsplit(base)._replace(path="/" + name).geturl()
    finally:
        with psycopg.connect(base, autocommit=True) as admin:
            admin.execute(f"DROP DATABASE {name} WITH (FORCE)")


@pytest.fixture
def managed(tmp_path, ledger_url):
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
        return httpx.Response(200, json={"id": "order_test123", "amount": data["amount"], "currency": data["currency"]})

    settings = Settings(accounts_enabled=True, accounts_db=str(tmp_path / "accounts.db"),
        accounts_database_url=ledger_url,
        encryption_key=Fernet.generate_key().decode(), radar_url="http://radar.local",
        allowed_hosts=("testserver", "127.0.0.1", "localhost"), credit_price_paise=10, credit_price_cents=2,
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
    if not accounts.database_url:
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
    order = client.post("/account/topups", headers=session, json={"credits": 300})
    assert order.status_code == 200
    assert (order.json()["data"]["amount"], order.json()["data"]["currency"]) == (3000, "INR")
    event = {"event": "payment.captured", "payload": {"payment": {"entity": {
        "id": "pay_test123", "order_id": "order_test123", "status": "captured", "amount": 2999, "currency": "INR"}}}}
    def deliver(event, signature=None):
        raw = json.dumps(event).encode()
        sign = hmac.new(settings.razorpay_webhook_secret.encode(), raw, hashlib.sha256).hexdigest()
        return client.post("/billing/webhook", content=raw, headers={"X-Razorpay-Signature": signature or sign})
    assert deliver(event, "bad").status_code == 401
    assert deliver(event).status_code == 400
    event["payload"]["payment"]["entity"].update(amount=3000, currency="USD")
    assert deliver(event).status_code == 400
    event["payload"]["payment"]["entity"]["currency"] = "INR"
    assert deliver(event).status_code == 200
    assert deliver(event).status_code == 200
    assert client.get("/account/usage", headers=session).json()["data"]["wallet_credits"] == 300
    assert client.post("/v1/companies/profile", headers=auth(key), json={"domain": "example.com"}).status_code == 402
    client.put("/account/spending", headers=session, json={"monthly_credit_limit": 1})
    assert client.post("/v1/companies/profile", headers=auth(key), json={"domain": "example.com"}).status_code == 200
    assert client.post("/v1/companies/profile", headers=auth(key), json={"domain": "example.com"}).status_code == 402
    assert client.get("/account/usage", headers=session).json()["data"]["wallet_credits"] == 299
    reverse = {"event": "refund.processed", "payload": {"refund": {"entity": {"payment_id": "pay_test123"}}}}
    assert deliver(reverse).status_code == 200
    assert deliver(reverse).status_code == 200
    assert client.get("/v1/capabilities", headers=auth(key)).status_code == 401
    with accounts.db() as db:
        assert db.execute("SELECT wallet,enabled FROM accounts").fetchone()[:] == (0, 0)


def test_topup_minimum_is_five_dollars_in_every_currency(managed):
    client, accounts, _, _ = managed
    session = {"X-Auth-Token": "session-a"}
    plans = client.get("/account/plans", headers=session).json()["data"]
    # 500 cents at 2 cents per credit: 250 credits, whichever currency pays for them.
    assert (plans["min_topup_credits"], plans["checkout_currencies"]) == (250, ["INR", "USD"])
    assert plans["credit_prices_minor"] == {"USD": 2, "INR": 10}
    for currency in ("USD", "INR"):
        r = client.post("/account/topups", headers=session, json={"credits": 249, "currency": currency})
        assert r.status_code == 422 and "US$5.00" in r.text
    usd = client.post("/account/topups", headers=session, json={"credits": 250, "currency": "USD"}).json()["data"]
    assert (usd["amount"], usd["currency"]) == (500, "USD")
    assert client.post("/account/topups", headers=session, json={"credits": 250, "currency": "EUR"}).status_code == 422
    with accounts.db() as db:
        assert db.execute("SELECT amount,currency FROM orders").fetchone()[:] == (500, "USD")
    event = {"event": "payment.captured", "payload": {"payment": {"entity": {
        "id": "pay_usd1", "order_id": "order_test123", "status": "captured", "amount": 500, "currency": "INR"}}}}
    def deliver():
        raw = json.dumps(event).encode()
        sign = hmac.new(b"test-hook", raw, hashlib.sha256).hexdigest()
        return client.post("/billing/webhook", content=raw, headers={"X-Razorpay-Signature": sign}).status_code
    assert deliver() == 400  # 500 paise is not 500 cents
    event["payload"]["payment"]["entity"]["currency"] = "USD"
    assert deliver() == 200
    assert client.get("/account/usage", headers=session).json()["data"]["wallet_credits"] == 250


def test_checkout_needs_usd_rate_and_old_ledgers_gain_currency(tmp_path):
    key = Fernet.generate_key().decode()
    path = tmp_path / "old.db"
    db = sqlite3.connect(path)
    db.execute("CREATE TABLE orders (id TEXT PRIMARY KEY, account TEXT NOT NULL, credits INTEGER NOT NULL, "
               "amount INTEGER NOT NULL, payment TEXT UNIQUE, credited INTEGER NOT NULL DEFAULT 0, reversed INTEGER NOT NULL DEFAULT 0)")
    db.execute("INSERT INTO orders(id,account,credits,amount) VALUES ('order_old','a',100,10000)")
    db.commit()
    db.close()
    path.chmod(0o600)
    accounts = Accounts(Settings(accounts_enabled=True, accounts_db=str(path), encryption_key=key, credit_price_paise=100,
                                 razorpay_key_id="rzp_test_x", razorpay_key_secret="s", razorpay_webhook_secret="h"))
    assert not accounts.checkout_enabled() and accounts.catalog()["checkout_currencies"] == []
    with accounts.db() as db:
        assert db.execute("SELECT currency FROM orders").fetchone()[0] == "INR"


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
@pytest.mark.parametrize('root_path', ['', '/radar-api'])
async def test_real_managed_http_mcp_and_rest_share_usage(managed, root_path):
    client, accounts, _, settings = managed
    key = create(client)
    client.post("/v1/companies/profile", headers=auth(key), json={"domain": "example.com"})
    # The reverse proxy strips the public prefix; Uvicorn restores it in ASGI scope.
    with served(create_app(settings, Upstream(settings, accounts.transport), accounts), root_path=root_path) as base:
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


@pytest.mark.parametrize('prefix', ['', '/radar-api', '/private/radar-api'])
def test_dashboard_console_mount_preserves_account_auth_and_assets(managed, prefix):
    client, _, _, _ = managed
    mounted = TestClient(client.app, root_path=prefix)
    page = mounted.get(prefix + '/developer')
    assert page.status_code == 200
    assert re.search(f'src="{prefix}/developer/console.js\\?v=[0-9a-f]{{12}}"', page.text)
    assert re.search(f'href="{prefix}/developer/console.css\\?v=[0-9a-f]{{12}}"', page.text)
    assert mounted.get(prefix + '/developer/console.js').status_code == 200
    # A prefix must not weaken the session or data-key gates.
    assert mounted.get(prefix + '/account/keys').status_code == 401
    assert mounted.post(prefix + '/v1/companies/profile', json={'domain': 'example.com'}).status_code == 401
    key = mounted.post(prefix + '/account/keys', headers={'X-Auth-Token': 'session-a'},
                       json={'name': 'Dashboard mount check', 'scopes': ['companies']})
    assert key.status_code == 200
    data = key.json()['data']
    listed = mounted.get(prefix + '/account/keys', headers={'X-Auth-Token': 'session-a'})
    assert listed.status_code == 200 and data['api_key'] not in listed.text
    assert mounted.get(prefix + '/account/keys', headers={'X-API-Key': data['api_key']}).status_code == 401
    assert mounted.delete(prefix + '/account/keys/' + data['id'],
                          headers={'X-Auth-Token': 'session-a'}).status_code == 200


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


@pytest.mark.parametrize("peer,forwarded,trusted,expected", [
    ("9.9.9.9", "1.1.1.1", (), "9.9.9.9"),                                   # no proxy configured
    ("9.9.9.9", "1.1.1.1", ("10.0.0.0/8",), "9.9.9.9"),                      # untrusted peer cannot spoof
    ("10.0.0.5", "1.1.1.1", ("10.0.0.0/8",), "1.1.1.1"),                     # one trusted proxy
    ("10.0.0.5", "6.6.6.6, 1.1.1.1, 10.0.0.9", ("10.0.0.0/8",), "1.1.1.1"),  # client-prepended hops ignored
    ("10.0.0.5", "1.1.1.1, not-an-ip", ("10.0.0.0/8",), "10.0.0.5"),         # malformed hop stops the walk
    ("10.0.0.5", "", ("10.0.0.0/8",), "10.0.0.5"),
])
def test_client_ip_trusts_only_configured_proxies(peer, forwarded, trusted, expected):
    from radar_api.auth import client_ip
    assert client_ip(peer, forwarded, trusted) == expected


def test_trusted_proxy_setting_is_validated():
    with pytest.raises(ValueError):
        Settings(trusted_proxies=("not-a-network",))
    with pytest.raises(ValueError):
        Settings(accounts_database_url="mysql://example/db")


async def test_new_accounts_are_limited_per_address_and_overall(managed):
    from dataclasses import replace
    _, accounts, _, settings = managed
    strict = Accounts(replace(settings, new_accounts_per_ip_day=1, new_accounts_per_hour=2), accounts.transport)
    await strict.identity("session-a", "203.0.113.7")
    await strict.identity("session-a", "203.0.113.7")  # an existing account is not a new signup
    with pytest.raises(RadarError) as exc:
        await strict.identity("session-b", "203.0.113.7")
    assert exc.value.status == 429
    await strict.identity("session-b", "198.51.100.4")
    with accounts.db() as db:
        assert db.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 2
    # Key-authenticated calls (peer=None) never count as signups.
    await strict.identity("session-b", None)


def test_revoking_an_unknown_key_is_not_reported_as_success(managed):
    client, _, _, _ = managed
    create(client)
    response = client.delete("/account/keys/does-not-exist", headers={"X-Auth-Token": "session-a"})
    assert response.status_code == 404


def _introspect_client(managed, secret="s" * 40, peers=("testclient",)):
    from dataclasses import replace
    client, accounts, state, settings = managed
    accounts.settings = replace(settings, introspect_secret=secret, introspect_peers=("127.0.0.1",)) if secret else settings
    # TestClient's socket peer is "testclient"; allow it the way an operator allows a local address.
    object.__setattr__(accounts.settings, "introspect_peers", peers)
    return client, accounts, state


def test_introspection_confirms_keys_for_sibling_apis(managed):
    client, accounts, state = _introspect_client(managed)
    key = create(client, scopes=["news"])
    h = {"X-Introspect-Secret": "s" * 40}
    r = client.post("/internal/keys/introspect", headers=h, json={"api_key": key["api_key"]})
    assert r.status_code == 200, r.text
    data = r.json()["data"]
    assert data["active"] and data["account_id"] == "a" and data["scopes"] == ["news"] and data["last4"] == key["api_key"][-4:]
    assert key["api_key"] not in r.text
    state["blocked"] = True
    assert client.post("/internal/keys/introspect", headers=h, json={"api_key": key["api_key"]}).json()["data"] == {"active": False, "reason": "account_unavailable"}
    state["blocked"] = False
    client.delete("/account/keys/" + key["id"], headers={"X-Auth-Token": "session-a"})
    assert client.post("/internal/keys/introspect", headers=h, json={"api_key": key["api_key"]}).json()["data"]["active"] is False
    fresh = create(client)
    state["identity_failure"] = True
    assert client.post("/internal/keys/introspect", headers=h, json={"api_key": fresh["api_key"]}).status_code == 503


@pytest.mark.parametrize("secret,peers,header", [("", ("testclient",), "s" * 40), ("s" * 40, ("127.0.0.1",), "s" * 40),
                                                 ("s" * 40, ("testclient",), "wrong"), ("s" * 40, ("testclient",), "")])
def test_introspection_is_hidden_without_secret_and_local_peer(managed, secret, peers, header):
    client, _, _ = _introspect_client(managed, secret, peers)
    key = create(client)
    r = client.post("/internal/keys/introspect", headers={"X-Introspect-Secret": header}, json={"api_key": key["api_key"]})
    assert r.status_code == 404
    assert "/internal/keys/introspect" not in client.get("/v1/openapi.json", headers=auth(key)).text


def test_own_key_is_used_for_news_when_no_news_key_is_linked(managed):
    client, accounts, _, _ = managed
    key = create(client)
    import asyncio
    user = asyncio.run(accounts.authenticate(key["api_key"]))
    assert user.news_key == key["api_key"]


def _wallet(accounts, account="a"):
    with accounts.db() as db:
        return db.execute("SELECT wallet FROM accounts WHERE id=?", (account,)).fetchone()[0]


def _fund(client, accounts, credits=1000, limit=1000):
    client.put("/account/spending", headers={"X-Auth-Token": "session-a"}, json={"monthly_credit_limit": limit})
    with accounts.db() as db:
        db.execute("UPDATE accounts SET wallet=? WHERE id='a'", (credits,))


def test_checkout_verification_credits_once_and_captures_authorized_payments(managed):
    client, accounts, _, settings = managed
    create(client)
    order = client.post("/account/topups", headers={"X-Auth-Token": "session-a"}, json={"credits": 600, "currency": "INR"}).json()["data"]
    state = {"status": "authorized", "captured": 0}

    def payments(request):
        if request.url.path == "/v1/orders":
            return httpx.Response(200, json={"id": order["order_id"], "amount": order["amount"], "currency": "INR"})
        if request.url.path.endswith("/capture"):
            state["status"], state["captured"] = "captured", state["captured"] + 1
        return httpx.Response(200, json={"id": "pay_ok1", "order_id": order["order_id"], "amount": order["amount"],
                                         "currency": "INR", "status": state["status"]})

    accounts.payment_transport = httpx.MockTransport(payments)
    sig = hmac.new(settings.razorpay_key_secret.encode(), f"{order['order_id']}|pay_ok1".encode(), hashlib.sha256).hexdigest()
    body = {"razorpay_order_id": order["order_id"], "razorpay_payment_id": "pay_ok1", "razorpay_signature": sig}
    forged = {**body, "razorpay_signature": "0" * 64}
    assert client.post("/account/topups/verify", headers={"X-Auth-Token": "session-a"}, json=forged).status_code == 401
    assert client.post("/account/topups/verify", headers={"X-Auth-Token": "session-b"}, json=body).status_code == 404
    r = client.post("/account/topups/verify", headers={"X-Auth-Token": "session-a"}, json=body)
    assert r.status_code == 200 and r.json()["data"] == {"credited": True, "credits": 600}
    assert state["captured"] == 1 and _wallet(accounts) == 600
    client.post("/account/topups/verify", headers={"X-Auth-Token": "session-a"}, json=body)
    assert _wallet(accounts) == 600  # idempotent


def test_news_pay_as_you_go_reserves_within_wallet_and_limit_and_refunds_unsettled(managed):
    client, accounts, _, _ = managed
    client2, *_ = _introspect_client(managed)
    create(client)
    h = {"X-Introspect-Secret": "s" * 40}
    def reserve(units):
        return client.post("/internal/credits/reserve", headers=h, json={"account_id": "a", "feature": "news:/v1/headlines", "units": units})
    assert reserve(1).status_code == 402  # no credits yet
    _fund(client, accounts, credits=10, limit=5)
    rid = reserve(3).json()["data"]["request_id"]
    assert _wallet(accounts) == 7
    assert reserve(3).status_code == 402  # monthly prepaid limit 5
    client.post("/internal/credits/settle", headers=h, json={"request_id": rid, "actual": 2})
    assert _wallet(accounts) == 8
    usage = client.get("/account/usage", headers={"X-Auth-Token": "session-a"}).json()["data"]
    assert {"feature": "news:/v1/headlines", "credits": 2, "completed_requests": 1} in usage["features"]
    rid2 = reserve(1).json()["data"]["request_id"]
    with accounts.db() as db:
        db.execute("UPDATE requests SET created=created-700 WHERE id=?", (rid2,))
    reserve(1)  # triggers the stale refund of rid2
    assert _wallet(accounts) == 7
    assert client.post("/internal/credits/reserve", json={"account_id": "a", "feature": "x", "units": 1}).status_code == 404


def test_usage_levels_lift_limits_after_credit_usage(managed):
    from radar_api.accounts import level_for
    client, accounts, _, _ = managed
    create(client)
    assert level_for(0)["level"] == 1 and level_for(10000)["name"] == "Growth" and level_for(10**6)["level"] == 4
    assert accounts.level("a")["level"] == 1 and accounts.level("a")["next_level"]["credits_to_go"] == 10000
    with accounts.db() as db:
        db.execute("INSERT INTO requests VALUES ('old1','a','2026-01','x',0,12000,'settled',0)")
    lv = accounts.level("a")
    assert lv["level"] == 2 and lv["concurrent_requests"] == 5 and lv["rate_per_minute"] == 120
    usage = client.get("/account/usage", headers={"X-Auth-Token": "session-a"}).json()["data"]
    assert usage["level"]["name"] == "Growth"
    assert client.get("/account/plans", headers={"X-Auth-Token": "session-a"}).json()["data"]["levels"][0]["name"] == "Starter"


def test_daily_prepaid_cap_follows_the_level(managed):
    client, accounts, _, _ = managed
    _introspect_client(managed)
    create(client)
    _fund(client, accounts, credits=10000, limit=10000)
    h = {"X-Introspect-Secret": "s" * 40}
    def reserve(units):
        return client.post("/internal/credits/reserve", headers=h, json={"account_id": "a", "feature": "news:/v1/export", "units": units})
    assert reserve(1000).status_code == 200
    with accounts.db() as db:
        db.execute("UPDATE requests SET prepaid=4500 WHERE account='a'")  # 4,500 used today at Starter (5,000/day)
    r = reserve(600)
    assert r.status_code == 429 and r.json()["error"]["kind"] == "daily_limit"


def test_included_credits_work_after_the_prepaid_limit_is_lowered(managed):
    client, accounts, _, _ = managed
    key = create(client)
    with accounts.db() as db:
        month = datetime.now(timezone.utc).strftime("%Y-%m")
        db.execute("INSERT OR IGNORE INTO usage(account,month) VALUES ('a',?)", (month,))
        db.execute("UPDATE usage SET prepaid=5 WHERE account='a'")   # spent 5 prepaid, limit now 0
    assert client.post("/v1/companies/profile", headers=auth(key), json={"domain": "example.com"}).status_code == 200
