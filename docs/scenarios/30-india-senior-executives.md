# Find India-based executives whose highest recorded seniority is director or above.

[All 50 scenarios](README.md) · [Workflow guide](../guides/teams-people-data-api.md) · [Endpoint reference](../reference/search_people.md)

**POST `/v1/people/search`** · MCP tool **`search_people`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 30-india-senior-executives -->
```json
{
  "roles": [
    "executive"
  ],
  "locations": [
    "India"
  ],
  "min_seniority": "director",
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:32.873569+00:00; HTTP **200**;
**qualified**, 0.064 seconds.
Local authenticated gateway with live configured read-only sources.

Recorded professional or key-person data; current roles and complete resumes are unverified.

Source people cards retain skills, education, experience and professional rankings. Skills and CV arrays are bounded source summaries; an omitted skill can be elsewhere in a full source profile. Highest seniority is a career attribute. Company-name/domain search is prefix-based; use get_company_team for an exact-domain affiliation check. Contact values require a separate scoped endpoint.

The baseline was HTTP 200, **qualified**:
Recorded professional or key-person data; current roles and complete resumes are unverified. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 30-india-senior-executives -->
```json
{
  "ok": true,
  "feature": "search_people",
  "data": {
    "people": [
      {
        "id": "6a1d2c3100edf351ec3ffe42",
        "name": "Nishant Rao",
        "headline": "Founder @ Avataar Ventures",
        "current_title": "Founder",
        "current_company": "Avataar Ventures",
        "current_company_domain": "avataar.vc",
        "location": "Gurugram, India",
        "gender_t5": "male",
        "image_url": null,
        "summary": "Avataar is a growth stage, Operational VC fund partnering actively with brilliant regional Tech-led B2B & SaaS startups to Re-invent, Scale & Transform into successful, enduring global businesses. We believe in the promise of India & South-East Asia transforming into B2B product…",
        "people_types": [
          "Angel Investor"
        ],
        "skills": [
          "strategy",
          "business strategy",
          "business development",
          "product management",
          "leadership",
          "management",
          "entrepreneurship",
          "go to market strategy"
        ],
        "education": [
          {
            "institution": "MIT",
            "degree": "Mba",
            "years": ""
          },
          {
            "institution": "Delhi Public School, R.K.Puram",
            "degree": "",
            "years": "1994–1996"
          },
          {
            "institution": "Mit Sloan School Of Management",
            "degree": "master of business administration in entrepreneurship",
            "years": "2005–2007"
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Avataar Ventures",
            "years": "2019–present"
          },
          {
            "title": "board advisor",
            "company": "zeta india",
            "years": "2019–present"
          },
          {
            "title": "board member",
            "company": "capillary technologies",
            "years": "2019–present"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/nishantrao",
        "twitter_url": "https://twitter.com/nishrao",
        "scores": {
          "people_rank": 99.76,
          "founder_rank": 99.17,
          "executive_rank": 93.58,
          "investor_rank": 92.17,
          "college_rank": 99.66,
          "experience_rank": 99.76
        },
        "founder": {
          "num_founded": 1,
          "top_company": "Avataar Ventures"
        },
        "investor": {
          "num_investments": 5,
          "total_invested_usd": null
        },
        "contact_gated": true
      },
      {
        "id": "6a1d2c5c00edf351ec4dbdef",
        "name": "Ramana Rao",
        "headline": "senior director, experience cloud engineering @ adobe",
        "current_title": "senior director, experience cloud engineering",
        "current_company": "adobe",
        "current_company_domain": "adobe.com",
        "location": "san francisco, India",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c5c00edf351ec4dbdef",
        "summary": "Product and technology executive across ventures and large companies in consumer media, enterprise software, and intelligence applications Balanced mix of leadership, strategic, and execution accomplishments Raised $80M+ funding across four ventures as founder and/or exec. Partic…",
        "people_types": [
          "Ex-Founder",
          "Angel Investor"
        ],
        "skills": [
          "start ups",
          "search",
          "information visualization",
          "software development",
          "product development",
          "interaction design",
          "human computer interaction",
          "product management"
        ],
        "education": [
          {
            "institution": "Davy Crockett Elementary School",
            "degree": "",
            "years": ""
          },
          {
            "institution": "Massachusetts Institute Of Technology",
            "degree": "master of science in computer science",
            "years": ""
          }
        ],
        "top_experience": [
          {
            "title": "senior director, experience cloud engineering",
            "company": "adobe",
            "years": "2016–present"
          },
          {
            "title": "Founder",
            "company": "iCurrent",
            "years": "2006–2010"
          },
          {
            "title": "chief technology officer",
            "company": "livefyre",
            "years": "2013–2016"
          }
        ],
        "linkedin_url": "http://linkedin.com/in/ramanarao",
        "twitter_url": "https://twitter.com/treerao",
        "scores": {
          "people_rank": 99.62,
          "founder_rank": 99.57,
          "executive_rank": 100.0,
          "investor_rank": 62.28,
          "college_rank": 99.66,
          "experience_rank": 99.87
        },
        "founder": {
          "num_founded": 1,
          "top_company": "iCurrent"
        },
        "investor": {
          "num_investments": 1,
          "total_invested_usd": null
        },
        "contact_gated": true
      },
      {
        "id": "6a1d2c4f00edf351ec497c11",
        "name": "Shubhrendu Khoche",
        "headline": "business development, asia pacific @ trūata",
        "current_title": "business development, asia pacific",
        "current_company": "trūata",
        "current_company_domain": "",
        "location": "kuala lumpur, India",
        "gender_t5": "female",
        "image_url": "/people_logo?id=6a1d2c4f00edf351ec497c11",
        "summary": "Scaling ecosystem businesses | Digital Commerce & Payments | Asia Pacific | Fintech\n\nA strategist who executes for the business of technology. \n\nSeasoned and resourceful executive seeding, commercializing & scaling mobile commerce & payments businesses and building high performin…",
        "people_types": [
          "Angel Investor"
        ],
        "skills": [
          "business development",
          "strategy",
          "product management",
          "leadership",
          "telecommunications",
          "mobile payments",
          "mobile devices",
          "nfc"
        ],
        "education": [
          {
            "institution": "Delhi Public School - R. K. Puram",
            "degree": "",
            "years": "1986–1992"
          },
          {
            "institution": "Insead",
            "degree": "master of business administration",
            "years": "2002–2002"
          },
          {
            "institution": "Massachusetts Institute Of Technology",
            "degree": "commerce",
            "years": "2016–2016"
          }
        ],
        "top_experience": [
          {
            "title": "business development, asia pacific",
            "company": "trūata",
            "years": "2020–present"
          },
          {
            "title": "Founder",
            "company": "yufin",
            "years": "2021–present"
          },
          {
            "title": "head, new products and new business units",
            "company": "finablr",
            "years": "2019–present"
          }
        ],
        "linkedin_url": "http://linkedin.com/in/shubhrendukhoche",
        "twitter_url": null,
        "scores": {
          "people_rank": 99.48,
          "founder_rank": 98.95,
          "executive_rank": 92.67,
          "investor_rank": 86.85,
          "college_rank": 99.66,
          "experience_rank": 99.5
        },
        "founder": {
          "num_founded": 1,
          "top_company": "yufin"
        },
        "investor": {
          "num_investments": 1,
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
    "retrieved_at": "2026-09-23T03:35:32.873372+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/30-india-senior-executives.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
