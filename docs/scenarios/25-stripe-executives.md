# Find Stripe professionals categorized as executives with exact domain affiliation.

[All 50 scenarios](README.md) · [Workflow guide](../guides/teams-people-data-api.md) · [Endpoint reference](../reference/get_company_team.md)

**POST `/v1/companies/team`** · MCP tool **`get_company_team`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 25-stripe-executives -->
```json
{
  "domain": "stripe.com",
  "group": "professionals",
  "roles": [
    "executive"
  ],
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.537481+00:00; HTTP **200**;
**qualified**, 0.33 seconds.
Local authenticated gateway with live configured read-only sources.

Recorded professional or key-person data; current roles and complete resumes are unverified; Coverage is explicitly bounded.

Founders and key people are company records; professionals are source profile cards filtered to an exact recorded company domain. Neither is a verified current employee roster. Keep update dates, excluded affiliations and partial flags. Highest career seniority can differ from a current role, and card count is not headcount.

The baseline was an unavailable operation registry check (no HTTP request), **unavailable**:
not_implemented. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 25-stripe-executives -->
```json
{
  "ok": true,
  "feature": "get_company_team",
  "data": {
    "domain": "stripe.com",
    "group": "professionals",
    "people": [
      {
        "id": "6a1d2c4d00edf351ec490d73",
        "name": "Matt Henderson",
        "headline": "Founder @ Stripe",
        "current_title": "Founder",
        "current_company": "Stripe",
        "current_company_domain": "stripe.com",
        "location": "london, United Kingdom",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c3c00edf351ec439145",
        "summary": "Before starting Rangespan, Matt worked at Amazon.com for 7 years, most recently as UK Director of Merchant Services, where he led the third party marketplace business and the WebStore software business.\n\nIn prior Amazon roles Matt was a category director and led a variety of func…",
        "people_types": [
          "Ex-Founder",
          "Angel Investor",
          "Currently Founder"
        ],
        "skills": [
          "e commerce",
          "product management",
          "management",
          "retail",
          "start ups",
          "business strategy",
          "entrepreneurship",
          "analytics"
        ],
        "education": [
          {
            "institution": "London Business School",
            "degree": "master of business administration",
            "years": ""
          },
          {
            "institution": "Massachusetts Institute Of Technology",
            "degree": "management",
            "years": ""
          },
          {
            "institution": "University Of Otago",
            "degree": "bachelors in economics",
            "years": ""
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Stripe",
            "years": "2010–present"
          },
          {
            "title": "Founder",
            "company": "Phoebe",
            "years": "2023–present"
          },
          {
            "title": "angel investor",
            "company": "tech start-ups",
            "years": "2014–present"
          }
        ],
        "linkedin_url": "http://linkedin.com/in/matthenderson",
        "twitter_url": "https://twitter.com/_matt_henderson",
        "scores": {
          "people_rank": 98.75,
          "founder_rank": 98.48,
          "executive_rank": 99.51,
          "investor_rank": 60.18,
          "college_rank": 99.66,
          "experience_rank": 98.48
        },
        "founder": {
          "num_founded": 1,
          "top_company": "Stripe"
        },
        "investor": {
          "num_investments": 1,
          "total_invested_usd": null
        },
        "contact_gated": true
      },
      {
        "id": "6a1d2c5700edf351ec4c6209",
        "name": "Ongki Kurniawan",
        "headline": "Founder @ Stripe",
        "current_title": "Founder",
        "current_company": "Stripe",
        "current_company_domain": "stripe.com",
        "location": "jakarta, Indonesia",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c5700edf351ec4c6209",
        "summary": "Result-oriented business executive with strong strategic, managerial, and operational experience in tech and telecommunication. Proven track record working in Indonesia and internationally in developing innovative growth strategies, maximizing corporate values, improving operatio…",
        "people_types": [
          "Currently Founder"
        ],
        "skills": [
          "strategy",
          "business development",
          "product management",
          "leadership",
          "management",
          "business strategy",
          "telecommunications",
          "mobile devices"
        ],
        "education": [
          {
            "institution": "Institut Teknologi Bandung",
            "degree": "Bachelor of Science",
            "years": "1991–1995"
          },
          {
            "institution": "Berkeley Haas",
            "degree": "Master of Business Administration",
            "years": ""
          },
          {
            "institution": "Harvard Business School",
            "degree": "leadership",
            "years": "2013–2013"
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Stripe",
            "years": "2010–present"
          },
          {
            "title": "Founder",
            "company": "SkorLife",
            "years": "2021–present"
          },
          {
            "title": "managing director, grabpay indonesia",
            "company": "grab",
            "years": "2017–2018"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/ongkikurniawan",
        "twitter_url": null,
        "scores": {
          "people_rank": 98.49,
          "founder_rank": 98.27,
          "executive_rank": 99.66,
          "investor_rank": null,
          "college_rank": 96.2,
          "experience_rank": 99.46
        },
        "founder": {
          "num_founded": 2,
          "top_company": "SkorLife"
        },
        "investor": null,
        "contact_gated": true
      },
      {
        "id": "6a1d2c3700edf351ec41fd39",
        "name": "Colin Kennedy",
        "headline": "Founder @ Stripe",
        "current_title": "Founder",
        "current_company": "Stripe",
        "current_company_domain": "stripe.com",
        "location": "New York, United States",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c3700edf351ec41fd39",
        "summary": "Proven Fortune 500 (Goldman Sachs & Amex) and startup (Clarity Money & Stripe) COO/CRO expert in growing nascent and established businesses, with a deep focus on payments and consumer/SMB FinTech. Passionate about both the \"Fin\" and the \"Tech\" in FinTech. Working with an amazing…",
        "people_types": [
          "Ex-Founder"
        ],
        "skills": [
          "product management",
          "business development",
          "business strategy",
          "strategic partnerships",
          "marketing strategy",
          "product marketing",
          "leadership",
          "strategic planning"
        ],
        "education": [
          {
            "institution": "The Hotchkiss School",
            "degree": "",
            "years": "1990–1993"
          },
          {
            "institution": "Harvard University",
            "degree": "bachelors in economics",
            "years": "1993–1997"
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Stripe",
            "years": "2010–present"
          },
          {
            "title": "Founder",
            "company": "Ramp",
            "years": "2019–present"
          },
          {
            "title": "managing director and chief operations officer and cro, marcus by goldman sachs",
            "company": "goldman sachs",
            "years": "2018–2019"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/colinkennedypartnerships",
        "twitter_url": null,
        "scores": {
          "people_rank": 97.62,
          "founder_rank": 97.3,
          "executive_rank": 99.65,
          "investor_rank": null,
          "college_rank": 96.2,
          "experience_rank": 99.74
        },
        "founder": {
          "num_founded": 2,
          "top_company": "Ramp"
        },
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
    "retrieved_at": "2026-09-23T03:35:32.537202+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/25-stripe-executives.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
