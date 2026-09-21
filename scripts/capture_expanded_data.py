#!/usr/bin/env python3
"""Capture apps, dedicated internships, job filters and opportunity screens."""
import asyncio
from dataclasses import replace
from datetime import datetime, timezone
import json
import logging
from pathlib import Path
import httpx
from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.service import BY_NAME
from capture_company_fields import save

ROOT = Path(__file__).resolve().parents[1]
CASES = {
    'company_apps': {'domain': 'swiggy.com', 'limit': 5},
    'opportunity_presets': {},
    'search_opportunities': {'preset': 'mobile_scale', 'filters': {'locations': ['India'], 'markets': ['Payments']}, 'limit': 2},
    'job_filter_catalog': {},
    'job_filter_options': {'field': 'title', 'q': 'software', 'limit': 5},
    'search_internships': {'title': 'Business Development', 'limit': 3},
    'companies_offering_internships': {'title': 'Business Development', 'limit': 3},
    'get_internship': {'id': 'from-search'},
    'search_apps': {'q': 'Swiggy', 'min_installs': 1000000, 'limit': 3},
    'get_app': {'app_id': 'in.swiggy.android'},
    'get_app_field': {'app_id': 'in.swiggy.android', 'field': 'growth'},
    'app_filter_options': {'q': 'Food', 'limit': 10},
}


async def capture():
    logging.getLogger('httpx').setLevel(logging.WARNING)
    settings = replace(Settings.from_env(), allowed_hosts=('capture.local',))
    assert settings.apps_ch_url and settings.jobs_mongo_uri
    key = (ROOT/'secrets/client-key.txt').read_text().strip()
    app = create_app(settings)
    rawfile = ROOT/'qa/private/endpoint-live.json'
    report = json.loads(rawfile.read_text())
    try:
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url='http://capture.local', headers={'X-API-Key': key}) as client:
            for name, body in CASES.items():
                if name == 'get_internship':
                    body = {'id': report['operations']['search_internships']['response']['data']['internships'][0]['id']}
                path = '/v1/'+BY_NAME[name].path
                r = await client.post(path, json=body)
                record = {'method': 'POST', 'path': path, 'request': body, 'http_status': r.status_code, 'response': r.json(),
                          'captured_at': datetime.now(timezone.utc).isoformat(), 'provenance': 'live gateway capture'}
                report['operations'][name] = record
                save(rawfile, report)
                print(name, r.status_code, r.json().get('error', {}).get('kind', 'ok'), flush=True)
            for field in ('listing', 'ratings', 'monetization', 'release', 'developer', 'growth', 'install_history'):
                body = {'app_id': 'in.swiggy.android', 'field': field, 'limit': 5}
                r = await client.post('/v1/apps/field', json=body)
                save(ROOT/'qa/private'/f'app-swiggy-{field}.json', {'operation': 'get_app_field', 'request': body, 'response': r.json(), 'http_status': r.status_code,
                    'captured_at': datetime.now(timezone.utc).isoformat(), 'provenance': 'live gateway capture', 'method': 'POST', 'path': '/v1/apps/field'})
                print('app field', field, r.status_code, flush=True)
    finally:
        app.state.service.internships.close()
        if app.state.service.profiles:
            app.state.service.profiles.close()


if __name__ == '__main__':
    asyncio.run(capture())
