"""Fair use: a free monthly allowance (with a daily cap) for every verified account, and the
OAuth discovery a chat connector needs to reach /mcp. Companies Radar identity is mocked: session-a is
account "a" on the free plan."""
from __future__ import annotations

import httpx
import pytest
from cryptography.fernet import Fernet
from fastapi.testclient import TestClient

from radar_api.accounts import Accounts
from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.upstream import Upstream

from conftest import payload_for

DEV = "https://example.test/keys"


def _app(tmp_path, **extra):
    state = {"plan": "free"}

    def respond(request):
        if request.url.path == "/auth/me":
            token = request.headers.get("X-Auth-Token", "")
            if token not in {"session-a", "session-b"}:
                return httpx.Response(401)
            business = state["plan"] == "business"
            return httpx.Response(200, json={"user": {"_id": token[-1], "email_verified": True}, "plan": state["plan"],
                "plan_details": {"features": ["api_access"] if business else [], "searches_per_month": 5000 if business else 50,
                                 "company_tracking": 0}})
        return httpx.Response(200, json=payload_for(request.url.path))

    settings = Settings(**{**dict(accounts_enabled=True, accounts_db=str(tmp_path / "accounts.db"),
        encryption_key=Fernet.generate_key().decode(), radar_url="http://radar.local",
        allowed_hosts=("testserver", "127.0.0.1", "localhost"), credit_price_cents=1,
        razorpay_key_id="rzp_test_fixture", razorpay_key_secret="s", razorpay_webhook_secret="h",
        free_monthly_credits=10, free_daily_credits=4, public_developer_url=DEV), **extra})
    transport = httpx.MockTransport(respond)
    accounts = Accounts(settings, transport)
    return create_app(settings, Upstream(settings, transport), accounts), accounts, state


@pytest.fixture
def free(tmp_path):
    app, accounts, state = _app(tmp_path)
    with TestClient(app) as client:
        yield client, accounts, state


def key(client, token="session-a"):
    r = client.post("/account/keys", headers={"X-Auth-Token": token}, json={"name": "chat"})
    assert r.status_code == 200, r.text
    return {"X-API-Key": r.json()["data"]["api_key"]}


def call(client, headers):
    return client.post("/v1/companies/funding", headers=headers, json={"domain": "example.com"})


def test_free_plan_calls_work_without_paying_until_the_daily_cap(free):
    client, accounts, _ = free
    h = key(client)
    for used in range(1, 5):
        r = call(client, h)
        assert r.status_code == 200, r.text
        assert r.json()["meta"]["billing"]["free_credits_left_this_month"] == 10 - used
    r = call(client, h)
    assert r.status_code == 429 and r.json()["error"]["kind"] == "free_daily_limit"
    assert DEV in r.json()["error"]["message"] and int(r.headers["retry-after"]) <= 86400
    with accounts.db() as db:  # Nothing was charged and no wallet exists.
        assert db.execute("SELECT wallet FROM accounts WHERE id='a'").fetchone()[0] == 0
    usage = client.get("/account/usage", headers={"X-Auth-Token": "session-a"}).json()["data"]
    assert usage["free_allowance"] == {"monthly_credits": 10, "daily_credits": 4, "left_this_month": 6, "left_today": 0}


def test_monthly_allowance_ends_with_a_top_up_message_and_low_balance_note(tmp_path):
    app, accounts, _ = _app(tmp_path, free_daily_credits=0)
    with TestClient(app) as client:
        h = key(client)
        notes = [call(client, h).json()["meta"]["notes"] for _ in range(10)]
        # Quiet until the last fifth of the allowance, then one line saying what is left.
        assert not any("free credits left" in n for row in notes[:7] for n in row)
        assert any("2 of 10 free credits left" in n and DEV in n for n in notes[7])
        r = call(client, h)
        assert r.status_code == 402 and r.json()["error"]["kind"] == "credits_required"
        assert "Free monthly allowance (10 credits) used" in r.json()["error"]["message"] and DEV in r.json()["error"]["message"]


def test_prepaid_credits_take_over_after_the_free_allowance(free):
    client, accounts, _ = free
    h = key(client)
    with accounts.db() as db:
        db.execute("UPDATE accounts SET wallet=5,spend_limit=5 WHERE id='a'")
    for _ in range(6):
        assert call(client, h).status_code == 200
    with accounts.db() as db:  # Four free today, then two from the wallet.
        assert db.execute("SELECT wallet FROM accounts WHERE id='a'").fetchone()[0] == 3


def test_failed_calls_do_not_use_the_allowance_and_accounts_are_separate(free):
    client, accounts, _ = free
    h = key(client)
    assert client.post("/v1/companies/funding", headers=h, json={}).status_code == 422
    assert accounts.free_allowance("a")["left_this_month"] == 10
    assert call(client, h).status_code == 200
    assert call(client, key(client, "session-b")).json()["meta"]["billing"]["free_credits_left_this_month"] == 9


def test_business_allowance_is_unchanged_and_off_by_default(tmp_path):
    app, accounts, state = _app(tmp_path)
    state["plan"] = "business"
    with TestClient(app) as client:
        h = key(client)
        for _ in range(6):  # No free daily cap on a paid allowance.
            r = call(client, h)
            assert r.status_code == 200 and "free_credits_left_this_month" not in r.json()["meta"]["billing"]
    (tmp_path / "off").mkdir()
    app, _, _ = _app(tmp_path / "off", free_monthly_credits=0, free_daily_credits=0)
    with TestClient(app) as client:
        assert call(client, key(client)).status_code == 402


def test_free_settings_are_validated():
    with pytest.raises(ValueError):
        Settings(free_monthly_credits=5, free_daily_credits=6)


def test_connector_discovery_from_the_mcp_url(tmp_path):
    app, _, _ = _app(tmp_path, oauth_issuer="https://127.0.0.1/gw", public_url="https://api.example.test",
                     oauth_authorize_url="https://dash.example.test/gw/oauth/authorize")
    with TestClient(app) as client:
        r = client.post("/mcp", json={"jsonrpc": "2.0", "id": 1, "method": "tools/list"})
        assert r.status_code == 401
        assert r.headers["www-authenticate"] == 'Bearer resource_metadata="https://api.example.test/.well-known/oauth-protected-resource/mcp"'
        for path in ("/.well-known/oauth-protected-resource", "/.well-known/oauth-protected-resource/mcp"):
            r = client.get(path, headers={"Origin": "https://chatgpt.com"})
            assert r.status_code == 200 and r.headers["access-control-allow-origin"] == "*"
            assert r.json()["resource"] == "https://api.example.test/mcp"
            assert r.json()["authorization_servers"] == ["https://127.0.0.1/gw"]
        docs = [client.get(p).json() for p in (
            "/.well-known/oauth-authorization-server", "/.well-known/oauth-authorization-server/gw",
            "/.well-known/openid-configuration", "/.well-known/openid-configuration/gw")]
        assert all(d == docs[0] for d in docs)
        assert docs[0]["authorization_endpoint"] == "https://dash.example.test/gw/oauth/authorize"
        assert docs[0]["token_endpoint"] == "https://127.0.0.1/gw/oauth/token"


def test_no_resource_pointer_without_oauth(free):
    client, _, _ = free
    r = client.post("/mcp", json={})
    assert r.status_code == 401 and r.headers["www-authenticate"] == "Bearer"
    assert client.get("/.well-known/oauth-protected-resource").status_code == 404


def test_every_mcp_tool_has_a_title_and_read_only_annotation(free):
    import asyncio
    client, _, _ = free
    tools = asyncio.run(client.app.state.mcp.list_tools())
    assert len(tools) == 53
    assert all(t.title and t.annotations.title == t.title and t.annotations.readOnlyHint for t in tools)
    assert next(t for t in tools if t.name == "get_company_funding").title == "Get company funding"


def _rpc(client, headers, method, params=None):
    r = client.post("/mcp", headers={**headers, "Accept": "application/json, text/event-stream"},
                    json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}})
    assert r.status_code == 200, r.text
    return r.json()["result"]


def test_chat_connectors_list_core_tools_and_can_still_call_the_rest(free):
    from radar_api.server import CHAT_TOOLS
    client, accounts, _ = free
    assert len(_rpc(client, key(client), "tools/list")["tools"]) == 53
    api_key, _, _ = accounts.issue_connector_key("a", "Connector rdrc_" + "0" * 32, ("*",), 30)
    chat = {"Authorization": "Bearer " + api_key}
    listed = _rpc(client, chat, "tools/list")["tools"]
    assert {t["name"] for t in listed} == set(CHAT_TOOLS) and len(listed) == 25
    # Advertised schemas are shortened; the request is still validated in full.
    assert "title" not in str(next(t for t in listed if t["name"] == "search_companies")["inputSchema"])
    hidden = _rpc(client, chat, "tools/call", {"name": "investor_directory", "arguments": {"request": {}}})
    assert hidden["structuredContent"]["ok"] is True
    bad = _rpc(client, chat, "tools/call", {"name": "get_company_funding", "arguments": {"request": {"domain": "x" * 500}}})
    assert bad["isError"] is True


def test_landing_docs_and_schema_are_public_but_data_is_not(tmp_path):
    app, _, _ = _app(tmp_path, public_url="https://api.example.test", public_privacy_url="https://example.test/privacy",
                     public_terms_url="https://example.test/terms", oauth_issuer="https://127.0.0.1")
    with TestClient(app) as client:
        page = client.get("/")
        assert page.status_code == 200 and "https://api.example.test/mcp" in page.text
        assert "10 lookups a month, up to 4 a day" in page.text and "https://example.test/privacy" in page.text
        assert "__" not in page.text and "frame-ancestors 'none'" in page.headers["content-security-policy"]
        assert client.get("/docs").status_code == 200
        assert client.get("/v1/openapi.json").json()["info"]["title"] == "Companies Radar API"
        assert client.post("/").status_code == 401 and client.get("/v1/capabilities").status_code == 401
        assert client.get("/.well-known/oauth-protected-resource").json()["resource_policy_uri"] == "https://example.test/privacy"
        assert client.get("/.well-known/oauth-authorization-server").json()["op_tos_uri"] == "https://example.test/terms"


def test_used_up_plan_search_allowance_is_not_reported_as_a_rate_limit(tmp_path):
    import asyncio
    from radar_api.auth import CURRENT, Principal
    from radar_api.errors import RadarError
    settings = Settings(radar_url="http://radar.local")
    upstream = Upstream(settings, httpx.MockTransport(lambda request: httpx.Response(429, json={"error": "quota_exceeded", "plan": "free"})))
    token = CURRENT.set(Principal("k", "n", "t"))
    try:
        with pytest.raises(RadarError) as caught:
            asyncio.run(upstream.call("radar", "/company_search/", body={}))
    finally:
        CURRENT.reset(token)
    assert caught.value.kind == "quota_exceeded" and caught.value.status == 402 and caught.value.retry_after is None


def test_a_key_about_to_expire_says_so(free):
    client, accounts, _ = free
    r = client.post("/account/keys", headers={"X-Auth-Token": "session-a"}, json={"name": "short", "expires_days": 3})
    notes = call(client, {"X-API-Key": r.json()["data"]["api_key"]}).json()["meta"]["notes"]
    assert any("expires in 3 day(s)" in n and DEV in n for n in notes)
    assert not any("expires in" in n for n in call(client, key(client, "session-b")).json()["meta"]["notes"])
