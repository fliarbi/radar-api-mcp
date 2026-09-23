"""Read verified Atlas business data after the live publication gate succeeds.

The configured directory is an immutable release containing meta/ and data/.
Private social/contact fields are excluded even though they exist in the source.
No arbitrary files, SQL, unpublished pages, or raw snapshots can be requested.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
from pathlib import Path

from .errors import RadarError
from .public import clean, company_logo

PROFILE_FIELDS = {
    "portfolio": "companies", "undated_portfolio": "undated_companies", "sectors": "sectors",
    "stages": "stages", "activity": "years", "follow_on": "cohort", "co_investors": "co_investors",
    "news": "editorial", "analysis": "readout", "related": "related",
}
DIRECTORY_FIELDS = {
    "investors": "investors", "stages": "stages", "activity": "years", "recent_rounds": "recent_rounds",
    "themes": "theme_intelligence", "research": "research", "geography": "shortlist_location", "related": "related",
    "selection": "shortlist_rule",
}
PROFILE_METRICS = (
    "total_companies", "total_rounds", "portfolio_count", "round_count", "early_entries", "early_pct",
    "entry_round_size", "recent_entries", "previous_entries", "repeat_companies", "lead_entries", "lead_pct", "syndicate_median",
)
DEFINITIONS = {
    "portfolio": "Dated equity investments; undated companies are retrieved separately. Debt and grants are excluded.",
    "amounts": "USD whole-round amounts, not the investor's cheque, fund size, assets under management or investment returns.",
    "follow_on": "Another investor's later financing and this investor's repeat backing are distinct. Only entries with a full 24-month observation window enter the cohort.",
    "sectors": "Historical company tags can overlap; their counts are not additive and do not establish a current investment mandate.",
    "directory": "A directory's stored shortlist is a selected subset of its measured investor universe, not every investor in the database.",
}
RESTRICTED = {"linkedin", "linkedin_url", "linkedin_preview", "id", "investor_id", "company_oid", "auth_sign"}


def business_data(value):
    """Keep the business schema intact; remove private identity/reveal fields recursively."""
    if isinstance(value, dict):
        out = {k: business_data(v) for k, v in value.items() if k not in RESTRICTED}
        domain = value.get("domain")
        if domain and "logo_url" in out:
            out["logo_url"] = company_logo(domain)
        return clean(out)
    if isinstance(value, list):
        return [business_data(v) for v in value]
    if isinstance(value, str) and ("linkedin.com/" in value.lower() or value.startswith("mailto:")):
        return None
    return value


def fields_for(meta):
    return PROFILE_FIELDS if meta["kind"] == "investor_profile" else DIRECTORY_FIELDS


def field_value(data, name, key):
    if name == "geography":
        value = {"headquarters": data.get("shortlist_location"), "localities": data.get("shortlist_localities")}
    elif name == "selection":
        value = {"rule": data.get("shortlist_rule"), "breadth": data.get("breadth")}
    else:
        return data.get(key)
    return value if any(v is not None for v in value.values()) else None


def matches(row, request):
    if request.q and request.q.casefold() not in " ".join(str(row.get(k) or "") for k in ("name", "domain", "description")).casefold():
        return False
    for key in ("city", "country", "kind"):
        value = getattr(request, key)
        if value and str(row.get(key) or "").casefold() != value.casefold():
            return False
    if request.sector and request.sector.casefold() not in {str(x).casefold() for x in row.get("sectors", [])}:
        return False
    if request.stage:
        stages = [row["stage"]] if "stage" in row else list(row.get("stages") or {})
        if request.stage.casefold() not in {str(x).casefold() for x in stages}:
            return False
    return True


class InvestorStore:
    def __init__(self, settings):
        self.root = Path(settings.investor_data_dir).resolve()
        self.max_bytes = settings.max_response_bytes

    async def get(self, request, gate):
        # The gate must be requested anew, using the caller's authenticated gateway path.
        if gate.get("slug") != request.slug or gate.get("family") not in {"investor", "investors", "angel_investors"}:
            raise RadarError("invalid_upstream_response", "Investor publication metadata is incomplete", 502)
        return await asyncio.to_thread(self._get, request, gate)

    def read(self, directory, slug, cap):
        path = self.root / directory / (slug + ".json")
        if not path.resolve().is_relative_to(self.root):
            raise RadarError("service_unavailable", "Investor release path is invalid", 503)
        with path.open("rb") as handle:
            value = handle.read(cap + 1)
        if len(value) > cap:
            raise RadarError("response_too_large", "The investor release exceeds the configured size limit", 502)
        return value

    def _get(self, request, gate):
        try:
            meta = json.loads(self.read("meta", request.slug, 65536))
            if (meta.get("status") != "built" or meta.get("slug") != request.slug
                    or meta.get("family") != gate["family"] or meta.get("kind") != gate.get("kind")):
                raise RadarError("no_data", "No verified investor data matches this published page", 404)
            raw = self.read("data", request.slug, self.max_bytes)
            if hashlib.sha256(raw).hexdigest() != meta.get("data_sha256"):
                raise RadarError("service_unavailable", "Investor release integrity check failed", 503)
            data = json.loads(raw)
            if data.get("slug") != request.slug:
                raise RadarError("service_unavailable", "Investor release identity check failed", 503)
        except FileNotFoundError:
            raise RadarError("service_unavailable", "Verified data for this investor page is not connected", 503) from None
        except (OSError, ValueError, TypeError, AttributeError):
            raise RadarError("service_unavailable", "Investor data could not be read", 503) from None
        mapping = fields_for(meta)
        common = {"slug": request.slug, "kind": meta["kind"], "family": meta["family"],
                  "coverage": {"data_through": data.get("coverage_end"), "computed_on": data.get("computed_on"),
                               "last_investment": data.get("last_investment", data.get("last_market_round")),
                               "first_investment": data.get("first_investment"),
                               "recent_window_start": data.get("window_start"), "previous_window_start": data.get("previous_start"),
                               "release": self.root.name, "snapshot_sha256": meta["data_sha256"],
                               "partial": False, "source": "verified_published_atlas_snapshot"}}
        if hasattr(request, "field"):
            if request.field not in mapping:
                raise RadarError("invalid_request", "This field is not available for this page kind; inspect available_fields", 422)
            filters = [request.q, request.sector, request.stage, request.city, request.country, request.kind]
            if (any(filters) or request.sort_by != "source") and request.field not in {"portfolio", "investors"}:
                raise RadarError("invalid_request", "Filters and sorting apply only to portfolio or investors fields", 422)
            if request.field == "investors" and request.sector or request.field == "portfolio" and (request.kind or request.sort_by == "companies"):
                raise RadarError("invalid_request", "This filter or sort does not apply to the selected field", 422)
            value = field_value(data, request.field, mapping[request.field])
            result = {**common, "field": request.field, "status": "available" if value is not None else "not_observed",
                      "definitions": DEFINITIONS}
            if isinstance(value, list):
                source_count = len(value)
                if request.field in {"portfolio", "investors"}:
                    value = [row for row in value if matches(row, request)]
                    if request.sort_by == "name":
                        value.sort(key=lambda row: str(row.get("name") or "").casefold())
                    elif request.sort_by == "latest":
                        value.sort(key=lambda row: str(row.get("last") or ""), reverse=True)
                    elif request.sort_by == "companies":
                        value.sort(key=lambda row: row.get("companies") or 0, reverse=True)
                total = len(value)
                selected = value[request.offset:request.offset + request.limit]
                result.update(value=business_data(selected), pagination={"source_total": source_count, "matched_total": total,
                              "offset": request.offset, "limit": request.limit, "returned": len(selected),
                              "next_offset": request.offset + len(selected) if request.offset + len(selected) < total else None})
            else:
                if request.offset:
                    raise RadarError("invalid_request", "Offset applies only to array fields", 422)
                result["value"] = business_data(value)
            return result
        fields = [name for name, key in mapping.items() if field_value(data, name, key) is not None]
        metrics = ({key: data[key] for key in PROFILE_METRICS if key in data}
                   if meta["kind"] == "investor_profile" else {"totals": data.get("totals", {})})
        return {**common, "name": data.get("name", data.get("title", meta.get("title"))),
                "location": data.get("location", data.get("city")), "sector": data.get("sector"),
                "profile_depth": "summary", "metrics": business_data(metrics),
                "available_fields": fields,
                "field_counts": {name: len(data[key]) for name, key in mapping.items() if isinstance(data.get(key), list)},
                "field_status": {name: "available" if name in fields else "not_observed" for name in mapping},
                "field_request": {"method": "POST", "path": "/v1/investors/field", "required": ["slug", "field"]},
                "definitions": DEFINITIONS}
