# Radar with Claude Code or Codex: seven animated API use cases

These GIFs show **client-built research UI concepts**: a large typed prompt slides
off-screen, a full-screen chart appears, then a detailed result view follows. Each
32-second loop gives the prompt and results their own space. The accompanying tool
recipes show the focused Radar MCP reads behind each view. They are not screen recordings of
the official Claude Code or Codex interface. Connecting MCP exposes tools; it does
not automatically install these dashboards. An assistant can build a local view
or format the results as a table when you ask it to.

Open the [interactive gallery](demos/index.html) locally for play/pause, replay,
copyable prompts, tool recipes, GIF downloads and still images. All seven GIFs
also render below on GitHub. Each has a persistent data-provenance badge. No live
service, account, contact reveal or payment is exercised by these animations.

| Workflow | Displayed evidence |
|---|---|
| Competitor analysis | Selected saved Radar peer cards |
| Financial comparison | Saved FY2025 news-derived income metrics |
| Founders and LinkedIn | Saved founder/professional lookups, including an unresolved match |
| GenAI startups | Fictional cohort demonstrating the UI and tool recipe |
| San Francisco funding in April 2026 | Fictional announcements; explicit publication and city checks |
| Top 10 dating apps and legal details | Fictional ranking and legal record, not a real market result |
| Founder emails to Excel | Synthetic identities/addresses and an illustrated local export |

To ask an agent to make a similar view, prepend this instruction to a prompt:

> Use my configured Radar MCP connection. Retrieve the available evidence, then
> build a simple local research view. Keep dates, source types, missing fields
> and access failures visible. Do not invent unavailable data.

The [MCP integration guide](guides/company-intelligence-mcp-server.md) and
[key onboarding](guides/api-keys-authentication.md) describe the existing private
preview connection. These illustrations do not establish current source uptime.

## Competitor analysis

![Map your competitive landscape. Captured data · 23 Sep 2026.](demos/media/competitor-analysis.gif)

**Prompt:** Find payment-company peers. Compare their recorded funding stages, locations and product focus. Keep source labels visible.

**What you would see:** The prompt becomes a Payments peer matrix with company domains, source-labelled stages, cities and recorded product focus. A stacked stage-distribution bar opens the result, followed by a full-width comparison table with all five complete product descriptions. The client selects five rows from the fifteen captured peer cards; the chart describes that selected sample, not market share. This is market-based discovery, not a claim that every candidate directly competes with every other one.

**Radar tool recipe:** `find_competitors`. Local selection, formatting and file writing are client actions.

[Download GIF](demos/media/competitor-analysis.gif) · [Static image](demos/media/competitor-analysis.png) · [API guide](guides/competitor-intelligence-api.md)

Source material: [find_competitors.json](examples/find_competitors.json).

## Financial comparison

![Compare financials without losing context. Captured data · 24 Sep 2026.](demos/media/financial-comparison.gif)

**Prompt:** Compare Qualys and Mastech Digital for FY2025: revenue, net income and EBITDA. Keep negative values, missing metrics and source types.

**What you would see:** The view compares two saved FY2025 observations with a grouped revenue/net-income column chart, calculated net margins, and a separate full-screen metric table. The table also includes available operating income and earnings per share, retaining the missing EPS currency. Qualys revenue is USD 669.1M and net income USD 198.3M; Mastech Digital revenue is USD 191.371M and net income USD -0.609M. Both are news_report metrics. Missing Mastech EBITDA remains missing. Exact period-end dates are unavailable, so a shared fiscal label does not certify matching calendar windows. Balance-sheet/cash-flow source availability is not demonstrated by this income comparison.

**Radar tool recipe:** `get_financials`, `get_financials`. Local selection, formatting and file writing are client actions.

[Download GIF](demos/media/financial-comparison.gif) · [Static image](demos/media/financial-comparison.png) · [API guide](guides/financial-filters-data-api.md)

Source material: [19-precise-profit-screen.json](examples/scenarios/19-precise-profit-screen.json), [mastech-annual-income.json](examples/additional/mastech-annual-income.json).

## Founders & LinkedIn

![Go from a company to founder profiles. Captured data · 23 Sep 2026.](demos/media/founder-linkedin.gif)

**Prompt:** Find Razorpay’s recorded founders and their LinkedIn profiles. Show roles and background. Leave unresolved identity matches unlinked.

**What you would see:** The client first retrieves company founders, then performs separate professional searches. The captured Shashank Kumar record supplies a recorded Razorpay affiliation, LinkedIn URL, location, all three recorded education entries and all eight skills. A relationship diagram gives way to a full-screen background view and the LinkedIn source URL. The exact Harshil Mathur lookup returned no professional card and stays unresolved. Source professional records are not independent identity or current-employment verification; no founder email or phone is revealed in this animation.

**Radar tool recipe:** `get_company_team`, `search_people`, `search_people`. Local selection, formatting and file writing are client actions.

[Download GIF](demos/media/founder-linkedin.gif) · [Static image](demos/media/founder-linkedin.png) · [API guide](guides/founder-contact-data-api.md)

Source material: [21-razorpay-founders.json](examples/scenarios/21-razorpay-founders.json), [founder-shashank.json](examples/contacts/founder-shashank.json), [founder-professional.json](examples/contacts/founder-professional.json).

## GenAI startups

![Turn a GenAI question into a company list. Illustrative data · fictional companies.](demos/media/genai-startups.gif)

**Prompt:** List US generative AI startups founded since 2021. Show what they build, where they are based and which company details I can open next.

**What you would see:** The illustrated result begins with a founding-year dot plot, then opens a five-company table with domains, founding year, US location and product focus. These companies and their attributes are fictional. The tool recipe uses semantic discovery with location/founding-year filters, followed by an explicit classification read. The client still needs to review classifications and matching metadata; a semantic result is not automatically a verified GenAI startup.

**Radar tool recipe:** `semantic_company_search`, `get_company_field`. Local selection, formatting and file writing are client actions.

[Download GIF](demos/media/genai-startups.gif) · [Static image](demos/media/genai-startups.png) · [API guide](guides/company-search-api.md)

No captured result set is claimed. All displayed company/app identities and numerical rows are illustrative.

## SF funding · April 2026

![Find funding announcements in a dated window. Illustrative data · fictional funding rows.](demos/media/sf-funding-april-2026.gif)

**Prompt:** As of 30 April 2026, show San Francisco startups with funding announcements from 1–30 April. Keep round amounts, dates and location evidence.

**What you would see:** Here recent means published from 1 through 30 April 2026, with a 30 April cutoff. A dated timeline places all four fictional announcements within April, then a full-screen funding ledger retains domains, dates, round types and amounts. The USD 50.2M displayed total is the sum of these four fictional round amounts, not a real San Francisco funding total. The API does not have a city parameter on funding-news search: the client resolves company identities, reads geography separately and filters verified San Francisco city matches, excluding unresolved identities and nearby cities. It follows news cursors, deduplicates transaction coverage and distinguishes a round amount from a valuation. A newer HQ snapshot cannot establish a company's HQ as of April; this is not a historical point-in-time reconstruction or a verified list of actual April recipients.

**Radar tool recipe:** `search_funding_news`, `get_company_field`. Local selection, formatting and file writing are client actions.

[Download GIF](demos/media/sf-funding-april-2026.gif) · [Static image](demos/media/sf-funding-april-2026.png) · [API guide](guides/funding-news-api.md)

No captured result set is claimed. All displayed company/app identities and numerical rows are illustrative.

## Dating apps & legal data

![Rank apps, then inspect the company behind them. Illustrative data · not a real app ranking.](demos/media/dating-apps-legal.gif)

**Prompt:** Show the top 10 observed Google Play Dating apps by recorded installs. Join developer websites to company legal records, keeping uncertain ownership links explicit.

**What you would see:** A horizontal lollipop chart shows all ten fictional apps in descending stored install order within the Google Play Dating category. A second full-screen view traces the selected app to its developer website and illustrative legal record. This is neither an actual top-ten ranking nor an all-platform market census. In real use, discover the source category label, retain observation dates, inspect pagination and then read each app's developer field. Resolve the developer website to a company and request its legal field separately. Missing or ambiguous company joins remain unresolved. A shared website alone does not verify ownership; installs do not mean active users. The registry reference shown is deliberately a DEMO value.

**Radar tool recipe:** `search_apps`, `get_app_field`, `get_company_field`. Local selection, formatting and file writing are client actions.

[Download GIF](demos/media/dating-apps-legal.gif) · [Static image](demos/media/dating-apps-legal.png) · [API guide](guides/apps-data-api.md)

No captured result set is claimed. All displayed company/app identities and numerical rows are illustrative.

## Founder emails to Excel

![Turn permitted founder contacts into a workbook. Synthetic contacts · no real email reveal.](demos/media/founder-email-excel.gif)

**Prompt:** Export the permitted founder emails to an Excel workbook. Include the company and contact source. Keep missing emails and company-mailbox fallbacks clearly marked.

**What you would see:** The illustrated worksheet uses fictional identities and reserved example.com emails. A contact-coverage donut counts the three synthetic row types; a separate full-width worksheet then shows all three rows: a person-record email, an explicitly marked company mailbox and a missing email. Real use requires identity resolution, explicit contacts scope and a paid linked Radar plan before contact retrieval. The agent or your application writes the local .xlsx file; there is no Radar export or email-sending tool. The animation illustrates a save and does not claim a real workbook was exported, an address was verified, or any message was sent.

**Radar tool recipe:** `get_company_team`, `get_person_contacts`. Local selection, formatting and file writing are client actions.

[Download GIF](demos/media/founder-email-excel.gif) · [Static image](demos/media/founder-email-excel.png) · [API guide](CONTACTS.md)

Source material: [person-direct.json](examples/contacts/person-direct.json), [person-company-fallback.json](examples/contacts/person-company-fallback.json), [person-no-data.json](examples/contacts/person-no-data.json).

## Reproduce and inspect

The [story data](demos/demo-data.json) records prompts, validated tool requests, source paths/hashes and data labels. The [renderer instructions](demos/README.md) explain deterministic frame capture, GIF encoding, reduced-motion behavior and verification. The API contracts and saved source captures are unchanged.
