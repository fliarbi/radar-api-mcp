"""Output conservation, selected-field isolation and source coverage regressions."""
from copy import deepcopy
from dataclasses import replace
import hashlib
import json
import re

import httpx
import pytest

from radar_api.company_signals import CompanySignalsStore, add_signals, add_signals_availability, aligned
from radar_api.apps import AppsStore
from radar_api.config import Settings
from radar_api.investors import InvestorStore
from radar_api.models import AppField, CompanyField, Financials, InvestorField, InvestorPage
from radar_api.profiles import FIELD_PROJECTIONS, ProfileStore, profile_payload
from radar_api.public import financial_data
from test_profiles import StoreClient, record
from test_investors import write_release


def base(field='traffic'):
    return {'field': field, 'value': {'legacy_score': 0}, 'status': 'available',
            'coverage': {'sections': {field: {'available': True, 'status': 'available'}}, 'arrays': {}, 'partial': False}}


def test_financial_evidence_retains_zero_negative_and_entitled_period_boundaries():
    source = {'intel': {'earnings': {'gated': True, 'history_total_count': 20, 'score': 70, 'yoy_pct': 18,
        'history': [{'period_year': 2026, 'period_qtr': 'Q1', 'period_label': 'Q1 FY2026', 'revenue_usd': 0,
                     'net_income_usd': -5, 'employees': 0, 'revenue_growth_pct': -2, 'guidance_revenue': 100,
                     'coverage_count': 4, 'quality_signals': ['Profitable'], 'has_official': False,
                     'period_has_official': True, 'primary_source': 'bi', 'source_target_ids': ['article-1']}],
        'latest': {'period_label': 'Q1 FY2026', 'revenue_usd': 999999}}}}
    original = deepcopy(source)
    result = financial_data(source, Financials(domain='example.com', statement='income'))
    period = result['periods'][0]
    assert period['metrics']['revenue']['value'] == 0 and period['metrics']['net_income']['value'] == -5
    assert period['operating_context']['employees'] == 0 and period['operating_context']['revenue_growth_pct'] == -2
    assert period['evidence']['coverage_count'] == 4 and period['evidence']['has_official'] is False
    assert result['available_period_count'] == 20 and len(result['periods']) == 1 and result['access_limited']
    assert result['summary']['assessment']['yoy_pct'] == 18 and '999999' not in str(result)
    balance = financial_data(source, Financials(domain='example.com', statement='balance_sheet'))
    assert balance['periods'][0]['metrics'] == {} and 'operating_context' not in balance['periods'][0]
    assert balance['coverage']['returned_periods_with_metrics'] == 0
    assert financial_data(source, Financials(domain='example.com', year_to=2025))['periods'] == []
    assert source == original


@pytest.mark.parametrize('field,new_key', [('classification', 'sector_details'), ('lifecycle', 'achievements'), ('assessments', 'uniqueness_scalability')])
def test_profile_context_is_selected_and_private_ids_never_escape(field, new_key):
    doc = record()
    doc['classification']['practice_areas'][0]['classification'] = {'market': 'Finance', 'id': 'hidden'}
    doc['lifecycle'] = {'stage': 'Series A', 'xcorn': {'rating': 'Unicorn', 'rationale': 'Source assessment'}}
    doc['structure'] = {'parent': {'name': 'Parent', 'id': 'hidden'}, 'tickers': ['EXAMPLE']}
    doc['traction']['achievements'] = [{'name': 'Award', 'category': 'Business'}]
    doc['enrichment']['uniqueness_scalability'] = {'label': 'Differentiated', 'reason': 'Source rationale', 'source': 'private'}
    result = profile_payload(doc, {}, CompanyField(domain='example.com', field=field), 'public-example')
    assert new_key in result['value']
    assert 'hidden' not in str(result) and 'private' not in str(result) and 'latest_estimated_revenue' not in str(result)
    other = {'classification': 'assessments', 'lifecycle': 'technology', 'assessments': 'people'}[field]
    assert new_key not in profile_payload(doc, {}, CompanyField(domain='example.com', field=other), 'public-example')['value']
    assert all(not p.startswith(('contact', 'financials')) for p in FIELD_PROJECTIONS[field])


def test_misaligned_traffic_arrays_keep_each_source_index_and_duplicate():
    result = aligned({'ts': ['same', 'same'], 'shares': [0], 'counts': [3, 4, 5]}, {'name': 'ts', 'share': 'shares', 'count': 'counts'})
    assert result == [{'name': 'same', 'share': 0, 'count': 3}, {'name': 'same', 'share': None, 'count': 4},
                      {'name': None, 'share': None, 'count': 5}]


@pytest.mark.asyncio
async def test_traffic_is_bounded_parameterized_and_preserves_derived_values():
    calls = []
    def respond(request):
        calls.append(request)
        return httpx.Response(200, json={'data': [{'visits': 0, 'visits_date': '2026-05-01', 'global_rank': 12,
            'mobile_share': .75, 'ts_source': ['Direct', 'Search'], 'ts_share': [.5], 'ts_visits': [0, 1]}]})
    store = CompanySignalsStore(Settings(company_ch_url='http://store.local', company_ch_password='secret-value'), httpx.MockTransport(respond))
    result = await add_signals(base(), CompanyField(domain='WWW.EXAMPLE.COM', field='traffic', item_limit=1), store)
    value = result['value']
    assert value['legacy_score'] == 0 and value['web_traffic']['snapshot']['visits'] == 0
    assert value['web_traffic']['snapshot']['ranks']['global_rank'] == 12
    path = '/value/web_traffic/snapshot/traffic_connections'
    assert result['coverage']['arrays'][path] == {'available': 2, 'returned': 1, 'truncated': True}
    assert result['coverage']['partial'] and 'secret-value' not in str(result)
    params = calls[0].url.params
    assert params['param_domain'] == 'example.com' and params['readonly'] == '1' and params['max_execution_time'] == '8'
    assert '{domain:String}' in params['query'] and 'example.com' not in params['query']
    assert not re.search(r'\b(email|phone|author)\b', params['query'])


@pytest.mark.asyncio
async def test_reviews_keep_profile_when_samples_fail_and_report_unknown():
    def respond(request):
        if 'trustpilot_review_samples' in request.url.params['query']:
            return httpx.Response(500, text='private SQL diagnostics')
        return httpx.Response(200, json={'data': [{'review_count': 0, 'trust_score': 0}]})
    store = CompanySignalsStore(Settings(company_ch_url='http://store.local'), httpx.MockTransport(respond))
    result = await add_signals(base('reputation'), CompanyField(domain='example.com', field='reputation'), store)
    reviews = result['value']['customer_reviews']
    assert reviews['platform'] == 'trustpilot'
    assert reviews['profile']['review_count'] == 0 and reviews['review_samples'] is None
    assert reviews['coverage']['review_samples']['status'] == 'unavailable'
    assert result['status'] == 'partial' and 'private SQL' not in str(result)


@pytest.mark.asyncio
async def test_review_source_total_survives_bounding_and_field_can_exist_without_mongo():
    def respond(request):
        rows = [{'review_id': 'one', 'rating': 1, 'available_rows': 10}] if 'review_samples' in request.url.params['query'] else []
        return httpx.Response(200, json={'data': rows})
    store = CompanySignalsStore(Settings(company_ch_url='http://store.local'), httpx.MockTransport(respond))
    data = base('reputation')
    data.update(value=None, status='not_observed')
    result = await add_signals(data, CompanyField(domain='example.com', field='reputation', item_limit=1), store)
    assert result['value']['customer_reviews']['profile'] is None
    assert result['coverage']['arrays']['/value/customer_reviews/review_samples']['available'] == 10
    assert result['status'] == 'partial'
    unconfigured = await add_signals(base(), CompanyField(domain='example.com', field='traffic'), None)
    assert unconfigured['value']['web_traffic']['coverage']['status'] == 'not_configured'
    empty = CompanySignalsStore(Settings(company_ch_url='http://store.local'), httpx.MockTransport(lambda r: httpx.Response(200, json={'data': []})))
    absent = await add_signals(data | {'status': 'not_observed', 'value': None, 'coverage': {'partial': False, 'arrays': {}, 'sections': {}}},
                               CompanyField(domain='example.com', field='traffic'), empty)
    assert absent['status'] == 'not_observed' and not absent['coverage']['partial']


@pytest.mark.asyncio
async def test_compact_availability_fetches_existence_only():
    calls = []
    def respond(r):
        calls.append(r)
        return httpx.Response(200, json={'data': [{'traffic': 1, 'reputation': 0}]})
    store = CompanySignalsStore(Settings(company_ch_url='http://store.local'), httpx.MockTransport(respond))
    result = await add_signals_availability({'company': {'name': 'Example'}, 'field_status': {}, 'available_fields': [], 'coverage': {'partial': False}}, 'example.com', store)
    assert result['available_fields'] == ['traffic'] and set(result['company']) == {'name'}
    sql = calls[0].url.params['query']
    assert 'count()' in sql and not any(s in sql for s in ('trust_score', 'review_count', 'mobile_share', 'SELECT *'))


def test_signal_queries_require_auth_and_only_run_for_requested_field(harness):
    from conftest import KEY
    client, _, _ = harness
    calls = []
    def respond(r):
        calls.append(r)
        return httpx.Response(200, json={'data': []})
    client.app.state.service.company_signals = CompanySignalsStore(Settings(company_ch_url='http://store.local'), httpx.MockTransport(respond))
    client.app.state.service.profiles = ProfileStore(Settings(), StoreClient([record()]))
    headers = {'X-API-Key': KEY}
    # Fixture's real ProfileStore is projected for each field.
    assert client.post('/v1/companies/field', json={'domain': 'example.com', 'field': 'technology'}, headers=headers).status_code == 200
    assert calls == []
    assert client.post('/v1/companies/field', json={'domain': 'example.com', 'field': 'traffic'}, headers=headers).status_code == 200
    assert len(calls) == 1
    client.headers.clear()
    assert client.post('/v1/companies/field', json={'domain': 'example.com', 'field': 'traffic'}).status_code == 401
    assert len(calls) == 1


def test_empty_investor_array_is_observed_and_filters_do_not_change_source_status(tmp_path):
    root = write_release(tmp_path / 'release')
    path = root / 'data/example-investor.json'
    data = json.loads(path.read_text())
    data['companies'] = []
    path.write_text(json.dumps(data))
    meta_path = root / 'meta/example-investor.json'
    meta = json.loads(meta_path.read_text())
    meta['data_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    meta_path.write_text(json.dumps(meta))
    store = InvestorStore(Settings(investor_data_dir=str(root)))
    page = store._get(InvestorPage(slug='example-investor'), meta)
    field = store._get(InvestorField(slug='example-investor', field='portfolio'), meta)
    assert page['field_status']['portfolio'] == field['status'] == 'available'
    assert 'portfolio' in page['available_fields'] and field['pagination']['source_total'] == 0 and field['value'] == []
    assert page['field_status']['analysis'] == 'not_observed'


def test_news_strict_coverage_failure_keeps_safe_reason(harness):
    from radar_api.upstream import Upstream
    client, _, _ = harness
    service = client.app.state.service
    def respond(r):
        return httpx.Response(503, json={'error': {'kind': 'coverage_unavailable', 'reason': 'private SQL and host'}})
    service.upstream = Upstream(replace(service.upstream.settings, news_url='http://news.local'), httpx.MockTransport(respond))
    response = client.post('/v1/news/search', json={'q': 'earnings'})
    assert response.status_code == 503 and response.json()['error']['kind'] == 'coverage_unavailable'
    assert 'private SQL' not in response.text and response.json()['data'] is None


def test_company_signal_credentials_are_runtime_only(monkeypatch):
    monkeypatch.setenv('RADAR_COMPANY_CH_PASSWORD', 'hidden-secret')
    monkeypatch.setenv('RADAR_COMPANY_CH_USER', 'hidden-user')
    settings = Settings.from_env()
    assert settings.company_ch_password == 'hidden-secret'
    assert 'hidden-secret' not in repr(settings) and 'hidden-user' not in repr(settings)


@pytest.mark.asyncio
async def test_selected_app_release_and_install_metadata_preserve_source_values():
    calls = []
    def respond(r):
        query = r.url.params['query']
        calls.append(query)
        if 'history_points' in query:
            row = {'app_id': 'com.example.app', 'observed_at': '2026-06-01', 'history_points': 0, 'growth_points': 0, 'velocity_points': 0}
        elif 'recent_changes_json' in query:
            row = {'version': '2.1', 'recent_changes_json': '"New business tools"', 'android_version_display_json': '', 'early_access_json': 'false'}
        else:
            row = {'name': 'Example', 'minimum_installs': 0, 'maximum_installs': 100, 'observed_installs': 0, 'installs_display': '0+'}
        return httpx.Response(200, json={'data': [row]})
    store = AppsStore(Settings(apps_ch_url='http://apps.local'), httpx.MockTransport(respond))
    release = await store.get('get_app_field', AppField(app_id='com.example.app', field='release'))
    assert release['value']['recent_changes'] == 'New business tools'
    assert release['value']['android_version_display'] is None and release['value']['early_access'] is False
    listing = await store.get('get_app_field', AppField(app_id='com.example.app', field='listing'))
    assert listing['value']['observed_installs'] == 0 and listing['value']['maximum_installs'] == 100
    assert 'recent_changes' not in listing['value']
    assert all('developerEmail' not in q and 'developerLegalPhoneNumber' not in q for q in calls)


def test_internship_detail_keeps_first_seen_separate_from_posted_and_direct_apply():
    from radar_api.internships import FIELDS, card
    doc = {'_id': 'example', 'first_seen': 1710000000, 'direct_apply': False, 'date_posted': '2026-01-01'}
    detail = card(doc, detail=True)
    assert detail['first_seen_epoch_seconds'] == 1710000000 and detail['direct_apply'] is False
    assert detail['posted'] == '2026-01-01' and not detail['current_opening_verified']
    assert {'first_seen', 'direct_apply'} <= FIELDS.keys()
    assert 'first_seen_epoch_seconds' not in card(doc)
