"""Bounded, read-only access to Radar's grouped company profile records.

Fixed collection names, indexed equality predicates and explicit projections.
No raw record, contact reveal, financial-history bypass or caller-supplied query.
"""
from __future__ import annotations

import asyncio
import json
import math
import re
from datetime import date, datetime, timezone

from bson import Decimal128
from pymongo import MongoClient
from pymongo.errors import PyMongoError

from .auth import principal
from .errors import RadarError
from .public import PRIVATE, PRIVATE_VALUE, company_logo, safe_asset
from .models import CompanyField, PROFILE_SECTIONS

# Every detail query selects only the explicitly requested field.
ENRICHMENT_SECTIONS = {"traffic": "digital", "hiring": "hiring", "innovation": "innovation",
                       "activity": "activity", "reputation": "reputation", "share_of_voice": "sov"}
HIDDEN = PRIVATE | {"source", "source_ids", "provenance", "id", "person_id", "uid",
                    "coord_source", "hq_country_id", "name_lc", "resolve_via", "default_for_financial"}
FIELD_PROJECTIONS = {
    "overview": ["identity.alternate_names", "identity.all_domains", "descriptive.short_description", "descriptive.detailed_description"],
    "classification": ["classification"], "people": ["people"],
    "technology": ["enrichment.website_stacks", "classification.technographics", "web_presence.technologies", "web_presence.crawl_date"],
    "web_presence": ["web_presence"], "apps": ["traction.mobile_app"],
    "products": ["enrichment.finalized_products"], "geography": ["geography"],
    "social": ["descriptive.social"], "lifecycle": ["lifecycle"],
    "legal": ["structure.legal_entities"], "assessments": ["scores"],
    **{key: [] for key in ENRICHMENT_SECTIONS},
}
SUMMARY_PROJECTION = {"identity.domain": 1, "identity.name": 1, "descriptive.short_description": 1,
                      "descriptive.founded_year": 1, "financials.employees": 1, "extras.updated_at": 1}


def observed(path):
    return {"$not": [{"$in": [{"$type": "$" + path}, ["missing", "null"]]}]}


def field_value(doc, path):
    for key in path.split("."):
        if not isinstance(doc, dict):
            return None
        doc = doc.get(key)
    return doc


def summary_projection():
    return {**SUMMARY_PROJECTION,
            "field_presence": {key: {"$or": [observed(p) for p in paths]}
                               for key, paths in FIELD_PROJECTIONS.items() if paths},
            "contact_presence": {key: {"$gt": [{"$size": {"$cond": [
                {"$isArray": "$contact." + key}, "$contact." + key, []]}}, 0]} for key in ("emails", "phones")}}


def summary_payload(doc, enrichment_presence, company_id, *, enrichment_failed=False):
    identity, descriptive = doc.get("identity") or {}, doc.get("descriptive") or {}
    presence = doc.get("field_presence", {})
    statuses = {}
    for name in PROFILE_SECTIONS:
        present = bool(presence.get(name) or enrichment_presence.get(ENRICHMENT_SECTIONS.get(name, name)))
        statuses[name] = "available" if present else "not_observed"
        if enrichment_failed and name in {*ENRICHMENT_SECTIONS, "social"}:
            statuses[name] = "partial" if present else "unavailable"
    return {"company": public_value({"company_id": company_id, "domain": identity.get("domain"),
                "name": identity.get("name"), "logo_url": company_logo(identity.get("domain")), "description": descriptive.get("short_description"),
                "founded": descriptive.get("founded_year"), "employee_count": (doc.get("financials") or {}).get("employees")}),
            "profile_depth": "summary", "available_fields": [name for name, status in statuses.items() if status in {"available", "partial"}],
            "field_status": statuses, "contacts": {"availability": doc.get("contact_presence", {}),
                "path": "/v1/contacts/company", "required_scope": "contacts", "access": "linked Radar paid-plan check"},
            "field_request": {"method": "POST", "path": "/v1/companies/field", "required": ["domain", "field"]},
            "updated_at": public_value((doc.get("extras") or {}).get("updated_at")),
            "coverage": {"partial": enrichment_failed},
            "financial_history": "Use get_financials; financial archive and estimated-revenue access remain upstream-controlled"}


def public_value(value, depth=0):
    if depth > 25:
        return None
    if isinstance(value, dict):
        return {str(k): public_value(safe_asset(str(k), v), depth + 1) for k, v in value.items()
                if not str(k).startswith("_") and str(k).lower() not in HIDDEN}
    if isinstance(value, (list, tuple)):
        return [public_value(v, depth + 1) for v in value]
    if isinstance(value, datetime):
        return (value if value.tzinfo else value.replace(tzinfo=timezone.utc)).isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, Decimal128):
        return str(value.to_decimal())
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, str):
        return None if PRIVATE_VALUE.search(value) else value
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return None


def names(rows):
    return [row["name"] for row in rows or [] if isinstance(row, dict) and row.get("name")]


def bounded(value, limit, path, counts):
    if isinstance(value, list):
        counts[path] = {"available": len(value), "returned": min(len(value), limit), "truncated": len(value) > limit}
        return [bounded(row, limit, f"{path}/{i}", counts) for i, row in enumerate(value[:limit])]
    if isinstance(value, dict):
        return {k: bounded(v, limit, f"{path}/{k}", counts) for k, v in value.items()}
    return value


def profile_payload(doc, enrichment, request, company_id, *, enrichment_failed=False):
    identity, descriptive = doc.get("identity") or {}, doc.get("descriptive") or {}
    classification, people = doc.get("classification") or {}, doc.get("people") or {}
    extra = doc.get("enrichment") or {}
    company = public_value({"name": identity.get("name"), "domain": identity.get("domain"),
                            "alternate_names": identity.get("alternate_names", []),
                            "other_domains": identity.get("all_domains", []),
                            "description": descriptive.get("short_description"),
                            "detailed_description": descriptive.get("detailed_description"),
                            "founded": descriptive.get("founded_year"),
                            "employee_count": (doc.get("financials") or {}).get("employees")})
    company["company_id"] = company_id
    key_people = public_value(people.get("key_people") or [])
    founders = [person for person in key_people if isinstance(person, dict)
                and re.search(r"\bfounder\b", str(person.get("designation", "")), re.I)]
    parts = {
        "overview": {"alternate_names": identity.get("alternate_names", []), "other_domains": identity.get("all_domains", []),
                     "description": descriptive.get("short_description"), "detailed_description": descriptive.get("detailed_description")},
        "classification": {"sectors": names(classification.get("practice_areas")),
                           "markets": names(classification.get("feeds_primary")),
                           "feeds": {"primary": names(classification.get("feeds_primary")),
                                     "other": names(classification.get("feeds_other"))},
                           "business_models": names(classification.get("business_model")),
                           "revenue_models": names(classification.get("revenue_model")),
                           "industries": names(classification.get("industry")),
                           "company_types": names(classification.get("company_type")),
                           "flags": classification.get("special_flags", {})},
        "people": {"key_people": key_people, "founders": founders,
                   "key_people_count": people.get("key_people_count"),
                   "background_flags": people.get("background_flags", []),
                   "founder_selection": "Source designation contains founder; not an independent verification"},
        "technology": {"website_stack": extra.get("website_stacks", []),
                       "technographics": classification.get("technographics", []),
                       "observed_technologies": (doc.get("web_presence") or {}).get("technologies", []),
                       "observed_at": (doc.get("web_presence") or {}).get("crawl_date")},
        "web_presence": doc.get("web_presence"),
        "apps": (doc.get("traction") or {}).get("mobile_app"),
        "products": extra.get("finalized_products"),
        "geography": doc.get("geography"),
        "social": {"links": descriptive.get("social", {}), **enrichment.get("social", {})},
        "lifecycle": {k: v for k, v in (doc.get("lifecycle") or {}).items()
                      if k in {"stage", "is_funded", "is_acquirer", "is_deadpooled", "deadpooled_date",
                               "has_ever_been_public", "ownership", "financing_status"}},
        "legal": (doc.get("structure") or {}).get("legal_entities"),
        "assessments": {k: v for k, v in (doc.get("scores") or {}).items()
                        if k in {"completion", "finance", "scalability", "momentum", "data_confidence",
                                 "maturity", "innovation", "prominence"}},
        **{dest: enrichment.get(src) for dest, src in ENRICHMENT_SECTIONS.items()},
    }
    # Assess availability from presence, not truthiness: [] and numeric zero are
    # valid source observations. A missing source block stays unknown.
    source_presence = {name: any(field_value(doc, path) is not None for path in paths) or
                       enrichment.get(ENRICHMENT_SECTIONS.get(name, name)) is not None
                       for name, paths in FIELD_PROJECTIONS.items()}
    counts, coverage = {}, {}
    for section in [request.field]:
        value = parts[section]
        available = source_presence.get(section, value is not None)
        failed = enrichment_failed and section in {*ENRICHMENT_SECTIONS, "social"}
        coverage[section] = {"available": available, "status": "partial" if failed and available else (
            "unavailable" if failed else "available" if available else "not_observed")}
        if available:
            company[section] = bounded(public_value(value), request.item_limit, "/value", counts)
    return {"domain": request.domain, "company_id": company_id, "field": request.field,
            "value": company.get(request.field), "status": coverage[request.field]["status"],
            "updated_at": public_value((doc.get("extras") or {}).get("updated_at")),
            "coverage": {"sections": coverage, "arrays": counts,
                         "partial": enrichment_failed or any(row["truncated"] for row in counts.values())},
            "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."}


class ProfileStore:
    def __init__(self, settings, client=None):
        self.settings = settings
        self.client = client or MongoClient(settings.profile_mongo_uri, serverSelectionTimeoutMS=3000,
                                            connectTimeoutMS=3000, socketTimeoutMS=6000,
                                            waitQueueTimeoutMS=1000, maxPoolSize=10, appname="radar-api-profile-reader")

    def close(self):
        self.client.close()

    async def get(self, request):
        principal()
        try:
            result = await asyncio.to_thread(self._read, request)
        except PyMongoError:
            raise RadarError("profile_store_unavailable", "Detailed company profiles are temporarily unavailable", 503) from None
        if len(json.dumps(result, ensure_ascii=False).encode()) > self.settings.max_response_bytes:
            raise RadarError("response_too_large", "Reduce item_limit for the requested company field", 502)
        return result

    def _read(self, request):
        db = self.client["companies_data"]
        query = {"identity.domain": request.domain}
        if request.company_id:
            mapping = db.company_pubmap.find_one({"_id": request.company_id}, {"src": 1}, max_time_ms=3000)
            if not mapping:
                raise RadarError("no_data", "Unknown public company identifier", 404)
            query["_id"] = mapping["src"]
        detailed = isinstance(request, CompanyField)
        if detailed:
            projection = {"identity.domain": 1, "extras.updated_at": 1, **{key: 1 for key in FIELD_PROJECTIONS[request.field]}}
            docs = list(db.main_data.find(query, projection).limit(2).max_time_ms(5000))
        else:
            # Availability is computed in Mongo; no contact values or rich arrays
            # are fetched for the compact overview.
            docs = list(db.main_data.aggregate([{"$match": query}, {"$limit": 2}, {"$project": summary_projection()}], maxTimeMS=5000))
        if not docs:
            raise RadarError("no_data", "No detailed company profile is available for this domain and identifier", 404)
        if len(docs) > 1:
            raise RadarError("ambiguous_company", "Multiple company records share this domain; supply a public company_id from Radar", 409)
        doc = docs[0]
        mapping = db.company_pubmap.find_one({"src": str(doc["_id"])}, {"_id": 1}, max_time_ms=3000)
        company_id = str(mapping["_id"]) if mapping else None
        enrichment, enrichment_failed = {}, False
        if not detailed or request.field in {*ENRICHMENT_SECTIONS, "social"}:
            try:
                if detailed:
                    projection = {ENRICHMENT_SECTIONS.get(request.field, request.field): 1}
                    enrichment = db.company_enrichment.find_one({"_id": request.domain}, projection, max_time_ms=3000) or {}
                else:
                    rows = list(db.company_enrichment.aggregate([{"$match": {"_id": request.domain}}, {"$limit": 1},
                        {"$project": {"_id": 0, **{key: observed(key) for key in [*ENRICHMENT_SECTIONS.values(), "social"]}}}], maxTimeMS=3000))
                    enrichment = rows[0] if rows else {}
            except PyMongoError:
                enrichment_failed = True
        if detailed:
            return profile_payload(doc, enrichment, request, company_id, enrichment_failed=enrichment_failed)
        return summary_payload(doc, enrichment, company_id, enrichment_failed=enrichment_failed)
