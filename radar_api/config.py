from __future__ import annotations

import os
from dataclasses import dataclass, field
from urllib.parse import urlsplit


def _base(value: str) -> str:
    if not value:
        return ""
    u = urlsplit(value)
    if u.scheme not in {"http", "https"} or not u.hostname or u.username or u.password or u.query or u.fragment:
        raise ValueError("Upstream URLs must be HTTP(S) base URLs without credentials, query or fragment")
    return value.rstrip("/")


@dataclass(frozen=True)
class Settings:
    radar_url: str = "http://127.0.0.1:5100"
    news_url: str = ""
    business_news_url: str = ""
    keys_file: str = "secrets/keys.json"
    timeout_seconds: float = 45
    max_response_bytes: int = 8 * 1024 * 1024
    allowed_hosts: tuple[str, ...] = ("127.0.0.1", "localhost", "::1")
    allowed_origins: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self):
        for name in ("radar_url", "news_url", "business_news_url"):
            object.__setattr__(self, name, _base(getattr(self, name)))
        if not 1 <= self.timeout_seconds <= 120:
            raise ValueError("Timeout must be between 1 and 120 seconds")
        if not 1024 <= self.max_response_bytes <= 32 * 1024 * 1024:
            raise ValueError("Response limit must be between 1 KiB and 32 MiB")
        if not self.allowed_hosts or "*" in self.allowed_hosts:
            raise ValueError("Configure explicit allowed hosts")

    @classmethod
    def from_env(cls):
        return cls(
            radar_url=os.getenv("RADAR_UPSTREAM_URL", "http://127.0.0.1:5100"),
            news_url=os.getenv("RADAR_NEWS_URL", ""),
            business_news_url=os.getenv("RADAR_BUSINESS_NEWS_URL", ""),
            keys_file=os.getenv("RADAR_KEYS_FILE", "secrets/keys.json"),
            timeout_seconds=float(os.getenv("RADAR_TIMEOUT_SECONDS", "45")),
            max_response_bytes=int(os.getenv("RADAR_MAX_RESPONSE_BYTES", str(8 * 1024 * 1024))),
            allowed_hosts=tuple(x.strip() for x in os.getenv(
                "RADAR_ALLOWED_HOSTS", "127.0.0.1,localhost,::1").split(",") if x.strip()),
            allowed_origins=tuple(x.strip() for x in os.getenv(
                "RADAR_ALLOWED_ORIGINS", "").split(",") if x.strip()),
        )
