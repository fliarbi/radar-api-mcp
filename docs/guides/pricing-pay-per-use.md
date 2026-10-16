# Radar API pricing plans, usage credits and pay-per-use

The private API follows Radar's existing subscription prices and data entitlement
checks. This page separates the current Radar plan catalog from the new API
credit policy, which remains a private implementation pending activation.

## Existing Radar subscription plans

The catalog was checked against Radar's configuration on **2026-09-20**:

| Plan | Monthly INR | Monthly USD | Radar searches/month | Company-following capacity | Catalog API access |
|---|---:|---:|---:|---:|---|
| Free | ₹0 | $0 | 50 | 0 | No |
| Pro | ₹1,600 | $19 | 1,000 | 100 | No |
| Business | ₹5,000 | $60 | 5,000 | 1,000 | Yes |

The Market.ai bundled grant allows 100 Radar searches and no company follows.
It is a cross-product entitlement, not a separately purchasable free subscription.
Quoted prices are catalog amounts, not a tax-inclusive checkout quotation.
Your current effective plan is verified against Radar, including expiry or downgrade.

## Private API credit policy

Business receives a separate API budget of up to 5,000 included credits per UTC
calendar month, capped by the live plan's configured search allowance and presence
of `api_access`. This mirrors the Business allowance; it is **not a shared counter
with dashboard searches**, which remain governed by Radar. Free and Pro receive
no included API credits.

The configurable private default allows verified users on any plan to buy prepaid
credits. Operators can restrict this to Business overages with
`RADAR_PAYG_ALL_PLANS=0`. Prepaid usage does not upgrade data entitlements, unlock
restricted filters, extend financial-history access or enlarge watchlists.

| Operation | API credits |
|---|---:|
| One successful data request | 1 |
| Company brief without news | Up to 6 |
| Company brief with news | Up to 7 |
| Comparison | Up to 3 per company; 2–5 companies |
| Key management, usage checks and API watchlist changes | 0 |

A successful empty response costs one credit. Failed operations are refunded;
partial briefs and comparisons charge only successful sections. The gateway
reserves the maximum cost before starting a composite request, so enough credit
must be available up front. Repeating a successful data request is a new paid
request; there is no free-response replay or data-request idempotency cache.

## Pay-per-use price and checkout status

**Live:** one credit costs **₹0.84 or US$0.01**; buyers choose INR or USD at checkout. The
minimum top-up is US$5 worth of credits (500 credits) in either currency, and the key page
shows the exact price before opening Razorpay checkout. Prices exclude GST.

Credits are added as soon as checkout succeeds: the gateway verifies the checkout signature
and Razorpay's own payment record (order, amount, currency, captured) before crediting, and a
repeated confirmation cannot add credits twice. Refunds and disputes reverse the credits
through the signed payment webhook.

The same wallet pays for the Prism News APIs after their plan allowance (one credit per
request or full-text article).

## Control spending and understand limits

Set a monthly prepaid credit limit on the key page. Its default is zero, so prepaid
spending stays off until you opt in. Included credits are used first; prepaid
credits cover the remainder within your balance and monthly cap. There is no
automatic recharge, negative balance, or automatic overage invoice.

Usage, rate limits and in-flight reservations are account-wide across all keys, REST and
MCP. Limits follow your **usage level**, which rises with lifetime credits used and never
goes down:

| Level | Credits used (lifetime) | Requests / min | Requests at once | Prepaid credits / day |
|---|---:|---:|---:|---:|
| Starter | 0 | 60 | 3 | 5,000 |
| Growth | 10,000 | 120 | 5 | 25,000 |
| Scale | 100,000 | 300 | 10 | 100,000 |
| Premier | 1,000,000 | 600 | 20 | 500,000 |

The usage page shows included usage, prepaid usage, remaining balance, the UTC month and
your level with credits to the next one. Returned data includes a metering receipt in
`meta.billing`.

Related: [get an API key](api-keys-authentication.md), [company monitoring](company-monitoring-api.md),
[operator billing setup](../ACCOUNTS.md), [B2B data guide](b2b-data-api.md).

<!-- captured-workflow -->
## Read credits, rupees and pending usage as separate quantities

The usage response distinguishes included credits, prepaid credits and wallet
balance. A monthly prepaid limit is denominated in credits, while a payment order's
amount is in the minor unit of its currency: paise for INR, cents for USD.
Neither value is a monthly subscription price.
Check the plan response for checkout availability and the current per-credit
rate before showing a payment action.

The local demonstration deliberately configures test rates of ten paise and one
US cent per credit. The US$5 minimum is therefore 500 credits, and an INR order for
500 credits has amount 5,000 paise, or ₹50. It remains awaiting captured payment
until the signed provider callback passes verification. The usage response below
follows that synthetic captured event, so its wallet has 500 credits and no data
usage. This is evidence that the account flow
executes locally, not that a real payment was collected or that ₹0.10 is a public
Radar credit tariff.

Used-or-reserved totals include in-flight requests, preventing concurrent requests
from spending the same remaining balance. Included credits are consumed before
prepaid credits, and the monthly prepaid cap defaults to zero. Buying credits
does not expand plan-limited watchlist capacity or bypass upstream financial-history
and News entitlements. Inspect actual `meta.billing.credits` after a composite
request because unavailable sections can reduce the final charged amount.

## Worked example: executed local account response with synthetic providers

The request captured for this example was **`GET /account/usage`**.
It is separate from any broader filter variants shown earlier in this guide.

This GET request has no JSON body.

<!-- response-example: account_usage -->
```json
{
  "ok": true,
  "feature": "account",
  "data": {
    "month_utc": "2026-10",
    "plan": "business",
    "included_limit": 5000,
    "included_used_or_reserved": 0,
    "prepaid_used_or_reserved": 0,
    "wallet_credits": 500,
    "monthly_prepaid_limit": 100,
    "features": []
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-10-16T04:29:41.844740+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-10-16T04:29:40.723433+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/account_usage.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The sample follows a synthetic captured top-up, so wallet_credits=100 while data usage remains zero. Used-or-reserved values include pending requests. A UTC month and configured plan are shown alongside the balance.

See the [complete account_usage endpoint reference](../reference/account_usage.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 69 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
