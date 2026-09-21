# Investor data depth: portfolio companies, co-investors, financing outcomes and news

The investor API reads the reviewed, database-derived Atlas release after checking
Radar's live publication gate. It checks the stored data fingerprint and page
identity. A publication heading alone is not treated as a complete investor profile.
The source snapshot and source cutoff stay visible on every response.

## Start with measured summary metrics

POST `/v1/investors/page`:

```json
{"slug":"anupam-mittal"}
```

The verified response contains 270 total companies / 303 equity participations;
268 companies / 301 participations have dates. The two undated companies remain
available through `undated_portfolio`. The summary reports entry-round size,
early-stage entry share, lead participation, activity and median syndicate size.
It lists detail fields and counts without embedding the entire portfolio.

The source coverage ends **2026-05-22** and was computed on **2026-09-14**.
Mittal's last recorded investment is **2026-03-28**. These dates describe the
source records, not a promise that the investor is accepting new opportunities.

## Select one field with a JSON POST

POST `/v1/investors/field`:

```json
{"slug":"anupam-mittal","field":"portfolio","limit":20,"offset":0,"sector":"FinTech","stage":"Seed"}
```

Each portfolio row keeps name, domain, company URL, description, city, country,
sectors, entry stage/date, last investment, disclosed whole-round USD amount,
participation count, lead flag, other backer count, repeat date, next financing
date/days and eligible-cohort outcome flags. Follow `pagination.next_offset`
until null. `source_total` describes stored rows; `matched_total` describes rows
after your filters. No nested business arrays are shortened by the docs renderer.

Portfolio filters: q, sector, stage, city, country. Directory `investors` filters:
q, stage, city, country, kind. Both support source/name/latest ordering;
directory investors additionally support companies ordering. Unsupported filter
and field combinations return 422 instead of being silently ignored.
Limits are 1–100 rows. Missing source values remain null, with zero and false
preserved. Arrays inside analytical objects retain their complete structure.

## Fields and captured output

| Page | Field | Actual JSON output |
|---|---|---|
| anupam-mittal | `activity` | [HTTP 200](examples/investors/anupam-mittal-activity.json) |
| anupam-mittal | `analysis` | [HTTP 200](examples/investors/anupam-mittal-analysis.json) |
| anupam-mittal | `co_investors` | [HTTP 200](examples/investors/anupam-mittal-co_investors.json) |
| anupam-mittal | `follow_on` | [HTTP 200](examples/investors/anupam-mittal-follow_on.json) |
| anupam-mittal | `news` | [HTTP 200](examples/investors/anupam-mittal-news.json) |
| anupam-mittal | `portfolio` | [HTTP 200](examples/investors/anupam-mittal-portfolio.json) |
| anupam-mittal | `related` | [HTTP 200](examples/investors/anupam-mittal-related.json) |
| anupam-mittal | `sectors` | [HTTP 200](examples/investors/anupam-mittal-sectors.json) |
| anupam-mittal | `stages` | [HTTP 200](examples/investors/anupam-mittal-stages.json) |
| anupam-mittal | `summary` | [HTTP 200](examples/investors/anupam-mittal-summary.json) |
| anupam-mittal | `undated_portfolio` | [HTTP 200](examples/investors/anupam-mittal-undated_portfolio.json) |
| fintech-investors-in-bengaluru | `activity` | [HTTP 200](examples/investors/fintech-investors-in-bengaluru-activity.json) |
| fintech-investors-in-bengaluru | `geography` | [HTTP 200](examples/investors/fintech-investors-in-bengaluru-geography.json) |
| fintech-investors-in-bengaluru | `investors` | [HTTP 200](examples/investors/fintech-investors-in-bengaluru-investors.json) |
| fintech-investors-in-bengaluru | `recent_rounds` | [HTTP 200](examples/investors/fintech-investors-in-bengaluru-recent_rounds.json) |
| fintech-investors-in-bengaluru | `related` | [HTTP 200](examples/investors/fintech-investors-in-bengaluru-related.json) |
| fintech-investors-in-bengaluru | `research` | [HTTP 200](examples/investors/fintech-investors-in-bengaluru-research.json) |
| fintech-investors-in-bengaluru | `selection` | [HTTP 200](examples/investors/fintech-investors-in-bengaluru-selection.json) |
| fintech-investors-in-bengaluru | `stages` | [HTTP 200](examples/investors/fintech-investors-in-bengaluru-stages.json) |
| fintech-investors-in-bengaluru | `summary` | [HTTP 200](examples/investors/fintech-investors-in-bengaluru-summary.json) |
| fintech-investors-in-bengaluru | `themes` | [HTTP 200](examples/investors/fintech-investors-in-bengaluru-themes.json) |

The `follow_on` field separates another financing round from repeat backing by
this investor. For 215 eligible companies, 125 received another equity round
within 24 months and 25 had repeat backing. The median time to a next round,
10.12 months, is conditional on the 125 observed successes. It is not a forecast.
Entry-round size has 247 disclosed observations and median USD 222,410; these
are total round amounts, not personal cheques. Sector tags overlap.

The `news` field includes six dated stories with publishers and source URLs,
observed facts, separately labeled interpretation, and flags identifying stories
after the deal cutoff. `analysis` contains the measured research readout.
`co_investors` supplies shared-company/shared-round counts and last observed dates.

The FinTech/Bengaluru directory's `investors` field exposes 1,199 selected
investors with stage distributions, example companies, entry-round statistics,
lead and repeat relationships, geography and theme associations. It is a selected
shortlist, not all 5,449 measured dated investors. Live pagination independently
traversed all 268 profile companies and all 1,199 selected directory investors.

All requests use the `investors` key scope and the regular account rate, concurrency
and spending limits. Successful operations cost one credit in account mode;
source failures do not. Contact values and gated LinkedIn links are excluded.
No website sign-in gate or source publication flag is changed.

## Operator connection and failure behavior

Set `RADAR_INVESTOR_DATA_DIR` to a reviewed immutable Atlas release containing
`meta/` and `data/`. It is a private operator path, not a client input. Every read
checks the live publication gate, matching slug/kind/family and recorded SHA-256.
Missing, held, mismatched and corrupt releases fail explicitly. When the optional
store is unconfigured, the summary is labeled metadata-only/partial and field
requests return 503. The captures prove the local authenticated gateway, not a
public deployment. A newer source release requires an operator-reviewed update.

See [investor workflow](guides/investor-data-api.md), [field reference](reference/get_investor_field.md)
and [response depth audit](DATA_DEPTH_AUDIT.md).
