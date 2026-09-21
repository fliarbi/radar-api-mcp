#!/usr/bin/env python3
"""Capture each published investor detail through the authenticated API, not by copying database rows."""
import asyncio
from dataclasses import replace
from datetime import datetime, timezone
import logging
from pathlib import Path

import httpx
from radar_api.config import Settings
from radar_api.investors import PROFILE_FIELDS, DIRECTORY_FIELDS
from radar_api.server import create_app
from capture_company_fields import save

ROOT = Path(__file__).resolve().parents[1]


async def capture():
    logging.getLogger("httpx").setLevel(logging.WARNING)
    settings = replace(Settings.from_env(), allowed_hosts=("capture.local",))
    assert settings.investor_data_dir, "Configure a verified Atlas release directory"
    key = (ROOT / 'secrets/client-key.txt').read_text().strip()
    app = create_app(settings)
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url='http://capture.local', headers={'X-API-Key': key}) as client:
        for slug, fields in [('anupam-mittal', PROFILE_FIELDS), ('fintech-investors-in-bengaluru', DIRECTORY_FIELDS)]:
            for field in [None, *fields]:
                body = {'slug': slug, **({'field': field, 'limit': 5} if field else {})}
                path = '/v1/investors/field' if field else '/v1/investors/page'
                r = await client.post(path, json=body)
                assert r.status_code == 200, (slug, field, r.status_code)
                record = {'operation': 'get_investor_field' if field else 'get_investor_page', 'capture_kind': 'live_gateway',
                          'captured_at': datetime.now(timezone.utc).isoformat(), 'method': 'POST', 'path': path,
                          'request': body, 'http_status': r.status_code, 'response': r.json(),
                          'provenance': 'Authenticated local gateway; live Radar publication check and verified database-derived Atlas release'}
                save(ROOT/'qa/private'/f'investor-{slug}-{field or "summary"}.json', record)
            # Verify that every portfolio/shortlist row is reachable through bounded requests.
            field = 'portfolio' if fields == PROFILE_FIELDS else 'investors'
            offset, count = 0, 0
            while offset is not None:
                r = await client.post('/v1/investors/field', json={'slug': slug, 'field': field, 'limit': 100, 'offset': offset})
                assert r.status_code == 200
                d = r.json()['data']
                count += len(d['value'])
                offset = d['pagination']['next_offset']
            assert count == d['pagination']['source_total']
            save(ROOT/'qa/private'/f'investor-{slug}-pagination-check.json', {'slug': slug, 'field': field, 'reachable_rows': count, 'source_total': count})
            print(slug, len(fields), 'fields; all', count, 'rows reachable', flush=True)


if __name__ == '__main__':
    asyncio.run(capture())
