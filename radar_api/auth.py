from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import threading
import time
from collections import deque
from contextvars import ContextVar
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from starlette.datastructures import Headers
from starlette.responses import JSONResponse

from .errors import RadarError, envelope


@dataclass(frozen=True)
class Principal:
    key_id: str
    name: str
    radar_token: str = field(default="", repr=False)
    news_key: str = field(default="", repr=False)
    rate_per_minute: int = 60
    account_id: str = ""
    scopes: tuple[str, ...] = ("*",)


CURRENT: ContextVar[Principal | None] = ContextVar("radar_principal", default=None)


def principal() -> Principal:
    user = CURRENT.get()
    if user is None:
        raise RadarError("unauthorized", "An API key is required", 401)
    return user


class KeyStore:
    """Reload each request: revocation is immediate, secrets never enter logs or responses."""

    def __init__(self, path: str):
        self.path = Path(path)

    def authenticate(self, key: str) -> Principal:
        if not re.fullmatch(r"rdr_[a-f0-9]{64}", key):
            raise RadarError("unauthorized", "Missing or invalid API key", 401)
        try:
            info = self.path.stat()
            if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
                raise ValueError("Key file must be owner-only")
            records = json.loads(self.path.read_text())["keys"]
            if not isinstance(records, list):
                raise ValueError("Invalid key records")
        except (OSError, ValueError, KeyError, TypeError):
            raise RadarError("configuration_unavailable", "Preview access is not configured", 503) from None
        digest = hashlib.sha256(key.encode()).hexdigest()
        for record in records:
            if not isinstance(record, dict) or record.get("sha256") != digest:
                continue
            if not record.get("active", False):
                break
            try:
                if record.get("expires_at"):
                    expiry = datetime.fromisoformat(record["expires_at"].replace("Z", "+00:00"))
                    if expiry.tzinfo is None or expiry <= datetime.now(timezone.utc):
                        break
                rate = int(record.get("rate_per_minute", 60))
                if not 1 <= rate <= 600:
                    raise ValueError("Invalid rate")
                scopes = record.get("scopes", ["*"])
                if not isinstance(scopes, list) or not scopes or not all(isinstance(s, str) for s in scopes):
                    raise ValueError("Invalid scopes")
                return Principal(digest, str(record.get("name", "preview")),
                                 str(record.get("radar_token", "")), str(record.get("news_key", "")), rate, scopes=tuple(scopes))
            except (TypeError, ValueError):
                break
        raise RadarError("unauthorized", "Missing, expired or revoked API key", 401)


class RateLimiter:
    """Single-process preview limiter; upstream account quotas apply independently."""

    def __init__(self):
        self.calls: dict[str, deque[float]] = {}
        self.lock = threading.Lock()

    def check(self, user: Principal):
        now = time.monotonic()
        with self.lock:
            self.calls = {k: v for k, v in self.calls.items() if v and v[-1] > now - 60}
            q = self.calls.setdefault(user.key_id, deque())
            while q and q[0] <= now - 60:
                q.popleft()
            if len(q) >= user.rate_per_minute:
                raise RadarError("rate_limited", "Request limit reached; retry later", 429,
                                 max(1, int(61 - (now - q[0]))))
            q.append(now)


class AuthMiddleware:
    """Pure ASGI middleware also covers MCP mounts without losing ContextVar state."""

    def __init__(self, app, *, store: KeyStore, limiter: RateLimiter, allowed_origins: tuple[str, ...], accounts=None):
        self.app, self.store, self.limiter = app, store, limiter
        self.allowed_origins = allowed_origins
        self.accounts = accounts

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        headers = Headers(scope=scope)
        path = scope.get("path", "")
        try:
            origin = headers.get("origin")
            if origin and origin not in self.allowed_origins:
                raise RadarError("forbidden", "Origin is not allowed", 403)
            if path == "/healthz":
                return await self.app(scope, receive, send)
            if self.accounts:
                self.accounts.throttle_peer((scope.get("client") or ("unknown",))[0])
            # Bound both Content-Length and chunked bodies before dispatching a tool.
            if scope.get("method") in {"POST", "PUT", "PATCH"}:
                length = headers.get("content-length", "")
                if length.isdigit() and int(length) > 262144:
                    raise RadarError("request_too_large", "Request body exceeds 256 KiB", 413)
                buffered, count = [], 0
                while True:
                    message = await receive()
                    if message["type"] == "http.disconnect":
                        return
                    count += len(message.get("body", b""))
                    if count > 262144:
                        raise RadarError("request_too_large", "Request body exceeds 256 KiB", 413)
                    buffered.append(message)
                    if not message.get("more_body", False):
                        break
                original_receive = receive

                async def replay():
                    if buffered:
                        return buffered.pop(0)
                    return await original_receive()

                receive = replay
            if self.accounts and (path.startswith("/account/") or path == "/billing/webhook" or path in {"/developer", "/developer/console.css", "/developer/console.js"}):
                # These routes authenticate Radar sessions or provider signatures themselves.
                return await self.app(scope, receive, send)
            bearer = headers.get("authorization", "")
            bearer_key = bearer[7:].strip() if bearer.lower().startswith("bearer ") else ""
            api_key = headers.get("x-api-key", "").strip()
            if bearer and not bearer_key or api_key and bearer_key and api_key != bearer_key:
                raise RadarError("unauthorized", "Supply one consistent API key", 401)
            if self.accounts:
                user = await self.accounts.authenticate(api_key or bearer_key)
                self.accounts.throttle_account(user.account_id)
            else:
                user = self.store.authenticate(api_key or bearer_key)
                self.limiter.check(user)
            token = CURRENT.set(user)
            try:
                await self.app(scope, receive, send)
            finally:
                CURRENT.reset(token)
        except RadarError as exc:
            headers_out = {"Cache-Control": "no-store"}
            if exc.status == 401:
                headers_out["WWW-Authenticate"] = "Bearer"
            if exc.retry_after:
                headers_out["Retry-After"] = str(exc.retry_after)
            response = JSONResponse(envelope("access", error=exc), status_code=exc.status, headers=headers_out)
            await response(scope, receive, send)
