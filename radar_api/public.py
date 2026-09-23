"""Translate legacy response names; never return credentials or operational diagnostics."""
from __future__ import annotations

import re
from urllib.parse import urlsplit


def company_logo(domain):
    """Radar's first-party fallback route; it may serve a favicon when no logo exists."""
    if isinstance(domain, str) and re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,63}", domain):
        return "https://fliarbi.com/logos/by_domain.php?domain=" + domain
    return None


def safe_asset(key, value):
    if key in {"logo", "logo_url", "image_url", "photo_url"} and isinstance(value, str) and value.startswith("http"):
        try:
            host = urlsplit(value).hostname or ""
        except ValueError:
            return None
        if host != "fliarbi.com" and not host.endswith(".fliarbi.com"):
            return None
    return value

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
    "_extras_gated": "extras_gated", "_extras": "extras", "_entitlements": "access", "_results_capped": "results_capped",
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
            out[RENAMES.get(key, key)] = clean(safe_asset(key, item), depth + 1)
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
               "_no_data", "logo", "logo_url", "total_funding", "progress_label", "size_label", "funding",
               "_extras", "finalized_products", "products", "skills", "funded_as", "website_stacks", "webstack", "has_email", "has_phone"}
    out = clean({key: value[key] for key in allowed if key in value})
    sectors = value.get("sectors_object")
    if isinstance(sectors, list):
        sectors = sectors[0] if sectors else {}
    if isinstance(sectors, dict) and "0" in sectors:
        sectors = sectors["0"]
    if isinstance(sectors, dict):
        out["classification"] = {dest: clean(sectors[src]) for src, dest in (
            ("PRACTICE AREA", "sectors"), ("FEED", "markets"), ("BUSINESS MODEL", "business_models")) if src in sectors}
    if isinstance(value.get("data"), dict) and "sk" in value["data"]:
        out["skills"] = clean(value["data"]["sk"])
    out.pop("logo", None)
    out["logo_url"] = company_logo(out.get("domain"))
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
                     "currency_conversion": row.get("fx_source") or None,
                     "evidence": {"coverage_count": row.get("coverage_count"),
                                  "quality_signals": row.get("quality_signals"),
                                  "headline": row.get("headline"),
                                  "has_official": row.get("has_official"),
                                  "period_has_official": row.get("period_has_official")},
                     **({"operating_context": {"employees": row.get("employees"),
                             "revenue_growth_pct": row.get("revenue_growth_pct"),
                             "net_income_growth_pct": row.get("net_income_growth_pct"),
                             "guidance_revenue": row.get("guidance_revenue"),
                             "beat_or_miss": row.get("beat_or_miss")}}
                        if request.statement in {"all", "income"} else {})})
    rows.sort(key=lambda r: (r.get("fiscal_year") or 0, r.get("fiscal_period") or ""), reverse=True)
    return {
        "domain": request.domain, "statement": request.statement,
        "has_data": bool(rows), "periods": rows[:request.limit], "returned": min(len(rows), request.limit),
        "truncated": len(rows) > request.limit, "access_limited": bool(earnings.get("gated")),
        "available_period_count": earnings.get("history_total_count", len(earnings.get("history") or [])),
        "coverage": {"accessible_periods_before_filters": len(earnings.get("history") or []),
                     "matching_periods": len(rows),
                     "returned_periods_with_metrics": sum(bool(r["metrics"]) for r in rows[:request.limit]),
                     "requested_metrics": [f.removesuffix("_usd") for f in sorted(fields)],
                     "note": "Only entitled upstream periods are evaluated. A period can lack metrics for the selected statement; missing is not zero. Growth, guidance and evidence are source observations, not independently verified forecasts."},
        "computed_at": payload.get("computed_at"),
        "summary": {**{k: earnings[k] for k in ("latest_period", "prior_period", "revenue_yoy_pct", "net_income_yoy_pct", "narrative") if k in earnings},
                    "assessment": {k: earnings.get(k) for k in ("score", "growth_consistency", "yoy_pct", "yoy_multiple", "yoy_basis", "quality_signals_aggregate")},
                    "comparison_periods": {k: {p: (earnings.get(k) or {}).get(p) for p in ("period_label", "period_year", "period_qtr", "date")}
                                           for k in ("latest", "prior")},
                    "source_coverage": earnings.get("official_coverage"),
                    "note": "Summary assessments describe the upstream company window, not the filtered statement rows. Source coverage may count observations beyond the entitled archive. Guidance currency and horizon are not supplied; do not compare it with USD actuals without checking the article."},
    }
