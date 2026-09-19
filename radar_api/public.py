"""Translate legacy response names; never return credentials or operational diagnostics."""
from __future__ import annotations

import re

PRIVATE = {
    "auth_sign", "uuid", "token", "password", "secret", "api_key", "news_key", "radar_token",
    "sql", "query_sql", "query_plan", "where", "where_condition", "table", "tables", "database",
    "traceback", "debug", "cache_key", "cache_state", "ttl_at", "file_id", "g_id", "data_src",
    "basicwdata_id", "bwd", "raw", "query_diagnostics", "diagnostics", "computation_version",
    "entity_resolution", "source_corpus", "collection", "host", "port", "credentials",
    "email", "emails", "phone", "phones", "mobile", "contact_info", "contact_infox",
    "contact_emails", "contact_phones", "raw_data", "details", "detail_error", "backend",
}
RENAMES = {
    "w": "domain", "short_d": "description", "desc": "description", "idx": "company_id", "li_p": "linkedin_slug",
    "name_code": "slug", "loc": "location", "_no_data": "no_data", "_plan": "plan",
    "_extras_gated": "extras_gated", "_entitlements": "access", "_results_capped": "results_capped",
    "_stripped_filters": "restricted_filters", "_searches_remaining": "searches_remaining",
    "_truncated": "truncated", "_data_freshness": "freshness", "_retrospective_likely": "retrospective_likely",
    "_partial_timeout": "partial_timeout", "_total_capped": "total_capped", "_page": "page",
    "_page_size": "page_size", "_location_relaxed": "location_relaxed", "_location_scope": "location_scope",
    "target_id": "article_id", "source_target_ids": "article_ids", "event_id": "article_id",
    "trending_feeds": "trending_markets", "feed": "market", "sub_category": "markets",
    "subcats": "topics", "feeds": "markets", "ai_ind": "industries", "clf": "sectors",
    "primary_source": "source_type", "field_sources": "metric_sources",
}
PRIVATE_VALUE = re.compile(r"(?:/home/|/mnt/|mongodb://|redis://|Traceback \(|SELECT .+ FROM |192\.168\.|127\.0\.0\.1|10\.\d+\.\d+\.\d+)", re.I)


def clean(value, depth=0):
    if depth > 35:
        return None
    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            if key.lower() in PRIVATE or key.startswith("_") and key not in RENAMES:
                continue
            if key == "primary_source":
                item = SOURCE_NAMES.get(item, "unspecified")
            elif key == "field_sources" and isinstance(item, dict):
                item = {k: SOURCE_NAMES.get(v, "unspecified") for k, v in item.items()}
            out[RENAMES.get(key, key)] = clean(item, depth + 1)
        return out
    if isinstance(value, list):
        return [clean(item, depth + 1) for item in value]
    if isinstance(value, str):
        if PRIVATE_VALUE.search(value):
            return None
        return value
    return value


def news_content(value):
    """The News service already sanitizes its public contract; preserve quoted evidence verbatim."""
    evidence_fields = {"text", "content", "body", "headline", "title", "description", "full_text"}
    if isinstance(value, dict):
        return {RENAMES.get(k, k): (v if k in evidence_fields and isinstance(v, str) else news_content(v))
                for k, v in value.items() if k.lower() not in PRIVATE and not k.startswith("_")}
    if isinstance(value, list):
        return [news_content(v) for v in value]
    return clean(value)


def company_card(value: dict):
    allowed = {"name", "w", "domain", "short_d", "description", "desc", "tagline", "li_p", "founded", "size",
               "hq", "loc", "idx", "name_code", "flags", "extras", "sectors", "industries",
               "_no_data", "logo", "logo_url", "total_funding", "progress_label", "size_label", "funding"}
    out = clean({key: value[key] for key in allowed if key in value})
    sectors = value.get("sectors_object")
    if isinstance(sectors, dict):
        out["classification"] = {dest: clean(sectors[src]) for src, dest in (
            ("PRACTICE AREA", "sectors"), ("FEED", "markets"), ("BUSINESS MODEL", "business_models")) if src in sectors}
    return out


SOURCE_NAMES = {"official": "filing", "bi": "news_report"}
STATEMENTS = {
    "income": ("revenue_usd", "gross_profit_usd", "operating_income_usd", "net_income_usd", "ebitda_usd", "eps"),
    "balance_sheet": ("total_assets_usd", "total_liabilities_usd", "stockholders_equity_usd", "cash_usd", "long_term_debt_usd"),
    "cash_flow": ("operating_cash_flow_usd", "investing_cash_flow_usd", "financing_cash_flow_usd", "free_cash_flow_usd", "capex_usd"),
}


def financial_data(payload: dict, request):
    earnings = payload.get("intel", {}).get("earnings", {})
    fields = set(STATEMENTS[request.statement]) if request.statement != "all" else set(sum(STATEMENTS.values(), ()))
    rows = []
    for row in earnings.get("history") or []:
        if not isinstance(row, dict):
            continue
        year, quarter = row.get("period_year"), row.get("period_qtr")
        if request.year_from and (not isinstance(year, int) or year < request.year_from):
            continue
        if request.year_to and (not isinstance(year, int) or year > request.year_to):
            continue
        if request.period_type == "annual" and quarter != "FY":
            continue
        if request.period_type == "quarterly" and quarter not in {"Q1", "Q2", "Q3", "Q4"}:
            continue
        metrics = {}
        for field in sorted(fields):
            number = row.get(field)
            if number is None:
                continue
            source = (row.get("field_sources") or {}).get(field, row.get("primary_source"))
            currency = "USD" if field.endswith("_usd") else None
            metrics[field.removesuffix("_usd")] = {
                "value": number, "currency": currency, "unit": "per_share" if field == "eps" else "absolute",
                "source_type": SOURCE_NAMES.get(source, "unspecified"),
                "native_value": (row.get("native") or {}).get(field),
                "native_currency": row.get("currency_native") or None,
            }
        rows.append({"period": row.get("period_label"), "fiscal_year": year, "fiscal_period": quarter,
                     "period_end": row.get("period_end"), "reported_date": row.get("date"),
                     "filed_date": row.get("filed_date"), "form_type": row.get("form_type") or None,
                     "metrics": metrics, "article_ids": row.get("source_target_ids") or [],
                     "currency_conversion": row.get("fx_source") or None})
    rows.sort(key=lambda r: (r.get("fiscal_year") or 0, r.get("fiscal_period") or ""), reverse=True)
    return {
        "domain": request.domain, "statement": request.statement,
        "has_data": bool(rows), "periods": rows[:request.limit], "returned": min(len(rows), request.limit),
        "truncated": len(rows) > request.limit, "access_limited": bool(earnings.get("gated")),
        "available_period_count": earnings.get("history_total_count", len(earnings.get("history") or [])),
        "computed_at": payload.get("computed_at"),
        "summary": {k: earnings[k] for k in ("latest_period", "prior_period", "revenue_yoy_pct", "net_income_yoy_pct", "narrative") if k in earnings},
    }
