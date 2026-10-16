#!/usr/bin/env python3
"""Turn the keyword research into docs/use-cases/plan.json: per segment, candidate pages
in search-demand order, each with the exact (validated) Radar API calls behind it.
scripts/capture_scenarios.py keeps the first `target` populated ones."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import scenario_common as sc  # noqa: E402
from radar_api.service import BY_NAME  # noqa: E402

RESEARCH_FILE = sc.RESEARCH / "keyword-research-2026-10-16.json"
TARGET = 50
WINDOW = {"date_from": "2026-01-01", "date_to": "2026-04-30"}
YEAR = {"date_from": "2025-05-01", "date_to": "2026-04-30"}
PATH = {name: "/v1/" + f.path for name, f in BY_NAME.items()}


def op(name: str, label: str, body: dict) -> dict:
    BY_NAME[name].model.model_validate(body)
    return {"name": label, "feature": name, "method": "POST", "path": PATH[name], "body": body}


def recipe(seg: str, t: dict) -> tuple[list[dict], dict]:
    if seg == "financial-news":
        q = t["q"]
        return [op("news_overview", "overview", {"q": q, **WINDOW}),
                op("news_trends", "trends", {"q": q, **YEAR, "granularity": "monthly"}),
                op("news_sentiment", "sentiment", {"q": q, **WINDOW, "granularity": "monthly"}),
                op("search_business_news", "headlines", {"q": q, **WINDOW, "priority_min": 6, "sort": "priority", "limit": 25})], \
            {"call": "overview", "field": "matched", "min": 60}
    if seg == "company-financials":
        d = t["domain"]
        return [op("get_financials", "financials", {"domain": d, "statement": "all", "period_type": "all", "limit": 8}),
                op("get_company_funding", "funding", {"domain": d}),
                op("news_overview", "news", {"company": d, **WINDOW})], \
            {"call": "financials", "field": "periods", "min": 1}
    if seg == "industry-companies":
        return [op("search_companies", "companies", {"filters": {"industries": [t["industry"]], "locations": ["India"]}, "limit": 20}),
                op("find_competitors", "competitors", {"market": t["topic"], "per_stage": 3})], \
            {"call": "companies", "field": "companies", "min": 5}
    d = t["domain"]
    return [op("get_company_team", "founders", {"domain": d, "group": "founders"}),
            op("get_company_team", "key_people", {"domain": d, "group": "key_people"}),
            op("get_company", "profile", {"domain": d})], \
        {"call": "founders", "field": "people", "min": 1}


def main() -> None:
    research = json.loads(RESEARCH_FILE.read_text())
    segments = []
    for seg in research["segments"]:
        scen = []
        for t in seg["topics"]:
            if t.get("excluded"):
                continue
            calls, primary = recipe(seg["id"], t)
            scen.append({"slug": sc.slugify(t["target"]["phrase"]), "segment": seg["id"], "topic": t["topic"],
                         "keyword": t["target"], "score": t["score"], "calls": calls, "primary": primary,
                         **{k: t[k] for k in ("q", "domain", "industry") if k in t}})
        segments.append({"id": seg["id"], "title": seg["title"], "target": TARGET, "scenarios": scen})
    sc.SCEN.mkdir(parents=True, exist_ok=True)
    sc.PLAN.write_text(json.dumps({"window": WINDOW, "year": YEAR, "research": RESEARCH_FILE.name,
                                   "segments": segments}, indent=1, ensure_ascii=False) + "\n")
    print({s["id"]: len(s["scenarios"]) for s in segments})


if __name__ == "__main__":
    main()
