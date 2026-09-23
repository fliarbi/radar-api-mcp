#!/usr/bin/env python3
"""Record source ownership and before/after live output shapes for every operation.

Reads ignored authenticated captures; exports bounded review metadata and genuine
error envelopes, never raw upstream payloads or operator connection settings.
"""
import hashlib
import json
from pathlib import Path

from radar_api.service import BY_NAME
from build_endpoint_docs import digest, encoded

ROOT = Path(__file__).resolve().parents[1]
GROUPS = [
    ('Company discovery', 'radar_api/service.py',
     'Bounded company/investor cards and matching metadata; rich company values belong to companies/field.',
     'Source company search, semantic search and segment summary cards; retained access and matching metadata.',
     ['search_companies', 'semantic_company_search', 'search_investors', 'find_competitors']),
    ('Compact company identity', 'radar_api/profiles.py',
     'Identity and existence only; contacts return availability, never values.',
     'Fixed Mongo summary projection plus existence-only LinkedIn/traffic/review queries.', ['get_company']),
    ('Selected company detail', 'radar_api/profiles.py',
     'One required field, bounded arrays and source coverage. Financial history and contacts have separate owners.',
     'Grouped Mongo projections, derived enrichment and explicit LinkedIn, traffic and review observations.', ['get_company_field']),
    ('Company discovery schema', 'radar_api/catalog.py',
     'Typed filter vocabulary and explicit listing columns; display numbers do not replace financial evidence.',
     'Reviewed Radar filter contract, typeahead and allowlisted column hydration.',
     ['company_filter_catalog', 'company_filter_options', 'get_company_columns']),
    ('Financial research', 'radar_api/research.py',
     'Entitled normalized periods and bounded candidate screening; no archive bypass or implicit universe-wide screen.',
     'Caller-authenticated Radar company intelligence earnings; period/source/currency context retained.',
     ['financial_filter_catalog', 'screen_company_financials', 'get_financials']),
    ('Company team', 'radar_api/research.py',
     'Company key people/founders or exact recorded employer affiliation. Contact reveal remains separate.',
     'Selected company people field and bounded Radar professional search.', ['get_company_team']),
    ('Company assessments and events', 'radar_api/service.py',
     'Existing intelligence, event, funding and enrichment contracts retain their source business structures. Native deep observations are added only to selected fields.',
     'Caller-authenticated company intelligence, activity, funding and company enrichment responses.',
     ['get_company_intelligence', 'get_company_events', 'get_company_funding', 'get_company_enrichment']),
    ('Compact research composition', 'radar_api/company_views.py',
     'Concise section summaries and separate detail requests; no embedded rosters or full selected-field payloads.',
     'Existing gated component endpoints; preserve individual failure and window information.', ['company_brief', 'compare_companies']),
    ('Investor data', 'radar_api/investors.py',
     'Directory discovery, compact profile metrics and explicitly selected portfolio/analysis fields. Preserve publication gates and exclude restricted contact/social identity.',
     'Live Radar publication gate and immutable Atlas business snapshot with SHA-256 verification.',
     ['investor_directory', 'get_investor_page', 'get_investor_field']),
    ('Market and geographic discovery', 'radar_api/service.py',
     'Source aggregates, windows and typed industry matches; no fabricated replacement for unavailable geography.',
     'Radar market pulse, analytical location and metadata discovery.', ['market_pulse', 'location_intelligence', 'discover_industries']),
    ('Jobs and salaries', 'radar_api/service.py',
     'Search cards, full stored job detail, bounded employer rollup and salary samples. Salary periods/currencies are not silently normalized.',
     'Radar job search/detail, suggestion vocabulary and salary aggregation.',
     ['search_jobs', 'job_filter_catalog', 'job_filter_options', 'companies_hiring', 'get_job', 'salary_benchmark']),
    ('Internship data', 'radar_api/internships.py',
     'Dedicated internship records; first observation and direct-apply flag belong to detail. Employer names are not guessed domain joins.',
     'Fixed projection on the dedicated internship corpus, including source validity and observation dates.',
     ['search_internships', 'companies_offering_internships', 'get_internship']),
    ('App data', 'radar_api/apps.py',
     'App cards and compact profiles discover seven explicit fields. Install bands, releases, ratings and prices stay in their selected detail; no developer contacts.',
     'Play Store app records, install observations and measured growth/velocity tables.',
     ['company_apps', 'search_apps', 'get_app', 'get_app_field', 'app_filter_options']),
    ('Potential-company research', 'radar_api/opportunities.py',
     'Ranked research candidates and observed investment/sales evidence; no claimed predictive probability or contact dump.',
     'Reviewed presets and existing bounded company reads with coverage/unknown flags.', ['opportunity_presets', 'search_opportunities']),
    ('Professional discovery', 'radar_api/service.py',
     'Bounded professional cards retain skills, education, experience, roles, scores and public profile links; contact retrieval is explicit.',
     'Radar people search and suggestions; preserve linked-account access flags.', ['search_people', 'people_filter_options']),
    ('Scoped contacts', 'radar_api/company_views.py',
     'Only explicitly requested email/phone types after scope and paid-plan checks. Contact origin and fallback remain visible.',
     'Caller-authenticated company/person contact endpoints. Live audit key intentionally lacks contacts scope.', ['get_company_contacts', 'get_person_contacts']),
    ('News and business evidence', 'radar_api/upstream.py',
     'Preserve upstream news/event/article structures, cursors and dates. A strict coverage failure returns no partial corpus totals.',
     'Actual News/business app queries under an isolated test identity with plan and coverage gates retained; production News auth is not verified.',
     ['search_news', 'search_business_news', 'news_overview', 'news_trends', 'news_sentiment', 'search_business_events', 'search_funding_news', 'get_article']),
]
CHANGES = {
    'get_company': 'Adds existence-only discovery for underlying traffic/review observations; compact company values unchanged.',
    'get_company_field': 'Adds selected traffic/review observations, structured sector context, lifecycle milestones and assessment rationale; existing fields retained.',
    'get_financials': 'Retains period evidence, income operating context and company-window assessment/coverage; entitlement and statement filters remain active.',
    'screen_company_financials': 'Receives the richer normalized financial evidence through its existing financial endpoint; candidate and unknown rules unchanged.',
    'company_brief': 'Financial summary includes the same source assessment context; section detail remains a separate request.',
    'compare_companies': 'Financial summaries inherit source assessment context; per-company scope and partial failure handling unchanged.',
    'get_investor_page': 'Observed empty fields remain discoverable; missing/null fields remain unknown.',
    'get_investor_field': 'Observed empty arrays return available with zero source count; missing composite fields no longer claim availability.',
    'get_internship': 'Adds source first-seen epoch and direct-apply flag only to detail.',
    'get_app_field': 'Adds listing install bands, score/price display text and release changes from allowlisted stored fields.',
}


def shape(value, path='data'):
    paths = set()
    if isinstance(value, dict):
        for key, child in value.items():
            at = path + '/' + key
            paths.add(at)
            paths.update(shape(child, at))
    elif isinstance(value, list):
        for child in value:
            paths.update(shape(child, path + '/*'))
    return paths


def build():
    before = json.loads((ROOT / 'qa/private/output-depth-baseline.json').read_text())['operations']
    after = json.loads((ROOT / 'qa/private/output-depth-after.json').read_text())['operations']
    examples = {row['operation']: row for row in json.loads((ROOT / 'docs/examples/index.json').read_text())}
    ownership = {name: (title, module, boundary, source) for title, module, boundary, source, names in GROUPS for name in names}
    assert set(ownership) == set(BY_NAME) == set(before) == set(after), 'Every data operation needs review and two live probes'
    rows = []
    for name, feature in BY_NAME.items():
        title, module, boundary, source = ownership[name]
        old, new = before[name], after[name]
        delta = None
        if old['http_status'] == new['http_status'] == 200 and old['request'] == new['request']:
            old_paths, new_paths = shape(old['response']['data']), shape(new['response']['data'])
            delta = {'added_paths': sorted(new_paths-old_paths), 'removed_paths': sorted(old_paths-new_paths)}
        row = {'operation': name, 'path': '/v1/'+feature.path, 'family': title, 'adapter': module,
               'source_review': source, 'ownership_boundary': boundary,
               'disposition': CHANGES.get(name, 'Retains the existing full source contract within its documented request bounds.'),
               'before': {'http_status': old['http_status'], 'captured_at': old['captured_at'], 'response_sha256': digest(old['response'])},
               'live_probe': {k: new[k] for k in ('http_status', 'captured_at', 'request', 'provenance')},
               'shape_delta': delta, 'documentation_example': '../examples/'+name+'.json',
               'documentation_capture_date': examples[name]['captured_at'], 'documentation_http_status': examples[name]['http_status']}
        row['live_probe']['response_sha256'] = digest(new['response'])
        row['live_probe']['capture_kind'] = new.get('capture_kind', 'live_gateway')
        row['live_probe']['error'] = new['response'].get('error')
        if feature.source != 'radar':
            row['disposition'] = 'Preserves strict News coverage_unavailable as a safe HTTP 503; source business payloads unchanged.'
        rows.append(row)
    controls = [{k: item[k] for k in ('operation', 'path', 'http_status', 'capture_kind', 'captured_at')}
                for name, item in examples.items() if name not in BY_NAME]
    files = sorted({r['adapter'] for r in rows} | {'radar_api/public.py', 'radar_api/social.py', 'radar_api/company_signals.py'})
    report = {'data_operations': len(rows), 'account_and_discovery_operations': len(controls),
              'live_status_counts': {str(code): sum(r['live_probe']['http_status'] == code for r in rows)
                                     for code in sorted({r['live_probe']['http_status'] for r in rows})},
              'source_files': [{'path': path, 'sha256': hashlib.sha256((ROOT/path).read_bytes()).hexdigest()} for path in files],
              'interpretation': 'Shape comparisons cover the same executed request, not all records. Additive data is tested separately from variable source availability. Historical successful News examples remain dated; the current probe is authoritative for current availability.',
              'operations': rows, 'controls': controls}
    (ROOT/'docs/research/endpoint-output-audit.json').write_text(encoded(report))
    lines = [f"| [{r['operation']}](reference/{r['operation']}.md) | {r['family']} | {r['live_probe']['http_status']} | {r['live_probe']['error']['kind'] if r['live_probe']['error'] else 'Response captured'} |" for r in rows]
    text = '''# Radar API output audit: company, financial, investor, app, jobs and news data

The audit covers every data operation and every account/discovery JSON operation.
It compares gateway output with the source adapter, reviews endpoint ownership,
and records a new live probe rather than treating an old HTTP 200 as current proof.
The [machine-readable evidence](research/endpoint-output-audit.json) contains all
requests, statuses, timestamps, response fingerprints, before/after shape changes
and reviewed adapter hashes. Private raw source responses remain outside the repo.

## What became richer

| Data requested | New retained information | Separate owner |
|---|---|---|
| Company traffic | Ranks, device visits/shares, engagement, backlinks, referring domains, traffic connections, countries and keywords | `get_company_field`, `field=traffic` |
| Customer reputation | Stored review profile and distinct review samples, with separate observation dates and source totals | `get_company_field`, `field=reputation` |
| Company classification | Structured sector context alongside existing sector names | `get_company_field`, `field=classification` |
| Lifecycle | Source xcorn rationale, parent/listing/acquisition context and achievements | `get_company_field`, `field=lifecycle` |
| Assessments | Uniqueness/scalability label, tagline and rationale alongside scores | `get_company_field`, `field=assessments` |
| Financial statements | Per-period evidence/quality, headcount, recorded growth and guidance; source summary comparisons and coverage | `get_financials` |
| App details | Install display/bands, score/price text, release changes and Android version display | Selected `get_app_field` |
| Internship detail | First-seen epoch and direct-apply indicator, separate from posted/expiry dates | `get_internship` |
| Investor fields | Observed empty arrays remain available and discoverable, distinct from missing/null | `get_investor_page` / `get_investor_field` |
| News failures | Explicit strict-coverage error instead of generic upstream failure | Existing News operations |

See [complete company examples](COMPANY_DATA_DEPTH.md), [financial evidence](guides/financial-data-api.md),
[all seven app fields](APP_DATA_DEPTH.md), and [investor fields](INVESTOR_DATA_DEPTH.md).
The refreshed company samples include three traffic snapshots and 60 distinct
stored customer-review sample rows across Razorpay, Stripe and Swiggy. Sample
counts do not represent the source review populations.

## How endpoint boundaries are preserved

Compact company and app profiles still return identity and field discovery. New
traffic/review values require a selected field request. Existing keys, value types
and arrays remain; native detail is not copied into search cards or the legacy
enrichment bundle. Briefs/comparisons retain compact sections and follow-up requests.
Financial screens reuse entitled normalized financial evidence and their existing
bounded candidate rules. Financial context never reads a deeper native archive.

The [selected-field conservation check](research/selected-field-conservation.json)
compares all 54 company fields and seven app fields with the previous commit.
Every existing business value survives unchanged in 56 of 61 captures. Three
hiring snapshots changed at source; Razorpay and Stripe innovation sections are
currently absent from derived enrichment. All five differences were independently
matched to the current native source projection. The API does not fill these
gaps with stale values from earlier examples. Primary before/after shape checks
removed only error branches for recovered component requests, not business fields.

Company founders and professional affiliation belong to team/people reads;
emails/phones belong to explicit, scoped, paid-plan contact reads. App developer
contacts and review author identities are not selected. Investor publication and
snapshot integrity checks remain in force. Authentication, usage charging, request
limits, response caps and read-only MCP behavior are unchanged.

Traffic source connections can repeat labels, and direction/denominators were not
retained. They cannot be summed into a complete acquisition mix. Review samples are
not a representative survey. Source corporate milestones and assessment rationale
are claims, not independently verified company facts. An unknown value stays null;
observed zeros/negative financial values survive. Partial store failures retain
available data while marking the missing part unavailable.

## Current live limitations

The two contact probes correctly returned `403 scope_required`; no paid contact
values were retrieved. Location intelligence still returned an upstream error.
The general News corpus could not establish strict coverage because a database
shard was unreachable. The gateway now preserves `503 coverage_unavailable` and
does not report incomplete corpus totals as success. Business-event and funding
queries have separate coverage and succeeded. These isolated News integration
calls verify actual data queries, not deployed production-key authentication.

Historical successful News examples remain visibly dated. Use the current probe
below for current availability. Live probes are bounded examples, not a guarantee
of every filter combination or full database parity. Employee-review analytics
keyed only by unverified company slugs were not joined by guessed names; those
need an authoritative domain mapping before they can safely extend reputation.

## Every data endpoint

| Operation | Owner/family | Latest probe HTTP | Outcome |
|---|---|---:|---|
''' + '\n'.join(lines) + '\n\n## Account and discovery operations\n\n'
    text += f"All {len(controls)} JSON control operations were recaptured using the isolated account fixture. "
    text += 'Key creation/revocation, plans, usage, spending, following and checkout keep their existing minimal control contracts. No real payment, customer account or live key was created.\n\n'
    text += 'The audit is reproducible from the ignored baseline/after captures with `scripts/audit_endpoint_outputs.py`. The public docs validator checks registry coverage, typed requests and adapter fingerprints. Regression tests cover field isolation, source counts, empty-vs-missing, gated periods, zero/negative values and coverage failures.\n'
    (ROOT/'docs/OUTPUT_DEPTH_AUDIT.md').write_text(text)
    print(f"Audited {len(rows)} data and {len(controls)} control operations: {report['live_status_counts']}")


if __name__ == '__main__':
    build()
