"""Bounded company LinkedIn observations, independent of derived enrichment coverage."""
from __future__ import annotations

import asyncio
import json

import httpx

from .errors import RadarError
from .profiles import bounded, public_value

PROFILES = """
SELECT name, li_slug AS linkedin_slug, sector AS recorded_sector, hq_country,
       if(followers < 0, NULL, followers) AS followers,
       if(employees < 0, NULL, employees) AS employee_count, company_size,
       if(total_reactions < 0, NULL, total_reactions) AS observed_reactions,
       if(total_comments < 0, NULL, total_comments) AS observed_comments,
       if(n_posts < 0, NULL, n_posts) AS observed_post_count,
       formatDateTime(fetched_at, '%Y-%m-%dT%H:%i:%SZ', 'UTC') AS observed_at,
       count() OVER () AS available_rows
FROM companies_data.linkedin_profile_logs FINAL
WHERE company_domain = {domain:String}
ORDER BY fetched_at DESC
LIMIT {limit:UInt32}
"""

# FINAL removes identical observations but retains different fetch dates. Group
# by post ID too, so repeated crawls cannot duplicate a post or sum its counters.
POSTS = """
SELECT official_post_id AS post_id, latest.1 AS page_url, latest.2 AS post_url,
       latest.3 AS title, latest.4 AS text, latest.5 AS media_urls,
       latest.6 AS hashtags, if(latest.7 < 0, NULL, latest.7) AS likes,
       if(latest.8 < 0, NULL, latest.8) AS comments,
       if(latest.9 < 0, NULL, latest.9) AS reposts, latest.10 AS author,
       formatDateTime(latest.11, '%Y-%m-%dT%H:%i:%SZ', 'UTC') AS posted_at,
       formatDateTime(observed_at, '%Y-%m-%dT%H:%i:%SZ', 'UTC') AS observed_at,
       count() OVER () AS available_rows
FROM (
    SELECT official_post_id,
           argMax(tuple(page_url, post_url, title, text, media_urls, hash_tags,
                        likes, comments, reposts, author, posted_at), fetched_at) AS latest,
           max(fetched_at) AS observed_at
    FROM companies_data.social_media_posts FINAL
    WHERE platform_name = 'linkedin' AND company_domain = {domain:String}
    GROUP BY official_post_id
)
ORDER BY latest.11 DESC NULLS LAST, official_post_id ASC
LIMIT {limit:UInt32}
"""


class SocialStore:
    def __init__(self, settings, transport=None):
        self.settings, self.transport = settings, transport

    async def available(self, domain):
        rows = await self.query("""SELECT
            (SELECT count() FROM companies_data.linkedin_profile_logs WHERE company_domain={domain:String}) > 0
            OR (SELECT count() FROM companies_data.social_media_posts
                WHERE platform_name='linkedin' AND company_domain={domain:String}) > 0 AS available""", domain, 1)
        return bool(rows and rows[0]['available'])

    async def query(self, sql, domain, limit):
        settings = self.settings
        params = {'query': sql + ' FORMAT JSON', 'param_domain': domain, 'param_limit': str(limit),
                  'readonly': '1', 'max_execution_time': '8', 'max_memory_usage': str(128 * 1024 * 1024),
                  'max_rows_to_read': '1000000', 'max_result_rows': '100',
                  'result_overflow_mode': 'throw', 'output_format_json_quote_64bit_integers': '0'}
        try:
            async with httpx.AsyncClient(timeout=min(settings.timeout_seconds, 12), follow_redirects=False,
                                         trust_env=False, transport=self.transport,
                                         auth=(settings.social_ch_user, settings.social_ch_password)) as client:
                async with client.stream('POST', settings.social_ch_url, params=params) as response:
                    if response.status_code != 200:
                        raise RadarError('social_store_unavailable', 'Company social storage could not complete the query', 502)
                    chunks, size = [], 0
                    async for chunk in response.aiter_bytes():
                        size += len(chunk)
                        if size > settings.max_response_bytes:
                            raise RadarError('response_too_large', 'Lower item_limit for company social data', 502)
                        chunks.append(chunk)
                    result = json.loads(b''.join(chunks))
            if not isinstance(result.get('data'), list) or result.get('exception'):
                raise ValueError('Invalid query result')
            return result['data']
        except httpx.TimeoutException:
            raise RadarError('social_store_timeout', 'Company social lookup timed out', 504) from None
        except (httpx.HTTPError, ValueError, TypeError, AttributeError):
            raise RadarError('social_store_unavailable', 'Company social storage returned an unreadable response', 502) from None

    async def get(self, request):
        results = await asyncio.gather(self.query(PROFILES, request.domain, request.item_limit),
                                       self.query(POSTS, request.domain, request.item_limit), return_exceptions=True)
        out, arrays, sources = {}, {}, {}
        for name, rows in zip(('profile_history', 'recent_posts'), results):
            if isinstance(rows, RadarError):
                out[name] = None
                sources[name] = {'status': 'unavailable', 'error_kind': rows.kind}
                continue
            if isinstance(rows, BaseException):
                raise rows
            total = int(rows[0]['available_rows']) if rows else 0
            values = [public_value({k: v for k, v in row.items() if k != 'available_rows'}) for row in rows]
            path = '/value/linkedin/' + name
            out[name] = bounded(values, request.item_limit, path, arrays)
            arrays[path] = {'available': total, 'returned': len(values), 'truncated': total > len(values)}
            sources[name] = {'status': 'available' if rows else 'not_observed'}
        out['profile'] = (out['profile_history'] or [None])[0]
        out['coverage'] = sources
        out['notes'] = [
            'Stored LinkedIn observations; employee_count is observed platform headcount, not audited payroll.',
            'Recent means newest stored posts, not a live feed. Observation time differs from publication time.',
            'Post counters are latest stored values, not sums across crawls. Source zeros can include parser defaults.',
            'Negative source counters become null. Profile reaction/comment totals cover the observed page cards, not lifetime engagement.',
            'Recorded sector is a source label and can disagree with the company classification.',
        ]
        partial = any(s['status'] == 'unavailable' for s in sources.values()) or any(v['truncated'] for v in arrays.values())
        return out, arrays, partial


async def add_social(data, request, store):
    """Augment only the explicitly selected social field; failures stay visible."""
    if store is None:
        linkedin = {'profile': None, 'profile_history': None, 'recent_posts': None,
                    'coverage': {'status': 'not_configured'}}
        arrays, partial = {}, True
    else:
        linkedin, arrays, partial = await store.get(request)
    observed = bool(linkedin.get('profile_history') or linkedin.get('recent_posts'))
    present = data['status'] in {'available', 'partial'} or observed
    partial = partial or data['coverage']['partial']
    status = 'partial' if partial and present else 'unavailable' if partial else 'available' if present else 'not_observed'
    data['value'] = {**(data['value'] or {}), 'linkedin': linkedin}
    data['status'] = status
    data['coverage']['sections']['social'] = {'available': present, 'status': status}
    data['coverage']['arrays'].update(arrays)
    data['coverage']['partial'] = partial
    return data


async def add_social_availability(data, domain, store):
    """Compact discovery reads only existence, never counts, posts or rich metrics."""
    if store is None:
        return data
    try:
        if await store.available(domain):
            data['field_status']['social'] = 'partial' if data['coverage']['partial'] else 'available'
            if 'social' not in data['available_fields']:
                data['available_fields'].append('social')
    except RadarError:
        present = 'social' in data['available_fields']
        data['field_status']['social'] = 'partial' if present else 'unavailable'
        data['coverage']['partial'] = True
    return data
