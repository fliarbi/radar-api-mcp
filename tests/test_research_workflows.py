import asyncio
from copy import deepcopy
from types import SimpleNamespace
import pytest
from pydantic import ValidationError
from radar_api.errors import RadarError
from radar_api.models import FinancialConstraint, FinancialScreen, CompanyTeam
from radar_api.research import evaluate_financials, screen, team, financial_catalog
from radar_api.service import BY_NAME
from test_accounts import ledger_url, managed as managed_research  # noqa: F401


def request(**extra):
    return FinancialScreen(
        domains=["example.com"],
        constraints=[{"metric": "revenue", "gte": 0, "lt": 10000}],
        period_type="annual",
        **extra,
    )


def data(value=9999, currency="USD", source="filing"):
    return {
        "periods": [
            {
                "fiscal_period": "FY",
                "fiscal_year": 2025,
                "metrics": {"revenue": {"value": value, "currency": currency, "source_type": source}},
            }
        ]
    }


@pytest.mark.parametrize(
    "value,status",
    [
        (9999, "matched"),
        (10000, "not_matched"),
        (0, "matched"),
        (-1, "not_matched"),
        (None, "unknown"),
        ("999", "unknown"),
        (True, "unknown"),
    ],
)
def test_exact_threshold_and_unknowns(value, status):
    assert evaluate_financials(data(value), request())["status"] == status


def test_period_and_provenance_do_not_fall_back_to_manufacture_match():
    d = data(None)
    d["periods"].append(data(100)["periods"][0])
    assert evaluate_financials(d, request())["status"] == "unknown"
    assert evaluate_financials(data(12, "INR"), request())["status"] == "unknown"
    assert (
        evaluate_financials(data(12, source="news_report"), request(source_type="filing"))["status"]
        == "unknown"
    )


@pytest.mark.parametrize(
    "body", [{"gt": 0, "gte": 1}, {"lt": 100, "gt": 100}, {"lte": 99, "gte": 100}, {"gt": float("nan")}, {}]
)
def test_reject_ambiguous_financial_bounds(body):
    with pytest.raises(ValidationError):
        FinancialConstraint(metric="revenue", **body)


def test_catalog_states_source_boundaries_and_money_types():
    c = financial_catalog()
    assert c["revenue_bands"]["under1m"].startswith("0 <")
    assert c["growth_bands_pct"]["growing"] == ">=10 and <30"
    assert "funding" in str(c["distinctions"]) and c["currency"] == "USD"


async def test_screen_preserves_mixed_outcomes_source_restrictions_and_bounded_concurrency():
    active = peak = 0

    async def dispatch(name, r):
        nonlocal active, peak
        if name == "search_companies":
            return {
                "companies": [
                    {"domain": d} for d in ["one.com", "two.com", "three.com", "four.com", "one.com"]
                ],
                "access": {"restricted_filters": ["stages"]},
            }
        active += 1
        peak = max(active, peak)
        try:
            await asyncio.sleep(0.001)
            if r.domain == "four.com":
                raise RadarError("upstream_timeout", "private source", 504)
            return data({"one.com": 100, "two.com": 20000, "three.com": None}[r.domain])
        finally:
            active -= 1

    req = FinancialScreen(
        filters={"industries": ["AdTech"]},
        candidate_limit=5,
        constraints=[{"metric": "revenue", "lt": 10000}],
        period_type="annual",
    )
    result = await screen(SimpleNamespace(dispatch=dispatch), req)
    assert len(result["evaluated"]) == 4 and peak <= 3
    assert [x["domain"] for x in result["matches"]] == ["one.com"]
    assert result["counts"] == {"matched": 1, "not_matched": 1, "unknown": 1, "unavailable": 1}
    assert result["successful_financial_reads"] == 3 and result["coverage"]["partial"]
    assert result["next_page"] == 1 and not result["coverage"]["complete"]
    assert result["discovery"]["access"]["restricted_filters"] == ["stages"]


async def test_professional_team_requires_exact_affiliation_and_preserves_summary_limits():
    async def dispatch(name, r):
        assert r.companies == ["example.com"]
        return {
            "people": [
                {"id": "1", "current_company_domain": "example.com"},
                {"id": "2", "current_company_domain": "example.com.evil"},
                {"id": "3", "current_company": "Example", "current_company_domain": ""},
            ],
            "_partial_timeout": False,
        }

    result = await team(
        SimpleNamespace(dispatch=dispatch), CompanyTeam(domain="example.com", group="professionals", limit=3)
    )
    assert len(result["people"]) == 1 and result["people"][0]["id"] == "1"
    assert result["excluded_unverified_affiliations"] == 2 and result["coverage"]["partial"]
    assert result["next_page"] == 1 and not result["coverage"]["complete"]


def test_team_filters_are_never_silently_ignored():
    for body in (
        {"group": "founders", "skills": ["Python"]},
        {"group": "professionals", "title": "CEO"},
        {"group": "key_people", "page": 100},
    ):
        with pytest.raises(ValidationError):
            CompanyTeam(domain="example.com", **body)


def test_correct_industry_vocabulary_never_calls_wrong_metas_taxonomy(harness):
    client, calls, _ = harness
    r = client.post("/v1/companies/filter-options", json={"field": "industries", "q": "adtech"})
    assert r.status_code == 200 and "AdTech" in r.json()["data"]["options"]
    assert not calls


def test_screen_reservations_and_unused_read_refunds(managed_research):  # noqa: F811
    from test_accounts import create, auth

    client, accounts, _, _ = managed_research
    key = create(client, scopes=["companies"])
    r = client.post(
        "/v1/companies/financials/screen",
        headers=auth(key),
        json=request().model_dump(mode="json", exclude_unset=True),
    )
    assert r.status_code == 200 and r.json()["meta"]["billing"]["credits"] == 2
    r = client.post(
        "/v1/companies/team", headers=auth(key), json={"domain": "example.com", "group": "professionals"}
    )
    assert r.status_code == 403


def test_all_fifty_scenarios_have_valid_models():
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
    from scenario_cases import CASES

    assert len(CASES) == 50
    for c in CASES:
        BY_NAME[c["operation"]].model.model_validate(deepcopy(c["request"]))


def test_strict_matching_excludes_broadened_and_unknown_rows_without_losing_pagination():
    from radar_api.models import SearchCompanies
    from radar_api.service import Service
    source = {"companies": [
        {"w": "india.com", "_tier": "strict"},
        {"w": "usa.com", "_tier": "semantic"},
        {"w": "unknown.com"}],
        "_tiers": [{"tier": "strict", "added": 1, "q": "private diagnostic"}],
        "_strict_count": 1, "_total_matched": 3}
    # Mixed tiers must not imply that an unlabelled card is strict.
    source["_tiers"].append({"tier": "semantic", "added": 2})
    result = Service.company_results(source, SearchCompanies(limit=3))
    assert [c["domain"] for c in result["companies"]] == ["india.com"]
    assert result["matching"]["excluded_candidates"] == 2 and result["next_page"] == 1
    assert "private diagnostic" not in str(result)
    expanded = Service.company_results(source, SearchCompanies(match_mode="expanded", limit=3))
    assert [c["match_tier"] for c in expanded["companies"]] == ["strict", "semantic", "unverified"]
    source["_stripped_filters"] = ["profitable"]
    blocked = Service.company_results(source, SearchCompanies(limit=3))
    assert not blocked["companies"] and blocked["access"]["restricted_filters"] == ["profitability"]


def test_direct_source_strict_metadata_and_unknown_metadata():
    from radar_api.models import SearchCompanies
    from radar_api.service import Service
    source = {"companies": [{"w": "example.com"}], "_tiers": [{"tier": "strict", "count": 25}]}
    assert Service.company_results(source, SearchCompanies())["returned"] == 1
    del source["_tiers"]
    assert Service.company_results(source, SearchCompanies())["returned"] == 0
