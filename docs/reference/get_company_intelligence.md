# Company intelligence API: scores, risks and business context

[All endpoints](README.md) · [Workflow guide](../guides/competitor-intelligence-api.md)

Retrieve Radar's computed view of a company's market position, innovation, management signals, financial trajectory, risk and investment readiness. This endpoint is useful for deciding which evidence to investigate next. Its scores and narratives are derived assessments and should remain separate from financial statement facts.

## Route, authentication and credits

**`POST /v1/companies/intelligence`** · MCP tool **`get_company_intelligence`** · key scope **`companies`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

| Parameter | Required / default | Type and accepted values |
|---|---|---|
| `domain` | required | string |

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/intelligence" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com"}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: get_company_intelligence -->
```json
{
  "name": "get_company_intelligence",
  "arguments": {
    "request": {
      "domain": "microsoft.com"
    }
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: get_company_intelligence -->
```json
{
  "ok": true,
  "feature": "get_company_intelligence",
  "data": {
    "domain": "microsoft.com",
    "intel": {
      "company_meta": {
        "country": "united states",
        "current_stage": "Unfunded",
        "estimated_revenue": null,
        "progress_label": "",
        "size_label": "",
        "markets": [
          "business intelligence"
        ],
        "total_funding": null,
        "valuation": null
      },
      "computed_at": "2026-09-19T17:19:34Z",
      "investment_readiness": {
        "breakdown": {
          "earnings": 82,
          "financial_trajectory": 100,
          "innovation": 55,
          "management": 55,
          "market_position": 100,
          "risk": 60
        },
        "label": "Moderate",
        "private_equity_score": 55,
        "public_shares_score": 56,
        "score": 56
      },
      "risk_profile": {
        "bankruptcy_events": 0,
        "lawsuits_360d": 24,
        "lawsuits_all": 583,
        "lawsuits_as_defendant": 459,
        "layoffs_180d": 5,
        "regulatory_360d": 12,
        "score": 60,
        "warning_flags": [
          "Recent Layoffs",
          "Active Litigation"
        ]
      }
    },
    "computed_at": "2026-09-19T17:19:34.120000Z"
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:58:45.958534+00:00",
    "partial": false,
    "notes": [
      "Scores and narratives are derived assessments. Financial metrics are retrieved evidence."
    ],
    "provider": "Fliar BI"
  }
}
```

This is the captured **response excerpt**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/get_company_intelligence.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
An omitted field or array tail in this excerpt is not evidence that the server
omitted it; original totals and returned counts have deliberately been preserved.

The live Microsoft response included intelligence components and an earnings archive with a gated history. The excerpt selects a few scores and coverage fields; it does not imply the other source components were absent.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.domain / computed_at` | The requested company and the source computation time, distinct from gateway retrieval time. |
| `data.intel.company_meta` | Available size, stage, market and other company context. |
| `data.intel.investment_readiness` | Derived labels and scores, not a recommendation issued by this gateway. |
| `data.intel.risk_profile` | Derived risk indicators and component counts when supplied. |
| `data.intel.earnings` | Source earnings context; use get_financials for normalized metric provenance. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Read the computation date and the component you need, then retrieve the supporting company events or financial metrics separately. Build a research view that labels a risk score as derived and a filing-sourced revenue value as retrieved financial evidence. Preserve a gap when a component is absent.

Do not sum unrelated score families, treat a score as a probability, or label a computed assessment as an audited financial value. The gateway does not establish the source scoring model's calibration.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/competitor-intelligence-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
