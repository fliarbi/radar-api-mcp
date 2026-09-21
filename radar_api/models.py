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


class SearchCompanies(Page):
    filters: CompanyFilters = Field(default_factory=CompanyFilters)


class SemanticSearch(Page):
    q: Query
    filters: CompanyFilters = Field(default_factory=CompanyFilters)


class Company(Input):
    domain: Domain


PROFILE_SECTIONS = ("classification", "people", "technology", "web_presence", "traffic", "apps",
                    "products", "geography", "social", "lifecycle", "legal", "assessments",
                    "hiring", "innovation", "activity", "reputation", "share_of_voice")


class CompanyProfile(Company):
    company_id: Annotated[str, Field(min_length=1, max_length=100, pattern=r"^[A-Za-z0-9_-]+$")] | None = None
    sections: list[Literal["classification", "people", "technology", "web_presence", "traffic", "apps",
                           "products", "geography", "social", "lifecycle", "legal", "assessments",
                           "hiring", "innovation", "activity", "reputation", "share_of_voice"]] = Field(
                               default_factory=lambda: list(PROFILE_SECTIONS), max_length=17,
                               json_schema_extra={"default": list(PROFILE_SECTIONS)})
    item_limit: int = Field(100, ge=1, le=250)


class CompanyDocument(BaseModel):
    """Documented company output; optional sections depend on selection and coverage."""
    model_config = ConfigDict(extra="allow")
    name: str | None = None
    domain: str
    company_id: str | int | None = Field(None, description="Opaque public company identifier, when available")
    description: str | None = None
    detailed_description: str | None = None
    founded: int | str | None = None
    employee_count: int | float | None = None
    classification: dict[str, JsonValue] | None = Field(None, description="Sectors, primary/other feeds, markets, business and revenue models, industries and flags")
    people: dict[str, JsonValue] | None = Field(None, description="Named key people, founder designations, count and background categories; no contacts")
    technology: dict[str, JsonValue] | None = Field(None, description="Website stack, technographics, observed technologies and crawl date")
    web_presence: dict[str, JsonValue] | None = Field(None, description="Rank, CDN, performance metrics, SEO, structured data and digital presence score")
    traffic: dict[str, JsonValue] | None = Field(None, description="Visits and date, geography shares, keywords, bounce rate and pages per visit")
    apps: dict[str, JsonValue] | None = Field(None, description="Aggregate app count, downloads and weighted rating; not an app roster")
    products: list[JsonValue] | None = None
    geography: dict[str, JsonValue] | None = None
    social: dict[str, JsonValue] | None = None
    lifecycle: dict[str, JsonValue] | None = None
    legal: list[JsonValue] | None = None
    assessments: dict[str, JsonValue] | None = Field(None, description="Derived scores, not financial statement values")
    hiring: dict[str, JsonValue] | None = None
    innovation: dict[str, JsonValue] | None = None
    activity: list[JsonValue] | None = None
    reputation: dict[str, JsonValue] | None = None
    share_of_voice: dict[str, JsonValue] | None = None


class CompanyProfileData(BaseModel):
    model_config = ConfigDict(extra="allow")
    company: CompanyDocument
    profile_depth: Literal["detailed", "card"]
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
    employment_type: Literal["full_time", "part_time", "contract", "temporary", "internship"] | None = None
    freshness_days: int | None = Field(None, ge=1, le=365)
    sort_by: Literal["recent", "relevance"] = "recent"


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
    roles: Annotated[list[Literal["founder", "investor", "executive"]], Field(max_length=3)] = Field(default_factory=list)
    locations: Terms = Field(default_factory=list)
    skills: Terms = Field(default_factory=list)
    companies: list[Domain] = Field(default_factory=list, max_length=20)
    sectors: Terms = Field(default_factory=list)
    min_experience_years: int | None = Field(None, ge=0, le=80)


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
