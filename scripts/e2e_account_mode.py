"""End-to-end account-mode check over real HTTP with several worker processes.

Starts a stub Radar identity/data service, runs `radar-api --workers N` against an
isolated ledger (SQLite file, or PostgreSQL with --database-url), and drives key
issuance, signup limits behind a trusted proxy, metering across workers, the account
request budget, revocation and signed payment webhooks. No production service,
credential or payment provider is contacted. Prints a pass/fail line per check.

    python scripts/e2e_account_mode.py [--database-url postgresql://...] [--workers 2]
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import socket
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import httpx
from cryptography.fernet import Fernet

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from radar_api.accounts import Accounts  # noqa: E402
from radar_api.config import Settings  # noqa: E402

SESSIONS = {f"session-{x}": x for x in "abcdef"}
HOOK_SECRET = "e2e-webhook-secret"


class StubRadar(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_POST(self):
        self.rfile.read(int(self.headers.get("Content-Length", 0) or 0))
        if self.path == "/auth/me":
            user = SESSIONS.get(self.headers.get("X-Auth-Token", ""))
            if not user:
                return self.reply(401, {"error": "unauthorized"})
            return self.reply(200, {"user": {"_id": user, "email_verified": True}, "plan": "business",
                                    "plan_details": {"features": ["api_access"], "searches_per_month": 5000,
                                                     "company_tracking": 1000}})
        if self.path == "/metas/":
            return self.reply(200, {"matched": [["Software", "feeds"], ["Digital Health", "PRACTICE_AREA"]]})
        self.reply(200, {"has_data": True, "items": []})

    def reply(self, status, body):
        raw = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)


def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--database-url", default="")
    parser.add_argument("--workers", type=int, default=2)
    args = parser.parse_args()

    stub = ThreadingHTTPServer(("127.0.0.1", 0), StubRadar)
    threading.Thread(target=stub.serve_forever, daemon=True).start()
    work = Path(tempfile.mkdtemp(prefix="radar-e2e-"))
    work.chmod(0o700)
    port = free_port()
    env = {**os.environ,
           "RADAR_ACCOUNTS_ENABLED": "1", "RADAR_ACCOUNTS_DB": str(work / "ledger.sqlite3"),
           "RADAR_ACCOUNTS_DATABASE_URL": args.database_url,
           "RADAR_ENCRYPTION_KEY": Fernet.generate_key().decode(),
           "RADAR_UPSTREAM_URL": f"http://127.0.0.1:{stub.server_address[1]}",
           "RADAR_TRUSTED_PROXIES": "127.0.0.1", "RADAR_NEW_ACCOUNTS_PER_IP_DAY": "2",
           "RADAR_CREDIT_PRICE_PAISE": "50", "RADAR_CREDIT_PRICE_CENTS": "1", "RADAR_RAZORPAY_KEY_ID": "rzp_test_e2e",
           "RADAR_RAZORPAY_KEY_SECRET": "unused", "RADAR_RAZORPAY_WEBHOOK_SECRET": HOOK_SECRET}
    server = subprocess.Popen([sys.executable, "-c", "from radar_api.cli import api; api()",
                               "--port", str(port), "--workers", str(args.workers)],
                              env=env, cwd=work, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    base = f"http://127.0.0.1:{port}"
    results = []

    def check(name, ok, detail=""):
        results.append(ok)
        print(("PASS " if ok else "FAIL ") + name + (f"  ({detail})" if detail else ""))

    try:
        for _ in range(100):
            try:
                if httpx.get(base + "/healthz", timeout=1).status_code == 200:
                    break
            except httpx.HTTPError:
                time.sleep(0.2)
        else:
            raise SystemExit("server did not start: " + server.stderr.read1().decode()[-2000:])
        client = httpx.Client(base_url=base, timeout=30)

        def session(token, ip):
            return {"X-Auth-Token": token, "X-Forwarded-For": ip}

        r = client.post("/account/keys", headers=session("session-a", "203.0.113.1"), json={"name": "e2e"})
        check("key issued once over HTTP", r.status_code == 200 and r.json()["data"]["api_key"].startswith("rdr_"), r.status_code)
        key = r.json()["data"]["api_key"]
        key_id = r.json()["data"]["id"]

        b = client.get("/account/usage", headers=session("session-b", "203.0.113.1")).status_code
        c = client.get("/account/usage", headers=session("session-c", "203.0.113.1")).status_code
        c2 = client.get("/account/usage", headers=session("session-c", "198.51.100.9")).status_code
        check("signup limit per forwarded client address", (b, c, c2) == (200, 429, 200), f"b={b} c={c} c-other-ip={c2}")
        again = client.get("/account/usage", headers=session("session-a", "203.0.113.1")).status_code
        check("existing account is not a new signup", again == 200, again)

        api = {"X-API-Key": key}
        codes = [client.post("/v1/industries/discover", headers=api, json={"q": "software"}).status_code for _ in range(5)]
        usage = client.get("/account/usage", headers=session("session-a", "203.0.113.1")).json()["data"]
        check("metered calls across workers settle exactly", codes == [200] * 5 and usage["included_used_or_reserved"] == 5,
              f"codes={codes} included={usage['included_used_or_reserved']}")

        def burst(_):
            return client.post("/v1/industries/discover", headers=api, json={"q": "software"}).status_code

        if time.time() % 60 > 40:  # keep the burst inside one request-budget minute
            time.sleep(61 - time.time() % 60)
        with ThreadPoolExecutor(16) as pool:
            burst_codes = list(pool.map(burst, range(80)))
        ok = burst_codes.count(200)
        time.sleep(61 - time.time() % 60)  # account management shares the exhausted budget
        usage = client.get("/account/usage", headers=session("session-a", "203.0.113.2")).json()["data"]
        check("account budget and concurrency limits hold across workers",
              429 in burst_codes and ok <= 60 and usage["included_used_or_reserved"] == 5 + ok,
              f"200={ok} 429={burst_codes.count(429)} metered={usage['included_used_or_reserved']}")

        missing = client.delete("/account/keys/not-a-key", headers=session("session-a", "203.0.113.3")).status_code
        check("revoking an unknown key returns 404", missing == 404, missing)
        client.delete(f"/account/keys/{key_id}", headers=session("session-a", "203.0.113.3"))
        after = client.post("/v1/industries/discover", headers=api, json={"q": "software"}).status_code
        check("revoked key is refused on every worker", after == 401, after)

        ledger = Accounts(Settings(accounts_enabled=True, accounts_db=env["RADAR_ACCOUNTS_DB"],
                                   accounts_database_url=args.database_url, encryption_key=env["RADAR_ENCRYPTION_KEY"],
                                   credit_price_paise=50, credit_price_cents=1, razorpay_key_id="rzp_test_e2e", razorpay_key_secret="unused",
                                   razorpay_webhook_secret=HOOK_SECRET))
        with ledger.db() as db:  # the order a Razorpay checkout would have created
            db.execute("INSERT INTO orders(id,account,credits,amount) VALUES (?,?,?,?)", ("order_e2e1", "a", 200, 10000))
        event = json.dumps({"event": "payment.captured", "payload": {"payment": {"entity": {
            "id": "pay_e2e1", "order_id": "order_e2e1", "status": "captured", "amount": 10000, "currency": "INR"}}}}).encode()
        signed = {"X-Razorpay-Signature": hmac.new(HOOK_SECRET.encode(), event, hashlib.sha256).hexdigest(),
                  "Content-Type": "application/json"}
        forged = client.post("/billing/webhook", content=event, headers={**signed, "X-Razorpay-Signature": "0" * 64}).status_code
        first = client.post("/billing/webhook", content=event, headers=signed).status_code
        replay = client.post("/billing/webhook", content=event, headers=signed).status_code
        wallet = client.get("/account/usage", headers=session("session-a", "203.0.113.4")).json()["data"]["wallet_credits"]
        check("signed webhook credits once; forged and replayed are harmless",
              (forged, first, replay, wallet) == (401, 200, 200, 200), f"forged={forged} first={first} replay={replay} wallet={wallet}")
        refund = json.dumps({"event": "refund.processed", "payload": {"refund": {"entity": {"payment_id": "pay_e2e1"}}}}).encode()
        r = client.post("/billing/webhook", content=refund, headers={
            "X-Razorpay-Signature": hmac.new(HOOK_SECRET.encode(), refund, hashlib.sha256).hexdigest()})
        frozen = client.get("/account/usage", headers=session("session-a", "203.0.113.4")).status_code
        check("refund removes credits and suspends the account", r.status_code == 200 and frozen == 403, f"refund={r.status_code} usage={frozen}")
    finally:
        server.terminate()
        server.wait(10)
        stub.shutdown()
    print(f"{sum(results)}/{len(results)} checks passed with {args.workers} workers on "
          + ("PostgreSQL" if args.database_url else "SQLite"))
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
