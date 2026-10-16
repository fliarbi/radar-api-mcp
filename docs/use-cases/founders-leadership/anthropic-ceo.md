# Anthropic CEO: Radar API example with live data

[Founders and leadership research](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “anthropic ceo” · 8,100/month India · 18,100/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [anthropic-ceo.json](../../examples/use-cases/anthropic-ceo.json).

**Question.** Who founded Anthropic, who are its key people, and what does its company profile say?

## At a glance

| Measure | Value |
| --- | ---: |
| Company | Anthropic (`anthropic.com`) |
| Founded | 2021 |
| Employees | 73 |
| Founders recorded | 6 |
| Key people recorded | 6 |

## Founders

`get_company_team` with `group=founders` (selected by recorded designation).

| Name | Designation |
| --- | --- |
| Benjamin Mann | Co-Founder |
| Jared Kaplan | Co-Founder & Chief Science Officer |
| Jack Clark | Co-Founder |
| Daniela Amodei | Co-Founder & President |
| Dario Amodei | Co-Founder & CEO |
| Sam Mccandlish | Co-Founder |

## Key people

`get_company_team` with `group=key_people`.

| Name | Designation |
| --- | --- |
| Benjamin Mann | Co-Founder |
| Jared Kaplan | Co-Founder & Chief Science Officer |
| Jack Clark | Co-Founder |
| Daniela Amodei | Co-Founder & President |
| Dario Amodei | Co-Founder & CEO |
| Sam Mccandlish | Co-Founder |

## Company snapshot

Provider of AI safety and research company

`get_company` returns this summary plus `available_fields`; request a field (technology, traffic, apps, legal…) with `get_company_field`.

Coverage: Company key-person records, not a full employee roster or verified headcount. Founders are selected by recorded designation; no contacts are included.

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar get-company-team --domain anthropic.com --group founders
radar get-company-team --domain anthropic.com --group key_people
radar get-company --domain anthropic.com
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/team" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"domain": "anthropic.com", "group": "founders"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/team", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"domain": "anthropic.com", "group": "key_people"}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`get_company_team`, `get_company`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Availability describes stored observations, not current accuracy or contact entitlement. Request one field at /v1/companies/field.

## Related use cases

- [Zomato Founder](zomato-founder.md)
- [Openai CEO](openai-ceo.md)
