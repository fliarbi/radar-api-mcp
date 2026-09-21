#!/usr/bin/env python3
"""Retain actual investment and sales-research screens alongside the primary example."""
import json
from pathlib import Path
from build_endpoint_docs import digest, encoded, excerpt

ROOT = Path(__file__).resolve().parents[1]


def build():
    target = ROOT/'docs/examples/opportunities'
    target.mkdir(exist_ok=True)
    manifest = []
    text = '''# Potential-company data: actual investment and sales-research outputs

These are two additional local authenticated gateway captures of
`POST /v1/companies/opportunities/search`. They complement the
[mobile-scale example](reference/search_opportunities.md) and use the same
companies scope, API key and one-credit successful-operation contract.
No source stores, Radar accounts or public deployment were changed.

The profitable-growth screen returned Quantafic Business Solution and Fino Payments
Bank, with recorded revenue display values of $853K and $218.5M. The hiring screen
returned FreeCharge and One97 Communications, with revenue display values of
$36.9M and $902.0M. These are source display columns, not independently verified
financial statements or current purchase intent. Retrieve dated financials and
hiring details before interpreting them. Missing employee/funding cells stay null.

Both captured responses retain the free source plan and exact submitted criteria.
The source supplies no per-row proof explaining every matched predicate; a result
is a source-filtered candidate, not a fully verified investment or sales lead.

'''
    for preset in ('profitable_growth', 'hiring_expansion'):
        raw = json.loads((ROOT/'qa/private'/f'opportunity-{preset}.json').read_text())
        response, omissions = excerpt('search_opportunities', raw['response'])
        record = {**raw, 'capture_kind': 'live_gateway', 'response': response, 'omitted_paths': omissions,
                  'credential_redactions': [], 'hash_basis': 'Parsed JSON with sorted keys',
                  'original_response_sha256': digest(raw['response']), 'response_excerpt_sha256': digest(response)}
        (target/f'{preset}.json').write_text(encoded(record))
        manifest.append({'preset': preset, 'file': preset+'.json', 'response_sha256': digest(response)})
        text += f'''## {preset}

```json
{encoded(raw['request']).rstrip()}
```

<!-- opportunity-response: {preset} -->
```json
{encoded(response).rstrip()}
```

[Download the actual HTTP {raw['http_status']} capture](examples/opportunities/{preset}.json),
recorded {raw['captured_at']}. No business arrays are shortened.

'''
    text += '''Read the [potential company guide](guides/potential-company-data-api.md) for
investment and sales workflows, nested hiring-role filters and source limitations.
Use [company field details](COMPANY_DATA_DEPTH.md) for follow-up evidence and
[contact access](CONTACTS.md) for the separate email/phone retrieval contract.
'''
    (target/'index.json').write_text(encoded(manifest))
    (ROOT/'docs/POTENTIAL_DATA_EXAMPLES.md').write_text(text)
    print('Rendered two additional potential-data captures')


if __name__ == '__main__':
    build()
