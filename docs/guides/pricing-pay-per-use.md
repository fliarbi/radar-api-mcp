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

**No per-credit price has been set. Checkout is disabled by default.** The operator
must configure an INR price in integer paise and the payment-provider credentials.
The console then displays the exact configured price before opening checkout.
This repository does not assume a new public tariff or charge a real payment.

Top-ups add credits only after a signed Razorpay `payment.captured` event matches
the stored order, amount and currency. Repeated payment events cannot add credits
twice. A browser checkout success message does not itself increase the balance.

## Control spending and understand limits

Set a monthly prepaid credit limit in the console. Its default is zero, so prepaid
spending stays off until you opt in. Included credits are used first; prepaid
credits cover the remainder within your balance and monthly cap. There is no
automatic recharge, negative balance, or automatic overage invoice.

Usage, rate limits and in-flight reservations are account-wide across all keys,
REST and MCP. The private default is 60 authenticated requests per minute and
three concurrent data requests. Each account's usage page shows included usage,
prepaid usage, remaining balance and the UTC month. Returned data includes a
metering receipt in `meta.billing`.

Related: [get an API key](api-keys-authentication.md), [company monitoring](company-monitoring-api.md),
[operator billing setup](../ACCOUNTS.md), [B2B data guide](b2b-data-api.md).
