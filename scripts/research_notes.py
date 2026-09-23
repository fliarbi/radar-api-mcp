"""Customer explanations for evidence screening and team workflows."""
NOTES = {
    "financial_filter_catalog": {
        "title": "Financial filter definitions API: exact USD constraints and source bands",
        "purpose": "Discover the typed numeric screen and the actual boundaries used by Radar's revenue, growth and profitability filters before building a screening interface.",
        "workflow": "Choose a metric, annual or quarterly periods, a source requirement and explicit inclusive/exclusive bounds. Use company filters to discover candidates or supply accepted domains directly.",
        "fields": {"data.numeric_screen": "Complete financial-screen JSON schema, including nested company filters and constraints.", "data.revenue_bands": "Legacy summary comparisons; exact boundary values and zero are excluded.", "data.growth_bands_pct": "Source one-year growth bucket edges in percent.", "data.coverage": "The exact screen is bounded, not an exhaustive financial database query."},
        "observed": "The capture includes precise metric constraints and the source definitions. The under-$10,000 startup scenario and a positive over-$1-million AdTech scenario are separately executed in the 50-question audit.",
        "pitfall": "Revenue models, funding deal sizes and estimated display values are not fiscal revenue. A missing financial value must not become zero.",
        "guide": "financial-filters-data-api",
    },
    "screen_company_financials": {
        "title": "Exact company financial screening API: dated revenue and profit conditions",
        "purpose": "Evaluate one bounded candidate page or up to ten explicit company domains against one to five USD financial conditions. Return the evidence and distinguish matches, non-matches, unknown values and failed reads.",
        "workflow": "Select annual or quarterly periods and optional fiscal-year bounds. All conditions use the same latest accessible period. Review evaluated rows, source-plan limits and matching metadata before continuing to another candidate page.",
        "fields": {"data.matches": "Rows whose available USD metrics satisfy every condition.", "data.evaluated": "Every inspected domain, including failed and unresolved reads; successful rows retain the dated financial period.", "data.counts": "Counts by matched, not_matched, unknown or unavailable outcome.", "data.discovery": "Source candidate page, strict matching labels, excluded rows and access limits; null for explicit domains.", "data.next_page": "Source continuation hint; keep the same filters and page size. It does not guarantee more matches.", "data.coverage": "Always bounded; partial indicates missing evidence, restricted filters, failed reads or source limits.", "data.successful_financial_reads": "Used to settle composite account credits; an empty successful financial read still counts."},
        "observed": "The US AdTech annual-revenue screen above $1 million returned two measured matches and one unknown. The separate startup screen below $10,000 had three unknown annual observations and no verified match; see scenario 03.",
        "pitfall": "This is not a global financial query or an exhaustive export. It does not infer startup status, bypass source plan gates or fall back to older periods to manufacture a match.",
        "guide": "financial-filters-data-api",
    },
    "get_company_team": {
        "title": "Company team data API: founders, key people and professional profiles",
        "purpose": "Retrieve one explicitly selected people group for a company domain. Founders and key people come from company records; professional profiles preserve skills, education, experience and exact recorded company-domain affiliation.",
        "workflow": "Choose founders, key_people or professionals. Use title only for company key-person records, and roles/skills/experience/seniority only for professionals. Page within the selected group and request contacts separately.",
        "fields": {"data.people": "Recorded people, not independently verified current employees. Professional cards have bounded skills and CV summaries.", "data.returned": "Number of delivered cards, not company headcount.", "data.excluded_unverified_affiliations": "Professional candidates removed because their recorded current company domain was absent or not an exact match.", "data.matched_observed_rows": "For key-person groups, count after local filtering within at most 100 observed records.", "data.next_page": "Continuation within the relevant source; can be present even if an exact-domain check removes all rows on this page.", "data.coverage": "Source status, partial state and affiliation limitations."},
        "observed": "The Microsoft example retains rich professional records but also source inconsistencies, including a retired-role label and an inverted experience date range. Separate Razorpay examples return two recorded founders and one CEO-designated key person.",
        "pitfall": "Professionals require both companies and people scopes. Highest career seniority does not establish the current role; source affiliation does not verify present employment. Team responses contain no emails or phone values.",
        "guide": "teams-people-data-api",
    },
}
