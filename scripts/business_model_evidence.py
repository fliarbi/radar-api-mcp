"""Render immutable gateway captures beside the exact business-model requests."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAPTURES = ROOT / 'docs/examples/business-models'


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def captures(case_id):
    files = [CAPTURES / f'{case_id}-{suffix}.json' for suffix in ('search', 'profile', 'classification')]
    return [(file.name, json.loads(file.read_text())) for file in files if file.exists()]


def summary(record):
    response = record['response']
    data = response.get('data') or {}
    if not response.get('ok'):
        return f"HTTP {record['http_status']}: {(response.get('error') or {}).get('kind', 'error')}"
    return f"HTTP {record['http_status']}: {len(data.get('companies') or [])} returned companies"


def render(case_id):
    rows = captures(case_id)
    if not rows:
        return ''
    first = rows[0][1]
    data = first['response'].get('data') or {}
    matching = data.get('matching') or {}
    text = f'''## Captured output for this exact request

**{summary(first)}**, captured **{first['captured_at']}** through the authenticated
local gateway calling its configured Radar source. This is an actual response,
including empty results and denials. Retrieval time does not certify the age of
the underlying source or independently verify a company's fee contract.

'''
    if first['http_status'] == 403:
        text += ('The linked session was denied access. A separate diagnostic with that session\n'
                 'returned `login_required`; reconnect a current Radar session before retrying.\n'
                 'This response establishes no matching-company count. See [API-key and session help](../guides/api-keys-authentication.md).\n\n')
    elif data.get('companies'):
        text += '| Returned company | Domain | Source matching tier |\n|---|---|---|\n'
        for company in data['companies']:
            values = [company.get('name'), company.get('domain'), company.get('match_tier')]
            text += '| ' + ' | '.join(str(v or 'Unknown').replace('|', '&#124;').replace('\n', ' ') for v in values) + ' |\n'
        text += '\nThese are source-matched candidates. The classification read below inspects one\nreturned domain; it does not verify all companies or their pricing terms.\n\n'
    else:
        text += (f"The source supplied **{matching.get('source_rows', 0)} candidates**; strict filtering\n"
                 f"excluded **{matching.get('excluded_candidates', 0)}** on this page. ")
        if data.get('next_page') is not None:
            text += f"`next_page={data['next_page']}` remains available. "
        text += 'An empty strict page is not proof that no such business exists.\n\n'
    for filename, record in rows:
        key = filename.removesuffix('.json')
        if record is not first:
            text += f'### Captured `{record["operation"]}` for a returned company\n\n'
            text += f'POST `{record["path"]}`, HTTP **{record["http_status"]}**, captured **{record["captured_at"]}**.\n\n'
            text += f'<!-- business-live-request: {key} -->\n```json\n{json.dumps(record["request"], indent=2)}\n```\n\n'
        text += f'<details open>\n<summary>Complete captured {record["operation"]} response</summary>\n\n'
        text += f'<!-- business-live-response: {key} -->\n```json\n{json.dumps(record["response"], ensure_ascii=False, indent=2)}\n```\n\n</details>\n\n'
        text += f'[Download this request and full response](../examples/business-models/{filename}). '
        text += 'All returned fields and rows are preserved; SHA-256 fingerprints are included.\n\n'
    if case_id.startswith('54-'):
        text += ('The returned Star Health classification includes `commission on transaction`,\n'
                 'but that label does not establish that it is a broker. Review the company’s\n'
                 'actual role before accepting it into an insurance-distributor list.\n\n')
    if case_id.startswith('57-'):
        text += ('The returned EMudhra classification contains both `subscription` and\n'
                 '`commission on transaction`. This establishes both tags in that snapshot;\n'
                 'it does not establish their revenue shares or the current fee schedule.\n\n')
    return text
