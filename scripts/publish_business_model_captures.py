#!/usr/bin/env python3
"""Copy reviewed captures into local documentation; does not push or query data."""
import json
import re

from business_model_evidence import CAPTURES, ROOT, digest
from business_model_cases import CASES
from radar_api.models import Envelope
from radar_api.service import BY_NAME


def main():
    raw = json.loads((ROOT / 'qa/private/business-model-live.json').read_text())
    expected = {case['id']: case for case in CASES}
    assert {row['id'] for row in raw} == expected.keys()
    CAPTURES.mkdir(parents=True, exist_ok=True)
    total = 0
    for row in raw:
        for i, record in enumerate(row['captures']):
            if i == 0:
                assert record['request'] == expected[row['id']]['request']
                assert record['operation'] == expected[row['id']]['operation']
            BY_NAME[record['operation']].model.model_validate(record['request'])
            Envelope.model_validate(record['response'])
            suffix = {0: 'search', 1: 'profile', 2: 'classification'}[i]
            text = json.dumps(record)
            assert not re.search(r'"(?:api_key|auth_sign|radar_token|password|authorization)"\s*:', text, re.I)
            assert not re.search(r'(?:rdr_[a-f0-9]{64}|ghp_[A-Za-z0-9]{30,}|github_pat_)', text)
            fingerprint = digest(record['response'])
            out = {**record, 'provenance': record['transport'], 'omitted_paths': [],
                   'credential_redactions': [], 'hash_basis': 'Parsed JSON with sorted keys',
                   'original_response_sha256': fingerprint, 'response_excerpt_sha256': fingerprint}
            (CAPTURES / f'{row["id"]}-{suffix}.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
            total += 1
    print('Copied', total, 'complete actual response captures to documentation')


if __name__ == '__main__':
    main()
