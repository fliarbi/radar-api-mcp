"""Typed, bounded, read-only queries over Radar's Play Store app records."""
from __future__ import annotations

import json
import httpx
from .errors import RadarError

APP_FIELDS = ('listing', 'ratings', 'monetization', 'release', 'developer', 'growth', 'install_history')
CARD = '''appId AS app_id, title AS name, developer, developerWebsite AS developer_website,
          genre AS category, realInstalls AS installs, score AS rating, ratings AS rating_count,
          formatDateTime(last_crawled_at, '%Y-%m-%dT%H:%i:%SZ', 'UTC') AS observed_at'''
DOMAIN = "replaceRegexpOne(lower(domain(developerWebsite)), '^www\\\\.', '')"
SORTS = {'installs': 'realInstalls DESC', 'rating': 'score DESC', 'observed': 'last_crawled_at DESC', 'name': 'title ASC'}
SELECTION = {
    'listing': "title AS name, summary, JSONExtractString(raw_json,'description') AS description, genre AS category, JSONExtractRaw(raw_json,'categories') AS categories_json, contentRating AS content_rating, JSONExtractString(raw_json,'privacyPolicy') AS privacy_policy, JSONExtractRaw(raw_json,'screenshots') AS screenshots_json, JSONExtractRaw(raw_json,'available') AS available_json",
    'ratings': "score AS rating, ratings AS rating_count, reviews AS review_count, JSONExtractRaw(raw_json,'histogram') AS histogram_json",
    'monetization': "price, free, currency, offersIAP AS offers_in_app_purchases, adSupported AS ad_supported, containsAds AS contains_ads, JSONExtractRaw(raw_json,'isAvailableInPlayPass') AS play_pass_json",
    'release': "released, updated, version, androidVersion AS minimum_android_version, JSONExtractString(raw_json,'androidMaxVersion') AS maximum_android_version, JSONExtractRaw(raw_json,'preregister') AS preregister_json, JSONExtractRaw(raw_json,'earlyAccessEnabled') AS early_access_json",
    'developer': "developer AS name, developerId AS store_developer_id, developerWebsite AS website, developerLegalName AS legal_name",
}


def decode(row):
    out = {}
    for key, value in row.items():
        if key.endswith('_json'):
            try:
                value = json.loads(value) if value else None
            except (ValueError, TypeError):
                value = None
            key = key.removesuffix('_json')
        out[key] = value
    return out


def app_card(row):
    return {**row, 'store': 'google_play', 'url': 'https://play.google.com/store/apps/details?id='+row['app_id'],
            'detail_request': {'method': 'POST', 'path': '/v1/apps/profile', 'body': {'app_id': row['app_id']}}}


class AppsStore:
    def __init__(self, settings, transport=None):
        self.settings, self.transport = settings, transport

    async def query(self, sql, params=None):
        settings = self.settings
        query = {'query': sql + ' FORMAT JSON', 'readonly': '1', 'max_execution_time': '8',
                 'output_format_json_quote_64bit_integers': '0', 'max_memory_usage': str(256*1024*1024), 'max_rows_to_read': '10000000',
                 'result_overflow_mode': 'throw', 'max_result_rows': '102',
                 **{'param_'+k: str(v) for k, v in (params or {}).items()}}
        try:
            async with httpx.AsyncClient(timeout=min(settings.timeout_seconds, 12), follow_redirects=False,
                                         trust_env=False, transport=self.transport,
                                         auth=(settings.apps_ch_user, settings.apps_ch_password)) as client:
                async with client.stream('POST', settings.apps_ch_url, params=query) as response:
                    if response.status_code != 200:
                        raise RadarError('upstream_unavailable', 'App storage could not complete this query', 502)
                    chunks, size = [], 0
                    async for chunk in response.aiter_bytes():
                        size += len(chunk)
                        if size > settings.max_response_bytes:
                            raise RadarError('response_too_large', 'Narrow the app query or lower its limit', 502)
                        chunks.append(chunk)
                    body = json.loads(b''.join(chunks))
            if not isinstance(body.get('data'), list) or body.get('exception'):
                raise ValueError('Invalid query result')
            return body['data']
        except httpx.TimeoutException:
            raise RadarError('upstream_timeout', 'App lookup timed out; narrow the query', 504) from None
        except (httpx.HTTPError, ValueError, TypeError, AttributeError):
            raise RadarError('upstream_unavailable', 'App storage returned an unreadable response', 502) from None

    async def get(self, name, r):
        if name == 'app_filter_options':
            rows = await self.query("SELECT DISTINCT genre AS category FROM play_store.apps_full WHERE genre IS NOT NULL AND positionCaseInsensitive(genre,{q:String}) > 0 ORDER BY genre LIMIT {limit:UInt32}", {'q': r.q or '', 'limit': r.limit})
            return {'field': 'category', 'options': [x['category'] for x in rows], 'complete': len(rows) < r.limit}
        if name in {'search_apps', 'company_apps'}:
            clauses, params = [], {'limit': r.limit+1, 'offset': r.page*r.limit}
            for field, expression in [('q', 'title'), ('developer', 'developer')]:
                if getattr(r, field, None):
                    clauses.append(f'positionCaseInsensitive({expression},{{{field}:String}}) > 0')
                    params[field] = getattr(r, field)
            if getattr(r, 'domain', None):
                clauses.append(DOMAIN+' = {domain:String}')
                params['domain'] = r.domain
            if getattr(r, 'category', None):
                clauses.append('genre = {category:String}')
                params['category'] = r.category
            for field, expression, typ in [('min_installs', 'realInstalls', 'UInt64'), ('min_score', 'score', 'Float64')]:
                if getattr(r, field, None) is not None:
                    clauses.append(f'{expression} >= {{{field}:{typ}}}')
                    params[field] = getattr(r, field)
            if getattr(r, 'free', None) is not None:
                clauses.append('free = {free:UInt8}')
                params['free'] = int(r.free)
            order = SORTS[getattr(r, 'sort_by', 'installs')]
            rows = await self.query('SELECT '+CARD+' FROM play_store.apps_full FINAL WHERE '+' AND '.join(clauses)+
                                    ' ORDER BY '+order+', appId LIMIT {limit:UInt32} OFFSET {offset:UInt32}', params)
            return {'apps': [app_card(row) for row in rows[:r.limit]], 'page': r.page, 'limit': r.limit,
                    'has_more': len(rows) > r.limit, 'total': None,
                    'match_method': 'Exact normalized developer website host; no fuzzy name, URL substring or ownership inference' if getattr(r, 'domain', None) else 'Explicit app filters',
                    'coverage': {'store': 'google_play', 'live_store_verified': False},
                    'note': 'Observed Play Store data only. Installs are cumulative source estimates; row observation dates are not current download dates.'}
        rows = await self.query('SELECT '+CARD+''', summary,
            (SELECT count() FROM play_store.installs_history WHERE appId={id:String}) AS history_points,
            (SELECT count() FROM play_store.app_yoy WHERE appId={id:String}) AS growth_points,
            (SELECT count() FROM play_store.app_velocity WHERE appId={id:String}) AS velocity_points
            FROM play_store.apps_full FINAL WHERE appId={id:String} LIMIT 1''', {'id': r.app_id})
        if not rows:
            raise RadarError('no_data', 'No app record was found for this store ID', 404)
        app = rows[0]
        common = {'app_id': r.app_id, 'store': 'google_play', 'observed_at': app['observed_at'],
                  'coverage': {'live_store_verified': False, 'source': 'radar_app_records'}}
        if name == 'get_app':
            fields = list(SELECTION)
            if app['growth_points'] or app['velocity_points']:
                fields.append('growth')
            if app['history_points']:
                fields.append('install_history')
            return {**common, 'app': app_card({k: v for k, v in app.items() if not k.endswith('_points')}),
                    'available_fields': fields, 'history_points': app['history_points'],
                    'history_points_note': 'Stored observation rows, including any source duplicates; not distinct days.',
                    'field_request': {'method': 'POST', 'path': '/v1/apps/field', 'required': ['app_id', 'field']}}
        if r.field == 'install_history':
            rows = await self.query('''SELECT formatDateTime(crawled_at, '%Y-%m-%dT%H:%i:%SZ', 'UTC') AS observed_at, realInstalls AS installs, minInstalls AS minimum_installs
                FROM play_store.installs_history WHERE appId={id:String} ORDER BY crawled_at DESC, realInstalls DESC, minInstalls DESC
                LIMIT {limit:UInt32} OFFSET {offset:UInt32}''', {'id': r.app_id, 'limit': r.limit+1, 'offset': r.offset})
            return {**common, 'field': r.field, 'value': rows[:r.limit], 'status': 'available' if app['history_points'] else 'not_observed',
                    'pagination': {'source_total': app['history_points'], 'offset': r.offset, 'limit': r.limit,
                                   'deduplicated': False, 'note': 'Exact duplicate source observations are preserved; source_total counts stored rows.',
                                   'next_offset': r.offset+r.limit if len(rows) > r.limit else None}}
        if r.offset:
            raise RadarError('invalid_request', 'Offset applies only to install_history', 422)
        if r.field == 'growth':
            yoy = await self.query('''SELECT formatDateTime(cur_t, '%Y-%m-%dT%H:%i:%SZ', 'UTC') AS current_observed_at, cur AS current_installs, prev AS previous_installs,
                formatDateTime(prev_t, '%Y-%m-%dT%H:%i:%SZ', 'UTC') AS previous_observed_at, gap_days, raw_pct AS observed_change_pct, yoy_pct AS annualized_change_pct, reliable
                FROM play_store.app_yoy WHERE appId={id:String} ORDER BY cur_t DESC LIMIT 1''', {'id': r.app_id})
            velocity = await self.query('''SELECT age_years, avg_installs_per_year, bogus_released AS release_date_suspect,
                young_fast_riser FROM play_store.app_velocity WHERE appId={id:String} LIMIT 1''', {'id': r.app_id})
            value = {'install_change': yoy[0] if yoy else None, 'velocity': velocity[0] if velocity else None,
                     'note': 'Annualized growth is derived from the measured gap, not necessarily a full-year observation. Retain reliable and suspect-date flags; this is not a forecast.'}
        else:
            rows = await self.query('SELECT '+SELECTION[r.field]+' FROM play_store.apps_full FINAL WHERE appId={id:String} LIMIT 1', {'id': r.app_id})
            value = decode(rows[0])
        return {**common, 'field': r.field, 'value': value,
                'status': 'not_observed' if r.field == 'growth' and not (app['growth_points'] or app['velocity_points']) else 'available'}
