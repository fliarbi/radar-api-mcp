# Upgrad Founder: Radar API example with live data

[Founders and leadership research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “upgrad founder” · 1,000/month India · 30/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [upgrad-founder.json](../../examples/use-cases/upgrad-founder.json).

**Question.** Who founded Upgrad, who are its key people, and what does its company profile say?

## At a glance

| Measure | Value |
| --- | ---: |
| Company | UpGrad (`upgrad.com`) |
| Founded | 2015 |
| Employees | 6181 |
| Founders recorded | 4 |
| Key people recorded | 6 |

## Founders

`get_company_team` with `group=founders` (selected by recorded designation).

| Name | Designation |
| --- | --- |
| Ronnie Screwvala | Chairperson & Co-Founder |
| Rohinton Screwvala | Co-Founder & Chairperson |
| Phalgun Kompalli | Co-Founder |
| Mayank Kumar | Co-Founder |

## Key people

`get_company_team` with `group=key_people`.

| Name | Designation |
| --- | --- |
| Ronnie Screwvala | Chairperson & Co-Founder |
| Rohinton Screwvala | Co-Founder & Chairperson |
| Phalgun Kompalli | Co-Founder |
| Mayank Kumar | Co-Founder |
| Srikanth Iyengar | Chief Executive Officer |
| Myleeta Williams | CEO |

## Company snapshot

Higher education and upskilling platform

`get_company` returns this summary plus `available_fields`; request a field (technology, traffic, apps, legal…) with `get_company_field`.

Coverage: Company key-person records, not a full employee roster or verified headcount. Founders are selected by recorded designation; no contacts are included.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-company-team --domain upgrad.com --group founders
radar get-company-team --domain upgrad.com --group key_people
radar get-company --domain upgrad.com
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/team" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "upgrad.com", "group": "founders"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/team", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "upgrad.com", "group": "key_people"}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`get_company_team`, `get_company`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field.

## Related use cases

- [Cars24 CEO](cars24-ceo.md)
- [Delhivery Founder](delhivery-founder.md)
- [Porter Founder](porter-founder.md)
- [Vedantu Founder](vedantu-founder.md)
