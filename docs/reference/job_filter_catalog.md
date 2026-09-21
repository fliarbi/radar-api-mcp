# Jobs API filter catalog: salaries, experience, sources and internships

[All endpoints](README.md) · [Workflow guide](../guides/hiring-signals-jobs-api.md)

Discover the typed job-search filter schema, suggestion fields and source-specific semantics before building a job-search form.

## Route, authentication and credits

**`POST /v1/jobs/filters`** · MCP tool **`job_filter_catalog`** · key scope **`jobs`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

This operation accepts an empty JSON object: `{}`.

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/jobs/filters" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: job_filter_catalog -->
```json
{
  "name": "job_filter_catalog",
  "arguments": {
    "request": {}
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: job_filter_catalog -->
```json
{
  "ok": true,
  "feature": "job_filter_catalog",
  "data": {
    "schema": {
      "additionalProperties": false,
      "properties": {
        "page": {
          "default": 0,
          "maximum": 200,
          "minimum": 0,
          "title": "Page",
          "type": "integer"
        },
        "limit": {
          "default": 20,
          "maximum": 100,
          "minimum": 1,
          "title": "Limit",
          "type": "integer"
        },
        "q": {
          "anyOf": [
            {
              "maxLength": 500,
              "minLength": 2,
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Q"
        },
        "title": {
          "anyOf": [
            {
              "maxLength": 200,
              "minLength": 1,
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Title"
        },
        "company": {
          "anyOf": [
            {
              "maxLength": 200,
              "minLength": 1,
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Employer name prefix, such as Microsoft; the Jobs source does not interpret this field as a website domain",
          "title": "Company"
        },
        "city": {
          "anyOf": [
            {
              "maxLength": 200,
              "minLength": 1,
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "City"
        },
        "country": {
          "anyOf": [
            {
              "maxLength": 200,
              "minLength": 1,
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Country"
        },
        "skills": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Skills",
          "type": "array"
        },
        "remote": {
          "default": false,
          "title": "Remote",
          "type": "boolean"
        },
        "employment_type": {
          "anyOf": [
            {
              "enum": [
                "full_time",
                "part_time",
                "contract",
                "temporary",
                "internship",
                "intern",
                "freelance"
              ],
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Employment Type"
        },
        "salary_min": {
          "anyOf": [
            {
              "exclusiveMinimum": 0,
              "maximum": 1000000000,
              "type": "number"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Source salary upper bound must reach this amount; source does not normalize currencies or periods",
          "title": "Salary Min"
        },
        "min_experience_months": {
          "anyOf": [
            {
              "maximum": 960,
              "minimum": 1,
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Min Experience Months"
        },
        "max_experience_months": {
          "anyOf": [
            {
              "maximum": 960,
              "minimum": 1,
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Max Experience Months"
        },
        "sources": {
          "items": {
            "enum": [
              "foundit",
              "shine",
              "talent"
            ],
            "type": "string"
          },
          "maxItems": 3,
          "title": "Sources",
          "type": "array"
        },
        "freshness_days": {
          "anyOf": [
            {
              "maximum": 365,
              "minimum": 1,
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Freshness Days"
        },
        "sort_by": {
          "default": "recent",
          "enum": [
            "recent",
            "relevance",
            "salary"
          ],
          "title": "Sort By",
          "type": "string"
        }
      },
      "title": "JobSearch",
      "type": "object"
    },
    "suggestion_fields": [
      "title",
      "skills",
      "company",
      "location"
    ],
    "source_employment_type_aliases": {
      "internship": "intern"
    },
    "notes": [
      "Title and employer use prefix matching; q uses source text search. Skills are OR matches.",
      "Salary minimum filters the recorded salary maximum. Source currencies and salary periods are not normalized; do not compare different currencies as equivalent.",
      "Experience is measured in months; positive bounds only. Remote=true filters remote records; false adds no onsite-only filter.",
      "The company hiring rollup is bounded and does not implement page offsets. Use dedicated internship search for the additional internship corpus."
    ]
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-21T10:48:29.884750+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-21T10:48:29.884907+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/job_filter_catalog.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The captured catalog includes salary_min, experience-month bounds, sources, salary sorting and both intern/internship inputs, as well as freelance.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.schema` | Complete accepted JobSearch input schema with bounds and enums. |
| `data.source_employment_type_aliases` | The public internship alias maps to the source value intern. |
| `data.notes` | Search matching, salary, experience, remote and rollup limitations. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Use job_filter_options for title, skills, company and location suggestions; apply the selected values to search_jobs. Dedicated internship records have additional stipend and date filters.

salary_min filters recorded salary_max, without currency or period normalization. Zero experience is not an effective source bound, so positive month bounds are required.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/hiring-signals-jobs-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
