#!/usr/bin/env python3
"""Refresh just the three social examples through the authenticated local gateway.

Requires operator-supplied profile and social read connections. Uses the existing
preview key; does not create accounts, reveal contacts or update source records.
"""
import json
import logging
from dataclasses import replace
from pathlib import Path

from fastapi.testclient import TestClient

from capture_company_fields import save
from radar_api.config import Settings
from radar_api.server import create_app

ROOT = Path(__file__).resolve().parents[1]


def capture():
    logging.getLogger('httpx').setLevel(logging.WARNING)
    settings = replace(Settings.from_env(), allowed_hosts=('testserver',))
    assert settings.profile_mongo_uri and settings.social_ch_url, 'Configure both read connections privately'
    key = (ROOT / 'secrets/client-key.txt').read_text().strip()
    with TestClient(create_app(settings)) as client:
        for domain in ('razorpay.com', 'stripe.com', 'swiggy.com'):
            body = {'domain': domain, 'field': 'social', 'item_limit': 100}
            response = client.post('/v1/companies/field', json=body, headers={'X-API-Key': key})
            assert response.status_code == 200, (domain, response.status_code)
            data = response.json()
            linkedin = data['data']['value']['linkedin']
            assert all(s['status'] != 'unavailable' for s in linkedin['coverage'].values()), domain
            save(ROOT / 'qa/private' / ('field-' + domain + '-social.json'), {'request': body, 'response': data})
            print(json.dumps({'domain': domain, 'status': data['data']['status'],
                              'profiles': len(linkedin['profile_history']), 'posts': len(linkedin['recent_posts'])}))


if __name__ == '__main__':
    capture()
