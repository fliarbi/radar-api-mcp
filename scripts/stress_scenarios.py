#!/usr/bin/env python3
"""Read-only scenario audit: bounded concurrency, honest limits, no fabricated passes."""

import argparse
import asyncio
from dataclasses import replace
from datetime import datetime, timezone
import json
import logging
from pathlib import Path
import time
import httpx
from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.service import BY_NAME
from radar_api.models import Envelope
from radar_api.upstream import Upstream
from contextlib import AsyncExitStack
from scenario_cases import CASES
from audit_examples import content_check

ROOT = Path(__file__).resolve().parents[1]


def assess(case, status, response):
    data = response.get("data") or {}
    problems = []
    if status != 200:
        return {
            "outcome": "unavailable",
            "findings": [response.get("error", {}).get("kind", "HTTP " + str(status))],
        }
    Envelope.model_validate(response)
    if response.get("feature") != case["operation"]:
        problems.append("Response operation differs from request")
    filters = case["request"].get("filters", {})
    # Only the fixed country scenarios are asserted here; city/radius semantics differ.
    countries = [v.casefold() for v in filters.get("locations", []) if v in ("India", "United States")]
    company_data = data.get("discovery") or data
    for company in company_data.get("companies", []):
        country = (company.get("location") or {}).get("c", "").casefold()
        if countries and country and country not in countries:
            problems.append("Company country violates requested location: " + company.get("domain", "unknown"))
        year = str(company.get("founded") or "")
        if year.isdigit() and (filters.get("founded_year_from", 0) > int(year) or filters.get("founded_year_to", 9999) < int(year)):
            problems.append("Company founding year violates requested range")
    for check in case["checks"]:
        if check == "adtech_option" and "AdTech" not in data.get("options", []):
            problems.append("AdTech is a valid source industry but suggestion lookup did not return it")
        if check == "financial_catalog" and not data.get("numeric_screen"):
            problems.append("Precise screen definitions missing")
        if check == "financial_screen":
            if not data.get("coverage") or "evaluated" not in data:
                problems.append("Missing evidence or bounded-screen coverage")
            for row in data.get("matches", []):
                for criterion in case["request"]["constraints"]:
                    metric = row.get("period", {}).get("metrics", {}).get(criterion["metric"]) or {}
                    v = metric.get("value")
                    if v is None or metric.get("currency") != "USD":
                        problems.append("Match lacks numeric USD evidence")
                        continue
                    for op in ("lt", "lte", "gt", "gte"):
                        if (
                            op in criterion
                            and not {
                                "lt": v < criterion[op],
                                "lte": v <= criterion[op],
                                "gt": v > criterion[op],
                                "gte": v >= criterion[op],
                            }[op]
                        ):
                            problems.append("Financial match violates " + op)
        if check == "financial_periods":
            r = case["request"]
            for p in data.get("periods", []):
                if r["period_type"] == "annual" and p["fiscal_period"] != "FY":
                    problems.append("Quarter mixed into annual request")
                if r["period_type"] == "quarterly" and p["fiscal_period"] not in ("Q1", "Q2", "Q3", "Q4"):
                    problems.append("Nonquarterly record returned")
                if r.get("year_from") and p["fiscal_year"] < r["year_from"]:
                    problems.append("Year below bound")
                if r.get("year_to") and p["fiscal_year"] > r["year_to"]:
                    problems.append("Year above bound")
        if check == "team":
            if "coverage" not in data:
                problems.append("Team coverage missing")
            if case["request"]["group"] == "professionals":
                for person in data.get("people", []):
                    if (
                        person.get("current_company_domain", "").lower().removeprefix("www.")
                        != case["request"]["domain"]
                    ):
                        problems.append("Wrong company affiliation admitted")
        if check == "app_filters":
            for app in data.get("apps", []):
                if (
                    app.get("installs", 0) < 1000000
                    or (app.get("rating") or 0) < 4
                    or app.get("category") != "Food & Drink"
                ):
                    problems.append("App violates requested predicate")
        if check == "app_domain":
            from urllib.parse import urlsplit

            for app in data.get("apps", []):
                if (urlsplit(app["developer_website"]).hostname or "").removeprefix("www.") != case["request"]["domain"]:
                    problems.append("Wrong app host")
        if check == "internship":
            for row in data.get("internships", []):
                if row.get("current_opening_verified") is not False:
                    problems.append("Vacancy verification invented")
                if (
                    case["request"].get("work_mode") == "remote"
                    and row.get("work_mode") != "remote_indicated"
                ):
                    problems.append("Remote evidence missing")
                if (
                    case["request"].get("stipend_min")
                    and (row["stipend"]["value"] or 0) < case["request"]["stipend_min"]
                ):
                    problems.append("Stipend below threshold")
    if problems:
        return {"outcome": "failed", "findings": problems}
    notes = []
    op = case["operation"]
    content = content_check(op, case["request"], status, response)
    if content["state"] == "empty":
        notes.append("Empty documentation example: " + content["reason"])
    if op == "get_company_field" and data.get("field") != case["request"]["field"]:
        return {"outcome": "failed", "findings": ["Wrong company field returned"]}
    if op == "get_app_field" and (data.get("field") != case["request"]["field"] or data.get("app_id") != case["request"]["app_id"]):
        return {"outcome": "failed", "findings": ["Wrong app or field returned"]}
    if op == "search_companies" and any(filters.get(k) for k in ("revenue_bands", "revenue_growth", "profitability", "deal_sizes", "revenue_models")):
        notes.append("Source-labelled predicates; cards do not independently verify financial/classification conditions")
    if op in {"search_people", "get_company_team"}:
        notes.append("Recorded professional or key-person data; current roles and complete resumes are unverified")
    if op in {"company_apps", "search_apps", "get_app_field"}:
        notes.append("Dated store observations, not a live store check; history can contain duplicate rows")
    if op in {"search_internships", "companies_offering_internships"}:
        notes.append("Observed internship listings; current vacancies unverified, deadlines can be expired")
    if op == "get_investor_field":
        notes.append("Dated published research snapshot; not current investment activity")
    access = data.get("access") or {}
    if response.get("meta", {}).get("partial") or data.get("partial_timeout"):
        notes.append("Partial result or source timeout")
    if (data.get("matching") or {}).get("excluded_candidates"):
        notes.append("Expanded or unverified source candidates were excluded")
    if access.get("restricted_filters"):
        notes.append("Source restricted requested filters")
    if data.get("access_limited"):
        notes.append("Financial history is source-plan limited")
    if data.get("coverage", {}).get("complete") is False:
        notes.append("Coverage is explicitly bounded")
    arrays = [
        data[k]
        for k in ("companies", "people", "periods", "internships", "apps", "items", "matches", "options", "jobs", "events")
        if isinstance(data.get(k), list)
    ]
    if arrays and not any(arrays):
        notes.append("No rows observed; not proof of a complete negative")
    if data.get("has_data") is False:
        notes.append("No accessible data")
    return {
        "outcome": "qualified" if notes else "observed",
        "findings": notes
        or [
            "Response contract and declared scenario checks passed; source truth not independently certified"
        ],
    }


async def run(args):
    logging.getLogger("httpx").setLevel(logging.WARNING)
    settings = replace(Settings.from_env(), allowed_hosts=("capture.local",), timeout_seconds=20)
    key = (ROOT / "secrets/client-key.txt").read_text().strip()
    stack = AsyncExitStack()
    transport = None
    if args.news_integration:
        from live_news_context import connect

        settings, transport = await stack.enter_async_context(connect(settings))
    app = create_app(settings, Upstream(settings, transport))
    report = {
        "round": args.round,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "concurrency": 2,
        "scope": "50 fixed semantic/business scenarios; bounded read load, not a production capacity benchmark",
        "results": [],
    }
    target = ROOT / "qa/private" / ("scenarios-" + args.round + ".json")

    def save():
        target.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
        target.chmod(0o600)

    sem = asyncio.Semaphore(2)
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app, raise_app_exceptions=False), base_url="http://capture.local", headers={"X-API-Key": key}
    ) as client:

        async def one(case):
            async with sem:
                started = time.monotonic()
                feature = BY_NAME.get(case["operation"])
                if feature is None:
                    status, response = 404, {"ok": False, "error": {"kind": "not_implemented"}}
                    path = None
                else:
                    path = "/v1/" + feature.path
                    try:
                        async with asyncio.timeout(90):
                            r = await client.post(path, json=case["request"])
                            status = r.status_code
                            try:
                                response = r.json()
                            except ValueError:
                                response = {"ok": False, "error": {"kind": "invalid_gateway_response"}}
                    except TimeoutError:
                        status, response = 504, {"ok": False, "error": {"kind": "audit_timeout"}}
                record = {
                    **case,
                    "path": path,
                    "http_status": status,
                    "response": response,
                    "elapsed_seconds": round(time.monotonic() - started, 3),
                    "captured_at": datetime.now(timezone.utc).isoformat(),
                    "capture_kind": "live_data_integration"
                    if args.news_integration and case["operation"] == "search_business_news"
                    else "live_gateway",
                    "assessment": assess(case, status, response),
                }
                guide = ROOT / "docs/guides" / (case["guide"] + ".md")
                record["documentation"] = {
                    "guide_exists": guide.exists(),
                    "scenario_linked": guide.exists() and case["id"] in guide.read_text(),
                }
                report["results"].append(record)
                report["results"].sort(key=lambda x: x["id"])
                save()
                print(case["id"], status, record["assessment"]["outcome"], flush=True)

        await asyncio.gather(*(one(c) for c in CASES if not args.only or c["id"] in args.only))
    if app.state.service.profiles:
        app.state.service.profiles.close()
    if app.state.service.internships:
        app.state.service.internships.close()
    await stack.aclose()
    report["finished_at"] = datetime.now(timezone.utc).isoformat()
    save()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--round", required=True)
    p.add_argument("--only", nargs="+")
    p.add_argument("--news-integration", action="store_true")
    asyncio.run(run(p.parse_args()))
