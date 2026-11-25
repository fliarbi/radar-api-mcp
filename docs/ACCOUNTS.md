# Accounts: keys, credits and fair use

An account holds your API keys, credit balance, usage record and followed companies.
Keys are created and revoked in the developer console.

## Account and key controls

- Keys contain 256 bits of random material, are shown once, and are stored as hashes.
- Companies Radar sessions and linked News keys are encrypted at rest. API keys only identify
  their own account and cannot call account-management routes.
- Keys have explicit data-group scopes and 1–90 day expiry; rotation preserves usage.
- Ten creations per rolling 24 hours; ten active keys on Business, three otherwise.
- Revocation is effective on subsequent authentication. Already admitted requests
  may finish; revocation is not cancellation of an in-flight request.
- Email verification and account status are rechecked with Companies Radar. Password/session
  revocation semantics remain those of `/auth/me`; use explicit API-key revocation
  when disabling an integration.

## Credit ledger

Credit allocation is documented in [pricing](guides/pricing-pay-per-use.md).
Business's included API budget mirrors, but does not share, the dashboard search
counter. Companies Radar and News source quotas remain independently authoritative.

The ledger reserves the maximum cost of a request in one transaction. Success
settles actual credits; exceptions and failed composite sections refund reserved
credits. No client-supplied cost, balance or success flag is trusted. Repeated
successful retrievals are separate paid operations. Data responses are not retained
in an idempotency cache. Audit rows contain feature, time, credit totals and account
ID, not company queries, article text or financial payloads.

## Contact retrieval access

Create a key with explicit `contacts` scope to request company or professional
emails/phones; `*` alone does not include it. The console offers contact-enabled
choices, and the linked Companies Radar plan is rechecked by the source contact route.
Contact requests share a transactional account counter of ten per minute across
keys and workers, plus regular account quotas and spending limits. See [contacts](CONTACTS.md).

## Fair use: free monthly allowance

- The allowance is used before prepaid credits. With credits in the wallet and a spending limit
  set, calls continue on prepaid credits after the day's or month's free credits are gone.
- Failed calls and failed sections are refunded as for paid credits.
- Successful responses carry `meta.billing.free_credits_left_this_month`; a note is added only
  once a fifth or less of the allowance remains. `GET /account/usage` returns `free_allowance`.
- A plan with a larger included allowance (Business) is unaffected. The linked account's own plan
  limits on data depth, company-search volume and contact retrieval still apply.
- A key that expires within seven days adds a note to each response naming the key page.
