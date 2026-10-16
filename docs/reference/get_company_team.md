# Company team data API: founders, key people and professional profiles

[All endpoints](README.md) · [Workflow guide](../guides/teams-people-data-api.md)

Retrieve one explicitly selected people group for a company domain. Founders and key people come from company records; professional profiles preserve skills, education, experience and exact recorded company-domain affiliation.

## Route, authentication and credits

**`POST /v1/companies/team`** · MCP tool **`get_company_team`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `page` | default `0` | integer; minimum: `0`; maximum: `200` |
| `limit` | default `20` | integer; minimum: `1`; maximum: `100` |
| `domain` | required | string |
| `group` | required | string; one of `key_people`, `founders`, `professionals` |
| `title` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `roles` | optional; empty by default | array of string; max items: `4`; one of `founder`, `investor`, `executive`, `board` |
| `skills` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `min_experience_years` | default `null` | integer or null; minimum: `0`; maximum: `80` |
| `min_seniority` | default `null` | string or null; one of `entry`, `senior`, `manager`, `director`, `vp`, `cxo`, `partner`, `owner` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

`RADAR_API_URL` is `https://radar-api.fliarbi.com` (the [installer](../../README.md#install-in-one-line) sets it);
load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/team" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com","group":"professionals","limit":3}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_team -->
```json
{
  "name": "get_company_team",
  "arguments": {
    "request": {
      "domain": "microsoft.com",
      "group": "professionals",
      "limit": 3
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_company_team -->
```json
{
  "ok": true,
  "feature": "get_company_team",
  "data": {
    "domain": "microsoft.com",
    "group": "professionals",
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
    "retrieved_at": "2026-09-23T06:47:28.421429+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:28.421655+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_team.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Microsoft example retains rich professional records but also source inconsistencies, including a retired-role label and an inverted experience date range. Separate Razorpay examples return two recorded founders and one CEO-designated key person.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.people` | Recorded people, not independently verified current employees. Professional cards have bounded skills and CV summaries. |
| `data.returned` | Number of delivered cards, not company headcount. |
| `data.excluded_unverified_affiliations` | Professional candidates removed because their recorded current company domain was absent or not an exact match. |
| `data.matched_observed_rows` | For key-person groups, count after local filtering within at most 100 observed records. |
| `data.next_page` | Continuation within the relevant source; can be present even if an exact-domain check removes all rows on this page. |
| `data.coverage` | Source status, partial state and affiliation limitations. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Choose founders, key_people or professionals. Use title only for company key-person records, and roles/skills/experience/seniority only for professionals. Page within the selected group and request contacts separately.

Professionals require both companies and people scopes. Highest career seniority does not establish the current role; source affiliation does not verify present employment. Team responses contain no emails or phone values.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/teams-people-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
