# Wow Momo Founder: Radar API example with live data

[Founders and leadership research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “wow momo founder” · 880/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [wow-momo-founder.json](../../examples/use-cases/wow-momo-founder.json).

**Question.** Who founded Wow Momo, who are its key people, and what does its company profile say?

## At a glance

| Measure | Value |
| --- | ---: |
| Company | Wow Momo (`wowmomo.com`) |
| Founded | 2008 |
| Employees | 5836 |
| Founders recorded | 4 |
| Key people recorded | 5 |

## Founders

`get_company_team` with `group=founders` (selected by recorded designation).

| Name | Designation |
| --- | --- |
| Shah Rahman | Co-Founder & Chief Finance & Operating Officer |
| Binod Homagai | Co-Founder & COO |
| Murali Krishnan | Co-Founder & CMO |
| Sagar Daryani | Co-Founder & CEO |

## Key people

`get_company_team` with `group=key_people`.

| Name | Designation |
| --- | --- |
| Shah Rahman | Co-Founder & Chief Finance & Operating Officer |
| Binod Homagai | Co-Founder & COO |
| Murali Krishnan | Co-Founder & CMO |
| Sagar Daryani | Co-Founder & CEO |
| Mithun Appaiah | Chief Executive Officer |

## Company snapshot

Chains providing diverse food options including dumplings and various fusion dishes

`get_company` returns this summary plus `available_fields`; request a field (technology, traffic, apps, legal…) with `get_company_field`.

Coverage: Company key-person records, not a full employee roster or verified headcount. Founders are selected by recorded designation; no contacts are included.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-company-team --domain wowmomo.com --group founders
radar get-company-team --domain wowmomo.com --group key_people
radar get-company --domain wowmomo.com
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/team" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "wowmomo.com", "group": "founders"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/team", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "wowmomo.com", "group": "key_people"}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`get_company_team`, `get_company`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field.

## Related use cases

- [Indiamart CEO](indiamart-ceo.md)
- [Licious Founder](licious-founder.md)
- [Policybazaar CEO](policybazaar-ceo.md)
- [Revolut Founder](revolut-founder.md)
