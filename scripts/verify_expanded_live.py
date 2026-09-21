#!/usr/bin/env python3
"""Verify bounded live pagination and both potential-data use cases; no writes."""
import asyncio
from dataclasses import replace
from datetime import datetime, timezone
import json
import logging
from pathlib import Path
import httpx
from radar_api.config import Settings
from radar_api.server import create_app
from capture_company_fields import save

ROOT = Path(__file__).resolve().parents[1]


async def main():
    logging.getLogger('httpx').setLevel(logging.WARNING)
    settings = replace(Settings.from_env(), allowed_hosts=('capture.local',), timeout_seconds=30)
    assert settings.apps_ch_url and settings.jobs_mongo_uri
    app = create_app(settings)
    key = (ROOT/'secrets/client-key.txt').read_text().strip()
    report = {'captured_at': datetime.now(timezone.utc).isoformat(),
              'provenance': 'Authenticated local gateway with existing live source stores; no deployment or source mutation', 'checks': {}}
    try:
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url='http://capture.local', headers={'X-API-Key': key}) as client:
            async def call(path, body):
                r = await client.post(path, json=body)
                assert r.status_code == 200, (path, r.status_code, r.json().get('error', {}).get('kind'))
                return r.json()
            seen, offset, total = [], 0, None
            for _ in range(10):
                data = (await call('/v1/apps/field', {'app_id': 'in.swiggy.android', 'field': 'install_history', 'limit': 5, 'offset': offset}))['data']
                seen.extend(data['value'])
                total, offset = data['pagination']['source_total'], data['pagination']['next_offset']
                if offset is None:
                    break
            assert offset is None and len(seen) == total
            complete = (await call('/v1/apps/field', {'app_id': 'in.swiggy.android', 'field': 'install_history', 'limit': 100}))['data']['value']
            assert seen == complete
            assert all(row['observed_at'].endswith('Z') for row in seen)
            report['checks']['app_history_pagination'] = {'app_id': 'in.swiggy.android', 'returned': len(seen), 'source_total': total,
                'duplicate_source_rows': len(seen)-len({json.dumps(row, sort_keys=True) for row in seen}),
                'matches_complete_source_sequence': True, 'all_timestamps_utc': True}
            ids, companies = [], []
            for page in (0, 1):
                data = (await call('/v1/jobs/internships/search', {'title': 'Business Development', 'limit': 3, 'page': page}))['data']
                ids.extend(row['id'] for row in data['internships'])
                data = (await call('/v1/jobs/internships/companies', {'title': 'Business Development', 'limit': 3, 'page': page}))['data']
                companies.extend(row['name'] for row in data['companies'])
            assert len(ids) == len(set(ids)) == 6 and len(companies) == len(set(companies)) == 6
            report['checks']['internship_pagination'] = {'pages': 2, 'unique_listings': len(ids), 'unique_employers': len(companies)}
            data = (await call('/v1/jobs/internships/search', {'work_mode': 'remote', 'part_time': True, 'limit': 3}))['data']
            assert data['internships'] and all(row['work_mode'] == 'remote_indicated' and 'PART_TIME' in row['employment_type'] for row in data['internships'])
            report['checks']['remote_part_time_internships'] = {'returned': len(data['internships']), 'matching_observations': data['total'], 'current_openings_verified': False}
            for preset in ('profitable_growth', 'hiring_expansion'):
                body = {'preset': preset, 'filters': {'locations': ['India'], 'markets': ['Payments']}, 'limit': 2}
                response = await call('/v1/companies/opportunities/search', body)
                save(ROOT/'qa/private'/f'opportunity-{preset}.json', {'operation': 'search_opportunities', 'method': 'POST', 'path': '/v1/companies/opportunities/search',
                    'request': body, 'http_status': 200, 'response': response, 'captured_at': datetime.now(timezone.utc).isoformat(), 'provenance': 'live gateway capture'})
                data = response['data']
                report['checks'][preset] = {'returned': data['returned'], 'evidence_rows': len(data['evidence']), 'partial': response['meta']['partial'], 'access': data['access'], 'effective_filters': data['effective_filters']}
            (ROOT/'qa/expanded-data-smoke.json').write_text(json.dumps(report, indent=2)+'\n')
            print(json.dumps(report, indent=2), flush=True)
    finally:
        app.state.service.internships.close()
        if app.state.service.profiles:
            app.state.service.profiles.close()


if __name__ == '__main__':
    asyncio.run(main())
