# Contact and social data investigation: source behavior, evidence and gaps

Reviewed on **2026-09-23** to support company email/phone retrieval, founder identity
linkage, professional details and recorded LinkedIn/social references. Read the
[structured evidence manifest](contact-workflow-evidence.json) for source file
fingerprints and capture references. This review made no live paid-contact request
and sent no messages.

## Source paths reviewed

| Component | Source location | Relevant behavior |
|---|---|---|
| Company contact handler | Radar `blueprints/company_search/routes.py`, `contact_reveal_func` | Linked source plan gate before contact lookup; company email/phone strings capped at 25; source lookup exceptions can appear as empty arrays |
| Person contact handler | Radar `blueprints/people_search/routes.py`, `_resolve_person_contact` / `people_contact_reveal` | Prefers person contact; company fallback only when both person email and phone are absent; an unresolved ID gets empty values |
| Gateway projection | `radar_api/company_views.py`, `contacts_payload` | Selects requested types, trims exact strings, removes exact duplicates, caps 25/type and keeps origin labels |
| Gateway access and metering | `radar_api/service.py`, `run` / contact dispatch | Explicit contacts scope, linked source session, source gate, account rate and successful-operation metering |
| Public inputs | `radar_api/models.py` | One domain or one person ID per contact request; only emails/phones accepted; other discovery inputs are separate models |
| Professional and company views | People search, `radar_api/research.py`, `radar_api/profiles.py` | Name/company-prefix discovery, exact recorded-domain team filtering, separate company people/social fields |

## Observed founder identity linkage

Company founder records listed Shashank Kumar and Harshil Mathur. The new live
name-plus-company query for Shashank returned one professional candidate, including
recorded domain `razorpay.com`, a source ID, LinkedIn/X references, education,
experience and skills. The same query for Harshil returned no rows.

The broader professional founder-role query returned Ammu Tiwari, Shashank Kumar
and Venkatesan Vaidhyanathan with the same recorded company domain. Two names do
not occur in the captured company founder list. This is a disagreement between
source views. The review does not resolve which affiliations/roles are stale or
incorrect, and it does not authorize treating every founder-tagged profile as a
confirmed company founder.

Practical consequence: preserve the company founder record and professional
candidate separately. Compare identity, exact domain and professional references;
leave absent or ambiguous joins unresolved. Do not automatically acquire contacts
for all profiles merely because a founder tag and company domain were returned.

## Contact resolution semantics

1. Person source email uses its confirmed list when populated, otherwise the general
   email list. Phone values come from the person record. The gateway does not expose
   per-email confirmation status, date, verifier or deliverability evidence.
2. If either person email **or phone** exists, the source stays person-level. Thus an
   emails-only request can be empty even when a person phone exists and a company
   mailbox could be found elsewhere. Fallback is not applied independently per field.
3. If both are absent, the source can look up the recorded current company's contact.
   Its origin remains `company_domain`; it is not the professional's verified address.
4. `available` is calculated after selecting the requested fields. Unrequested types
   are omitted, so absence of a phones key is not a phones-coverage conclusion.
5. Company/source lookup failures are not uniformly distinguishable from empty
   results. Successful empty data is therefore an unresolved observation, not a
   guarantee that no contact exists. The gateway cannot invent that distinction.

The eight [local fixture captures](../examples/contacts/index.json) exercise company
email-only, company phone-only, direct person, fallback, a phone-only source with an
empty email request, no data, unknown provenance and source plan denial. Every
fixture is explicitly labelled and uses fictional contact values. These are actual
gateway executions against synthetic upstream payloads, not live paid-contact success.

## Supported capabilities versus open gaps

| User intent | Implemented path | Current gap / boundary |
|---|---|---|
| Founder details plus contacts | Company founder record → professional discovery → accepted ID → separate contact lookup | No guaranteed company-founder/person identity join; source views can disagree |
| Employee / professional emails | Exact recorded-domain professional team → one person contact lookup per selected ID | No exhaustive roster, bulk contact input or current-employment verification |
| Company business contacts | One company domain and selected emails/phones | No department, named-inbox owner or line-type classification |
| Work emails only | Source email strings and their record association | No `email_type` filter; suffix matching alone cannot certify work-email type |
| Verified emails | Source strings; source may prefer an internal confirmed list | No exposed verification evidence, SMTP status or current deliverability test |
| Suppress company fallback at the server | Inspect `contact_source` and decline fallback in the client | No `allow_company_fallback` input flag |
| Filter lists by contact availability | Individual company profile availability indicators | No `has_email`/`has_phone` discovery predicate in the public models |
| LinkedIn and social references | Company social field and person professional cards | No exact reverse-LinkedIn-URL lookup or social messaging endpoint |
| Company LinkedIn metrics and posts | Selected social field reads profile logs and distinct stored posts independently of derived enrichment | Dated observations; no universal platform coverage, live follower guarantee, person-post or comment-thread reader |
| Contact-level history and pagination | Bounded selected arrays | No source-total, per-address timestamps or contact-array pagination |

These gaps are recorded as product/coverage work, not advertised as available
variables. [24 readable request recipes](../CONTACT_REQUEST_RECIPES.md) and
[their JSON form](../examples/contacts/requests.json) validate against
the current public models. They demonstrate accepted syntax; only separately
labelled captures claim execution.

## Documentation changes resulting from this review

[CONTACTS.md](../CONTACTS.md) now connects founder/company identity, professional
detail, source attribution, work-email limitations, social links, key scopes,
error handling and billing. Three specialist guides cover
[founder contacts](../guides/founder-contact-data-api.md),
[company email/phone workflows](../guides/company-email-phone-api.md), and
[LinkedIn/social links](../guides/linkedin-social-data-api.md).

The documentation checker validates every recipe and displayed request against
its model, compares each displayed response with its saved capture, checks hashes
and retains the source arrays. Local checks also compare new captures with their
ignored original responses. Historical search research is retained separately in
[the research index](README.md).
