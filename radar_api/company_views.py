"""Small company cards, bounded brief summaries, and explicit contact projections."""
from .errors import RadarError
from .public import company_card, clean, PRIVATE_VALUE, news_content


def compact_card(row):
    card = company_card(row)
    return {key: card.get(key) for key in ("name", "domain", "company_id", "description", "founded", "employee_count", "logo_url")}


def brief_section(name, result):
    d = result["data"] or {}
    if name == "get_company":
        return result
    if name == "get_financials":
        d = {**{k: d[k] for k in ("domain", "has_data", "summary", "access_limited", "available_period_count", "computed_at") if k in d},
             "latest_period": next(iter(d.get("periods", [])), None), "detail_required_for_history": True}
    elif name == "get_company_intelligence":
        intel = d.get("intel", {})
        d = {"domain": d.get("domain"), "computed_at": d.get("computed_at"), "assessments": {
            key: {k: value[k] for k in ("score", "label", "grade", "level") if k in value}
            for key, value in intel.items() if isinstance(value, dict) and key in {
                "innovation_index", "investment_readiness", "management_quality", "market_position", "risk_profile"}},
            "detail_required_for_analysis": True}
    elif name == "get_company_enrichment":
        d = {"domain": d.get("domain"), "has_data": d.get("has_data"),
             "available_fields": [key for key in ("activity", "digital", "hiring", "innovation", "legal", "reputation", "social", "sov") if d.get(key) is not None],
             "detail_required": True}
    elif name == "get_company_funding":
        d = {**{key: d[key] for key in ("amount_approx", "stages") if key in d},
             "returned_round_count": len(d.get("rounds", [])), "returned_event_count": len(d.get("events", [])),
             "returned_investor_count": len(d.get("investors", [])), "detail_required_for_records": True}
    elif name == "get_company_events":
        d = {**{key: d[key] for key in ("domain", "freshness", "truncated", "window_days", "totals_by_type") if key in d},
             "returned_event_count": len(d.get("events", [])), "detail_required_for_records": True}
    else:
        d = {"items": [{key: item[key] for key in ("id", "article_id", "headline", "title", "url", "published_at", "datetime", "date", "source") if key in item}
                       for item in d.get("items", [])[:5]], "detail_required_for_full_articles": True}
        return {**result, "data": news_content(d)}
    return {**result, "data": clean(d)}


def contacts_payload(name, request, source):
    is_person = name == "get_person_contacts"
    row = source.get("contacts", {}).get(request.person_id, source) if is_person else source
    if not isinstance(row, dict) or not any(key in row for key in ("emails", "phones")):
        raise RadarError("invalid_upstream_response", "The contact service returned no usable contact response", 502)
    values = {}
    for key in dict.fromkeys(request.fields):
        raw = row.get(key, [])
        if not isinstance(raw, list):
            raise RadarError("invalid_upstream_response", "The contact service returned an invalid field", 502)
        values[key] = list(dict.fromkeys(v.strip() for v in raw if isinstance(v, str) and v.strip() and not PRIVATE_VALUE.search(v)))[:25]
    origin = row.get("source", "none") if is_person else "company_domain"
    if origin not in {"person", "company_domain", "none"}:
        origin = "unknown"
    return {("person_id" if is_person else "domain"): request.person_id if is_person else request.domain,
            **values, "contact_source": origin, "available": any(values.values()),
            "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."}
