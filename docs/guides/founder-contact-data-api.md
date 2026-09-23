# Founder contact data API: resolve a founder, inspect details and request contacts

A founder contact workflow spans company founder records, professional identity
and a separately entitled email/phone lookup. Keeping those steps separate lets
you see what matched and prevents a generic company mailbox being stored as a
founder's direct address.

## 1. Read the company's recorded founders

POST `/v1/companies/team`, MCP `get_company_team`:

<!-- contact-request: get_company_team -->
```json
{"domain":"razorpay.com","group":"founders","limit":10}
```

The company record names Shashank Kumar and Harshil Mathur with recorded
designations. `group=founders` selects source key-person designations containing
founder; it is not a verified current management register. Use the separate
`people` company field for background flags, and keep those company-level flags
separate from a particular person's education or employment history.

## 2. Resolve a professional candidate and inspect the details

POST `/v1/people/search`, MCP `search_people`:

<!-- contact-request: search_people -->
```json
{"name":"Shashank Kumar","companies":["razorpay.com"],"limit":3}
```

The executed September 23 request returned one professional with ID
`6a1d2c3200edf351ec402e4d`, recorded current-company domain `razorpay.com`, a LinkedIn
reference and an X reference. Its captured record includes skills, education,
experience summaries, role information and source rankings. The full response
appears below; its dates and source text are preserved.

Check the returned name, exact normalized company domain and professional reference
against the company founder record. Names can collide, company search is prefix-based,
and current-company associations can be stale. If more than one plausible person
remains, retain that ambiguity before choosing a contact ID. Neither a shared name
nor a high professional rank proves identity.

## 3. Request only the contact types you need

POST `/v1/contacts/person`, MCP `get_person_contacts`:

<!-- contact-request: get_person_contacts -->
```json
{"person_id":"6a1d2c3200edf351ec402e4d","fields":["emails","phones"]}
```

This is a schema-validated next step using the discovered ID, not a live paid-contact
success capture. The key needs explicit `contacts` scope and the linked Radar
account must pass its source entitlement. The profile lookup needs `people` scope;
the founder-list request needs `companies`.

Keep profile details and the contact response as separate objects linked by the
accepted person ID. `contact_source=person` is a source association, not work-email
verification. `company_domain` is a business-contact fallback and must remain a
company contact. See [full contact response cases](../CONTACTS.md) for direct,
fallback, unknown-origin, empty and denied results using executed fictional fixtures.

## Handle a missing or conflicting founder profile

The same name-plus-company query for Harshil Mathur returned zero rows while the
company founder record still named him. Record the unresolved professional link;
do not create a substitute profile or infer that he has no contacts.

For broader candidate discovery, this request was also executed:

<!-- contact-request: get_company_team -->
```json
{"domain":"razorpay.com","group":"professionals","roles":["founder"],"limit":3}
```

It returned Ammu Tiwari, Shashank Kumar and Venkatesan Vaidhyanathan as source
founder-role profiles with the recorded company domain. Only Shashank Kumar's name
also occurs in the company founder capture. That is a discrepancy between source
views, not permission to describe every profile as a confirmed Razorpay founder.
The output below retains the disagreement so an integrator can handle it explicitly.

Use company `key_people` plus a designation substring such as CEO for a leadership
list. Use professional skills, roles, experience and seniority to discover potential
people. These are discovery variables; the contact endpoint itself still accepts
one person ID and selected email/phone types. [All 24 request recipes](../examples/contacts/requests.json)
show the separation.

For related workflows, see [company professional emails](company-email-phone-api.md),
[LinkedIn/social references](linkedin-social-data-api.md),
[teams and people](teams-people-data-api.md), and
[the source findings](../research/CONTACT_WORKFLOW_FINDINGS.md).

<!-- contact-evidence -->

### Company founder names

**`POST /v1/companies/field`** · MCP **`get_company_field`**.
**Recorded live gateway response.** This capture is historical evidence, not a fresh health or identity verification.
Captured **2026-09-23T06:46:26.703684+00:00**, HTTP **200**,
mode **`live_gateway`**.

Exact executed request:

<!-- contact-captured-request: fields/razorpay.com-people.json -->
```json
{
  "domain": "razorpay.com",
  "field": "people",
  "item_limit": 100
}
```

Complete saved response:

<!-- contact-captured-response: fields/razorpay.com-people.json -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "razorpay.com",
    "company_id": "2gowls1wmc",
    "field": "people",
    "value": {
      "key_people": [
        {
          "name": "Shashank Kumar",
          "designation": "Co-Founder & Managing Director"
        },
        {
          "name": "Harshil Mathur",
          "designation": "Co-Founder & CEO"
        }
      ],
      "founders": [
        {
          "name": "Shashank Kumar",
          "designation": "Co-Founder & Managing Director"
        },
        {
          "name": "Harshil Mathur",
          "designation": "Co-Founder & CEO"
        }
      ],
      "key_people_count": 2,
      "background_flags": [
        {
          "name": "Indian School of Business",
          "category": "College Wise"
        },
        {
          "name": "Intel",
          "category": "Company Wise"
        },
        {
          "name": "IIT Roorkee",
          "category": "College Wise"
        }
      ],
      "founder_selection": "Source designation contains founder; not an independent verification"
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "people": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/key_people": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/founders": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/background_flags": {
          "available": 3,
          "returned": 3,
          "truncated": false
        }
      },
      "partial": false
    },
    "note": "Only the requested field is returned. Missing data is not zero; array limits are explicit."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:46:26.703684+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](../examples/fields/razorpay.com-people.json).

### Resolved professional candidate

**`POST /v1/people/search`** · MCP **`search_people`**.
**Recorded live gateway response.** This capture is historical evidence, not a fresh health or identity verification.
Captured **2026-09-23T05:03:48.957668+00:00**, HTTP **200**,
mode **`live_gateway`**. Candidate linkage by recorded name and company domain; preserve the returned profile ID and LinkedIn reference. Not independent identity or current-role verification.

Exact executed request:

<!-- contact-captured-request: contacts/founder-shashank.json -->
```json
{
  "name": "Shashank Kumar",
  "companies": [
    "razorpay.com"
  ],
  "limit": 3
}
```

Complete saved response:

<!-- contact-captured-response: contacts/founder-shashank.json -->
```json
{
  "ok": true,
  "feature": "search_people",
  "data": {
    "people": [
      {
        "id": "6a1d2c3200edf351ec402e4d",
        "name": "Shashank Kumar",
        "headline": "Founder @ Razorpay",
        "current_title": "Founder",
        "current_company": "Razorpay",
        "current_company_domain": "razorpay.com",
        "location": "Bengaluru, India",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c3200edf351ec402e4d",
        "summary": "Spearheading technology, product and other internal functions at Razorpay. Aim to bring meaningful change in India via modernising payments and financial infra.",
        "people_types": [
          "Currently Founder",
          "Angel Investor"
        ],
        "skills": [
          "c++",
          "java",
          "c",
          "algorithms",
          "entrepreneurship",
          "data mining",
          "software development",
          "computer science"
        ],
        "education": [
          {
            "institution": "Indian Institute of Technology Roorkee",
            "degree": "B. Tech.",
            "years": "?–2012"
          },
          {
            "institution": "Indian Institute Of Technology",
            "degree": "",
            "years": ""
          },
          {
            "institution": "Dav Public School Bseb Patna",
            "degree": "",
            "years": "?–2008"
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Razorpay",
            "years": "2014–present"
          },
          {
            "title": "Founder",
            "company": "Mars Shot Ventures",
            "years": "2016–present"
          },
          {
            "title": "software development engineer",
            "company": "microsoft",
            "years": "2011–2011"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/kumarshashank",
        "twitter_url": "https://twitter.com/shashank_kr",
        "scores": {
          "people_rank": 89.35,
          "founder_rank": 90.78,
          "executive_rank": 98.47,
          "investor_rank": 98.77,
          "college_rank": 71.52,
          "experience_rank": 95.19
        },
        "founder": {
          "num_founded": 2,
          "top_company": "Mars Shot Ventures"
        },
        "investor": {
          "num_investments": 19,
          "total_invested_usd": 637995
        },
        "contact_gated": true
      }
    ],
    "total_estimate": 1,
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
    "retrieved_at": "2026-09-23T05:03:48.956737+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](../examples/contacts/founder-shashank.json).

### A founder name with no matching professional row

**`POST /v1/people/search`** · MCP **`search_people`**.
**Recorded live gateway response.** This capture is historical evidence, not a fresh health or identity verification.
Captured **2026-09-23T05:03:49.350515+00:00**, HTTP **200**,
mode **`live_gateway`**. Name-plus-company-prefix discovery; inspect recorded domain and LinkedIn URL before accepting a contact ID.

Exact executed request:

<!-- contact-captured-request: contacts/founder-professional.json -->
```json
{
  "name": "Harshil Mathur",
  "companies": [
    "razorpay.com"
  ],
  "limit": 3
}
```

Complete saved response:

<!-- contact-captured-response: contacts/founder-professional.json -->
```json
{
  "ok": true,
  "feature": "search_people",
  "data": {
    "people": [],
    "total_estimate": 0,
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
    "retrieved_at": "2026-09-23T05:03:49.349822+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](../examples/contacts/founder-professional.json).

### Source founder-role candidates requiring reconciliation

**`POST /v1/companies/team`** · MCP **`get_company_team`**.
**Recorded live gateway response.** This capture is historical evidence, not a fresh health or identity verification.
Captured **2026-09-23T05:03:49.383375+00:00**, HTTP **200**,
mode **`live_gateway`**. Exactly affiliated professional cards classified as founders by the source; current roles and completeness remain unverified.

Exact executed request:

<!-- contact-captured-request: contacts/founder-team.json -->
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

Complete saved response:

<!-- contact-captured-response: contacts/founder-team.json -->
```json
{
  "ok": true,
  "feature": "get_company_team",
  "data": {
    "domain": "razorpay.com",
    "group": "professionals",
    "people": [
      {
        "id": "6a1d2c3600edf351ec4173ba",
        "name": "Ammu Tiwari",
        "headline": "Founder @ Razorpay",
        "current_title": "Founder",
        "current_company": "Razorpay",
        "current_company_domain": "razorpay.com",
        "location": "bombay, India",
        "gender_t5": "unknown",
        "image_url": "/people_logo?id=6a1d2c3600edf351ec4173ba",
        "summary": "Ex-Cashfree Payments, Adyen, Razorpay, PayU. Don Bosco Institute of Technology BE 2010, IIT Dhanbad MBA 2015",
        "people_types": [
          "Currently Founder"
        ],
        "skills": [
          "management",
          "microsoft office",
          "team management",
          "business development",
          "engineering",
          "microsoft word",
          "operations management",
          "training"
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
            "institution": "Navy Children School",
            "degree": "",
            "years": ""
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Razorpay",
            "years": "2014–present"
          },
          {
            "title": "Founder",
            "company": "Edviron",
            "years": "2022–present"
          },
          {
            "title": "regional sales manager",
            "company": "payu",
            "years": "2017–2018"
          }
        ],
        "linkedin_url": "https://www.linkedin.com/in/ammu-kumar-tiwari-4b1bb95a/",
        "twitter_url": null,
        "scores": {
          "people_rank": 89.74,
          "founder_rank": 93.04,
          "executive_rank": 97.8,
          "investor_rank": null,
          "college_rank": 98.98,
          "experience_rank": 87.66
        },
        "founder": {
          "num_founded": 2,
          "top_company": "Edviron"
        },
        "investor": null,
        "contact_gated": true
      },
      {
        "id": "6a1d2c3200edf351ec402e4d",
        "name": "Shashank Kumar",
        "headline": "Founder @ Razorpay",
        "current_title": "Founder",
        "current_company": "Razorpay",
        "current_company_domain": "razorpay.com",
        "location": "Bengaluru, India",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c3200edf351ec402e4d",
        "summary": "Spearheading technology, product and other internal functions at Razorpay. Aim to bring meaningful change in India via modernising payments and financial infra.",
        "people_types": [
          "Currently Founder",
          "Angel Investor"
        ],
        "skills": [
          "c++",
          "java",
          "c",
          "algorithms",
          "entrepreneurship",
          "data mining",
          "software development",
          "computer science"
        ],
        "education": [
          {
            "institution": "Indian Institute of Technology Roorkee",
            "degree": "B. Tech.",
            "years": "?–2012"
          },
          {
            "institution": "Indian Institute Of Technology",
            "degree": "",
            "years": ""
          },
          {
            "institution": "Dav Public School Bseb Patna",
            "degree": "",
            "years": "?–2008"
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Razorpay",
            "years": "2014–present"
          },
          {
            "title": "Founder",
            "company": "Mars Shot Ventures",
            "years": "2016–present"
          },
          {
            "title": "software development engineer",
            "company": "microsoft",
            "years": "2011–2011"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/kumarshashank",
        "twitter_url": "https://twitter.com/shashank_kr",
        "scores": {
          "people_rank": 89.35,
          "founder_rank": 90.78,
          "executive_rank": 98.47,
          "investor_rank": 98.77,
          "college_rank": 71.52,
          "experience_rank": 95.19
        },
        "founder": {
          "num_founded": 2,
          "top_company": "Mars Shot Ventures"
        },
        "investor": {
          "num_investments": 19,
          "total_invested_usd": 637995
        },
        "contact_gated": true
      },
      {
        "id": "6a1d2c3400edf351ec4103c9",
        "name": "Venkatesan Vaidhyanathan",
        "headline": "Founder @ Razorpay",
        "current_title": "Founder",
        "current_company": "Razorpay",
        "current_company_domain": "razorpay.com",
        "location": "Bengaluru, India",
        "gender_t5": "male",
        "image_url": "/people_logo?id=6a1d2c3400edf351ec4103c9",
        "summary": "Exposure to different programming languages and architectures. Experience in designing and implementing large scale and fault tolerant systems.\n\nSpecialties: Distributed Systems, Scalability, Web Apps, PHP, perl, *nix, HTTP, Web Services, munching bits and bytes",
        "people_types": [
          "Currently Founder"
        ],
        "skills": [
          "web services",
          "perl",
          "scalability",
          "mysql",
          "algorithms",
          "php",
          "web applications",
          "html"
        ],
        "education": [
          {
            "institution": "Birla Institute Of Technology And Science, Pilani",
            "degree": "master of science in mathematics",
            "years": "1998–2004"
          }
        ],
        "top_experience": [
          {
            "title": "Founder",
            "company": "Razorpay",
            "years": "2014–present"
          },
          {
            "title": "Founder",
            "company": "slice",
            "years": "2015–present"
          },
          {
            "title": "vice president engineering",
            "company": "teabox",
            "years": "2015–2016"
          }
        ],
        "linkedin_url": "http://linkedin.com/in/venkatesanv",
        "twitter_url": null,
        "scores": {
          "people_rank": 83.48,
          "founder_rank": 84.12,
          "executive_rank": 98.64,
          "investor_rank": null,
          "college_rank": 44.33,
          "experience_rank": 98.7
        },
        "founder": {
          "num_founded": 2,
          "top_company": "slice"
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
    "retrieved_at": "2026-09-23T05:03:49.382567+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](../examples/contacts/founder-team.json).
