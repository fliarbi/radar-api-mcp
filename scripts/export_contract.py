#!/usr/bin/env python3
"""Generate the public capability reference and OpenAPI contract from the registry."""
import json
from pathlib import Path

from radar_api.server import create_app
from radar_api.service import FEATURES

root = Path(__file__).resolve().parent.parent
text = """# Capability reference

All data operations are authenticated JSON POST requests. MCP uses the same tool
name and a single `request` object containing the REST body. The input schema is
available from `/v1/capabilities` and [openapi.json](openapi.json).

This is retrieval coverage, not parity with every Radar account-management or
application action. Existing upstream plan gates remain authoritative. Financial
archive depth depends on the linked Radar session; associated news requires the
connected News services and a linked News key. Derived scores are labelled as
assessments, with financial evidence available separately.

| MCP tool | REST path | Purpose |
|---|---|---|
"""
for feature in FEATURES:
    text += f"| `{feature.name}` | `/v1/{feature.path}` | {feature.description} |\n"
text += """
The preview deliberately does not expose login, payment changes, contact-reveal
actions, CRM delivery, saved-search writes, application submissions, resume uploads,
report-generation jobs, arbitrary queries or arbitrary upstream routes. Financial
statement coverage is limited to the metrics Radar supplies; a missing metric is
not backfilled or fabricated. The existing market-analysis report application and
conversational agent are separate workflows, not generic pass-through tools here.
"""
(root / "docs/CAPABILITIES.md").write_text(text)
(root / "docs/openapi.json").write_text(json.dumps(create_app().openapi(), indent=2) + "\n")
print(f"Exported {len(FEATURES)} capabilities and OpenAPI schema")
