#!/usr/bin/env python3
"""Build ten schema-validated monetization recipes; never query company stores."""
import asyncio
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shlex

from business_model_cases import CASES
from radar_api.catalog import OPTIONS
from radar_api.config import Settings
from radar_api.service import BY_NAME, Service
from radar_api.upstream import Upstream

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/research/business-model-recipes.json"


class OfflineUpstream(Upstream):
    async def call(self, *args, **kwargs):
        raise AssertionError("Recipe generation must not make upstream requests")


def encoded(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def step(key, label, operation, request):
    BY_NAME[operation].model.model_validate(request)
    for field in ("industries", "revenue_models"):
        assert set(request.get("filters", {}).get(field, [])) <= set(OPTIONS[field]), (key, field)
    return {"key": key, "label": label, "operation": operation,
            "path": "/v1/" + BY_NAME[operation].path, "request": request}


def request_block(item):
    return (f'**POST `{item["path"]}`** · MCP `{item["operation"]}`\n\n'
            f'<!-- business-request: {item["key"]} -->\n```json\n{encoded(item["request"]).rstrip()}\n```\n')


def insert_index_section():
    path = ROOT / "docs/scenarios/README.md"
    text = path.read_text()
    text = re.sub(r'\n<!-- business-model-recipes -->.*?<!-- /business-model-recipes -->\n', '\n', text, flags=re.S)
    text = text.replace('# 50 executed Radar API questions and full response examples',
                        '# Radar API scenarios: captured examples and business-model recipes')
    text = text.replace('Each page has an exact REST/MCP request, captured output, baseline comparison and\ninterpretation.',
                        'Scenarios 01–50 have exact REST/MCP requests, captured outputs, baseline comparisons\nand interpretation.')
    intro = '''
<!-- business-model-recipes -->
## Business-model and revenue-model scenarios

Start with [investment companies earning commission per deal](51-investment-commission-per-deal.md).
These **10 additional recipes (51–60)** have validated REST/MCP requests and field
review steps. Their company searches have **not been executed** against live stores;
no matching company list or live result count is claimed. Local vocabulary outputs
and historical classification evidence are labeled separately.

| Scenario | Business question |
|---|---|
'''
    intro += ''.join(f'| [{c["id"]}]({c["id"]}.md) | {c["title"]} |\n' for c in CASES)
    intro += '\n[Business-model filter guide](../guides/business-model-revenue-model-api.md) explains commission labels, OR/AND matching, investor portfolio semantics and separate field reads.\n<!-- /business-model-recipes -->\n\n## Original 50 captured scenarios\n'
    # Remove the generated heading when refreshing this section.
    text = text.replace('\n## Original 50 captured scenarios\n', '\n')
    first, rest = text.split('\n', 1)
    path.write_text(first + '\n' + intro + '\n' + rest.lstrip())


async def build():
    service = Service(OfflineUpstream(Settings()))
    records = []
    local_outputs = {}
    for case in CASES:
        base = case['id']
        requests = [step(base + '-lookup', 'Discover the relevant vocabulary', 'company_filter_options', case['lookup']),
                    step(base + '-search', 'Search the candidate cohort', case['operation'], case['request'])]
        for i, (label, operation, request) in enumerate(case['variants'], 1):
            requests.append(step(f'{base}-variant-{i}', label, operation, request))
        requests.extend([
            step(base + '-columns', 'Add listing columns to reviewed domains', 'get_company_columns',
                 {'domains': ['candidate.example'], 'columns': ['industry', 'business_model', 'revenue_model', 'country', 'latest_revenue']}),
            step(base + '-profile', 'Discover available company detail fields', 'get_company', {'domain': 'candidate.example'}),
            step(base + '-classification', 'Read company classifications separately', 'get_company_field',
                 {'domain': 'candidate.example', 'field': 'classification', 'item_limit': 100}),
        ])
        if case['lookup']['field'] != 'business_models':
            lookup = requests[0]
            local_outputs[lookup['key']] = {
                'capture_kind': 'local_code_execution', 'http_executed': False,
                'outbound_requests': 0, 'request': lookup['request'],
                'output': await service.dispatch('company_filter_options', BY_NAME['company_filter_options'].model.model_validate(lookup['request'])),
            }
        records.append({'id': base, 'title': case['title'], 'status': 'schema_validated_recipe',
                        'company_search_executed': False, 'requests': requests})
        page = f'''# {case['title']}

[Scenario index](README.md) · [Business/revenue-model guide](../guides/business-model-revenue-model-api.md)

**Business question:** {case['question']}

**Validation status:** request schemas and known catalogue values checked locally.
The company search is an authored recipe, **not a live company-result capture**.
The original [50 captured scenarios](README.md#original-50-captured-scenarios) remain separate.

## Discover the filter vocabulary

{request_block(requests[0])}
'''
        lookup_key = requests[0]['key']
        if lookup_key in local_outputs:
            page += f'''The following is the actual local output of the catalogue handler. This lookup
used no company-store connection and was not an HTTP/live-company search.

<!-- business-local-output: {lookup_key} -->
```json
{encoded(local_outputs[lookup_key]['output']).rstrip()}
```
'''
        elif case.get('evidence') == 'software':
            saved = json.loads((ROOT / 'docs/examples/company_filter_options.json').read_text())
            page += f'''The [saved lookup](../examples/company_filter_options.json), captured on
{saved['captured_at'][:10]}, returned these exact values. This is historical vocabulary evidence.

<!-- business-saved-output: software-options -->
```json
{encoded(saved['response']['data']).rstrip()}
```
'''
        else:
            page += 'This business-model lookup depends on Radar\'s upstream vocabulary service. No fresh\noptions were captured for this recipe. Select a returned value; do not assume the\nquery text itself is a valid `business_models` value.\n'
        primary = requests[1]
        curl_body = shlex.quote(json.dumps(primary['request'], ensure_ascii=False, separators=(',', ':')))
        page += f'''
## Main request

{request_block(primary)}
{case['interpretation']}

Set `RADAR_BASE_URL` to your operator-supplied gateway and `RADAR_API_KEY` to your
issued key ([onboarding](../guides/api-keys-authentication.md)). Run from Bash:

```bash
curl --fail-with-body -sS "$RADAR_BASE_URL{primary['path']}" \\
  -H "Authorization: Bearer $RADAR_API_KEY" \\
  -H 'Content-Type: application/json' \\
  -d {curl_body}
```

Equivalent MCP tool call:

<!-- business-mcp: {primary['key']} -->
```json
{encoded({'name': primary['operation'], 'arguments': {'request': primary['request']}}).rstrip()}
```

## Related request variants

'''
        for variant in requests[2:-3]:
            page += f'### {variant["label"]}\n\n{request_block(variant)}\n'
        page += f'''## Inspect the returned company’s own model

Search cards are compact. Use `data.companies[].domain` from a reviewed result;
**`candidate.example` below is a placeholder, not a claimed company match**.
Column batches accept up to 20 domains. Column values are formatted summaries,
not precise dated financial facts.

{request_block(requests[-3])}
{request_block(requests[-2])}
Inspect `available_fields` and `field_status` before the separate field read:

{request_block(requests[-1])}
Keep `data.value.business_models`, `data.value.revenue_models`, `data.updated_at`,
`data.status`, `data.coverage.partial` and the array coverage for
`/value/revenue_models`. An unavailable field is unresolved evidence, not an empty
business model. Use a separate `overview` or `products` field read when listed as
available and inspect dated source pricing/terms for fee details the API does not contain.

| Evidence to review | How to interpret it |
|---|---|
'''
        page += ''.join(f'| {label} | {meaning} |\n' for label, meaning in case['review'])
        page += f'''
{case['pitfall']}

## Accept, reject or leave unresolved

Check `data.matching.filters_restricted`, each card’s `match_tier`, excluded
candidates, access limits and partial results. `strict` means the source labelled
the candidate strict and retained the requested filters; it is not independent
verification of the commercial model. Semantic wording still needs review.

Follow `data.next_page` even when a strict page returns no companies: that page
may have contained only excluded candidates. Keep filters fixed, stop when the
continuation hint is absent or the allowed page bound is reached, and deduplicate
by domain. An empty page or failed upstream read does not prove the segment is empty.

For a final export, retain the domain, source model labels, classification date,
review status and any pricing/terms evidence. Leave unsupported rates, billing
events and revenue shares unknown. The [guide’s evidence table](../guides/business-model-revenue-model-api.md#build-a-reviewable-result)
separates API fields from client-reviewed conclusions.
'''
        if case.get('evidence') in {'hybrid', 'swiggy'}:
            capture = json.loads((ROOT / 'docs/examples/fields/swiggy.com-classification.json').read_text())
            data = capture['response']['data']
            projection = {'domain': data['domain'], 'updated_at': data['updated_at'],
                          'revenue_models': data['value']['revenue_models'], 'marketplace_flag': data['value']['flags']['Marketplace'],
                          'revenue_models_coverage': data['coverage']['arrays']['/value/revenue_models']}
            page += f'''
## Saved evidence: a marketplace flag is not a commission tag

This is a selected-field projection from the [complete saved Swiggy classification](../examples/fields/swiggy.com-classification.json),
captured {capture['captured_at'][:10]}. It is not a response to this new search.

<!-- business-saved-output: swiggy-models -->
```json
{encoded(projection).rstrip()}
```

The snapshot includes a Marketplace flag and subscription/e-commerce service tags,
but no `commission on transaction` label. It therefore does not support a
subscription-plus-commission tag match. It also does not prove what Swiggy’s actual
commercial contracts charge. Do not fill the missing label from brand familiarity.
'''
        if case.get('evidence') == 'hybrid':
            page += '''
## Require both tags in the client

The API request above is an OR search. Given a saved or newly returned
`get_company_field` response, this client-side check retains an explicit unknown
state when coverage is unavailable. It evaluates the observed snapshot only.

```python
required = {"subscription", "commission on transaction"}
data = response.get("data") or {}
coverage = data.get("coverage") or {}
array = (coverage.get("arrays") or {}).get("/value/revenue_models") or {}
models = (data.get("value") or {}).get("revenue_models")
if (not response.get("ok") or data.get("status") != "available"
        or (response.get("meta") or {}).get("partial")
        or coverage.get("partial") is not False or array.get("truncated") is not False
        or not isinstance(models, list) or not all(isinstance(v, str) for v in models)
        or array.get("returned") != len(models) or array.get("available") != len(models)):
    review = "unknown"
else:
    observed = {v.casefold() for v in models}
    review = "both tags observed" if required <= observed else "not both tags in this snapshot"
```

The saved Swiggy example evaluates to `not both tags in this snapshot`. A missing
classification must evaluate to `unknown`. A future pricing check is a separate
review outcome; do not label the catalogue test as fee verification.
'''
        (ROOT / 'docs/scenarios' / (base + '.md')).write_text(page)
    sources = ['radar_api/catalog.py', 'radar_api/models.py', 'radar_api/service.py', 'radar_api/industry_options.py',
               'docs/examples/company_filter_options.json', 'docs/examples/fields/swiggy.com-classification.json']
    manifest = {'scope': 'Ten schema-validated business-model recipes; company searches not executed',
                'review_date': datetime.now(timezone.utc).date().isoformat(),
                'source_review': 'Reviewed Radar company-search and semantic-search filter routing, revenue options and investor portfolio rewrites. No store query was executed.',
                'sources': [{'file': name, 'sha256': hashlib.sha256((ROOT / name).read_bytes()).hexdigest()} for name in sources],
                'recipes': records, 'local_catalog_outputs': local_outputs}
    MANIFEST.write_text(encoded(manifest))
    insert_index_section()
    print(f'Built {len(records)} recipes, {sum(len(r["requests"]) for r in records)} validated requests and {len(local_outputs)} offline catalogue outputs; no upstream calls.')


if __name__ == '__main__':
    asyncio.run(build())
