from __future__ import annotations

import asyncio
from contextvars import ContextVar
from dataclasses import dataclass

from . import models as m
from .auth import principal
from .errors import RadarError, envelope
from .public import clean, company_card, financial_data, news_content
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
    Feature("get_company", "companies/profile", m.Company, "Retrieve a company profile by its website domain."),
    Feature("get_company_intelligence", "companies/intelligence", m.Company, "Read company scores, peer comparisons, earnings and risk narratives. Scores are derived assessments, not financial facts."),
    Feature("get_financials", "companies/financials", m.Financials, "Retrieve income, balance-sheet and cash-flow metrics by fiscal period; distinguish filings from news reports and preserve currency and access limits."),
    Feature("get_company_events", "companies/events", m.CompanyEvents, "Read a company's event timeline, momentum, risks and the effective account-limited date window."),
    Feature("get_company_funding", "companies/funding", m.Company, "Read reported funding rounds and investors; retain approximate-amount flags."),
    Feature("get_company_enrichment", "companies/enrichment", m.Company, "Read legal identity, hiring, reputation, digital presence, innovation and social activity when available."),
    Feature("find_competitors", "companies/competitors", m.Competitors, "Find competitors in a named market, grouped by funding stage."),
    Feature("company_brief", "companies/brief", m.Brief, "Combine profile, financials, intelligence, events, enrichment, funding and linked news; report each unavailable section explicitly."),
    Feature("compare_companies", "companies/compare", m.Compare, "Compare two to five companies with separately labelled fiscal periods and partial-coverage flags."),
    Feature("search_investors", "investors/search", m.SearchCompanies, "Find investors by headquarters and portfolio industries or markets."),
    Feature("investor_directory", "investors/directory", m.Empty, "List published investor pages, sectors and cities."),
    Feature("get_investor_page", "investors/page", m.InvestorPage, "Retrieve a published investor profile or investor list by the slug from investor_directory."),
    Feature("market_pulse", "markets/pulse", m.Pulse, "Read recent funding, trending markets, sectors and investors for a bounded window."),
    Feature("location_intelligence", "locations/intelligence", m.Location, "Retrieve Radar's existing business intelligence for a named location."),
    Feature("discover_industries", "industries/discover", m.Lookup, "Find up to five matching industry or market names using a specific query."),
    Feature("search_jobs", "jobs/search", m.JobSearch, "Find job listings by company, skills, role, geography and freshness."),
    Feature("companies_hiring", "jobs/companies", m.JobSearch, "Find hiring companies for the same job filters."),
    Feature("get_job", "jobs/detail", m.JobDetail, "Retrieve a job listing by an ID returned by search_jobs."),
    Feature("salary_benchmark", "jobs/salary-benchmark", m.Salary, "Read salary statistics for a role, geography and optional currency; retain sample size and coverage."),
    Feature("search_people", "people/search", m.People, "Find professional profiles by name, role, company, skills and location; no contact-reveal actions."),
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

FILTERS = {
    "company_names": "company_name", "industries": "ai_ind", "sectors": "modern_sectors",
    "markets": "feeds", "business_models": "business_model", "locations": "selected_location",
    "sizes": "size", "stages": "funded_as", "technologies": "webstack", "products": "products",
    "skills": "skills", "event_types": "news_types", "financing_status": "financing_status",
    "ownership_status": "ownership_status", "revenue_bands": "revenue_band",
    "revenue_growth": "revenue_growth", "profitability": "profitable", "entity_type": "entity_type",
}


def filters(value: m.CompanyFilters):
    out = {FILTERS[k]: v for k, v in value.model_dump().items() if v and v != "all"}
    if out.get("revenue_band") == ["under1m"]:
        out["revenue_band"] = ["<1m"]
    return out


class Service:
    def __init__(self, upstream: Upstream, accounts=None):
        self.upstream = upstream
        self.accounts = accounts

    def catalog(self):
        user = principal()
        return [{"name": f.name, "method": "POST", "path": "/v1/" + f.path,
                 "description": f.description, "read_only": True,
                 "connection_configured": bool(self.upstream.settings.radar_url) if f.source == "radar" else bool(
                     user.news_key and (self.upstream.settings.news_url if f.source == "news" else self.upstream.settings.business_news_url)),
                 "input_schema": f.model.model_json_schema()} for f in FEATURES]

    async def run(self, name: str, request: m.Input):
        user = principal()
        if not self.accounts or METERING.get():
            return await self._run(name, request)
        units = 6 + int(request.include_news) if name == "company_brief" else (
            3 * len(request.domains) if name == "compare_companies" else 1)
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
            public_data = clean(data)
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
        partial = isinstance(data, dict) and bool(data.get("_partial_timeout") or data.get("partial_timeout"))
        if partial:
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
        if name in {"search_companies", "search_investors"}:
            fd = filters(r.filters)
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
            data = await self.radar("/company_search/shortlist_hydrate", {"websites": [r.domain]})
            rows = data.get("companies") or []
            if not rows or rows[0].get("_no_data"):
                raise RadarError("no_data", "No company profile is available for this domain", 404)
            return {"company": company_card(rows[0]), "access": data.get("_entitlements"),
                    "extras_gated": data.get("_extras_gated", False)}
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
        if name == "get_investor_page":
            return await self.radar("/investors/page/" + r.slug)
        if name == "market_pulse":
            return await self.radar("/analytical_q_radar/homepage_pulse", {"days": r.days,
                **{k + "_limit": r.limit for k in ("funding", "feed", "sector", "industry", "investor")}})
        if name == "location_intelligence":
            return await self.radar("/analytical_loc/", {"key": "analytical_loc", "final_data": r.model_dump()})
        if name == "discover_industries":
            data = await self.radar("/metas/", {"key": "search_metas_deep", "final_data": {"value": r.q}})
            kinds = {"feeds": "market", "PRACTICE_AREA": "sector", "linkedin_ind": "industry"}
            return {"query": r.q, "matches": [{"name": row[0], "kind": kinds.get(row[1], "industry")}
                for row in data.get("matched", [])[:r.limit] if isinstance(row, (list, tuple)) and len(row) >= 2]}
        if name in {"search_jobs", "companies_hiring"}:
            fd = r.model_dump(exclude_none=True, exclude={"page", "limit", "sort_by"})
            return await self.radar("/jobs/", {"key": "find_jobs" if name == "search_jobs" else name,
                 "filters": fd, "page": r.page, "results_per_page": r.limit, "sort_by": r.sort_by})
        if name == "get_job":
            return await self.radar("/jobs/detail", {"id": r.id})
        if name == "salary_benchmark":
            return await self.radar("/jobs/salary_benchmark", {"filters": r.model_dump(exclude_none=True)})
        if name == "search_people":
            fd = r.model_dump(exclude_none=True, exclude={"page", "limit"})
            for source, dest in (("roles", "people_types"), ("locations", "location"),
                                 ("companies", "current_company"), ("sectors", "industry_sectors")):
                fd[dest] = fd.pop(source)
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
        return {"companies": [company_card(c) for c in rows[:request.limit]], "page": request.page,
                "requested_limit": request.limit, "returned": min(len(rows), request.limit),
                "total": data.get("total"), "access": clean(access),
                "partial_timeout": bool(data.get("_partial_timeout")),
                "pagination": "Increment page; account caps can apply. No total is inferred from a page."}

    async def brief(self, r: m.Brief):
        calls = {
            "profile": ("get_company", m.Company(domain=r.domain)),
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
                    return {"available": not missing, "result": result,
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
                    "profile": ("get_company", m.Company(domain=domain)),
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
