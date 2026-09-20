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
from .public import PRIVATE, PRIVATE_VALUE

# Do not fetch contact documents, full financials, provider IDs or provenance.
PROJECTION = {"identity.domain": 1, "identity.name": 1, "identity.alternate_names": 1,
              "identity.all_domains": 1, "descriptive": 1, "classification": 1, "people": 1,
              "enrichment.website_stacks": 1, "enrichment.finalized_products": 1,
              "web_presence": 1, "traction.mobile_app": 1, "geography": 1, "lifecycle": 1,
              "structure.legal_entities": 1, "scores": 1, "financials.employees": 1,
              "extras.updated_at": 1}
ENRICHMENT_SECTIONS = {"traffic": "digital", "hiring": "hiring", "innovation": "innovation",
                       "activity": "activity", "reputation": "reputation", "share_of_voice": "sov"}
HIDDEN = PRIVATE | {"source", "source_ids", "provenance", "id", "person_id", "uid",
                    "coord_source", "hq_country_id", "name_lc", "resolve_via", "default_for_financial"}


def public_value(value, depth=0):
    if depth > 25:
        return None
    if isinstance(value, dict):
        return {str(k): public_value(v, depth + 1) for k, v in value.items()
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
    identity, descriptive = doc.get("identity", {}), doc.get("descriptive", {})
    classification, people = doc.get("classification", {}), doc.get("people", {})
    extra = doc.get("enrichment", {})
    company = public_value({"name": identity.get("name"), "domain": identity.get("domain"),
                            "alternate_names": identity.get("alternate_names", []),
                            "other_domains": identity.get("all_domains", []),
                            "description": descriptive.get("short_description"),
                            "detailed_description": descriptive.get("detailed_description"),
                            "founded": descriptive.get("founded_year"), "logo_url": descriptive.get("logo_url"),
                            "employee_count": doc.get("financials", {}).get("employees")})
    company["company_id"] = company_id
    key_people = public_value(people.get("key_people", []))
    founders = [person for person in key_people if isinstance(person, dict)
                and re.search(r"\bfounder\b", str(person.get("designation", "")), re.I)]
    parts = {
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
                       "observed_technologies": doc.get("web_presence", {}).get("technologies", []),
                       "observed_at": doc.get("web_presence", {}).get("crawl_date")},
        "web_presence": doc.get("web_presence"),
        "apps": doc.get("traction", {}).get("mobile_app"),
        "products": extra.get("finalized_products"),
        "geography": doc.get("geography"),
        "social": {"links": descriptive.get("social", {}), **enrichment.get("social", {})},
        "lifecycle": {k: v for k, v in doc.get("lifecycle", {}).items()
                      if k in {"stage", "is_funded", "is_acquirer", "is_deadpooled", "deadpooled_date",
                               "has_ever_been_public", "ownership", "financing_status"}},
        "legal": doc.get("structure", {}).get("legal_entities"),
        "assessments": {k: v for k, v in doc.get("scores", {}).items()
                        if k in {"completion", "finance", "scalability", "momentum", "data_confidence",
                                 "maturity", "innovation", "prominence"}},
        **{dest: enrichment.get(src) for dest, src in ENRICHMENT_SECTIONS.items()},
    }
    # Assess availability from presence, not truthiness: [] and numeric zero are
    # valid source observations. A missing source block stays unknown.
    source_presence = {"classification": "classification" in doc, "people": "people" in doc,
                       "technology": "enrichment" in doc or "web_presence" in doc,
                       "social": "social" in descriptive or "social" in enrichment,
                       "lifecycle": "lifecycle" in doc, "assessments": "scores" in doc}
    counts, coverage = {}, {}
    for section in dict.fromkeys(request.sections):
        value = parts[section]
        available = source_presence.get(section, value is not None)
        failed = enrichment_failed and section in {*ENRICHMENT_SECTIONS, "social"}
        coverage[section] = {"available": available, "status": "partial" if failed and available else (
            "unavailable" if failed else "available" if available else "not_observed")}
        if available:
            company[section] = bounded(public_value(value), request.item_limit, f"/company/{section}", counts)
    return {"company": company, "profile_depth": "detailed", "updated_at": public_value(doc.get("extras", {}).get("updated_at")),
            "coverage": {"sections": coverage, "arrays": counts,
                         "partial": enrichment_failed or any(row["truncated"] for row in counts.values())},
            "financial_history": "Use get_financials; financial archive and estimated-revenue access remain upstream-controlled"}


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
            raise RadarError("response_too_large", "Request fewer profile sections or reduce item_limit", 502)
        return result

    def _read(self, request):
        db = self.client["companies_data"]
        query = {"identity.domain": request.domain}
        if request.company_id:
            mapping = db.company_pubmap.find_one({"_id": request.company_id}, {"src": 1}, max_time_ms=3000)
            if not mapping:
                raise RadarError("no_data", "Unknown public company identifier", 404)
            query["_id"] = mapping["src"]
        docs = list(db.main_data.find(query, PROJECTION).limit(2).max_time_ms(5000))
        if not docs:
            raise RadarError("no_data", "No detailed company profile is available for this domain and identifier", 404)
        if len(docs) > 1:
            raise RadarError("ambiguous_company", "Multiple company records share this domain; supply a public company_id from Radar", 409)
        doc = docs[0]
        mapping = db.company_pubmap.find_one({"src": str(doc["_id"])}, {"_id": 1}, max_time_ms=3000)
        company_id = str(mapping["_id"]) if mapping else None
        enrichment, enrichment_failed = {}, False
        if set(request.sections) & {*ENRICHMENT_SECTIONS, "social"}:
            try:
                projection = {value: 1 for key, value in ENRICHMENT_SECTIONS.items() if key in request.sections}
                if "social" in request.sections:
                    projection["social"] = 1
                enrichment = db.company_enrichment.find_one({"_id": request.domain}, projection, max_time_ms=3000) or {}
            except PyMongoError:
                enrichment_failed = True
        return profile_payload(doc, enrichment, request, company_id, enrichment_failed=enrichment_failed)
