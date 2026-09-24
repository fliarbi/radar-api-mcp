# Find observed internship listings with stipend value at least 10,000, preserving currency and unknown period.

[All 50 scenarios](README.md) · [Workflow guide](../guides/internships-companies-api.md) · [Endpoint reference](../reference/search_internships.md)

**POST `/v1/jobs/internships/search`** · MCP tool **`search_internships`**.
Use your operator-supplied API URL and API key; [onboarding](../guides/api-keys-authentication.md)
explains how to obtain one. For MCP, put the same JSON body inside `arguments.request`.

**Populated worked example.** 3 internships; totals and context do not substitute for requested rows.

## Exact executed request

<!-- scenario-request: 43-internship-stipend -->
```json
{
  "stipend_min": 10000,
  "limit": 3
}
```

## Observed result and interpretation

Captured 2026-09-23T03:35:33.649324+00:00; HTTP **200**;
**qualified**, 0.006 seconds.
Local authenticated gateway with live configured read-only sources.

Observed internship listings; current vacancies unverified, deadlines can be expired.

The source explicitly selects internship records. Remote means supporting source evidence, not an assumption from a city name. Preserve stipend currency and its unknown pay period. Expired or far-future deadlines do not establish a current opening; current_opening_verified stays false.

The baseline was HTTP 200, **qualified**:
Observed internship listings; current vacancies unverified, deadlines can be expired. The exact business question and request were held fixed across these two captures.
Assertions cover the response contract and declared observable predicates, not an
independent certification of all source facts or exhaustive coverage.

## Captured output

<!-- scenario-response: 43-internship-stipend -->
```json
{
  "ok": true,
  "feature": "search_internships",
  "data": {
    "internships": [
      {
        "id": "1783090513",
        "title": "Graphic Design - Internship (WFH)",
        "company": "Reducate.ai",
        "company_domain": null,
        "url": "https://internshala.com/internship/detail/work-from-home-graphic-design-internship-at-reducateai1783090513",
        "posted": "2026-07-03",
        "valid_through": "2026-08-02 23:59:59",
        "validity_status": "expired",
        "current_opening_verified": false,
        "employment_type": "INTERN, FULL_TIME",
        "locations": [
          {
            "locality": "Bengaluru",
            "region": "Karnataka",
            "country": "IN"
          }
        ],
        "skills": [
          "Adobe Photoshop",
          "CorelDRAW",
          "Adobe Illustrator",
          "Video Editing",
          "Adobe Premiere Pro",
          "Adobe Creative Suite",
          "Adobe InDesign",
          "UI & UX Design",
          "Adobe After Effects",
          "Adobe Photoshop Lightroom CC",
          "Effective Communication"
        ],
        "work_mode": "remote_indicated",
        "industry": "Education",
        "experience_months": null,
        "stipend": {
          "value": 15000,
          "currency": "INR",
          "period": null
        },
        "salary": {
          "min": null,
          "max": null,
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
        "id": "1782971282",
        "title": "Digital Marketing - Internship",
        "company": "Brandshark",
        "company_domain": null,
        "url": "https://internshala.com/internship/detail/digital-marketing-internship-in-bangalore-at-brandshark1782971282",
        "posted": "2026-07-02",
        "valid_through": "2026-08-01 23:59:59",
        "validity_status": "expired",
        "current_opening_verified": false,
        "employment_type": "INTERN, FULL_TIME",
        "locations": [
          {
            "locality": "Bangalore",
            "region": "Karnataka",
            "country": "IN"
          }
        ],
        "skills": [
          "Social Media Marketing",
          "Search Engine Marketing (SEM)",
          "Digital Marketing",
          "Search Engine Optimization (SEO)",
          "Instagram Marketing"
        ],
        "work_mode": "location_listed",
        "industry": "Marketing",
        "experience_months": null,
        "stipend": {
          "value": 10000,
          "currency": "INR",
          "period": null
        },
        "salary": {
          "min": null,
          "max": null,
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
        "id": "1782995146",
        "title": "Sales - Internship",
        "company": "Brandshark",
        "company_domain": null,
        "url": "https://internshala.com/internship/detail/sales-internship-in-bangalore-at-brandshark1782995146",
        "posted": "2026-07-02",
        "valid_through": "2026-08-01 23:59:59",
        "validity_status": "expired",
        "current_opening_verified": false,
        "employment_type": "INTERN, FULL_TIME",
        "locations": [
          {
            "locality": "Bangalore",
            "region": "Karnataka",
            "country": "IN"
          }
        ],
        "skills": [
          "LinkedIn Marketing",
          "English Proficiency (Spoken)"
        ],
        "work_mode": "location_listed",
        "industry": "Marketing",
        "experience_months": null,
        "stipend": {
          "value": 10000,
          "currency": "INR",
          "period": null
        },
        "salary": {
          "min": null,
          "max": null,
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
    "total": 131,
    "page": 0,
    "limit": 3,
    "has_more": true,
    "note": "These are observed internship listings, not verified current vacancies. Posted and crawl dates are separate. Far-future source deadlines are not proof a listing remains open. Stipend periods are not supplied."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:35:33.649081+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Download the current and baseline JSON](../examples/scenarios/43-internship-stipend.json)
for both timestamps, statuses, elapsed times, assessments, original-response hashes
and explicit prose omissions. No returned array rows are removed. A checksum
proves consistency with a capture, not the accuracy or completeness of its source.
