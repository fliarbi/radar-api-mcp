"""Native-store limits, evidence semantics and retrieval integration regressions."""
import json
from dataclasses import replace

import httpx
import pytest
from pydantic import ValidationError
from pymongo.errors import ExecutionTimeout

from radar_api.apps import AppsStore, SELECTION
from radar_api.config import Settings
from radar_api.errors import RadarError
from radar_api.internships import InternshipStore, card, query_for
from radar_api.models import App, AppField, AppSearch, InternshipDetail, InternshipSearch, SearchCompanies
from radar_api.opportunities import PRESETS
from test_accounts import ledger_url, managed as managed_account  # noqa: F401 - shared account fixture

APP_ROW = {'app_id': 'com.example.app', 'name': 'Example', 'developer': 'Example',
           'developer_website': 'https://www.example.com', 'category': 'Business', 'installs': 0,
           'rating': 0, 'rating_count': 0, 'observed_at': '2026-06-07T00:00:00Z'}
DOC = {'_id': '123', 'posting_type': 'internship', 'title': 'Sales - Internship (WFH)',
       'company': 'Example', 'locations': [{'locality': 'Delhi'}], 'skills': ['Sales'],
       'stipend_value': 0, 'salary_currency': 'INR', 'valid_through': '2035-01-01',
       'employment_type': 'INTERN, PART_TIME', 'date_posted': '2026-07-01', 'description': 'Learn sales.'}


def app_response(request):
    sql = request.url.params['query']
    if 'DISTINCT genre' in sql:
        rows = [{'category': 'Business'}]
    elif 'history_points' in sql:
        rows = [{**APP_ROW, 'summary': 'Example app', 'history_points': 2, 'growth_points': 1, 'velocity_points': 1}]
    elif 'app_yoy' in sql:
        rows = [{'current_installs': 120, 'previous_installs': 100, 'gap_days': 30, 'reliable': 0}]
    elif 'app_velocity' in sql:
        rows = [{'release_date_suspect': 1, 'young_fast_riser': 0}]
    elif 'installs_history' in sql:
        rows = [{'observed_at': '2026-06-07T00:00:00Z', 'installs': 120}, {'observed_at': '2026-05-07T00:00:00Z', 'installs': 100}]
    elif 'store_developer_id' in sql:
        rows = [{'name': 'Example', 'store_developer_id': '123', 'website': 'https://example.com', 'legal_name': None}]
    elif 'histogram_json' in sql:
        rows = [{'rating': 0, 'rating_count': 0, 'review_count': None, 'histogram_json': '{"1":0,"5":10}'}]
    else:
        rows = [APP_ROW]
    return httpx.Response(200, json={'data': rows})


class InternshipFixture:
    """Small source fixture for REST/MCP transport tests; native logic tested below."""
    async def get(self, name, request):
        if name == 'get_internship':
            return {'internship': card(DOC, detail=True)}
        if name == 'search_internships':
            return {'internships': [card(DOC)], 'total': 1, 'has_more': False}
        return {'companies': [{'name': 'Example', 'observed_internships': 1, 'current_openings_verified': False}]}

    def close(self):
        pass


@pytest.mark.asyncio
async def test_app_sql_is_bound_read_only_and_credentials_never_enter_result():
    calls = []
    def respond(request):
        calls.append(request)
        return app_response(request)
    store = AppsStore(Settings(apps_ch_url='http://apps.local', apps_ch_password='private-password'), httpx.MockTransport(respond))
    result = await store.get('search_apps', AppSearch(domain='WWW.EXAMPLE.COM', min_installs=1, free=False, limit=1, page=2))
    params = calls[0].url.params
    assert params['readonly'] == '1' and params['max_execution_time'] == '8'
    assert params['param_domain'] == 'example.com' and params['param_offset'] == '2' and params['param_limit'] == '2'
    assert params['param_free'] == '0' and '{domain:String}' in params['query']
    assert 'domain(developerWebsite)' in params['query'] and 'example.com' not in params['query']
    assert result['apps'][0]['installs'] == 0
    assert 'private-password' not in json.dumps(result)
    assert 'raw_json' not in SELECTION['developer'] and 'Email' not in SELECTION['developer'] and 'Phone' not in SELECTION['developer']


@pytest.mark.asyncio
async def test_app_detail_separates_fields_and_keeps_growth_flags_and_history_pages():
    store = AppsStore(Settings(apps_ch_url='http://apps.local'), httpx.MockTransport(app_response))
    profile = await store.get('get_app', App(app_id='com.example.app'))
    assert profile['history_points'] == 2 and len(profile['available_fields']) == 7
    assert 'install_change' not in profile and 'description' not in profile['app']
    growth = await store.get('get_app_field', AppField(app_id='com.example.app', field='growth'))
    assert growth['value']['install_change']['reliable'] == 0
    assert growth['value']['velocity']['release_date_suspect'] == 1
    history = await store.get('get_app_field', AppField(app_id='com.example.app', field='install_history', limit=1))
    assert len(history['value']) == 1 and history['pagination']['next_offset'] == 1 and history['pagination']['source_total'] == 2
    ratings = await store.get('get_app_field', AppField(app_id='com.example.app', field='ratings'))
    assert ratings['value']['histogram'] == {'1': 0, '5': 10}
    assert ratings['value']['rating'] == 0 and ratings['value']['review_count'] is None
    with pytest.raises(RadarError, match='Offset applies'):
        await store.get('get_app_field', AppField(app_id='com.example.app', field='ratings', offset=1))


@pytest.mark.asyncio
@pytest.mark.parametrize('status,body,kind', [(403, {'secret': 'private-password'}, 'upstream_unavailable'),
    (200, {'exception': 'SELECT hidden', 'data': []}, 'upstream_unavailable'),
    (200, {'data': ['x'*2048]}, 'response_too_large')])
async def test_app_failures_are_bounded_and_sanitized(status, body, kind):
    store = AppsStore(Settings(apps_ch_url='http://apps.local', max_response_bytes=1024),
                      httpx.MockTransport(lambda r: httpx.Response(status, json=body)))
    with pytest.raises(RadarError) as error:
        await store.get('get_app', App(app_id='com.example.app'))
    assert error.value.kind == kind and 'private-password' not in str(error.value) and 'SELECT' not in str(error.value)


@pytest.mark.asyncio
async def test_missing_app_is_not_empty_success():
    store = AppsStore(Settings(apps_ch_url='http://apps.local'), httpx.MockTransport(lambda r: httpx.Response(200, json={'data': []})))
    with pytest.raises(RadarError) as error:
        await store.get('get_app', App(app_id='com.example.absent'))
    assert error.value.status == 404


def test_internship_filters_exclude_regular_jobs_and_do_not_invent_remote_or_validity():
    query = query_for(InternshipSearch(company='A.B', skills=['C++'], work_mode='remote', part_time=True, stipend_min=1000))
    assert query['$and'][0] == {'posting_type': 'internship'}
    assert query['$and'][1]['company']['$regex'] == r'^A\.B'
    assert any('WFH' in str(part) for part in query['$and'])
    result = card(DOC, detail=True)
    assert result['work_mode'] == 'remote_indicated' and result['stipend']['value'] == 0
    assert result['stipend']['period'] is None and result['company_domain'] is None
    assert result['validity_status'] == 'future_deadline_unverified' and not result['current_opening_verified']
    assert card({**DOC, 'title': 'Sales intern', 'locations': []})['work_mode'] == 'unknown'
    assert card({**DOC, 'valid_through': '2020-01-01'})['validity_status'] == 'expired'
    valid = query_for(InternshipSearch(validity='not_expired'))['$and'][-1]['valid_through']
    assert valid['$lt'] < '2035-01-01'


@pytest.mark.asyncio
async def test_native_internship_detail_projects_public_fields_and_requires_type():
    class Collection:
        def find_one(self, query, projection, **kwargs):
            assert query == {'_id': '123', 'posting_type': 'internship'}
            assert kwargs['max_time_ms'] == 5000 and 'var' not in projection
            return {**DOC, 'var': {'logged_to_ch': True}, 'password': 'private-value'}
    store = object.__new__(InternshipStore)
    store.collection = Collection()
    result = await store.get('get_internship', InternshipDetail(id='123'))
    assert result['internship']['description'] == 'Learn sales.'
    assert 'private-value' not in json.dumps(result) and 'logged_to_ch' not in json.dumps(result)
    def fail(*args, **kwargs):
        raise ExecutionTimeout('private collection name')
    store.collection.find_one = fail
    with pytest.raises(RadarError) as error:
        await store.get('get_internship', InternshipDetail(id='123'))
    assert 'private collection' not in str(error.value)


def test_new_models_reject_unbounded_or_unsupported_queries():
    for body in ({}, {'q': 'app', 'min_installs': 10**30}, {'q': 'app', 'store': 'ios'}, {'domain': 'example.com/path'}):
        with pytest.raises(ValidationError):
            AppSearch.model_validate(body)
    with pytest.raises(ValidationError):
        InternshipSearch(posted_since='2026-07-01', posted_until='2026-06-01')
    for preset in PRESETS.values():
        SearchCompanies(filters=preset['filters'], sort_by=preset['sort_by'])


def test_jobs_alias_filters_and_rollup_limits(harness):
    client, calls, _ = harness
    r = client.post('/v1/jobs/search', json={'employment_type': 'internship', 'salary_min': 1000,
        'min_experience_months': 1, 'max_experience_months': 12, 'sources': ['shine'], 'sort_by': 'salary'})
    assert r.status_code == 200
    sent = json.loads(calls[-1].content)
    assert sent['filters']['employment_type'] == 'intern' and sent['filters']['salary_min'] == 1000
    assert sent['filters']['sources'] == ['shine'] and sent['sort_by'] == 'salary'
    for body in ({'page': 1}, {'sort_by': 'salary'}):
        n = len(calls)
        assert client.post('/v1/jobs/companies', json=body).status_code == 422
        assert len(calls) == n
    r = client.post('/v1/jobs/companies', json={'limit': 1})
    assert r.status_code == 200 and len(r.json()['data']['companies']) <= 1
    assert client.post('/v1/jobs/search', json={'min_experience_months': 12, 'max_experience_months': 1}).status_code == 422


def test_opportunities_cannot_override_preset_and_expose_filters_evidence(harness):
    client, calls, _ = harness
    r = client.post('/v1/companies/opportunities/search', json={'preset': 'mobile_scale', 'filters': {'locations': ['India']}})
    assert r.status_code == 200
    data = r.json()['data']
    assert data['effective_filters']['mobile_downloads'] == ['1m+']
    assert data['effective_filters']['locations'] == ['India']
    assert data['evidence'][0]['domain'] == 'example.com'
    n = len(calls)
    r = client.post('/v1/companies/opportunities/search', json={'preset': 'mobile_scale', 'filters': {'mobile_downloads': ['100m+']}})
    assert r.status_code == 422 and len(calls) == n
    r = client.post('/v1/companies/opportunities/search', json={'preset': 'hiring_expansion', 'filters': {'hiring': {'roles': ['engineer']}}})
    assert r.status_code == 200
    criteria = r.json()['data']['effective_filters']['hiring']
    assert criteria['is_hiring'] is True and criteria['min_open_roles'] == 1 and criteria['recency_days'] == 90
    assert criteria['roles'] == ['engineer']


def test_native_catalog_connection_and_missing_store(harness):
    client, _, app = harness
    app.state.service.apps = None
    app.state.service.internships = None
    catalog = client.get('/v1/capabilities').json()['data']['features']
    assert not next(x for x in catalog if x['name'] == 'get_app')['connection_configured']
    assert client.post('/v1/apps/profile', json={'app_id': 'com.example.app'}).status_code == 503
    assert client.post('/v1/jobs/internships/search', json={}).status_code == 503


def test_app_scopes_in_managed_accounts(managed_account):  # noqa: F811
    from test_accounts import create, auth
    client, accounts, _, settings = managed_account
    service = client.app.state.service
    service.apps = AppsStore(replace(settings, apps_ch_url='http://apps.local'), httpx.MockTransport(app_response))
    app_key = create(client, scopes=['apps'])
    companies_key = create(client, scopes=['companies'])
    assert client.post('/v1/apps/profile', headers=auth(companies_key), json={'app_id': 'com.example.app'}).status_code == 403
    r = client.post('/v1/apps/profile', headers=auth(app_key), json={'app_id': 'com.example.app'})
    assert r.status_code == 200
    assert r.json()['meta']['billing']['credits'] == 1
    assert client.post('/v1/companies/apps', headers=auth(app_key), json={'domain': 'example.com'}).status_code == 403
