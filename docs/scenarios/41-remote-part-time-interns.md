# Find observed remote part-time internships with explicit work-mode evidence.

[All 50 scenarios](README.md) · [Workflow guide](../guides/internships-companies-api.md) · [Endpoint reference](../reference/search_internships.md)

**POST `/v1/jobs/internships/search`** · MCP tool **`search_internships`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

## Exact executed request

<!-- scenario-request: 41-remote-part-time-interns -->
```json
{
  "work_mode": "remote",
  "part_time": true,
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.627101+00:00; HTTP **200**;
**qualified**, 0.024 seconds.
Local authenticated gateway with live configured read-only sources.

Observed internship listings; current vacancies unverified, deadlines can be expired.

The source explicitly selects internship records. Remote means supporting source evidence, not an assumption from a city name. Preserve stipend currency and its unknown pay period. Expired or far-future deadlines do not establish a current opening; current_opening_verified stays false.

The baseline was HTTP 200, **qualified**:
Observed internship listings; current vacancies unverified, deadlines can be expired. The exact business question and request were held fixed across runs.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 41-remote-part-time-interns -->
```json
{
  "ok": true,
  "feature": "search_internships",
  "data": {
    "internships": [
      {
        "id": "1783099960",
        "title": "Software Development - Internship (WFH & Part Time)",
        "company": "Foundertruth",
        "company_domain": null,
        "url": "https://internshala.com/internship/detail/work-from-home-part-time-software-development-internship-at-foundertruth1783099960",
        "posted": "2026-07-04",
        "valid_through": "2026-08-03 23:59:59",
        "validity_status": "expired",
        "current_opening_verified": false,
        "employment_type": "INTERN, PART_TIME",
        "locations": [
          {
            "locality": "Siliguri",
            "region": "West Bengal",
            "country": "IN"
          }
        ],
        "skills": [
          "JavaScript",
          "Python",
          "Git",
          "Node.js",
          "GitHub",
          "React",
          "Vibe Coding"
        ],
        "work_mode": "remote_indicated",
        "industry": "Computer Services",
        "experience_months": null,
        "stipend": {
          "value": null,
          "currency": "INR",
          "period": null
        },
        "salary": {
          "min": 1000,
          "max": 1001,
          "currency": "INR",
          "period": null
        },
        "scraped_at": 1783143472,
        "last_seen": 1783143472,
        "source": "internshala",
        "detail_request": {
          "method": "POST",
          "path": "/v1/jobs/internships/detail"
        }
      },
      {
        "id": "1783103343",
        "title": "Content Writing - Internship (WFH & Part Time)",
        "company": "SwipeWise",
        "company_domain": null,
        "url": "https://internshala.com/internship/detail/work-from-home-content-writing-internship-at-swipewise1783103343",
        "posted": "2026-07-04",
        "valid_through": "2026-08-03 23:59:59",
        "validity_status": "expired",
        "current_opening_verified": false,
        "employment_type": "INTERN, PART_TIME",
        "locations": [
          {
            "locality": "New Delhi",
            "region": "Delhi",
            "country": "IN"
          }
        ],
        "skills": [
          "Social Media Marketing",
          "Blogging",
          "Digital Marketing",
          "Search Engine Optimization (SEO)",
          "Creative Writing",
          "Financial Analysis",
          "Risk Management",
          "English Proficiency (Spoken)",
          "English Proficiency (Written)",
          "Research and Analytics",
          "Financial literacy"
        ],
        "work_mode": "remote_indicated",
        "industry": "Computer Services , Consulting , Finance",
        "experience_months": null,
        "stipend": {
          "value": null,
          "currency": "INR",
          "period": null
        },
        "salary": {
          "min": 6000,
          "max": 8000,
          "currency": "INR",
          "period": null
        },
        "scraped_at": 1783143472,
        "last_seen": 1783143472,
        "source": "internshala",
        "detail_request": {
          "method": "POST",
          "path": "/v1/jobs/internships/detail"
        }
      },
      {
        "id": "1783106161",
        "title": "Content and Social Media Marketing - Internship (WFH & Part Time)",
        "company": "Fashtrend Marketing Pvt Ltd",
        "company_domain": null,
        "url": "https://internshala.com/internship/detail/work-from-home-content-and-social-media-marketing-internship-at-fashtrend-marketing-pvt-ltd1783106161",
        "posted": "2026-07-04",
        "valid_through": "2026-08-03 23:59:59",
        "validity_status": "expired",
        "current_opening_verified": false,
        "employment_type": "INTERN, PART_TIME",
        "locations": [
          {
            "locality": "Delhi",
            "region": "Delhi",
            "country": "IN"
          }
        ],
        "skills": [
          "Social Media Marketing",
          "Canva",
          "ChatGPT"
        ],
        "work_mode": "remote_indicated",
        "industry": "Retail",
        "experience_months": null,
        "stipend": {
          "value": null,
          "currency": "INR",
          "period": null
        },
        "salary": {
          "min": 3000,
          "max": 4001,
          "currency": "INR",
          "period": null
        },
        "scraped_at": 1783143472,
        "last_seen": 1783143472,
        "source": "internshala",
        "detail_request": {
          "method": "POST",
          "path": "/v1/jobs/internships/detail"
        }
      }
    ],
    "total": 441,
    "page": 0,
    "limit": 3,
    "has_more": true,
    "note": "These are observed internship listings, not verified current vacancies. Posted and crawl dates are separate. Far-future source deadlines are not proof a listing remains open. Stipend periods are not supplied."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.626864+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/41-remote-part-time-interns.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
