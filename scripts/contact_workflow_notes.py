"""Typed customer recipes and evidence choices; no invented contact capabilities."""
VARIANTS = []


def add(key, question, operation, request, scopes, interpretation):
    VARIANTS.append({"id": key, "question": question, "operation": operation,
                     "request": request, "scopes": scopes, "interpretation": interpretation,
                     "evidence_level": "schema_validated_recipe; not a live execution claim"})


add("company-identity", "Inspect company identity and stored contact availability", "get_company", {"domain": "razorpay.com"}, ["companies"], "Availability is not contact access or current deliverability.")
add("company-email", "Get company-associated email strings", "get_company_contacts", {"domain": "razorpay.com", "fields": ["emails"]}, ["contacts"], "Requires an entitled linked source account.")
add("company-phone", "Get company-associated phone strings", "get_company_contacts", {"domain": "razorpay.com", "fields": ["phones"]}, ["contacts"], "No mobile, department or WhatsApp verification is supplied.")
add("company-both", "Get both company contact types explicitly", "get_company_contacts", {"domain": "razorpay.com", "fields": ["emails", "phones"]}, ["contacts"], "Only company attribution, not every employee's contact.")
add("company-social", "Get company LinkedIn metrics, stored posts and social links", "get_company_field", {"domain": "razorpay.com", "field": "social", "item_limit": 100}, ["companies"], "Dated followers, observed headcount, snapshots and stored posts remain separate from email/phone retrieval.")
add("company-people", "Get founder names, designations and source background flags", "get_company_field", {"domain": "razorpay.com", "field": "people", "item_limit": 100}, ["companies"], "Names and background flags are not professional IDs or per-person CV evidence.")
add("founders", "Get only recorded company founders", "get_company_team", {"domain": "razorpay.com", "group": "founders", "limit": 10}, ["companies"], "Recorded designation selection, not independently verified founders.")
add("chief-executive", "Filter company key-person designations for CEO", "get_company_team", {"domain": "razorpay.com", "group": "key_people", "title": "CEO", "limit": 5}, ["companies"], "Title substring filter applies to key_people/founders only.")
add("founder-profile", "Find the professional record for a named company founder", "search_people", {"name": "Shashank Kumar", "companies": ["razorpay.com"], "limit": 3}, ["people"], "Inspect name, exact recorded domain and professional references before selecting an ID.")
add("founder-role-team", "Discover founder-tagged professional candidates for a company", "get_company_team", {"domain": "razorpay.com", "group": "professionals", "roles": ["founder"], "limit": 3}, ["companies", "people"], "Source founder tags can disagree with company founder records.")
add("company-professionals", "Retrieve exactly affiliated professional cards", "get_company_team", {"domain": "microsoft.com", "group": "professionals", "limit": 5, "page": 0}, ["companies", "people"], "Recorded exact affiliation, not verified current employee roster.")
add("executives", "Retrieve executive-tagged professional candidates", "get_company_team", {"domain": "stripe.com", "group": "professionals", "roles": ["executive"], "limit": 5}, ["companies", "people"], "Source role classification; inspect the current title separately.")
add("board", "Discover board-role candidates by company", "search_people", {"companies": ["microsoft.com"], "roles": ["board"], "limit": 5}, ["people"], "People company predicate is prefix-based; review exact domain.")
add("python-professionals", "Retrieve company professionals with recorded Python skills", "get_company_team", {"domain": "microsoft.com", "group": "professionals", "skills": ["Python"], "limit": 5}, ["companies", "people"], "Returned cards expose bounded skill summaries.")
add("experienced-professionals", "Retrieve professionals with at least ten recorded years of experience", "get_company_team", {"domain": "microsoft.com", "group": "professionals", "min_experience_years": 10, "limit": 5}, ["companies", "people"], "Recorded career measure, not ten years at this company.")
add("senior-executives", "Retrieve director-or-higher career-seniority executive candidates", "get_company_team", {"domain": "stripe.com", "group": "professionals", "roles": ["executive"], "min_seniority": "director", "limit": 5}, ["companies", "people"], "Highest career seniority, not necessarily current seniority.")
add("india-founders", "Discover founder-tagged people in India", "search_people", {"roles": ["founder"], "locations": ["India"], "limit": 5}, ["people"], "Location is a source professional attribute; not nationality or company incorporation.")
add("founder-school", "Discover founders with recorded institution association", "search_people", {"roles": ["founder"], "schools": ["Indian Institute of Technology Roorkee"], "limit": 5}, ["people"], "Use canonical institution suggestions and inspect the returned education entries.")
add("degree-search", "Discover company people by recorded degree text", "search_people", {"companies": ["microsoft.com"], "degrees": ["Computer Science"], "limit": 5}, ["people"], "Degree/major source matching, not degree verification.")
add("people-vocabulary", "Find accepted school suggestion values", "people_filter_options", {"field": "schools", "q": "Roorkee", "limit": 5}, ["people"], "Use the same field in the subsequent discovery request.")
add("person-email", "Request emails for an accepted professional ID", "get_person_contacts", {"person_id": "ID_FROM_ACCEPTED_PROFILE", "fields": ["emails"]}, ["contacts"], "Replace the placeholder. Source person versus company fallback is part of the result.")
add("person-phone", "Request phones for an accepted professional ID", "get_person_contacts", {"person_id": "ID_FROM_ACCEPTED_PROFILE", "fields": ["phones"]}, ["contacts"], "A returned string does not certify a mobile or direct line.")
add("person-both", "Request both permitted contact types for an accepted profile", "get_person_contacts", {"person_id": "ID_FROM_ACCEPTED_PROFILE", "fields": ["emails", "phones"]}, ["contacts"], "One person per request; no bulk list input.")
add("professional-next-page", "Continue the same professional-team query", "get_company_team", {"domain": "stripe.com", "group": "professionals", "roles": ["executive"], "limit": 5, "page": 1}, ["companies", "people"], "Keep the original filters and page size. A page is not the full roster.")
assert len(VARIANTS) == 24

# These JSON blocks are rendered verbatim and checked against their source files.
CONTACT_EVIDENCE = [
    ("Founder professional details: real discovery", "contacts/founder-shashank.json"),
    ("Company social data: followers, headcount and stored posts", "fields/razorpay.com-social.json"),
    ("Default-key contact denial: live gateway capture", "get_company_contacts.json"),
    ("Company emails only: executed fictional fixture", "contacts/company-email-only.json"),
    ("Company phones only: executed fictional fixture", "contacts/company-phone-only.json"),
    ("Direct person association: executed fictional fixture", "contacts/person-direct.json"),
    ("Company mailbox fallback: executed fictional fixture", "contacts/person-company-fallback.json"),
    ("Phone exists but email-only lookup is empty: fictional fixture", "contacts/person-phone-only-source.json"),
    ("No contact returned: executed fictional fixture", "contacts/person-no-data.json"),
    ("Unknown source label: executed fictional fixture", "contacts/person-unknown-origin.json"),
    ("Source plan denial with values suppressed: fictional fixture", "contacts/paid-plan-denial.json"),
]
GUIDE_EVIDENCE = {
    "founder-contact-data-api": [
        ("Company founder names", "fields/razorpay.com-people.json"),
        ("Resolved professional candidate", "contacts/founder-shashank.json"),
        ("A founder name with no matching professional row", "contacts/founder-professional.json"),
        ("Source founder-role candidates requiring reconciliation", "contacts/founder-team.json"),
    ],
    "company-email-phone-api": [
        ("Company email-only projection: fictional fixture", "contacts/company-email-only.json"),
        ("Company phone-only projection: fictional fixture", "contacts/company-phone-only.json"),
        ("Employee lookup that returns a company mailbox: fictional fixture", "contacts/person-company-fallback.json"),
    ],
    "linkedin-social-data-api": [
        ("Company LinkedIn profile, metrics, snapshots and stored posts", "fields/razorpay.com-social.json"),
        ("Person LinkedIn/X references and professional detail", "contacts/founder-shashank.json"),
    ],
}
