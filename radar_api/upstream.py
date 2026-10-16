from __future__ import annotations

import json

import httpx

from .auth import principal
from .config import Settings
from .errors import RadarError


class Upstream:
    def __init__(self, settings: Settings, transport: httpx.AsyncBaseTransport | None = None):
        self.settings, self.transport = settings, transport

    async def call(self, service: str, path: str, *, body=None, params=None):
        user = principal()
        base = {"radar": self.settings.radar_url, "news": self.settings.news_url,
                "business_news": self.settings.business_news_url}[service]
        if not base:
            raise RadarError("service_unavailable", "This data service is not connected", 503)
        headers = {"Accept": "application/json"}
        if service == "radar":
            if body is not None:
                body = {**body, "auth_sign": user.radar_token}
            if user.radar_token:
                headers["X-Auth-Token"] = user.radar_token
        else:
            if not user.news_key:
                raise RadarError("access_required", "A linked News API key is required for this data", 403)
            headers["X-API-Key"] = user.news_key
        try:
            async with httpx.AsyncClient(timeout=self.settings.timeout_seconds, follow_redirects=False,
                                         transport=self.transport, trust_env=False) as client:
                async with client.stream("POST" if body is not None else "GET", base + path,
                                         json=body, params=params, headers=headers) as response:
                    chunks, size = [], 0
                    async for chunk in response.aiter_bytes():
                        size += len(chunk)
                        if size > self.settings.max_response_bytes:
                            raise RadarError("response_too_large", "Narrow the query or reduce the result limit", 502)
                        chunks.append(chunk)
                    raw = b"".join(chunks)
            retry = response.headers.get("retry-after", "")
            retry_after = min(3600, max(1, int(retry))) if retry.isdigit() else None
            if response.status_code >= 400 or 300 <= response.status_code < 400:
                # Preserve the News service's explicit strict-coverage failure,
                # without forwarding its diagnostic body or weakening its gate.
                if service in {"news", "business_news"} and response.status_code == 503:
                    try:
                        error_body = json.loads(raw)
                        error = error_body.get("error", {}) if isinstance(error_body, dict) else {}
                    except (ValueError, UnicodeError):
                        error = {}
                    if isinstance(error, dict) and error.get("kind") == "coverage_unavailable":
                        raise RadarError("coverage_unavailable", "Reliable News coverage is temporarily unavailable; no partial corpus totals are returned", 503)
                self._http_error(response.status_code, retry_after)
            payload = json.loads(raw)
            if not isinstance(payload, (dict, list)):
                raise ValueError("Invalid response shape")
            if isinstance(payload, dict) and (payload.get("error") or payload.get("ok") is False):
                code = payload.get("errorCode")
                if isinstance(code, int) and code in {401, 402, 403, 404, 429}:
                    self._http_error(code, retry_after)
                if isinstance(payload.get("error"), dict):
                    kind = payload["error"].get("kind", "")
                    if kind == "no_data":
                        raise RadarError("no_data", "No matching data was returned", 404)
                raise RadarError("upstream_unavailable", "The data service could not complete this request", 502)
            return payload
        except httpx.TimeoutException:
            raise RadarError("upstream_timeout", "The data service timed out; narrow the query or retry", 504) from None
        except httpx.HTTPError:
            raise RadarError("upstream_unavailable", "The data service is temporarily unavailable", 502) from None
        except (ValueError, UnicodeError, RecursionError):
            raise RadarError("invalid_upstream_response", "The data service returned an unreadable response", 502) from None

    @staticmethod
    def _http_error(status: int, retry_after=None):
        if status in {400, 422}:
            raise RadarError("invalid_request", "The data service rejected these query parameters", 400)
        if status in {401, 403}:
            raise RadarError("access_required", "The linked account does not have access to this data", 403)
        if status == 402:
            raise RadarError("quota_exceeded", "The linked account quota has been reached", 402)
        if status == 429:
            raise RadarError("rate_limited", "The data service request limit has been reached", 429, retry_after or 60)
        if status == 404:
            raise RadarError("no_data", "No matching data was returned", 404)
        raise RadarError("upstream_unavailable", "The data service could not complete this request", 502)
