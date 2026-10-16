# Indiamart CEO: Radar API example with live data

[Founders and leadership research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “indiamart ceo” · 590/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [indiamart-ceo.json](../../examples/use-cases/indiamart-ceo.json).

**Question.** Who founded Indiamart, who are its key people, and what does its company profile say?

## At a glance

| Measure | Value |
| --- | ---: |
| Company | IndiaMART (`indiamart.com`) |
| Founded | 1999 |
| Employees | 3592 |
| Founders recorded | 3 |
| Key people recorded | 3 |

## Founders

`get_company_team` with `group=founders` (selected by recorded designation).

| Name | Designation |
| --- | --- |
| Brijesh Agrawal | Co-Founder & Director |
| Dinesh Agarwal | Co-Founder & CEO |
| Brijesh Agarwal | Co-Founder & Director |

## Key people

`get_company_team` with `group=key_people`.

| Name | Designation |
| --- | --- |
| Brijesh Agrawal | Co-Founder & Director |
| Dinesh Agarwal | Co-Founder & CEO |
| Brijesh Agarwal | Co-Founder & Director |

## Company snapshot

B2B marketplace platform connecting buyers and suppliers offering diverse industrial products

`get_company` returns this summary plus `available_fields`; request a field (technology, traffic, apps, legal…) with `get_company_field`.

Coverage: Company key-person records, not a full employee roster or verified headcount. Founders are selected by recorded designation; no contacts are included.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-company-team --domain indiamart.com --group founders
radar get-company-team --domain indiamart.com --group key_people
radar get-company --domain indiamart.com
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/team" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "indiamart.com", "group": "founders"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/team", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "indiamart.com", "group": "key_people"}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`get_company_team`, `get_company`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field.

## Related use cases

- [Freshworks CEO](freshworks-ceo.md)
- [Klarna CEO](klarna-ceo.md)
- [Licious Founder](licious-founder.md)
- [Wow Momo Founder](wow-momo-founder.md)
