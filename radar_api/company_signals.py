"""Selected company traffic/reputation observations; never a bulk profile dump."""
from __future__ import annotations

import asyncio
import json

import httpx

from .errors import RadarError
from .profiles import bounded, public_value

TRAFFIC = """SELECT authority_score, global_rank, country_rank, category_rank, country_rank_name,
    visits, visits_date, desktop_visits, mobile_visits, desktop_share, mobile_share,
    backlinks, referring_domains, bounce_rate, pages_per_visit, time_on_site,
    n_competitors, competitors, ts_source, ts_share, ts_visits,
    cc, country_name, country_traffic, country_share, kw, kw_position, kw_volume, kw_cpc,
    formatDateTime(fetched_at, '%Y-%m-%dT%H:%i:%SZ', 'UTC') AS observed_at
    FROM companies_data.semrush_website FINAL WHERE domain={domain:String}
    ORDER BY fetched_at DESC LIMIT 1"""
REVIEWS = """SELECT display_name, trust_score, stars, review_count, reviews_12mo,
    is_claimed, is_closed, is_collecting, primary_category, categories, website,
    city, country, locations_count,
    formatDateTime(fetched_at, '%Y-%m-%dT%H:%i:%SZ', 'UTC') AS observed_at
    FROM companies_data.trustpilot_reviews FINAL WHERE domain={domain:String} AND found=1
    ORDER BY fetched_at DESC LIMIT 1"""
SAMPLES = """SELECT review_id, latest.1 AS rating, latest.2 AS headline, latest.3 AS body,
    latest.4 AS likes, latest.5 AS published, latest.6 AS experienced,
    latest.7 AS country, latest.8 AS language, latest.9 AS replied,
    formatDateTime(observed_at, '%Y-%m-%dT%H:%i:%SZ', 'UTC') AS observed_at,
    count() OVER () AS available_rows
    FROM (SELECT review_id, argMax(tuple(rating,title,text,likes,published,experienced,country,language,replied), fetched_at) AS latest,
          max(fetched_at) AS observed_at FROM companies_data.trustpilot_review_samples FINAL
          WHERE domain={domain:String} GROUP BY review_id)
    ORDER BY latest.5 DESC, review_id LIMIT {limit:UInt32}"""
DETAIL_KEYS = {'traffic': 'web_traffic', 'reputation': 'customer_reviews'}


def aligned(row, columns):
    """Keep source index alignment and duplicate labels; never silently zip-short."""
    values = {name: row.get(column) or [] for name, column in columns.items()}
    return [{name: array[i] if i < len(array) else None for name, array in values.items()}
            for i in range(max((len(a) for a in values.values()), default=0))]


def traffic_value(row):
    return {
        'observed_at': row.get('observed_at'), 'measurement_date': row.get('visits_date'),
        'visits': row.get('visits'), 'authority_score': row.get('authority_score'),
        'ranks': {key: row.get(key) for key in ('global_rank', 'country_rank', 'country_rank_name', 'category_rank')},
        'devices': {'desktop': {'visits': row.get('desktop_visits'), 'share': row.get('desktop_share')},
                    'mobile': {'visits': row.get('mobile_visits'), 'share': row.get('mobile_share')}},
        'engagement': {'bounce_rate': row.get('bounce_rate'), 'pages_per_visit': row.get('pages_per_visit'),
                       'time_on_site_seconds': row.get('time_on_site')},
        'backlinks': row.get('backlinks'), 'referring_domains': row.get('referring_domains'),
        'traffic_connections': aligned(row, {'label': 'ts_source', 'share': 'ts_share', 'visits': 'ts_visits'}),
        'countries': aligned(row, {'code': 'cc', 'name': 'country_name', 'visits': 'country_traffic', 'share': 'country_share'}),
        'keywords': aligned(row, {'keyword': 'kw', 'position': 'kw_position', 'volume': 'kw_volume', 'cpc': 'kw_cpc'}),
        'comparison_domains': row.get('competitors'), 'comparison_domain_count': row.get('n_competitors'),
        'notes': ['Stored estimated website traffic; visits are not unique visitors, customers or revenue.',
                  'Shares and bounce rate are source fractions, not percentages. Measurement and observation dates differ.',
                  'Traffic connections retain source order and duplicates; direction and denominator were not retained, so do not sum or treat them all as acquisition channels.',
                  'Keyword CPC currency is not supplied. Comparison domains are source suggestions, not verified business competitors.'],
    }


class CompanySignalsStore:
    def __init__(self, settings, transport=None):
        self.settings, self.transport = settings, transport

    async def query(self, sql, domain, limit=1):
        settings = self.settings
        params = {'query': sql + ' FORMAT JSON', 'param_domain': domain, 'param_limit': str(limit),
                  'readonly': '1', 'max_execution_time': '8', 'max_memory_usage': str(128 * 1024 * 1024),
                  'max_rows_to_read': '1000000', 'max_result_rows': '100',
                  'result_overflow_mode': 'throw', 'output_format_json_quote_64bit_integers': '0'}
        try:
            async with httpx.AsyncClient(timeout=min(settings.timeout_seconds, 12), follow_redirects=False,
                                         trust_env=False, transport=self.transport,
                                         auth=(settings.company_ch_user, settings.company_ch_password)) as client:
                async with client.stream('POST', settings.company_ch_url, params=params) as response:
                    if response.status_code != 200:
                        raise RadarError('company_signals_unavailable', 'Company observations could not complete this query', 502)
                    chunks, size = [], 0
                    async for chunk in response.aiter_bytes():
                        size += len(chunk)
                        if size > settings.max_response_bytes:
                            raise RadarError('response_too_large', 'Lower item_limit for company observations', 502)
                        chunks.append(chunk)
                    result = json.loads(b''.join(chunks))
            if not isinstance(result.get('data'), list) or result.get('exception'):
                raise ValueError('Invalid result')
            return result['data']
        except httpx.TimeoutException:
            raise RadarError('company_signals_timeout', 'Company observation lookup timed out', 504) from None
        except (httpx.HTTPError, ValueError, TypeError, AttributeError):
            raise RadarError('company_signals_unavailable', 'Company observations returned an unreadable response', 502) from None

    async def available(self, domain):
        rows = await self.query("""SELECT
            (SELECT count() FROM companies_data.semrush_website WHERE domain={domain:String}) > 0 AS traffic,
            ((SELECT count() FROM companies_data.trustpilot_reviews WHERE domain={domain:String} AND found=1) > 0
             OR (SELECT count() FROM companies_data.trustpilot_review_samples WHERE domain={domain:String}) > 0) AS reputation""", domain)
        return rows[0] if rows else {}

    async def get(self, request):
        queries = [('snapshot', TRAFFIC)] if request.field == 'traffic' else [('profile', REVIEWS), ('review_samples', SAMPLES)]
        results = await asyncio.gather(*(self.query(sql, request.domain, request.item_limit) for _, sql in queries), return_exceptions=True)
        values, sources, arrays = {}, {}, {}
        for (name, _), rows in zip(queries, results):
            if isinstance(rows, RadarError):
                values[name], sources[name] = None, {'status': 'unavailable', 'error_kind': rows.kind}
                continue
            if isinstance(rows, BaseException):
                raise rows
            sources[name] = {'status': 'available' if rows else 'not_observed'}
            if name == 'review_samples':
                total = int(rows[0]['available_rows']) if rows else 0
                values[name] = [{k: v for k, v in row.items() if k != 'available_rows'} for row in rows]
                path = '/value/customer_reviews/review_samples'
                arrays[path] = {'available': total, 'returned': len(rows), 'truncated': total > len(rows)}
            else:
                values[name] = (traffic_value(rows[0]) if name == 'snapshot' else rows[0]) if rows else None
        values['coverage'] = sources
        if request.field == 'reputation':
            values['platform'] = 'trustpilot'
            values['notes'] = ['Stored customer-review observations; this is not employee reputation or a representative survey.',
                               'Review samples are a stored subset; review_count belongs to the source profile, not the returned sample.',
                               'Profile and samples have independent observation dates. Repeated crawls are deduplicated by review_id; author contact/identity fields are excluded.']
        path = '/value/' + DETAIL_KEYS[request.field]
        nested_arrays = {}
        values = bounded(public_value(values), request.item_limit, path, nested_arrays)
        # SQL source totals must survive generic in-memory array accounting.
        arrays = {**nested_arrays, **arrays}
        return values, arrays, any(s['status'] == 'unavailable' for s in sources.values()) or any(a['truncated'] for a in arrays.values())


async def add_signals(data, request, store):
    detail = DETAIL_KEYS[request.field]
    if store:
        value, arrays, partial = await store.get(request)
    else:
        value, arrays, partial = {'coverage': {'status': 'not_configured'}}, {}, True
    observed = any(isinstance(s, dict) and s.get('status') == 'available' for s in value['coverage'].values())
    present = data['status'] in {'available', 'partial'} or observed
    partial = partial or data['coverage']['partial']
    status = 'partial' if partial and present else 'unavailable' if partial else 'available' if present else 'not_observed'
    data['value'] = {**(data['value'] or {}), detail: value}
    data['status'] = status
    data['coverage']['sections'][request.field] = {'available': present, 'status': status}
    data['coverage']['arrays'].update(arrays)
    data['coverage']['partial'] = partial
    return data


async def add_signals_availability(data, domain, store):
    if store is None:
        return data
    try:
        availability = await store.available(domain)
        for field in DETAIL_KEYS:
            if availability.get(field):
                data['field_status'][field] = 'partial' if data['coverage']['partial'] else 'available'
                if field not in data['available_fields']:
                    data['available_fields'].append(field)
    except RadarError:
        for field in DETAIL_KEYS:
            data['field_status'][field] = 'partial' if field in data['available_fields'] else 'unavailable'
        data['coverage']['partial'] = True
    return data
