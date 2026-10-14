# Private account mode: key issuance, abuse controls and prepaid API usage

Account mode adds a developer console, account-owned keys, a transactional usage
ledger, API watchlists and Razorpay prepaid orders to the standalone gateway.
It is opt-in and has not been deployed to the public Radar service. Existing
production identity, subscription and News products are not modified.

## Identity and activation

Set `RADAR_ACCOUNTS_ENABLED=1`, `RADAR_ACCOUNTS_DB` to an owner-only local SQLite
file, and `RADAR_ENCRYPTION_KEY` to a persistent Fernet key from your secret manager.
Use `Fernet.generate_key()` to generate it privately; never commit it. Preserve
this key with encrypted backups: losing it prevents decryption of linked sessions.

`POST Radar/auth/me` validates every supplied or stored Radar session. The adapter
requires `user._id`, explicitly true `email_verified`, no active `disabled`,
`banned` or `suspended` flag, a known effective plan, and plan details. Missing or
unreadable identity data fails closed. The gateway never accepts a caller-supplied
account ID or plan. An identity outage stops access instead of reusing a stale grant.

Account mode entirely replaces the JSON preview-key store; it does not fall back
to static keys. Stdio requires this same configuration and ledger. Remote clients
should use HTTP so server credentials and account storage stay on the server.

Expose `/developer` and its two static assets through an approved private proxy.
To reuse Radar's existing `radar_auth_token` browser session, host the console on
the same trusted origin and route `/account/*`, `/v1/*` and `/mcp` to this gateway.
Do not overwrite an existing route without checking its owner. The package itself
includes an [optional dashboard integration](../integrations/fliar-dashboard/README.md)
that adds a local Radar API & MCP help panel. It does not deploy production proxy
or dashboard files. For a same-origin prefix, start Uvicorn with the matching
`--root-path`; console assets, account requests and displayed connection URLs
retain that prefix. The local-development session
field is for private integration testing, not a public SSO handoff mechanism.

Use TLS, explicit allowed hosts and the exact browser origin. The console has a
noindex header, no-referrer policy, a restrictive CSP and no third-party analytics.
Razorpay's checkout script loads only after a user chooses to buy credits. Public
indexing must be directed at approved documentation, never this console.

## Account and key controls

- Keys contain 256 bits of random material, are shown once, and are stored as hashes.
- Radar sessions and linked News keys are encrypted at rest. API keys only identify
  their own account and cannot call account-management routes.
- Keys have explicit data-group scopes and 1–90 day expiry; rotation preserves usage.
- Ten creations per rolling 24 hours; ten active keys on Business, three otherwise.
- Revocation is effective on subsequent authentication. Already admitted requests
  may finish; revocation is not cancellation of an in-flight request.
- Email verification and account status are rechecked with Radar. Password/session
  revocation semantics remain those of `/auth/me`; use explicit API-key revocation
  when disabling an integration.

## Abuse and resource controls

| Control | Account-mode behavior |
|---|---|
| Peer request budget | 300 requests/minute from the socket peer, before identity verification |
| Account request budget | 60 authenticated HTTP requests or stdio tool calls/minute across keys |
| Concurrent data requests | Maximum 3 per account; composites additionally bound internal fanout |
| Request size | 256 KiB, including chunked account and webhook requests |
| Data response size | Default 8 MiB from each data service |
| Request duration | 120 second hard ceiling around a metered operation |
| Query bounds | Typed filters, result/page caps, domain validation, bounded comparison size |
| Quota storage failure | Request fails closed with a service error |
| Spending | Reserve included/prepaid credits atomically before data work; never overdraw |

Peer identities are keyed hashes. Forwarded IP headers are ignored unless the socket
peer is listed in `RADAR_TRUSTED_PROXIES` (exact addresses or CIDRs). Then
`X-Forwarded-For` is read right to left through trusted hops only, so a client-prepended
address is never believed and a malformed hop ends the walk. Without that setting, the
peer budget applies to the proxy collectively.

New API accounts are admitted at most `RADAR_NEW_ACCOUNTS_PER_IP_DAY` (default 3) per
client address per day and `RADAR_NEW_ACCOUNTS_PER_HOUR` (default 100) overall. Existing
accounts and API-key calls never count. Account/key rotation cannot evade account limits.
CAPTCHA, email delivery and network DDoS protection remain responsibilities of the
identity system and deployment edge; this gateway does not claim to solve them.

SQLite WAL transactions support multiple workers **on one host** using the same
local disk. Do not put the SQLite ledger on NFS or run independent per-replica databases:
that would split quotas. For several hosts, install the `postgres` extra and set
`RADAR_ACCOUNTS_DATABASE_URL=postgresql://...`; every host must use the same database.
Each ledger transaction takes one PostgreSQL advisory lock, giving the same
all-writers ordering as SQLite, so reservations, wallets and rate counters stay exact
across hosts. Use a role limited to that database, TLS to the server and encrypted
backups. Counter buckets expire and are pruned on use. Usage/payment audit
records are retained; size storage and define retention before sustained service.

## Credit ledger

The private allocation is documented in [pricing](guides/pricing-pay-per-use.md).
Business's included API budget mirrors, but does not share, the dashboard search
counter. Radar and News upstream quotas remain independently authoritative.

The ledger reserves the maximum cost of a request in one transaction. Success
settles actual credits; exceptions and failed composite sections refund reserved
credits. No client-supplied cost, balance or success flag is trusted. Repeated
successful retrievals are separate paid operations. Data responses are not retained
in an idempotency cache. Audit rows contain feature, time, credit totals and account
ID, not company queries, article text or financial payloads.

After a crashed worker, pending reservations older than ten minutes are refunded
on the account's next data reservation. The operation deadline is two minutes,
so ordinary running calls do not overlap this recovery interval. Usage can show
those reserved credits until recovery runs. A database failure during settlement
is an error, not a successful billable-response claim; investigate pending rows.

## Configure prepaid checkout

Required environment variables are `RADAR_CREDIT_PRICE_PAISE`,
`RADAR_RAZORPAY_KEY_ID`, `RADAR_RAZORPAY_KEY_SECRET` and
`RADAR_RAZORPAY_WEBHOOK_SECRET`. With any missing or zero-price setting, checkout
is disabled. Use provider test credentials for integration testing; activating
real payments or public deployment is a separate owner decision.

`POST /account/topups` accepts 100–100,000 credits, with a ₹100,000 per-order ceiling
and five order attempts per account per hour. The gateway fixes INR and calculates
the amount from its configured rate. The returned order ID, amount, currency and
public provider key configure Razorpay Checkout. Creating an order does not debit
an account or grant API credits. Do not automatically retry an uncertain order
creation; reconcile the provider order before creating another checkout.

Register `/billing/webhook` for `payment.captured`, `refund.processed` and
`payment.dispute.created`. The gateway verifies an HMAC-SHA256 signature over the
unmodified raw body and matches the stored order and captured payment amount/currency.
Unique order and payment IDs make repeated deliveries harmless. Unrelated capture
events are acknowledged without crediting a wallet. Authorized-only events do not
grant credits. Client checkout callbacks are informational only.

Refund/dispute processing removes the original credit grant as far as the available
wallet permits and suspends the API account for reconciliation. Even a partial
refund freezes access; an operator must reconcile spent credits and the actual
refund before clearing `enabled=0`. Out-of-order reversal events return 409 for
retry until capture is recorded. Preserve the old webhook secret during provider
rotation/retry planning; this version accepts one configured secret at a time.

There is no operator HTTP endpoint that grants arbitrary credit, no automatic
charge, no automatic subscription creation and no public billing activation in CI.
Provider sandbox checkout, tax treatment, invoices, refund policy, consumer-facing
terms and production monitoring must be configured before commercial activation.

Official integration references:
[Razorpay orders](https://razorpay.com/docs/api/orders/create/),
[webhook validation and delivery behavior](https://razorpay.com/docs/webhooks/validate-test/),
[payment event payloads](https://razorpay.com/docs/webhooks/payloads/payments/).

## Developer console design and validation

The console uses a compact research-workspace layout: one account connection,
key rows, an explicit usage ledger summary, spending controls and a company list.
The palette is paper white `#ffffff`, cool background `#f5f8fc`, ink `#17324d`,
action blue `#1758a0`, border `#c8d5e2` and focus amber `#cc7800`. Aptos/Trebuchet
sets interface text; Consolas sets request examples. Alignment is left-led with
responsive forms, visible labels and keyboard focus. The primary visual emphasis
is key creation, not a promotional pricing hero. Repeated decorative metric cards
were removed in favor of one readable usage line and a key table.

## Contact retrieval access

Create a key with explicit `contacts` scope to request company or professional
emails/phones; `*` alone does not include it. The console offers contact-enabled
choices, and the linked Radar plan is rechecked by the source contact route.
Contact requests share a transactional account counter of ten per minute across
keys and workers, plus regular account quotas and spending limits. See [contacts](CONTACTS.md).
