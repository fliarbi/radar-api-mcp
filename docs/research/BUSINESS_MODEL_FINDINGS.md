# Business-model and revenue-model scenario review

Reviewed September 25, 2026. This work adds ten documentation recipes and checks
existing filter behavior; it does not introduce a new data endpoint or establish
a live commission-based company cohort.

## Source findings

The gateway's [filter catalogue](../../radar_api/catalog.py),
[request models](../../radar_api/models.py),
[operation handlers](../../radar_api/service.py) and
[industry vocabulary](../../radar_api/industry_options.py) were inspected together
with Radar's company-search and semantic-search handlers.

| Finding | Documentation consequence |
|---|---|
| `business_models` and `revenue_models` are distinct dimensions | Activity, monetization and precise pricing must not be collapsed into one field |
| `commission on transaction` is an existing revenue option | Use this exact label for candidate discovery; do not invent a `commission per deal` option |
| `Investment Management & Fund Operators` is an existing industry option | The lead structured recipe uses this label and provides a separate semantic route for other investment-service categories |
| Revenue-model lists use OR matching within the dimension | The hybrid recipe requires a separate client-side all-of check |
| Investor entity mode rewrites certain activity filters to portfolio criteria | An investor's portfolio preference does not establish its own operating business model |
| Company columns expose singular `business_model` / `revenue_model` display fields | Examples request those columns separately, then retrieve plural classification arrays for review |
| Commission rate, payer, fee trigger and revenue share have no dedicated request fields | Preserve these as client review questions, not guaranteed API output |
| An existing software lookup supplies `software development` | Scenario 60 uses the saved lookup as historical vocabulary evidence |
| Saved Swiggy data has a Marketplace flag without a commission revenue label | Market-category evidence cannot manufacture a missing revenue tag |

## What was executed

The [recipe manifest](business-model-recipes.json) records ten cases,
all request bodies, local catalogue outputs and hashes of the reviewed gateway
files and saved examples. Static industry/revenue option requests were executed
against the real local handler with an upstream implementation that raises if
any outbound request is attempted. These outputs have `http_executed=false` and
`outbound_requests=0`; they are not live HTTP/company-result captures.

Business-model typeahead depends on the upstream vocabulary source. The investment
lookup remains a request example; no new investment vocabulary response is claimed.
The software lookup and Swiggy projection are explicitly dated saved evidence.
The checked-in company-store shutdown finding was respected: no source shard was
queried or restarted for this documentation task.

The new pages are numbered 51–60, but the original fifty-case baseline, captured
requests, outputs and audit totals remain unchanged. Request syntax and declared
catalogue membership are testable offline. Neither proves nonempty results,
current commercial fees, source truth, or current source availability.

## Review and reproduction

```bash
python scripts/build_business_model_scenarios.py
python scripts/check_business_model_scenarios.py
python scripts/check_docs.py
```

The first command renders the authored recipes and runs static catalogue lookups.
It cannot call an upstream. The checker validates REST and MCP bodies, catalogue
values, evidence projections, source hashes, page links and the hybrid-model
example. The legacy scenario builder restores the new index section after
regenerating the original captured pages, so future documentation builds keep
both sets discoverable.

For live execution later, use the operator-supplied API URL and key from the
[onboarding guide](../guides/api-keys-authentication.md). Capture the unchanged
request, source dates, restriction metadata and full result before labeling a
recipe a successful live example. Preserve failures and empty qualified pages.
