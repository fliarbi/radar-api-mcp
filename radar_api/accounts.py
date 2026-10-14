"""Opt-in account gateway. SQLite transactions are shared by workers on one host;
a PostgreSQL ledger is shared by workers on many hosts.

No production identity database is modified. Radar remains the identity and plan
authority; the API ledger only grants usage, never additional data entitlements.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import re
import secrets
import sqlite3
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import httpx
from cryptography.fernet import Fernet, InvalidToken
from fastapi import Request
from pydantic import Field

from .auth import Principal
from .errors import RadarError, envelope
from .models import Company, Input, Text

# Snapshot of Radar's existing catalog, verified 2026-09-20. No provider plan IDs.
PLANS = {
    "free": {"monthly_inr": 0, "monthly_usd": 0, "searches": 50, "following": 0, "api_access": False},
    "pro": {"monthly_inr": 1600, "monthly_usd": 19, "searches": 1000, "following": 100, "api_access": False},
    "business": {"monthly_inr": 5000, "monthly_usd": 60, "searches": 5000, "following": 1000, "api_access": True},
    "marketai_bundled": {"monthly_inr": 0, "monthly_usd": 0, "searches": 100, "following": 0, "api_access": False},
}
GROUPS = {"companies", "investors", "markets", "locations", "industries", "jobs", "people", "news", "contacts", "apps"}


@dataclass(frozen=True)
class Identity:
    id: str
    plan: str
    token: str = field(repr=False)
    included: int = 0
    following: int = 0


class NewKey(Input):
    name: Text
    scopes: list[str] = Field(default_factory=lambda: ["*"], min_length=1, max_length=11, description="Data groups; contact retrieval requires explicit contacts even alongside *")
    expires_days: int = Field(30, ge=1, le=90)


class LinkNews(Input):
    api_key: str = Field(min_length=1, max_length=512, repr=False)


class Spending(Input):
    monthly_credit_limit: int = Field(0, ge=0, le=1000000, strict=True)


class TopUp(Input):
    credits: int = Field(1000, ge=100, le=100000, strict=True)


class _Row(dict):
    """Rows readable by column name or position, like sqlite3.Row."""

    def __getitem__(self, key):
        return tuple(self.values())[key] if isinstance(key, (int, slice)) else super().__getitem__(key)


class _Postgres:
    """Runs the ledger's SQLite dialect on PostgreSQL inside one serialized transaction.

    One advisory transaction lock gives the same all-writers ordering as SQLite's
    BEGIN IMMEDIATE, so quotas, reservations and wallets stay exact across hosts.
    """
    LOCK = 7_221_034

    def __init__(self, conn):
        self.conn = conn

    @property
    def in_transaction(self):
        from psycopg.pq import TransactionStatus
        return self.conn.info.transaction_status != TransactionStatus.IDLE

    @staticmethod
    def _sql(sql):
        if sql.startswith("INSERT OR IGNORE"):
            sql = "INSERT" + sql[len("INSERT OR IGNORE"):] + " ON CONFLICT DO NOTHING"
        return sql.replace("MAX(0,", "GREATEST(0,").replace("?", "%s")

    def execute(self, sql, params=()):
        return self.conn.execute(self._sql(sql), params)

    def executescript(self, script):
        self.conn.execute(script.replace("INTEGER", "BIGINT"))


def _rows(cursor):
    names = [column.name for column in cursor.description or ()]
    return lambda values: _Row(zip(names, values))


class Accounts:
    def __init__(self, settings, transport=None, payment_transport=None):
        self.settings, self.transport, self.payment_transport = settings, transport, payment_transport
        self.cipher = Fernet(settings.encryption_key.encode())
        self.database_url = settings.accounts_database_url
        if self.database_url:
            self._create_schema()
            return
        self.path = Path(settings.accounts_db)
        self.path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        if self.path.is_symlink():
            raise ValueError("Account database must not be a symlink")
        try:
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            pass  # Another worker may have initialized it concurrently.
        else:
            os.close(fd)
        info = self.path.lstat()
        if self.path.is_symlink() or info.st_uid != os.getuid() or info.st_mode & 0o077:
            raise ValueError("Account database must be owner-only and not a symlink")
        self._create_schema()

    def _create_schema(self):
        with self.db() as db:
            db.executescript("""
            CREATE TABLE IF NOT EXISTS accounts (
              id TEXT PRIMARY KEY, token TEXT NOT NULL, news TEXT NOT NULL DEFAULT '',
              plan TEXT NOT NULL, wallet INTEGER NOT NULL DEFAULT 0 CHECK(wallet>=0),
              spend_limit INTEGER NOT NULL DEFAULT 0, enabled INTEGER NOT NULL DEFAULT 1,
              included_limit INTEGER NOT NULL DEFAULT 0);
            CREATE TABLE IF NOT EXISTS api_keys (
              id TEXT PRIMARY KEY, account TEXT NOT NULL, hash TEXT UNIQUE NOT NULL,
              name TEXT NOT NULL, last4 TEXT NOT NULL, scopes TEXT NOT NULL,
              created INTEGER NOT NULL, expires INTEGER NOT NULL, revoked INTEGER NOT NULL DEFAULT 0);
            CREATE INDEX IF NOT EXISTS keys_account ON api_keys(account);
            CREATE TABLE IF NOT EXISTS usage (
              account TEXT NOT NULL, month TEXT NOT NULL, included INTEGER NOT NULL DEFAULT 0,
              prepaid INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(account,month));
            CREATE TABLE IF NOT EXISTS requests (
              id TEXT PRIMARY KEY, account TEXT NOT NULL, month TEXT NOT NULL, feature TEXT NOT NULL,
              included INTEGER NOT NULL, prepaid INTEGER NOT NULL, state TEXT NOT NULL, created INTEGER NOT NULL);
            CREATE INDEX IF NOT EXISTS requests_account ON requests(account,state);
            CREATE TABLE IF NOT EXISTS counters (
              key TEXT PRIMARY KEY, count INTEGER NOT NULL, expires INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS follows (
              account TEXT NOT NULL, domain TEXT NOT NULL, created INTEGER NOT NULL, PRIMARY KEY(account,domain));
            CREATE TABLE IF NOT EXISTS orders (
              id TEXT PRIMARY KEY, account TEXT NOT NULL, credits INTEGER NOT NULL, amount INTEGER NOT NULL,
              payment TEXT UNIQUE, credited INTEGER NOT NULL DEFAULT 0, reversed INTEGER NOT NULL DEFAULT 0);
            """)

    @contextmanager
    def db(self):
        if self.database_url:
            with self._postgres() as db:
                yield db
            return
        db = None
        try:
            db = sqlite3.connect(self.path, timeout=5, isolation_level=None)
            db.row_factory = sqlite3.Row
            db.execute("PRAGMA journal_mode=WAL")
            db.execute("BEGIN IMMEDIATE")
            yield db
            if db.in_transaction:
                db.execute("COMMIT")
        except sqlite3.Error:
            if db and db.in_transaction:
                db.execute("ROLLBACK")
            raise RadarError("account_store_unavailable", "Account usage storage is unavailable", 503) from None
        except BaseException:
            if db and db.in_transaction:
                db.execute("ROLLBACK")
            raise
        finally:
            if db:
                db.close()

    @contextmanager
    def _postgres(self):
        import psycopg
        conn = None
        try:
            conn = psycopg.connect(self.database_url, connect_timeout=5, row_factory=_rows,
                                   options="-c statement_timeout=5000 -c lock_timeout=5000")
            db = _Postgres(conn)
            conn.execute("SELECT pg_advisory_xact_lock(%s)", (_Postgres.LOCK,))
            yield db
            conn.commit()
        except psycopg.Error:
            if conn:
                conn.rollback()
            raise RadarError("account_store_unavailable", "Account usage storage is unavailable", 503) from None
        except BaseException:
            if conn:
                conn.rollback()
            raise
        finally:
            if conn:
                conn.close()

    def rate(self, key, limit, seconds):
        now = int(time.time())
        bucket = f"{key}:{now // seconds}"
        with self.db() as db:
            db.execute("DELETE FROM counters WHERE expires<=?", (now,))
            row = db.execute("SELECT count FROM counters WHERE key=?", (bucket,)).fetchone()
            if row and row[0] >= limit:
                raise RadarError("rate_limited", "Request limit reached", 429, seconds - now % seconds)
            db.execute("INSERT INTO counters VALUES (?,1,?) ON CONFLICT(key) DO UPDATE SET count=counters.count+1",
                       (bucket, (now // seconds + 1) * seconds))

    def throttle_peer(self, peer):
        # Socket peer only. Forwarded headers never control the abuse identity.
        self.rate("peer:" + self._peer_key(peer), 300, 60)

    def throttle_account(self, account):
        self.rate("account:" + account, 60, 60)

    def _peer_key(self, peer):
        return hmac.new(self.settings.encryption_key.encode(), peer.encode(), hashlib.sha256).hexdigest()

    def admit_new_account(self, account, client):
        """Bound how fast new API accounts appear from one address and in total."""
        with self.db() as db:
            if db.execute("SELECT 1 FROM accounts WHERE id=?", (account,)).fetchone():
                return
        if client:
            self.rate("signup-ip:" + self._peer_key(client), self.settings.new_accounts_per_ip_day, 86400)
        self.rate("signup-all", self.settings.new_accounts_per_hour, 3600)

    async def identity(self, token, peer=""):
        if not token or len(token) > 8192 or "\n" in token or "\r" in token:
            raise RadarError("unauthorized", "Sign in with a verified Radar account", 401)
        try:
            async with httpx.AsyncClient(timeout=10, transport=self.transport, trust_env=False,
                                         follow_redirects=False) as client:
                async with client.stream("POST", self.settings.radar_url + "/auth/me",
                                         headers={"X-Auth-Token": token}, json={}) as response:
                    raw = bytearray()
                    async for chunk in response.aiter_bytes():
                        raw.extend(chunk)
                        if len(raw) > 262144:
                            raise ValueError()
            if response.status_code in {401, 403, 404}:
                raise RadarError("session_expired", "Sign in to Radar and reconnect your API account", 401)
            if response.status_code != 200:
                raise ValueError()
            data = json.loads(raw)
            user, cfg = data["user"], data["plan_details"]
            if not isinstance(user, dict) or not isinstance(cfg, dict):
                raise ValueError()
            if user.get("email_verified") is not True or any(user.get(x) for x in ("disabled", "banned", "suspended")):
                raise RadarError("account_unavailable", "A verified, active Radar account is required", 403)
            account, plan = user["_id"], data["plan"]
            if not isinstance(account, str) or not re.fullmatch(r"[a-zA-Z0-9_-]{1,100}", account) or plan not in PLANS:
                raise ValueError()
            included = min(PLANS[plan]["searches"], max(0, int(cfg.get("searches_per_month", 0))))
            if not PLANS[plan]["api_access"] or "api_access" not in cfg.get("features", []):
                included = 0
            following = min(PLANS[plan]["following"], max(0, int(cfg.get("company_tracking", 0))))
            identity = Identity(account, plan, token, included, following)
        except (ValueError, KeyError, TypeError, httpx.HTTPError):
            raise RadarError("identity_unavailable", "Radar account verification is unavailable", 503) from None
        if peer is not None:
            self.admit_new_account(account, peer)
        with self.db() as db:
            db.execute("INSERT INTO accounts(id,token,plan,included_limit) VALUES (?,?,?,?) ON CONFLICT(id) DO UPDATE SET token=excluded.token,plan=excluded.plan,included_limit=excluded.included_limit",
                       (account, self.cipher.encrypt(token.encode()).decode(), plan, included))
            if not db.execute("SELECT enabled FROM accounts WHERE id=?", (account,)).fetchone()[0]:
                raise RadarError("account_unavailable", "API account access is suspended", 403)
        return identity

    async def manage(self, request):
        identity = await self.identity(request.headers.get("X-Auth-Token", ""),
                                       request.scope.get("radar.client_ip", ""))
        self.throttle_account(identity.id)
        return identity

    async def authenticate(self, key):
        if not re.fullmatch(r"rdr_[a-f0-9]{64}", key):
            raise RadarError("unauthorized", "Missing or invalid API key", 401)
        with self.db() as db:
            row = db.execute("SELECT k.*,a.token,a.news,a.enabled FROM api_keys k JOIN accounts a ON k.account=a.id WHERE k.hash=? AND k.revoked=0 AND k.expires>?",
                             (hashlib.sha256(key.encode()).hexdigest(), int(time.time()))).fetchone()
        if not row or not row["enabled"]:
            raise RadarError("unauthorized", "Missing, expired or revoked API key", 401)
        try:
            token = self.cipher.decrypt(row["token"].encode()).decode()
            news = self.cipher.decrypt(row["news"].encode()).decode() if row["news"] else ""
        except InvalidToken:
            raise RadarError("account_store_unavailable", "Account credentials cannot be read", 503) from None
        identity = await self.identity(token, peer=None)
        if identity.id != row["account"]:
            raise RadarError("unauthorized", "Account identity changed", 401)
        # Carry the authoritative limits only within this request, never trust key input.
        return Principal(row["id"], row["name"], token, news, 60, identity.id, tuple(json.loads(row["scopes"])))

    def create_key(self, user, request):
        if any(x not in GROUPS | {"*"} for x in request.scopes):
            raise RadarError("invalid_request", "Unknown API scope", 422)
        now = int(time.time())
        key, key_id = "rdr_" + secrets.token_hex(32), secrets.token_hex(12)
        with self.db() as db:
            active = db.execute("SELECT COUNT(*) FROM api_keys WHERE account=? AND revoked=0 AND expires>?", (user.id, now)).fetchone()[0]
            recent = db.execute("SELECT COUNT(*) FROM api_keys WHERE account=? AND created>?", (user.id, now-86400)).fetchone()[0]
            if recent >= 10:
                raise RadarError("rate_limited", "Key creation limit reached; try again tomorrow", 429, 86400)
            if active >= (10 if user.plan == "business" else 3):
                raise RadarError("key_limit", "Revoke an existing key before creating another", 409)
            db.execute("INSERT INTO api_keys VALUES (?,?,?,?,?,?,?,?,0)",
                       (key_id, user.id, hashlib.sha256(key.encode()).hexdigest(), request.name, key[-4:],
                        json.dumps(sorted(set(request.scopes))), now, now + request.expires_days * 86400))
        return {"id": key_id, "name": request.name, "api_key": key, "expires_at": now + request.expires_days * 86400,
                "message": "Save this key now. It will not be shown again."}

    def keys(self, account):
        with self.db() as db:
            return [dict(r) for r in db.execute("SELECT id,name,last4,scopes,created,expires,revoked FROM api_keys WHERE account=? ORDER BY created DESC", (account,))]

    def revoke(self, account, key_id):
        with self.db() as db:
            changed = db.execute("UPDATE api_keys SET revoked=1 WHERE account=? AND id=?", (account, key_id)).rowcount
        if not changed:
            raise RadarError("not_found", "No such API key on this account", 404)
        return {"revoked": True}

    def reserve(self, user, feature, group, units):
        if "*" not in user.scopes and group not in user.scopes:
            raise RadarError("scope_required", "This key does not permit this data group", 403)
        # Composite calls also need every group they can invoke.
        if feature == "company_brief" and units == 7 and "*" not in user.scopes and "news" not in user.scopes:
            raise RadarError("scope_required", "A brief with news requires the news scope", 403)
        now = int(time.time())
        month = datetime.now(timezone.utc).strftime("%Y-%m")
        request_id = secrets.token_hex(16)
        with self.db() as db:
            for stale in db.execute("SELECT * FROM requests WHERE account=? AND state='pending' AND created<?", (user.account_id, now-600)).fetchall():
                self._settle(db, stale, 0)
            account = db.execute("SELECT * FROM accounts WHERE id=?", (user.account_id,)).fetchone()
            if not account or not account["enabled"]:
                raise RadarError("account_unavailable", "API account access is suspended", 403)
            active = db.execute("SELECT COUNT(*) FROM requests WHERE account=? AND state='pending'", (user.account_id,)).fetchone()[0]
            if active >= 3:
                raise RadarError("concurrency_limited", "At most three data requests may run at once", 429, 5)
            db.execute("INSERT OR IGNORE INTO usage(account,month) VALUES (?,?)", (user.account_id, month))
            usage = db.execute("SELECT * FROM usage WHERE account=? AND month=?", (user.account_id, month)).fetchone()
            included_limit = account["included_limit"]
            included = min(units, max(0, included_limit - usage["included"]))
            prepaid = units - included
            if prepaid and (not self.settings.payg_all_plans and not PLANS[account["plan"]]["api_access"]):
                raise RadarError("plan_required", "This API requires a Radar Business plan", 402)
            if prepaid > account["wallet"] or usage["prepaid"] + prepaid > account["spend_limit"]:
                raise RadarError("credits_required", "Add prepaid credits and set a monthly spending limit, or use available Business credits", 402)
            db.execute("UPDATE accounts SET wallet=wallet-? WHERE id=?", (prepaid, user.account_id))
            db.execute("UPDATE usage SET included=included+?,prepaid=prepaid+? WHERE account=? AND month=?", (included, prepaid, user.account_id, month))
            db.execute("INSERT INTO requests VALUES (?,?,?,?,?,?,?,?)", (request_id, user.account_id, month, feature, included, prepaid, "pending", now))
        return request_id

    @staticmethod
    def _settle(db, row, actual):
        if row["state"] != "pending":
            return
        actual = min(actual, row["included"] + row["prepaid"])
        included = min(actual, row["included"])
        prepaid = actual - included
        db.execute("UPDATE accounts SET wallet=wallet+? WHERE id=?", (row["prepaid"] - prepaid, row["account"]))
        db.execute("UPDATE usage SET included=included-?,prepaid=prepaid-? WHERE account=? AND month=?",
                   (row["included"] - included, row["prepaid"] - prepaid, row["account"], row["month"]))
        db.execute("UPDATE requests SET included=?,prepaid=?,state='settled' WHERE id=?", (included, prepaid, row["id"]))

    def settle(self, request_id, actual):
        with self.db() as db:
            row = db.execute("SELECT * FROM requests WHERE id=?", (request_id,)).fetchone()
            if row:
                self._settle(db, row, actual)

    def usage(self, user):
        month = datetime.now(timezone.utc).strftime("%Y-%m")
        with self.db() as db:
            account = db.execute("SELECT wallet,spend_limit,plan FROM accounts WHERE id=?", (user.id,)).fetchone()
            row = db.execute("SELECT included,prepaid FROM usage WHERE account=? AND month=?", (user.id, month)).fetchone()
            features = [dict(r) for r in db.execute("SELECT feature,CAST(SUM(included+prepaid) AS BIGINT) AS credits,COUNT(*) AS completed_requests FROM requests WHERE account=? AND month=? AND state='settled' AND included+prepaid>0 GROUP BY feature", (user.id, month))]
        return {"month_utc": month, "plan": user.plan, "included_limit": user.included,
                "included_used_or_reserved": row[0] if row else 0, "prepaid_used_or_reserved": row[1] if row else 0,
                "wallet_credits": account["wallet"], "monthly_prepaid_limit": account["spend_limit"], "features": features}

    def catalog(self):
        return {"plans": PLANS, "catalog_verified_on": "2026-09-20", "currency": "INR",
                "credit_price_paise": self.settings.credit_price_paise or None,
                "checkout_enabled": self.checkout_enabled(), "payg_all_verified_plans": self.settings.payg_all_plans,
                "metering": "One credit per successful data operation; briefs reserve 6 or 7, comparisons reserve 3 per company. Failed sections refunded.",
                "note": "Private API allocation mirrors Business search allowance; dashboard search usage is separate. Upstream data access limits still apply. Market.ai bundled is a cross-grant, not a standalone free subscription."}

    def checkout_enabled(self):
        s = self.settings
        return bool(s.credit_price_paise and s.razorpay_key_id and s.razorpay_key_secret and s.razorpay_webhook_secret)

    async def order(self, user, credits):
        if not self.checkout_enabled():
            raise RadarError("checkout_unavailable", "Pay-per-use checkout is not activated", 503)
        if not self.settings.payg_all_plans and not PLANS[user.plan]["api_access"]:
            raise RadarError("plan_required", "Prepaid overages require Radar Business", 402)
        self.rate("checkout:" + user.id, 5, 3600)
        amount = credits * self.settings.credit_price_paise
        if amount > 10000000:
            raise RadarError("invalid_request", "Top-up exceeds the per-order limit", 422)
        try:
            async with httpx.AsyncClient(timeout=15, trust_env=False, follow_redirects=False,
                                         transport=self.payment_transport) as client:
                response = await client.post("https://api.razorpay.com/v1/orders",
                    auth=(self.settings.razorpay_key_id, self.settings.razorpay_key_secret),
                    json={"amount": amount, "currency": "INR", "receipt": secrets.token_hex(16), "partial_payment": False})
            data = response.json()
            if response.status_code != 200 or data.get("amount") != amount or data.get("currency") != "INR" or not re.fullmatch(r"order_[a-zA-Z0-9]+", data.get("id", "")):
                raise ValueError()
        except (httpx.HTTPError, ValueError, TypeError):
            raise RadarError("checkout_unavailable", "Payment order could not be created; no API credits were added", 502) from None
        with self.db() as db:
            db.execute("INSERT INTO orders(id,account,credits,amount) VALUES (?,?,?,?)", (data["id"], user.id, credits, amount))
        return {"order_id": data["id"], "key_id": self.settings.razorpay_key_id, "amount": amount,
                "currency": "INR", "credits": credits, "status": "awaiting_captured_payment"}

    def webhook(self, raw, signature):
        if not self.checkout_enabled():
            raise RadarError("checkout_unavailable", "Pay-per-use checkout is not activated", 503)
        expected = hmac.new(self.settings.razorpay_webhook_secret.encode(), raw, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected, signature):
            raise RadarError("unauthorized", "Invalid payment signature", 401)
        try:
            payload = json.loads(raw)
            event = payload["event"]
            if event not in {"payment.captured", "refund.processed", "payment.dispute.created"}:
                return {"received": True}
            entity = payload["payload"]
            payment = entity.get("payment", {}).get("entity", {})
            reverse = event != "payment.captured"
            linked = entity.get("refund" if event == "refund.processed" else "dispute", {}).get("entity", {})
            payment_id = linked["payment_id"] if reverse else payment["id"]
            with self.db() as db:
                row = db.execute("SELECT * FROM orders WHERE " + ("payment=?" if reverse else "id=?"),
                                 (payment_id if reverse else payment["order_id"],)).fetchone()
                if not row:
                    if reverse:
                        # Retry after capture instead of losing an out-of-order reversal.
                        raise RadarError("payment_pending", "Payment capture must be reconciled first", 409)
                    return {"received": True}
                if reverse:
                    if not row["reversed"]:
                        # Full grant is frozen for any refund/dispute; operator reconciles partial refunds.
                        db.execute("UPDATE accounts SET wallet=MAX(0,wallet-?),enabled=0 WHERE id=?", (row["credits"], row["account"]))
                        db.execute("UPDATE orders SET reversed=1 WHERE id=?", (row["id"],))
                else:
                    if payment["status"] != "captured" or payment["amount"] != row["amount"] or payment["currency"] != "INR":
                        raise RadarError("payment_mismatch", "Payment does not match the stored order", 400)
                    if row["credited"] and row["payment"] != payment_id:
                        raise RadarError("payment_mismatch", "Order has already been paid", 409)
                    if not row["credited"]:
                        db.execute("UPDATE orders SET payment=?,credited=1 WHERE id=?", (payment_id, row["id"]))
                        db.execute("UPDATE accounts SET wallet=wallet+? WHERE id=?", (row["credits"], row["account"]))
        except (ValueError, KeyError, TypeError):
            raise RadarError("invalid_request", "Invalid payment event", 400) from None
        return {"received": True}


def register_account_routes(app, accounts):
    """Account mutations are HTTP-only, authenticated with a Radar dashboard session."""
    def result(data):
        from fastapi.responses import JSONResponse
        return JSONResponse(envelope("account", data), headers={"Cache-Control": "no-store"})

    from fastapi.responses import FileResponse, HTMLResponse

    @app.get("/developer", include_in_schema=False)
    async def developer_console(request: Request):
        # root_path is set by the operator/proxy deployment, never a caller URL.
        prefix = request.scope.get("root_path", "").rstrip("/")
        if prefix and not re.fullmatch(r"(?:/[A-Za-z0-9_-]+)+", prefix):
            raise RadarError("configuration_unavailable", "Invalid developer console mount path", 503)
        html = (Path(__file__).parent / "static/developer.html").read_text()
        html = html.replace('"/developer', '"' + prefix + '/developer')
        return HTMLResponse(html, headers={
            "Cache-Control": "no-store", "X-Robots-Tag": "noindex, nofollow", "Referrer-Policy": "no-referrer",
            "X-Content-Type-Options": "nosniff", "Content-Security-Policy": "default-src 'self'; script-src 'self' https://checkout.razorpay.com; style-src 'self'; frame-src https://api.razorpay.com https://checkout.razorpay.com; connect-src 'self' https://api.razorpay.com; img-src 'self' data: https://*.razorpay.com; frame-ancestors 'none'; base-uri 'none'; form-action 'self'"})

    @app.get("/developer/console.css", include_in_schema=False)
    async def console_css():
        return FileResponse(Path(__file__).parent / "static/console.css")

    @app.get("/developer/console.js", include_in_schema=False)
    async def console_js():
        return FileResponse(Path(__file__).parent / "static/console.js")

    @app.get("/account/plans", tags=["account"])
    async def plans(request: Request):
        await accounts.manage(request)
        return result(accounts.catalog())

    @app.post("/account/keys", tags=["account"])
    async def create_key(body: NewKey, request: Request):
        return result(accounts.create_key(await accounts.manage(request), body))

    @app.get("/account/keys", tags=["account"])
    async def list_keys(request: Request):
        return result(accounts.keys((await accounts.manage(request)).id))

    @app.delete("/account/keys/{key_id}", tags=["account"])
    async def revoke_key(key_id: str, request: Request):
        return result(accounts.revoke((await accounts.manage(request)).id, key_id))

    @app.post("/account/session", tags=["account"])
    async def reconnect(request: Request):
        await accounts.manage(request)
        return result({"connected": True})

    @app.put("/account/news-key", tags=["account"])
    async def link_news(body: LinkNews, request: Request):
        user = await accounts.manage(request)
        with accounts.db() as db:
            db.execute("UPDATE accounts SET news=? WHERE id=?", (accounts.cipher.encrypt(body.api_key.encode()).decode(), user.id))
        return result({"linked": True})

    @app.get("/account/usage", tags=["account"])
    async def usage(request: Request):
        return result(accounts.usage(await accounts.manage(request)))

    @app.put("/account/spending", tags=["account"])
    async def spending(body: Spending, request: Request):
        user = await accounts.manage(request)
        with accounts.db() as db:
            db.execute("UPDATE accounts SET spend_limit=? WHERE id=?", (body.monthly_credit_limit, user.id))
        return result({"monthly_prepaid_limit": body.monthly_credit_limit})

    @app.get("/account/following", tags=["account"])
    async def following(request: Request):
        user = await accounts.manage(request)
        with accounts.db() as db:
            items = [dict(r) for r in db.execute("SELECT domain,created FROM follows WHERE account=? ORDER BY created DESC", (user.id,))]
        return result({"companies": items, "limit": user.following, "count": len(items)})

    @app.put("/account/following", tags=["account"])
    async def follow(body: Company, request: Request):
        user = await accounts.manage(request)
        with accounts.db() as db:
            exists = db.execute("SELECT 1 FROM follows WHERE account=? AND domain=?", (user.id, body.domain)).fetchone()
            count = db.execute("SELECT COUNT(*) FROM follows WHERE account=?", (user.id,)).fetchone()[0]
            if not exists and count >= user.following:
                raise RadarError("following_limit", "This Radar plan's API watchlist limit has been reached", 402)
            db.execute("INSERT OR IGNORE INTO follows VALUES (?,?,?)", (user.id, body.domain, int(time.time())))
        return result({"domain": body.domain, "following": True})

    @app.delete("/account/following/{domain}", tags=["account"])
    async def unfollow(domain: str, request: Request):
        user = await accounts.manage(request)
        with accounts.db() as db:
            db.execute("DELETE FROM follows WHERE account=? AND domain=?", (user.id, domain))
        return result({"following": False})

    @app.post("/account/topups", tags=["account"])
    async def topup(body: TopUp, request: Request):
        return result(await accounts.order(await accounts.manage(request), body.credits))

    @app.post("/billing/webhook", tags=["billing"])
    async def webhook(request: Request):
        return result(accounts.webhook(await request.body(), request.headers.get("X-Razorpay-Signature", "")))
