# Find founders who studied at Stanford University.

[All 50 scenarios](README.md) · [Workflow guide](../guides/teams-people-data-api.md) · [Endpoint reference](../reference/search_people.md)

**POST `/v1/people/search`** · MCP tool **`search_people`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 people; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 27-founder-education -->
```json
{
  "roles": [
    "founder"
  ],
  "schools": [
    "Stanford University"
  ],
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.523767+00:00; HTTP **200**;
**qualified**, 1.217 seconds.
Local authenticated gateway with live configured read-only sources.

Recorded professional or key-person data; current roles and complete resumes are unverified.

Source people cards retain skills, education, experience and professional rankings. Skills and CV arrays are bounded source summaries; an omitted skill can be elsewhere in a full source profile. Highest seniority is a career attribute. Company-name/domain search is prefix-based; use get_company_team for an exact-domain affiliation check. Contact values require a separate scoped endpoint.

The baseline was HTTP 200, **qualified**:
Recorded professional or key-person data; current roles and complete resumes are unverified. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 27-founder-education -->
```json
{
  "ok": true,
  "feature": "search_people",
  "data": {
    "people": [
      {
        "id": "6a1d2c5a00edf351ec4d688a",
        "name": "Sangam Sangameswara",
        "headline": "Co-Founder & CEO @ RightSense",
        "current_title": "Co-Founder & CEO",
        "current_company": "RightSense",
        "current_company_domain": "rightsense.ai",
        "location": "Cupertino, United States",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c5a00edf351ec4d688a",
        "summary": "Executive with Business, Product & Technology Leadership Experiences with startups and large companies. \n\nExperience in software technologies for multiple domains: Cloud, Software-as-a-Service (SaaS), Big Data, Analytics, AI/ML/DL, Video Streaming, Blockchain, Online Advertisemen…",
        "people_types": [
          "Ex-Founder",
          "Currently Founder"
        ],
        "skills": [
          "cloud computing",
          "saas",
          "strategic partnerships",
          "start ups",
          "mobile applications",
          "entrepreneurship",
          "analytics",
          "mobile devices"
        ],
        "education": [
          {
            "institution": "University Of Illinois",
            "degree": "master of science in computer science",
            "years": ""
          },
          {
            "institution": "University Vishweshwaraya College Of Engineering",
            "degree": "bachelors in electronics engineering",
            "years": ""
          },
          {
            "institution": "Massachusetts Institute Of Technology",
            "degree": "data science",
            "years": "2014–2014"
          }
        ],
        "top_experience": [
          {
            "title": "Co-Founder & CEO",
            "company": "RightSense",
            "years": "?–present"
          },
          {
            "title": "co-founder and chief executive officer",
            "company": "rightsense",
            "years": "2018–present"
          },
          {
            "title": "member of the board",
            "company": "vigyanlabs",
            "years": "2014–present"
          }
        ],
        "linkedin_url": "http://linkedin.com/in/sgsangam",
        "twitter_url": "https://twitter.com/sgsangam",
        "scores": {
          "people_rank": 99.88,
          "founder_rank": 98.96,
          "executive_rank": 94.58,
          "investor_rank": null,
          "college_rank": 99.66,
          "experience_rank": 99.99
        },
        "founder": null,
        "investor": null,
        "contact_gated": true
      },
      {
        "id": "6a1d2c4700edf351ec4727b1",
        "name": "John Mathon",
        "headline": "chief executive officer @ agile stacks, inc",
        "current_title": "chief executive officer",
        "current_company": "agile stacks, inc",
        "current_company_domain": "",
        "location": "san mateo, United States",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c4700edf351ec4727b1",
        "summary": "I have been CEO, CTO, COB, VP Engineering, Board member, advisor to numerous companies. I have been in companies during 2 public offerings, 2 sales of companies to other companies.\n\n I invented publish/subscribe and have 10+ patents in messaging, security, content management, fil…",
        "people_types": [
          "Ex-Founder",
          "Currently Founder"
        ],
        "skills": [
          "enterprise software",
          "cloud computing",
          "saas",
          "enterprise architecture",
          "software development",
          "start ups",
          "agile methodologies",
          "integration"
        ],
        "education": [
          {
            "institution": "University Of Vermont",
            "degree": "",
            "years": ""
          },
          {
            "institution": "South Burlington High School",
            "degree": "",
            "years": ""
          },
          {
            "institution": "Stanford University",
            "degree": "physics",
            "years": "2011–2014"
          }
        ],
        "top_experience": [
          {
            "title": "chief executive officer",
            "company": "agile stacks, inc",
            "years": "?–present"
          },
          {
            "title": "Founder",
            "company": "SuperHub",
            "years": "2017–present"
          },
          {
            "title": "chief executive officer",
            "company": "agile stacks, inc",
            "years": "2016–present"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/jmathon",
        "twitter_url": "https://twitter.com/john_mathon",
        "scores": {
          "people_rank": 99.79,
          "founder_rank": 99.19,
          "executive_rank": 94.23,
          "investor_rank": null,
          "college_rank": 99.66,
          "experience_rank": 99.82
        },
        "founder": {
          "num_founded": 1,
          "top_company": "SuperHub"
        },
        "investor": null,
        "contact_gated": true
      },
      {
        "id": "6a1d2c3200edf351ec406e2d",
        "name": "Godard Abel",
        "headline": "Founder @ ThreeKit",
        "current_title": "Founder",
        "current_company": "ThreeKit",
        "current_company_domain": "threekit.com",
        "location": "Boulder, United States",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c3200edf351ec406e2d",
        "summary": "Entrepreneur delivering success to B2B technology buyers and vendors via our G2 review platform...and building ThreeKit into world's most amazing 3D visual selling platform. \n\nPreviously built cloud CPQ software pioneers BigMachines (acquired by Oracle) and SteelBrick (acquired b…",
        "people_types": [
          "Ex-Founder",
          "Currently Founder",
          "Angel Investor"
        ],
        "skills": [
          "saas",
          "enterprise software",
          "start ups",
          "salesforce.com",
          "entrepreneurship",
          "cloud computing",
          "business strategy",
          "strategic partnerships"
        ],
        "education": [
          {
            "institution": "MIT",
            "degree": "Bachelor of Science",
            "years": ""
          },
          {
            "institution": "MIT",
            "degree": "Master of Science",
            "years": ""
          },
          {
            "institution": "Stanford Graduate School of Business",
            "degree": "Master of Business Administration",
            "years": ""
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "ThreeKit",
            "years": "2005–present"
          },
          {
            "title": "Founder",
            "company": "BackFuture",
            "years": "2023–present"
          },
          {
            "title": "Founder",
            "company": "G2",
            "years": "2012–present"
          }
        ],
        "linkedin_url": "https://www.linkedin.com/in/godardabel/",
        "twitter_url": "https://twitter.com/godardabel",
        "scores": {
          "people_rank": 99.78,
          "founder_rank": 99.61,
          "executive_rank": 97.81,
          "investor_rank": 98.48,
          "college_rank": 99.66,
          "experience_rank": 99.84
        },
        "founder": {
          "num_founded": 3,
          "top_company": "BackFuture"
        },
        "investor": {
          "num_investments": 8,
          "total_invested_usd": null
        },
        "contact_gated": true
      }
    ],
    "total_estimate": 10000,
    "total_capped": true,
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
    "retrieved_at": "2026-09-23T03:35:33.523466+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/27-founder-education.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
