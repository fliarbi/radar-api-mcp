# Quantum Computing Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “quantum computing companies in india” · 320/month India · 10/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [quantum-computing-companies-in-india.json](../../examples/use-cases/quantum-computing-companies-in-india.json).

**Question.** Which Quantum Computing companies are based in India, how large and how old are they, and who competes in the Quantum Computing market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Quantum Computing” |
| Companies returned (India, first page) | 20 |
| Competitive set for “quantum computing” (worldwide) | 40 |

## Quantum Computing companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| QNu Labs (qnulabs.com) | Bengaluru | 2016 | 51-200 | Provider of quantum cryptography solutions, key distribution, random number generation |
| QpiAI (qpiai.tech) | Bengaluru | 2019 | 11-50 | Developer of integrated quantum computing and artificial intelligence solutions |
| Qbit Labs (qbitlabs.co.in) | Gurugram | 2020 | 51-200 | Provider of quantum computing research solutions |
| TAQBit (taqbit.com) | Bengaluru | 2018 | 11-50 | Provider of data security for enterprises using quantum technology |
| BosonQ Psi (bosonqpsi.com) | Bhilai | 2020 | 11-50 | Developer of quantum simulation software |
| Arishti CyberTech (arishti.in) | Pune | 2020 | — | Provider of cloud encryption based secure messaging platform |
| SecureMachines (securemachines.in) | Bengaluru | 2019 | — | Developer of quantum-safe hardware, security modules, and data integrity solutions |
| GDQLabs (gdqlabs.com) | Pune | 2022 | — | Developer of quantum magnetometers for navigation, healthcare, and resource exploration |
| QuPrayog (quprayog.com) | Pune | 2024 | — | Provider of precision scientific equipment for research and industry |
| amPICQ (ampicq.com) | Hyderabad | 2022 | — | Developer of photonic integrated circuit chips for quantum communication applications |
| AugSenseLab (augsenselab.com) | Thiruvananthapuram | 2019 | — | Developer of quantum sensing technology for software-defined radar receiver applications |
| Pramatra Space (pramatra.space) | Bengaluru | 2023 | — | Developer of quantum key distribution satellites |
| QpiCloud (qpicloud.tech) | Bengaluru | 2020 | — | Cloud-based computing and collaborative platform |
| QpiSemi (qpisemi.tech) | Bengaluru | 2021 | — | Manufacturer of quantum and CMOS-based chips |
| Quanastra (quanastra.com) | Delhi | 2024 | — | Manufacturer of superconducting nanowire single photon detectors and cryogenic systems |
| Quanfluence (quanfluence.com) | Bengaluru | 2021 | — | Provider of quantum computing system and services |
| SuperQuantum (superquantum.tech) | Bengaluru | 2020 | — | Provider of superconducting nanowire single-photon detectors and rotating machines |
| Quan2D Technologies (quan2d.com) | Bengaluru | 2021 | — | Manufacturer of nanomaterials and developer of quantum technology-based sensing solutions |
| Bloq Quantum (bloq.in) | Kollam | 2024 | — | Provider of quantum algorithm development solutions for accelerating various use cases |
| PrenishQ (prenishq.com) | Delhi | 2022 | — | Developer of custom lasers, optics, electronics, and automation for quantum computing |

## Competitive set: “quantum computing” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage. Countries: United States 17, United Kingdom 5, Canada 3, China 3, Switzerland 3, Finland 2.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |
| Public | Xanadu | Toronto | Manufacturer of cloud and AI-based application-specific ICs for quantum computing applications |
| Public | Infleqtion | Louisville | Provider of neutral-atom quantum technology, products and solutions |
| Public | IonQ | College Park | Provider of cloud and trapped ion technology-based universal quantum computers |
| Seed | Bluefors | Helsinki | Manufacturer of cryogenic measurement systems and cryocoolers |
| Seed | Quantum Fabrix | Kidlington | Manufacturer of modular quantum hardware components for quantum systems integrators |
| Seed | Qubit Pharmaceuticals | Paris | Developer of drugs for the treatment of cancer and inflammatory diseases |
| Series A | QNu Labs | Bengaluru | Provider of quantum cryptography solutions, key distribution, random number generation |
| Series A | Quantum Brilliance | Sydney | Developer of quantum computers using superconducting qubit technology |
| Series A | Terra Quantum | St. Gallen | Provider of quantum as a service platform |
| Series B | IQM | Espoo | Developer of superconducting quantum computers |
| Series B | CIQTEK | Hefei | Developer of quantum analysers, generators and sensors |
| Series B | QuEra | Boston | Manufacturer of universal quantum computers based on Rydberg atoms |
| Series C | Quantum Machines | Tel Aviv | Provider of cloud-powered qubit controllers for quantum computers |
| Series C | Riverlane | Cambridge | Provider of software for quantum computers |
| Series C | Cambridge Quantum | London | Provider of AI-based software for quantum computing |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Quantum Computing" --filters.locations India --limit 20
radar find-competitors --market "quantum computing" --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Quantum Computing"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "quantum computing", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Music Companies in India](music-companies-in-india.md)
- [Data Analytics Companies in India](data-analytics-companies-in-india.md)
- [Hotel Companies in India](hotel-companies-in-india.md)
- [Sports Companies in India](sports-companies-in-india.md)
