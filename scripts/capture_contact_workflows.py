#!/usr/bin/env python3
"""Capture read-only profile discovery and clearly labelled local contact fixtures.

--live executes three non-contact profile searches with the configured preview key.
Contact success examples always use an isolated synthetic upstream and temporary
keys. No paid contact request, production identity change or message is performed.
"""
import argparse
import hashlib
import json
import tempfile
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

import httpx
from fastapi.testclient import TestClient

from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.service import BY_NAME
from radar_api.upstream import Upstream
from build_endpoint_docs import digest, encoded, excerpt

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ID = "example-founder"
FIXTURES = [
    ("company-email-only", "get_company_contacts", {"domain": "example.com", "fields": ["emails"]},
     {"emails": ["sales@example.com", "support@example.com"], "phones": ["+1-202-555-0123"]}, 200,
     "Company-associated mailboxes, with phone values excluded by field selection."),
    ("company-phone-only", "get_company_contacts", {"domain": "example.com", "fields": ["phones"]},
     {"emails": ["sales@example.com"], "phones": ["+1-202-555-0123"]}, 200,
     "Requested phone strings only; the gateway does not certify mobile status or E.164 normalization."),
    ("person-direct", "get_person_contacts", {"person_id": FIXTURE_ID, "fields": ["emails", "phones"]},
     {"contacts": {FIXTURE_ID: {"emails": ["alex@example.com"], "phones": ["+1-202-555-0142"], "source": "person"}}}, 200,
     "A fictional person's source-associated record. Person origin does not establish verified work-email type."),
    ("person-company-fallback", "get_person_contacts", {"person_id": FIXTURE_ID, "fields": ["emails"]},
     {"contacts": {FIXTURE_ID: {"emails": ["sales@example.com"], "phones": ["+1-202-555-0123"], "source": "company_domain"}}}, 200,
     "Company mailbox fallback; never relabel this as the founder's personal address."),
    ("person-phone-only-source", "get_person_contacts", {"person_id": FIXTURE_ID, "fields": ["emails"]},
     {"contacts": {FIXTURE_ID: {"emails": [], "phones": ["+1-202-555-0142"], "source": "person"}}}, 200,
     "Source had a person phone but no email; an email-only request is empty. Fallback is not independently applied per requested field."),
    ("person-no-data", "get_person_contacts", {"person_id": FIXTURE_ID, "fields": ["emails", "phones"]},
     {"contacts": {FIXTURE_ID: {"emails": [], "phones": [], "source": "none"}}}, 200,
     "No returned source contact, including when the source did not resolve the person ID. This is not proof of nonexistence."),
    ("person-unknown-origin", "get_person_contacts", {"person_id": FIXTURE_ID, "fields": ["emails"]},
     {"emails": ["alex@example.com"], "phones": [], "source": "unrecognised_fixture_origin"}, 200,
     "Unexpected provenance stays unknown, not silently classified as a person's direct contact."),
    ("paid-plan-denial", "get_company_contacts", {"domain": "example.com", "fields": ["emails"]},
     {"gated": True, "plan": "free", "emails": ["must-not-return@example.com"]}, 403,
     "The linked source gate wins even if a malformed gated response contains contact values."),
]


def save(key, operation, body, status, response, kind, provenance, explanation):
    timestamp = datetime.now(timezone.utc).isoformat()
    raw = {"operation": operation, "method": "POST", "path": "/v1/" + BY_NAME[operation].path,
           "request": body, "http_status": status, "response": response, "capture_kind": kind,
           "captured_at": timestamp, "provenance": provenance, "interpretation": explanation}
    private = ROOT / "qa/private" / ("contact-workflow-" + key + ".json")
    private.parent.mkdir(parents=True, exist_ok=True)
    private.write_text(encoded(raw))
    private.chmod(0o600)
    projected, omissions = excerpt(operation, response)
    record = {**raw, "response": projected, "omitted_paths": omissions, "credential_redactions": [],
              "hash_basis": "Parsed JSON with sorted keys; retained business fields and all returned array rows are unchanged",
              "original_response_sha256": digest(response), "response_excerpt_sha256": digest(projected)}
    directory = ROOT / "docs/examples/contacts"
    directory.mkdir(exist_ok=True)
    (directory / (key + ".json")).write_text(encoded(record))
    print(key, status, kind)


def fixture_capture():
    with tempfile.TemporaryDirectory() as directory:
        key = "rdr_" + "f" * 64
        path = Path(directory) / "keys.json"
        path.write_text(json.dumps({"keys": [{"sha256": hashlib.sha256(key.encode()).hexdigest(),
            "active": True, "name": "contact documentation fixture", "radar_token": "fixture-linked-session",
            "scopes": ["contacts"], "rate_per_minute": 600}]}))
        path.chmod(0o600)
        settings = Settings(keys_file=str(path), radar_url="http://fixture.invalid", allowed_hosts=("testserver",))
        for label, operation, body, source, expected, interpretation in FIXTURES:
            transport = httpx.MockTransport(lambda req, payload=source: httpx.Response(200, json=payload))
            with TestClient(create_app(settings, Upstream(settings, transport))) as client:
                response = client.post("/v1/" + BY_NAME[operation].path, json=body, headers={"X-API-Key": key})
                assert response.status_code == expected, label
                assert "must-not-return" not in response.text
                save(label, operation, body, response.status_code, response.json(), "local_contact_fixture",
                     "Executed local gateway; synthetic contact upstream and temporary fixture key. All addresses use example.com and phone values are fictional. No live contact retrieval or production account mutation.", interpretation)


def live_capture():
    settings = replace(Settings.from_env(), allowed_hosts=("testserver",))
    key = (ROOT / "secrets/client-key.txt").read_text().strip()
    cases = [
        ("founder-shashank", "search_people", {"name": "Shashank Kumar", "companies": ["razorpay.com"], "limit": 3},
         "Candidate linkage by recorded name and company domain; preserve the returned profile ID and LinkedIn reference. Not independent identity or current-role verification."),
        ("founder-professional", "search_people", {"name": "Harshil Mathur", "companies": ["razorpay.com"], "limit": 3},
         "Name-plus-company-prefix discovery; inspect recorded domain and LinkedIn URL before accepting a contact ID."),
        ("founder-team", "get_company_team", {"domain": "razorpay.com", "group": "professionals", "roles": ["founder"], "limit": 3},
         "Exactly affiliated professional cards classified as founders by the source; current roles and completeness remain unverified."),
    ]
    with TestClient(create_app(settings)) as client:
        for label, operation, body, interpretation in cases:
            response = client.post("/v1/" + BY_NAME[operation].path, json=body, headers={"X-API-Key": key})
            save(label, operation, body, response.status_code, response.json(), "live_gateway",
                 "Authenticated read-only gateway discovery against configured Radar HTTP sources. No contact-reveal endpoint was called.", interpretation)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    fixture_capture()
    if args.live:
        live_capture()
