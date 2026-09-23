"""Public search vocabulary mapped to the current Radar sidebar and handlers."""
from typing import get_args

from .models import CompanyFilters, CompanySort, Column
from .industry_options import INDUSTRIES

FILTERS = {
    "company_names": "company_name", "industries": "ai_ind", "sectors": "modern_sectors",
    "markets": "feeds", "business_models": "business_model", "locations": "selected_location",
    "sizes": "size", "stages": "funded_as", "technologies": "webstack", "products": "products",
    "skills": "skills", "event_types": "news_types", "financing_status": "financing_status",
    "ownership_status": "ownership_status", "revenue_bands": "revenue_band",
    "revenue_growth": "revenue_growth", "profitability": "profitable", "entity_type": "entity_type",
    "revenue_models": "revenue", "business_approaches": "business_approach", "scalability": "scalablity",
    "growth_stages": "progress_label", "operating_status": "status", "organization_types": "org_type",
    "deal_sizes": "deal_label", "ages": "current_age", "positions": "positions", "verticals": "verticals",
    **{k: k for k in ("industrial_applications", "founders_background", "web_popularity", "web_cwv",
        "web_speed", "web_seo_maturity", "web_sd_maturity", "web_business_hints", "web_score",
        "mobile_downloads", "mobile_growth", "hiring")},
}
SORTS = dict(zip(get_args(CompanySort), (None, "valuation", "funding amount", "estimated revenue",
    "no of financing rounds", "recent deal amount", "no of employees", "prominence", "finance strength",
    "scalability", "momentum", "innovation", "maturity")))
SUGGESTIONS = {"company_names": "company_name", "markets": "feeds", "locations": "selected_location",
               "technologies": "webstack", "products": "products", "skills": "skills", "positions": "positions",
               "verticals": "verticals"}
# Labels are copied from the active Radar sidebar, not inferred from database values.
OPTIONS = {
    "industries": INDUSTRIES,
    "sizes": ["Small", "Medium-Small", "Medium", "Medium-Large", "Large", "Very Large", "Giant", "Super Giant"],
    "organization_types": ["Company", "Investor"],
    "sectors": ["Enterprise Applications", "Enterprise Infrastructure", "High Tech", "Gig Economy", "Consumer", "Retail", "FinTech", "InsurTech", "HealthTech", "Life Sciences", "Energy Tech", "Mobile", "EdTech", "Semiconductors", "Travel and Hospitality Tech", "Real Estate and Construction Tech", "Aerospace, Maritime and Defense Tech", "Gaming", "Food and Agriculture Tech", "Telecom", "Auto Tech", "Media & Entertainment", "Transportation and Logistics Tech", "Chemicals and Materials Tech", "Conglomerates", "Industrial Goods and Manufacturing", "Mining", "Environment Tech", "Blockchain Technology"],
    "revenue_models": ["fee-for-service", "e-commerce - product", "e-commerce - service", "physical commerce", "advertising", "subscription", "commission on transaction", "donations", "sponsorship", "affiliate marketing", "renting / leasing", "lending", "freemium", "licensing", "interest", "selling data"],
    "business_approaches": ["traditional", "tech-enabled traditional", "little innovative", "unique & innovative"],
    "scalability": ["no or less scalability", "good scalability", "high scalability"],
    "growth_stages": ["Very Early Stage", "Early-Stage Scaling", "Early Stage with Growth Potential", "Stable Company", "Matured Company", "Consistent Growth", "Scaled Good", "Established and Scaling", "Steady Growth", "Scaling Super Fast", "Aggressively Scaling", "Funding Giant"],
    "deal_sizes": ["0-10K", "10-100K", "1M-10M", "10M-100M", "100M-1B", "1B+"],
    "stages": ["Most Recent", "Seed", *["Series " + c for c in "ABCDEFGHIJ"]],
    "web_seo_maturity": ["advanced", "good"], "web_sd_maturity": ["rich", "basic"],
    "web_business_hints": ["ecommerce", "local_service", "saas", "content", "vertical:restaurant", "vertical:hotel", "vertical:auto_dealer", "vertical:real_estate", "vertical:retail"],
    "industrial_applications": ["Internet of Things", "Artificial Intelligence", "Robotics", "AR VR", "Blockchain", "Big Data", "3D Printing", "Vertical SaaS", "Sustainability Tech"],
}


def catalog():
    schema = CompanyFilters.model_json_schema()
    fields = []
    for name, spec in schema["properties"].items():
        options = OPTIONS.get(name, spec.get("enum", spec.get("items", {}).get("enum", [])))
        fields.append({"field": name, "schema": spec, "options": options,
                       "suggestions_available": name in SUGGESTIONS or name in {"industries", "business_models"},
                       "options_complete": bool(spec.get("enum", spec.get("items", {}).get("enum", [])))})
    return {"filters": fields, "definitions": schema.get("$defs", {}),
            "sort_options": list(SORTS), "sort_direction": "descending; relevance uses source ranking",
            "columns": list(get_args(Column)), "page": {"first": 0, "max": 200, "limit_max": 100},
            "semantics": "Values generally OR within a filter and AND across filters. Structured search defaults to strict source matching; expanded mode exposes labelled fallback candidates. Inspect access and matching metadata. Band filters accept one value.",
            "column_note": "Selected columns are formatted display values, not precise financial statements. Empty values have unknown coverage; source suppresses zero/negative display values.",
            "contact_note": "Search returns availability only. Request emails or phones separately using an explicit contacts scope and an entitled linked Radar account."}
