# Radar API + MCP — B2B company data, financial data and news

Retrieve B2B company data, company intelligence, financial statements, financial
news, startup funding data, funding news, investors and hiring signals from
**one interface with 30 data capabilities**.
The same validated operations are available over REST and MCP.

**Private preview — owner approval is required before public release.** No public
API host, active checkout or production API-key integration is claimed. Installing
this package does not deploy a service or change Radar.

Optional account mode adds a developer console for API-key issuance and revocation,
account-wide usage limits, prepaid credit metering, company following and payment
verification. It follows Radar's existing subscription catalog. The per-use rate
is unset and checkout stays disabled until configured. Start with
[API keys](docs/guides/api-keys-authentication.md),
[pricing and pay-per-use](docs/guides/pricing-pay-per-use.md), or the
[complete documentation hub](docs/README.md).

Financial responses distinguish filing-derived figures from news-reported earnings,
retain fiscal periods and currencies, and disclose when the linked Radar account
exposes only part of the archive. Company briefs combine multiple sections and
mark individual failures instead of treating unavailable data as zero.

## Quick start

The server runs on Linux/macOS with POSIX file permissions; HTTP clients can run
on other platforms.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
```

Set `RADAR_UPSTREAM_URL` to the Radar service supplied by your operator. Optionally
set `RADAR_NEWS_URL` and `RADAR_BUSINESS_NEWS_URL` to the separately operated News
API services. `.env.example` lists the settings; the application reads environment
variables, not `.env` files automatically.

Create a preview key locally:

```bash
radar-create-key --name local-preview
export RADAR_API_KEY="$(cat secrets/client-key.txt)"
radar-api --port 8810
```

The server binds to `127.0.0.1`. The key store and client key are owner-only files
under the ignored `secrets/` directory. Each preview key can link to its own Radar
session and News API key; see [operator setup](docs/OPERATIONS.md). A key without a
linked Radar session receives Radar's anonymous coverage. This does not unlock
paid features. News requires a linked News API key and a configured News service.

```bash
curl -sS http://127.0.0.1:8810/v1/companies/financials \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com","statement":"income","period_type":"annual"}'

curl -sS http://127.0.0.1:8810/v1/companies/brief \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"domain":"microsoft.com","include_news":true}'
```

## Connect an MCP client

For a local stdio client, use this server configuration with absolute paths and
your issued preview key in the client's secret/environment configuration:

```json
{
  "mcpServers": {
    "radar": {
      "command": "/absolute/path/radar-api-mcp/.venv/bin/radar-mcp",
      "env": {
        "RADAR_KEYS_FILE": "/absolute/path/radar-api-mcp/secrets/keys.json",
        "RADAR_UPSTREAM_URL": "http://127.0.0.1:5100",
        "RADAR_API_KEY": "YOUR_ISSUED_PREVIEW_KEY"
      }
    }
  }
}
```

The HTTP server also serves **Streamable HTTP MCP at `/mcp`**, protected by the
same `Authorization: Bearer ...` or `X-API-Key` header as REST. Use a client that
supports custom authentication headers. OAuth discovery and public connector
onboarding are not part of this private preview.

Try: “Find enterprise AI companies in India, compare two companies' financials,
and show the news and funding behind their recent activity.”

## What you can retrieve

| Area | Capabilities |
|---|---|
| Companies | Filtered and natural-language search, profiles, competitors, intelligence, comparison |
| Financials | Income, balance-sheet and cash-flow metrics, annual/quarterly filters, source labels |
| Activity | Company events, funding rounds, legal details, reputation, hiring, digital presence |
| Investors and markets | Investor search/directory/pages, market pulse, location intelligence, industry discovery |
| People and jobs | Professional search, job search/detail, hiring companies, salary benchmarks |
| News | General/business headlines, full articles, volume, sentiment, overview, business events, funding coverage |
| Combined research | Company brief with section-level errors, access limits and dates |

The 30 MCP tools are retrieval operations. Optional account-management HTTP routes
are separate; contact reveals, CRM sending, applications and resume handling are
not included. Published investor pages
may supply metadata only when their detailed roster has a separate access gate.

Read the [user guide](docs/USER_GUIDE.md), [capability map](docs/CAPABILITIES.md),
[operator guide](docs/OPERATIONS.md) and [verification record](docs/VERIFICATION.md).
Authenticated discovery is at `/v1/capabilities`; OpenAPI is at `/v1/openapi.json`.

## Guides by data and use case

| Build with Radar | Documentation |
|---|---|
| B2B business data and company lookup | [B2B data API](docs/guides/b2b-data-api.md), [company data API](docs/guides/company-data-api.md) |
| Company discovery and CRM research | [Company search](docs/guides/company-search-api.md), [company enrichment](docs/guides/company-enrichment-api.md) |
| Company financial research | [Financial data](docs/guides/financial-data-api.md), [financial statements](docs/guides/company-financial-statements-api.md) |
| Earnings and investment announcements | [Financial news](docs/guides/financial-news-api.md), [funding news](docs/guides/funding-news-api.md) |
| Startup and venture capital research | [Funding rounds](docs/guides/startup-funding-data-api.md), [investor data](docs/guides/investor-data-api.md) |
| Business activity and peer analysis | [Company monitoring](docs/guides/company-monitoring-api.md), [competitor intelligence](docs/guides/competitor-intelligence-api.md), [hiring signals](docs/guides/hiring-signals-jobs-api.md) |
| AI-agent research tools | [Company intelligence MCP server](docs/guides/company-intelligence-mcp-server.md) |

These guides include request examples, interpretation details, source coverage and
common integration questions. [Search research](docs/SEARCH_RESEARCH.md) records
the terminology research and the distinction between private documentation and
future public discoverability.

## Development

```bash
pytest
ruff check radar_api tests scripts
python -m build
```

Tests use synthetic data and include real MCP HTTP and stdio protocol sessions.
Live probes are separate, opt-in and never run in CI. The implementation uses the
[official MCP Python SDK v1](https://py.sdk.modelcontextprotocol.io/v1/), pinned
below v2 to match the tested FastMCP API.

Copyright Fliar Business Intelligence. Proprietary; all rights reserved.
