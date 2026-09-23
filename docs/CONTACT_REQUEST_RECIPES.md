# Contact request recipes: founders, professionals, company emails and social links

These 24 request bodies validate against the current API models. They are accepted
syntax examples, not claims that every query was executed or returned results.
Replace `ID_FROM_ACCEPTED_PROFILE` with an ID you accepted from professional discovery.

Use your API key with each POST request. For MCP, call the named tool with
`arguments.request` set to the same JSON body. Contact requests additionally need
an entitled linked Radar account. See [contact access, output and errors](CONTACTS.md),
[founder identity and details](guides/founder-contact-data-api.md),
[company/professional emails](guides/company-email-phone-api.md), and
[LinkedIn/social references](guides/linkedin-social-data-api.md).

Real discovery responses and clearly labelled synthetic contact outputs are
preserved in those guides. [Download the machine-readable recipes](examples/contacts/requests.json).

## Inspect company identity and stored contact availability

**`POST /v1/companies/profile`** · MCP **`get_company`** ·
Required key scopes: `companies`.

<!-- contact-recipe: company-identity -->
```json
{
  "domain": "razorpay.com"
}
```

Availability is not contact access or current deliverability.

## Get company-associated email strings

**`POST /v1/contacts/company`** · MCP **`get_company_contacts`** ·
Required key scopes: `contacts`.

<!-- contact-recipe: company-email -->
```json
{
  "domain": "razorpay.com",
  "fields": [
    "emails"
  ]
}
```

Requires an entitled linked source account.

## Get company-associated phone strings

**`POST /v1/contacts/company`** · MCP **`get_company_contacts`** ·
Required key scopes: `contacts`.

<!-- contact-recipe: company-phone -->
```json
{
  "domain": "razorpay.com",
  "fields": [
    "phones"
  ]
}
```

No mobile, department or WhatsApp verification is supplied.

## Get both company contact types explicitly

**`POST /v1/contacts/company`** · MCP **`get_company_contacts`** ·
Required key scopes: `contacts`.

<!-- contact-recipe: company-both -->
```json
{
  "domain": "razorpay.com",
  "fields": [
    "emails",
    "phones"
  ]
}
```

Only company attribution, not every employee's contact.

## Get company LinkedIn metrics, stored posts and social links

**`POST /v1/companies/field`** · MCP **`get_company_field`** ·
Required key scopes: `companies`.

<!-- contact-recipe: company-social -->
```json
{
  "domain": "razorpay.com",
  "field": "social",
  "item_limit": 100
}
```

Dated followers, observed headcount, snapshots and stored posts remain separate from email/phone retrieval.

## Get founder names, designations and source background flags

**`POST /v1/companies/field`** · MCP **`get_company_field`** ·
Required key scopes: `companies`.

<!-- contact-recipe: company-people -->
```json
{
  "domain": "razorpay.com",
  "field": "people",
  "item_limit": 100
}
```

Names and background flags are not professional IDs or per-person CV evidence.

## Get only recorded company founders

**`POST /v1/companies/team`** · MCP **`get_company_team`** ·
Required key scopes: `companies`.

<!-- contact-recipe: founders -->
```json
{
  "domain": "razorpay.com",
  "group": "founders",
  "limit": 10
}
```

Recorded designation selection, not independently verified founders.

## Filter company key-person designations for CEO

**`POST /v1/companies/team`** · MCP **`get_company_team`** ·
Required key scopes: `companies`.

<!-- contact-recipe: chief-executive -->
```json
{
  "domain": "razorpay.com",
  "group": "key_people",
  "title": "CEO",
  "limit": 5
}
```

Title substring filter applies to key_people/founders only.

## Find the professional record for a named company founder

**`POST /v1/people/search`** · MCP **`search_people`** ·
Required key scopes: `people`.

<!-- contact-recipe: founder-profile -->
```json
{
  "name": "Shashank Kumar",
  "companies": [
    "razorpay.com"
  ],
  "limit": 3
}
```

Inspect name, exact recorded domain and professional references before selecting an ID.

## Discover founder-tagged professional candidates for a company

**`POST /v1/companies/team`** · MCP **`get_company_team`** ·
Required key scopes: `companies`, `people`.

<!-- contact-recipe: founder-role-team -->
```json
{
  "domain": "razorpay.com",
  "group": "professionals",
  "roles": [
    "founder"
  ],
  "limit": 3
}
```

Source founder tags can disagree with company founder records.

## Retrieve exactly affiliated professional cards

**`POST /v1/companies/team`** · MCP **`get_company_team`** ·
Required key scopes: `companies`, `people`.

<!-- contact-recipe: company-professionals -->
```json
{
  "domain": "microsoft.com",
  "group": "professionals",
  "limit": 5,
  "page": 0
}
```

Recorded exact affiliation, not verified current employee roster.

## Retrieve executive-tagged professional candidates

**`POST /v1/companies/team`** · MCP **`get_company_team`** ·
Required key scopes: `companies`, `people`.

<!-- contact-recipe: executives -->
```json
{
  "domain": "stripe.com",
  "group": "professionals",
  "roles": [
    "executive"
  ],
  "limit": 5
}
```

Source role classification; inspect the current title separately.

## Discover board-role candidates by company

**`POST /v1/people/search`** · MCP **`search_people`** ·
Required key scopes: `people`.

<!-- contact-recipe: board -->
```json
{
  "companies": [
    "microsoft.com"
  ],
  "roles": [
    "board"
  ],
  "limit": 5
}
```

People company predicate is prefix-based; review exact domain.

## Retrieve company professionals with recorded Python skills

**`POST /v1/companies/team`** · MCP **`get_company_team`** ·
Required key scopes: `companies`, `people`.

<!-- contact-recipe: python-professionals -->
```json
{
  "domain": "microsoft.com",
  "group": "professionals",
  "skills": [
    "Python"
  ],
  "limit": 5
}
```

Returned cards expose bounded skill summaries.

## Retrieve professionals with at least ten recorded years of experience

**`POST /v1/companies/team`** · MCP **`get_company_team`** ·
Required key scopes: `companies`, `people`.

<!-- contact-recipe: experienced-professionals -->
```json
{
  "domain": "microsoft.com",
  "group": "professionals",
  "min_experience_years": 10,
  "limit": 5
}
```

Recorded career measure, not ten years at this company.

## Retrieve director-or-higher career-seniority executive candidates

**`POST /v1/companies/team`** · MCP **`get_company_team`** ·
Required key scopes: `companies`, `people`.

<!-- contact-recipe: senior-executives -->
```json
{
  "domain": "stripe.com",
  "group": "professionals",
  "roles": [
    "executive"
  ],
  "min_seniority": "director",
  "limit": 5
}
```

Highest career seniority, not necessarily current seniority.

## Discover founder-tagged people in India

**`POST /v1/people/search`** · MCP **`search_people`** ·
Required key scopes: `people`.

<!-- contact-recipe: india-founders -->
```json
{
  "roles": [
    "founder"
  ],
  "locations": [
    "India"
  ],
  "limit": 5
}
```

Location is a source professional attribute; not nationality or company incorporation.

## Discover founders with recorded institution association

**`POST /v1/people/search`** · MCP **`search_people`** ·
Required key scopes: `people`.

<!-- contact-recipe: founder-school -->
```json
{
  "roles": [
    "founder"
  ],
  "schools": [
    "Indian Institute of Technology Roorkee"
  ],
  "limit": 5
}
```

Use canonical institution suggestions and inspect the returned education entries.

## Discover company people by recorded degree text

**`POST /v1/people/search`** · MCP **`search_people`** ·
Required key scopes: `people`.

<!-- contact-recipe: degree-search -->
```json
{
  "companies": [
    "microsoft.com"
  ],
  "degrees": [
    "Computer Science"
  ],
  "limit": 5
}
```

Degree/major source matching, not degree verification.

## Find accepted school suggestion values

**`POST /v1/people/filter-options`** · MCP **`people_filter_options`** ·
Required key scopes: `people`.

<!-- contact-recipe: people-vocabulary -->
```json
{
  "field": "schools",
  "q": "Roorkee",
  "limit": 5
}
```

Use the same field in the subsequent discovery request.

## Request emails for an accepted professional ID

**`POST /v1/contacts/person`** · MCP **`get_person_contacts`** ·
Required key scopes: `contacts`.

<!-- contact-recipe: person-email -->
```json
{
  "person_id": "ID_FROM_ACCEPTED_PROFILE",
  "fields": [
    "emails"
  ]
}
```

Replace the placeholder. Source person versus company fallback is part of the result.

## Request phones for an accepted professional ID

**`POST /v1/contacts/person`** · MCP **`get_person_contacts`** ·
Required key scopes: `contacts`.

<!-- contact-recipe: person-phone -->
```json
{
  "person_id": "ID_FROM_ACCEPTED_PROFILE",
  "fields": [
    "phones"
  ]
}
```

A returned string does not certify a mobile or direct line.

## Request both permitted contact types for an accepted profile

**`POST /v1/contacts/person`** · MCP **`get_person_contacts`** ·
Required key scopes: `contacts`.

<!-- contact-recipe: person-both -->
```json
{
  "person_id": "ID_FROM_ACCEPTED_PROFILE",
  "fields": [
    "emails",
    "phones"
  ]
}
```

One person per request; no bulk list input.

## Continue the same professional-team query

**`POST /v1/companies/team`** · MCP **`get_company_team`** ·
Required key scopes: `companies`, `people`.

<!-- contact-recipe: professional-next-page -->
```json
{
  "domain": "stripe.com",
  "group": "professionals",
  "roles": [
    "executive"
  ],
  "limit": 5,
  "page": 1
}
```

Keep the original filters and page size. A page is not the full roster.
