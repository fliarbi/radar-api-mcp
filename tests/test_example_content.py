"""Regression checks for falsely populated documentation examples."""
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_examples import content_check  # noqa: E402


def check(operation, data, request=None, status=200):
    return content_check(operation, request or {}, status, {"ok": status == 200, "data": data})


def test_period_labels_and_company_context_do_not_make_a_statement_populated():
    data = {"has_data": True, "available_period_count": 30,
            "summary": {"revenue": 10}, "periods": [{"period": "FY2024", "metrics": {}}]}
    assert check("get_financials", data, {"statement": "balance_sheet"})["state"] == "empty"
    data["periods"][0]["metrics"] = {"revenue": {"value": 100}}
    assert check("get_financials", data, {"statement": "balance_sheet"})["state"] == "empty"
    assert check("get_financials", data, {"statement": "income"})["state"] == "populated"


@pytest.mark.parametrize("value,populated", [(0, True), (-10, True), (12.5, True), (None, False), (False, False), ("100", False)])
def test_only_numeric_observations_count_but_zero_and_negative_are_valid(value, populated):
    data = {"periods": [{"metrics": {"net_income": {"value": value}}}]}
    assert (check("get_financials", data, {"statement": "income"})["state"] == "populated") is populated


@pytest.mark.parametrize("operation,data", [
    ("get_company_events", {"events": [], "pulse": {"total": 100}}),
    ("search_jobs", {"jobs": [], "total": 10000}),
    ("screen_company_financials", {"matches": [], "evaluated": [{"status": "unknown"}]}),
    ("get_company_field", {"field": "products", "status": "available", "value": []}),
    ("get_company_field", {"field": "innovation", "status": "not_observed", "value": None}),
    ("get_person_contacts", {"person_id": "example-founder", "emails": [], "phones": [], "available": False}),
])
def test_metadata_is_not_a_positive_row_or_selected_value(operation, data):
    assert check(operation, data)["state"] == "empty"


def test_expected_contact_denial_is_separate_from_source_failure():
    assert check("get_company_contacts", None, status=403)["state"] == "expected_denial"
    assert check("get_company_contacts", None, status=503)["state"] == "unavailable"
    assert check("get_financials", None, status=403)["state"] == "unavailable"
