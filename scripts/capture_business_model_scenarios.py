#!/usr/bin/env python3
"""Opt-in bounded live reads for the ten business-model documentation scenarios."""
import asyncio
from dataclasses import replace
from datetime import datetime, timezone
import json
import logging
import os
from pathlib import Path
import time

import httpx

from business_model_cases import CASES
from radar_api.config import Settings
from radar_api.server import create_app
from radar_api.service import BY_NAME

ROOT = Path(__file__).resolve().parents[1]


async def capture():
    logging.getLogger('httpx').setLevel(logging.WARNING)
    target = ROOT / 'qa/private/business-model-live.json'
    target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    key = os.environ.get('RADAR_API_KEY') or (ROOT / 'secrets/client-key.txt').read_text().strip()
    app = create_app(replace(Settings.from_env(), allowed_hosts=('capture.local',), timeout_seconds=60))
    records = []
    sem = asyncio.Semaphore(2)

    def save():
        fd = os.open(target, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0o600)
        with os.fdopen(fd, 'w') as stream:
            os.fchmod(stream.fileno(), 0o600)
            json.dump(records, stream, ensure_ascii=False, indent=2)

    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app, raise_app_exceptions=False),
                                 base_url='http://capture.local', headers={'X-API-Key': key}) as client:
        async def request(operation, body):
            BY_NAME[operation].model.model_validate(body)
            path = '/v1/' + BY_NAME[operation].path
            started = time.monotonic()
            async with asyncio.timeout(125):
                response = await client.post(path, json=body)
            return {'operation': operation, 'method': 'POST', 'path': path, 'request': body,
                    'http_status': response.status_code, 'response': response.json(),
                    'captured_at': datetime.now(timezone.utc).isoformat(),
                    'capture_kind': 'live_gateway', 'http_executed': True,
                    'transport': 'Local authenticated ASGI gateway with live configured source reads',
                    'elapsed_seconds': round(time.monotonic() - started, 3)}

        async def one(case):
            async with sem:
                record = {'id': case['id'], 'captures': []}
                records.append(record)
                try:
                    search = await request(case['operation'], case['request'])
                    record['captures'].append(search)
                    save()
                    data = search['response'].get('data') or {}
                    companies = data.get('companies') or []
                    print(case['id'], search['http_status'], 'returned', len(companies), flush=True)
                    if search['response'].get('ok') and companies:
                        domain = next((row.get('domain') for row in companies if row.get('domain')), None)
                        if domain:
                            for operation, body in [
                                ('get_company', {'domain': domain}),
                                ('get_company_field', {'domain': domain, 'field': 'classification', 'item_limit': 100}),
                            ]:
                                record['captures'].append(await request(operation, body))
                                save()
                            print(case['id'], 'detail reads captured', flush=True)
                except Exception as exc:
                    record['capture_error'] = type(exc).__name__
                    save()
                    print(case['id'], 'capture_error', type(exc).__name__, flush=True)

        await asyncio.gather(*(one(case) for case in CASES))
    if app.state.service.profiles:
        app.state.service.profiles.close()
    if app.state.service.internships:
        app.state.service.internships.close()
    print('Saved bounded live reads for', len(records), 'scenarios', flush=True)


if __name__ == '__main__':
    asyncio.run(capture())
