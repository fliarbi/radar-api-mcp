from __future__ import annotations

import ipaddress
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
    profile_mongo_uri: str = field(default="", repr=False)
    investor_data_dir: str = ""
    jobs_mongo_uri: str = field(default="", repr=False)
    apps_ch_url: str = ""
    apps_ch_user: str = field(default="default", repr=False)
    apps_ch_password: str = field(default="", repr=False)
    social_ch_url: str = ""
    social_ch_user: str = field(default="", repr=False)
    social_ch_password: str = field(default="", repr=False)
    company_ch_url: str = ""
    company_ch_user: str = field(default="", repr=False)
    company_ch_password: str = field(default="", repr=False)
    timeout_seconds: float = 45
    max_response_bytes: int = 8 * 1024 * 1024
    allowed_hosts: tuple[str, ...] = ("127.0.0.1", "localhost", "::1")
    allowed_origins: tuple[str, ...] = field(default_factory=tuple)
    accounts_enabled: bool = False
    accounts_db: str = "secrets/accounts.sqlite3"
    accounts_database_url: str = field(default="", repr=False)
    trusted_proxies: tuple[str, ...] = field(default_factory=tuple)
    new_accounts_per_ip_day: int = 3
    new_accounts_per_hour: int = 100
    encryption_key: str = field(default="", repr=False)
    payg_all_plans: bool = True
    credit_price_paise: int = 0
    credit_price_cents: int = 0
    min_topup_cents: int = 500
    razorpay_key_id: str = ""
    razorpay_key_secret: str = field(default="", repr=False)
    razorpay_webhook_secret: str = field(default="", repr=False)
    # Key checks for sibling Fliar APIs (Prism News) that accept the same rdr_ keys.
    introspect_secret: str = field(default="", repr=False)
    introspect_peers: tuple[str, ...] = ("127.0.0.1", "::1")
    # Public base URLs of the Prism News APIs shown on the combined developer page.
    public_news_url: str = ""
    public_business_news_url: str = ""

    def __post_init__(self):
        for name in ("radar_url", "news_url", "business_news_url", "apps_ch_url", "social_ch_url", "company_ch_url",
                     "public_news_url", "public_business_news_url"):
            object.__setattr__(self, name, _base(getattr(self, name)))
        if not 1 <= self.timeout_seconds <= 120:
            raise ValueError("Timeout must be between 1 and 120 seconds")
        if not 1024 <= self.max_response_bytes <= 32 * 1024 * 1024:
            raise ValueError("Response limit must be between 1 KiB and 32 MiB")
        if not self.allowed_hosts or "*" in self.allowed_hosts:
            raise ValueError("Configure explicit allowed hosts")
        if not 0 <= self.credit_price_paise <= 100000:
            raise ValueError("Credit price must be an integer from 0 to 100000 paise")
        if not 0 <= self.credit_price_cents <= 100000:
            raise ValueError("Credit price must be an integer from 0 to 100000 US cents")
        if not 100 <= self.min_topup_cents <= 100000:
            raise ValueError("Minimum top-up must be from 100 to 100000 US cents")
        if self.accounts_database_url and urlsplit(self.accounts_database_url).scheme not in {"postgresql", "postgres"}:
            raise ValueError("RADAR_ACCOUNTS_DATABASE_URL must be a postgresql:// URL")
        for proxy in self.trusted_proxies:
            ipaddress.ip_network(proxy, strict=False)  # Raises on a malformed proxy address.
        if not 1 <= self.new_accounts_per_ip_day <= 1000 or not 1 <= self.new_accounts_per_hour <= 100000:
            raise ValueError("New account limits must be positive and bounded")
        if self.introspect_secret and len(self.introspect_secret) < 32:
            raise ValueError("RADAR_INTROSPECT_SECRET must be at least 32 characters")
        for peer in self.introspect_peers:
            ipaddress.ip_address(peer)  # Raises on a malformed peer address.
        if self.accounts_enabled and not self.encryption_key:
            raise ValueError("Account mode requires RADAR_ENCRYPTION_KEY")

    @classmethod
    def from_env(cls):
        return cls(
            radar_url=os.getenv("RADAR_UPSTREAM_URL", "http://127.0.0.1:5100"),
            news_url=os.getenv("RADAR_NEWS_URL", ""),
            business_news_url=os.getenv("RADAR_BUSINESS_NEWS_URL", ""),
            keys_file=os.getenv("RADAR_KEYS_FILE", "secrets/keys.json"),
            profile_mongo_uri=os.getenv("RADAR_PROFILE_MONGO_URI", ""),
            investor_data_dir=os.getenv("RADAR_INVESTOR_DATA_DIR", ""),
            jobs_mongo_uri=os.getenv("RADAR_JOBS_MONGO_URI", ""),
            apps_ch_url=os.getenv("RADAR_APPS_CH_URL", ""),
            apps_ch_user=os.getenv("RADAR_APPS_CH_USER", "default"),
            apps_ch_password=os.getenv("RADAR_APPS_CH_PASSWORD", ""),
            social_ch_url=os.getenv("RADAR_SOCIAL_CH_URL", ""),
            social_ch_user=os.getenv("RADAR_SOCIAL_CH_USER", ""),
            social_ch_password=os.getenv("RADAR_SOCIAL_CH_PASSWORD", ""),
            company_ch_url=os.getenv("RADAR_COMPANY_CH_URL", ""),
            company_ch_user=os.getenv("RADAR_COMPANY_CH_USER", ""),
            company_ch_password=os.getenv("RADAR_COMPANY_CH_PASSWORD", ""),
            timeout_seconds=float(os.getenv("RADAR_TIMEOUT_SECONDS", "45")),
            max_response_bytes=int(os.getenv("RADAR_MAX_RESPONSE_BYTES", str(8 * 1024 * 1024))),
            allowed_hosts=tuple(x.strip() for x in os.getenv(
                "RADAR_ALLOWED_HOSTS", "127.0.0.1,localhost,::1").split(",") if x.strip()),
            allowed_origins=tuple(x.strip() for x in os.getenv(
                "RADAR_ALLOWED_ORIGINS", "").split(",") if x.strip()),
            accounts_enabled=os.getenv("RADAR_ACCOUNTS_ENABLED", "0") == "1",
            accounts_db=os.getenv("RADAR_ACCOUNTS_DB", "secrets/accounts.sqlite3"),
            accounts_database_url=os.getenv("RADAR_ACCOUNTS_DATABASE_URL", ""),
            trusted_proxies=tuple(x.strip() for x in os.getenv(
                "RADAR_TRUSTED_PROXIES", "").split(",") if x.strip()),
            new_accounts_per_ip_day=int(os.getenv("RADAR_NEW_ACCOUNTS_PER_IP_DAY", "3")),
            new_accounts_per_hour=int(os.getenv("RADAR_NEW_ACCOUNTS_PER_HOUR", "100")),
            encryption_key=os.getenv("RADAR_ENCRYPTION_KEY", ""),
            payg_all_plans=os.getenv("RADAR_PAYG_ALL_PLANS", "1") == "1",
            credit_price_paise=int(os.getenv("RADAR_CREDIT_PRICE_PAISE", "0")),
            credit_price_cents=int(os.getenv("RADAR_CREDIT_PRICE_CENTS", "0")),
            min_topup_cents=int(os.getenv("RADAR_MIN_TOPUP_CENTS", "500")),
            razorpay_key_id=os.getenv("RADAR_RAZORPAY_KEY_ID", ""),
            razorpay_key_secret=os.getenv("RADAR_RAZORPAY_KEY_SECRET", ""),
            razorpay_webhook_secret=os.getenv("RADAR_RAZORPAY_WEBHOOK_SECRET", ""),
            introspect_secret=os.getenv("RADAR_INTROSPECT_SECRET", ""),
            introspect_peers=tuple(x.strip() for x in os.getenv(
                "RADAR_INTROSPECT_PEERS", "127.0.0.1,::1").split(",") if x.strip()),
            public_news_url=os.getenv("RADAR_PUBLIC_NEWS_URL", ""),
            public_business_news_url=os.getenv("RADAR_PUBLIC_BUSINESS_NEWS_URL", ""),
        )
