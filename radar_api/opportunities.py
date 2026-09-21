"""Explainable Radar discovery presets, never invented opportunity probabilities."""
from copy import deepcopy

PRESETS = {
    'high_growth': {'title': 'Companies with recorded scaling signals',
                    'filters': {'growth_stages': ['Scaling Super Fast', 'Aggressively Scaling']}, 'sort_by': 'momentum',
                    'evidence_columns': ['employees', 'total_funding', 'latest_revenue'],
                    'interpretation': 'Derived scaling labels; verify financial and hiring evidence separately.'},
    'profitable_growth': {'title': 'Companies with recorded profits and revenue growth',
                         'filters': {'profitability': ['profitable'], 'revenue_growth': ['growing']}, 'sort_by': 'finance',
                         'evidence_columns': ['latest_revenue', 'growth_stage', 'total_funding'],
                         'interpretation': 'Recorded financial bands can be stale or source-plan restricted; use financial statements for exact periods.'},
    'early_stage': {'title': 'Young companies with seed-stage records', 'filters': {'ages': ['< 5y'], 'stages': ['Seed']},
                    'sort_by': 'funding', 'evidence_columns': ['total_funding', 'employees'],
                    'interpretation': 'Historical age and funding classification; no claim of a current fundraising mandate.'},
    'hiring_expansion': {'title': 'Companies with recorded hiring demand', 'filters': {'hiring': {'is_hiring': True, 'min_open_roles': 1, 'recency_days': 90}},
                        'sort_by': 'employees', 'evidence_columns': ['employees', 'latest_revenue'],
                        'interpretation': 'Hiring is an observed demand signal, not verified intent to buy a service.'},
    'technology_modernization': {'title': 'Scaling companies using selected web technologies',
                                'filters': {'technologies': ['PHP', 'MySQL'], 'growth_stages': ['Aggressively Scaling']},
                                'sort_by': 'employees', 'evidence_columns': ['web_presence', 'employees'],
                                'interpretation': 'A technology-and-growth screen. PHP or MySQL use does not prove poor technology or a modernization budget.'},
    'mobile_scale': {'title': 'Companies with a substantial mobile-app footprint', 'filters': {'mobile_downloads': ['1m+']},
                     'sort_by': 'employees', 'evidence_columns': ['mobile_downloads', 'mobile_growth', 'employees'],
                     'interpretation': 'Historical cumulative install bands; inspect individual apps and observation dates before estimating momentum.'},
}


def catalog():
    return {'presets': [{'id': name, **deepcopy(value)} for name, value in PRESETS.items()],
            'note': 'Presets reproduce explicit Radar filters, not predicted investment returns, purchase intent or eligibility. Source gates and widened matches remain visible.'}
