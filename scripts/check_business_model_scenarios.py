#!/usr/bin/env python3
"""Validate authored recipes and their evidence without accessing company stores."""
import asyncio
from copy import deepcopy
import hashlib
import json
import re
import shlex

from build_business_model_scenarios import MANIFEST, OfflineUpstream, ROOT
from business_model_cases import CASES
from radar_api.catalog import OPTIONS
from radar_api.config import Settings
from radar_api.service import BY_NAME, Service


def blocks(text, kind):
    matches = re.findall(r'<!-- business-' + kind + r': ([^ ]+) -->\n```json\n(.*?)\n```', text, re.S)
    assert len({key for key, _ in matches}) == len(matches), f'Duplicate {kind} marker'
    return {key: json.loads(body) for key, body in matches}


async def check_catalogue(outputs):
    service = Service(OfflineUpstream(Settings()))
    for key, capture in outputs.items():
        assert capture['capture_kind'] == 'local_code_execution', key
        assert capture['http_executed'] is False and capture['outbound_requests'] == 0, key
        assert capture['request']['field'] in {'industries', 'revenue_models'}, key
        request = BY_NAME['company_filter_options'].model.model_validate(capture['request'])
        assert await service.dispatch('company_filter_options', request) == capture['output'], key


def check_hybrid(page, saved):
    snippets = re.findall(r'```python\n(.*?)\n```', page, re.S)
    assert len(snippets) == 1
    code = compile(snippets[0], '57-hybrid-subscription-and-commission.md', 'exec')

    def outcome(response):
        namespace = {'response': deepcopy(response)}
        exec(code, namespace)
        return namespace['review']

    assert outcome(saved) == 'not both tags in this snapshot'
    assert outcome({}) == 'unknown'
    # These altered inputs are validator fixtures, never published as API results.
    both = deepcopy(saved)
    both['data']['value']['revenue_models'] = ['subscription', 'commission on transaction']
    assert outcome(both) == 'both tags observed'
    for path, value in [
        (('ok',), False),
        (('meta', 'partial'), True),
        (('data', 'status'), 'unavailable'),
        (('data', 'coverage', 'partial'), True),
        (('data', 'coverage', 'arrays', '/value/revenue_models', 'truncated'), True),
        (('data', 'coverage', 'arrays', '/value/revenue_models', 'available'), 3),
        (('data', 'value', 'revenue_models'), None),
    ]:
        changed = deepcopy(both)
        parent = changed
        for key in path[:-1]:
            parent = parent.setdefault(key, {})
        parent[path[-1]] = value
        assert outcome(changed) == 'unknown', path
    missing_coverage = deepcopy(both)
    del missing_coverage['data']['coverage']
    assert outcome(missing_coverage) == 'unknown'


def check():
    manifest = json.loads(MANIFEST.read_text())
    assert len(manifest['recipes']) == len(CASES) == 10
    assert [row['id'] for row in manifest['recipes']] == [case['id'] for case in CASES]
    assert [int(case['id'][:2]) for case in CASES] == list(range(51, 61))
    for source in manifest['sources']:
        assert hashlib.sha256((ROOT / source['file']).read_bytes()).hexdigest() == source['sha256'], source

    saved_options = json.loads((ROOT / 'docs/examples/company_filter_options.json').read_text())
    swiggy = json.loads((ROOT / 'docs/examples/fields/swiggy.com-classification.json').read_text())
    data = swiggy['response']['data']
    saved_projections = {
        'software-options': saved_options['response']['data'],
        'swiggy-models': {
            'domain': data['domain'], 'updated_at': data['updated_at'],
            'revenue_models': data['value']['revenue_models'],
            'marketplace_flag': data['value']['flags']['Marketplace'],
            'revenue_models_coverage': data['coverage']['arrays']['/value/revenue_models'],
        },
    }
    guide = (ROOT / 'docs/guides/business-model-revenue-model-api.md').read_text()
    index = (ROOT / 'docs/scenarios/README.md').read_text()
    assert index.count('<!-- business-model-recipes -->') == 1
    assert index.count('## Original 50 captured scenarios') == 1
    all_requests = {}
    local_seen = set()
    evidence_seen = []
    for case, recipe in zip(CASES, manifest['recipes']):
        assert recipe['status'] == 'schema_validated_recipe'
        assert recipe['company_search_executed'] is False
        page = (ROOT / 'docs/scenarios' / (case['id'] + '.md')).read_text()
        assert '**not a live company-result capture**' in page
        assert 'candidate.example' in page and 'placeholder' in page
        assert f'({case["id"]}.md)' in index
        assert f'(../scenarios/{case["id"]}.md)' in guide
        displayed = blocks(page, 'request')
        expected = {item['key']: item for item in recipe['requests']}
        assert displayed.keys() == expected.keys(), case['id']
        assert not (all_requests.keys() & expected.keys())
        all_requests.update(expected)
        primary = expected[case['id'] + '-search']
        assert primary['operation'] == case['operation'] and primary['request'] == case['request']
        assert expected[case['id'] + '-lookup']['request'] == case['lookup']
        for i, (_, operation, request) in enumerate(case['variants'], 1):
            item = expected[f'{case["id"]}-variant-{i}']
            assert item['operation'] == operation and item['request'] == request
        for key, item in expected.items():
            assert item['request'] == displayed[key], key
            feature = BY_NAME[item['operation']]
            feature.model.model_validate(item['request'])
            assert item['path'] == '/v1/' + feature.path
            heading = f'**POST `{item["path"]}`** · MCP `{item["operation"]}`\n\n<!-- business-request: {key} -->'
            assert heading in page, key
            filters = item['request'].get('filters', {})
            for field in ('industries', 'revenue_models'):
                assert set(filters.get(field, [])) <= set(OPTIONS[field]), key
            assert set(filters.get('business_models', [])) <= set(saved_options['response']['data']['options']), key

        assert blocks(page, 'mcp') == {primary['key']: {
            'name': primary['operation'], 'arguments': {'request': primary['request']}}}
        commands = re.findall(r'```bash\n(.*?)\n```', page, re.S)
        assert len(commands) == 1
        words = shlex.split(commands[0].replace('\\\n', ''))
        assert words[:4] == ['curl', '--fail-with-body', '-sS', '$RADAR_BASE_URL' + primary['path']]
        assert 'Authorization: Bearer $RADAR_API_KEY' in words
        assert 'Content-Type: application/json' in words
        assert json.loads(words[words.index('-d') + 1]) == primary['request']

        for key, value in blocks(page, 'local-output').items():
            assert key not in local_seen
            local_seen.add(key)
            capture = manifest['local_catalog_outputs'][key]
            assert capture['request'] == expected[key]['request']
            assert value == capture['output']
        for key, value in blocks(page, 'saved-output').items():
            assert value == saved_projections[key]
            evidence_seen.append(key)
        if case.get('evidence') == 'hybrid':
            check_hybrid(page, swiggy['response'])

    assert len(all_requests) == 62
    assert local_seen == manifest['local_catalog_outputs'].keys() and len(local_seen) == 8
    assert sorted(evidence_seen) == ['software-options', 'swiggy-models', 'swiggy-models']
    for key, request in blocks(guide, 'request').items():
        assert request == all_requests[key]['request']
    asyncio.run(check_catalogue(manifest['local_catalog_outputs']))
    print('Validated 10 business-model recipes: 62 request bodies, 10 curl/MCP calls, '
          '8 offline catalogue outputs, saved evidence and hybrid coverage checks; no upstream calls')


if __name__ == '__main__':
    check()
