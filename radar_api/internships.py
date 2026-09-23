"""Bounded read-only access to Radar's dedicated internship records."""
from __future__ import annotations

import asyncio
from datetime import date, datetime, timedelta, timezone
import re

from pymongo import MongoClient
from pymongo.errors import PyMongoError

from .errors import RadarError
from .public import clean

FIELDS = {k: 1 for k in ('_id', 'title', 'company', 'url', 'description', 'date_posted', 'valid_through',
          'employment_type', 'posting_type', 'locations', 'skills', 'industry', 'occupational_category',
          'months_experience', 'salary_currency', 'salary_min', 'salary_max', 'stipend_value', 'scraped_at', 'last_seen',
          'first_seen', 'direct_apply')}
NOTE = ('These are observed internship listings, not verified current vacancies. Posted and crawl dates are separate. '
        'Far-future source deadlines are not proof a listing remains open. Stipend periods are not supplied.')
REMOTE_PATTERN = r'work from home|remote|\bWFH\b'


def query_for(r):
    parts = [{'posting_type': 'internship'}]
    for key in ('title', 'company'):
        value = getattr(r, key)
        if value:
            parts.append({key: {'$regex': '^' + re.escape(value), '$options': 'i'}})
    if r.location:
        rx = {'$regex': '^' + re.escape(r.location), '$options': 'i'}
        parts.append({'$or': [{'locations.locality': rx}, {'locations.region': rx}, {'locations.country': rx}]})
    if r.skills:
        parts.append({'skills': {'$in': [re.compile('^' + re.escape(s) + '$', re.I) for s in r.skills]}})
    if r.part_time:
        parts.append({'employment_type': {'$regex': 'PART_TIME'}})
    if r.work_mode != 'any':
        remote = {'$or': [{key: {'$regex': REMOTE_PATTERN, '$options': 'i'}} for key in ('locations.locality', 'title')]}
        parts.append(remote if r.work_mode == 'remote' else {'$and': [{'locations.locality': {'$exists': True, '$nin': [None, '']}}, {'$nor': [remote]}]})
    if r.stipend_min:
        parts.append({'stipend_value': {'$gte': r.stipend_min}})
    if r.posted_since or r.posted_until:
        span = {}
        if r.posted_since:
            span['$gte'] = r.posted_since.isoformat()
        if r.posted_until:
            span['$lt'] = (r.posted_until + timedelta(days=1)).isoformat()
        parts.append({'date_posted': span})
    if r.validity == 'not_expired':
        today = datetime.now(timezone.utc).date()
        parts.append({'valid_through': {'$gte': today.isoformat(), '$lt': (today + timedelta(days=365)).isoformat()}})
    return {'$and': parts}


def card(doc, detail=False):
    expiry = str(doc.get('valid_through') or '')
    status = 'unknown'
    try:
        end = date.fromisoformat(expiry[:10])
        today = datetime.now(timezone.utc).date()
        status = 'expired' if end < today else 'future_deadline_unverified' if end > today + timedelta(days=365) else 'not_expired_by_source_date'
    except ValueError:
        pass
    remote = any(re.search(REMOTE_PATTERN, str(text or ''), re.I) for text in
                 [doc.get('title'), *[loc.get('locality') for loc in doc.get('locations') or []]])
    has_location = any(loc.get('locality') for loc in doc.get('locations') or [])
    row = {'id': str(doc['_id']), 'title': doc.get('title'), 'company': doc.get('company'),
           'company_domain': None, 'url': doc.get('url'), 'posted': doc.get('date_posted'),
           'valid_through': doc.get('valid_through'), 'validity_status': status, 'current_opening_verified': False,
           'employment_type': doc.get('employment_type'), 'locations': doc.get('locations'), 'skills': doc.get('skills'),
           'work_mode': 'remote_indicated' if remote else 'location_listed' if has_location else 'unknown',
           'industry': doc.get('industry'), 'experience_months': doc.get('months_experience'),
           'stipend': {'value': doc.get('stipend_value'), 'currency': doc.get('salary_currency'), 'period': None},
           'salary': {'min': doc.get('salary_min'), 'max': doc.get('salary_max'), 'currency': doc.get('salary_currency'), 'period': None},
           'scraped_at': doc.get('scraped_at'), 'last_seen': doc.get('last_seen'), 'source': 'internshala'}
    if detail:
        row.update(description=doc.get('description'), occupational_category=doc.get('occupational_category'),
                   direct_apply=doc.get('direct_apply'), first_seen_epoch_seconds=doc.get('first_seen'))
    else:
        row['detail_request'] = {'method': 'POST', 'path': '/v1/jobs/internships/detail', 'body': {'id': row['id']}}
    return clean(row)


class InternshipStore:
    def __init__(self, settings, client=None):
        self.client = client or MongoClient(settings.jobs_mongo_uri, serverSelectionTimeoutMS=3000, socketTimeoutMS=6000)
        self.collection = self.client['companies_data']['internshala_jobs']

    def close(self):
        self.client.close()

    async def get(self, name, request):
        try:
            return await asyncio.to_thread(self._get, name, request)
        except PyMongoError:
            raise RadarError('upstream_unavailable', 'Internship storage could not complete this query', 502) from None

    def _get(self, name, r):
        if name == 'get_internship':
            doc = self.collection.find_one({'_id': r.id, 'posting_type': 'internship'}, FIELDS, max_time_ms=5000)
            if not doc:
                raise RadarError('no_data', 'No internship was found for this ID', 404)
            return {'internship': card(doc, detail=True), 'note': NOTE}
        query = query_for(r)
        if name == 'search_internships':
            rows = list(self.collection.find(query, FIELDS).sort([('date_posted', -1), ('_id', 1)])
                        .skip(r.page * r.limit).limit(r.limit + 1).max_time_ms(5000))
            total = self.collection.count_documents(query, maxTimeMS=5000)
            return {'internships': [card(d) for d in rows[:r.limit]], 'total': total,
                    'page': r.page, 'limit': r.limit, 'has_more': len(rows) > r.limit, 'note': NOTE}
        pipeline = [{'$match': query}, {'$sort': {'date_posted': -1}},
                    {'$group': {'_id': '$company', 'observed_internships': {'$sum': 1}, 'latest_posted': {'$max': '$date_posted'},
                                'sample_titles': {'$firstN': {'input': '$title', 'n': 5}},
                                'sample_ids': {'$firstN': {'input': '$_id', 'n': 5}}}},
                    {'$sort': {'observed_internships': -1, '_id': 1}}, {'$skip': r.page * r.limit}, {'$limit': r.limit + 1}]
        rows = list(self.collection.aggregate(pipeline, maxTimeMS=5000, allowDiskUse=False))
        companies = [{'name': row['_id'], 'company_domain': None, 'observed_internships': row['observed_internships'],
                      'latest_posted': row['latest_posted'], 'sample_titles': row['sample_titles'],
                      'sample_internship_ids': row['sample_ids'], 'current_openings_verified': False} for row in rows[:r.limit]]
        return {'companies': companies, 'page': r.page, 'limit': r.limit, 'has_more': len(rows) > r.limit,
                'grouping': 'Exact source employer name, not a verified company identity or domain join', 'note': NOTE}
