#!/usr/bin/env python3
"""Generate the public capability reference and OpenAPI contract from the registry."""
import json
import tempfile
from pathlib import Path

from cryptography.fernet import Fernet

from radar_api.server import create_app
from radar_api.service import FEATURES
from radar_api.config import Settings

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
The retrieval tool list deliberately does not expose login, payment changes, contact-reveal
actions, CRM delivery, saved-search writes, application submissions, resume uploads,
report-generation jobs, arbitrary queries or arbitrary upstream routes. Financial
statement coverage is limited to the metrics Radar supplies; a missing metric is
not backfilled or fabricated. The existing market-analysis report application and
conversational agent are separate workflows, not generic pass-through tools here.

Optional account mode adds HTTP-only key management, usage, spending limits,
API watchlists and prepaid checkout. See [account operations](ACCOUNTS.md),
[API-key onboarding](guides/api-keys-authentication.md), and the
[account-mode schema](account-openapi.json). The MCP tool list remains read-only.
"""
(root / "docs/CAPABILITIES.md").write_text(text)
(root / "docs/openapi.json").write_text(json.dumps(create_app().openapi(), indent=2) + "\n")
with tempfile.TemporaryDirectory() as directory:
    settings = Settings(accounts_enabled=True, accounts_db=str(Path(directory) / "accounts.db"),
                        encryption_key=Fernet.generate_key().decode())
    (root / "docs/account-openapi.json").write_text(json.dumps(create_app(settings).openapi(), indent=2) + "\n")
print(f"Exported {len(FEATURES)} capabilities and OpenAPI schema")
