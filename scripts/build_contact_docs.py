#!/usr/bin/env python3
"""Render complete recorded contact evidence and validated workflow recipes."""
import json
from pathlib import Path
from build_endpoint_docs import encoded
from contact_workflow_notes import VARIANTS, CONTACT_EVIDENCE, GUIDE_EVIDENCE
from radar_api.service import BY_NAME

ROOT = Path(__file__).resolve().parents[1]


def evidence_section(entries):
    text = "\n<!-- contact-evidence -->\n"
    for title, source in entries:
        record = json.loads((ROOT / "docs/examples" / source).read_text())
        kind = record["capture_kind"]
        note = ("**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made."
                if kind == "local_contact_fixture" else
                "**Recorded live gateway response.** This capture is historical evidence, not a fresh health or identity verification.")
        interpretation = (' ' + record['interpretation']) if record.get('interpretation') else ''
        text += f'''\n### {title}

**`{record['method']} {record['path']}`** · MCP **`{record['operation']}`**.
{note}
Captured **{record['captured_at']}**, HTTP **{record['http_status']}**,
mode **`{kind}`**.{interpretation}

Exact executed request:

<!-- contact-captured-request: {source} -->
```json
{encoded(record['request']).rstrip()}
```

Complete saved response:

<!-- contact-captured-response: {source} -->
```json
{encoded(record['response']).rstrip()}
```

[Capture, provenance and checksums](@@PREFIX@@examples/{source}).
'''
    return text


def build():
    paths = {ROOT / 'docs/CONTACTS.md': CONTACT_EVIDENCE,
             **{ROOT / 'docs/guides' / (name + '.md'): entries for name, entries in GUIDE_EVIDENCE.items()}}
    for path, entries in paths.items():
        base = path.read_text().split('<!-- contact-evidence -->')[0].rstrip()
        prefix = '../' if path.parent.name == 'guides' else ''
        path.write_text(base + '\n' + evidence_section(entries).replace('@@PREFIX@@', prefix))
    requests = []
    for variant in VARIANTS:
        feature = BY_NAME[variant['operation']]
        feature.model.model_validate(variant['request'])
        requests.append({**variant, 'method': 'POST', 'path': '/v1/' + feature.path})
    target = ROOT / 'docs/examples/contacts'
    target.mkdir(exist_ok=True)
    (target / 'requests.json').write_text(encoded(requests))
    recipes = '''# Contact request recipes: founders, professionals, company emails and social links

These 24 request bodies validate against the current API models. They are accepted
syntax examples, not claims that every query was executed or returned results.
Replace `ID_FROM_ACCEPTED_PROFILE` with an ID you accepted from professional discovery.

Use your API key with each POST request. For MCP, call the named tool with
`arguments.request` set to the same JSON body. Contact requests additionally need
an entitled linked Radar account. See [contact access, output and errors](CONTACTS.md),
[founder identity and details](guides/founder-contact-data-api.md),
[company/professional emails](guides/company-email-phone-api.md), and
[LinkedIn/social references](guides/linkedin-social-data-api.md).

Real discovery responses and clearly labelled synthetic contact outputs are
preserved in those guides. [Download the machine-readable recipes](examples/contacts/requests.json).
'''
    for item in requests:
        recipes += f'''
## {item['question']}

**`POST {item['path']}`** · MCP **`{item['operation']}`** ·
Required key scopes: {', '.join('`' + s + '`' for s in item['scopes'])}.

<!-- contact-recipe: {item['id']} -->
```json
{encoded(item['request']).rstrip()}
```

{item['interpretation']}
'''
    (ROOT / 'docs/CONTACT_REQUEST_RECIPES.md').write_text(recipes)
    records = []
    for path in sorted(target.glob('*.json')):
        if path.name in {'index.json', 'requests.json'}:
            continue
        item = json.loads(path.read_text())
        records.append({k: item[k] for k in ('operation', 'request', 'capture_kind', 'captured_at', 'http_status', 'response_excerpt_sha256')})
        records[-1]['file'] = path.name
    (target / 'index.json').write_text(encoded(records))
    print(f'Rendered {len(CONTACT_EVIDENCE)} contact examples and {sum(map(len, GUIDE_EVIDENCE.values()))} specialist-guide examples; validated {len(requests)} recipes')


if __name__ == '__main__':
    build()
