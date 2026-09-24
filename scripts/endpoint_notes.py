"""Authored endpoint explanations used by the documentation renderer."""
from expanded_notes import NOTES as EXPANDED_NOTES
from research_notes import NOTES as RESEARCH_NOTES

NOTES = {'search_companies': {'title': 'Company search API: filter B2B companies',
                      'purpose': 'Use company search when you can describe a business segment with explicit criteria: '
                                 'industry, geography, company size, funding stage or a financial band. The response is a '
                                 'bounded page of company cards that can become the input to profile, enrichment, financial '
                                 'and news requests. It is a discovery step, not a complete database export.',
                      'workflow': 'Discover a vocabulary label, search a narrow segment, review candidate names and '
                                  'descriptions, and save each accepted domain with your own account identifier. Increase '
                                  'page only after processing the current page. If a filter is restricted by your plan, '
                                  'show that restriction instead of silently claiming the entire segment was searched.',
                      'fields': {'data.companies': 'The company cards returned on this page. Use domain for the next '
                                                   'lookup; company_id may be a string or number.',
                                 'data.page / requested_limit / returned': 'Page zero is the first page. Requested and '
                                                                           'returned counts can differ.',
                                 'data.total': 'May be null. Never use the page length as an inferred market total.',
                                 'data.access': 'Effective plan, result caps, remaining search allowance and restricted '
                                                'filters when supplied.',
                                 'data.partial_timeout': 'A partial upstream search may have completed even when HTTP '
                                                         'status is 200.'},
                      'observed': 'The current Software/India capture preserves two source company cards and access '
                                  'metadata. Full detail values require get_company_field; sortable listings and on-demand '
                                  'columns are separate documented requests.',
                      'pitfall': "A company's headquarters and the market where it sells are different attributes. Also "
                                 'distinguish a revenue-band filter from an exact revenue figure for a known fiscal year.',
                      'guide': 'company-search-api'},
 'semantic_company_search': {'title': 'Semantic company search API: natural-language business discovery',
                             'purpose': 'Use semantic search when you know the business problem or product category but do '
                                        "not yet know Radar's classification labels. A natural-language query can be "
                                        'combined with supported company filters. Returned businesses are candidates for '
                                        'review, not a certified list of every company matching the sentence.',
                             'workflow': 'Describe a product or service in a short, specific query. Examine returned '
                                         'company descriptions and domains, then use structured company search if you need '
                                         'a repeatable segment. Save the original query with the results so another analyst '
                                         'understands why each candidate was retrieved.',
                             'fields': {'data.companies': 'Candidate company cards; the source may return fewer than '
                                                          'requested.',
                                        'data.total': 'Unknown totals remain null.',
                                        'data.access': 'Plan restrictions apply to semantic and structured searches alike.',
                                        'data.pagination': 'Instructions for the bounded page model; no cursor is implied.'},
                             'observed': 'The captured enterprise-software query returned one company, Karanam, although '
                                         'the request allowed two. The endpoint returned no public relevance score. That '
                                         'output is a useful discovery lead, but the preview has not measured precision or '
                                         'recall for this query.',
                             'pitfall': 'Do not turn the ordering into a numerical relevance rating or promise that the '
                                        'first match is the best supplier. Product meaning, corporate identity and '
                                        'geography still need review.',
                             'guide': 'company-search-api'},
 'get_company': {'title': 'Company profile API: identity and available fields',
                 'purpose': 'Retrieve a compact company identity by domain. The response keeps the important name, domain, '
                            'company ID, short description, founding year, employee count and Radar image URL. It lists '
                            'available detail fields and contact availability without returning their values. Use '
                            'get_company_field for exactly one rich field per separate JSON POST.',
                 'workflow': 'Find a company, verify its identity, inspect available_fields and field_status, then POST '
                             'domain and field to /v1/companies/field. Email and phone values use the separate contact '
                             'endpoints and paid-access checks.',
                 'fields': {'data.company': 'Compact identity only; no founder roster, technology arrays, traffic or legal '
                                            'archive.',
                            'data.available_fields': 'Names of observed detail fields, not their values.',
                            'data.field_status': 'available, not_observed, unavailable or partial for each field.',
                            'data.contacts.availability': 'Email/phone presence booleans; not contact values or '
                                                          'entitlement.',
                            'data.field_request': 'The separate field endpoint and its required JSON keys.'},
                 'observed': 'The live Razorpay response contains compact identity and available-field metadata. Its richer '
                             'classification, founders, seventy technology entries, traffic and app observations are '
                             'captured through separate field requests in COMPANY_DATA_DEPTH.md. The profile no longer '
                             'embeds them.',
                 'pitfall': 'Availability is a stored-data observation. It is not a promise of current facts or contact '
                            'entitlement. Old sections/item_limit inputs on get_company now return HTTP 422.',
                 'guide': 'company-data-api'},
 'get_company_intelligence': {'title': 'Company intelligence API: scores, risks and business context',
                              'purpose': "Retrieve Radar's computed view of a company's market position, innovation, "
                                         'management signals, financial trajectory, risk and investment readiness. This '
                                         'endpoint is useful for deciding which evidence to investigate next. Its scores '
                                         'and narratives are derived assessments and should remain separate from financial '
                                         'statement facts.',
                              'workflow': 'Read the computation date and the component you need, then retrieve the '
                                          'supporting company events or financial metrics separately. Build a research view '
                                          'that labels a risk score as derived and a filing-sourced revenue value as '
                                          'retrieved financial evidence. Preserve a gap when a component is absent.',
                              'fields': {'data.domain / computed_at': 'The requested company and the source computation '
                                                                      'time, distinct from gateway retrieval time.',
                                         'data.intel.company_meta': 'Available size, stage, market and other company '
                                                                    'context.',
                                         'data.intel.investment_readiness': 'Derived labels and scores, not a '
                                                                            'recommendation issued by this gateway.',
                                         'data.intel.risk_profile': 'Derived risk indicators and component counts when '
                                                                    'supplied.',
                                         'data.intel.earnings': 'Source earnings context; use get_financials for normalized '
                                                                'metric provenance.'},
                              'observed': 'The live Microsoft response included all available intelligence components and '
                                          'an earnings archive with gated history. The example now retains the full '
                                          'captured intelligence object, rather than selecting a few scores. Archive gates '
                                          'remain source-controlled.',
                              'pitfall': 'Do not sum unrelated score families, treat a score as a probability, or label a '
                                         'computed assessment as an audited financial value. The gateway does not establish '
                                         "the source scoring model's calibration.",
                              'guide': 'competitor-intelligence-api'},
 'get_financials': {'title': 'Financial data API: company statements with fiscal periods and sources',
                    'purpose': 'Retrieve available income-statement, balance-sheet and cash-flow metrics in one normalized '
                               'period model. Each numerical metric retains currency, unit, original-currency information '
                               'where supplied, and a source type. This is useful for a financial research table that must '
                               'explain what each number represents.',
                    'workflow': 'Choose statement and annual/quarterly filters, inspect the accessible periods, and display '
                                'every value with its currency and fiscal label. Follow article_ids only through an '
                                'authorized News connection. Align actual fiscal dates before making a cross-company '
                                'comparison; do not substitute reporting date for period_end.',
                    'fields': {'data.periods[].period / fiscal_year / fiscal_period': 'Source fiscal labels, not '
                                                                                      'necessarily calendar-year labels.',
                               'data.periods[].period_end / reported_date / filed_date': 'Different date meanings. An '
                                                                                         'unknown period end remains null.',
                               'data.periods[].metrics.*': 'value, currency, unit, source_type, native_value and '
                                                           'native_currency.',
                               'data.periods[].evidence / operating_context': 'Article counts, source quality flags and income-specific headcount, growth and guidance. Guidance currency/horizon can be unknown.',
                               'data.summary.assessment / comparison_periods / source_coverage': 'Upstream company-window context, independent of the request filters. Not additional accessible archive rows.',
                               'data.coverage': 'Accessible, matching and metric-bearing period counts; statement metrics requested.',
                               'data.access_limited / available_period_count': 'A larger known archive may exist beyond the '
                                                                               "linked account's view.",
                               'data.returned / truncated': 'The response limit and account gates can both reduce visible '
                                                            'history.'},
                    'observed': 'The electroCore annual-income request returned FY2024 revenue of USD 25,200,000, '
                                'net income of USD -11,890,000, EBITDA of USD -9,000,000 and EPS -1.59, with '
                                'news_report provenance. The negative values are preserved. This is an actual populated '
                                'income example, not independently audited financials. The separate balance-sheet and '
                                'cash-flow scenario pages are marked blocked because they returned no requested metrics; '
                                'strict source checks on 2026-09-24 failed on an unreachable financial-store shard.',
                    'pitfall': 'Missing metrics are omitted; zero and negative values are real values and must be retained. '
                               'Do not invent filing URLs, calculate FX conversions from guessed rates, or assume that '
                               'available_period_count equals accessible rows.',
                    'guide': 'financial-data-api'},
 'get_company_events': {'title': 'Company events API: business activity and effective date windows',
                        'purpose': "Retrieve a company's event timeline and available activity summaries. Use the timeline "
                                   'for company monitoring and the summaries as context, while inspecting their respective '
                                   'windows. A plan can expose a shorter timeline than the number of days requested.',
                        'workflow': "Request a bounded window, read window.effective_days and the source's freshness "
                                    'fields, and deduplicate stable article or event identifiers in your application. Show '
                                    'source dates and retrieval time separately. If you poll, each successful call is a new '
                                    'data operation.',
                        'fields': {'data.events': 'Returned timeline rows; an empty list is a valid response shape.',
                                   'data.window_days / window.effective_days': 'The effective source window after account '
                                                                               'gates.',
                                   'data.truncated': 'Indicates the returned timeline is not an unrestricted complete '
                                                     'archive.',
                                   'data.freshness': 'Latest event and insertion timestamps supplied by the source.',
                                   'data.pulse': 'Broader activity indicators can use windows different from the visible '
                                                 'event list.'},
                        'observed': 'The captured thirty-day Microsoft request returned events=[] and truncated=true. Its '
                                    'source freshness pointed to an older latest event date, and its pulse included broader '
                                    'historical activity. An empty thirty-day list therefore cannot establish that the '
                                    'company has never had any relevant events.',
                        'pitfall': 'Do not mix a 360-day activity score with a thirty-day visible event count, and do not '
                                   'turn a freshness gap into a claim that no news exists.',
                        'guide': 'company-monitoring-api'},
 'get_company_funding': {'title': 'Company funding API: reported rounds, amounts and investors',
                         'purpose': 'Retrieve reported company funding rounds and associated investor information. The '
                                    'endpoint is designed for a fundraising-history section or a research drilldown from '
                                    'company discovery. It does not represent a capitalization table, audited capital '
                                    'receipts or confirmed current ownership percentages.',
                         'workflow': 'Review round dates, labels and amount_approx together. Compare reported investors '
                                     'with the underlying announcement when available through News. Keep debt, equity, '
                                     'valuation, cumulative funding and individual round amounts separate in your own data '
                                     'model.',
                         'fields': {'data.rounds': 'Reported financing entries with a name, date, amount and investor '
                                                   'associations when available.',
                                    'data.amount_approx': 'A source qualifier that must travel with displayed amounts.',
                                    'data.investors': 'Company-level investor records, not automatically participants in '
                                                      'every round.',
                                    'data.stages': 'Source stage summaries; avoid adding these to individual rounds as if '
                                                   'they were separate transactions.'},
                         'observed': 'The OpenAI capture contained ten round records and amount_approx=true. Its source '
                                     'announcement text and structured investor associations were not fully reconciled: one '
                                     'announcement referred to SoftBank while a structured association named Microsoft. The '
                                     'excerpt retains numerical and identity fields but omits long announcement text. '
                                     'Review the source before treating a particular association as confirmed '
                                     'participation.',
                         'pitfall': 'Several reports can describe the same transaction. Summing every round, stage summary '
                                    'and announcement together can double-count capital; a funding amount is not '
                                    'automatically a valuation.',
                         'guide': 'startup-funding-data-api'},
 'get_company_enrichment': {'title': 'Company enrichment API: legal, digital and reputation data',
                            'purpose': 'Add context to an existing company domain using available legal registrations, '
                                       'digital audience information, reputation summaries and share-of-voice data. These '
                                       'sections come from different source processes and should not be presented as if all '
                                       'were measured on the same date.',
                            'workflow': 'Retrieve the base company profile, then inspect enrichment sections relevant to '
                                        'your use case. Preserve section dates, units and source categories. Map known '
                                        'values into your account model; leave existing data intact when a section is '
                                        'missing or its coverage is unknown.',
                            'fields': {'data.has_data': 'Some enrichment exists; this is not a completeness certificate.',
                                       'data.legal': 'Available legal names and registry identifiers, which can help review '
                                                     'domain-identity ambiguity.',
                                       'data.digital.visits / visits_date': 'Traffic observation and its source period; not '
                                                                            'company revenue or customer count.',
                                       'data.reputation.score / n': 'A source-specific score and review count, not a '
                                                                    'gateway quality guarantee.',
                                       'data.sov': 'Available comparison context whose denominator depends on the source '
                                                   'cohort.'},
                            'observed': 'The Stripe capture returned digital traffic and audience, hiring history and '
                                        'roles, innovation and patents, social engagement, activity, legal entries, '
                                        'reputation aggregates and share-of-voice peers. All these business-data sections '
                                        'and their array rows are shown. Individual review snippets are excluded from '
                                        'documentation reproduction.',
                            'pitfall': 'The source does not always distinguish a missing section from a failed enrichment '
                                       'subsection. Do not interpret an omitted legal, reputation or digital field as proof '
                                       'of nonexistence.',
                            'guide': 'company-enrichment-api'},
 'find_competitors': {'title': 'Competitor discovery API: companies grouped by funding stage',
                      'purpose': 'Find candidate peer companies for a named market, optionally narrowed by business model. '
                                 'The source groups returned companies by funding stage. This is market discovery, not a '
                                 'verified competitive-ranking model or a list centered on an input company domain.',
                      'workflow': 'Choose a precise market label from industry discovery, request a small number of '
                                  "companies per stage, and review each candidate's product and geography. Pass selected "
                                  'distinct domains to compare_companies for separate profile and financial evidence.',
                      'fields': {'data.market': 'The market label supplied in the request.',
                                 'data.companies': 'A dictionary of returned stage groups, each containing company cards.',
                                 'data.summary': 'Additional source summary fields when available.',
                                 'per_stage': 'Requested companies per stage, between three and ten; this is not a global '
                                              'result limit.'},
                      'observed': 'The Payments query returns fifteen peer cards: three each in Seed, Series A, Series B, '
                                  'Series C and Public. The source summary totals 52 sampled candidates across a wider set '
                                  'of stages; it is not a full-market census or the number of cards delivered in these five '
                                  'groups.',
                      'pitfall': 'Do not describe an empty or narrow source result as the full competitive landscape. A '
                                 'similar industry label does not establish that two businesses compete for the same buyer.',
                      'guide': 'competitor-intelligence-api'},
 'company_brief': {'title': 'Company brief API: compact summaries and detail requests',
                   'purpose': 'Combine compact profile, financial, intelligence, event, funding, enrichment and news '
                              'summaries. This endpoint does not embed full rich company records, funding rosters or '
                              'article bodies. Every successful section includes a separate detail_request so clients can '
                              'choose the next read.',
                   'workflow': 'Review the compact identity and latest financial period, inspect section availability and '
                               'dates, then call only the detail endpoint required for your workflow. Use the profile '
                               'available_fields list to retrieve a single field.',
                   'fields': {'data.sections.*.available': 'Whether the source section supplied data. Empty recent-event '
                                                           'windows can still be available.',
                              'data.sections.*.result': 'A compact summary with the original section window, source '
                                                        'metadata and partial flag.',
                              'data.sections.*.detail_request': 'Method, path and JSON body for a separate read.',
                              'data.sections.profile.result.data.available_fields': 'Observed company fields to request '
                                                                                    'individually.',
                              'data.partial': 'True if a section failed or has partial coverage.'},
                   'observed': 'The refreshed Stripe brief uses real Radar data and the documented isolated News '
                               'integration identity. It returns summaries for seven available sections and short linked '
                               'headlines; it does not establish a deployed News connection. The source Tracxn logo URL is '
                               'no longer exposed.',
                   'pitfall': 'Financial periods and source windows differ between sections. Summaries are not a complete '
                              'company archive; follow the detail request and its access limits.',
                   'guide': 'b2b-data-api'},
 'compare_companies': {'title': 'Company comparison API: profiles, financials and intelligence',
                       'purpose': 'Retrieve comparable research sections for two to five selected company domains. The '
                                  "response organizes each company's profile, financials and intelligence separately. It "
                                  'does not normalize fiscal calendars, compute a combined valuation or rank investment '
                                  'opportunities.',
                       'workflow': 'Select companies through search or competitor discovery, verify their identities, and '
                                   'request distinct domains. Build a comparison table from available metrics while '
                                   'retaining period labels, currency and source type. Leave cells unknown when one company '
                                   'lacks a metric or section.',
                       'fields': {'data.companies[].domain': 'Which requested company each section set describes.',
                                  'data.companies[].sections': 'Profile, financials and intelligence envelopes for that '
                                                               'company.',
                                  'data.companies[].partial / error': 'Company-level gaps can coexist with successful '
                                                                      'peers.',
                                  'data.comparison_note': 'The response explicitly avoids cross-company totals or ranking.',
                                  'meta.billing': 'Account mode reserves three credits per company and refunds failed '
                                                  'sections.'},
                       'observed': 'The live Razorpay/Stripe comparison returned both companies with compact identity, '
                                   'latest-period financial evidence and derived-score summaries. Each section supplies a '
                                   'separate detail_request; full profile fields and financial histories require their own '
                                   'calls.',
                       'pitfall': 'Never convert a missing financial value to zero just to make a comparison table '
                                  'rectangular. An alias in a company profile must be reviewed before attaching a corporate '
                                  "parent's financial history.",
                       'guide': 'competitor-intelligence-api'},
 'search_investors': {'title': 'Investor search API: discover investors by business filters',
                      'purpose': 'Discover investor entities using supported headquarters and portfolio-related filters. '
                                 'This uses the same bounded company-search input model but selects investor entities '
                                 'internally. It is useful for the first stage of a venture-capital or investment research '
                                 'workflow.',
                      'workflow': 'Begin with a narrow geography or portfolio category, inspect returned investor identity, '
                                  'then use the published investor directory or company funding history for supporting '
                                  'context. A discovered investor is not a verified current mandate or a promise of funding '
                                  'availability.',
                      'fields': {'data.companies': 'Investor company cards when the source query succeeds.',
                                 'data.access': 'Effective plan, filter restrictions and result caps.',
                                 'data.total': 'May be unknown; a page count is not a complete investor universe.',
                                 'error.kind': 'A failed search is explicitly different from an empty successful page.'},
                      'observed': 'The source investor path does not return strict tier metadata. The default strict request excluded five unverified cards. This capture explicitly selects expanded mode to show those candidates with match_tier=unverified; it does not certify every filter.',
                      'pitfall': 'Do not retry a broad expensive search in a tight loop or convert a timeout into '
                                 'companies=[]. Narrow the query, use backoff and retain the failure status in your '
                                 'research workflow.',
                      'guide': 'investor-data-api'},
 'investor_directory': {'title': 'Investor directory API: published profiles, lists and locations',
                        'purpose': 'Discover published investor pages without guessing URL slugs. The directory includes '
                                   'page counts and selected profiles, lists, cities and sectors. It is particularly useful '
                                   'when an application needs navigable investor research pages rather than a free-form '
                                   'company query.',
                        'workflow': 'Request the directory with an empty JSON body, select a returned slug and pass it to '
                                    "get_investor_page. Keep the record's family or kind so your application can "
                                    'distinguish an investor profile from a curated list. Do not construct slugs by '
                                    'lowercasing a display name.',
                        'fields': {'data.counts': 'Published-page counts by source category, not necessarily unique '
                                                  'investor entities.',
                                   'data.top_profiles[].slug': 'The identifier to use in the investor-page request.',
                                   'data.top_lists / top_angel_lists': 'Published list references when available.',
                                   'data.cities / sectors': 'Navigation categories with source counts that can overlap.'},
                        'observed': 'The live directory supplied anupam-mittal as a profile slug. That returned identifier '
                                    'was used for the separate successful investor-page capture. The source also returned '
                                    'counts for investor lists, angel lists and profiles; those categories should not be '
                                    'summed into a unique-investor estimate.',
                        'pitfall': 'Directory metadata may be available even when the detailed roster behind a published '
                                   'page has another access gate. Do not imply that every directory entry includes an '
                                   'unrestricted investor dataset.',
                        'guide': 'investor-data-api'},
 'get_investor_page': {'title': 'Investor profile API: portfolio metrics and available research fields',
    'purpose': 'Retrieve measured investor or directory metrics, source dates and available detail fields from the verified Atlas release. The live Radar publication gate is checked on every request.',
    'workflow': 'Discover a slug, request its summary, then POST the slug and one field to get_investor_field. Portfolio, co-investors, cohorts, sourced news and market shortlists have separate retrieval.',
    'fields': {'data.metrics': 'Whole and dated portfolio counts, entry stages, disclosed whole-round size quartiles and activity. Directory pages instead carry measured totals.',
               'data.available_fields / field_counts': 'Available field names and stored array counts; no roster is embedded in this summary.',
               'data.coverage': 'Source cutoff, computation date, last observation, immutable release and verified snapshot fingerprint.',
               'data.definitions': 'Definitions that distinguish round amounts, financing cohorts and selected investor populations.'},
    'observed': 'Anupam Mittal has 270 recorded companies and 303 equity participations; the dated analytical subset is 268 companies and 301 participations. Coverage ends 2026-05-22 and his last recorded investment is 2026-03-28. The median disclosed entry round is USD 222,410 across 247 entries; this is not his personal cheque.',
    'pitfall': 'Retrieval time does not advance a snapshot cutoff. If detail storage is disconnected, the response is explicitly metadata-only and partial. A live publication gate never substitutes for the rich data connection.',
    'guide': 'investor-data-api'},
 'get_investor_field': {'title': 'Investor portfolio, co-investor, follow-on analysis and funding news API',
    'purpose': 'Request one rich investor field or one market-directory field with complete business attributes. Portfolio and shortlist arrays are paginated; analysis objects retain their full structure.',
    'workflow': 'Use available_fields from get_investor_page. Request portfolio to examine named investments, follow_on for measured 24-month outcomes, co_investors for syndicate relationships, news for dated source-linked reporting, or investors for a directory shortlist. Advance pagination.next_offset until null.',
    'fields': {'data.value': 'The selected data only. Portfolio rows retain identity, sector/stage, entry and latest dates, amounts, round counts, lead flags, syndicate size and later-financing outcomes.',
               'data.pagination': 'Stored source_total, filtered matched_total, returned count, offset, limit and next_offset. Present on array fields; nested row attributes are retained.',
               'data.coverage': 'Source cutoff and computation date, separate from retrieval time.',
               'data.definitions': 'Non-additive sectors, whole-round USD amounts and cohort eligibility definitions.'},
    'observed': 'The Anupam Mittal portfolio capture returns five complete company rows from 268 dated companies. Separate captures expose all ten available profile fields and nine FinTech/Bengaluru directory fields. Live pagination traversed all 268 portfolio rows and all 1,199 selected directory investors.',
    'pitfall': 'Directory shortlists are selected subsets, not the full investor universe. Offsets page top-level arrays; portfolio filters accept q, sector, stage, city and country, while directory investors accept q, stage, city, country and kind. LinkedIn reveals, emails, phone numbers and internal source identifiers are excluded.',
    'guide': 'investor-data-api'},
 'market_pulse': {'title': 'Market pulse API: funding activity and trending business categories',
                  'purpose': "Retrieve Radar's existing market pulse: funding summaries, recent-funding candidates, "
                             'investor references and trending categories. It can help an analyst decide which market or '
                             'company to investigate next. The gateway returns source observations rather than calculating '
                             'a fresh market census.',
                  'workflow': 'Request a bounded day window and a small limit. Inspect the dates and amount fields of '
                              'returned funding records before placing them on a timeline. Follow a company domain into its '
                              'funding history and associated news, and review the original evidence before adding any '
                              'market totals.',
                  'fields': {'data.config': 'The effective source request configuration.',
                             'data.funding_pulse': 'Source summary counters, whose coverage is not a complete capital-flow '
                                                   'measure.',
                             'data.recent_fundings': 'Candidate funding records; check dates and sentinel values.',
                             'data.trending_markets / top_investors': 'Available category and entity references, not a '
                                                                      'comprehensive ranking universe.'},
                  'observed': 'The live output contained a recent_fundings row dated 2074-08-22 and latest_deal_amount=-1. '
                              'Those are retained in the excerpt to expose the source issue. They must not be presented as '
                              'a current funding event or a negative-dollar transaction. This capture demonstrates the '
                              'response shape and a validation need, not validated recent-funding coverage.',
                  'pitfall': 'Reject or quarantine future-dated activity and documented unknown-value sentinels in your '
                             "application view. Do not use the source's recent label alone to establish recency, or sum "
                             'overlapping summaries as total invested capital.',
                  'guide': 'startup-funding-data-api'},
 'location_intelligence': {'title': 'Location intelligence API: business context by geography',
                           'purpose': "Request Radar's existing analytical context for a named geography. The location_type "
                                      'tells the source whether the name is a city, state, country or country code. This '
                                      'endpoint is a specific geographical-research request, not arbitrary SQL or a general '
                                      'report-generation job.',
                           'workflow': 'Choose the intended geographic level explicitly. If the source returns data, '
                                       "preserve the geography and the source's definitions before comparing it with "
                                       'another place. Avoid treating similarly named cities or states as interchangeable '
                                       'identifiers.',
                           'fields': {'location': 'The place name supplied to the source.',
                                      'location_type': 'city, state, country or cc; the default is country.',
                                      'data': 'The source analytical payload when available; no universal metric '
                                              'completeness is promised.',
                                      'error.kind / message': 'Explicit source availability failures.'},
                           'observed': 'The India/country request was retried on 2026-09-21 and still returns HTTP 502 '
                                       'upstream_unavailable; a direct read-only probe confirmed HTTP 500 at the Radar '
                                       'source. This remains an unresolved source failure. The separate city adapter was '
                                       "corrected to pass the source's location label, but that fix does not establish "
                                       'location-service availability.',
                           'pitfall': 'Do not interpret a service error as zero companies, zero funding or no economic '
                                      'activity in the location. Data availability and the underlying economic quantity are '
                                      'different questions.',
                           'guide': 'b2b-data-api'},
 'discover_industries': {'title': 'Industry discovery API: find market, sector and industry labels',
                         'purpose': 'Find a small set of vocabulary labels that can be used in company and investor '
                                    'filters. A search phrase may match a market, a sector or an industry; the returned '
                                    'kind tells you which structured filter field to use.',
                         'workflow': 'Send a specific term, examine the returned names, and place the chosen label in '
                                     'filters.markets, filters.sectors or filters.industries according to kind. Then run a '
                                     'bounded company search. This reduces errors caused by guessing the classification '
                                     'vocabulary.',
                         'fields': {'data.query': 'The submitted lookup phrase.',
                                    'data.matches[].name': 'A source classification label.',
                                    'data.matches[].kind': 'market, sector or industry; use the corresponding plural filter '
                                                           'name.',
                                    'limit': 'At most five lookup matches can be requested.'},
                         'observed': 'The live software lookup returned Software Libraries with kind=market. That should be '
                                     'placed in filters.markets, not automatically in industries simply because the request '
                                     'searched for an industry-like term.',
                         'pitfall': 'A returned label is a vocabulary match, not a count of companies in that category. Do '
                                    'not equate a broad common word with every source classification containing it.',
                         'guide': 'company-search-api'},
 'search_jobs': {'title': 'Jobs API: search company hiring by role, skills and location',
                 'purpose': 'Search observed job listings using employer name, role, geography, skills, remote status and '
                            'freshness. The company filter is a name prefix, not a domain lookup. The response can support '
                            'a hiring-signals section in company research. It does not submit applications, upload resumes '
                            'or guarantee that every listed role remains open.',
                 'workflow': 'Start with a company or narrow role/geography combination, check whether the response is '
                             'partial, and save stable job IDs before requesting detail. Preserve source dates. A posting '
                             'is an observed vacancy signal, not evidence that a person was hired.',
                 'fields': {'data.jobs': 'Returned listings; extract an actual ID for get_job.',
                            'data.total_estimate / total_capped': 'A capped estimate is not an exact vacancy count.',
                            'data.partial_timeout / meta.partial': 'Incomplete source work can be returned with HTTP 200.',
                            'data.page / page_size / access': 'Page and effective account result limits.'},
                 'observed': 'A software engineer title-prefix query in the US returns three real job listings from 503 '
                             'matches with partial_timeout=false and total_capped=false. Cards include returned IDs, '
                             'employer names, locations, posting dates and source URLs. Unknown salary and company-domain '
                             'fields remain null. The first returned ID successfully resolves in the job-detail example.',
                 'pitfall': 'Never display the capped estimate as an exact market total or overwrite existing jobs with an '
                            'empty partial page. Retain the failure/partial state and retry a narrower query with backoff.',
                 'guide': 'hiring-signals-jobs-api'},
 'companies_hiring': {'title': 'Hiring companies API: discover employers from recruitment signals',
                      'purpose': 'Use the same job filters to discover companies associated with observed hiring. This is '
                                 'useful when your unit of research is the employer rather than an individual vacancy. It '
                                 'is separate from firmographic company search and from a measured headcount-growth '
                                 'dataset.',
                      'workflow': 'Select a skill, role or geography, inspect returned company identity, and retrieve its '
                                  'company profile before enriching an account list. Keep the source query and partial '
                                  'status alongside the hiring observation so a later analyst can assess the evidence.',
                      'fields': {'data.companies': 'Returned hiring-company records when available.',
                                 'data.total / total_capped': 'Source count and any cap, subject to partial coverage.',
                                 'data.partial_timeout': 'A partial empty result must not be treated as a complete negative '
                                                         'result.',
                                 'data.access': 'Linked plan and query-result restrictions.'},
                      'observed': 'The narrower US machine learning engineer query returns three employers with observed '
                                  'open-role counts, example titles and locations, without a partial timeout. '
                                  'total_capped=true remains visible: three is the delivered grouped result, not a complete '
                                  'count of every employer hiring for that role. Missing resolved domains are not inferred '
                                  'from employer names.',
                      'pitfall': "A vacancy signal is not a confirmed net-new employee or a company's total workforce. Do "
                                 'not rank business growth solely from a partial hiring feed.',
                      'guide': 'hiring-signals-jobs-api'},
 'get_job': {'title': 'Job detail API: retrieve a listing by returned job ID',
             'purpose': 'Retrieve one job listing after discovery. The accepted identifier should come from search_jobs. '
                        'This separates a lightweight results page from a detail view and avoids inferring detail URLs from '
                        'company names or job titles.',
             'workflow': 'Run a successful nonpartial search, retain its listing ID, then request detail. Keep any date and '
                         'source link provided. If detail no longer exists, mark it unavailable without automatically '
                         'removing unrelated job observations.',
             'fields': {'id': 'A job identifier returned by search, using the allowed ID characters.',
                        'data': 'The source listing representation when available.',
                        'error.kind=no_data': 'No accessible listing was returned for that identifier.'},
             'observed': 'The capture now uses talent:636631531523081796 from successful job search and returns HTTP 200: '
                         'Software Engineer Controls at Optimal Inc., Sunrise, Florida, US. Posting date, source URL, '
                         'employment type and active flag are returned. Salary, resolved company domain and validity end '
                         'remain unknown. Long job-description prose is omitted only from the documentation projection.',
             'pitfall': 'A 404 can reflect an unknown, removed or inaccessible listing; it does not establish that the '
                        'employer has no vacancies. Do not turn the sample negative ID into a recommended production '
                        'identifier.',
             'guide': 'hiring-signals-jobs-api'},
 'salary_benchmark': {'title': 'Salary benchmark API: role and geography statistics',
                      'purpose': 'Retrieve source salary statistics for a role, geography and optional currency. Use it to '
                                 'add sample-based compensation context to a research interface, while keeping the '
                                 'observation count and sparse-data indicator visible.',
                      'workflow': 'Choose a specific role and location, request the intended currency, and inspect sample '
                                  'count before displaying any summary. Compare like geography and currency. Do not convert '
                                  "a benchmark into a promise of an individual company's compensation offer.",
                      'fields': {'data.count': 'The number of observed records in the source sample.',
                                 'data.currency': 'The requested or returned currency context.',
                                 'data.sparse': 'The sample is too sparse for a strong benchmark interpretation.',
                                 'data.filter_echo': "The source's effective filters, which may normalize country names to "
                                                     'codes.'},
                      'observed': 'The US/software engineer/USD query returns 206 observations, sparse=false, p25=99025, '
                                  'median=124000 and p75=150000. These are source salary-midpoint statistics within one '
                                  'currency. A salary period is not supplied here, so the documentation does not invent '
                                  'annual or hourly units. This explicitly different query does not replace the earlier '
                                  'sparse India sample with a US salary.',
                      'pitfall': 'An absent salary statistic is unknown, not a zero salary. A large salary figure from '
                                 'another region or currency is not a valid substitute for a sparse requested sample.',
                      'guide': 'hiring-signals-jobs-api'},
 'search_people': {'title': 'Professional profile search API: founders, investors and executives',
                   'purpose': 'Search professional profiles by name, supported role categories, current company, skills and '
                              'location. Use this for identity context in company or investor research. The gateway '
                              'keeps professional detail; email and phone retrieval use separate explicit contact endpoints.',
                   'workflow': 'Start with a name plus a company or location when possible. Review current title, company '
                               'domain and returned identifiers before associating a person with an account. Treat source '
                               'role categories as labels to inspect, not verified legal or employment status.',
                   'fields': {'data.people[].id / name': 'The returned profile identity.',
                              'data.people[].current_title / current_company_domain': 'Available professional context for '
                                                                                      'matching.',
                              'data.people[].people_types': "Source categories that can differ from the person's current "
                                                            'job title.',
                              'data.total_estimate / total_capped / partial_timeout': 'Count precision and query '
                                                                                      'completeness.',
                              'data.access': "The account's effective access restrictions."},
                   'observed': 'The Satya Nadella query returned a Microsoft professional profile, while its people_types '
                               'classification included Angel Investor. The example preserves professional skills, education, experience, scores and founder/investor attributes, and '
                               'omits biography and unnecessary personal attributes. A returned category is not proof of '
                               'participation in a particular financing round.',
                   'pitfall': 'Names are not unique. Do not attach a profile to the wrong company, reveal contact data from '
                              'another source, or interpret a source category as a verified current executive appointment.',
                   'guide': 'b2b-data-api'},
 'search_news': {'title': 'News search API: discover financial and business headlines',
                 'purpose': 'Search a topic or company for relevant news articles. Use this to discover source evidence, '
                            'then retrieve selected articles rather than treating a headline alone as a complete report.',
                 'workflow': 'Supply q or company, use explicit dates for a historical investigation, and check the '
                             'returned coverage before interpreting results. For cursor-based searches, send the returned '
                             'cursor unchanged with the same filters. Overview, trend and sentiment operations use their '
                             'own analysis models rather than headline pagination.',
                 'fields': {'data when connected': 'data.items and next_cursor when supplied; window and coverage describe '
                                                   'the accessible results',
                            'window': 'Effective source dates and data-through information, not an assurance of complete or '
                                      'current coverage.',
                            'meta.coverage / plan / quota': 'Relayed when the connected News service provides them.',
                            'error.kind=service_unavailable': 'The gateway has no configured connection for this operation.',
                            'error.kind=access_required': 'A linked News key is missing or the upstream account rejects '
                                                          'access.',
                            'data.items[].id / headline / url / publisher / published_at': 'Article identity, short source '
                                                                                           'title, attribution and '
                                                                                           'reporting date; separate from '
                                                                                           'retrieval time.',
                            'data.items[].sentiment / priority / classes': 'Derived labels and scores; classification paths '
                                                                           "and codes retain the source's taxonomy.",
                            'data.items[].organizations / people / country': 'Entities and location labels observed in the '
                                                                             'article; not proof of corporate ownership or '
                                                                             'residence.',
                            'data.returned / total_estimate / limit': 'Delivered page length, matching source count and '
                                                                      'requested page ceiling are distinct.',
                            'data.next_cursor / unresolved / duplicates_dropped': 'Continue with the opaque cursor and '
                                                                                  'unchanged filters; missing article '
                                                                                  'records and deduplicated URLs can '
                                                                                  'shorten a page.'},
                 'observed': 'The captured response was executed through the real gateway and News application against live '
                             'data, with an isolated test identity and quota dependencies. It verifies data retrieval, not '
                             'a deployed News URL, production key authentication or customer billing. The exact query '
                             'software earnings matched one article in April 2026. Its headline, publisher, source URL, '
                             'publication date, sentiment, priority, classifications, organizations and people are '
                             'retained. The requested limit is a ceiling, not an instruction to manufacture five items.',
                 'pitfall': "The example is a historical query, not a current news feed. Read each dataset's data_through "
                            'and freshness values. Configure both News service URLs and link an authorized News key for '
                            'normal use; local integration identities never enter the deployed gateway. Search-engine '
                            'results are not API responses.',
                 'guide': 'financial-news-api'},
 'search_business_news': {'title': 'Business news API: company-associated financial reporting',
                          'purpose': 'Retrieve headlines associated with a company domain or business topic. This is the '
                                     'news side of a company-research workflow, separate from structured financial '
                                     'statements and company-event summaries.',
                          'workflow': 'Supply q or company, use explicit dates for a historical investigation, and check '
                                      'the returned coverage before interpreting results. For cursor-based searches, send '
                                      'the returned cursor unchanged with the same filters. Overview, trend and sentiment '
                                      'operations use their own analysis models rather than headline pagination.',
                          'fields': {'data when connected': 'company-associated headline records, source references and '
                                                            'opaque cursor pagination when supplied',
                                     'window': 'Effective source dates and data-through information, not an assurance of '
                                               'complete or current coverage.',
                                     'meta.coverage / plan / quota': 'Relayed when the connected News service provides '
                                                                     'them.',
                                     'error.kind=service_unavailable': 'The gateway has no configured connection for this '
                                                                       'operation.',
                                     'error.kind=access_required': 'A linked News key is missing or the upstream account '
                                                                   'rejects access.',
                                     'data.items[].id / headline / url / publisher / published_at': 'Article identity, '
                                                                                                    'short source title, '
                                                                                                    'attribution and '
                                                                                                    'reporting date; '
                                                                                                    'separate from '
                                                                                                    'retrieval time.',
                                     'data.items[].sentiment / priority / classes': 'Derived labels and scores; '
                                                                                    'classification paths and codes retain '
                                                                                    "the source's taxonomy.",
                                     'data.items[].organizations / people / country': 'Entities and location labels '
                                                                                      'observed in the article; not proof '
                                                                                      'of corporate ownership or residence.',
                                     'data.returned / total_estimate / limit': 'Delivered page length, matching source '
                                                                               'count and requested page ceiling are '
                                                                               'distinct.',
                                     'data.next_cursor / unresolved / duplicates_dropped': 'Continue with the opaque cursor '
                                                                                           'and unchanged filters; missing '
                                                                                           'article records and '
                                                                                           'deduplicated URLs can shorten a '
                                                                                           'page.'},
                          'observed': 'The captured response was executed through the real gateway and News application '
                                      'against live data, with an isolated test identity and quota dependencies. It '
                                      'verifies data retrieval, not a deployed News URL, production key authentication or '
                                      "customer billing. Microsoft's April 2026 query returned five items from 4,401 "
                                      'matches, with an opaque next_cursor, source URLs, classifications and associated '
                                      "events. The source's latest news date is 2026-08-24, with a separate warning about "
                                      'thinner recent ingestion.',
                          'pitfall': "The example is a historical query, not a current news feed. Read each dataset's "
                                     'data_through and freshness values. Configure both News service URLs and link an '
                                     'authorized News key for normal use; local integration identities never enter the '
                                     'deployed gateway. Search-engine results are not API responses.',
                          'guide': 'financial-news-api'},
 'news_overview': {'title': 'News overview API: measured topic coverage and context',
                   'purpose': 'Request an overview for a focused query or company and a bounded date window. Use it to '
                              'inspect coverage and contextual examples before drawing a conclusion from a narrow headline '
                              'search.',
                   'workflow': 'Supply q or company, use explicit dates for a historical investigation, and check the '
                               'returned coverage before interpreting results. For cursor-based searches, send the returned '
                               'cursor unchanged with the same filters. Overview, trend and sentiment operations use their '
                               'own analysis models rather than headline pagination.',
                   'fields': {'data when connected': 'source overview data, measured coverage and effective window; not a '
                                                     'guaranteed narrative summary',
                              'window': 'Effective source dates and data-through information, not an assurance of complete '
                                        'or current coverage.',
                              'meta.coverage / plan / quota': 'Relayed when the connected News service provides them.',
                              'error.kind=service_unavailable': 'The gateway has no configured connection for this '
                                                                'operation.',
                              'error.kind=access_required': 'A linked News key is missing or the upstream account rejects '
                                                            'access.'},
                   'observed': 'The captured response was executed through the real gateway and News application against '
                               'live data, with an isolated test identity and quota dependencies. It verifies data '
                               'retrieval, not a deployed News URL, production key authentication or customer billing. The '
                               'same software earnings query matched one April article, with one positive sentiment '
                               'observation and one article meeting the supplied critical-priority threshold. These are '
                               'measured classifications of one record, not a broad market conclusion.',
                   'pitfall': "The example is a historical query, not a current news feed. Read each dataset's data_through "
                              'and freshness values. Configure both News service URLs and link an authorized News key for '
                              'normal use; local integration identities never enter the deployed gateway. Search-engine '
                              'results are not API responses.',
                   'guide': 'financial-news-api'},
 'news_trends': {'title': 'News trends API: daily, weekly and monthly volume',
                 'purpose': 'Measure observed news volume over time for a topic or company. This supports a trend chart '
                            "whose denominator is the connected News service's accessible records, rather than every "
                            'publication on the internet.',
                 'workflow': 'Supply q or company, use explicit dates for a historical investigation, and check the '
                             'returned coverage before interpreting results. For cursor-based searches, send the returned '
                             'cursor unchanged with the same filters. Overview, trend and sentiment operations use their '
                             'own analysis models rather than headline pagination.',
                 'fields': {'data when connected': 'time buckets and coverage when supplied; granularity selects daily, '
                                                   'weekly or monthly grouping',
                            'window': 'Effective source dates and data-through information, not an assurance of complete or '
                                      'current coverage.',
                            'meta.coverage / plan / quota': 'Relayed when the connected News service provides them.',
                            'error.kind=service_unavailable': 'The gateway has no configured connection for this operation.',
                            'error.kind=access_required': 'A linked News key is missing or the upstream account rejects '
                                                          'access.'},
                 'observed': 'The captured response was executed through the real gateway and News application against live '
                             'data, with an isolated test identity and quota dependencies. It verifies data retrieval, not '
                             'a deployed News URL, production key authentication or customer billing. The April software '
                             'earnings series has five weekly buckets, one matched article, three complete periods and two '
                             'partial boundary periods. The returned peak bucket is 2026-04-13; boundary buckets are not '
                             'silently treated as complete weeks.',
                 'pitfall': "The example is a historical query, not a current news feed. Read each dataset's data_through "
                            'and freshness values. Configure both News service URLs and link an authorized News key for '
                            'normal use; local integration identities never enter the deployed gateway. Search-engine '
                            'results are not API responses.',
                 'guide': 'financial-news-api'},
 'news_sentiment': {'title': 'News sentiment API: company tone distributions over time',
                    'purpose': "Retrieve the source's sentiment distribution and timeline for a company or topic. Sentiment "
                               'is a derived classification of observed content, not a factual determination that a '
                               'business is performing well or badly.',
                    'workflow': 'Supply q or company, use explicit dates for a historical investigation, and check the '
                                'returned coverage before interpreting results. For cursor-based searches, send the '
                                'returned cursor unchanged with the same filters. Overview, trend and sentiment operations '
                                'use their own analysis models rather than headline pagination.',
                    'fields': {'data when connected': 'source sentiment categories, timelines and coverage when supplied',
                               'window': 'Effective source dates and data-through information, not an assurance of complete '
                                         'or current coverage.',
                               'meta.coverage / plan / quota': 'Relayed when the connected News service provides them.',
                               'error.kind=service_unavailable': 'The gateway has no configured connection for this '
                                                                 'operation.',
                               'error.kind=access_required': 'A linked News key is missing or the upstream account rejects '
                                                             'access.'},
                    'observed': 'The captured response was executed through the real gateway and News application against '
                                'live data, with an isolated test identity and quota dependencies. It verifies data '
                                'retrieval, not a deployed News URL, production key authentication or customer billing. The '
                                'Microsoft analysis matched 4,401 April articles and returned label/group counts, baseline '
                                'comparisons and a weekly timeline. Preserve the source denominator and baseline window '
                                'when interpreting percentages or ratios.',
                    'pitfall': "The example is a historical query, not a current news feed. Read each dataset's "
                               'data_through and freshness values. Configure both News service URLs and link an authorized '
                               'News key for normal use; local integration identities never enter the deployed gateway. '
                               'Search-engine results are not API responses.',
                    'guide': 'financial-news-api'},
 'search_business_events': {'title': 'Business news events API: structured events with article references',
                            'purpose': 'Discover structured business events associated with a company or topic through the '
                                       "News service. This differs from Radar's company event timeline: it uses the "
                                       'connected business-news contract and its own date window, quotas and article '
                                       'identifiers.',
                            'workflow': 'Supply q or company, use explicit dates for a historical investigation, and check '
                                        'the returned coverage before interpreting results. For cursor-based searches, send '
                                        'the returned cursor unchanged with the same filters. Overview, trend and sentiment '
                                        'operations use their own analysis models rather than headline pagination.',
                            'fields': {'data when connected': 'business event records and article references when supplied; '
                                                              'event and publication dates must remain distinct',
                                       'window': 'Effective source dates and data-through information, not an assurance of '
                                                 'complete or current coverage.',
                                       'meta.coverage / plan / quota': 'Relayed when the connected News service provides '
                                                                       'them.',
                                       'error.kind=service_unavailable': 'The gateway has no configured connection for this '
                                                                         'operation.',
                                       'error.kind=access_required': 'A linked News key is missing or the upstream account '
                                                                     'rejects access.'},
                            'observed': 'The captured response was executed through the real gateway and News application '
                                        'against live data, with an isolated test identity and quota dependencies. It '
                                        'verifies data retrieval, not a deployed News URL, production key authentication or '
                                        'customer billing. The Microsoft query returned five records from 68 April events '
                                        "with a by_type breakdown and article IDs. The event dataset's data_through is "
                                        '2026-05-05. Longer extracted source sentences are omitted only from documentation, '
                                        'with paths listed; the API result remains unchanged.',
                            'pitfall': "The example is a historical query, not a current news feed. Read each dataset's "
                                       'data_through and freshness values. Configure both News service URLs and link an '
                                       'authorized News key for normal use; local integration identities never enter the '
                                       'deployed gateway. Search-engine results are not API responses.',
                            'guide': 'company-monitoring-api'},
 'search_funding_news': {'title': 'Funding news API: announcements by investor, sector and round',
                         'purpose': 'Search funding-announcement coverage using a topic or company plus optional investor, '
                                    'sector, round type and reported amount. This retrieves news evidence, not a verified '
                                    'cap table or a transaction settlement ledger.',
                         'workflow': 'Supply q or company, use explicit dates for a historical investigation, and check the '
                                     'returned coverage before interpreting results. For cursor-based searches, send the '
                                     'returned cursor unchanged with the same filters. Overview, trend and sentiment '
                                     'operations use their own analysis models rather than headline pagination.',
                         'fields': {'data when connected': 'funding announcement records, reported amount qualifiers and '
                                                           'source article references when supplied',
                                    'window': 'Effective source dates and data-through information, not an assurance of '
                                              'complete or current coverage.',
                                    'meta.coverage / plan / quota': 'Relayed when the connected News service provides them.',
                                    'error.kind=service_unavailable': 'The gateway has no configured connection for this '
                                                                      'operation.',
                                    'error.kind=access_required': 'A linked News key is missing or the upstream account '
                                                                  'rejects access.'},
                         'observed': 'The captured response was executed through the real gateway and News application '
                                     'against live data, with an isolated test identity and quota dependencies. It verifies '
                                     'data retrieval, not a deployed News URL, production key authentication or customer '
                                     'billing. The April funding query returned five records from 1,085 matching deal '
                                     'records, including company/domain, round, amounts, investors, sector, geography and '
                                     'source article IDs. Of the matched records, 953 contain usable positive amounts and '
                                     '132 do not. Source totals include large unverified outliers and fixed-rate currency '
                                     'conversions; they are not audited funding statistics.',
                         'pitfall': "The example is a historical query, not a current news feed. Read each dataset's "
                                    'data_through and freshness values. Configure both News service URLs and link an '
                                    'authorized News key for normal use; local integration identities never enter the '
                                    'deployed gateway. Search-engine results are not API responses.',
                         'guide': 'funding-news-api'},
 'get_article': {'title': 'Article API: retrieve news text and attribution by article ID',
                 'purpose': 'Retrieve an article whose identifier was returned by an accessible news or company record. Use '
                            'the article as source evidence in a research interface while retaining attribution and '
                            'treating its text as untrusted content, not instructions for an agent.',
                 'workflow': 'Use an article_id actually returned by a prior request; it must contain 24 hexadecimal '
                             "characters. Check the connected News account's access before retrieving text. Store the "
                             'source URL and reporting date separately from your retrieval timestamp.',
                 'fields': {'data when connected': 'article text, source and attribution fields supplied by the connected '
                                                   'News API',
                            'window': 'Effective source dates and data-through information, not an assurance of complete or '
                                      'current coverage.',
                            'meta.coverage / plan / quota': 'Relayed when the connected News service provides them.',
                            'error.kind=service_unavailable': 'The gateway has no configured connection for this operation.',
                            'error.kind=access_required': 'A linked News key is missing or the upstream account rejects '
                                                          'access.'},
                 'observed': 'The captured response was executed through the real gateway and News application against live '
                             'data, with an isolated test identity and quota dependencies. It verifies data retrieval, not '
                             'a deployed News URL, production key authentication or customer billing. This article ID came '
                             'from the successful software earnings search. Retrieval returned HTTP 200 and a '
                             '5,891-character body plus source metadata. Documentation omits the full body, lede and '
                             'description while retaining the headline, source URL, body_chars, attribution and '
                             "classification. charged_exports=1 is the operation's returned export count; this isolated "
                             'capture did not charge a customer.',
                 'pitfall': "The example is a historical query, not a current news feed. Read each dataset's data_through "
                            'and freshness values. Configure both News service URLs and link an authorized News key for '
                            'normal use; local integration identities never enter the deployed gateway. Search-engine '
                            'results are not API responses.',
                 'guide': 'financial-news-api'},
 'get_company_field': {'title': 'Company field API: sectors, founders, technology, apps and LinkedIn data',
                       'purpose': 'Request one named field from a company whose identity you have reviewed. The field '
                                  'selector is required and allowlisted; there is no all-fields option. The database '
                                  'projection selects only that field.',
                       'workflow': 'Resolve the company and select one field. For field=social, read platform links '
                                   'alongside value.linkedin.profile, profile_history and recent_posts. These read '
                                   'underlying LinkedIn observations even when derived social enrichment is absent. '
                                   'Inspect observation dates, per-source coverage and array truncation.',
                       'fields': {'data.field / value': 'Selected field and its source data only.',
                                  'data.status': 'Stored observation status; missing is not zero.',
                                  'data.coverage.arrays': 'Per-array available, returned and truncated counts.',
                                  'data.value.linkedin': 'Social field only: latest observed company followers/headcount, bounded profile history and distinct stored posts.',
                                  'data.value.web_traffic': 'Traffic field only: dated ranks, device splits, engagement, backlinks, source connections, countries and keywords.',
                                  'data.value.customer_reviews': 'Reputation field only: source review profile and bounded distinct review samples, with independent coverage and observation dates.',
                                  'data.value.sector_details / corporate_structure / uniqueness_scalability': 'Respectively classification, lifecycle and assessments details; source identifiers and contacts are removed.',
                                  'data.updated_at': 'Source record update, distinct from gateway retrieval time.'},
                       'observed': 'The technology example preserves all seventy Razorpay stack entries with '
                                   'item_limit=100. Other company fields have separate real JSON captures.',
                       'pitfall': 'A successful HTTP response does not independently establish current accuracy or complete '
                                  'coverage. Contact access checks and source plan limits remain authoritative.',
                       'guide': 'company-data-api'},
 'company_filter_catalog': {'title': 'Company filter catalog API: filters, sort and listing columns',
                            'purpose': 'Discover the supported company search inputs, categorical values, typeahead '
                                       'availability, sort choices, pagination bounds and result-column names.',
                            'workflow': 'Inspect the request schema and returned coverage; use the related discovery '
                                        'response before selecting an identifier or field. Preserve access errors and '
                                        'unknown values in your application.',
                            'fields': {'data.filters': 'Public field names, validation schemas and known options.',
                                       'data.sort_options': 'Allowed descending sort choices; relevance uses source '
                                                            'ranking.',
                                       'data.columns': 'Allowlisted on-demand display columns.',
                                       'data.page': 'Zero-based pagination bounds.'},
                            'observed': 'This response is generated from the validated gateway contract and reviewed Radar '
                                        'sidebar vocabulary. It does not query or count every company.',
                            'pitfall': 'A successful HTTP response does not independently establish current accuracy or '
                                       'complete coverage. Contact access checks and source plan limits remain '
                                       'authoritative.',
                            'guide': 'company-search-api'},
 'company_filter_options': {'title': 'Company filter options API: vocabulary and typeahead',
                            'purpose': 'Find bounded suggestions for a company filter. Business models use Radar '
                                       'vertical_suggest; companies, markets, technologies, products, skills and locations '
                                       'use their corresponding typeahead handlers.',
                            'workflow': 'Inspect the request schema and returned coverage; use the related discovery '
                                        'response before selecting an identifier or field. Preserve access errors and '
                                        'unknown values in your application.',
                            'fields': {'data.field / query': 'The requested public filter name and typed text.',
                                       'data.options': 'Accepted suggestion values or source selection records.',
                                       'data.complete': 'False: bounded suggestions are not the complete vocabulary.'},
                            'observed': 'The live business-model query for software returned five suggestions from the '
                                        'current Radar handler.',
                            'pitfall': 'A successful HTTP response does not independently establish current accuracy or '
                                       'complete coverage. Contact access checks and source plan limits remain '
                                       'authoritative.',
                            'guide': 'company-search-api'},
 'get_company_columns': {'title': 'Company listing columns API: selected company data points',
                         'purpose': 'Select up to fourteen listing columns for up to twenty visible company domains. This '
                                    'matches Radar’s Show columns workflow: search cards first, chosen data points in a '
                                    'separate request.',
                         'workflow': 'Inspect the request schema and returned coverage; use the related discovery response '
                                     'before selecting an identifier or field. Preserve access errors and unknown values in '
                                     'your application.',
                         'fields': {'data.companies[].columns': 'Only requested column names; source display label/value '
                                                                'pairs or null.',
                                    'data.companies[].status': 'available if the source supplied columns; otherwise '
                                                               'unknown.',
                                    'data.note': 'Display values are rounded and may suppress zero/negative values; use '
                                                 'financials for precise evidence.'},
                         'observed': 'The live Razorpay/Stripe request returned the selected employee, funding, revenue, '
                                     'web-presence and app-download display columns, with missing values retained as null.',
                         'pitfall': 'A successful HTTP response does not independently establish current accuracy or '
                                    'complete coverage. Contact access checks and source plan limits remain authoritative.',
                         'guide': 'company-search-api'},
 'people_filter_options': {'title': 'People filter options API: schools, skills and sectors',
                           'purpose': 'Find canonical professional search values using Radar’s people suggestion handler.',
                           'workflow': 'Inspect the request schema and returned coverage; use the related discovery '
                                       'response before selecting an identifier or field. Preserve access errors and '
                                       'unknown values in your application.',
                           'fields': {'data.field / options': 'Chosen school, skill or sector vocabulary and matching '
                                                              'suggestions.',
                                      'data.returned / complete': 'Bounded suggestion count; not total records or complete '
                                                                  'vocabulary.'},
                           'observed': 'The live machine-learning skill query returns source suggestions rather than '
                                       'guessed company-sector labels.',
                           'pitfall': 'A successful HTTP response does not independently establish current accuracy or '
                                      'complete coverage. Contact access checks and source plan limits remain '
                                      'authoritative.',
                           'guide': 'b2b-data-api'},
 'get_company_contacts': {'title': 'Company contact API: request business emails or phone numbers',
                          'purpose': 'Retrieve only explicitly requested emails and/or phone numbers for one company. An '
                                     'explicit contacts key scope and an entitled linked Radar account are required; a '
                                     'wildcard key alone does not grant contact access.',
                          'workflow': 'Resolve the company domain, then select emails, phones or both explicitly. '
                                      'For LinkedIn and other company social references, use get_company_field with '
                                      'field=social. For individual professional contacts, discover and accept a '
                                      'professional ID before using get_person_contacts.',
                          'fields': {'data.domain': 'Requested company domain.',
                                     'data.emails / phones': 'Only the requested contact types, each bounded to twenty-five '
                                                             'source values.',
                                     'data.contact_source': 'company_domain: business contacts, not an inferred '
                                                            'person-specific address.',
                                     'data.available': 'At least one requested contact type was supplied.'},
                          'observed': 'The default preview key is deliberately denied with scope_required. This is an '
                                      'access-control capture, not a service outage. Successful response-shape tests use '
                                      'synthetic example.com contacts; no production paid-contact retrieval is claimed.',
                          'pitfall': 'Company association does not identify the mailbox owner, department, work-email '
                                     'verification or phone line type. Successful empty lookups cost one API credit in '
                                     'account mode; source errors can sometimes appear as empty arrays. There is no '
                                     'contact-array pagination or source-total count.',
                          'guide': 'company-email-phone-api'},
 'get_person_contacts': {'title': 'Professional contact API: email and phone lookup by person ID',
                         'purpose': 'Use the person ID returned by search_people to request only emails and/or phones. The '
                                    'source prefers person-level records and can fall back to the current company’s '
                                    'business contacts. Explicit contacts scope and paid Radar access apply.',
                         'workflow': 'Read company founder names, then compare a professional candidate by name, exact '
                                     'recorded company domain and LinkedIn reference. Use only the accepted person ID. '
                                     'Professional founder-role tags can disagree with company founder records; preserve '
                                     'ambiguous or missing joins. Request emails and/or phones separately from discovery.',
                         'fields': {'data.person_id': 'ID returned by professional search; do not use a company public ID.',
                                    'data.emails / phones': 'Requested contact types only.',
                                    'data.contact_source': 'person, company_domain, none or unknown; company fallback is '
                                                           'never relabeled as personal.',
                                    'data.available': 'Whether a requested value was supplied; not deliverability '
                                                      'verification.'},
                         'observed': 'The default preview key returns scope_required before contacting the source. '
                                     'Synthetic tests cover paid source responses, requested-field filtering and '
                                     'company-domain fallback. No live private contact values are published in these '
                                     'examples.',
                         'pitfall': 'Company fallback happens only when both person email and phone are absent. A '
                                    'person phone can prevent fallback on an empty email-only request. The person origin '
                                    'label is not a verified-work-email classification; no server-side fallback toggle, '
                                    'email-type filter or deliverability check is exposed.',
                         'guide': 'founder-contact-data-api'}}


ACCOUNT_NOTES = {
"health": ("Health endpoint: process liveness", "Checks that this gateway process responds. It does not test Radar, News, identity, billing, database coverage or permission to retrieve a particular company.", "Read ok and version. Treat visibility as a package label; GitHub privacy and proxy exposure must be verified separately."),
"capabilities": ("Capability discovery: tools, routes and input schemas", "Lists the shared data-operation registry. Use it to discover the exact tool name, REST route and accepted input model instead of building arbitrary upstream calls.", "connection_configured means configuration is present for the caller, not that the service is healthy or that every query is entitled. The response shows all 53 tools, omitting only their lengthy embedded input schemas; the complete schemas remain in OpenAPI."),
"openapi": ("OpenAPI schema endpoint: REST and account contracts", "Returns the machine-readable contract for the active gateway mode. Account mode includes session-authenticated management routes alongside key-authenticated data routes.", "Use the served schema from your deployment. The excerpt omits most schemas and paths; use the complete downloadable account-openapi.json for code generation. Account routes are absent when account mode is disabled."),
"account_session": ("Reconnect a Radar account session", "Verifies the supplied Radar session and replaces the encrypted session link for the same account. This reconnects existing keys after a session expires without giving them a new usage allowance.", "connected=true acknowledges validation and storage. This endpoint does not log in a password, create a Radar account or extend the upstream session's validity."),
"account_plans": ("Read Radar plans and API credit policy", "Returns the catalog snapshot, configured per-credit rate, prepaid policy and checkout availability. Use this to explain pricing before asking a user to create a paid order.", "The sample uses a synthetic ten-paise test rate so the checkout path can be exercised. The real default rate remains unset and checkout disabled. Catalog subscription prices and API credit budgets have separate meanings."),
"account_create_key": ("Create an API key: scopes, expiry and one-time reveal", "Creates a random key owned by the verified account and returns it once. Set a recognizable application name, the smallest necessary data scopes and an explicit expiry. The server stores its hash rather than the plaintext key.", "Copy api_key into a secret store immediately; it is redacted in the published capture. The public id is used for later revocation. New keys share the account's existing rate limits and credit budget."),
"account_list_keys": ("List API keys: names, expiry and revocation state", "Lists the verified account's key metadata so users can manage integrations. It includes identifiers and last-four characters but never re-reveals the key or exposes a stored hash.", "created and expires are Unix seconds; revoked is the persisted integer flag. scopes is currently a JSON-encoded string in this response, so parse it explicitly if your interface needs an array. That wire shape is preserved in the real local capture."),
"account_link_news": ("Link a News API key to the Radar account", "Stores an encrypted connection credential for the separately operated News service. It does not create a News subscription, activate an upstream server or change the News account's quota.", "linked=true is a storage acknowledgment, not a live validation of the credential. A later news request can still fail because its service is unavailable or its key is not entitled. The demonstration key is an explicit placeholder."),
"account_follow": ("Follow a company in the API watchlist", "Adds a normalized company domain to the account's API watchlist. Repeating the same follow is idempotent. Capacity follows the effective Radar plan and prepaid credits do not expand it.", "following=true records the API watchlist state. It does not send alerts, schedule paid polling or synchronize the production Radar dashboard watchlist."),
"account_list_following": ("List followed companies and the plan limit", "Reads the account's API watchlist, its current count and effective capacity. This is suitable for a console list or an application-controlled monitoring workflow.", "The sample contains the company added by the preceding follow request. created is Unix seconds. If a downgrade leaves the count above the new limit, existing entries remain readable and removable."),
"account_spending": ("Set a monthly prepaid credit spending limit", "Sets the maximum prepaid credits the account may spend in a UTC calendar month. The default zero disables prepaid consumption even when a wallet has credits. Included Business credits are used before prepaid funds.", "monthly_prepaid_limit is credits, not rupees. Changing the limit does not charge money, buy credits or reset already-used monthly credit totals. In-flight reservations are already included in usage."),
"account_topup": ("Create a prepaid API credit checkout order", "Creates a Razorpay order for a server-calculated INR amount. The user must complete provider Checkout, and the gateway must receive a verified captured-payment event, before the wallet receives credits.", "The synthetic example requests 100 credits at ten paise each, producing amount=1000 paise (₹10). This is an execution fixture, not the public tariff. The response is awaiting_captured_payment and does not itself grant balance."),
"billing_webhook": ("Payment webhook: verify captured payments and credit once", "Receives provider payment events with an HMAC signature over the original raw request body. A matching captured payment credits its stored order once; duplicate delivery cannot create an additional grant.", "The example was generated using a synthetic provider event and the real local signature verifier. The secret and signature are redacted. Browser checkout success is not accepted as proof of payment. Refund/dispute events freeze the affected account for reconciliation."),
"account_usage": ("Read API usage, prepaid balance and monthly limits", "Returns account-wide included usage, prepaid usage, balance, spending cap and charged feature summaries. REST and MCP calls using any account key share these values.", "The sample follows a synthetic captured top-up, so wallet_credits=100 while data usage remains zero. Used-or-reserved values include pending requests. A UTC month and configured plan are shown alongside the balance."),
"account_unfollow": ("Remove a company from the API watchlist", "Removes the named domain from the verified account's API watchlist. It is safe to repeat and remains available after a downgrade so users can reduce their list.", "following=false acknowledges removal for this account. It does not delete company data, cancel an unrelated integration or alter another account's watchlist."),
"account_revoke_key": ("Revoke an API key owned by the current account", "Revokes an account-owned key by its public identifier. Subsequent authentication with that key fails, while already admitted requests may finish. Rotation should update the application before revoking its old key.", "The endpoint returns revoked=true idempotently, including when no matching account-owned record exists. That acknowledgment does not reveal whether another user's key exists. API credits and historical usage remain attached to the account."),
}

NOTES.update(EXPANDED_NOTES)

NOTES.update(RESEARCH_NOTES)
