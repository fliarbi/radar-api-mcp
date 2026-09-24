# Find Microsoft-associated professionals with Python skills.

[All 50 scenarios](README.md) · [Workflow guide](../guides/teams-people-data-api.md) · [Endpoint reference](../reference/search_people.md)

**POST `/v1/people/search`** · MCP tool **`search_people`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 people; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 28-professional-skills -->
```json
{
  "companies": [
    "Microsoft"
  ],
  "skills": [
    "Python"
  ],
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.761703+00:00; HTTP **200**;
**qualified**, 0.22 seconds.
Local authenticated gateway with live configured read-only sources.

Recorded professional or key-person data; current roles and complete resumes are unverified.

Source people cards retain skills, education, experience and professional rankings. Skills and CV arrays are bounded source summaries; an omitted skill can be elsewhere in a full source profile. Highest seniority is a career attribute. Company-name/domain search is prefix-based; use get_company_team for an exact-domain affiliation check. Contact values require a separate scoped endpoint.

The baseline was HTTP 200, **qualified**:
Recorded professional or key-person data; current roles and complete resumes are unverified. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 28-professional-skills -->
```json
{
  "ok": true,
  "feature": "search_people",
  "data": {
    "people": [
      {
        "id": "6a1d2c4800edf351ec474d18",
        "name": "Aditya Ketkar",
        "headline": "Founder @ Microsoft's Powerapps",
        "current_title": "Founder",
        "current_company": "Microsoft's Powerapps",
        "current_company_domain": "microsoft.com",
        "location": "noida, India",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c4800edf351ec474d18",
        "summary": "I’m a Computer Science major by day, a professional Table Tennis player by evening, a functional wantrepreneur hunting for market gaps by midnight and a hustler always. If you can’t find me, it’s because I’m already cycling or hiking, off to a tournament, or studying for an exam!…",
        "people_types": [
          "Currently Founder"
        ],
        "skills": [
          "table tennis",
          "python",
          "java",
          "ultimate frisbee",
          "c"
        ],
        "education": [
          {
            "institution": "Harvard University",
            "degree": "",
            "years": ""
          },
          {
            "institution": "University of Cambridge",
            "degree": "BA",
            "years": ""
          },
          {
            "institution": "Birla Institute Of Technology And Science, Pilani - Goa Campus",
            "degree": "bachelor of engineering in computer science",
            "years": "2016–2020"
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Microsoft's Powerapps",
            "years": "2001–present"
          },
          {
            "title": "teaching assistant",
            "company": "interviewbit",
            "years": "2019–present"
          },
          {
            "title": "Founder",
            "company": "Broccoli AI",
            "years": "1995–present"
          }
        ],
        "linkedin_url": "https://www.linkedin.com/in/adityaketkar/",
        "twitter_url": null,
        "scores": {
          "people_rank": 98.62,
          "founder_rank": 98.5,
          "executive_rank": 99.96,
          "investor_rank": null,
          "college_rank": 98.98,
          "experience_rank": 99.19
        },
        "founder": {
          "num_founded": 2,
          "top_company": "Microsoft's Powerapps"
        },
        "investor": null,
        "contact_gated": true
      },
      {
        "id": "6a1d2c3a00edf351ec42fdab",
        "name": "Gil Shulman",
        "headline": "Founder @ Microsoft's Powerapps",
        "current_title": "Founder",
        "current_company": "Microsoft's Powerapps",
        "current_company_domain": "microsoft.com",
        "location": "Seattle, United States",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c3a00edf351ec42fdab",
        "summary": "I help train machine learning models for email ranking and classification to help users with Email Triage. Prior to that I worked on vector representation of products at Amazon (Embeddings) and on goal-oriented, restricted domain conversational agents. I am a tech product manager…",
        "people_types": [
          "Ex-Founder",
          "Currently Founder"
        ],
        "skills": [
          "entrepreneurship",
          "product management",
          "strategy",
          "mergers and acquisitions",
          "valuation",
          "business strategy",
          "corporate finance",
          "venture capital"
        ],
        "education": [
          {
            "institution": "University of Pennsylvania",
            "degree": "MBA",
            "years": "2006–2008"
          },
          {
            "institution": "The Wharton School",
            "degree": "master of business administration",
            "years": "2006–2008"
          },
          {
            "institution": "Bar - Ilan University",
            "degree": "bachelors",
            "years": ""
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Microsoft's Powerapps",
            "years": "2001–present"
          },
          {
            "title": "Founder",
            "company": "ficc",
            "years": "2020–present"
          },
          {
            "title": "advisor",
            "company": "chargeitspot",
            "years": "2012–present"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/gilshulman",
        "twitter_url": null,
        "scores": {
          "people_rank": 98.23,
          "founder_rank": 97.94,
          "executive_rank": 99.98,
          "investor_rank": null,
          "college_rank": 93.82,
          "experience_rank": 99.65
        },
        "founder": {
          "num_founded": 2,
          "top_company": "ficc"
        },
        "investor": null,
        "contact_gated": true
      },
      {
        "id": "6a1d2c4900edf351ec479700",
        "name": "Alana Marzoev",
        "headline": "Founder @ Microsoft's Powerapps",
        "current_title": "Founder",
        "current_company": "Microsoft's Powerapps",
        "current_company_domain": "microsoft.com",
        "location": "New York, United States",
        "gender_t5": "female",
        "image_url": "/people_logo?id=6a1d2c4900edf351ec479700",
        "summary": "Readyset, ex-Readyset Technology, ex-Massachusetts Institute Of Technology, Cornell University",
        "people_types": [
          "Currently Founder"
        ],
        "skills": [
          "python",
          "leadership",
          "java",
          "discrete mathematics",
          "object oriented design",
          "public speaking",
          "social media",
          "ruby on rails"
        ],
        "education": [
          {
            "institution": "Massachusetts Institute Of Technology",
            "degree": "doctorates in philosophy",
            "years": "2018–?"
          },
          {
            "institution": "Moorestown Friends School",
            "degree": "",
            "years": "2010–2014"
          },
          {
            "institution": "Cornell University",
            "degree": "bachelors in computer science",
            "years": "2014–2018"
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Microsoft's Powerapps",
            "years": "2001–2018"
          },
          {
            "title": "Founder",
            "company": "ReadySet",
            "years": "2018–present"
          },
          {
            "title": "ai + computer systems researcher",
            "company": "cornell university college of engineering",
            "years": "2017–2018"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/alanamarzoev",
        "twitter_url": null,
        "scores": {
          "people_rank": 98.05,
          "founder_rank": 98.29,
          "executive_rank": 99.92,
          "investor_rank": null,
          "college_rank": 99.66,
          "experience_rank": 98.3
        },
        "founder": {
          "num_founded": 2,
          "top_company": "ReadySet"
        },
        "investor": null,
        "contact_gated": true
      }
    ],
    "total_estimate": 329,
    "total_capped": false,
    "access": {
      "plan": "free",
      "results_per_query": 50,
      "searches_per_month": 50,
      "anonymous": true
    },
    "plan": "free",
    "searches_remaining": 50,
    "page": 0,
    "page_size": 3,
    "partial_timeout": false
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:32.761428+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/28-professional-skills.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
