"""Fifty current documentation questions; original requests remain in baseline captures."""

CASES = []


def add(key, question, operation, request, guide, checks=()):
    CASES.append(
        dict(
            id=f"{len(CASES) + 1:02d}-{key}",
            question=question,
            operation=operation,
            request=request,
            guide=guide,
            checks=list(checks),
        )
    )


F = "financial-filters-data-api"
T = "teams-people-data-api"
C = "company-search-api"
A = "apps-data-api"
J = "hiring-signals-jobs-api"
INTERNS = "internships-companies-api"
add(
    "adtech-vocabulary",
    "Which industry value selects AdTech companies?",
    "company_filter_options",
    {"field": "industries", "q": "AdTech", "limit": 5},
    C,
    ["adtech_option"],
)
add(
    "usa-vocabulary",
    "Which location value selects the United States?",
    "company_filter_options",
    {"field": "locations", "q": "United States", "limit": 5},
    C,
)
add(
    "usa-adtech-under-10k",
    "Find US AdTech startups founded since 2021 with latest annual revenue below USD 10,000.",
    "screen_company_financials",
    {
        "filters": {"industries": ["AdTech"], "locations": ["United States"], "founded_year_from": 2021},
        "constraints": [{"metric": "revenue", "lt": 10000, "gte": 0}],
        "period_type": "annual",
        "candidate_limit": 3,
    },
    F,
    ["financial_screen"],
)
add(
    "usa-adtech-over-1m",
    "Find US AdTech companies with latest annual revenue of at least USD 1 million.",
    "screen_company_financials",
    {
        "filters": {"industries": ["AdTech"], "locations": ["United States"]},
        "constraints": [{"metric": "revenue", "gte": 1000000}],
        "period_type": "annual",
        "candidate_limit": 3,
    },
    F,
    ["financial_screen"],
)
add(
    "india-profitable",
    "Find profitable Indian software companies with recorded revenue growth.",
    "search_companies",
    {
        "filters": {
            "industries": ["Software"],
            "locations": ["India"],
            "profitability": ["profitable"],
            "revenue_growth": ["growing"],
        },
        "limit": 3,
    },
    F,
)
add(
    "under-1m-band",
    "Find US AdTech candidates in Radar’s positive-revenue under-USD-1M band.",
    "search_companies",
    {
        "filters": {"industries": ["AdTech"], "locations": ["United States"], "revenue_bands": ["under1m"]},
        "limit": 3,
    },
    F,
)
add(
    "10m-100m-band",
    "Find Indian software companies in the USD 10M–100M revenue band.",
    "search_companies",
    {
        "filters": {"industries": ["Software"], "locations": ["India"], "revenue_bands": ["10m-100m"]},
        "limit": 3,
    },
    F,
)
add(
    "high-growth",
    "Find Indian software candidates with recorded 30–100% revenue growth.",
    "search_companies",
    {"filters": {"industries": ["Software"], "locations": ["India"], "revenue_growth": ["high"]}, "limit": 3},
    F,
)
add(
    "loss-making",
    "Find Indian payments companies with recorded net losses.",
    "search_companies",
    {"filters": {"markets": ["Payments"], "locations": ["India"], "profitability": ["loss"]}, "limit": 3},
    F,
)
add(
    "startup-age",
    "Find US AdTech companies founded from 2021 through 2026 without assuming a funding stage.",
    "search_companies",
    {
        "filters": {
            "industries": ["AdTech"],
            "locations": ["United States"],
            "founded_year_from": 2021,
            "founded_year_to": 2026,
        },
        "limit": 3,
    },
    C,
)
add(
    "seed-small-round",
    "Find Indian seed-stage software companies with funding rounds in the USD 10K–100K band.",
    "search_companies",
    {
        "filters": {
            "industries": ["Software"],
            "locations": ["India"],
            "stages": ["Seed"],
            "deal_sizes": ["10-100K"],
        },
        "limit": 3,
    },
    "startup-funding-data-api",
)
add(
    "subscription-model",
    "Find US software companies classified with subscription revenue models.",
    "search_companies",
    {
        "filters": {
            "industries": ["Software"],
            "locations": ["United States"],
            "revenue_models": ["subscription"],
        },
        "limit": 3,
    },
    C,
)
add(
    "balance-sheet",
    "Check electroCore FY2024 balance-sheet coverage for assets, liabilities and equity.",
    "get_financials",
    {
        "domain": "electrocore.com",
        "statement": "balance_sheet",
        "period_type": "annual",
        "year_from": 2024,
        "year_to": 2024,
        "limit": 3,
    },
    F,
    ["financial_periods"],
)
add(
    "annual-income",
    "Retrieve electroCore FY2024 income figures without quarterly mixing.",
    "get_financials",
    {
        "domain": "electrocore.com",
        "statement": "income",
        "period_type": "annual",
        "year_from": 2024,
        "year_to": 2024,
        "limit": 3,
    },
    F,
    ["financial_periods"],
)
add(
    "annual-cash-flow",
    "Check electroCore annual operating cash flow, capex and free cash flow coverage.",
    "get_financials",
    {"domain": "electrocore.com", "statement": "cash_flow", "period_type": "annual", "year_from": 2024, "year_to": 2024, "limit": 3},
    F,
    ["financial_periods"],
)
add(
    "quarterly-income",
    "Retrieve electroCore’s latest accessible quarterly income periods.",
    "get_financials",
    {"domain": "electrocore.com", "statement": "income", "period_type": "quarterly", "limit": 3},
    F,
    ["financial_periods"],
)
add(
    "funding-rounds",
    "Retrieve OpenAI funding rounds separately from revenue.",
    "get_company_funding",
    {"domain": "openai.com"},
    "startup-funding-data-api",
)
add(
    "finance-columns",
    "Compare available revenue and funding display columns for Razorpay and Stripe.",
    "get_company_columns",
    {"domains": ["razorpay.com", "stripe.com"], "columns": ["latest_revenue", "total_funding", "employees"]},
    F,
)
add(
    "precise-profit-screen",
    "Check whether Qualys has positive annual profit and revenue of at least USD 100M in its latest accessible year.",
    "screen_company_financials",
    {
        "domains": ["qualys.com"],
        "constraints": [{"metric": "net_income", "gt": 0}, {"metric": "revenue", "gte": 100000000}],
        "period_type": "annual",
    },
    F,
    ["financial_screen"],
)
add(
    "financial-filter-definitions",
    "Discover exact financial thresholds, growth meanings and screening limits.",
    "financial_filter_catalog",
    {},
    F,
    ["financial_catalog"],
)
add(
    "razorpay-founders",
    "Retrieve Razorpay’s recorded founders with role descriptions.",
    "get_company_team",
    {"domain": "razorpay.com", "group": "founders", "limit": 10},
    T,
    ["team"],
)
add(
    "stripe-leadership",
    "Retrieve Stripe’s recorded key people and designations.",
    "get_company_team",
    {"domain": "stripe.com", "group": "key_people", "limit": 10},
    T,
    ["team"],
)
add(
    "swiggy-leadership",
    "Retrieve Swiggy’s recorded key people and their roles.",
    "get_company_team",
    {"domain": "swiggy.com", "group": "key_people", "limit": 10},
    T,
    ["team"],
)
add(
    "microsoft-team",
    "Retrieve professional records with an exact current-company domain of microsoft.com.",
    "get_company_team",
    {"domain": "microsoft.com", "group": "professionals", "limit": 3},
    T,
    ["team"],
)
add(
    "stripe-executives",
    "Find Stripe professionals categorized as executives with exact domain affiliation.",
    "get_company_team",
    {"domain": "stripe.com", "group": "professionals", "roles": ["executive"], "limit": 3},
    T,
    ["team"],
)
add(
    "razorpay-chief",
    "Find Razorpay key people whose recorded designation contains CEO.",
    "get_company_team",
    {"domain": "razorpay.com", "group": "key_people", "title": "CEO", "limit": 10},
    T,
    ["team"],
)
add(
    "founder-education",
    "Find founders who studied at Stanford University.",
    "search_people",
    {"roles": ["founder"], "schools": ["Stanford University"], "limit": 3},
    T,
)
add(
    "professional-skills",
    "Find Microsoft-associated professionals with Python skills.",
    "search_people",
    {"companies": ["Microsoft"], "skills": ["Python"], "limit": 3},
    T,
)
add(
    "professional-experience",
    "Find Microsoft-associated professionals with at least ten years of experience.",
    "search_people",
    {"companies": ["Microsoft"], "min_experience_years": 10, "limit": 3},
    T,
)
add(
    "india-senior-executives",
    "Find India-based executives whose highest recorded seniority is director or above.",
    "search_people",
    {"roles": ["executive"], "locations": ["India"], "min_seniority": "director", "limit": 3},
    T,
)
add(
    "company-apps",
    "Which Google Play apps have swiggy.com as the developer website host?",
    "company_apps",
    {"domain": "swiggy.com", "limit": 5},
    A,
    ["app_domain"],
)
add(
    "food-apps",
    "Find Food & Drink apps with at least one million installs and rating at least four.",
    "search_apps",
    {"category": "Food & Drink", "min_installs": 1000000, "min_score": 4, "limit": 3},
    A,
    ["app_filters"],
)
add(
    "app-growth",
    "Retrieve Swiggy app growth together with the dated measurements and reliability flag.",
    "get_app_field",
    {"app_id": "in.swiggy.android", "field": "growth"},
    A,
)
add(
    "app-history-page",
    "Retrieve the second page of Swiggy install observations while retaining source duplicates.",
    "get_app_field",
    {"app_id": "in.swiggy.android", "field": "install_history", "limit": 5, "offset": 5},
    A,
)
add(
    "app-monetization",
    "Does Swiggy’s app record show ads, purchases, currency and paid/free status?",
    "get_app_field",
    {"app_id": "in.swiggy.android", "field": "monetization"},
    A,
)
add(
    "app-ratings",
    "Retrieve Swiggy’s rating histogram and review counts.",
    "get_app_field",
    {"app_id": "in.swiggy.android", "field": "ratings"},
    A,
)
add(
    "us-software-jobs",
    "Find observed US software engineer job postings.",
    "search_jobs",
    {"title": "software engineer", "country": "US", "limit": 3},
    J,
)
add(
    "normalized-interns",
    "Find internship-type records from Shine using the public internship alias.",
    "search_jobs",
    {"title": "intern", "employment_type": "internship", "sources": ["shine"], "limit": 3},
    J,
)
add(
    "company-skill-jobs",
    "Find Connvertex job listings with Python in the role title.",
    "search_jobs",
    {"company": "Connvertex", "title": "Python", "limit": 3},
    J,
)
add(
    "salary-benchmark",
    "Retrieve the USD software-engineer salary benchmark for the US with sample size.",
    "salary_benchmark",
    {"title": "software engineer", "country": "US", "currency": "USD"},
    J,
)
add(
    "remote-part-time-interns",
    "Find observed remote part-time internships with explicit work-mode evidence.",
    "search_internships",
    {"work_mode": "remote", "part_time": True, "limit": 3},
    INTERNS,
    ["internship"],
)
add(
    "internship-employers",
    "Which source employers have Business Development internship listings?",
    "companies_offering_internships",
    {"title": "Business Development", "limit": 3},
    INTERNS,
)
add(
    "internship-stipend",
    "Find observed internship listings with stipend value at least 10,000, preserving currency and unknown period.",
    "search_internships",
    {"stipend_min": 10000, "limit": 3},
    INTERNS,
    ["internship"],
)
add(
    "investor-fintech",
    "Retrieve Anupam Mittal’s recorded FinTech portfolio entries.",
    "get_investor_field",
    {"slug": "anupam-mittal", "field": "portfolio", "sector": "FinTech", "limit": 3},
    "investor-data-api",
)
add(
    "investor-co-backers",
    "Retrieve Anupam Mittal’s measured co-investor relationships.",
    "get_investor_field",
    {"slug": "anupam-mittal", "field": "co_investors"},
    "investor-data-api",
)
add(
    "investor-directory",
    "Retrieve three investors from the reviewed Bengaluru FinTech directory.",
    "get_investor_field",
    {"slug": "fintech-investors-in-bengaluru", "field": "investors", "limit": 3},
    "investor-data-api",
)
add(
    "company-taxonomy",
    "Retrieve Razorpay sectors, primary feeds and other business classifications.",
    "get_company_field",
    {"domain": "razorpay.com", "field": "classification", "item_limit": 100},
    "technology-traffic-data-api",
)
add(
    "company-technologies",
    "Retrieve Stripe’s observed technologies with their available source structure.",
    "get_company_field",
    {"domain": "stripe.com", "field": "technology", "item_limit": 100},
    "technology-traffic-data-api",
)
add(
    "company-traffic",
    "Retrieve Swiggy traffic and geography observations.",
    "get_company_field",
    {"domain": "swiggy.com", "field": "traffic", "item_limit": 100},
    "technology-traffic-data-api",
)
add(
    "company-news",
    "Retrieve Microsoft business news for April 2026 and retain dates and source links.",
    "search_business_news",
    {"company": "microsoft.com", "date_from": "2026-04-01", "date_to": "2026-04-30", "limit": 3},
    "financial-news-api",
)
assert len(CASES) == 50 and len({x["id"] for x in CASES}) == 50
