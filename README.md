# Radar API + MCP: company data, financial data and financial news API

Company data API, financial data API and financial news API in one: company search and
profiles, financial statements and reported revenue, funding rounds, investors, founders
and teams, apps, jobs, and real-time and historical financial and business news.
**53 data operations** over REST and MCP, for your application, AI agents, Claude Code and Codex.

**Live.** Base URL `https://radar-api.fliarbi.com` · MCP `https://radar-api.fliarbi.com/mcp` ·
[create a key](https://fliarbi.com/radar-api/developer) in the Fliar dashboard (**API keys**).
One key also works on the [Prism News API](https://github.com/fliarbi/prism-news-api) and the
[Prism Business News API](https://github.com/fliarbi/prism-business-news-api). Subscribe or pay as you go.

<!-- use-cases:start -->
## 200 worked examples with live data

Each page answers one researched search query (“stock market news”, “Zomato revenue”, “fintech
companies in India”, “Razorpay founder”…) with saved live API responses and the exact CLI, curl,
Python and MCP calls. [Browse all 200](docs/use-cases/README.md) or start with a segment:

| Segment | Pages | Start with |
| --- | ---: | --- |
| **[Financial news research](docs/use-cases/financial-news/README.md)** | 50 | [Stock Market](docs/use-cases/financial-news/stock-market-news.md) · [Crypto](docs/use-cases/financial-news/crypto-news.md) · [GST](docs/use-cases/financial-news/gst-news.md) · [Gold Price](docs/use-cases/financial-news/gold-price-news.md) |
| **[Company financials research](docs/use-cases/company-financials/README.md)** | 50 | [Openai](docs/use-cases/company-financials/openai-revenue.md) · [Anthropic](docs/use-cases/company-financials/anthropic-revenue.md) · [Zoho](docs/use-cases/company-financials/zoho-revenue.md) · [Zomato](docs/use-cases/company-financials/zomato-revenue.md) |
| **[Companies by industry](docs/use-cases/industry-companies/README.md)** | 50 | [Automotive](docs/use-cases/industry-companies/automotive-companies-in-india.md) · [AI](docs/use-cases/industry-companies/ai-companies-in-india.md) · [Digital Marketing](docs/use-cases/industry-companies/digital-marketing-companies-in-india.md) · [Pharmaceutical](docs/use-cases/industry-companies/pharmaceutical-companies-in-india.md) |
| **[Founders and leadership research](docs/use-cases/founders-leadership/README.md)** | 50 | [Anthropic](docs/use-cases/founders-leadership/anthropic-ceo.md) · [Zomato](docs/use-cases/founders-leadership/zomato-founder.md) · [Openai](docs/use-cases/founders-leadership/openai-ceo.md) · [Oyo](docs/use-cases/founders-leadership/oyo-founder.md) |

Topics come from [keyword research](docs/research/KEYWORD_RESEARCH.md) (India and US monthly searches).
Also see the [60 tested business scenarios](docs/scenarios/README.md).
<!-- use-cases:end -->

## See the API in a research UI

[Seven animated Claude Code / Codex workflow concepts](docs/ANIMATED_USE_CASES.md)
show competitor analysis, financial comparisons, founder LinkedIn profiles, GenAI
startup discovery, San Francisco funding in April 2026, dating-app rankings with
company legal details, and founder-email exports to Excel. Each GIF labels saved
Radar data or illustrative rows; these are client-built UI concepts, not recordings
of official client interfaces or claims of live service availability.

Each animation opens with a large typed prompt that slides away, then shows a
full-screen chart and detailed results. Click any animation to open it at full size.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Competitor analysis</h3>
      <a href="docs/demos/media/competitor-analysis.gif"><img src="docs/demos/media/competitor-analysis.gif" width="420" alt="Animated competitor research with five saved Radar peer cards"></a>
      <p>Compare market peers, locations and funding stages. Saved Radar data.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Financial comparison</h3>
      <a href="docs/demos/media/financial-comparison.gif"><img src="docs/demos/media/financial-comparison.gif" width="420" alt="Animated FY2025 revenue and profit comparison with source labels"></a>
      <p>Compare revenue, net income and EBITDA with source labels. Saved Radar data.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Founders &amp; LinkedIn</h3>
      <a href="docs/demos/media/founder-linkedin.gif"><img src="docs/demos/media/founder-linkedin.gif" width="420" alt="Animated founder research showing LinkedIn, education and skills"></a>
      <p>Explore founder profiles, LinkedIn links, education and skills. Saved Radar data.</p>
    </td>
    <td width="50%" valign="top">
      <h3>GenAI startup discovery</h3>
      <a href="docs/demos/media/genai-startups.gif"><img src="docs/demos/media/genai-startups.gif" width="420" alt="Animated GenAI startup search and company shortlist using fictional rows"></a>
      <p>Turn a research prompt into a filtered startup shortlist. Illustrative data.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>San Francisco funding · April 2026</h3>
      <a href="docs/demos/media/sf-funding-april-2026.gif"><img src="docs/demos/media/sf-funding-april-2026.gif" width="420" alt="Animated April 2026 funding-news research with a San Francisco geography check"></a>
      <p>Combine dated funding news with company geography. Illustrative data.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Top 10 dating apps &amp; legal details</h3>
      <a href="docs/demos/media/dating-apps-legal.gif"><img src="docs/demos/media/dating-apps-legal.gif" width="420" alt="Animated top ten dating apps by stored Google Play installs and company legal details"></a>
      <p>Rank apps by stored installs and inspect company legal records. Illustrative data.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Founder emails to Excel</h3>
      <a href="docs/demos/media/founder-email-excel.gif"><img src="docs/demos/media/founder-email-excel.gif" width="420" alt="Animated founder contact workflow and illustrated Excel export with synthetic addresses"></a>
      <p>Prepare a spreadsheet with contact provenance and missing rows. Synthetic contacts; illustrated export.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Explore every workflow</h3>
      <p><a href="docs/ANIMATED_USE_CASES.md">Read the prompts, requests and data notes</a>.</p>
      <p><a href="docs/demos/README.md">Run the local interactive gallery</a> for workflow selection, pause and replay.</p>
    </td>
  </tr>
</table>

[Browse all seven GIFs](docs/ANIMATED_USE_CASES.md) ·
[Open the local interactive gallery](docs/demos/index.html)

## Install in one line

Requires Bash, curl and Python 3.8+. Installs the `radar` command to `~/.local/bin` and sets
`RADAR_API_URL` for every new shell, so curl, Python, MCP clients and the CLI work without
configuring a URL. It never uses sudo or starts services.

```bash
curl -fsSL https://raw.githubusercontent.com/fliarbi/radar-api-mcp/main/scripts/install.sh | bash
```

See [Getting started](docs/GETTING_STARTED.md) for options, every command and troubleshooting.
To run your own gateway server instead, see [run your own gateway](#run-your-own-gateway).

## Get started in five steps

| Step | Do this | You get |
|---:|---|---|
| 1 | [Fliar dashboard](https://fliarbi.com/radar/dashboard?tab=radarapi) → **API keys** → **Create or manage API keys** → create a key | One `rdr_` key for Radar and the Prism News APIs |
| 2 | Run the one-line installer above | The `radar` command; `RADAR_API_URL` set |
| 3 | `radar login` | Your key saved owner-only in `~/.config/radar/config.json` |
| 4 | `radar features` | All 53 operations and their paths |
| 5 | Open a [use case](docs/use-cases/README.md), copy its commands and change the company or topic | Your own version of a worked example |

| Task | Command | Endpoint |
|---|---|---|
| Company financials | `radar get-financials --domain zomato.com --period-type annual` | `POST /v1/companies/financials` |
| Companies in an industry | `radar search-companies --filters.industries FinTech --filters.locations India --limit 20 --table` | `POST /v1/companies/search` |
| Company profile | `radar get-company --domain swiggy.com` | `POST /v1/companies/profile` |
| Founders and key people | `radar get-company-team --domain razorpay.com --group founders` | `POST /v1/companies/team` |
| Funding history | `radar get-company-funding --domain razorpay.com` | `POST /v1/companies/funding` |
| Competitors | `radar find-competitors --market "food delivery"` | `POST /v1/companies/competitors` |
| Financial news | `radar search-business-news --q "stock market" --priority-min 7 --limit 10 --table` | `POST /v1/news/business` |
| News volume and tone | `radar news-overview --q inflation --date-from 2026-01-01 --date-to 2026-04-30` | `POST /v1/news/overview` |
| Funding news | `radar search-funding-news --sector fintech --limit 10 --table` | `POST /v1/news/funding` |
| Company brief | `radar company-brief --domain razorpay.com --include-news true` | `POST /v1/companies/brief` |

## API at a glance

| Item | Value |
|---|---|
| Base URL | `https://radar-api.fliarbi.com` (also `https://fliarbi.com/radar-api`) |
| Authentication | `Authorization: Bearer rdr_…` or `X-API-Key: rdr_…` |
| Requests | `POST /v1/<operation>` with a JSON body; see `radar features` or [all 53 references](docs/reference/README.md) |
| MCP | Streamable HTTP at `/mcp` with the same header; `radar mcp-config` prints a client configuration |
| Discovery | `/v1/capabilities` (authenticated), OpenAPI at `/v1/openapi.json`, interactive docs at `/docs` |
| Responses | `{ok, feature, data, window, meta}`; errors carry `error.kind` and `error.message` |
| Metering | One credit per successful operation (briefs up to 7, comparisons 3 per company); failed sections are refunded |
| Limits | Per-minute rate, requests at once and daily prepaid credits by [usage level](#plans-and-prices) |

## Plans and prices

| Plan | Price / month | API credits included | Pay as you go | Dashboard searches | Company following |
|---|---|---:|---|---:|---:|
| Free | ₹0 | — | Yes | 50 | — |
| Pro | ₹1,600 (US$19) | — | Yes | 1,000 | 100 |
| Business | ₹5,000 (US$60) | 5,000 | Yes, after included credits | 5,000 | 1,000 |
| **Pay as you go** | **₹0.84 / US$0.01 per credit** | — | Minimum top-up 500 credits (US$5) | — | — |

Prices exclude GST. Buy credits and set a monthly spending limit on the
[API key page](https://fliarbi.com/radar-api/developer); credits appear as soon as checkout
succeeds. The same wallet pays for the Prism News APIs after their own plan allowance.

**Usage levels.** Limits rise automatically with lifetime credits used (Radar and Prism News
together) and never go down:

| Level | Credits used (lifetime) | Requests / min | Requests at once | Prepaid credits / day |
|---|---:|---:|---:|---:|
| Starter | 0 | 60 | 3 | 5,000 |
| Growth | 10,000 | 120 | 5 | 25,000 |
| Scale | 100,000 | 300 | 10 | 100,000 |
| Premier | 1,000,000 | 600 | 20 | 500,000 |

The key page shows your level, usage and credits to the next level.

## Make a first request with curl or Python

The installer sets `RADAR_API_URL`; without it, `export RADAR_API_URL=https://radar-api.fliarbi.com`.

```bash
curl -sS "$RADAR_API_URL/v1/companies/financials" \
  -H "Authorization: Bearer $RADAR_API_KEY" -H 'Content-Type: application/json' \
  -d '{"domain":"zomato.com","statement":"income","period_type":"annual"}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "/v1/companies/search", headers={"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]},
                  json={"filters": {"industries": ["FinTech"], "locations": ["India"]}, "limit": 20}, timeout=120)
for c in r.json()["data"]["companies"]:
    print(c["name"], c["domain"], c.get("hq"))
```

## Connect an MCP client

Remote (Streamable HTTP), for Claude Code, Codex and other clients with custom headers:

```json
{
  "mcpServers": {
    "radar": {
      "type": "http",
      "url": "https://radar-api.fliarbi.com/mcp",
      "headers": {"Authorization": "Bearer ${RADAR_API_KEY}"}
    }
  }
}
```

Try: “Find fintech companies in India, compare two companies' financials, and show the news
and funding behind their recent activity.”


## What you can retrieve

| Area | Capabilities |
|---|---|
| Companies | Filtered and natural-language search, profiles, competitors, intelligence, comparison |
| Financials | Income, balance-sheet and cash-flow metrics, annual/quarterly filters, source labels |
| Activity | Company events, funding rounds, legal details, reputation, hiring, digital presence |
| Investors and markets | Investor search/directory/pages, market pulse, location intelligence, industry discovery |
| People and jobs | Professional search, job filters/suggestions, salaries, experience, employment types, sources and hiring companies |
| Internships | Skill/location/stipend/date search, employer lists, listing detail and deadline qualifications |
| Mobile apps | App/category search, exact-host company apps, compact profiles, ratings, monetization, growth and install history |
| Company potential | Six explainable growth, investment and B2B prospecting screens with measured evidence |
| News | General/business headlines, full articles, volume, sentiment, overview, business events, funding coverage |
| Combined research | Company brief with section-level errors, access limits and dates |

The 53 MCP tools are retrieval operations. Optional account-management HTTP routes
are separate. Email/phone retrieval requires explicit contact scope and a paid
linked Radar account. CRM sending, applications and resume handling are not included. Published investor pages
now expose measured summaries and separate paginated fields from a verified Atlas release.
The optional investor data connection is required for detail; source publication gates remain authoritative.

Read the [user guide](docs/USER_GUIDE.md), [capability map](docs/CAPABILITIES.md),
[getting started](docs/GETTING_STARTED.md) and [verification record](docs/VERIFICATION.md).
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
| App and mobile intelligence | [Individual apps, ratings and install growth](docs/guides/apps-data-api.md) |
| Early-career hiring | [Internship listings and employer lists](docs/guides/internships-companies-api.md) |
| Growth research and sales prospects | [Company potential data](docs/guides/potential-company-data-api.md) |
| AI-agent research tools | [Company intelligence MCP server](docs/guides/company-intelligence-mcp-server.md) |

These guides include request examples, interpretation details, source coverage and
common integration questions. [Search research](docs/SEARCH_RESEARCH.md) and the
[keyword research](docs/research/KEYWORD_RESEARCH.md) record how topics were chosen.

## Data depth, references and tested scenarios

**Company data depth:** [see real Razorpay, Stripe and Swiggy records](docs/COMPANY_DATA_DEPTH.md)
with sectors, primary/other feeds, founders, technology stacks, website performance,
traffic, apps, products, hiring, patents and social data. Start with compact identity
and available fields, then request one of 18 fields separately.
[Filters and listing columns](docs/FILTERS_AND_LISTINGS.md) and
[email/phone retrieval](docs/CONTACTS.md) have separate JSON POST workflows.

Start with [real endpoint request/response examples](docs/reference/README.md):
all **53 data operations and 16 account/discovery operations**, plus a captured
MCP session and browser-route responses. Each reference includes parameter tables,
REST/MCP calls, field explanations and downloadable JSON. The 19 workflow guides
also include worked outputs inline. [Observed data quality](docs/DATA_QUALITY.md)
explains identity mismatches, incomplete searches and unavailable News connections.

Financial responses distinguish filing-derived figures from news-reported earnings,
retain fiscal periods and currencies, and disclose when the linked Radar account
exposes only part of the archive. Company briefs combine multiple sections and
mark individual failures instead of treating unavailable data as zero.

**Tested business questions:** [50 executed requests and full outputs](docs/scenarios/README.md),
[baseline findings and repairs](docs/SCENARIO_AUDIT.md), and
[all 43 company filters analysed](docs/FILTER_AUDIT.md).
**Business-model recipes:** [10 additional scenarios](docs/scenarios/README.md#business-model-and-revenue-model-scenarios),
starting with [investment companies earning commission per deal](docs/scenarios/51-investment-commission-per-deal.md).
These include full captured main-search responses, REST/MCP requests and evidence
review steps; additional variants are labeled as recipes.
Start with [exact financial screening](docs/guides/financial-filters-data-api.md),
[company teams and professional data](docs/guides/teams-people-data-api.md), or
[technology stacks and website traffic](docs/guides/technology-traffic-data-api.md).

The [endpoint output audit](docs/OUTPUT_DEPTH_AUDIT.md) explains which endpoint owns
each kind of detail, the richer financial/company/app outputs, and current live
coverage failures. [Complete company examples](docs/COMPANY_DATA_DEPTH.md) include
traffic devices and ranks, customer-review samples, lifecycle context and LinkedIn observations.

**Contact and social workflows:** [founder details and contacts](docs/guides/founder-contact-data-api.md),
[company/professional emails](docs/guides/company-email-phone-api.md),
[LinkedIn and social references](docs/guides/linkedin-social-data-api.md),
[24 request recipes](docs/CONTACT_REQUEST_RECIPES.md) and the
[research findings index](docs/research/README.md).

**Expanded data workflows:** [mobile apps and seven detail fields](docs/guides/apps-data-api.md),
[companies offering internships](docs/guides/internships-companies-api.md), and
[company growth potential and B2B prospects](docs/guides/potential-company-data-api.md).
Real examples include four exact-host Swiggy apps, dated install growth and internship
requirements/stipends. See the [Radar coverage map](docs/RADAR_FEATURE_COVERAGE.md).

## Run your own gateway

Most users only need the hosted API above. To run the gateway yourself (operators with
their own Radar upstream), install the server package instead:

```bash
curl -fsSL https://raw.githubusercontent.com/fliarbi/radar-api-mcp/main/scripts/install-server.sh | bash
~/.local/share/radar-api-mcp/bin/radar-api --port 8810
```

See [installation and operator setup](docs/INSTALL.md) and [operations](docs/OPERATIONS.md).

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

Investor depth: [portfolio, cohorts, co-investors and sourced news](docs/INVESTOR_DATA_DEPTH.md).
The [response depth audit](docs/DATA_DEPTH_AUDIT.md) checks every endpoint example for silently omitted business fields.
