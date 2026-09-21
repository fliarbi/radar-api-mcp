# Company email and phone API; professional contact lookup

Email addresses and phone numbers are separate retrieval actions. Company profiles
return availability booleans; search and brief responses do not automatically
reveal the values. The gateway uses Radar's existing contact handlers and preserves
their paid-plan checks. It does not query the contact store directly.

## Obtain a contact-enabled API key

In the developer console, choose **All data plus contact retrieval** or
**Contact retrieval only** when creating a key. In account mode, the equivalent
JSON POST to `/account/keys`, authenticated with your Radar session, is:

```json
{"name":"Company research","scopes":["companies","people","contacts"],"expires_days":30}
```

The explicit `contacts` scope is required even when the key has `*`. Older keys
remain valid for their existing data operations and do not gain contact access.
The linked Radar account must also pass the source paid-plan check; buying API
credits does not override that check. The source currently allows its paid tiers
and denies anonymous/Free contact retrieval. Gateway API plan eligibility still
applies independently. Operator-issued keys support repeated `--scope` arguments.

## Request a company's business contact

POST to `/v1/contacts/company`, or call MCP `get_company_contacts`:

```json
{"domain":"razorpay.com","fields":["emails"]}
```

Use `fields:["phones"]` for phone numbers or explicitly select both types. Each
request addresses one company. Responses include only requested contact types,
with at most 25 values of each type. No message is sent by this operation.

## Request a professional's contact

Get the person's ID from `search_people`; then POST to `/v1/contacts/person`,
or call MCP `get_person_contacts`:

```json
{"person_id":"ID_FROM_SEARCH_PEOPLE","fields":["emails","phones"]}
```

`contact_source=person` means the source returned a person-level record.
`contact_source=company_domain` means it fell back to the person's current
company's business contact details. A company mailbox is not a verified personal
address. `none`/`unknown`, missing values and source uncertainty remain explicit.
Presence does not establish deliverability or current ownership.

## Successful response shape and live access evidence

The following is a **synthetic contract example**, using reserved example.com and
a fictional phone number. It is not a live contact or a production-access capture:

```json
{
  "person_id":"example-person",
  "emails":["sales@example.com"],
  "phones":["+1-202-555-0123"],
  "contact_source":"company_domain",
  "available":true,
  "note":"Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
}
```

This is the `data` portion of the usual envelope. The checked-in primary captures
show the real default-key `403 scope_required` response, not invented paid-contact
success. Tests cover successful source shapes, one-type selection, fallback labels,
plan denials, rate limits and shared account metering. Production paid-contact
retrieval has not been verified in this preview.

## Limits and billing

Contact requests have a separate limit of 10 per minute per API account, shared by
its keys. Manually issued preview keys are limited individually. The regular API
rate, account concurrency and monthly-credit/spending limits also apply. Account
mode charges one credit for a successful contact request; access denials and
upstream failures do not consume operation credits. Empty successful responses
are still completed lookups; they are not guaranteed contacts.

See [company contact reference](reference/get_company_contacts.md),
[person contact reference](reference/get_person_contacts.md),
[API-key onboarding](guides/api-keys-authentication.md) and [pricing](guides/pricing-pay-per-use.md).
