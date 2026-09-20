#!/usr/bin/env python3
"""Check local documentation links and validate guide examples against API models."""
import json
import re
from pathlib import Path

from radar_api.models import Company
from radar_api.service import BY_NAME

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = {
    "b2b-data-api": ["search_companies", "company_brief"],
    "company-search-api": ["search_companies", "semantic_company_search"],
    "company-enrichment-api": ["get_company_enrichment"],
    "financial-data-api": ["get_financials"],
    "company-financial-statements-api": ["get_financials"] * 3,
    "financial-news-api": ["search_business_news"],
    "funding-news-api": ["search_funding_news"],
    "startup-funding-data-api": ["get_company_funding", "market_pulse"],
    "investor-data-api": ["search_investors", "investor_directory"],
    "company-monitoring-api": [None, "get_company_events"],
    "competitor-intelligence-api": ["find_competitors", "compare_companies"],
    "hiring-signals-jobs-api": ["search_jobs", "salary_benchmark"],
    "company-intelligence-mcp-server": ["get_financials"],
}
links = examples = 0
for path in [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]:
    text = path.read_text()
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        target = target.split("#", 1)[0]
        if target:
            assert (path.parent / target).exists(), f"Broken link in {path.name}: {target}"
            links += 1
    if path.parent.name == "guides":
        blocks = re.findall(r"```json\n(.*?)\n```", text, re.S)
        operations = EXAMPLES.get(path.stem, [])
        assert len(blocks) == len(operations), f"Unmapped example in {path.name}"
        for block, operation in zip(blocks, operations):
            data = json.loads(block)
            data = data.get("request", data)
            (BY_NAME[operation].model if operation else Company).model_validate(data)
            examples += 1
        # Validate the JSON body of shell examples too.
        for body in re.findall(r"-d '(\{[^\n]+\})'", text):
            Company.model_validate_json(body)
            examples += 1
print(f"Checked {links} local links and {examples} guide request examples")
