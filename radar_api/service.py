from __future__ import annotations

import asyncio
from contextvars import ContextVar
from dataclasses import dataclass

from . import models as m
from .auth import principal, RateLimiter
from .errors import RadarError, envelope
from .public import clean, company_card, financial_data, news_content
from .profiles import ProfileStore
from .investors import InvestorStore
from .apps import AppsStore
from .research import financial_catalog, screen as financial_screen, team as company_team
from .internships import InternshipStore
from .opportunities import PRESETS, catalog as opportunity_catalog
from .catalog import FILTERS, SORTS, SUGGESTIONS, OPTIONS, catalog
from .company_views import compact_card, brief_section, contacts_payload
from .upstream import Upstream

METERING: ContextVar[bool] = ContextVar("radar_metering", default=False)


@dataclass(frozen=True)
class Feature:
    name: str
    path: str
    model: type[m.Input]
    description: str
    source: str = "radar"


# This registry generates REST routes, MCP tools, schemas and the capability catalog.
FEATURES = [
    Feature("search_companies", "companies/search", m.SearchCompanies, "Filter companies by industry, market, location, size, stage, technology, funding and financial bands."),
    Feature("semantic_company_search", "companies/semantic-search", m.SemanticSearch, "Find companies using a natural-language description plus optional filters."),
    Feature("get_company", "companies/profile", m.CompanyProfile, "Read compact company identity and available fields. Retrieve field data separately with get_company_field."),
    Feature("get_company_field", "companies/field", m.CompanyField, "Retrieve one explicitly selected company field, such as classification, people, technology, traffic or apps, with coverage and bounded arrays."),
    Feature("company_apps", "companies/apps", m.CompanyApps, "List individual Play Store apps whose normalized developer website exactly matches the company domain."),
    Feature("opportunity_presets", "companies/opportunities/presets", m.Empty, "Discover explainable growth, hiring, financial and technology prospecting screens and their limits."),
    Feature("search_opportunities", "companies/opportunities/search", m.OpportunitySearch, "Find companies using an explicit opportunity preset plus additional filters; return measured display evidence and source restrictions."),
    Feature("company_filter_catalog", "companies/filters", m.Empty, "Discover company filters, accepted values, sort options, pagination and selectable result columns."),
    Feature("company_filter_options", "companies/filter-options", m.CompanyFilterOptions, "Look up matching company filter values using Radar's sidebar vocabulary and typeahead services."),
    Feature("get_company_columns", "companies/columns", m.CompanyColumns, "Fetch only selected display columns for up to twenty company domains. Formatted values are not financial statements."),
    Feature("get_company_intelligence", "companies/intelligence", m.Company, "Read company scores, peer comparisons, earnings and risk narratives. Scores are derived assessments, not financial facts."),
    Feature("financial_filter_catalog", "companies/financials/filters", m.Empty, "Discover precise USD screening, source financial band boundaries, fiscal-period semantics and limits."),
    Feature("screen_company_financials", "companies/financials/screen", m.FinancialScreen, "Screen a bounded candidate page or explicit domains against exact dated USD financial constraints; retain unknowns, source gates and evidence."),
    Feature("get_company_team", "companies/team", m.CompanyTeam, "Retrieve recorded company founders, key people or exactly affiliated professional cards with separate group requests and bounded pagination."),
    Feature("get_financials", "companies/financials", m.Financials, "Retrieve income, balance-sheet and cash-flow metrics by fiscal period; distinguish filings from news reports and preserve currency and access limits."),
    Feature("get_company_events", "companies/events", m.CompanyEvents, "Read a company's event timeline, momentum, risks and the effective account-limited date window."),
    Feature("get_company_funding", "companies/funding", m.Company, "Read reported funding rounds and investors; retain approximate-amount flags."),
    Feature("get_company_enrichment", "companies/enrichment", m.Company, "Read legal identity, hiring, reputation, digital presence, innovation and social activity when available."),
    Feature("find_competitors", "companies/competitors", m.Competitors, "Find competitors in a named market, grouped by funding stage."),
    Feature("company_brief", "companies/brief", m.Brief, "Return compact summaries of profile, financials, intelligence, events, funding, enrichment and news with separate detail requests and explicit coverage."),
    Feature("compare_companies", "companies/compare", m.Compare, "Compare two to five companies with separately labelled fiscal periods and partial-coverage flags."),
    Feature("search_investors", "investors/search", m.SearchCompanies, "Find investors by headquarters and portfolio industries or markets."),
    Feature("investor_directory", "investors/directory", m.Empty, "List published investor pages, sectors and cities."),
    Feature("get_investor_page", "investors/page", m.InvestorPage, "Read investor identity, measured portfolio metrics, dated coverage and available detail fields by published slug."),
    Feature("get_investor_field", "investors/field", m.InvestorField, "Retrieve one investor field: paginated portfolio or shortlist, sector/stage analysis, follow-on cohorts, co-investors or sourced news."),
    Feature("market_pulse", "markets/pulse", m.Pulse, "Read recent funding, trending markets, sectors and investors for a bounded window."),
    Feature("location_intelligence", "locations/intelligence", m.Location, "Retrieve Radar's existing business intelligence for a named location."),
    Feature("discover_industries", "industries/discover", m.Lookup, "Find up to five matching industry or market names using a specific query."),
    Feature("search_jobs", "jobs/search", m.JobSearch, "Find job listings by company, skills, role, geography and freshness."),
    Feature("job_filter_catalog", "jobs/filters", m.Empty, "Discover job filters, source values, sorting and source matching semantics."),
    Feature("job_filter_options", "jobs/filter-options", m.JobOptions, "Suggest observed job titles, skills, employer names or locations."),
    Feature("search_internships", "jobs/internships/search", m.InternshipSearch, "Search dedicated internship records by employer, title, location, skills, stipend and posted dates; preserve vacancy-status uncertainty."),
    Feature("companies_offering_internships", "jobs/internships/companies", m.InternshipSearch, "Group matching observed internship listings by exact employer name, with counts, titles and detail IDs."),
    Feature("get_internship", "jobs/internships/detail", m.InternshipDetail, "Retrieve a source internship with description, stipend, skills, dates, application URL and validity qualifications."),
    Feature("companies_hiring", "jobs/companies", m.JobSearch, "Find hiring companies for the same job filters."),
    Feature("get_job", "jobs/detail", m.JobDetail, "Retrieve a job listing by an ID returned by search_jobs."),
    Feature("salary_benchmark", "jobs/salary-benchmark", m.Salary, "Read salary statistics for a role, geography and optional currency; retain sample size and coverage."),
    Feature("search_apps", "apps/search", m.AppSearch, "Search individual Android apps by name, developer, exact website host, category, installs, ratings and price model."),
    Feature("get_app", "apps/profile", m.App, "Read compact app identity, observed installs and rating, detail availability and history count."),
    Feature("get_app_field", "apps/field", m.AppField, "Retrieve one app field: listing, ratings, monetization, release, developer, growth or paginated install history."),
    Feature("app_filter_options", "apps/filter-options", m.AppOptions, "List matching observed Play Store categories for app discovery."),
    Feature("search_people", "people/search", m.People, "Find professional profiles by name, role, company, schools, skills, seniority and location; contact values require a separate request."),
    Feature("people_filter_options", "people/filter-options", m.PeopleOptions, "Look up canonical schools, skills and sectors accepted by people search."),
    Feature("get_company_contacts", "contacts/company", m.CompanyContacts, "Request company emails and/or phones separately; requires explicit contacts scope and a paid linked Radar account."),
    Feature("get_person_contacts", "contacts/person", m.PersonContacts, "Request one person's emails and/or phones; preserve whether the source is the person or a company-domain fallback. Requires contacts scope and paid Radar access."),
    Feature("search_news", "news/search", m.News, "Search associated news; a company filter uses business-news coverage. Headlines default to 100 per page.", "news"),
    Feature("search_business_news", "news/business", m.News, "Search business headlines for a topic or company with date, sentiment and priority filters.", "business_news"),
    Feature("news_overview", "news/overview", m.NewsQuery, "Read measured coverage, headline examples and topic context in a bounded date window.", "news"),
    Feature("news_trends", "news/trends", m.NewsAnalysis, "Measure daily, weekly or monthly news volume while preserving the available date window.", "news"),
    Feature("news_sentiment", "news/sentiment", m.NewsAnalysis, "Read the distribution and timeline of news sentiment.", "news"),
    Feature("search_business_events", "news/events", m.News, "Read structured business events associated with a topic or company and their article references.", "business_news"),
    Feature("search_funding_news", "news/funding", m.FundingNews, "Find funding coverage by company, topic, investor, sector, round and reported USD amount.", "business_news"),
    Feature("get_article", "news/article", m.Article, "Retrieve the full article and attribution for an article ID returned by news or company events.", "news"),
]
BY_NAME = {f.name: f for f in FEATURES}

def filters(value: m.CompanyFilters):
    out = {FILTERS[k]: v for k, v in value.model_dump().items() if k in FILTERS and v and v != "all"}
    if out.get("revenue_band") == ["under1m"]:
        out["revenue_band"] = ["<1m"]
    if value.founded_year_from or value.founded_year_to:
        out["founded_year"] = [value.founded_year_from or "", value.founded_year_to or ""]
    if value.radius_km:
        out.update(custom_range=value.radius_km * 1000, radius_explicit=True)
    return out


class Service:
    def __init__(self, upstream: Upstream, accounts=None):
        self.upstream = upstream
        self.accounts = accounts
        self.profiles = ProfileStore(upstream.settings) if upstream.settings.profile_mongo_uri else None
        self.investors = InvestorStore(upstream.settings) if upstream.settings.investor_data_dir else None
        self.apps = AppsStore(upstream.settings, upstream.transport) if upstream.settings.apps_ch_url else None
        self.internships = InternshipStore(upstream.settings) if upstream.settings.jobs_mongo_uri else None
        self.contact_limiter = RateLimiter()

    def catalog(self):
        user = principal()
        return [{"name": f.name, "method": "POST", "path": "/v1/" + f.path,
                 "description": f.description, "read_only": True,
                 **({"detailed_profile_configured": self.profiles is not None} if f.name in {"get_company", "get_company_field"} else {}),
                 **({"detailed_investor_configured": self.investors is not None} if f.name in {"get_investor_page", "get_investor_field"} else {}),
                 "requires_explicit_scope": "contacts" if f.path.startswith("contacts/") else None,
                 "connection_configured": (self.apps is not None) if f.path.startswith("apps/") or f.name == "company_apps" else (self.internships is not None) if f.path.startswith("jobs/internships/") else (self.investors is not None and bool(self.upstream.settings.radar_url)) if f.name == "get_investor_field" else (self.profiles is not None) if f.name == "get_company_field" else bool(self.upstream.settings.radar_url) if f.source == "radar" else bool(
                     user.news_key and (self.upstream.settings.news_url if f.source == "news" else self.upstream.settings.business_news_url)),
                 "input_schema": f.model.model_json_schema()} for f in FEATURES]

    async def run(self, name: str, request: m.Input):
        user = principal()
        if "*" not in user.scopes and BY_NAME[name].path.split("/")[0] not in user.scopes:
            raise RadarError("scope_required", "This key does not permit this data group", 403)
        if name == "company_brief" and request.include_news and "*" not in user.scopes and "news" not in user.scopes:
            raise RadarError("scope_required", "A brief with news requires the news scope", 403)
        if name == "get_company_team" and request.group == "professionals" and "*" not in user.scopes and "people" not in user.scopes:
            raise RadarError("scope_required", "Professional team lookup also requires the people scope", 403)
        if name in {"get_company_contacts", "get_person_contacts"}:
            # Explicit permission, including for keys with wildcard data access.
            # Apply before upstream calls and before reserving billable credits.
            if "contacts" not in user.scopes:
                raise RadarError("scope_required", "Create a key with the explicit contacts scope for contact retrieval", 403)
            if not user.radar_token:
                raise RadarError("access_required", "Link an entitled Radar account before requesting contacts", 403)
            if self.accounts:
                self.accounts.rate("contacts:" + user.account_id, 10, 60)
            else:
                from dataclasses import replace
                self.contact_limiter.check(replace(user, rate_per_minute=10))
        if not self.accounts or METERING.get():
            return await self._run(name, request)
        units = 6 + int(request.include_news) if name == "company_brief" else (
            3 * len(request.domains) if name == "compare_companies" else (
                1 + (len(request.domains) or request.candidate_limit) if name == "screen_company_financials" else 1))
        request_id = self.accounts.reserve(user, name, BY_NAME[name].path.split("/")[0], units)
        marker = METERING.set(True)
        actual = 0
        try:
            async with asyncio.timeout(120):
                result = await self._run(name, request)
            if name == "company_brief":
                actual = sum("result" in s for s in result["data"]["sections"].values())
            elif name == "compare_companies":
                actual = sum("result" in s for c in result["data"]["companies"] for s in c.get("sections", {}).values())
            elif name == "screen_company_financials":
                actual = 1 + result["data"]["successful_financial_reads"]
            else:
                actual = 1
            result["meta"]["billing"] = {"request_id": request_id, "credits": actual}
            return result
        except TimeoutError:
            raise RadarError("upstream_timeout", "The request exceeded its processing limit", 504) from None
        finally:
            METERING.reset(marker)
            self.accounts.settle(request_id, actual)

    async def _run(self, name: str, request: m.Input):
        principal()
        notes = []
        if name in {"company_brief", "compare_companies"}:
            data = await (self.brief(request) if name == "company_brief" else self.compare(request))
            return envelope(name, data, partial=data["partial"], notes=[
                "Each section retains its own date window and access limits. Missing data is not zero."])
        data = await self.dispatch(name, request)
        window = {"data_through": None}
        if BY_NAME[name].source != "radar":
            window = clean(data.get("window", window))
            notes = clean(data.get("meta", {}).get("notes", []))
            public_data = news_content(data.get("data", {}))
        else:
            # The native profile reader already emits its public field contract.
            # Legacy key translation would rename its feeds block to markets.
            public_data = data if name in {"get_company", "get_company_field", "get_company_contacts", "get_person_contacts", "company_filter_catalog"} else clean(data)
            if isinstance(data, dict):
                freshness = data.get("_data_freshness", {})
                window["data_through"] = freshness.get("latest_event_date")
                if "window_days" in data:
                    window["effective_days"] = data["window_days"]
                    window["requested_days"] = request.days
                if name == "get_financials":
                    window["data_through"] = max((r["reported_date"] for r in data["periods"] if r.get("reported_date")), default=None)
                    notes = ["Metrics retain their own source type. Filing URLs and exact period ends are absent when Radar does not supply them.",
                             "EPS currency is unspecified unless supplied by the source. Native values are not summed across currencies."]
                    if data.get("access_limited"):
                        notes.append("The linked Radar account exposes only part of the financial archive.")
                if name in {"search_companies", "search_investors", "semantic_company_search"}:
                    notes.append("Filters and result counts remain subject to the linked Radar account's limits.")
                if name == "get_company_intelligence":
                    notes.append("Scores and narratives are derived assessments. Financial metrics are retrieved evidence.")
                if name == "get_company_enrichment":
                    notes.append("Absent enrichment sections have unknown coverage; the source does not distinguish missing data from a failed section.")
                if name in {"get_investor_page", "get_investor_field"}:
                    window["data_through"] = data.get("coverage", {}).get("data_through")
                    if data.get("profile_depth") == "metadata":
                        notes.append("Investor detail storage is not connected; publication metadata is not a complete investor profile.")
                    else:
                        notes.append("Investor metrics use the dated, verified Atlas snapshot. Retrieval time is not data freshness. Use available_fields for separate detail requests.")
                if name in {"get_company", "get_company_field"}:
                    notes.append("Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field.")
                    if data.get("profile_depth") == "card":
                        notes.append("Detailed profile storage is not connected; this response contains only the upstream company card.")
                    elif data.get("coverage", {}).get("partial"):
                        notes.append("Some field arrays were limited or an enrichment lookup failed; inspect field_status and coverage.")
        timeout_partial = isinstance(data, dict) and bool(data.get("_partial_timeout") or data.get("partial_timeout"))
        partial = timeout_partial or isinstance(data, dict) and bool(data.get("coverage", {}).get("partial"))
        if timeout_partial:
            notes.append("The source timed out on part of this query; returned counts may be incomplete.")
        result = envelope(name, public_data, window=window, notes=notes, partial=partial)
        if BY_NAME[name].source != "radar":
            for key in ("coverage", "plan", "quota"):
                if key in data.get("meta", {}):
                    result["meta"][key] = clean(data["meta"][key])
            coverage = result["meta"].get("coverage") or {}
            result["meta"]["partial"] = bool(data.get("meta", {}).get("partial") or coverage.get("available") is False)
        return result

    async def radar(self, path, body=None):
        return await self.upstream.call("radar", path, body=body)

    async def dispatch(self, name, r):
        if name == "financial_filter_catalog":
            return financial_catalog()
        if name == "screen_company_financials":
            return await financial_screen(self, r)
        if name == "get_company_team":
            return await company_team(self, r)
        if BY_NAME[name].path.startswith("apps/") or name == "company_apps":
            if not self.apps:
                raise RadarError("service_unavailable", "Individual app storage is not connected", 503)
            return await self.apps.get(name, r)
        if BY_NAME[name].path.startswith("jobs/internships/"):
            if not self.internships:
                raise RadarError("service_unavailable", "Dedicated internship storage is not connected", 503)
            return await self.internships.get(name, r)
        if name == "opportunity_presets":
            return opportunity_catalog()
        if name == "search_opportunities":
            preset = PRESETS[r.preset]
            extra = r.filters.model_dump(exclude_unset=True)
            merged = {**preset["filters"]}
            for key, value in extra.items():
                base = merged.get(key)
                if isinstance(base, dict) and isinstance(value, dict):
                    if any(k in base and base[k] != v for k, v in value.items()):
                        raise RadarError("invalid_request", "Additional filters cannot replace this preset's defining criteria", 422)
                    merged[key] = {**base, **value}
                elif key in merged and value != base:
                    raise RadarError("invalid_request", "Additional filters cannot replace this preset's defining criteria", 422)
                else:
                    merged[key] = value
            query = m.SearchCompanies(filters=merged, page=r.page, limit=r.limit, match_mode=r.match_mode,
                                      sort_by=r.sort_by if "sort_by" in r.model_fields_set else preset["sort_by"])
            data = await self.dispatch("search_companies", query)
            domains = list(dict.fromkeys(row["domain"] for row in data.get("companies", []) if row.get("domain")))
            evidence, partial = [], False
            if domains:
                try:
                    evidence = (await self.dispatch("get_company_columns", m.CompanyColumns(domains=domains, columns=preset["evidence_columns"])))['companies']
                except RadarError:
                    partial = True
            return {**data, "preset": r.preset, "effective_filters": query.filters.model_dump(include=query.filters.model_fields_set),
                    "sort_by": query.sort_by, "evidence": evidence, "interpretation": preset["interpretation"],
                    "coverage": {"partial": partial or bool(data.get("partial_timeout")), "evidence_available": bool(evidence)},
                    "note": "These are source-filtered candidates, not verified opportunities. Inspect access/restricted_filters and matching metadata; display columns may suppress zero or negative values. Retrieve exact financials and detail fields separately."}
        if name in {"search_companies", "search_investors"}:
            fd = filters(r.filters)
            if SORTS[r.sort_by]:
                fd["sort_by"] = [SORTS[r.sort_by]]
            if name == "search_investors":
                fd["entity_type"] = "investor"
            data = await self.radar("/company_search/", {"key": "find_companies", "final_data": {
                **fd, "current_page": r.page, "results_per_page": r.limit}})
            return self.company_results(data, r)
        if name == "semantic_company_search":
            data = await self.radar("/semantic_search/", {"q": r.q, "page": r.page,
                                    "page_size": r.limit, "extra_filters": filters(r.filters)})
            return self.company_results(data, r)
        if name == "get_company":
            if self.profiles:
                return await self.profiles.get(r)
            data = await self.radar("/company_search/shortlist_hydrate", {"websites": [r.domain]})
            rows = data.get("companies") or []
            if not rows or rows[0].get("_no_data"):
                raise RadarError("no_data", "No company profile is available for this domain", 404)
            return {"company": compact_card(rows[0]), "access": clean(data.get("_entitlements")),
                    "extras_gated": data.get("_extras_gated", False), "profile_depth": "card",
                    "available_fields": [], "field_status": {name: "unavailable" for name in m.PROFILE_SECTIONS},
                    "detailed_profile_available": False}
        if name == "get_company_field":
            if not self.profiles:
                raise RadarError("service_unavailable", "Company field storage is not connected", 503)
            return await self.profiles.get(r)
        if name == "company_filter_catalog":
            return catalog()
        if name == "company_filter_options":
            if r.field not in m.CompanyFilters.model_fields:
                raise RadarError("invalid_request", "Unknown company filter; inspect company_filter_catalog", 422)
            if r.field in SUGGESTIONS:
                data = await self.radar("/company_search/", {"key": SUGGESTIONS[r.field], "value": r.q})
                rows = data.get("results", [])
            elif r.field == "business_models":
                data = await self.radar("/company_search/vertical_suggest", {"value": r.q, "limit": r.limit})
                rows = [row["value"] for row in data.get("verticals", []) if isinstance(row, dict) and isinstance(row.get("value"), str)]
            elif r.field == "industries":
                rows = [v for v in OPTIONS["industries"] if r.q.casefold() in v.casefold()]
            else:
                spec = m.CompanyFilters.model_json_schema()["properties"][r.field]
                values = OPTIONS.get(r.field, spec.get("enum", spec.get("items", {}).get("enum", [])))
                if not values:
                    raise RadarError("invalid_request", "This filter accepts typed input but has no option lookup; inspect company_filter_catalog", 422)
                rows = [v for v in values if r.q.lower() in str(v).lower()]
            return {"field": r.field, "query": r.q, "options": clean(rows[:r.limit]), "returned": min(len(rows), r.limit),
                    "complete": False, "note": "Suggestions are bounded matches, not the complete company universe."}
        if name == "get_company_columns":
            domains, columns = list(dict.fromkeys(r.domains)), list(dict.fromkeys(r.columns))
            data = await self.radar("/company_search/cols", {"final_data": {"websites": domains, "columns": columns}})
            return {"companies": [{"domain": domain, "columns": {key: clean(data.get(domain, {}).get(key)) for key in columns},
                "status": "available" if data.get(domain) else "unknown"} for domain in domains],
                "note": "Radar display values only. Missing values may be suppressed zero/negative values or source failure; use get_financials for precise values and provenance."}
        if name in {"get_company_contacts", "get_person_contacts"}:
            body = {"website": r.domain} if name == "get_company_contacts" else {"id": r.person_id}
            path = "/company_search/contact" if name == "get_company_contacts" else "/people_search/contact"
            data = await self.radar(path, body)
            if data.get("gated"):
                raise RadarError("access_required", "The linked Radar plan does not permit contact retrieval", 403)
            return contacts_payload(name, r, data)
        if name == "people_filter_options":
            data = await self.radar("/people_search/suggest", {"field": r.field, "value": r.q})
            rows = data.get("results", [])
            return {"field": r.field, "query": r.q, "options": rows[:r.limit], "returned": min(len(rows), r.limit), "complete": False}
        if name == "get_company_intelligence":
            data = await self.radar("/company_intel/", {"domain": r.domain})
            return {k: data[k] for k in ("domain", "intel", "computed_at") if k in data}
        if name == "get_financials":
            data = await self.radar("/company_intel/", {"domain": r.domain})
            return financial_data(data, r)
        if name == "get_company_events":
            return await self.radar("/company_events/", r.model_dump())
        if name == "get_company_funding":
            return await self.radar("/funding/", {"key": "investment_summary", "final_data": {"domain": r.domain}})
        if name == "get_company_enrichment":
            return await self.radar("/company_enrichment/", {"domain": r.domain})
        if name == "find_competitors":
            stages = ["Seed", "Series A", "Series B", "Series C", "Public"]
            data = await self.radar("/competitive/", {"key": "segment_summary", "final_data": {
                "feed": r.market, "feedbm": r.business_model or "", "max_limits": r.per_stage,
                "companies": {"elements": stages, "vpaths": [[s.lower()] for s in stages]}}})
            return {"market": r.market, "summary": clean(data.get("summary", {})), "companies": {
                stage: [company_card(c) for c in rows[:r.per_stage]] for stage, rows in data.get("companies", {}).items()}}
        if name == "investor_directory":
            data = await self.radar("/investors/index")
            for key in ("top_lists", "top_angel_lists", "top_profiles"):
                data[key] = [{"slug": row.get("_id"), **{k: v for k, v in row.items() if k != "_id"}}
                             for row in data.get(key, [])]
            for key in ("cities", "sectors"):
                data[key] = [{"name": row.get("_id"), **{k: v for k, v in row.items() if k != "_id"}}
                             for row in data.get(key, [])]
            return data
        if name in {"get_investor_page", "get_investor_field"}:
            if self.investors:
                gate = await self.radar("/investors/publication/" + r.slug)
                return await self.investors.get(r, gate)
            if name == "get_investor_field":
                raise RadarError("service_unavailable", "Verified investor detail storage is not connected", 503)
            data = await self.radar("/investors/page/" + r.slug)
            metadata = {key: data[key] for key in ("slug", "kind", "family", "h1", "name", "edition") if key in data}
            return {**metadata, "profile_depth": "metadata", "available_fields": [],
                    "coverage": {"partial": True, "detail_available": False},
                    "note": "This is publication metadata only. Connect verified investor detail storage for portfolio and analysis."}
        if name == "market_pulse":
            return await self.radar("/analytical_q_radar/homepage_pulse", {"days": r.days,
                **{k + "_limit": r.limit for k in ("funding", "feed", "sector", "industry", "investor")}})
        if name == "location_intelligence":
            body = r.model_dump()
            # The public geographic level is city; the legacy source calls it location.
            # Passing city unchanged leaves its geographic predicate empty.
            if body["location_type"] == "city":
                body["location_type"] = "location"
            return await self.radar("/analytical_loc/", {"key": "analytical_loc", "final_data": body})
        if name == "discover_industries":
            data = await self.radar("/metas/", {"key": "search_metas_deep", "final_data": {"value": r.q}})
            kinds = {"feeds": "market", "PRACTICE_AREA": "sector", "linkedin_ind": "industry"}
            return {"query": r.q, "matches": [{"name": row[0], "kind": kinds.get(row[1], "industry")}
                for row in data.get("matched", [])[:r.limit] if isinstance(row, (list, tuple)) and len(row) >= 2]}
        if name in {"search_jobs", "companies_hiring"}:
            if name == "companies_hiring" and r.page:
                raise RadarError("invalid_request", "The source hiring-company rollup does not paginate; narrow the filters instead", 422)
            if name == "companies_hiring" and r.sort_by != "recent":
                raise RadarError("invalid_request", "The hiring-company rollup ranks by matching roles and does not support job sorting", 422)
            fd = r.model_dump(exclude_none=True, exclude={"page", "limit", "sort_by"})
            if fd.get("employment_type") == "internship":
                fd["employment_type"] = "intern"
            data = await self.radar("/jobs/", {"key": "find_jobs" if name == "search_jobs" else name,
                 "filters": fd, "page": r.page, "results_per_page": r.limit, "sort_by": r.sort_by})
            if name == "companies_hiring":
                rows = data.get("companies", [])
                data.update(companies=rows[:r.limit], returned=min(len(rows), r.limit),
                            rollup_note="Ranked by matching roles in a bounded source scan; total describes returned groups, not all hiring companies. Page offsets are unsupported.")
            return data
        if name == "job_filter_catalog":
            return {"schema": m.JobSearch.model_json_schema(), "suggestion_fields": ["title", "skills", "company", "location"],
                    "source_employment_type_aliases": {"internship": "intern"},
                    "notes": ["Title and employer use prefix matching; q uses source text search. Skills are OR matches.",
                              "Salary minimum filters the recorded salary maximum. Source currencies and salary periods are not normalized; do not compare different currencies as equivalent.",
                              "Experience is measured in months; positive bounds only. Remote=true filters remote records; false adds no onsite-only filter.",
                              "The company hiring rollup is bounded and does not implement page offsets. Use dedicated internship search for the additional internship corpus."]}
        if name == "job_filter_options":
            data = await self.radar("/jobs/suggest", {"field": r.field, "value": r.q})
            return {"field": r.field, "options": data.get("results", [])[:r.limit], "complete": False,
                    "note": "Bounded source suggestions; an empty response can also reflect a source lookup failure."}
        if name == "get_job":
            return await self.radar("/jobs/detail", {"id": r.id})
        if name == "salary_benchmark":
            return await self.radar("/jobs/salary_benchmark", {"filters": r.model_dump(exclude_none=True)})
        if name == "search_people":
            fd = r.model_dump(exclude_none=True, exclude={"page", "limit"})
            for source, dest in (("roles", "people_types"), ("locations", "location"),
                                 ("companies", "current_company"), ("sectors", "industry_sectors")):
                fd[dest] = fd.pop(source)
            fd["degree"] = fd.pop("degrees")
            fd.update(current_page=r.page, results_per_page=r.limit)
            return await self.radar("/people_search/", {"key": "find_people", "final_data": fd})
        if name == "get_article":
            source = "news" if self.upstream.settings.news_url else "business_news"
            return await self.upstream.call(source, "/v1/articles/" + r.article_id)
        paths = {"search_news": "headlines", "search_business_news": "headlines", "news_overview": "overview",
                 "news_trends": "trends", "news_sentiment": "sentiment", "search_business_events": "events",
                 "search_funding_news": "funding"}
        if name in paths:
            business = BY_NAME[name].source == "business_news" or bool(r.company)
            params = r.model_dump(exclude_none=True, mode="json")
            for source, dest in (("date_from", "since"), ("date_to", "until")):
                if source in params:
                    params[dest] = params.pop(source)
            return await self.upstream.call("business_news" if business else "news",
                "/v1/" + ("business/" if business else "") + paths[name], params=params)
        raise RadarError("unknown_feature", "Unknown capability", 404)

    @staticmethod
    def company_results(data, request):
        rows = data.get("companies", [])
        access = {k: data[k] for k in ("_plan", "_results_capped", "_searches_remaining", "_stripped_filters") if k in data}
        reverse = {v: k for k, v in FILTERS.items()}
        if isinstance(access.get("_stripped_filters"), list):
            access["_stripped_filters"] = [reverse.get(key, "account_restricted_filter") for key in access["_stripped_filters"]]
        tiers = data.get("_tiers") or []
        # Exclude diagnostic queries, SQL and implementation paths.
        tier_names = {"strict", "synonym", "synonyms", "radius", "semantic"}
        source_tiers = [{k: v for k, v in tier.items() if k in {"tier", "count", "added", "cumulative"}}
                        for tier in tiers if isinstance(tier, dict) and tier.get("tier") in tier_names]
        all_strict = bool(tiers) and all(t.get("tier") == "strict" for t in tiers)
        restricted = bool(access.get("_stripped_filters"))
        candidates, excluded = [], 0
        for row in rows[:request.limit]:
            tier = row.get("_tier") or ("strict" if all_strict else "unverified")
            tier = tier if tier in tier_names else "unverified"
            if request.match_mode == "strict" and (tier != "strict" or restricted):
                excluded += 1
                continue
            candidates.append({**company_card(row), "match_tier": tier})
        return {"companies": candidates, "page": request.page,
                "requested_limit": request.limit, "returned": len(candidates),
                "total": data.get("total"), "access": clean(access),
                "partial_timeout": bool(data.get("_partial_timeout")),
                "matching": {**clean({key: data[key] for key in ("_location_relaxed", "_location_scope") if key in data}),
                             "mode": request.match_mode, "tiers": clean(source_tiers),
                             "source_rows": len(rows), "excluded_candidates": excluded,
                             "strict_count_reported": data.get("_strict_count"),
                             "candidate_pool_count_reported": data.get("_total_matched"),
                             "count_capped": bool(data.get("_total_capped")),
                             "filters_restricted": restricted,
                             "note": "Strict means the source labelled the row strict and did not strip filters. Counts may describe an expanded candidate pool, not all matching companies. Missing tier metadata is unverified."},
                "next_page": request.page + 1 if rows and request.page < 200 else None,
                "pagination": "Increment source page even when strict filtering returns no rows; next_page is a continuation hint, not a guarantee of more matches. Account caps apply."}

    async def brief(self, r: m.Brief):
        calls = {
            "profile": ("get_company", m.CompanyProfile(domain=r.domain)),
            "financials": ("get_financials", m.Financials(domain=r.domain)),
            "intelligence": ("get_company_intelligence", m.Company(domain=r.domain)),
            "events": ("get_company_events", m.CompanyEvents(domain=r.domain, days=r.event_days)),
            "funding": ("get_company_funding", m.Company(domain=r.domain)),
            "enrichment": ("get_company_enrichment", m.Company(domain=r.domain)),
        }
        if r.include_news:
            calls["news"] = ("search_business_news", m.News(company=r.domain, limit=r.news_limit))
        return await self.sections(r.domain, calls)

    async def sections(self, domain, calls):
        # Keep fanout bounded; failures remain local to their sections.
        semaphore = asyncio.Semaphore(3)

        async def one(name, request):
            async with semaphore:
                try:
                    result = await self.run(name, request)
                    data = result["data"]
                    missing = isinstance(data, dict) and data.get("has_data") is False
                    return {"available": not missing, "result": brief_section(name, result),
                            "detail_request": {"method": "POST", "path": "/v1/" + BY_NAME[name].path, "body": request.model_dump(mode="json")},
                            **({"reason": "No data was supplied for this section"} if missing else {})}
                except RadarError as exc:
                    return {"available": False, "error": {"kind": exc.kind, "message": exc.message}}

        values = await asyncio.gather(*(one(name, request) for name, request in calls.values()))
        sections = dict(zip(calls, values))
        if not any(v["available"] for v in values):
            raise RadarError("coverage_unavailable", "None of the requested company sections is available", 503)
        return {"domain": domain, "sections": sections, "partial": any(
            not v["available"] or v.get("result", {}).get("meta", {}).get("partial", False) for v in values)}

    async def compare(self, request):
        results = []
        for domain in request.domains:
            try:
                result = await self.sections(domain, {
                    "profile": ("get_company", m.CompanyProfile(domain=domain)),
                    "financials": ("get_financials", m.Financials(domain=domain)),
                    "intelligence": ("get_company_intelligence", m.Company(domain=domain)),
                })
                results.append(result)
            except RadarError as exc:
                results.append({"domain": domain, "partial": True,
                                "error": {"kind": exc.kind, "message": exc.message}})
        if all("error" in item for item in results):
            raise RadarError("coverage_unavailable", "None of the requested companies is available", 503)
        return {"companies": results, "partial": any(r["partial"] for r in results),
                "comparison_note": "Fiscal calendars and available periods differ. No cross-company totals or investment ranking are calculated."}
