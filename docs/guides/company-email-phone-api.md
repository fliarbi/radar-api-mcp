# Company email and phone API: business contacts and professional email workflows

Start with a known company website domain. A company contact response contains
company-associated mailboxes or phone strings; it is separate from a professional's
contact record and from the company's social profile URLs.

## Inspect company identity and contact availability

POST `/v1/companies/profile`, MCP `get_company`:

<!-- contact-request: get_company -->
```json
{"domain":"razorpay.com"}
```

Inspect identity and `contacts.availability` before a contact request. Availability
is a stored-data indication, not deliverability, a contact count or proof that this
key has paid access. A missing field store can make coverage unavailable even when
the source has data elsewhere.

## Retrieve emails, phones or both

POST `/v1/contacts/company`, MCP `get_company_contacts`:

<!-- contact-request: get_company_contacts -->
```json
{"domain":"razorpay.com","fields":["emails"]}
```

Change `fields` to `["phones"]`, or `["emails","phones"]`. Select only what the
application needs. The response omits unrequested types and caps each requested
list at 25 values. It contains no department, work/personal classification, mailbox
verification timestamp or phone line-type classification. Preserve strings and
source attribution before applying any separately labelled application normalization.

The executed fictional examples below show email-only and phone-only output.
Reserved addresses and fictional numbers demonstrate the contract; they are not
live Razorpay contacts. Live paid-contact access has not been verified by these
examples. [CONTACTS.md](../CONTACTS.md) includes the actual default-key denial.

## Retrieve professional emails for people associated with the company

POST `/v1/companies/team`, MCP `get_company_team`:

<!-- contact-request: get_company_team -->
```json
{"domain":"stripe.com","group":"professionals","roles":["executive"],"limit":5,"page":0}
```

This returns professional candidates with an exact recorded company-domain match.
It does not establish current employment or a complete employee roster. Review the
returned identity and role, then send an accepted `id` to `/v1/contacts/person` with
`fields=["emails"]`. Request each person separately within contact/account limits.
Do not pass an array of employee IDs to the current contact contract.

A result can contain a person-associated email, a company fallback, no requested
email, or a denied/failed lookup. Keep those outcomes distinct. A source person phone
can prevent company fallback even when an email-only lookup is empty, because source
fallback occurs only when both person email and phone are absent.

## Business email quality and CRM field mapping

Store company contacts under the company domain. Store person-associated contacts
under the accepted person ID with `contact_source`; if a person lookup returns
`company_domain`, associate it with the company-contact result rather than asserting
it belongs to that person. Keep the originating professional profile link for review.

`available=true` means at least one requested string was returned. It does not mean
all requested types are present, that an email is a work address, or that a phone
supports calls/texts/WhatsApp. An observed company-domain suffix match can be a local
label, but subsidiaries and other company domains mean it cannot be a universal
work-email classifier. Do not infer missing addresses from naming conventions.

Empty successful lookups consume their normal operation credit. Separate discovery
calls also consume their normal credits. Contact scope, source plan, account-wide
rate limits and spending controls remain independent. See [pricing](pricing-pay-per-use.md)
and the [full variables/error guide](../CONTACTS.md).

Use [social-field retrieval](linkedin-social-data-api.md) for recorded LinkedIn, X,
Facebook and blog links. It is a separate data read, not an email or phone request.

<!-- contact-evidence -->

### Company email-only projection: fictional fixture

**`POST /v1/contacts/company`** · MCP **`get_company_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:42.815623+00:00**, HTTP **200**,
mode **`local_contact_fixture`**. Company-associated mailboxes, with phone values excluded by field selection.

Exact executed request:

<!-- contact-captured-request: contacts/company-email-only.json -->
```json
{
  "domain": "example.com",
  "fields": [
    "emails"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/company-email-only.json -->
```json
{
  "ok": true,
  "feature": "get_company_contacts",
  "data": {
    "domain": "example.com",
    "emails": [
      "sales@example.com",
      "support@example.com"
    ],
    "contact_source": "company_domain",
    "available": true,
    "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:42.814920+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](../examples/contacts/company-email-only.json).

### Company phone-only projection: fictional fixture

**`POST /v1/contacts/company`** · MCP **`get_company_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:42.987821+00:00**, HTTP **200**,
mode **`local_contact_fixture`**. Requested phone strings only; the gateway does not certify mobile status or E.164 normalization.

Exact executed request:

<!-- contact-captured-request: contacts/company-phone-only.json -->
```json
{
  "domain": "example.com",
  "fields": [
    "phones"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/company-phone-only.json -->
```json
{
  "ok": true,
  "feature": "get_company_contacts",
  "data": {
    "domain": "example.com",
    "phones": [
      "+1-202-555-0123"
    ],
    "contact_source": "company_domain",
    "available": true,
    "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:42.987105+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](../examples/contacts/company-phone-only.json).

### Employee lookup that returns a company mailbox: fictional fixture

**`POST /v1/contacts/person`** · MCP **`get_person_contacts`**.
**Executed synthetic fixture.** All contact values are fictional; no live paid-contact request was made.
Captured **2026-09-23T05:03:43.232582+00:00**, HTTP **200**,
mode **`local_contact_fixture`**. Company mailbox fallback; never relabel this as the founder's personal address.

Exact executed request:

<!-- contact-captured-request: contacts/person-company-fallback.json -->
```json
{
  "person_id": "example-founder",
  "fields": [
    "emails"
  ]
}
```

Complete saved response:

<!-- contact-captured-response: contacts/person-company-fallback.json -->
```json
{
  "ok": true,
  "feature": "get_person_contacts",
  "data": {
    "person_id": "example-founder",
    "emails": [
      "sales@example.com"
    ],
    "contact_source": "company_domain",
    "available": true,
    "note": "Only requested contact types are returned. Company-domain fallback is not a verified personal contact. Source presence does not confirm deliverability or current ownership."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T05:03:43.231867+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

[Capture, provenance and checksums](../examples/contacts/person-company-fallback.json).
