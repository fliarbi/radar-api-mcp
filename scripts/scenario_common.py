"""Shared engine for the keyword-researched demonstration pages (adapted from the Prism News repos:
Radar pages live in docs/use-cases).

plan.json (written by plan_scenarios.py) lists, per segment, candidate scenarios in
search-demand order. Each scenario carries the exact API calls behind its page.
capture_scenarios.py runs those calls against a live API and keeps the first
`target` populated scenarios per segment; build_scenario_pages.py renders them.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCEN = ROOT / "docs/use-cases"
CAPS = ROOT / "docs/examples/use-cases"
RESEARCH = ROOT / "docs/research"
PLAN = SCEN / "plan.json"
LOG = SCEN / "capture_log.json"
PRIVATE_META = ("plan", "quota", "key", "account", "billing")
README_START, README_END = "<!-- use-cases:start -->", "<!-- use-cases:end -->"


# ── capture ────────────────────────────────────────────────────────────────────
def call(base: str, key: str, method: str, path: str, body: dict, timeout: int = 180) -> tuple[int, dict]:
    url, data = base + path, None
    if method == "GET":
        if body:
            url += "?" + urllib.parse.urlencode(body, doseq=True)
    else:
        data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"X-API-Key": key, "Content-Type": "application/json", "User-Agent": "fliar-docs-capture/1.0"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 502, 503) and attempt < 4:
                time.sleep(int(e.headers.get("Retry-After") or 15))
                continue
            try:
                return e.code, json.loads(e.read() or b"{}")
            except ValueError:
                return e.code, {"ok": False, "error": {"kind": f"http_{e.code}"}}
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < 4:
                time.sleep(10)
                continue
            return 599, {"ok": False, "error": {"kind": "network", "reason": str(e)[:120]}}
    return 429, {"ok": False, "error": {"kind": "rate_limited"}}


def clean(payload: dict) -> dict:
    payload["meta"] = {k: v for k, v in (payload.get("meta") or {}).items() if k not in PRIVATE_META}
    return payload


def capture_scenario(base: str, key: str, s: dict) -> dict:
    """Run every call of one scenario; returns the record written to docs/examples/scenarios."""
    out = []
    for c in s["calls"]:
        status, payload = call(base, key, c["method"], c["path"], c.get("body") or {})
        out.append({"name": c["name"], "request": {"method": c["method"], "path": c["path"], "body": c.get("body") or {}},
                    "status": status, "response": clean(payload)})
    rec = {"slug": s["slug"], "segment": s["segment"], "kind": "captured",
           "captured_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           **({"coverage_note": os.environ["PRISM_CAPTURE_COVERAGE"]} if os.environ.get("PRISM_CAPTURE_COVERAGE") else {}),
           "calls": out}
    return rec


def load_capture(slug: str) -> dict | None:
    p = CAPS / f"{slug}.json"
    return json.loads(p.read_text()) if p.exists() else None


def response(rec: dict, name: str) -> dict:
    """The `data` block of one named call, or {} when that call did not succeed."""
    for c in rec["calls"]:
        if c["name"] == name:
            r = c["response"]
            return (r.get("data") or {}) if c["status"] == 200 and r.get("ok") else {}
    return {}


def call_of(rec: dict, name: str) -> dict | None:
    return next((c for c in rec["calls"] if c["name"] == name), None)


def notes(rec: dict) -> list[str]:
    seen, out = set(), []
    for c in rec["calls"]:
        for n in (c["response"].get("meta") or {}).get("notes") or []:
            if n not in seen:
                seen.add(n)
                out.append(n)
    return out


# ── formatting ─────────────────────────────────────────────────────────────────
def n(x) -> str:
    return "—" if x is None else f"{x:,}" if isinstance(x, int) else f"{x:,.1f}"


def pct(x) -> str:
    return "—" if x is None else f"{x:.0f}%" if x >= 10 else f"{x:.1f}%"


def usd(x) -> str:
    if x is None:
        return "—"
    for div, suf in ((1e9, "B"), (1e6, "M"), (1e3, "k")):
        if abs(x) >= div:
            return f"${x / div:,.1f}{suf}".replace(f".0{suf}", suf)
    return f"${x:,.0f}"


def day(iso: str | None) -> str:
    return dt.date.fromisoformat(iso[:10]).strftime("%-d %b %Y") if iso else "—"


def month(iso: str) -> str:
    return dt.date.fromisoformat(iso[:10]).strftime("%b %Y")


def esc(s) -> str:
    """Make text safe inside a Markdown table cell."""
    s = " ".join(str(s or "").split())
    return s.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")


def trim(s, k: int) -> str:
    s = " ".join(str(s or "").split())
    return s if len(s) <= k else s[: k - 1].rsplit(" ", 1)[0] + "…"


def bar(value: float, top: float, width: int = 20) -> str:
    if not top or not value:
        return ""
    return "█" * max(1, round(width * value / top))


def table(head: list[str], rows: list[list], align: str | None = None) -> str:
    align = align or "l" * len(head)
    sep = ["---:" if a == "r" else "---" for a in align]
    lines = ["| " + " | ".join(head) + " |", "| " + " | ".join(sep) + " |"]
    lines += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def title_case(s: str) -> str:
    small = {"and", "or", "of", "in", "the", "for", "to", "vs"}
    acr = {"ai", "ev", "ipo", "gst", "rbi", "ecb", "gdp", "etf", "sip", "nbfc", "upi", "cbdc", "imf", "fii", "fdi",
           "sebi", "sec", "esg", "hiv", "rsv", "copd", "adhd", "pcos", "lng", "opec", "msp", "pli", "wto", "nep",
           "fssai", "fda", "cbam", "gdpr", "fmcg", "saas", "5g", "6g", "tsmc", "amd", "isro", "ibm", "tcs", "sbi",
           "itc", "hcl", "d2c", "a16z", "nea", "gv", "kkr", "tpg", "gic", "dcvc", "stv", "ma", "qip", "us", "eu",
           "covid", "h5n1", "glp-1", "crispr", "iot", "vr", "ar", "llm", "ceo", "cfo", "sme", "jp", "e-commerce"}
    words = s.split()
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        if lw == "s&p":
            out.append("S&P")
        elif lw in acr and lw != "e-commerce":
            out.append(lw.upper().replace("COVID", "COVID"))
        elif i and lw in small:
            out.append(lw)
        else:
            out.append(w[:1].upper() + w[1:])
    return " ".join(out)


def search_line(s: dict) -> str:
    """Search-demand line for the keyword a page targets."""
    k = s["keyword"]
    vol = []
    for loc, label in (("in", "India"), ("us", "US")):
        v = (k.get("volume") or {}).get(loc)
        if v:
            vol.append(f"{v:,}/month {label}")
    return f"“{k['phrase']}”" + (f" · {' · '.join(vol)}" if vol else " · volume below estimate threshold")


def coverage_line(rec: dict) -> str:
    base = f"Captured {day(rec['captured_at'])} from the live API"
    if rec.get("coverage_note"):
        return base + f" · {rec['coverage_note']}: counts are lower bounds"
    return base


def replace_section(text: str, section: str, start: str, end: str, anchor: str) -> str:
    if start in text:
        head, rest = text.split(start, 1)
        return head + section + rest.split(end, 1)[1]
    return text.replace(anchor, section + "\n\n" + anchor, 1) if anchor in text else section + "\n\n" + text


# ── checks (tests/test_scenarios.py) ──────────────────────────────────────────
def check() -> dict:
    """Every page exists, links resolve, and every number source is a saved capture."""
    plan = json.loads(PLAN.read_text())
    log = json.loads(LOG.read_text())
    pages = 0
    problems = []
    for seg in plan["segments"]:
        kept = [s for s in seg["scenarios"] if log.get(s["slug"], {}).get("kept")]
        if len(kept) < min(seg["target"], 40):
            problems.append(f"{seg['id']}: only {len(kept)} pages")
        for s in kept:
            page = SCEN / seg["id"] / f"{s['slug']}.md"
            cap = CAPS / f"{s['slug']}.json"
            if not page.exists() or not cap.exists():
                problems.append(f"missing {page.name} or capture")
                continue
            pages += 1
            text = page.read_text()
            for link in re.findall(r"\]\(([^)#\s]+)", text):
                if link.startswith("http"):
                    continue
                if not (page.parent / link).resolve().exists():
                    problems.append(f"{page.relative_to(ROOT)}: broken link {link}")
    if problems:
        raise AssertionError("\n".join(problems[:40]))
    return {"pages": pages, "segments": len(plan["segments"])}
