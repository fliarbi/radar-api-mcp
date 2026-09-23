# Founder contacts, company emails, professional phones and social links API

Use this guide to combine company and founder details with recorded professional
profiles, LinkedIn/social references and a separate contact lookup. Contact values
are requested explicitly; company identity, founder names and social links are
available through their own data operations. These are different source records,
so a shared name alone is not a reliable join.

## Choose the workflow

| You need | Discovery or detail request | Contact request / interpretation |
|---|---|---|
| Company email addresses | `get_company` for domain and contact availability | `get_company_contacts`, `fields=["emails"]` |
| Company phone numbers | Resolve the company domain | Same operation, `fields=["phones"]` |
| Both company contact types | Resolve the company domain | Same operation, select both explicitly |
| Founder names and recorded designations | `get_company_team`, `group=founders` | This group does not supply contact IDs or values |
| Founder details and a person ID | `search_people` by accepted name and company; compare identity and profile links | `get_person_contacts` for the accepted returned ID |
| Company professional / employee emails | `get_company_team`, `group=professionals`, then select accepted people | One separate person lookup per ID; no company-wide employee email dump |
| Executives, board members or other professional groups | Team `roles`, `skills`, experience or seniority filters | Role labels and career seniority do not verify a current position |
| Company LinkedIn, X, Facebook or blog URL | `get_company_field`, `field=social` | Returned links do not require a contact-reveal request |
| Company LinkedIn followers, headcount and stored posts | Same selected social field, `value.linkedin` | Dated profile snapshots and bounded distinct posts; latest stored observations, not a live feed |
| A person's LinkedIn or X reference | Professional card's `linkedin_url` and `twitter_url` | Recorded references, not live LinkedIn access or a messaging channel |
| Only work emails or verified mailboxes | Retrieve the explicitly permitted contact types and inspect provenance | The API currently supplies neither email-type nor deliverability verification filters |

Detailed guides: [founder contact workflows](guides/founder-contact-data-api.md),
[company email and phone workflows](guides/company-email-phone-api.md),
[LinkedIn and social links](guides/linkedin-social-data-api.md),
[teams and people](guides/teams-people-data-api.md).

## Obtain a key with the necessary scopes

POST this request to `/account/keys`, authenticated with the existing verified
Radar session. The developer console offers the corresponding scope choices.

<!-- contact-request: account_create_key -->
```json
{"name":"Company and founder research","scopes":["companies","people","contacts"],"expires_days":30}
```

The data requests below use that generated API key in `Authorization: Bearer` or
`X-API-Key`. A contact-only key can request an already known domain/person ID but
cannot also perform company and people discovery. `contacts` must be explicit,
even alongside `*`. Professional team discovery requires `companies` and `people`.
Social-field retrieval requires `companies`; person discovery requires `people`.

The linked Radar account must also pass the source paid-plan check. Adding the
contacts scope or buying API credits does not bypass it. Older keys retain their
existing scopes. See [key onboarding](guides/api-keys-authentication.md) and
[pricing](guides/pricing-pay-per-use.md) for account policy.

## Founder contact with details: an executed discovery example

Start with the company founder records:

<!-- contact-request: get_company_team -->
```json
{"domain":"razorpay.com","group":"founders","limit":10}
```

POST `/v1/companies/team`, MCP `get_company_team`. The saved company capture names
Shashank Kumar and Harshil Mathur. Those rows contain names/designations; they are
not contact IDs. Now discover the professional record for a selected founder:

<!-- contact-request: search_people -->
```json
{"name":"Shashank Kumar","companies":["razorpay.com"],"limit":3}
```

POST `/v1/people/search`, MCP `search_people`. The September 23 live query returned
one candidate with ID `6a1d2c3200edf351ec402e4d`, recorded company domain
`razorpay.com`, LinkedIn URL `https://linkedin.com/in/kumarshashank` and an X reference.
Its complete captured education, experience, skills and professional fields appear
in the [founder guide](guides/founder-contact-data-api.md). Compare the name,
recorded domain, company founder record and professional references before selecting
the ID. This cross-check is candidate linkage, not independent identity or current-role verification.

Then make the separate contact request if your key and linked account are entitled:

<!-- contact-request: get_person_contacts -->
```json
{"person_id":"6a1d2c3200edf351ec402e4d","fields":["emails","phones"]}
```

POST `/v1/contacts/person`, MCP `get_person_contacts`. This contact body is a
schema-validated next step; **no live paid-contact success is claimed or published
for this person**. Do not replace it with a made-up address or a pattern such as
first-name@company. The actual live default-key denial and executed synthetic
success/fallback outputs are shown in the evidence section below.

### Why resolving the person is a separate step

The same name-plus-company query for Harshil Mathur returned zero records. That
result does not disprove the company founder record or establish that he has no
contacts. Leave the join unresolved and preserve both observations.

The professional founder-role query returned three exact-domain profiles, including
names absent from the company founder list. A `roles=["founder"]` tag is therefore
candidate discovery, not confirmation that every result founded that company.
Keep unmatched people separate; do not acquire their contacts under another founder's
identity. The [source findings](research/CONTACT_WORKFLOW_FINDINGS.md) retain these
positive, empty and conflicting captures.

## Company email, phone and social contact

Request only company emails:

<!-- contact-request: get_company_contacts -->
```json
{"domain":"razorpay.com","fields":["emails"]}
```

Request only company phones:

<!-- contact-request: get_company_contacts -->
```json
{"domain":"razorpay.com","fields":["phones"]}
```

Request both:

<!-- contact-request: get_company_contacts -->
```json
{"domain":"razorpay.com","fields":["emails","phones"]}
```

These are POST requests to `/v1/contacts/company`, MCP `get_company_contacts`.
The response describes company-associated contact strings. It does not identify
which mailbox is sales, support, procurement or a named founder's address, and it
does not label a phone as a mobile, switchboard, direct line or WhatsApp number.
A familiar-looking mailbox name or country code is not verification.

For recorded social references, use a separate field request:

<!-- contact-request: get_company_field -->
```json
{"domain":"razorpay.com","field":"social","item_limit":100}
```

POST `/v1/companies/field`, MCP `get_company_field`. The captured company social
record includes LinkedIn, X, Facebook and blog links. Do not put `social`,
`linkedin` or `twitter` inside the contact endpoint's `fields`: only `emails` and
`phones` are accepted there. [The social-link guide](guides/linkedin-social-data-api.md)
shows the full response and missing-link handling.

`value.linkedin` also supplies the latest stored LinkedIn profile, bounded profile
history and distinct posts when the social read connection is configured. The
Razorpay example includes 1,252,056 followers, 4,052 observed employees and eight
posts, collected in July 2026. Keep those observation dates separate from the
September gateway capture date and company record update date.

## Company professional emails: discover people, then retrieve individually

<!-- contact-request: get_company_team -->
```json
{"domain":"stripe.com","group":"professionals","roles":["executive"],"min_seniority":"director","limit":5,"page":0}
```

POST `/v1/companies/team`, MCP `get_company_team`. The team operation filters
source candidates to an exact recorded company domain and reports excluded
unresolved affiliations. Page zero is the first page. A page can contain no accepted
rows and still have a continuation because source pagination includes excluded
candidates. Source cards are not a complete employee roster.

For each selected professional, use that card's `id` in a separate person contact
request. Keep the contact result alongside the originating profile ID, recorded
company, source update/retrieval time, requested contact types and `contact_source`.
Do not attach every company contact address to every member of the team.

`min_seniority` uses highest recorded career seniority, not necessarily the person's
current job. Source skills and education/experience arrays are bounded summaries.
Changing roles, location, school or skills changes discovery; it does not introduce
new filters inside `/v1/contacts/person`.

## All supported variables and their boundaries

| Request family | Variables | Meaning / bounds |
|---|---|---|
| Company contact | `domain`, `fields` | One normalized website domain; emails, phones or both; no URL scheme/path |
| Person contact | `person_id`, `fields` | One source profile ID from discovery; not a company ID, name or LinkedIn URL |
| Company field | `domain`, optional `company_id`, `field`, `item_limit` | Select `social` or `people` explicitly; array limit 1–100 |
| Company team, every group | `domain`, required `group`, `page`, `limit` | founders / key_people / professionals; page 0–200, limit 1–100; key-person paging bounded to 100 observed records |
| Founders / key people | `title` | Case-insensitive designation substring, e.g. CEO; not supported for professionals |
| Professional team | `roles`, `skills`, `min_experience_years`, `min_seniority` | Role values founder/investor/executive/board; experience 0–80 years; source classifications and career measures |
| People search | `name`, `companies`, `roles`, `locations`, `skills`, `sectors`, `schools`, `degrees`, `min_experience_years`, `min_seniority`, `min_people_rank`, `page`, `limit` | More discovery dimensions; company names/domains use a source prefix predicate; people rank is 0–100 |
| People vocabulary | `field`, `q`, `limit` | `people_filter_options` suggests schools, skills or sectors; use returned canonical labels |

Text filters accept nonempty strings up to 200 characters; term lists accept up
to 20 values. Quotes, backslashes, semicolons and control characters are rejected.
`min_seniority` accepts `entry`, `senior`, `manager`, `director`, `vp`, `cxo`, `partner`
or `owner`. People vocabulary `q` accepts 2–500 characters and `limit` is 1–10.
Person IDs accept 1–100 letters, numbers, underscores or hyphens. Contact `fields`
must be an array containing one or both accepted types.

The [24 readable request recipes](CONTACT_REQUEST_RECIPES.md) and
[machine-readable variants](examples/contacts/requests.json) provide copyable
bodies with their exact routes and scopes. These are labelled request
recipes; model validation is not a claim that every variant was executed or returns
a nonempty result.

Unsupported current parameters include `email_type`, `verified_only`, `has_email`,
`has_phone`, `allow_company_fallback`, `linkedin_url`, bulk `person_ids` or `domains`
on the contact endpoints. Unknown fields are rejected rather than silently honored.
There is no server-side department or guaranteed-work-email selection in this
contract. See [the capability/gap map](research/CONTACT_WORKFLOW_FINDINGS.md).

## Interpret the contact response correctly

| Field / condition | Interpretation |
|---|---|
| `contact_source=person` | Contact strings associated with the person source record; not automatically current, deliverable or work-only |
| `contact_source=company_domain` | Company-associated contact or person lookup fallback; never a verified personal contact |
| `contact_source=none` | Source reported no origin/contact, or omitted its origin label; inspect the arrays too. An unresolved ID can also produce this state |
| `contact_source=unknown` | Source supplied an unrecognized origin value; do not upgrade it to direct-person provenance |
| `available=true` | At least one of the requested types has a returned value |
| `available=false` | None of the requested types has a returned value; another unrequested type can still exist |
| An omitted contact type | You did not request it; this says nothing about its source availability |
| `emails=[]` / `phones=[]` | Requested type returned no values; absence and some source lookup failures are not always distinguishable |

### Fallback is all-or-nothing at the source

The person resolver first uses person email and phone records. It prefers the
source's confirmed-email list when present, otherwise its general email list.
The gateway does not expose a per-address verification label, verification date,
deliverability score or those original source lists.

Company fallback occurs only when **both** person emails and person phones are
absent. If a person has a phone but no email, an emails-only request returns
`emails=[]`, `contact_source=person`, `available=false`; it does not independently
fill the email from the company. Request company email separately if that is useful,
and retain its company-level attribution. No caller flag currently turns source
fallback on or off; an application can decline to use a fallback after inspecting
the returned provenance.

### Work email, personal email and verification are different questions

`person` describes the source association, not an email category. A company-domain
suffix can be recorded by your application as an observed suffix match, but it
does not prove employment, mailbox ownership or deliverability. A company may use
a subsidiary, acquired-company or other business domain. Do not invent missing
addresses, classify every nonmatching suffix as personal, or label the data SMTP
verified. This API performs no email validation, message delivery or social messaging.

## Limits, costs and failure handling

Each lookup returns at most 25 distinct nonempty strings per requested contact type.
The gateway trims strings and removes exact duplicates. It does not promise
case-insensitive mailbox deduplication, phone normalization, a full contact archive,
source-total counts or contact-array pagination. `item_limit` and `page` belong to
discovery/detail operations, not contact requests.

Contacts have a separate 10-per-minute limit per API account, shared across keys;
manual preview keys are limited individually. The regular rate/concurrency and
monthly spending controls also apply. In account mode each successful contact
request costs one credit, including an empty successful lookup. Company and people
discovery are additional operations. Access denials and upstream failures do not
consume operation credits. Buying credits does not change source entitlements.

| HTTP / error | Action |
|---|---|
| 401 | Check API-key validity, expiry and authorization header |
| 403 `scope_required` | Use a key with explicit contacts scope; discovery scopes remain separate |
| 403 `access_required` | Check the linked Radar session and source entitlement; a new key alone does not upgrade the plan |
| 422 | Correct the identifier, requested fields or unsupported parameters |
| 429 | Honor `Retry-After`; do not rotate keys to evade account limits |
| 502/503/504 | Preserve the failed lookup and retry with bounded backoff when appropriate; do not turn it into an empty successful contact |
| 200 with empty requested arrays | Store an unresolved observation; do not infer that the person or company has no contact anywhere |

Keep API keys out of browser bundles and examples. No data operation in this
workflow sends messages or changes company/person source records.

## Captured outputs and their provenance

The following section includes real discovery data, real default-key access
failures and executed local contract fixtures. Every synthetic success uses a
fictional person, reserved `example.com` addresses and fictional phone values.
Those fixtures demonstrate the real gateway's projections and gates; they are
not live paid-contact access evidence or contact details for the founders above.

<!-- contact-evidence -->

### Founder professional details: real discovery

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

[Capture, provenance and checksums](examples/contacts/founder-shashank.json).

### Company social data: followers, headcount and stored posts

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

[Capture, provenance and checksums](examples/fields/razorpay.com-social.json).

### Default-key contact denial: live gateway capture

**`POST /v1/contacts/company`** · MCP **`get_company_contacts`**.
**Recorded live gateway response.** This capture is historical evidence, not a fresh health or identity verification.
Captured **2026-09-23T06:47:59.312198+00:00**, HTTP **403**,
mode **`live_gateway`**.

Exact executed request:

<!-- contact-captured-request: get_company_contacts.json -->
```json
{
  "domain": "razorpay.com",
  "fields": [
    "emails"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: get_company_contacts.json -->
```json
{
  "ok": false,
  "feature": "get_company_contacts",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:59.312096+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  },
  "error": {
    "kind": "scope_required",
    "message": "Create a key with the explicit contacts scope for contact retrieval"
  }
}
```

[Capture, provenance and checksums](examples/get_company_contacts.json).

### Company emails only: executed fictional fixture

**`POST /v1/contacts/company`** · MCP **`get_company_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:42.815623+00:00**, HTTP **200**,
mode **`local_contact_fixture`**. Company-associated mailboxes, with phone values excluded by field selection.

Exact executed request:

<!-- contact-captured-request: contacts/company-email-only.json -->
```json
{
  "domain": "example.com",
  "fields": [
    "emails"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/company-email-only.json -->
```json
{
  "ok": true,
  "feature": "get_company_contacts",
  "data": {
    "domain": "example.com",
    "emails": [
      "sales@example.com",
      "support@example.com"
    ],
    "contact_source": "company_domain",
    "available": true,
    "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:42.814920+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](examples/contacts/company-email-only.json).

### Company phones only: executed fictional fixture

**`POST /v1/contacts/company`** · MCP **`get_company_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:42.987821+00:00**, HTTP **200**,
mode **`local_contact_fixture`**. Requested phone strings only; the gateway does not certify mobile status or E.164 normalization.

Exact executed request:

<!-- contact-captured-request: contacts/company-phone-only.json -->
```json
{
  "domain": "example.com",
  "fields": [
    "phones"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/company-phone-only.json -->
```json
{
  "ok": true,
  "feature": "get_company_contacts",
  "data": {
    "domain": "example.com",
    "phones": [
      "+1-202-555-0123"
    ],
    "contact_source": "company_domain",
    "available": true,
    "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:42.987105+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](examples/contacts/company-phone-only.json).

### Direct person association: executed fictional fixture

**`POST /v1/contacts/person`** · MCP **`get_person_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:43.110329+00:00**, HTTP **200**,
mode **`local_contact_fixture`**. A fictional person's source-associated record. Person origin does not establish verified work-email type.

Exact executed request:

<!-- contact-captured-request: contacts/person-direct.json -->
```json
{
  "person_id": "example-founder",
  "fields": [
    "emails",
    "phones"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/person-direct.json -->
```json
{
  "ok": true,
  "feature": "get_person_contacts",
  "data": {
    "person_id": "example-founder",
    "emails": [
      "alex@example.com"
    ],
    "phones": [
      "+1-202-555-0142"
    ],
    "contact_source": "person",
    "available": true,
    "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:43.109656+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](examples/contacts/person-direct.json).

### Company mailbox fallback: executed fictional fixture

**`POST /v1/contacts/person`** · MCP **`get_person_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:43.232582+00:00**, HTTP **200**,
mode **`local_contact_fixture`**. Company mailbox fallback; never relabel this as the founder's personal address.

Exact executed request:

<!-- contact-captured-request: contacts/person-company-fallback.json -->
```json
{
  "person_id": "example-founder",
  "fields": [
    "emails"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/person-company-fallback.json -->
```json
{
  "ok": true,
  "feature": "get_person_contacts",
  "data": {
    "person_id": "example-founder",
    "emails": [
      "sales@example.com"
    ],
    "contact_source": "company_domain",
    "available": true,
    "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:43.231867+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](examples/contacts/person-company-fallback.json).

### Phone exists but email-only lookup is empty: fictional fixture

**`POST /v1/contacts/person`** · MCP **`get_person_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:43.359783+00:00**, HTTP **200**,
mode **`local_contact_fixture`**. Source had a person phone but no email; an email-only request is empty. Fallback is not independently applied per requested field.

Exact executed request:

<!-- contact-captured-request: contacts/person-phone-only-source.json -->
```json
{
  "person_id": "example-founder",
  "fields": [
    "emails"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/person-phone-only-source.json -->
```json
{
  "ok": true,
  "feature": "get_person_contacts",
  "data": {
    "person_id": "example-founder",
    "emails": [],
    "contact_source": "person",
    "available": false,
    "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:43.359064+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](examples/contacts/person-phone-only-source.json).

### No contact returned: executed fictional fixture

**`POST /v1/contacts/person`** · MCP **`get_person_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:43.563355+00:00**, HTTP **200**,
mode **`local_contact_fixture`**. No returned source contact, including when the source did not resolve the person ID. This is not proof of nonexistence.

Exact executed request:

<!-- contact-captured-request: contacts/person-no-data.json -->
```json
{
  "person_id": "example-founder",
  "fields": [
    "emails",
    "phones"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/person-no-data.json -->
```json
{
  "ok": true,
  "feature": "get_person_contacts",
  "data": {
    "person_id": "example-founder",
    "emails": [],
    "phones": [],
    "contact_source": "none",
    "available": false,
    "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:43.562692+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](examples/contacts/person-no-data.json).

### Unknown source label: executed fictional fixture

**`POST /v1/contacts/person`** · MCP **`get_person_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:43.682659+00:00**, HTTP **200**,
mode **`local_contact_fixture`**. Unexpected provenance stays unknown, not silently classified as a person's direct contact.

Exact executed request:

<!-- contact-captured-request: contacts/person-unknown-origin.json -->
```json
{
  "person_id": "example-founder",
  "fields": [
    "emails"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/person-unknown-origin.json -->
```json
{
  "ok": true,
  "feature": "get_person_contacts",
  "data": {
    "person_id": "example-founder",
    "emails": [
      "alex@example.com"
    ],
    "contact_source": "unknown",
    "available": true,
    "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:43.682033+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](examples/contacts/person-unknown-origin.json).

### Source plan denial with values suppressed: fictional fixture

**`POST /v1/contacts/company`** · MCP **`get_company_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:43.801738+00:00**, HTTP **403**,
mode **`local_contact_fixture`**. The linked source gate wins even if a malformed gated response contains contact values.

Exact executed request:

<!-- contact-captured-request: contacts/paid-plan-denial.json -->
```json
{
  "domain": "example.com",
  "fields": [
    "emails"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/paid-plan-denial.json -->
```json
{
  "ok": false,
  "feature": "get_company_contacts",
  "data": null,
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:43.801013+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  },
  "error": {
    "kind": "access_required",
    "message": "The linked Radar plan does not permit contact retrieval"
  }
}
```

[Capture, provenance and checksums](examples/contacts/paid-plan-denial.json).
