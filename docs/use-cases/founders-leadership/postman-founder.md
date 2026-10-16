# Postman Founder: Radar API example with live data

[Founders and leadership research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “postman founder” · 720/month India · 90/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [postman-founder.json](../../examples/use-cases/postman-founder.json).

**Question.** Who founded Postman, who are its key people, and what does its company profile say?

## At a glance

| Measure | Value |
| --- | ---: |
| Company | Postman (`postman.com`) |
| Founded | 2014 |
| Employees | 279 |
| Founders recorded | 3 |
| Key people recorded | 3 |

## Founders

`get_company_team` with `group=founders` (selected by recorded designation).

| Name | Designation |
| --- | --- |
| Abhinav Asthana | Co-Founder & CEO |
| Abhijit Kane | Co-Founder |
| Ankit Sobti | Founder And Chief Technical Officer |

## Key people

`get_company_team` with `group=key_people`.

| Name | Designation |
| --- | --- |
| Abhinav Asthana | Co-Founder & CEO |
| Abhijit Kane | Co-Founder |
| Ankit Sobti | Founder And Chief Technical Officer |

## Company snapshot

Provider of platform unifying API design, testing, documentation, monitoring, and discovery

`get_company` returns this summary plus `available_fields`; request a field (technology, traffic, apps, legal…) with `get_company_field`.

Coverage: Company key-person records, not a full employee roster or verified headcount. Founders are selected by recorded designation; no contacts are included.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-company-team --domain postman.com --group founders
radar get-company-team --domain postman.com --group key_people
radar get-company --domain postman.com
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/team" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "postman.com", "group": "founders"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/team", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "postman.com", "group": "key_people"}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`get_company_team`, `get_company`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field.

## Related use cases

- [Spinny Founder](spinny-founder.md)
- [Acko Founder](acko-founder.md)
- [Bigbasket CEO](bigbasket-ceo.md)
- [Country Delight Founder](country-delight-founder.md)
