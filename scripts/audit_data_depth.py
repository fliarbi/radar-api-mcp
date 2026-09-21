#!/usr/bin/env python3
"""Prevent business data from being silently stripped by documentation rendering."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE_OR_SCHEMA = {'headline', 'biography', 'bio', 'snippets', 'gender', 'input_schema', 'body', 'lede',
                   'full_text', 'meta_description', 'source_sentence', 'description', 'description_snippet', 'snippet'}


def dimensions(value, path='data'):
    leaves, arrays = 0, {}
    if isinstance(value, dict):
        for k, child in value.items():
            n, a = dimensions(child, path+'/'+k)
            leaves += n
            arrays.update(a)
    elif isinstance(value, list):
        arrays[path] = len(value)
        for i, child in enumerate(value):
            n, a = dimensions(child, path+'/'+str(i))
            leaves += n
            arrays.update(a)
    else:
        leaves = 1
    return leaves, arrays


def audit():
    manifest = json.loads((ROOT/'docs/examples/index.json').read_text())
    rows = []
    for item in manifest:
        name = item['operation']
        record = json.loads((ROOT/'docs/examples'/f'{name}.json').read_text())
        omissions = record['omitted_paths']
        if name != 'openapi':
            assert all(p.rsplit('/', 1)[-1] in PROSE_OR_SCHEMA for p in omissions), (name, 'Business field omitted', omissions)
        data = record['response'].get('data')
        leaves, arrays = dimensions(data)
        rows.append({'operation': name, 'http_status': record['http_status'], 'capture_kind': record['capture_kind'],
                     'data_keys': list(data) if isinstance(data, dict) else [], 'scalar_values': leaves,
                     'array_lengths': arrays, 'omitted_paths': omissions,
                     'request': record['request'], 'response_sha256': record['response_excerpt_sha256']})
    records = {row['operation']: row for row in rows}
    for field in ('education', 'skills', 'scores', 'top_experience', 'founder', 'investor'):
        person = json.loads((ROOT/'docs/examples/search_people.json').read_text())['response']['data']['people'][0]
        assert field in person, 'Professional detail omitted: '+field
    investor = json.loads((ROOT/'docs/examples/get_investor_page.json').read_text())['response']['data']
    assert investor['profile_depth'] == 'summary' and investor['metrics']['total_companies'] == 270
    assert investor['field_counts']['portfolio'] == 268
    assert 'available_fields' in records['get_company']['data_keys']
    assert len(json.loads((ROOT/'docs/examples/investors/index.json').read_text())) == 21
    return {'scope': 'Every primary endpoint capture; business structures, explicit omissions and request bounds',
            'operations': len(rows), 'investor_supplemental_captures': 21, 'company_field_captures': 54, 'app_field_captures': 7, 'examples': rows}


def build():
    report = audit()
    (ROOT/'docs/DATA_DEPTH_AUDIT.json').write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n')
    text = '''# Response depth audit: source data, API retrieval and documentation

The previous investor adapter called a public publication-metadata route and
never reached the database-derived profile. Separately, the docs renderer reduced
professional profiles to seven identity fields. Both were implementation gaps.
A successful HTTP response and correct checksum alone did not detect them.

The investor adapter now reads the verified Atlas business snapshot after the live
publication gate; separate fields expose portfolio rows, sectors, stages, activity,
cohorts, co-investors, research and news. Professional examples now retain skills,
education, experience, founder/investor attributes, scores and access indicators.
Short financial/funding headlines are retained instead of categorically removed.

## What the audit checks

Every primary capture is inventoried below. The machine-readable report lists all
returned top-level keys, nested array lengths, scalar counts, exact request and
omitted paths. Counts measure the example's shape, not source completeness or
accuracy. Request limits explain intentionally small result pages. The renderer
must retain every business field and every returned array row. Only named source
prose, sensitive demographics and embedded discovery schemas may be omitted.
Local checks compare rendered records to original gateway responses; CI checks
fingerprints, expected rich fields and the checked-in inventory.

## Where source depth enters the API

| Data | Source path inspected | Retrieval boundary |
|---|---|---|
| Company identity and native fields | Mongo grouped profile and enrichment records | Compact identity; one fixed-projection field per POST; 54 captures |
| Investor portfolios and research | Published Atlas data built from ClickHouse equity records and reviewed news | Verified release hash and live publication gate; 19 fields across two page types; bounded portfolio/shortlist pages |
| People | Radar people-search response | Preserve all returned non-contact professional attributes in the docs |
| Financial statements and intelligence | Radar company intelligence and earnings | Preserve fiscal periods, metrics, currency, provenance and source-plan limits |
| Funding and events | Radar funding summary and event handlers | Preserve returned rounds, associations and headlines; event window can be empty or gated |
| Company enrichment | Radar enrichment response | Preserve all supplied digital, hiring, innovation, legal and reputation sections; unknown source failures stay documented |
| Company/investor search and competitors | Radar company search and segment handlers | Bounded cards with source restrictions; cards are not the detailed profile |
| General/business/funding news | Actual News applications and live archive queries | Isolated integration identity explicitly labeled; no production-connection claim |
| Individual apps | ClickHouse app profiles, growth, velocity and install history | Compact app profile plus seven selected fields; exact developer-host company association; no developer contacts |
| Dedicated internships | Mongo internship records selected by posting type | Skill/stipend/date filters, exact-name employer groups, description detail and explicit vacancy-status uncertainty |
| Company potential | Radar company filters plus measured display columns | Six transparent growth/investment and B2B prospecting screens; preserve source restrictions and partial evidence |
| Jobs and salary | Radar job handlers | Preserve structured listing fields, salary distributions, sample sizes and paging; long job prose is omitted only from docs |
| Contact retrieval | Existing Radar paid contact handlers | Separate explicit scope and linked source account; primary captures show real default-key denials |

## Primary examples

| Operation | HTTP | Scalar values | Arrays | Prose/schema omissions |
|---|---:|---:|---:|---:|
'''
    for row in report['examples']:
        name = row['operation']
        text += f"| [{name}](reference/{name}.md) | {row['http_status']} | {row['scalar_values']} | {len(row['array_lengths'])} | {len(row['omitted_paths'])} |\n"
    text += '''
## Remaining limits are not described as complete data

The location-intelligence source still fails. Microsoft's captured recent event
window is empty and source-plan limited. Paid contact success has not been
verified with a live entitled account. Investor search still includes a source
identity ambiguity; it searches investor-classified companies, not every angel.
The investor dataset is a dated reviewed release, not a real-time feed; directory
shortlists are selected subsets. API schemas and rich captures do not establish
that every company or investor has every field.

See [all investor field captures](INVESTOR_DATA_DEPTH.md), [all company fields](COMPANY_DATA_DEPTH.md),
[error and coverage audit](EXAMPLE_AUDIT.md) and [machine-readable depth inventory](DATA_DEPTH_AUDIT.json).
'''
    (ROOT/'docs/DATA_DEPTH_AUDIT.md').write_text(text)
    print(f"Depth audit passed for {report['operations']} primary captures")


if __name__ == '__main__':
    build()
