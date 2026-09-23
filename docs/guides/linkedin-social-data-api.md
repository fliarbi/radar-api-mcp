# LinkedIn company data API: followers, headcount, stored posts and social profiles

Radar returns company LinkedIn observations, follower counts, observed employee
counts, company-size bands and stored posts through the selected `social` field.
It also returns company and professional social references. These are dated source
observations, not a live LinkedIn session or a claim of current accuracy.

## Pull company LinkedIn metrics, posts and social references

POST `/v1/companies/field`, MCP `get_company_field`:

<!-- contact-request: get_company_field -->
```json
{"domain":"razorpay.com","field":"social","item_limit":100}
```

The captured `value.links` includes LinkedIn, X, Facebook and blog URLs. Keys and
coverage can differ by company. Preserve missing links as unknown; do not construct
handles from the company name or assume every platform must be present.

The same explicitly selected social field now includes:

| Response path under `data.value.linkedin` | Meaning |
|---|---|
| `profile` | Latest stored profile: name, LinkedIn slug, followers, observed `employee_count`, company-size band, country, recorded sector and page-card engagement totals |
| `profile.observed_at` | When that profile was collected; separate from the gateway retrieval time and the company record's `updated_at` |
| `profile_history` | Stored profile snapshots, newest first; bounded by `item_limit` |
| `recent_posts` | Distinct posts using the latest stored version per post ID, ordered by publication time descending, unknown dates last |
| `recent_posts[].post_url`, `text`, `title`, `media_urls`, `hashtags`, `author` | Recorded post content and references; titles can be empty even when text exists |
| `recent_posts[].likes`, `comments`, `reposts` | Latest observed counters; source negatives become null and source zeros may include parser defaults |
| `recent_posts[].posted_at` / `observed_at` | Publication and collection time, expressed in UTC |
| `coverage` | Separate profile-history and post availability; failed sources return null with `unavailable`, not an invented empty success |

The September 23 gateway capture returned **1,252,056 followers**, **4,052 observed
employees**, a **1,001–5,000** size band and **eight posts** for Razorpay. Its profile
observation is dated **July 2, 2026**. The stored posts span June 26 through July 2.
The complete saved response below preserves all eight, rather than a single sample.
There is one stored profile snapshot here, so it does not establish a follower or
headcount trend. Platform employee counts are not audited payroll.

The recorded sector is `HRTech`; it disagrees with the company's business
classification and remains labelled `recorded_sector`. Source metadata is not
silently rewritten. Page-card reaction/comment totals are not lifetime totals and
need not equal the separately stored per-post counters.

`item_limit` is 1–100 (default 50). `coverage.arrays` reports source counts and
truncation for both top-level lists and nested media/hashtag arrays. This bounded
field has no offset or full-archive export. A missing LinkedIn connection is
`not_configured` and makes the social response partial while preserving existing
links. The compact company endpoint probes availability without loading these
metrics or post content. [Operator configuration](../OPERATIONS.md#company-linkedin-observations)
is separate from customer API-key setup.

Keep social references separate from email/phone values. A social URL is a profile
or page reference; this operation does not establish that a direct-message channel
is open or send anything. Use the [company contact endpoint](company-email-phone-api.md)
for a separate entitled email/phone lookup.

The company enrichment operation can supply additional source social activity or
engagement fields when present. Those are a distinct source view with its own
coverage and dates. It does not guarantee followers, posts, social account IDs or
LinkedIn-specific engagement for every company.

## Pull a person's recorded LinkedIn/X reference and professional detail

POST `/v1/people/search`, MCP `search_people`:

<!-- contact-request: search_people -->
```json
{"name":"Shashank Kumar","companies":["razorpay.com"],"limit":3}
```

The executed example returned a source profile ID, name, recorded company/domain,
LinkedIn URL, X URL, skills, education, experience summaries and professional rankings.
These source fields remain separate from contact values. `contact_gated` is an
access signal, not an email or phone number.

There is currently no public `linkedin_url` lookup/filter parameter, profile-slug
resolver, person-post reader, comment-thread reader or social-message action.
Company snapshots and company posts are retrieved by domain using the social field
above. Do not put a LinkedIn URL in `person_id`: use an accepted ID returned by
professional discovery. If an integration begins with only a URL, it must first
resolve identity through an available workflow and inspect the returned reference;
this contract does not provide an exact reverse-URL search.

## Match people and companies carefully

Company social links and a person's LinkedIn/X links are different entities. A
company's public page is not a founder's personal profile. Plain people search uses
a company-name/domain prefix predicate, while `get_company_team` with
`group=professionals` checks the exact recorded domain. Neither proves current
employment or resolves all name collisions.

Keep company domain, person ID, recorded reference URL, source/capture date and
identity-review outcome separate. A changed or absent social link should not erase
a previously reviewed identity without review. Social data can be stale even when
the API request completed successfully.

See [founder identity and contact workflow](founder-contact-data-api.md),
[all contact request variables](../CONTACTS.md), and
[the company data examples](../COMPANY_DATA_DEPTH.md#linkedin-company).

<!-- contact-evidence -->

### Company LinkedIn profile, metrics, snapshots and stored posts

**`POST /v1/companies/field`** · MCP **`get_company_field`**.
**Recorded live gateway response.** This capture is historical evidence, not a fresh health or identity verification.
Captured **2026-09-23T06:46:26.823192+00:00**, HTTP **200**,
mode **`live_gateway`**.

Exact executed request:

<!-- contact-captured-request: fields/razorpay.com-social.json -->
```json
{
  "domain": "razorpay.com",
  "field": "social",
  "item_limit": 100
}
```

Complete saved response:

<!-- contact-captured-response: fields/razorpay.com-social.json -->
```json
{
  "ok": true,
  "feature": "get_company_field",
  "data": {
    "domain": "razorpay.com",
    "company_id": "2gowls1wmc",
    "field": "social",
    "value": {
      "links": {
        "linkedin": "https://linkedin.com/company/razorpay/about",
        "x": "https://twitter.com/razorpay",
        "facebook": "https://facebook.com/razorpay",
        "blog": "https://razorpay.com/blog"
      },
      "linkedin": {
        "profile_history": [
          {
            "name": "Razorpay",
            "linkedin_slug": "razorpay",
            "recorded_sector": "HRTech",
            "hq_country": "India",
            "followers": 1252056,
            "employee_count": 4052,
            "company_size": "1,001-5,000",
            "observed_reactions": 719,
            "observed_comments": 25,
            "observed_post_count": 8,
            "observed_at": "2026-07-02T15:19:12Z"
          }
        ],
        "recent_posts": [
          {
            "post_id": "7478336549894426624",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-bangaloreogs-activity-7478336549894426624-oic9",
            "title": "",
            "text": "Keep it simple. That's the whole business philosophy Mr. Narayan Rao has ever needed at Corner House Ice Creams. \n\nFor decades generations of Bangalore have grown up enjoying and bonding over the same Hot Chocolate Fudge and DBC, grandparents and grandchildren alike.\n\nThis is Bangalore OGs, our love letter to the builders who made Bengaluru what it is today.\n\n#Razorpay #BangaloreOGs",
            "media_urls": [],
            "hashtags": [
              "Razorpay",
              "BangaloreOGs"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-07-02T01:09:34Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7478016085380878336",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_event-usmixer-razorpay-activity-7478016085380878336-lUpB",
            "title": "",
            "text": "Outtakes from a very special evening in SF, hosted in partnership with Silicon Valley Bank and Lightspeed. 💫\n\nA room full of Founders and operators from some of the most exciting companies, all building for the globe from Day 1. \n\nA big takeaway from the evening: The old playbook of expanding across geographies (years of groundwork, local entities, endless compliance) is dead. AI collapsed the timeline, and now going global is a decision you make on Day 1, not a milestone you earn years later.\n\nThank you to everyone who came out. This is just the beginning.\n\n#Event #USMixer #Razorpay",
            "media_urls": [],
            "hashtags": [
              "Event",
              "USMixer",
              "Razorpay"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-07-01T03:56:09Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7477959074165260290",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-netbanking-nbbl-activity-7477959074165260290-H5Vb",
            "title": "",
            "text": "\n🥁 Exciting news! Razorpay has partnered with NPCI Bharat BillPay Limited (NBBL) to bring a fast NetBanking experience to businesses and consumers across India.\n\nIntroducing Banking Connect - a standardised, mobile-first NetBanking experience built for the next era of digital payments.\n\n✨ We believe NetBanking has earned India’s trust for years. Today, we’re striving to make the experience even better.\n✅One network connecting banks, PAs, and users.\n✅All participant banks are enabled through one integration.\n✅Mobile-first Intent & QR flows for fast payments.\n✅Unified settlements and refunds .\n\nFor businesses, it means simpler enablement and fewer drop-offs. For users, it means NetBanking that is built for today.\n⚡UPI-like speed.\n🛡️The trust of the bank.\n🚀NetBanking 2.0, entering its next era.\n\nRazorpay🤝NPCI NBBL\n\nTo read more: https://lnkd.in/dhn2Qmah \n\n#Razorpay #NetBanking #NBBL #BankingConnect",
            "media_urls": [],
            "hashtags": [
              "Razorpay",
              "NetBanking",
              "NBBL",
              "BankingConnect"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-07-01T00:09:37Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7477683363114446848",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_event-razorpay-activity-7477683363114446848-H_zu",
            "title": "",
            "text": "Super excited to join the World's Largest Hermes Buildathon as the Ecosystem Partner in Bangalore!\n\nThe buildathon is happening across 10 cities and 5 countries, with builders getting access to $750K worth of credits to build on Hermes.\n\nPresented by GrowthX® alongside incredible partners like OpenAI, ElevenLabs, Wispr Flow, Cloudflare, and Convex, we're excited to bring this global buildathon to Bangalore.\n\nThousands of builders will be building on Hermes, and we're thrilled to welcome some of the best builders to Razorpay.\n\nSuper pumped to be part of this global wave.\n\n#event #razorpay",
            "media_urls": [],
            "hashtags": [
              "event",
              "razorpay"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-06-30T05:54:02Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7477633979073097728",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-activity-7477633979073097728-QbE9",
            "title": "",
            "text": "Revenue leaks are the biggest silent killers of your business 😑\n\nChargebacks, abandoned carts, and failed subscriptions drain your bottom line while you focus on growth.\n\nRazorpay Agent Studio deploys intelligent agents that take care of operational overheads, so you can focus on customers and growth. \n\nNo manual heavy lifting. Just measurable outcomes your CFO will love.\n\nInterested? Sign Up: https://lnkd.in/gYgvU_pi\n\n#Razorpay #3SlidesToConvinceYourCFO #AgentStudio ",
            "media_urls": [],
            "hashtags": [
              "Razorpay",
              "3SlidesToConvinceYourCFO",
              "AgentStudio"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-06-30T02:37:48Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7476884600569618432",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-razorpayftx26-activity-7476884600569618432-EGNA",
            "title": "",
            "text": "Rewinding to FTX 26, where the Agentic Era of Fintech began!\n\n#Razorpay #RazorpayFTX26 ",
            "media_urls": [],
            "hashtags": [
              "Razorpay",
              "RazorpayFTX26"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-06-28T01:00:02Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7476522238662516736",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-whateverittakes-sandoclub-activity-7476522238662516736-u_-o",
            "title": "",
            "text": "How much spice is too much spice? 🌶️\n\nWe put Jassil Jamaludhin and Carl Pinto, founders of Sando Club, through a spicy sando challenge to get their hottest takes on building brands, the F&B space, and everything in between.\n\nAs the sandwich got hotter, so did the questions. And let's just say, some answers were spicier than the sauce itself. 🔥\n\n#Razorpay #WhateverItTakes #SandoClub #Founders",
            "media_urls": [],
            "hashtags": [
              "Razorpay",
              "WhateverItTakes",
              "SandoClub",
              "Founders"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-06-27T01:00:08Z",
            "observed_at": "2026-07-02T15:19:12Z"
          },
          {
            "post_id": "7476244688887263232",
            "page_url": "https://www.linkedin.com/company/razorpay/",
            "post_url": "https://www.linkedin.com/posts/razorpay_razorpay-agenticdashboard-activity-7476244688887263232-beae",
            "title": "",
            "text": "In a sticky situation with a customer who get charged twice? 🫣\n\nRay's got you covered.\n\nRazorpay's Agentic Dashboard spots duplicate payments, flags them instantly, and walks you through the refund, in under a minute.\n\nNo digging. No delays. Just get it done.\n\n#razorpay #agenticdashboard",
            "media_urls": [],
            "hashtags": [
              "razorpay",
              "agenticdashboard"
            ],
            "likes": 0,
            "comments": 0,
            "reposts": 0,
            "author": "Razorpay",
            "posted_at": "2026-06-26T06:37:15Z",
            "observed_at": "2026-07-02T15:19:12Z"
          }
        ],
        "profile": {
          "name": "Razorpay",
          "linkedin_slug": "razorpay",
          "recorded_sector": "HRTech",
          "hq_country": "India",
          "followers": 1252056,
          "employee_count": 4052,
          "company_size": "1,001-5,000",
          "observed_reactions": 719,
          "observed_comments": 25,
          "observed_post_count": 8,
          "observed_at": "2026-07-02T15:19:12Z"
        },
        "coverage": {
          "profile_history": {
            "status": "available"
          },
          "recent_posts": {
            "status": "available"
          }
        },
        "notes": [
          "Stored LinkedIn observations; employee_count is observed platform headcount, not audited payroll.",
          "Recent means newest stored posts, not a live feed. Observation time differs from publication time.",
          "Post counters are latest stored values, not sums across crawls. Source zeros can include parser defaults.",
          "Negative source counters become null. Profile reaction/comment totals cover the observed page cards, not lifetime engagement.",
          "Recorded sector is a source label and can disagree with the company classification."
        ]
      }
    },
    "status": "available",
    "updated_at": "2026-06-01T04:43:22.775000+00:00",
    "coverage": {
      "sections": {
        "social": {
          "available": true,
          "status": "available"
        }
      },
      "arrays": {
        "/value/linkedin/profile_history": {
          "available": 1,
          "returned": 1,
          "truncated": false
        },
        "/value/linkedin/recent_posts": {
          "available": 8,
          "returned": 8,
          "truncated": false
        },
        "/value/linkedin/recent_posts/0/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/0/hashtags": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/linkedin/recent_posts/1/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/1/hashtags": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/linkedin/recent_posts/2/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/2/hashtags": {
          "available": 4,
          "returned": 4,
          "truncated": false
        },
        "/value/linkedin/recent_posts/3/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/3/hashtags": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/linkedin/recent_posts/4/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/4/hashtags": {
          "available": 3,
          "returned": 3,
          "truncated": false
        },
        "/value/linkedin/recent_posts/5/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/5/hashtags": {
          "available": 2,
          "returned": 2,
          "truncated": false
        },
        "/value/linkedin/recent_posts/6/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/6/hashtags": {
          "available": 4,
          "returned": 4,
          "truncated": false
        },
        "/value/linkedin/recent_posts/7/media_urls": {
          "available": 0,
          "returned": 0,
          "truncated": false
        },
        "/value/linkedin/recent_posts/7/hashtags": {
          "available": 2,
          "returned": 2,
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
    "retrieved_at": "2026-09-23T06:46:26.823192+00:00",
    "partial": false,
    "notes": [
      "Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field."
    ],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](../examples/fields/razorpay.com-social.json).

### Person LinkedIn/X references and professional detail

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
