# Company teams, founders and professional people data API

Radar has both company key-person records and professional profiles. Use the
company team endpoint to retrieve one kind explicitly. It does not merge unrelated
people with the same company name or expose contact details inside a team response.

## Select the right team group

| Group | Evidence and useful fields | Appropriate interpretation |
|---|---|---|
| `founders` | Company key-person records whose designation includes founder | Recorded founders; not a verified current executive roster |
| `key_people` | Company-associated names and designations | Named leadership records; not all employees |
| `professionals` | Recorded company domain, title, skills, education, experience, professional links and ranking fields | A source professional profile affiliated with the exact domain; not verified current employment |

All three use **`POST /v1/companies/team`**, MCP `get_company_team`. Choose `group`
explicitly. The key needs `companies`; professional profiles additionally need
`people`. Use [API-key onboarding](api-keys-authentication.md) to select those scopes.

## Founders and leadership, with real returned rows

```json
{"domain":"razorpay.com","group":"founders","limit":5}
```

The executed [Razorpay founders example](../scenarios/21-razorpay-founders.md)
returned Shashank Kumar, Co-Founder & Managing Director, and Harshil Mathur,
Co-Founder & CEO. The source update timestamp was June 1, 2026; retrieval in
September does not make the underlying roles newly verified.

```json
{"domain":"razorpay.com","group":"key_people","title":"CEO","limit":5}
```

`title` is a case-insensitive substring filter on the recorded key-person
designation. It is supported for founders and key people, and rejected for
professionals because the underlying professional search has no equivalent title
predicate. [Stripe leadership](../scenarios/22-stripe-leadership.md) and
[Swiggy leadership](../scenarios/23-swiggy-leadership.md) retain their different
record shapes and returned names; sparse fields are not padded with invented CVs.

Key-person paging is over at most 100 observed records returned by the selected
company field. `matched_observed_rows` counts that bounded set after title filtering.
It is not employee headcount or a count of every executive ever associated with the
company. A partial field response remains partial even when its last observed page
has no continuation.

## Professional teams with exact domain matching

```json
{"domain":"microsoft.com","group":"professionals","limit":3}
```

```json
{"domain":"stripe.com","group":"professionals","roles":["executive"],"limit":3}
```

The source people search accepts a company-name/domain prefix. The team endpoint
adds an exact normalized `current_company_domain` check, so a profile from
`example.com.other-domain.test` cannot enter the `example.com` team. Profiles with
only an unresolved company name are excluded and counted in
`excluded_unverified_affiliations`. Source pagination continues even when that
check removes all candidates from a page.

The [Microsoft profile capture](../scenarios/24-microsoft-team.md) includes skills,
education, experience, professional links, source ranking scores and founder
attributes. One profile explicitly says “Researcher Emeritus (ret)”; another has
an inconsistent experience date range. Exact recorded affiliation does not prove
present employment or resolve contradictory source dates. Keep these source values
visible for review and do not advertise this endpoint as a live employee directory.

Professional cards contain at most eight skills, three education entries and three
experience summaries from the source. These are useful research details, not full
resumes. `min_seniority` is highest recorded career seniority, not necessarily the
current role. `roles` is a source role classification. Neither a high founder score
nor a past executive role proves that a person currently holds an executive post.

## Search across people, then join accepted identities

```json
{"roles":["founder"],"schools":["Stanford"],"limit":3}
```

Send this body to **`POST /v1/people/search`**, MCP `search_people`, rather than the
team endpoint. [Examples 27–30](../scenarios/README.md) cover founder education,
Python skills, minimum experience and Indian senior executives. Get suggestion
values through `people_filter_options` before building a filter UI. Company-wide
headcount should come from an explicitly labelled company measure, not the length
of one people-search page or an approximate source total.

## Emails, phone numbers and richer company context

`has_email` / `has_phone` and `contact_gated` are availability or access signals.
They are not contact values. Use the separately scoped
[company and person contact endpoints](../CONTACTS.md), with the returned person
ID or company domain, for an explicit `emails` or `phones` request. The linked Radar
plan and contact limits still apply. Creating another key does not create another
contact quota.

For the company itself, first retrieve its identity and available fields, then
request classification, technology, web presence, hiring or other sections using
`get_company_field`. See [company data depth](../COMPANY_DATA_DEPTH.md),
[technology and traffic](technology-traffic-data-api.md), and the
[team endpoint reference](../reference/get_company_team.md) for the full contract.

<!-- scenario-links -->
## Executed scenarios for this workflow

- [21-razorpay-founders: Retrieve Razorpay’s recorded founders with role descriptions.](../scenarios/21-razorpay-founders.md)
- [22-stripe-leadership: Retrieve Stripe’s recorded key people and designations.](../scenarios/22-stripe-leadership.md)
- [23-swiggy-leadership: Retrieve Swiggy’s recorded key people and their roles.](../scenarios/23-swiggy-leadership.md)
- [24-microsoft-team: Retrieve professional records with an exact current-company domain of microsoft.com.](../scenarios/24-microsoft-team.md)
- [25-stripe-executives: Find Stripe professionals categorized as executives with exact domain affiliation.](../scenarios/25-stripe-executives.md)
- [26-razorpay-chief: Find Razorpay key people whose recorded designation contains CEO.](../scenarios/26-razorpay-chief.md)
- [27-founder-education: Find founders who studied at Stanford University.](../scenarios/27-founder-education.md)
- [28-professional-skills: Find Microsoft-associated professionals with Python skills.](../scenarios/28-professional-skills.md)
- [29-professional-experience: Find Microsoft-associated professionals with at least ten years of experience.](../scenarios/29-professional-experience.md)
- [30-india-senior-executives: Find India-based executives whose highest recorded seniority is director or above.](../scenarios/30-india-senior-executives.md)

## From team cards to founder or employee contacts

Use the [founder contact workflow](founder-contact-data-api.md) to cross-check a
company founder name against a professional record before selecting a contact ID.
Live source views can disagree: an exact recorded domain plus a founder role tag
is not independent proof that the person founded the company. Preserve unresolved
or ambiguous links rather than substituting the first name match.

For employee/professional email workflows, retrieve accepted team members and
request each person's selected contact types separately. The
[company email/phone guide](company-email-phone-api.md) explains company mailbox
fallback and why person-level source association does not establish work-email
verification. [Social references](linkedin-social-data-api.md) remain separate
recorded URLs, not contact-reveal fields.

<!-- captured-workflow -->
## Read the full captured professional team cards

All three captured cards and their structured education, skill and experience rows are retained. These are source professional records, including retired-role and date inconsistencies; do not convert them into a verified current headcount. Compare the founders and key-person scenarios for the separate company-record view.

## Worked example: live gateway response

The request captured for this example was **`POST /v1/companies/team`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: get_company_team -->
```json
{
  "domain": "microsoft.com",
  "group": "professionals",
  "limit": 3
}
```

<!-- response-example: get_company_team -->
```json
{
  "ok": true,
  "feature": "get_company_team",
  "data": {
    "domain": "microsoft.com",
    "group": "professionals",
    "people": [
      {
        "id": "6a1d2cda5e131005f7e2c536",
        "name": "Gordon Bell",
        "headline": "Researcher Emeritus (ret) @ Microsoft",
        "current_title": "Researcher Emeritus (ret)",
        "current_company": "Microsoft",
        "current_company_domain": "microsoft.com",
        "location": "San Francisco, United States",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2cda5e131005f7e2c536",
        "summary": "The Computer Museum was opened at a closet at Digital Equipment Corp Maynard MA headquarters in 1975. It move to Marlboro MA in 1979 and opened in Boston in 1983. It moved to Silicon Valley in 1995 where it became the Computer History Museum,1401 Shoreline Blvd., Mountain View, C…",
        "people_types": [],
        "skills": [
          "cloud computing",
          "start ups",
          "high performance computing",
          "networking",
          "business strategy",
          "distributed systems",
          "strategic partnerships",
          "computer science"
        ],
        "education": [
          {
            "institution": "Worcester Polytechnic Institute",
            "degree": "engineering",
            "years": "1993–1993"
          },
          {
            "institution": "Massachusetts Institute Of Technology",
            "degree": "electrical engineering",
            "years": "1956–1957"
          },
          {
            "institution": "Carnegie Mellon University",
            "degree": "computer science",
            "years": "2010–2010"
          }
        ],
        "top_experience": [
          {
            "title": "Researcher Emeritus (ret)",
            "company": "Microsoft",
            "years": "2015–2012"
          },
          {
            "title": "researcher at microsoft",
            "company": "gordon bell@large",
            "years": "2015–present"
          },
          {
            "title": "board member",
            "company": "tti/vanguard",
            "years": "1994–present"
          }
        ],
        "linkedin_url": "https://www.linkedin.com/in/gordon-bell-3035b43",
        "twitter_url": null,
        "scores": {
          "people_rank": 99.49,
          "founder_rank": 98.9,
          "executive_rank": 100.0,
          "investor_rank": null,
          "college_rank": 99.66,
          "experience_rank": 99.92
        },
        "founder": {
          "num_founded": 1,
          "top_company": "Computer History"
        },
        "investor": null,
        "contact_gated": true
      },
      {
        "id": "6a1d2c3700edf351ec420ccb",
        "name": "Bobby Yerramilli-Rao",
        "headline": "Founder @ Microsoft HoloLens",
        "current_title": "Founder",
        "current_company": "Microsoft HoloLens",
        "current_company_domain": "microsoft.com",
        "location": "London, United States",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c3700edf351ec420ccb",
        "summary": "I enjoy the application of science and technology to business problems that matter to lots of people. I am co-founder and managing partner of Fusion Global Capital (formerly Hermes Growth Partners) which invests from a growth equity fund into technology companies that improve ent…",
        "people_types": [
          "Ex-Founder",
          "Currently Founder"
        ],
        "skills": [
          "strategy",
          "business strategy",
          "mergers and acquisitions",
          "private equity",
          "investments"
        ],
        "education": [
          {
            "institution": "Amridge University",
            "degree": "Electrical And Information Sciences Tripos",
            "years": ""
          },
          {
            "institution": "University Of Cambridge",
            "degree": "electronics engineering",
            "years": "1985–1988"
          },
          {
            "institution": "University Of Oxford",
            "degree": "doctorates in electrical engineering",
            "years": "1988–1991"
          }
        ],
        "top_experience": [
          {
            "title": "chief strategy officer",
            "company": "microsoft",
            "years": "2020–present"
          },
          {
            "title": "Founder",
            "company": "Microsoft HoloLens",
            "years": "2010–present"
          },
          {
            "title": "co-founder and managing partner",
            "company": "fusion global capital",
            "years": "2018–present"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/bobby-yerramilli-rao-93b01027",
        "twitter_url": null,
        "scores": {
          "people_rank": 99.24,
          "founder_rank": 98.89,
          "executive_rank": 100.0,
          "investor_rank": null,
          "college_rank": 98.98,
          "experience_rank": 99.96
        },
        "founder": {
          "num_founded": 2,
          "top_company": "Biomodal"
        },
        "investor": null,
        "contact_gated": true
      },
      {
        "id": "6a1d2d1d5e131005f7e63455",
        "name": "Mike Flannagan",
        "headline": "vice president @ microsoft",
        "current_title": "vice president",
        "current_company": "microsoft",
        "current_company_domain": "microsoft.com",
        "location": "Austin, United States",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2d1d5e131005f7e63455",
        "summary": "Senior executive with an entrepreneurial background and track record of delivering P&L results, growing top-line revenue and executing M&A transactions. Functional expertise in setting and executing business strategy, leading product management, product marketing, go-to-market st…",
        "people_types": [],
        "skills": [
          "managed services",
          "product management",
          "cisco technologies",
          "cloud computing",
          "strategic partnerships",
          "product marketing",
          "enterprise software",
          "go to market strategy"
        ],
        "education": [
          {
            "institution": "University Of Central Lancashire",
            "degree": "bachelors",
            "years": ""
          },
          {
            "institution": "Stanford University",
            "degree": "",
            "years": "2019–2019"
          },
          {
            "institution": "The University Of Texas At San Antonio",
            "degree": "business administration",
            "years": "1994–1997"
          }
        ],
        "top_experience": [
          {
            "title": "vice president",
            "company": "microsoft",
            "years": "2020–present"
          },
          {
            "title": "member, board of directors",
            "company": "data coalition",
            "years": "2018–present"
          },
          {
            "title": "advisory council member",
            "company": "mccombs school of business, the university of texas at austin",
            "years": "2018–present"
          }
        ],
        "linkedin_url": "https://www.linkedin.com/in/mikeflannagan",
        "twitter_url": "https://twitter.com/mikeflannagan",
        "scores": {
          "people_rank": 99.23,
          "founder_rank": null,
          "executive_rank": 99.99,
          "investor_rank": null,
          "college_rank": 98.11,
          "experience_rank": 99.47
        },
        "founder": null,
        "investor": null,
        "contact_gated": true
      }
    ],
    "returned": 3,
    "page": 0,
    "next_page": 1,
    "source_candidates": 3,
    "excluded_unverified_affiliations": 0,
    "access": {},
    "coverage": {
      "complete": false,
      "partial": false,
      "affiliation": "Exact recorded current-company domain; not independently verified current employment",
      "note": "Search cards contain bounded skills, education and experience summaries. Page totals are not company headcount."
    }
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:32.296730+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T03:35:32.297001+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_team.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Microsoft example retains rich professional records but also source inconsistencies, including a retired-role label and an inverted experience date range. Separate Razorpay examples return two recorded founders and one CEO-designated key person.

See the [complete get_company_team endpoint reference](../reference/get_company_team.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
