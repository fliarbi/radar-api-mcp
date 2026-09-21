# Radar source review: company fields, listings, filters and contacts

Reviewed on 2026-09-21 before changing the gateway contract. This record identifies
the current product behavior used to design the API. It is not a claim that every
Radar action or every stored value has been independently verified.

| Radar behavior inspected | Source implementation | Gateway consequence |
|---|---|---|
| Company view loads identity, intelligence, events, enrichment and people through distinct requests | `radar/src/js/profile/company-page.js`; company intel/events/enrichment handlers | Compact identity and summaries; separate detail requests |
| Hero images use a Radar logo route with fallback handling | `company-page.js` logo helpers; `company_logo/routes.py` | Do not expose stored provider CDN logo URLs; use Radar's first-party image fallback, which may return a favicon |
| Search sidebar contains taxonomy, models, geography, funding, financial, web/app and founder-background groups | `radar/src/js/filters/search-system.js`; `radar/public/search.php`; `company_search/routes.py` filter mapping | Typed public filter model and discoverable vocabulary/schema |
| Company results have a separate Show columns request | `company_search/routes.py`: `/cols`, `_RESULT_COLUMN_MAP` | Separate bounded selected-column endpoint; preserve formatted-value limitations |
| Result ordering recognizes an allowlist of financial, size and derived-score sorts | `company_search/routes.py` sort mapping | Explicit public sort enum; no arbitrary sort expressions |
| Business-model suggestions use a dedicated hybrid vocabulary handler | `company_search/routes.py`: `/vertical_suggest` | Call the actual business-model suggestion route; do not substitute industry labels |
| Company email/phone reveal checks the account plan before reading contact values | `company_search/routes.py`: `/contact`, `/contacts_bulk` | Separate contact endpoint, explicit key scope, source entitlement checks and bounded output |
| People suggestions and search cover schools, degrees, skills, company name/domain, role and seniority | `people_search/routes.py`: `/suggest`, `_build_mongo_filter` | Expanded professional filters and a dedicated suggestion endpoint |
| Person contact lookup can fall back to company-domain contacts | `people_search/routes.py`: `_resolve_person_contact`, `/contact` | Preserve `contact_source`; never present fallback as a verified personal address |
| Source search plan gates can strip filters, cap rows and consume source searches | `services/entitlements.py` and company search gate | Preserve restrictions and source limits; API credits do not grant wider source access |

The previous gateway's Mongo profile reader copied `descriptive.logo_url` and
defaulted to all seventeen rich sections. That produced a large profile and placed
a Tracxn S3 asset URL in the brief. The corrected profile computes availability
metadata in Mongo without fetching rich arrays or contact values. Detail requests
select one allowlisted field using a fixed projection. An additional `overview`
field contains long descriptions and alternate names.

Company summaries, each of the 18 fields for three companies, filter suggestions,
selected columns, REST/MCP parity and contact access-control behavior are verified
separately. Live contact success is not claimed without an entitled linked account.
News examples retain their isolated-integration provenance. Location intelligence's
existing upstream failure remains documented in the [example audit](EXAMPLE_AUDIT.md).

Read [company fields](COMPANY_DATA_DEPTH.md), [filters and listings](FILTERS_AND_LISTINGS.md)
and [contact retrieval](CONTACTS.md) for the user-facing request flow.
