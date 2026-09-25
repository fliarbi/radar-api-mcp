# Business-model and revenue-model API: find commission, subscription and service businesses

Use Radar to discover companies by **what they do** and **how they are classified
as earning revenue**. For “investment companies earning commission per deal,”
start with the investment-services industry and the exact revenue label
`commission on transaction`, then inspect the company's own classification and
commercial evidence. A revenue-model tag does not specify the billing event or fee.

The [complete investment-commission scenario](../scenarios/51-investment-commission-per-deal.md)
includes a structured search, a natural-language alternative, US location filtering,
an investor-entity variant, listing columns and separate classification reads.

## Choose the right filter dimension

| What you need | Public field or operation | Interpretation |
|---|---|---|
| Investment-service companies | `filters.industries` | The catalogue contains `Investment Management & Fund Operators`; this is a broad industry, not proof of brokerage |
| A specific business activity | `filters.business_models` | Discover the current exact label with `company_filter_options`; activity is separate from monetization |
| Commission-based monetization | `filters.revenue_models` | Use `commission on transaction`; `commission per deal` and `success fee` are not catalogue options |
| US or India company location | `filters.locations` | Recorded company geography, not every customer market or place of incorporation |
| A natural-language service description | `semantic_company_search` | Candidate discovery; wording and source matching still need review |
| Own company models in a shortlist | `get_company_columns` | Request `business_model` and `revenue_model` display columns separately |
| Full classification with dates and coverage | `get_company_field`, `field=classification` | Read the plural arrays `value.business_models` and `value.revenue_models` |
| Investor entities and portfolio research | `search_investors`, investor detail tools | Portfolio preferences and the investor firm's own revenue model are different questions |
| Exact revenue or profit amount | `screen_company_financials`, `get_financials` | Financial amounts and periods are separate from revenue-model labels |

The naming is deliberate: filters and classification arrays use **plural**
`business_models` / `revenue_models`; listing columns use **singular**
`business_model` / `revenue_model`. Do not pass a pricing percentage as a model label.

## Investment companies with commission per deal

**POST `/v1/companies/search`** · MCP `search_companies`:

<!-- business-request: 51-investment-commission-per-deal-search -->
```json
{
  "filters": {
    "industries": ["Investment Management & Fund Operators"],
    "revenue_models": ["commission on transaction"]
  },
  "match_mode": "strict",
  "page": 0,
  "limit": 20
}
```

The [captured response](../scenarios/51-investment-commission-per-deal.md#captured-output-for-this-exact-request)
returned HTTP 200 with no strict companies: the source supplied 20 expanded
candidates and strict mode excluded all 20. It retained `next_page=1`.
This is not evidence that commission-based investment companies do not exist. The
[scenario](../scenarios/51-investment-commission-per-deal.md) shows the exact local
vocabulary output and copyable curl/MCP commands. The API key and base URL come
from your operator; see [key onboarding](api-keys-authentication.md).

The business question has two tests. The API can screen for the recorded industry
and commission label. To establish **per completed deal**, review dated fee terms
or source descriptions specifying the billable event, payer and fee basis. If
those details are absent, keep the row as a commission-tagged candidate with
`billing event unknown`. Do not assign an assumed percentage.

Use the semantic variant for advisers or brokers categorized outside the broad
investment-management industry. It is a separate discovery request with different
coverage, so retain its request body and origin when combining results.

## Ten practical business-model scenarios

| Scenario | Question and key distinction |
|---|---|
| [51 · Investment commissions](../scenarios/51-investment-commission-per-deal.md) | Investment-service companies with transaction commission; verify the completed-deal trigger |
| [52 · Investment success fees](../scenarios/52-investment-advisers-success-fees.md) | Advisers and deal platforms; distinguish success fees from retainers |
| [53 · Property brokerage](../scenarios/53-real-estate-brokerage-commission.md) | Property commissions; distinguish sales, leases, listings and management fees |
| [54 · Insurance distribution](../scenarios/54-insurance-broker-commission.md) | Commission-based intermediaries; separate commission revenue from premium volume |
| [55 · Recruitment fees](../scenarios/55-recruitment-placement-fees.md) | Placement, retained search and staffing; two model labels are an OR screen |
| [56 · Marketplace take rates](../scenarios/56-marketplace-transaction-commission.md) | Transaction monetization; a Marketplace flag does not establish a commission tag |
| [57 · Subscription plus commission](../scenarios/57-hybrid-subscription-and-commission.md) | Require both tags by checking each classification after the OR candidate search |
| [58 · Lending and interest](../scenarios/58-lending-interest-vs-commission.md) | Separate interest-earning lenders from fee-based intermediation |
| [59 · Data vendors and licensing](../scenarios/59-data-vendors-licensing.md) | Selling data, licensing, B2B buyers and actual billing units |
| [60 · Software services](../scenarios/60-software-services-business-model.md) | Combine a saved software-development business-model label with fee-for-service revenue |

Each page has request bodies, curl, MCP, variants and a review sequence. The
[machine-readable recipe manifest](../research/business-model-recipes.json)
contains all typed requests, actual offline catalogue outputs and source hashes.
All ten main requests now have captured responses: two populated lists, six empty
strict pages and two account denials. Four additional captures show the profile
and classification of a company returned by each populated search. Additional
variants remain recipes unless a response is shown. No fee schedule is inferred.

## Revenue labels are not pricing terms

The reviewed catalogue includes `fee-for-service`, `e-commerce - product`,
`e-commerce - service`, `physical commerce`, `advertising`, `subscription`,
`commission on transaction`, `donations`, `sponsorship`, `affiliate marketing`,
`renting / leasing`, `lending`, `freemium`, `licensing`, `interest` and `selling data`.
Query `/v1/companies/filter-options` for your chosen field rather than guessing.

`B2B`, `pay-per-use`, `success fee`, `carried interest`, `management fee` and
`commission per deal` are not revenue-model options in that catalogue. They may
be useful research wording, but accepted free-text syntax does not make a string
a supported taxonomy value. There is no dedicated commission-rate, fee-payer,
fee-trigger, take-rate-percentage or revenue-share filter in this gateway.

A subscription tag does not establish monthly billing, annual recurring revenue
or an active paid product. `fee-for-service` does not establish hourly pricing.
`commission on transaction` does not establish a particular fee percentage.
Funding `deal_sizes` describe financing bands, not service prices.

## OR within one filter; AND across dimensions

Values within a filter generally form an OR candidate condition. An industry
filter and a revenue-model filter are combined across dimensions. For example,
`revenue_models=["subscription", "commission on transaction"]` must not be presented
as requiring both models. Scenario 57 includes an explicit all-of check using the
separate classification response, array coverage and an `unknown` state.

For “commission only, no subscription,” search commission candidates and review
the classification. No general negative model predicate is exposed. Even a
complete returned snapshot without a subscription tag does not prove the
company never offers subscriptions. Preserve the source's date and coverage.

## Company business model versus investor portfolio preference

Use company search when the question concerns the firm's own business activity.
`search_investors` forces investor entity mode. In that mode Radar can interpret
sectors, markets and business-model filters as **portfolio preferences**. An
investor matching a business-model term may invest in companies with that model;
it does not follow that the investor itself operates that way.

The commission-label investor variant in scenario 51 uses `revenue_models` and
explicitly includes expanded candidates for review. It does not use a portfolio
business-model filter as evidence of the investor's own model. Inspect each
candidate's own classification and the [investor matching notes](investor-data-api.md#investor-search-matching-and-portfolio-filters).

## Build a reviewable result

Search returns compact cards. Read columns for a shortlist, request `get_company`
for `available_fields`, then POST a separate `classification` request for each
selected domain. Use `overview` and `products` when available for business context.
Additional requests retain their normal plan/credit and rate-limit behavior.

| Suggested output column | Source and meaning |
|---|---|
| Company, domain | The returned company card; retain the resolved identity |
| Business-model labels | `data.value.business_models` from the classification response |
| Revenue-model labels | `data.value.revenue_models`; keep the full returned array |
| Classification updated at | `data.updated_at`; retrieval time is a different timestamp |
| Search tier and restrictions | `data.companies[].match_tier`, `data.matching` and `data.access` from discovery |
| Classification coverage | `data.status`, `data.coverage.partial`, and `data.coverage.arrays` from the field response |
| Billing event, payer, rate, fee unit | Client-reviewed source evidence when available; these are **not promised API fields** |
| Review status | A client conclusion such as `tag observed / fee trigger unknown`; not a server-issued certification |
| Evidence link and date | Retain the underlying company/source URL and its date when reviewed |

The saved [Swiggy example](../scenarios/56-marketplace-transaction-commission.md#saved-evidence-a-marketplace-flag-is-not-a-commission-tag)
shows a Marketplace flag with `e-commerce - service` and `subscription` labels,
but no commission label. This demonstrates a source-evidence limit, not a claim
about Swiggy's actual fee contracts. Brand familiarity must not fill missing tags.

Do not report a complete market count from a bounded page. Follow continuation
hints, retain partial/errors, inspect restricted filters and record the request
used for each cohort. The [filter guide](../FILTERS_AND_LISTINGS.md),
[financial-filter guide](financial-filters-data-api.md) and
[research findings](../research/BUSINESS_MODEL_FINDINGS.md) explain the boundaries.
