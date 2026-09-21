from __future__ import annotations

import ipaddress
import re
from datetime import date
from typing import Annotated, Literal

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, JsonValue, model_validator


def clean_text(value: str) -> str:
    value = value.strip()
    # Some legacy Radar handlers interpolate strings. Restrict their input at this boundary.
    if not value or re.search(r"[\x00-\x1f\x7f'\"\\;]", value):
        raise ValueError("Use nonempty text without control characters, quotes, backslashes or semicolons")
    return value


Text = Annotated[str, Field(min_length=1, max_length=200), AfterValidator(clean_text)]
Query = Annotated[str, Field(min_length=2, max_length=500), AfterValidator(clean_text)]
Terms = Annotated[list[Text], Field(max_length=20)]


def domain_name(value: str) -> str:
    value = value.strip().lower().removeprefix("www.")
    try:
        value = value.encode("idna").decode("ascii")
        ipaddress.ip_address(value)
    except UnicodeError:
        raise ValueError("Invalid domain") from None
    except ValueError:
        pass
    else:
        raise ValueError("Use a company domain, not an IP address")
    if not re.fullmatch(r"(?=.{3,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}", value):
        raise ValueError("Use a domain such as microsoft.com, without a URL, path or port")
    return value


Domain = Annotated[str, AfterValidator(domain_name)]
Slug = Annotated[str, Field(min_length=1, max_length=180, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")]
ArticleID = Annotated[str, Field(pattern=r"^[0-9a-fA-F]{24}$")]


class Input(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, allow_inf_nan=False)


class Empty(Input):
    pass


class ResponseMeta(BaseModel):
    retrieved_at: str
    partial: bool
    notes: list[str]
    provider: str
    coverage: dict[str, JsonValue] | None = None
    plan: str | None = None
    quota: dict[str, JsonValue] | None = None
    billing: dict[str, JsonValue] | None = None


class ResponseError(BaseModel):
    kind: str
    message: str
    retry_after: int | None = None


class Envelope(BaseModel):
    ok: bool
    feature: str
    data: JsonValue = None
    window: dict[str, JsonValue]
    meta: ResponseMeta
    error: ResponseError | None = None


class Page(Input):
    page: int = Field(0, ge=0, le=200)
    limit: int = Field(20, ge=1, le=100)


class HiringFilter(Input):
    is_hiring: bool = True
    min_open_roles: int = Field(1, ge=1, le=100000)
    roles: Terms = Field(default_factory=list)
    cities: Terms = Field(default_factory=list)
    recency_days: int = Field(30, ge=1, le=365)


class CompanyFilters(Input):
    company_names: Terms = Field(default_factory=list)
    industries: Terms = Field(default_factory=list)
    sectors: Terms = Field(default_factory=list)
    markets: Terms = Field(default_factory=list)
    business_models: Terms = Field(default_factory=list)
    locations: Terms = Field(default_factory=list)
    sizes: Terms = Field(default_factory=list)
    stages: Terms = Field(default_factory=list)
    technologies: Terms = Field(default_factory=list)
    products: Terms = Field(default_factory=list)
    skills: Terms = Field(default_factory=list)
    event_types: Terms = Field(default_factory=list)
    financing_status: Terms = Field(default_factory=list)
    ownership_status: Terms = Field(default_factory=list)
    revenue_bands: list[Literal["under1m", "1m-10m", "10m-100m", "100m-1b", "1b+"]] = Field(default_factory=list, max_length=1)
    revenue_growth: list[Literal["declining", "flat", "growing", "high", "hyper"]] = Field(default_factory=list, max_length=1)
    profitability: list[Literal["profitable", "loss"]] = Field(default_factory=list, max_length=1)
    entity_type: Literal["all", "investor", "incubator"] = "all"
    revenue_models: Terms = Field(default_factory=list)
    business_approaches: Terms = Field(default_factory=list)
    scalability: Terms = Field(default_factory=list)
    growth_stages: Terms = Field(default_factory=list)
    operating_status: Terms = Field(default_factory=list)
    organization_types: Terms = Field(default_factory=list)
    deal_sizes: Terms = Field(default_factory=list)
    ages: list[Literal["Most Recent", "< 5y", "5-10y", "10-25y", "25+y"]] = Field(default_factory=list, max_length=1)
    founded_year_from: int | None = Field(None, ge=1800, le=2100)
    founded_year_to: int | None = Field(None, ge=1800, le=2100)
    positions: Terms = Field(default_factory=list)
    verticals: Terms = Field(default_factory=list)
    industrial_applications: Terms = Field(default_factory=list)
    founders_background: list[Literal["serial_entrepreneur", "first_time_founder", "founder_with_exit", "top_ranked_founder", "top_tier_university", "elite_alumni", "technical_founder", "ex_notable_employer", "c_level_exec", "seasoned_15y"]] = Field(default_factory=list, max_length=10)
    web_popularity: list[Literal["high", "medium", "low"]] = Field(default_factory=list, max_length=3)
    web_cwv: list[Literal["pass", "needs_improvement", "poor"]] = Field(default_factory=list, max_length=3)
    web_speed: list[Literal["fast", "average", "slow"]] = Field(default_factory=list, max_length=3)
    web_seo_maturity: Terms = Field(default_factory=list)
    web_sd_maturity: Terms = Field(default_factory=list)
    web_business_hints: Terms = Field(default_factory=list)
    web_score: list[Literal["80+", "60-80", "40-60", "<40"]] = Field(default_factory=list, max_length=1)
    mobile_downloads: list[Literal["1k+", "100k+", "1m+", "10m+"]] = Field(default_factory=list, max_length=1)
    mobile_growth: list[Literal["declining", "flat", "growing", "high", "hyper"]] = Field(default_factory=list, max_length=1)
    hiring: HiringFilter | None = None
    radius_km: int | None = Field(None, ge=21, le=250, description="Explicit radius expansion around the selected location; source matching tiers apply")

    @model_validator(mode="after")
    def year_range(self):
        if self.founded_year_from and self.founded_year_to and self.founded_year_from > self.founded_year_to:
            raise ValueError("founded_year_from must not exceed founded_year_to")
        if self.radius_km and not self.locations:
            raise ValueError("radius_km requires locations")
        return self


CompanySort = Literal["relevance", "valuation", "funding", "estimated_revenue", "financing_rounds", "latest_deal", "employees", "prominence", "finance", "scalability", "momentum", "innovation", "maturity"]


class SearchCompanies(Page):
    filters: CompanyFilters = Field(default_factory=CompanyFilters)
    sort_by: CompanySort = "relevance"


class SemanticSearch(Page):
    q: Query
    filters: CompanyFilters = Field(default_factory=CompanyFilters)


class Company(Input):
    domain: Domain


PROFILE_SECTIONS = ("overview", "classification", "people", "technology", "web_presence", "traffic", "apps",
                    "products", "geography", "social", "lifecycle", "legal", "assessments",
                    "hiring", "innovation", "activity", "reputation", "share_of_voice")


class CompanyProfile(Company):
    company_id: Annotated[str, Field(min_length=1, max_length=100, pattern=r"^[A-Za-z0-9_-]+$")] | None = None


class CompanyField(CompanyProfile):
    field: Literal["overview", "classification", "people", "technology", "web_presence", "traffic", "apps", "products", "geography", "social", "lifecycle", "legal", "assessments", "hiring", "innovation", "activity", "reputation", "share_of_voice"]
    item_limit: int = Field(50, ge=1, le=100)


Column = Literal["founded_year", "employees", "total_funding", "latest_revenue", "valuation", "financing_rounds", "growth_stage", "funding_stage", "web_presence", "mobile_downloads", "mobile_growth", "revenue_model", "business_model", "industry", "country", "ownership"]


class CompanyColumns(Input):
    domains: list[Domain] = Field(min_length=1, max_length=20)
    columns: list[Column] = Field(min_length=1, max_length=14)


class CompanyFilterOptions(Input):
    field: Annotated[str, Field(pattern=r"^[a-z_]+$", max_length=60)]
    q: Query
    limit: int = Field(10, ge=1, le=10)


class CompanyContacts(Company):
    fields: list[Literal["emails", "phones"]] = Field(min_length=1, max_length=2)


class PersonContacts(Input):
    person_id: Annotated[str, Field(pattern=r"^[A-Za-z0-9_-]{1,100}$")]
    fields: list[Literal["emails", "phones"]] = Field(min_length=1, max_length=2)


class CompanyDocument(BaseModel):
    """Compact identity only; detail fields require a separate CompanyField request."""
    model_config = ConfigDict(extra="forbid")
    name: str | None = None
    domain: str
    company_id: str | int | None = None
    description: str | None = None
    founded: int | str | None = None
    employee_count: int | float | None = None
    logo_url: str | None = Field(None, description="Radar image route; can fall back to a favicon")


class CompanyProfileData(BaseModel):
    model_config = ConfigDict(extra="allow")
    company: CompanyDocument
    profile_depth: Literal["summary", "card"]
    available_fields: list[str] = Field(default_factory=list)
    field_status: dict[str, str] = Field(default_factory=dict)
    coverage: dict[str, JsonValue] | None = Field(None, description="Per-section availability and per-array available/returned/truncated counts")
    updated_at: str | None = None


class CompanyProfileEnvelope(Envelope):
    data: CompanyProfileData | None = None


class CompanyEvents(Company):
    days: int = Field(365, ge=1, le=1095)
    limit: int = Field(100, ge=1, le=100)
    event_types: Terms = Field(default_factory=list)


class Financials(Company):
    statement: Literal["all", "income", "balance_sheet", "cash_flow"] = "all"
    period_type: Literal["all", "annual", "quarterly"] = "all"
    year_from: int | None = Field(None, ge=1900, le=2100)
    year_to: int | None = Field(None, ge=1900, le=2100)
    limit: int = Field(40, ge=1, le=100)

    @model_validator(mode="after")
    def years(self):
        if self.year_from and self.year_to and self.year_from > self.year_to:
            raise ValueError("year_from must not exceed year_to")
        return self


class Competitors(Input):
    market: Text
    business_model: Text | None = None
    per_stage: int = Field(5, ge=3, le=10)


class Lookup(Input):
    q: Query
    limit: int = Field(5, ge=1, le=5)


class InvestorPage(Input):
    slug: Slug


class InvestorField(InvestorPage):
    field: Literal["portfolio", "undated_portfolio", "sectors", "stages", "activity", "follow_on",
                   "co_investors", "news", "analysis", "related", "investors", "recent_rounds",
                   "themes", "research", "geography", "selection"]
    limit: int = Field(20, ge=1, le=100)
    offset: int = Field(0, ge=0, le=100000)
    q: Query | None = None
    sector: Text | None = None
    stage: Text | None = None
    city: Text | None = None
    country: Text | None = None
    kind: Literal["angel", "firm"] | None = None
    sort_by: Literal["source", "name", "latest", "companies"] = "source"


class Pulse(Input):
    days: int = Field(30, ge=1, le=365)
    limit: int = Field(5, ge=1, le=10)


class Location(Input):
    location: Text
    location_type: Literal["city", "state", "country", "cc"] = "country"


class JobSearch(Page):
    q: Query | None = None
    title: Text | None = None
    company: Text | None = Field(None, description="Employer name prefix, such as Microsoft; the Jobs source does not interpret this field as a website domain")
    city: Text | None = None
    country: Text | None = None
    skills: Terms = Field(default_factory=list)
    remote: bool = False
    employment_type: Literal["full_time", "part_time", "contract", "temporary", "internship", "intern", "freelance"] | None = None
    salary_min: float | None = Field(None, gt=0, le=1000000000, description="Source salary upper bound must reach this amount; source does not normalize currencies or periods")
    min_experience_months: int | None = Field(None, ge=1, le=960)
    max_experience_months: int | None = Field(None, ge=1, le=960)
    sources: list[Literal["foundit", "shine", "talent"]] = Field(default_factory=list, max_length=3)
    freshness_days: int | None = Field(None, ge=1, le=365)
    sort_by: Literal["recent", "relevance", "salary"] = "recent"

    @model_validator(mode="after")
    def experience_window(self):
        if self.min_experience_months and self.max_experience_months and self.min_experience_months > self.max_experience_months:
            raise ValueError("Minimum experience must not exceed maximum")
        return self


class JobOptions(Input):
    field: Literal["title", "skills", "company", "location"]
    q: Query
    limit: int = Field(10, ge=1, le=10)


class InternshipSearch(Page):
    title: Text | None = None
    company: Text | None = None
    location: Text | None = None
    skills: Terms = Field(default_factory=list)
    work_mode: Literal["any", "remote", "onsite"] = "any"
    part_time: bool = False
    stipend_min: float | None = Field(None, gt=0, le=10000000)
    posted_since: date | None = None
    posted_until: date | None = None
    validity: Literal["observed", "not_expired"] = "observed"

    @model_validator(mode="after")
    def posting_window(self):
        if self.posted_since and self.posted_until and self.posted_since > self.posted_until:
            raise ValueError("posted_since must not exceed posted_until")
        return self


class InternshipDetail(Input):
    id: Annotated[str, Field(min_length=1, max_length=100, pattern=r"^[A-Za-z0-9_-]+$")]


AppID = Annotated[str, Field(min_length=3, max_length=255, pattern=r"^[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+$")]


class App(Input):
    app_id: AppID


class AppField(App):
    field: Literal["listing", "ratings", "monetization", "release", "developer", "growth", "install_history"]
    limit: int = Field(20, ge=1, le=100)
    offset: int = Field(0, ge=0, le=10000)


class AppSearch(Page):
    q: Query | None = None
    developer: Text | None = None
    domain: Domain | None = None
    category: Text | None = None
    min_installs: int | None = Field(None, ge=1, le=10**15)
    min_score: float | None = Field(None, ge=0, le=5)
    free: bool | None = None
    sort_by: Literal["installs", "rating", "observed", "name"] = "installs"

    @model_validator(mode="after")
    def bounded_discovery(self):
        if not any([self.q, self.developer, self.domain, self.category, self.min_installs]):
            raise ValueError("Supply a query, developer, domain, category or minimum installs")
        return self


class CompanyApps(Page):
    domain: Domain


class AppOptions(Input):
    q: Text | None = None
    limit: int = Field(20, ge=1, le=100)


class OpportunitySearch(SearchCompanies):
    preset: Literal["high_growth", "profitable_growth", "early_stage", "hiring_expansion", "technology_modernization", "mobile_scale"]
    limit: int = Field(10, ge=1, le=20)


class JobDetail(Input):
    id: Annotated[str, Field(min_length=1, max_length=160, pattern=r"^[a-zA-Z0-9:_-]+$")]


class Salary(Input):
    title: Text
    city: Text | None = None
    country: Text | None = None
    currency: Annotated[str, Field(pattern=r"^[A-Z]{3}$")] | None = None
    skills: Terms = Field(default_factory=list)


class People(Page):
    name: Text | None = None
    roles: Annotated[list[Literal["founder", "investor", "executive", "board"]], Field(max_length=4)] = Field(default_factory=list)
    locations: Terms = Field(default_factory=list)
    skills: Terms = Field(default_factory=list)
    companies: Terms = Field(default_factory=list, description="Company name or domain prefix")
    sectors: Terms = Field(default_factory=list)
    min_experience_years: int | None = Field(None, ge=0, le=80)
    schools: Terms = Field(default_factory=list)
    degrees: Terms = Field(default_factory=list)
    min_seniority: Literal["entry", "senior", "manager", "director", "vp", "cxo", "partner", "owner"] | None = None
    min_people_rank: float | None = Field(None, ge=0, le=100)


class PeopleOptions(Input):
    field: Literal["schools", "skills", "sectors"]
    q: Query
    limit: int = Field(10, ge=1, le=10)


class NewsQuery(Input):
    q: Annotated[str, Field(min_length=2, max_length=120), AfterValidator(clean_text)] | None = None
    company: Domain | None = None
    country: Text | None = None
    date_from: date | None = None
    date_to: date | None = None
    sentiment: Literal["positive", "neutral", "negative"] | None = None
    priority_min: int | None = Field(None, ge=1, le=9)

    @model_validator(mode="after")
    def valid_window(self):
        if self.date_from and self.date_to and self.date_from > self.date_to:
            raise ValueError("date_from must not exceed date_to")
        if not self.q and not self.company:
            raise ValueError("Supply q or company")
        return self


class News(NewsQuery):
    limit: int = Field(100, ge=1, le=100)
    cursor: Annotated[str, Field(max_length=2048, pattern=r"^[A-Za-z0-9_=+-]+$")] | None = None
    sort: Literal["newest", "oldest", "priority"] = "newest"


class NewsAnalysis(NewsQuery):
    granularity: Literal["daily", "weekly", "monthly"] = "weekly"


class FundingNews(News):
    investor: Text | None = None
    sector: Text | None = None
    round_type: Text | None = None
    min_amount_usd: float | None = Field(None, ge=0)


class Article(Input):
    article_id: ArticleID


class Brief(Company):
    include_news: bool = True
    news_limit: int = Field(10, ge=1, le=100)
    event_days: int = Field(365, ge=1, le=1095)


class Compare(Input):
    domains: list[Domain] = Field(min_length=2, max_length=5)

    @model_validator(mode="after")
    def distinct(self):
        if len(set(self.domains)) != len(self.domains):
            raise ValueError("Supply distinct company domains")
        return self
