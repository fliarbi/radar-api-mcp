# Professional profile search API: founders, investors and executives

[All endpoints](README.md) · [Workflow guide](../guides/b2b-data-api.md)

Search professional profiles by name, supported role categories, current company, skills and location. Use this for identity context in company or investor research. The gateway keeps professional detail; email and phone retrieval use separate explicit contact endpoints.

## Route, authentication and credits

**`POST /v1/people/search`** · MCP tool **`search_people`** · key scope **`people`**.
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
| `name` | default `null` | string or null; min characters: `1`; max characters: `200` |
| `roles` | optional; empty by default | array of string; max items: `4`; one of `founder`, `investor`, `executive`, `board` |
| `locations` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `skills` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `companies` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `sectors` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `min_experience_years` | default `null` | integer or null; minimum: `0`; maximum: `80` |
| `schools` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `degrees` | optional; empty by default | array of string; max items: `20`; min characters: `1`; max characters: `200` |
| `min_seniority` | default `null` | string or null; one of `entry`, `senior`, `manager`, `director`, `vp`, `cxo`, `partner`, `owner` |
| `min_people_rank` | default `null` | number or null; minimum: `0`; maximum: `100` |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/people/search" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"name":"Satya Nadella","limit":1}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: search_people -->
```json
{
  "name": "search_people",
  "arguments": {
    "request": {
      "name": "Satya Nadella",
      "limit": 1
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: search_people -->
```json
{
  "ok": true,
  "feature": "search_people",
  "data": {
    "people": [
      {
        "id": "6a1d2c3900edf351ec4270fc",
        "name": "Satya Nadella",
        "headline": "Chairman & CEO @ Microsoft",
        "current_title": "Chairman & CEO",
        "current_company": "Microsoft",
        "current_company_domain": "microsoft.com",
        "location": "Redmond, United States",
        "gender_t5": "unknown",
        "image_url": "/people_logo?id=6a1d2c3900edf351ec4270fc",
        "summary": "Current CEO at Microsoft, where our mission is to empower every person and every organization on the planet to achieve more. Joined Microsoft in 1992, and have held a variety of roles, most recently executive vice president of Microsoft's Cloud and Enterprise group, prior to beco…",
        "people_types": [
          "Angel Investor"
        ],
        "skills": [],
        "education": [
          {
            "institution": "Manipal",
            "degree": "BE",
            "years": ""
          },
          {
            "institution": "UWM",
            "degree": "Master of Computer Science",
            "years": ""
          },
          {
            "institution": "The University of Chicago",
            "degree": "MBA",
            "years": ""
          }
        ],
        "top_experience": [
          {
            "title": "Chairman & CEO",
            "company": "Microsoft",
            "years": "2014–present"
          },
          {
            "title": "member board of trustees",
            "company": "university of chicago",
            "years": "2018–present"
          },
          {
            "title": "board member",
            "company": "starbucks",
            "years": "2017–present"
          }
        ],
        "linkedin_url": "https://linkedin.com/in/satyanadella",
        "twitter_url": "https://twitter.com/satyanadella",
        "scores": {
          "people_rank": 97.27,
          "founder_rank": null,
          "executive_rank": 99.97,
          "investor_rank": 98.38,
          "college_rank": 94.62,
          "experience_rank": 99.14
        },
        "founder": null,
        "investor": {
          "num_investments": 4,
          "total_invested_usd": null
        },
        "contact_gated": true
      }
    ],
    "total_estimate": 5,
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
    "page_size": 1,
    "partial_timeout": false
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T06:47:59.290816+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-23T06:47:59.291013+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/search_people.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The Satya Nadella query returned a Microsoft professional profile, while its people_types classification included Angel Investor. The example preserves professional skills, education, experience, scores and founder/investor attributes, and omits biography and unnecessary personal attributes. A returned category is not proof of participation in a particular financing round.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.people[].id / name` | The returned profile identity. |
| `data.people[].current_title / current_company_domain` | Available professional context for matching. |
| `data.people[].people_types` | Source categories that can differ from the person's current job title. |
| `data.total_estimate / total_capped / partial_timeout` | Count precision and query completeness. |
| `data.access` | The account's effective access restrictions. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Start with a name plus a company or location when possible. Review current title, company domain and returned identifiers before associating a person with an account. Treat source role categories as labels to inspect, not verified legal or employment status.

Names are not unique. Do not attach a profile to the wrong company, reveal contact data from another source, or interpret a source category as a verified current executive appointment.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/b2b-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
