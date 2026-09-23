"""Regression for social detail being lost when the derived enrichment is absent."""
from copy import deepcopy
from dataclasses import replace

import httpx
import pytest

from radar_api.config import Settings
from radar_api.models import CompanyField
from radar_api.social import SocialStore, add_social, add_social_availability


def base():
    return {'domain': 'example.com', 'field': 'social', 'value': {'links': {'linkedin': 'https://linkedin.com/company/example'}},
            'status': 'available', 'coverage': {'sections': {'social': {'available': True, 'status': 'available'}},
                                              'arrays': {}, 'partial': False}}


@pytest.mark.asyncio
async def test_raw_linkedin_survives_absent_derived_signals_and_uses_bound_read_only_queries():
    calls = []
    def respond(request):
        calls.append(request)
        query = request.url.params['query']
        if 'linkedin_profile_logs' in query:
            rows = [{'name': 'Example', 'followers': 123, 'employee_count': 0, 'available_rows': 1}]
        else:
            rows = [{'post_id': 'post-1', 'text': 'Company update', 'likes': 0, 'available_rows': 2,
                     'media_urls': ['https://example.com/1', 'https://example.com/2']}]
        return httpx.Response(200, json={'data': rows})
    store = SocialStore(Settings(social_ch_url='http://social.local', social_ch_password='private-password'),
                        httpx.MockTransport(respond))
    result = await add_social(base(), CompanyField(domain='WWW.EXAMPLE.COM', field='social', item_limit=1), store)
    assert result['value']['linkedin']['profile']['followers'] == 123
    assert result['value']['linkedin']['profile']['employee_count'] == 0
    assert result['value']['linkedin']['recent_posts'][0]['text'] == 'Company update'
    assert result['coverage']['arrays']['/value/linkedin/recent_posts'] == {'available': 2, 'returned': 1, 'truncated': True}
    assert result['coverage']['arrays']['/value/linkedin/recent_posts/0/media_urls']['truncated']
    assert result['status'] == 'partial' and 'private-password' not in str(result)
    for call in calls:
        params = call.url.params
        assert params['readonly'] == '1' and params['param_domain'] == 'example.com' and params['param_limit'] == '1'
        assert '{domain:String}' in params['query'] and 'example.com' not in params['query']
        assert 'li_company_signals' not in params['query']
    assert 'GROUP BY official_post_id' in calls[1].url.params['query']


@pytest.mark.asyncio
async def test_social_failure_preserves_links_and_profile_without_claiming_empty_posts():
    def respond(request):
        if 'social_media_posts' in request.url.params['query']:
            return httpx.Response(500, text='private storage error')
        return httpx.Response(200, json={'data': [{'followers': 123, 'available_rows': 1}]})
    store = SocialStore(Settings(social_ch_url='http://social.local'), httpx.MockTransport(respond))
    result = await add_social(base(), CompanyField(domain='example.com', field='social'), store)
    assert result['status'] == 'partial'
    linkedin = result['value']['linkedin']
    assert linkedin['profile']['followers'] == 123 and linkedin['recent_posts'] is None
    assert linkedin['coverage']['recent_posts']['status'] == 'unavailable'
    assert 'private storage error' not in str(result)


@pytest.mark.asyncio
async def test_social_missing_source_configuration_and_absent_records_are_distinct():
    request = CompanyField(domain='example.com', field='social')
    unconfigured = await add_social(base(), request, None)
    assert unconfigured['status'] == 'partial'
    assert unconfigured['value']['linkedin']['coverage']['status'] == 'not_configured'
    store = SocialStore(Settings(social_ch_url='http://social.local'),
                        httpx.MockTransport(lambda req: httpx.Response(200, json={'data': []})))
    absent = await add_social(base(), request, store)
    assert absent['status'] == 'available'  # Social links still exist.
    assert absent['value']['linkedin']['profile'] is None
    assert absent['value']['linkedin']['recent_posts'] == []
    assert absent['value']['linkedin']['coverage']['recent_posts']['status'] == 'not_observed'


@pytest.mark.asyncio
async def test_social_can_supply_the_field_when_mongo_links_are_absent():
    data = base()
    data.update(status='not_observed', value=None)
    store = SocialStore(Settings(social_ch_url='http://social.local'),
                        httpx.MockTransport(lambda req: httpx.Response(200, json={'data': [{'followers': 0, 'available_rows': 1}]
                            if 'linkedin_profile_logs' in req.url.params['query'] else []})))
    result = await add_social(data, CompanyField(domain='example.com', field='social'), store)
    assert result['status'] == 'available' and result['value']['linkedin']['profile']['followers'] == 0


def test_social_runs_only_for_selected_field_and_requires_authentication(harness):
    from conftest import KEY
    from radar_api.service import Service
    from radar_api.upstream import Upstream
    client, _, _ = harness
    calls = []
    def respond(request):
        calls.append(request)
        return httpx.Response(200, json={'data': []})
    settings = replace(client.app.state.service.upstream.settings, social_ch_url='http://social.local')
    store = SocialStore(settings, httpx.MockTransport(respond))
    client.app.state.service.social = store
    class Profiles:
        async def get(self, request):
            return deepcopy(base()) if request.field == 'social' else {'field': request.field, 'value': {}, 'coverage': {}}
        def close(self):
            pass
    client.app.state.service.profiles = Profiles()
    response = client.post('/v1/companies/field', json={'domain': 'example.com', 'field': 'social'}, headers={'X-API-Key': KEY})
    assert response.status_code == 200 and len(calls) == 2
    client.post('/v1/companies/field', json={'domain': 'example.com', 'field': 'technology'}, headers={'X-API-Key': KEY})
    assert len(calls) == 2
    client.headers.pop('X-API-Key')
    denied = client.post('/v1/companies/field', json={'domain': 'example.com', 'field': 'social'})
    assert denied.status_code == 401 and len(calls) == 2
    # Configuration status is exposed, never credentials.
    service = Service(Upstream(settings, httpx.MockTransport(respond)))
    assert service.social is not None


def test_social_credentials_are_operator_only_and_hidden_from_settings_repr(monkeypatch):
    monkeypatch.setenv('RADAR_SOCIAL_CH_URL', 'http://social.local')
    monkeypatch.setenv('RADAR_SOCIAL_CH_USER', 'private-user')
    monkeypatch.setenv('RADAR_SOCIAL_CH_PASSWORD', 'private-password')
    settings = Settings.from_env()
    assert settings.social_ch_user == 'private-user'
    assert 'private-password' not in repr(settings) and 'private-user' not in repr(settings)
    with pytest.raises(ValueError):
        Settings(social_ch_url='http://private-user:private-password@social.local')


@pytest.mark.asyncio
async def test_compact_company_discovers_social_availability_without_fetching_details():
    calls = []
    def respond(request):
        calls.append(request)
        return httpx.Response(200, json={'data': [{'available': 1}]})
    store = SocialStore(Settings(social_ch_url='http://social.local'), httpx.MockTransport(respond))
    data = {'field_status': {'social': 'not_observed'}, 'available_fields': [], 'coverage': {'partial': False}}
    result = await add_social_availability(data, 'example.com', store)
    assert result['available_fields'] == ['social'] and result['field_status']['social'] == 'available'
    assert 'followers' not in calls[0].url.params['query'] and 'text' not in calls[0].url.params['query']
    assert set(result) == {'field_status', 'available_fields', 'coverage'}
