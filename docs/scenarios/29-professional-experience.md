# Find Microsoft-associated professionals with at least ten years of experience.

[All 50 scenarios](README.md) · [Workflow guide](../guides/teams-people-data-api.md) · [Endpoint reference](../reference/search_people.md)

**POST `/v1/people/search`** · MCP tool **`search_people`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 people; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 29-professional-experience -->
```json
{
  "companies": [
    "Microsoft"
  ],
  "min_experience_years": 10,
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.805956+00:00; HTTP **200**;
**qualified**, 0.04 seconds.
Local authenticated gateway with live configured read-only sources.

Recorded professional or key-person data; current roles and complete resumes are unverified.

Source people cards retain skills, education, experience and professional rankings. Skills and CV arrays are bounded source summaries; an omitted skill can be elsewhere in a full source profile. Highest seniority is a career attribute. Company-name/domain search is prefix-based; use get_company_team for an exact-domain affiliation check. Contact values require a separate scoped endpoint.

The baseline was HTTP 200, **qualified**:
Recorded professional or key-person data; current roles and complete resumes are unverified. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 29-professional-experience -->
```json
{
  "ok": true,
  "feature": "search_people",
  "data": {
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
    "total_estimate": 1429,
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
    "retrieved_at": "2026-09-23T03:35:32.805729+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/29-professional-experience.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
