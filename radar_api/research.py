"""Bounded evidence workflows over existing entitled Radar operations."""

from __future__ import annotations
import asyncio
from collections import Counter
import math
from . import models as m
from .errors import RadarError
from .public import clean


def financial_catalog():
    return {
        "currency": "USD",
        "numeric_screen": m.FinancialScreen.model_json_schema(),
        "period_selection": "Latest accessible period of the requested annual/quarterly type and year window. All constraints use the same period. Never fall back to an older period to manufacture a match.",
        "revenue_bands": {
            "under1m": "0 < revenue < 1000000",
            "1m-10m": "1000000 < revenue < 10000000",
            "10m-100m": "10000000 < revenue < 100000000",
            "100m-1b": "100000000 < revenue < 1000000000",
            "1b+": "revenue > 1000000000",
        },
        "source_band_boundary_note": "Radar legacy bands exclude exact boundary values and zero. They refer to source financial summary fields, not a selected fiscal period.",
        "growth_bands_pct": {
            "declining": "<0",
            "flat": ">=0 and <10",
            "growing": ">=10 and <30",
            "high": ">=30 and <100",
            "hyper": ">=100",
        },
        "profitability": {"profitable": "net profit > 0", "loss": "net profit < 0"},
        "distinctions": [
            "Revenue models describe how a business earns money.",
            "Deal-size filters select funding rounds, not revenue.",
            "Display columns and estimated-revenue sorts are not verified financial statements.",
            "Unknown financial values do not satisfy a numeric filter, including zero.",
        ],
        "billing": "Reserve 1 + candidate_limit credits (or 1 + number of domains); settle one screen credit plus successful financial reads. Unused/failed reads are refunded.",
        "coverage": {"complete": False, "note": "A bounded screen over a source candidate page or explicit domains, not an exhaustive database-wide financial query. Source gates remain authoritative."},
    }


def evaluate_financials(data, request):
    if not data.get("periods"):
        return {
            "status": "unknown",
            "reason": "No accessible period matches the requested type/year window",
            "period": None,
            "checks": [],
        }
    period = data["periods"][0]
    checks = []
    for criterion in request.constraints:
        metric = period.get("metrics", {}).get(criterion.metric) or {}
        value = metric.get("value")
        known = (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
            and math.isfinite(value)
            and metric.get("currency") == "USD"
        )
        qualified = request.source_type == "any" or metric.get("source_type") == request.source_type
        if not known or not qualified:
            checks.append(
                {
                    "metric": criterion.metric,
                    "status": "unknown",
                    "reason": "Missing/non-numeric USD value or disallowed source type",
                }
            )
            continue
        bounds = criterion.model_dump(exclude_none=True, exclude={"metric"})
        matches = all(
            {"gt": value > b, "gte": value >= b, "lt": value < b, "lte": value <= b}[op]
            for op, b in bounds.items()
        )
        checks.append(
            {
                "metric": criterion.metric,
                "status": "matched" if matches else "not_matched",
                "value": value,
                "currency": "USD",
                "bounds": bounds,
                "source_type": metric.get("source_type"),
            }
        )
    status = (
        "not_matched"
        if any(x["status"] == "not_matched" for x in checks)
        else "unknown"
        if any(x["status"] == "unknown" for x in checks)
        else "matched"
    )
    return {"status": status, "period": period, "checks": checks}


async def screen(service, request):
    discovery = None
    if request.domains:
        candidates = [{"domain": d} for d in request.domains]
    else:
        discovery = await service.dispatch(
            "search_companies",
            m.SearchCompanies(filters=request.filters, page=request.page, limit=request.candidate_limit),
        )
        candidates = discovery["companies"]
    # Source duplicates must not multiply charges or measurements.
    unique = {row["domain"]: row for row in candidates if row.get("domain")}
    sem = asyncio.Semaphore(3)

    async def one(domain, company):
        async with sem:
            try:
                async with asyncio.timeout(25):
                    data = await service.dispatch(
                        "get_financials",
                        m.Financials(
                            domain=domain,
                            period_type=request.period_type,
                            year_from=request.year_from,
                            year_to=request.year_to,
                            limit=1,
                        ),
                    )
                return {
                    "domain": domain,
                    "company": company,
                    **evaluate_financials(data, request),
                    "access_limited": data.get("access_limited", False),
                    "successful_read": True,
                }
            except (RadarError, TimeoutError) as exc:
                return {
                    "domain": domain,
                    "company": company,
                    "status": "unavailable",
                    "error": getattr(exc, "kind", "upstream_timeout"),
                    "successful_read": False,
                }

    rows = await asyncio.gather(*(one(d, c) for d, c in unique.items()))
    counts = dict(Counter(row["status"] for row in rows))
    partial = any(row["status"] in {"unknown", "unavailable"} or row.get("access_limited") for row in rows)
    access = (discovery or {}).get("access", {})
    partial = partial or bool((discovery or {}).get("partial_timeout") or access.get("restricted_filters"))
    return {
        "matches": [row for row in rows if row["status"] == "matched"],
        "evaluated": rows,
        "counts": counts,
        "constraints": [x.model_dump(exclude_none=True) for x in request.constraints],
        "period_type": request.period_type,
        "source_type": request.source_type,
        "discovery": discovery,
        "next_page": request.page + 1 if not request.domains and (discovery or {}).get("matching", {}).get("source_rows", len(candidates)) and request.page < 200 else None,
        "coverage": {
            "complete": False,
            "partial": partial,
            "candidate_count": len(unique),
            "company_filters_independently_verified": False,
            "note": "Numeric matches are verified against returned dated metrics. Candidate company classification/geography remains source-filtered; inspect source access and matching. Empty matches do not mean there are no matching companies elsewhere.",
        },
        "successful_financial_reads": sum(row["successful_read"] for row in rows),
    }


async def team(service, request):
    if request.group == "professionals":
        source = await service.dispatch(
            "search_people",
            m.People(
                companies=[request.domain],
                roles=request.roles,
                skills=request.skills,
                min_experience_years=request.min_experience_years,
                min_seniority=request.min_seniority,
                page=request.page,
                limit=request.limit,
            ),
        )
        raw = source.get("people") or []
        rows = [
            p
            for p in raw
            if str(p.get("current_company_domain") or "").lower().removeprefix("www.") == request.domain
        ]
        partial = bool(source.get("partial_timeout") or len(raw) != len(rows))
        return {
            "domain": request.domain,
            "group": request.group,
            "people": clean(rows),
            "returned": len(rows),
            "page": request.page,
            "next_page": request.page + 1 if raw and request.page < 200 else None,
            "source_candidates": len(raw),
            "excluded_unverified_affiliations": len(raw) - len(rows),
            "access": clean(source.get("access") or {}),
            "coverage": {
                "complete": False,
                "partial": partial,
                "affiliation": "Exact recorded current-company domain; not independently verified current employment",
                "note": "Search cards contain bounded skills, education and experience summaries. Page totals are not company headcount.",
            },
        }
    if not service.profiles:
        raise RadarError("service_unavailable", "Company team records are not connected", 503)
    data = await service.profiles.get(m.CompanyField(domain=request.domain, field="people", item_limit=100))
    rows = (data.get("value") or {}).get(request.group) or []
    if request.title:
        rows = [
            p
            for p in rows
            if request.title.casefold() in str(p.get("designation") or p.get("title") or "").casefold()
        ]
    start = request.page * request.limit
    return {
        "domain": request.domain,
        "group": request.group,
        "people": rows[start : start + request.limit],
        "returned": len(rows[start : start + request.limit]),
        "matched_observed_rows": len(rows),
        "page": request.page,
        "next_page": request.page + 1 if start + request.limit < len(rows) else None,
        "updated_at": data.get("updated_at"),
        "coverage": {
            "complete": False,
            "partial": data.get("coverage", {}).get("partial", False),
            "source_status": data.get("status"),
            "note": "Company key-person records, not a full employee roster or verified headcount. Founders are selected by recorded designation; no contacts are included.",
        },
    }
