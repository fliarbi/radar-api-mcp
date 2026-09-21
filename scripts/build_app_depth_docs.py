#!/usr/bin/env python3
"""Publish separate measured app fields without shortening business arrays."""
import json
from pathlib import Path
from build_endpoint_docs import digest, encoded, excerpt
from radar_api.apps import APP_FIELDS

ROOT = Path(__file__).resolve().parents[1]


def build():
    target = ROOT/'docs/examples/apps'
    target.mkdir(exist_ok=True)
    manifest = []
    text = '''# App data depth: seven separate live field responses

These captures used the local authenticated gateway against Radar's stored
Google Play data. They do not prove public deployment or a current store refresh.
The app is `in.swiggy.android`; its profile reports 15 stored history rows.
The live pagination audit found 13 duplicate rows, leaving two distinct
observations. The API preserves the source sequence and explicitly reports that
history is not deduplicated. Do not treat those rows as 15 distinct dates.
All business fields and returned array rows are retained. Long listing prose is
omitted explicitly, with its original-response hash preserved in the JSON record.

Use [app discovery and field requests](guides/apps-data-api.md) to reproduce the
workflow. Responses below correspond to one selected field per POST, not a single
oversized company or app profile. Developer contacts are not included.

'''
    for field in APP_FIELDS:
        raw = json.loads((ROOT/'qa/private'/f'app-swiggy-{field}.json').read_text())
        assert raw['http_status'] == 200
        response, omissions = excerpt('get_app_field', raw['response'])
        record = {**raw, 'capture_kind': 'live_gateway', 'response': response, 'omitted_paths': omissions,
                  'credential_redactions': [], 'hash_basis': 'Parsed JSON with sorted keys',
                  'original_response_sha256': digest(raw['response']), 'response_excerpt_sha256': digest(response)}
        filename = 'swiggy-'+field+'.json'
        (target/filename).write_text(encoded(record))
        manifest.append({'file': filename, 'field': field, 'response_sha256': digest(response)})
        text += f'''## {field}

POST `/v1/apps/field`:

```json
{encoded(raw['request']).rstrip()}
```

<!-- app-field-response: {field} -->
```json
{encoded(response).rstrip()}
```

[Download this captured response](examples/apps/{filename}). HTTP 200 captured
{raw['captured_at']}. Omitted paths: {', '.join('`'+p+'`' for p in omissions) or 'none'}.

'''
    text += '''## Interpret dates, estimates and flags

The growth example compares 223,179,065 and 281,013,619 recorded installs across
360 days. Its 25.91% observed change and 26.32% annualized change are different
quantities. `reliable` and `release_date_suspect` remain visible, including zero.
Install totals are source estimates, not monthly users or revenue. Observation
timestamps are normalized to UTC. Source release text and update epoch retain
their original formats. Install-history pagination exposes `source_total` and
`next_offset`; each response contains every requested row without docs truncation.

See [profile output](reference/get_app.md), [exact-domain company app output](reference/company_apps.md)
and [potential-company evidence](guides/potential-company-data-api.md).
'''
    (target/'index.json').write_text(encoded(manifest))
    (ROOT/'docs/APP_DATA_DEPTH.md').write_text(text)
    print('Rendered seven actual app field responses')


if __name__ == '__main__':
    build()
