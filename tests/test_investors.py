from __future__ import annotations

import hashlib
import json
from pathlib import Path

import httpx
import pytest
from fastapi.testclient import TestClient

from radar_api.config import Settings
from radar_api.investors import InvestorStore
from radar_api.models import InvestorField, InvestorPage
from radar_api.server import create_app
from radar_api.upstream import Upstream
from radar_api.errors import RadarError

from conftest import KEY


def write_release(root):
    root = Path(root)
    (root / "meta").mkdir(parents=True)
    (root / "data").mkdir()
    data = {"slug": "example-investor", "name": "Example Investor", "coverage_end": "2026-05-22",
            "computed_on": "2026-09-14", "total_companies": 4, "total_rounds": 6,
            "portfolio_count": 3, "round_count": 5, "entry_round_size": {"n": 2, "median": 100000},
            "companies": [{"name": f"Company {i}", "domain": f"example{i}.com", "city": "Delhi",
                           "stage": "Seed", "sectors": ["FinTech"], "entry_amount": 0 if i == 0 else 100000,
                           "last": f"2026-01-0{i+1}", "rounds": 1, "next_days": None,
                           "linkedin_url": "https://linkedin.com/private", "emails": ["private@example.com"]}
                          for i in range(3)],
            "undated_companies": [{"name": "Undated", "stage": "Seed"}],
            "cohort": {"eligible": 2, "funded": 1, "repeat": 0, "funded_pct": 50},
            "co_investors": [{"name": "Partner", "rounds": 2}],
            "editorial": {"stories": [{"title": "A short funding headline", "url": "https://example.com/news"}]}}
    raw = json.dumps(data).encode()
    (root / "data/example-investor.json").write_bytes(raw)
    (root / "meta/example-investor.json").write_text(json.dumps({"slug": "example-investor", "family": "investor",
        "kind": "investor_profile", "status": "built", "data_sha256": hashlib.sha256(raw).hexdigest()}))
    return root


def test_investor_summary_has_metrics_without_rosters(harness):
    client, calls, _ = harness
    response = client.post('/v1/investors/page', json={"slug": "example-investor"})
    assert response.status_code == 200
    data = response.json()['data']
    assert data['metrics']['total_companies'] == 4
    assert data['field_counts']['portfolio'] == 3
    assert data['field_counts']['undated_portfolio'] == 1
    assert 'portfolio' in data['available_fields'] and 'companies' not in data
    assert 'Company 0' not in response.text
    assert response.json()['window']['data_through'] == '2026-05-22'
    assert calls[-1].url.path == '/investors/publication/example-investor'


def test_investor_field_preserves_depth_and_paginates_without_loss(harness):
    client, calls, _ = harness
    rows = []
    for offset in [0, 2]:
        response = client.post('/v1/investors/field', json={"slug": "example-investor", "field": "portfolio", "limit": 2, "offset": offset})
        assert response.status_code == 200
        data = response.json()['data']
        assert data['pagination']['source_total'] == 3
        assert 'private@example.com' not in response.text and 'linkedin.com' not in response.text
        rows.extend(data['value'])
    assert [r['name'] for r in rows] == ['Company 0', 'Company 1', 'Company 2']
    assert rows[0]['entry_amount'] == 0 and rows[0]['next_days'] is None
    assert rows[0]['sectors'] == ['FinTech']
    assert len(calls) == 2  # a fresh publication check on every page


def test_investor_filters_sorting_and_invalid_combinations(harness):
    client, _, _ = harness
    base = {"slug": "example-investor", "field": "portfolio"}
    d = client.post('/v1/investors/field', json={**base, "stage": "Seed", "city": "Delhi", "sort_by": "latest"}).json()['data']
    assert d['value'][0]['name'] == 'Company 2'
    assert client.post('/v1/investors/field', json={**base, "sector": "Health"}).json()['data']['pagination']['matched_total'] == 0
    for invalid in [{"kind": "angel"}, {"sort_by": "companies"}, {"field": "follow_on", "q": "ignored"}, {"field": "follow_on", "offset": 1}, {"field": "investors"}, {"field": "all"}, {"limit": 101}]:
        assert client.post('/v1/investors/field', json={**base, **invalid}).status_code == 422


def test_investor_integrity_error_is_not_metadata_success(harness):
    client, _, app = harness
    path = app.state.service.investors.root / 'data/example-investor.json'
    path.write_text(path.read_text() + ' ')
    response = client.post('/v1/investors/page', json={"slug": "example-investor"})
    assert response.status_code == 503
    assert 'integrity' in response.json()['error']['message']


@pytest.mark.parametrize('status', [403, 404, 503])
def test_live_gate_cannot_be_bypassed_by_local_snapshot(keyfile, tmp_path, status):
    settings = Settings(keys_file=str(keyfile), allowed_hosts=('testserver',), investor_data_dir=str(write_release(tmp_path/'release')))
    app = create_app(settings, Upstream(settings, httpx.MockTransport(lambda request: httpx.Response(status))))
    with TestClient(app) as client:
        response = client.post('/v1/investors/field', headers={'X-API-Key': KEY}, json={'slug': 'example-investor', 'field': 'portfolio'})
    assert response.status_code in [403, 404, 502]
    assert 'Company 0' not in response.text


@pytest.mark.asyncio
async def test_snapshot_mismatch_and_symlink_fail_closed(tmp_path):
    root = write_release(tmp_path/'release')
    store = InvestorStore(Settings(investor_data_dir=str(root)))
    gate = {'slug': 'example-investor', 'kind': 'investor_profile', 'family': 'investor'}
    with pytest.raises(RadarError):
        await store.get(InvestorPage(slug='example-investor'), {**gate, 'kind': 'investor_list'})
    path = root/'data/example-investor.json'
    outside = tmp_path/'outside.json'
    outside.write_bytes(path.read_bytes())
    path.unlink()
    path.symlink_to(outside)
    with pytest.raises(RadarError):
        await store.get(InvestorField(slug='example-investor', field='portfolio'), gate)


def test_unconnected_investor_detail_is_explicit(harness):
    client, _, app = harness
    app.state.service.investors = None
    response = client.post('/v1/investors/page', json={'slug': 'example-investor'})
    assert response.json()['meta']['partial'] is True
    assert response.json()['data']['profile_depth'] == 'metadata'
    assert client.post('/v1/investors/field', json={'slug': 'example-investor', 'field': 'portfolio'}).status_code == 503


@pytest.mark.asyncio
async def test_directory_keeps_statistics_while_excluding_social_reveal(tmp_path):
    root = write_release(tmp_path/'release')
    path = root/'data/example-investor.json'
    data = {'slug': 'example-investor', 'title': 'FinTech investors', 'coverage_end': '2026-05-22',
            'totals': {'selected': 2, 'dated_investors': 50}, 'shortlist_rule': {'minimum_companies': 2},
            'breadth': [{'label': '1 company', 'angel': 40, 'firm': 8}],
            'shortlist_location': {'local': 1}, 'shortlist_localities': {'areas': [{'name': 'City Centre', 'count': 1}]},
            'investors': [{'id': 'internal-id', 'name': 'Angel', 'kind': 'angel', 'companies': 2, 'stages': {'Seed': 2},
                           'stage_sizes': {'Seed': {'n': 2, 'median': 10000}}, 'examples': [{'name': 'Product', 'rounds': 2}],
                           'linkedin_url': 'https://linkedin.com/private', 'linkedin_preview': True},
                          {'name': 'Fund', 'kind': 'firm', 'companies': 5, 'stages': {'Series A': 5}}]}
    raw = json.dumps(data).encode()
    path.write_bytes(raw)
    meta = {'slug': 'example-investor', 'family': 'investors', 'kind': 'investor_list', 'status': 'built',
            'data_sha256': hashlib.sha256(raw).hexdigest()}
    (root/'meta/example-investor.json').write_text(json.dumps(meta))
    store = InvestorStore(Settings(investor_data_dir=str(root)))
    result = await store.get(InvestorField(slug='example-investor', field='investors', kind='angel', stage='Seed'), meta)
    assert result['pagination']['source_total'] == 2 and result['pagination']['matched_total'] == 1
    row = result['value'][0]
    assert row['stage_sizes']['Seed']['median'] == 10000
    assert row['examples'] == [{'name': 'Product', 'rounds': 2}]
    assert not {'id', 'linkedin_url', 'linkedin_preview'} & row.keys()
    selection = await store.get(InvestorField(slug='example-investor', field='selection'), meta)
    assert selection['value']['breadth'][0]['angel'] == 40
    geography = await store.get(InvestorField(slug='example-investor', field='geography'), meta)
    assert geography['value']['localities']['areas'][0]['count'] == 1


def test_docs_renderer_keeps_professional_business_fields(monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).resolve().parents[1]/'scripts'))
    from build_endpoint_docs import excerpt
    person = {'id': 'public-id', 'name': 'Example', 'skills': list(range(70)), 'education': [{'degree': 'MBA'}],
              'scores': {'rank': 0}, 'top_experience': [{'company': 'Example', 'years': 12}], 'founder': False,
              'investor': {'rounds': 5}, 'contact_gated': True, 'headline': 'An executive and investor',
              'summary': 'Professional career summary'}
    response = {'data': {'people': [person]}}
    rendered, omissions = excerpt('search_people', response)
    assert rendered == response and not omissions


def test_docs_renderer_preserves_funding_headlines_and_all_returned_rows(monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).resolve().parents[1]/'scripts'))
    from build_endpoint_docs import excerpt
    response = {'data': {'events': [{'headline': f'Company {i} raises a seed round', 'amount': i} for i in range(40)]}}
    rendered, omissions = excerpt('get_company_funding', response)
    assert rendered == response and not omissions
