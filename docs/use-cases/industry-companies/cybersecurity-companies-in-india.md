# Cybersecurity Companies in India: Radar API example with live data

[Companies by industry](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

> **Search demand:** “cybersecurity companies in india” · 1,600/month India · 40/month US  
> **Data:** Captured 16 Oct 2026 from the live API · 86% of indexed articles (2 of 14 shards offline): counts are lower bounds. Saved API responses: [cybersecurity-companies-in-india.json](../../examples/use-cases/cybersecurity-companies-in-india.json).

**Question.** Which Cybersecurity companies are based in India, how large and how old are they, and who competes in the Cybersecurity market worldwide?

## At a glance

| Measure | Value |
| --- | ---: |
| Radar industry | “Cyber Security” |
| Companies returned (India, first page) | 18 |
| Competitive set for “cybersecurity” (worldwide) | 52 |

## Cybersecurity companies in India

`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).

| Company | HQ | Founded | Employees | What they do |
| --- | --- | --- | --- | --- |
| QNu Labs (qnulabs.com) | Bengaluru | 2016 | 51-200 | Provider of quantum cryptography solutions, key distribution, random number generation |
| TAQBit (taqbit.com) | Bengaluru | 2018 | 11-50 | Provider of data security for enterprises using quantum technology |
| SecureMachines (securemachines.in) | Bengaluru | 2019 | — | Developer of quantum-safe hardware, security modules, and data integrity solutions |
| QDIT Labs (qditlabs.com) | Bengaluru | 2018 | — | Developer of enterprise-grade quantum encryption cybersecurity solutions |
| Qulabs (qulabs.ai) | Hyderabad | 2018 | — | Provider of AI-powered quantum computing solution for secured communication |
| Scytale Alpha (scytaleindia.com) | Delhi | 2019 | — | Provider of security and privacy solutions |
| KrytoTech (krytotech.com) | Kolkata | 2010 | — | Quantum ready encryption technology solution |
| Cipherion (cipherion.in) | Belgaum | 2025 | — | Provider of encryption software for securing sensitive data field information |
| Merkletreelabs (merkletreelabs.com) | Hyderabad | 2018 | — | Developer of post-quantum cryptographic solutions and integration support for secure systems |
| Survlens (survlens.com) | Hyderabad | 2023 | — | Provider of AI-powered surveillance solutions |
| E2E Encrypter (e2eencrypter.com) | Mumbai | 2021 | — | Cloud based cryptographic encryption solutions provider |
| Ozone Chain Technologies (ozonechain.io) | Chennai | 2023 | — | Quantum-resistant blockchain network |
| QuantumShift (quantumshift.in) | Delhi | 2023 | — | Provider of quantum-enabled communication, AI/ML, sensing, and semiconductor design services |
| Utkalika Research and Development (utkalikard.com) | Bengaluru | 2024 | — | Developer of quantum communication, cryptography, sensing, radar, and positioning systems |
| Shieldcuresolutions (shieldcuresolutions.com) | Khordha | 2022 | — | Developer of hardware lock solution using quantum cryptography for edge device security |
| Unitech Cyber Solutions (unitechcybersolutions.com) | Gurugram | 2020 | — | Chain of education centers providing cyber security training programs |
| QRL (qrl.co.in) | — | 2017 | — | Blockchain based quantum resistance data encryption solutions |
| HaQien (haqien.com) | — | 2019 | — |  |

## Competitive set: “cybersecurity” worldwide

`find_competitors` (`per_stage=3`): companies grouped by stage. Countries: United States 28, China 14, France 2, India 2, Brazil 1, Canada 1.

| Stage | Company | Location | Description |
| --- | --- | --- | --- |
| Public | Q Tech Microelectronics India | Suzhou | Q Tech is a manufacturer of camera and fingerprint recognition modules for mobile devices. |
| Public | Cisco | San Jose | Provider of AI infrastructure, secure networking, and software solutions |
| Public | Asseco | Rzeszow | Provider of an omnichannel banking solutions |
| Seed | Xiaobanhui | Beijing | Platform offering audio and video conferencing tools |
| Seed | Proton | Geneva | Provider of encrypted email, calendar, VPN, password management, and cloud services |
| Seed | Shenzhen Huafu Information Technology | Shenzhen | Provider of facial recognition solutions for multiple applications |
| Series A | ABT Networks | Beijing | Security platform operating system for network security |
| Series A | SSI | Palo Alto | Platform offering security solutions for AI models |
| Series A | Stitch | San Francisco | Care coordination platform for healthcare teams, enabling seamless communication and collaboration |
| Series B | Guangzhou Trustmo Information System | Guangzhou | Network violation behavior monitoring and analysis system |
| Series B | CertiK | New York City | Provider of comprehensive blockchain security solutions, including smart contract audits, due… |
| Series B | Incode | San Francisco | Developer of identity verification software using biometric and document analysis |
| Series C | 1Password | Toronto | Cloud based platform for remote access software |
| Series C | Nord Security | Vilnius | Cloud based cybersecurity suite solutions provider |
| Series C | Malwarebytes | Santa Clara | Provider of cybersecurity software including antivirus, VPN, and scam protection |

## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
radar search-companies --filters.industries "Cyber Security" --filters.locations India --limit 20
radar find-competitors --market cybersecurity --per-stage 3
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL/v1/companies/search" -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' -d '{"filters": {"industries": ["Cyber Security"], "locations": ["India"]}, "limit": 20}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/competitors", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"market": "cybersecurity", "per_stage": 3}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools (`find_competitors`, `search_companies`) at `$RADAR_API_URL/mcp`.

## Read the result carefully

- Captured while part of the news index was offline (86% of indexed articles (2 of 14 shards offline)): news counts are lower bounds.
- Filters and result counts remain subject to the linked Radar account's limits.

## Related use cases

- [Electronics Companies in India](electronics-companies-in-india.md)
- [Advertising Companies in India](advertising-companies-in-india.md)
- [Robotics Companies in India](robotics-companies-in-india.md)
- [Biotech Companies in India](biotech-companies-in-india.md)
