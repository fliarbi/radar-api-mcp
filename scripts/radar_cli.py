#!/usr/bin/env python3
"""radar: command-line client for the Radar API (company data, financials, funding,
investors, people, apps, jobs and financial news). Standard library only (Python 3.8+).
The same key works on the Prism News APIs.

    radar login                                   # save your API key (owner-only file)
    radar get-financials --domain zomato.com --period-type annual
    radar companies/search --filters.industries FinTech --filters.locations India --limit 10 --table
    radar search-news --q "stock market" --date-from 2026-01-01 --limit 10 --table
    radar features                                # every operation and its path
    radar call companies/brief '{"domain": "razorpay.com"}'

`--a.b value` builds nested fields ({"a": {"b": value}}); repeat an option for a list.
Environment overrides: RADAR_API_KEY, RADAR_API_URL (default https://radar-api.fliarbi.com).
"""
from __future__ import annotations

import getpass
import json
import os
import stat
import sys
import urllib.error
import urllib.request
from pathlib import Path

VERSION = "1.0.0"
DEFAULT_URL = "https://radar-api.fliarbi.com"
CONFIG = Path(os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config") / "radar" / "config.json"
LISTS = {"industries", "sectors", "markets", "business_models", "locations", "sizes", "stages", "technologies",
         "products", "skills", "event_types", "financing_status", "ownership_status", "revenue_bands", "revenue_growth",
         "profitability", "entity_type", "revenue_models", "business_approaches", "company_names", "domains", "roles",
         "sections", "fields", "scopes"}
FEATURES = {"search-companies": "companies/search", "semantic-company-search": "companies/semantic-search", "get-company": "companies/profile", "get-company-field": "companies/field", "company-apps": "companies/apps", "opportunity-presets": "companies/opportunities/presets", "search-opportunities": "companies/opportunities/search", "company-filter-catalog": "companies/filters", "company-filter-options": "companies/filter-options", "get-company-columns": "companies/columns", "get-company-intelligence": "companies/intelligence", "financial-filter-catalog": "companies/financials/filters", "screen-company-financials": "companies/financials/screen", "get-company-team": "companies/team", "get-financials": "companies/financials", "get-company-events": "companies/events", "get-company-funding": "companies/funding", "get-company-enrichment": "companies/enrichment", "find-competitors": "companies/competitors", "company-brief": "companies/brief", "compare-companies": "companies/compare", "search-investors": "investors/search", "investor-directory": "investors/directory", "get-investor-page": "investors/page", "get-investor-field": "investors/field", "market-pulse": "markets/pulse", "location-intelligence": "locations/intelligence", "discover-industries": "industries/discover", "search-jobs": "jobs/search", "job-filter-catalog": "jobs/filters", "job-filter-options": "jobs/filter-options", "search-internships": "jobs/internships/search", "companies-offering-internships": "jobs/internships/companies", "get-internship": "jobs/internships/detail", "companies-hiring": "jobs/companies", "get-job": "jobs/detail", "salary-benchmark": "jobs/salary-benchmark", "search-apps": "apps/search", "get-app": "apps/profile", "get-app-field": "apps/field", "app-filter-options": "apps/filter-options", "search-people": "people/search", "people-filter-options": "people/filter-options", "get-company-contacts": "contacts/company", "get-person-contacts": "contacts/person", "search-news": "news/search", "search-business-news": "news/business", "news-overview": "news/overview", "news-trends": "news/trends", "news-sentiment": "news/sentiment", "search-business-events": "news/events", "search-funding-news": "news/funding", "get-article": "news/article"}


def die(msg: str, code: int = 1) -> None:
    print(msg, file=sys.stderr)
    sys.exit(code)


def load_config() -> dict:
    try:
        return json.loads(CONFIG.read_text())
    except (OSError, ValueError):
        return {}


def save_config(cfg: dict) -> None:
    CONFIG.parent.mkdir(parents=True, exist_ok=True)
    os.chmod(CONFIG.parent, stat.S_IRWXU)
    fd = os.open(CONFIG, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(cfg, f, indent=1)
    os.chmod(CONFIG, 0o600)


def settings() -> tuple:
    cfg = load_config()
    base = (os.environ.get("RADAR_API_URL") or cfg.get("url") or DEFAULT_URL).rstrip("/")
    key = os.environ.get("RADAR_API_KEY") or cfg.get("key") or ""
    if not key:
        die("No API key. Run `radar login`, or set RADAR_API_KEY. Create a key at https://fliarbi.com/radar-api/developer")
    return base, key


def request(base: str, key: str, method: str, path: str, body: dict | None):
    data = json.dumps(body or {}).encode() if method == "POST" else None
    req = urllib.request.Request(base + path, data=data, method=method, headers={
        "Authorization": "Bearer " + key, "Content-Type": "application/json", "User-Agent": "radar-cli/" + VERSION})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            raw, status = r.read(), r.status
    except urllib.error.HTTPError as e:
        raw, status = e.read(), e.code
    except urllib.error.URLError as e:
        die(f"Cannot reach {base}: {e.reason}")
    try:
        return status, json.loads(raw or b"{}")
    except ValueError:
        return status, {"ok": False, "error": {"kind": "not_json", "message": raw[:200].decode(errors="replace")}}


def value(v: str):
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    for cast in (int, float):
        try:
            return cast(v)
        except ValueError:
            pass
    return v


def parse(argv: list) -> tuple:
    """Positional words, a nested request body and client flags (--table, -o FILE, --json BODY)."""
    pos, body, flags = [], {}, {}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ("--table", "--raw"):
            flags[a[2:]] = True
        elif a in ("-o", "--output", "--json"):
            if i + 1 >= len(argv):
                die(f"{a} needs a value", 2)
            flags["output" if a != "--json" else "json"] = argv[i + 1]
            i += 1
        elif a.startswith("--"):
            name, _, inline = a[2:].partition("=")
            if not inline:
                if i + 1 >= len(argv):
                    die(f"--{name} needs a value", 2)
                inline = argv[i + 1]
                i += 1
            parts = [p.replace("-", "_") for p in name.split(".")]
            node = body
            for p in parts[:-1]:
                node = node.setdefault(p, {})
            leaf, v = parts[-1], value(inline)
            if leaf in node:
                node[leaf] = (node[leaf] if isinstance(node[leaf], list) else [node[leaf]]) + [v]
            else:
                node[leaf] = [v] if leaf in LISTS else v
        else:
            pos.append(a)
        i += 1
    return pos, body, flags


def table(payload: dict) -> str:
    data = payload.get("data") or {}
    items = next((v for v in data.values() if isinstance(v, list) and v and isinstance(v[0], dict)), None) \
        if isinstance(data, dict) else None
    if not items:
        return json.dumps(payload, indent=1, ensure_ascii=False)
    keys = [k for k in items[0] if not isinstance(items[0][k], (list, dict))][:7]
    rows = [[str(it.get(k, ""))[:60] for k in keys] for it in items]
    width = [max(len(k), *(len(r[j]) for r in rows)) for j, k in enumerate(keys)]
    line = lambda cells: "  ".join(c.ljust(w) for c, w in zip(cells, width))  # noqa: E731
    return "\n".join([line(keys), line(["-" * w for w in width])] + [line(r) for r in rows])


def login() -> None:
    cfg = load_config()
    print("Radar API login. Create a key at https://fliarbi.com/radar-api/developer")
    url = input(f"API URL [{cfg.get('url') or DEFAULT_URL}]: ").strip()
    cfg["url"] = (url or cfg.get("url") or DEFAULT_URL).rstrip("/")
    key = getpass.getpass("API key (input hidden): ").strip()
    if key:
        cfg["key"] = key
    if not cfg.get("key"):
        die("An API key is required.")
    status, payload = request(cfg["url"], cfg["key"], "GET", "/v1/capabilities", None)
    if status != 200:
        die(f"Check failed: HTTP {status} {(payload.get('error') or {}).get('kind')}. Nothing was saved.")
    save_config(cfg)
    print(f"Saved to {CONFIG}. Try: radar features")


def usage() -> str:
    return ("radar " + VERSION + "\nusage: radar OPERATION [--field value ...] [--json BODY] [--table] [-o FILE]\n"
            "       radar login | logout | features | mcp-config | call PATH [JSON]\n"
            "OPERATION is a name (get-financials) or a path (companies/financials); see `radar features`.\n"
            "Example: radar get-financials --domain zomato.com --period-type annual")


def main(argv: list) -> None:
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(usage())
        return
    if argv[0] in ("-V", "--version"):
        print(VERSION)
        return
    cmd, rest = argv[0], argv[1:]
    if cmd == "login":
        return login()
    if cmd == "logout":
        cfg = load_config()
        cfg.pop("key", None)
        save_config(cfg)
        print("Key removed from", CONFIG)
        return
    if cmd == "features":
        for name, path in FEATURES.items():
            print(f"{name:34} POST /v1/{path}")
        return
    if cmd == "mcp-config":
        base = (os.environ.get("RADAR_API_URL") or load_config().get("url") or DEFAULT_URL).rstrip("/")
        print(json.dumps({"mcpServers": {"radar": {"type": "http", "url": base + "/mcp",
                                                   "headers": {"Authorization": "Bearer ${RADAR_API_KEY}"}}}}, indent=2))
        return
    pos, body, flags = parse(rest)
    if cmd == "call":
        if not pos:
            die("usage: call PATH [JSON]", 2)
        path, body = pos[0].strip("/"), {**(json.loads(pos[1]) if len(pos) > 1 else {}), **body}
    else:
        path = FEATURES.get(cmd) or FEATURES.get(cmd.replace("_", "-")) or (cmd.strip("/") if cmd.strip("/") in FEATURES.values() else None)
        if not path:
            die(f"Unknown operation {cmd!r}. Run `radar features`.", 2)
        body = {**(json.loads(flags["json"]) if "json" in flags else {}), **body}
    base, key = settings()
    status, payload = request(base, key, "POST", "/v1/" + (path[3:] if path.startswith("v1/") else path), body)
    out = table(payload) if flags.get("table") and status == 200 else json.dumps(payload, indent=1, ensure_ascii=False)
    if flags.get("output"):
        Path(flags["output"]).write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n")
        print(f"HTTP {status}: wrote {flags['output']}", file=sys.stderr)
    else:
        print(out)
    if status != 200 or not payload.get("ok", True):
        sys.exit(1)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit(130)
