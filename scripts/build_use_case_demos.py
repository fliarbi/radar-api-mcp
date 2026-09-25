#!/usr/bin/env python3
"""Build source-qualified UI animation stories without calling any live service."""
import hashlib
import json
from pathlib import Path

from radar_api.service import BY_NAME

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "docs/demos"


def read(relative):
    return json.loads((ROOT / "docs/examples" / relative).read_text())


def tool(name, request, label):
    BY_NAME[name].model.model_validate(request)
    return {"name": name, "request": request, "label": label, "type": "radar"}


def local(label, detail):
    return {"name": detail, "label": label, "type": "client"}


def evidence(paths):
    return [{"file": "../examples/" + p, "sha256": hashlib.sha256((ROOT / "docs/examples" / p).read_bytes()).hexdigest()} for p in paths]


def build():
    peers = read("find_competitors.json")["response"]["data"]["companies"]
    chosen = {"Param", "TNG Digital", "Atome", "Flip", "Clara"}
    peer_rows = [{"name": c["name"], "domain": c["domain"], "stage": stage,
                  "city": c["location"].title(), "description": c["description"]}
                 for stage, group in peers.items() for c in group if c["name"] in chosen]
    qualys = read("scenarios/19-precise-profit-screen.json")["current"]["response"]["data"]["matches"][0]["period"]
    mastech = read("additional/mastech-annual-income.json")["response"]["data"]["periods"][0]
    person = read("contacts/founder-shashank.json")["response"]["data"]["people"][0]
    finance_rows = [{"name": name, "domain": domain, "period": period["period"],
                     "metrics": period["metrics"], "period_end": period["period_end"]}
                    for name, domain, period in (("Qualys", "qualys.com", qualys), ("Mastech Digital", "mastechdigital.com", mastech))]
    common = {"duration": 32, "width": 1280, "height": 800,
              "disclosure": "Concept UI, not a recording of Claude Code or Codex. Tool activity is animated; no live requests run."}
    stories = [
        {"id": "competitor-analysis", "title": "Map your competitive landscape", "nav": "Competitor analysis", "client": "Claude Code",
         "kind": "captured", "badge": "Captured data · 23 Sep 2026", "view": "peers",
         "prompt": "Find payment-company peers. Compare their recorded funding stages, locations and product focus. Keep source labels visible.",
         "result_title": "Payments peer matrix", "result_subtitle": "5 selected candidates from 15 captured cards",
         "steps": [tool("find_competitors", {"market": "Payments", "per_stage": 3}, "Discover payment companies"),
                   local("Review the source labels", "Stages and locations are recorded observations"), local("Build a comparison view", "Client-side table, no new API endpoint")],
         "rows": peer_rows, "footnote": "Source-labelled peers, not independently confirmed direct competitors.",
         "takeaway": "Ask a market question. Get a shortlist you can inspect, compare and refine.",
         "sources": evidence(["find_competitors.json"]), "guide": "../guides/competitor-intelligence-api.md"},
        {"id": "financial-comparison", "title": "Compare financials without losing context", "nav": "Financial comparison", "client": "Codex",
         "kind": "captured", "badge": "Captured data · 24 Sep 2026", "view": "finance",
         "prompt": "Compare Qualys and Mastech Digital for FY2025: revenue, net income and EBITDA. Keep negative values, missing metrics and source types.",
         "result_title": "FY2025 financial comparison", "result_subtitle": "Reported USD metrics · news_report sources",
         "steps": [tool("get_financials", {"domain": "qualys.com", "statement": "income", "period_type": "annual", "year_from": 2025, "year_to": 2025, "limit": 3}, "Read Qualys income"),
                   tool("get_financials", {"domain": "mastechdigital.com", "statement": "income", "period_type": "annual", "year_from": 2025, "year_to": 2025, "limit": 3}, "Read Mastech income"),
                   local("Align the fiscal labels", "Do not invent missing calendar-period dates")],
         "rows": finance_rows, "footnote": "Both labeled FY2025; exact period-end dates are missing. Not audited filings.",
         "takeaway": "Compare real metrics, with source provenance and missing values intact.",
         "sources": evidence(["scenarios/19-precise-profit-screen.json", "additional/mastech-annual-income.json"]), "guide": "../guides/financial-filters-data-api.md"},
        {"id": "founder-linkedin", "title": "Go from a company to founder profiles", "nav": "Founders & LinkedIn", "client": "Claude Code",
         "kind": "captured", "badge": "Captured data · 23 Sep 2026", "view": "founder",
         "prompt": "Find Razorpay’s recorded founders and their LinkedIn profiles. Show roles and background. Leave unresolved identity matches unlinked.",
         "result_title": "A founder profile with its source link", "result_subtitle": "Recorded affiliation, not a verified current-role check",
         "steps": [tool("get_company_team", {"domain": "razorpay.com", "group": "founders", "limit": 10}, "Read company founders"),
                   tool("search_people", {"name": "Shashank Kumar", "companies": ["razorpay.com"], "limit": 3}, "Resolve a professional profile"),
                   tool("search_people", {"name": "Harshil Mathur", "companies": ["razorpay.com"], "limit": 3}, "Keep unresolved matches visible")],
         "person": {key: person[key] for key in ("name", "current_title", "current_company", "current_company_domain", "location", "linkedin_url", "education", "skills")},
         "unresolved": "Harshil Mathur", "footnote": "No contact values revealed. Missing professional matches stay unresolved.",
         "takeaway": "Follow a recorded LinkedIn link, without guessing which person a name refers to.",
         "sources": evidence(["scenarios/21-razorpay-founders.json", "contacts/founder-shashank.json", "contacts/founder-professional.json"]), "guide": "../guides/founder-contact-data-api.md"},
        {"id": "genai-startups", "title": "Turn a GenAI question into a company list", "nav": "GenAI startups", "client": "Codex",
         "kind": "illustrative", "badge": "Illustrative data · fictional companies", "view": "startups",
         "prompt": "List US generative AI startups founded since 2021. Show what they build, where they are based and which company details I can open next.",
         "result_title": "A researchable GenAI shortlist", "result_subtitle": "Fictional rows illustrating the output your client could build",
         "steps": [tool("semantic_company_search", {"q": "generative AI startups", "filters": {"locations": ["United States"], "founded_year_from": 2021}, "limit": 5}, "Discover candidate companies"),
                   tool("get_company_field", {"domain": "aster.example", "field": "classification", "item_limit": 10}, "Inspect classifications separately"),
                   local("Review the candidate fit", "Semantic matches need classification checks")],
         "rows": [
             ["Aster Research", "aster.example", "2022", "San Francisco", "Model evaluation"],
             ["Clearframe AI", "clearframe.example", "2023", "New York", "Generative video"],
             ["Harbor Reasoning", "harbor.example", "2021", "Boston", "Enterprise agents"],
             ["Folio Models", "folio.example", "2024", "Seattle", "Document intelligence"],
             ["Signal Foundry", "signalfoundry.example", "2023", "Austin", "Speech generation"]],
         "footnote": "Demo cohort. Semantic candidates are not automatically verified GenAI matches.",
         "takeaway": "Discover a segment, inspect classifications, then retrieve only the fields you need.",
         "sources": [], "guide": "../guides/company-search-api.md"},
        {"id": "sf-funding-april-2026", "title": "Find funding announcements in a dated window", "nav": "SF funding · April 2026", "client": "Claude Code",
         "kind": "illustrative", "badge": "Illustrative data · fictional funding rows", "view": "funding",
         "prompt": "As of 30 April 2026, show San Francisco startups with funding announcements from 1–30 April. Keep round amounts, dates and location evidence.",
         "result_title": "San Francisco funding watch", "result_subtitle": "Publication window: 1–30 April 2026",
         "steps": [tool("search_funding_news", {"q": "funding", "country": "United States", "date_from": "2026-04-01", "date_to": "2026-04-30", "limit": 50}, "Read the April announcement window"),
                   tool("get_company_field", {"domain": "bellweather.example", "field": "geography", "item_limit": 10}, "Check company geography"),
                   local("Keep San Francisco matches", "Client-side city check and round deduplication")],
         "rows": [["Bellweather AI", "bellweather.example", "28 Apr", "Seed", "$8.2M"],
                  ["North Pier Robotics", "northpier.example", "23 Apr", "Series A", "$14M"],
                  ["Signal Harbor", "signalharbor.example", "11 Apr", "Seed", "$6M"],
                  ["Foundry Graph", "foundrygraph.example", "03 Apr", "Series A", "$22M"]],
         "footnote": "April publication window only. Newer HQ records cannot establish April HQ history.",
         "takeaway": "Choose a date cutoff and verify city evidence; a Bay Area mention is not an SF match.",
         "sources": [], "guide": "../guides/funding-news-api.md"},
        {"id": "dating-apps-legal", "title": "Rank apps, then inspect the company behind them", "nav": "Dating apps & legal data", "client": "Codex",
         "kind": "illustrative", "badge": "Illustrative data · not a real app ranking", "view": "apps", "duration": 32,
         "prompt": "Show the top 10 observed Google Play Dating apps by recorded installs. Join developer websites to company legal records, keeping uncertain ownership links explicit.",
         "result_title": "Dating apps ranked by stored installs", "result_subtitle": "Google Play cohort · illustrative values · source dates required",
         "steps": [tool("search_apps", {"category": "Dating", "sort_by": "installs", "limit": 10, "page": 0}, "Rank the recorded app cohort"),
                   tool("get_app_field", {"app_id": "com.example.orbit.dating", "field": "developer"}, "Read developer details"),
                   tool("get_company_field", {"domain": "orbit.example", "field": "legal", "item_limit": 10}, "Retrieve company legal detail")],
         "rows": [["Demo Orbit", "orbit.example", 54200000], ["Demo Kindred", "kindred.example", 39800000],
                  ["Demo Pair", "pair.example", 28400000], ["Demo Together", "together.example", 19600000],
                  ["Demo Hello", "hello.example", 14200000], ["Demo Spark", "spark.example", 9800000],
                  ["Demo Sunday", "sunday.example", 7400000], ["Demo Clover", "clover.example", 5600000],
                  ["Demo Hearts", "hearts.example", 3900000], ["Demo Trail", "trail.example", 2800000]],
         "legal": {"company": "Orbit Example Ltd", "domain": "orbit.example", "jurisdiction": "England and Wales", "registry": "DEMO-10001", "developer": "Orbit Example Studio"},
         "footnote": "Installs are not active users. Website association is not verified legal ownership.",
         "takeaway": "Keep the ranking and the legal join separate, with dates and unresolved matches visible.",
         "sources": [], "guide": "../guides/apps-data-api.md"},
        {"id": "founder-email-excel", "title": "Turn permitted founder contacts into a workbook", "nav": "Founder emails to Excel", "client": "Codex",
         "kind": "illustrative", "badge": "Synthetic contacts · no real email reveal", "view": "excel", "duration": 32,
         "prompt": "Export the permitted founder emails to an Excel workbook. Include the company and contact source. Keep missing emails and company-mailbox fallbacks clearly marked.",
         "result_title": "Founder contacts, with provenance", "result_subtitle": "Synthetic export demonstration · contact scope + paid plan required",
         "steps": [tool("get_company_team", {"domain": "example.com", "group": "founders", "limit": 10}, "Resolve founder identities"),
                   tool("get_person_contacts", {"person_id": "example-founder", "fields": ["emails"]}, "Read permitted email fields"),
                   local("Write the workbook locally", "Client creates .xlsx; Radar has no export endpoint")],
         "rows": [["Alex Example", "Example Labs", "alex@example.com", "Person record"],
                  ["Jordan Sample", "Sample Works", "sales@example.com", "Company mailbox"],
                  ["Taylor Demo", "Demo Studio", "", "No email returned"]],
         "filename": "founder-contacts.demo.xlsx", "footnote": "Synthetic addresses. No message is sent; source presence does not verify deliverability.",
         "takeaway": "The agent can write a local spreadsheet after scoped reads, preserving missing data.",
         "sources": evidence(["contacts/person-direct.json", "contacts/person-company-fallback.json", "contacts/person-no-data.json"]), "guide": "../CONTACTS.md"},
    ]
    data = [{**common, **story} for story in stories]
    DEST.mkdir(parents=True, exist_ok=True)
    (DEST / "demo-data.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    (DEST / "demo-data.js").write_text("window.RADAR_DEMOS = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n")
    paragraphs = {
        "competitor-analysis": "The prompt becomes a Payments peer matrix with company domains, source-labelled stages, cities and recorded product focus. A stacked stage-distribution bar opens the result, followed by a full-width comparison table with all five complete product descriptions. The client selects five rows from the fifteen captured peer cards; the chart describes that selected sample, not market share. This is market-based discovery, not a claim that every candidate directly competes with every other one.",
        "financial-comparison": "The view compares two saved FY2025 observations with a grouped revenue/net-income column chart, calculated net margins, and a separate full-screen metric table. The table also includes available operating income and earnings per share, retaining the missing EPS currency. Qualys revenue is USD 669.1M and net income USD 198.3M; Mastech Digital revenue is USD 191.371M and net income USD -0.609M. Both are news_report metrics. Missing Mastech EBITDA remains missing. Exact period-end dates are unavailable, so a shared fiscal label does not certify matching calendar windows. Balance-sheet/cash-flow source availability is not demonstrated by this income comparison.",
        "founder-linkedin": "The client first retrieves company founders, then performs separate professional searches. The captured Shashank Kumar record supplies a recorded Razorpay affiliation, LinkedIn URL, location, all three recorded education entries and all eight skills. A relationship diagram gives way to a full-screen background view and the LinkedIn source URL. The exact Harshil Mathur lookup returned no professional card and stays unresolved. Source professional records are not independent identity or current-employment verification; no founder email or phone is revealed in this animation.",
        "genai-startups": "The illustrated result begins with a founding-year dot plot, then opens a five-company table with domains, founding year, US location and product focus. These companies and their attributes are fictional. The tool recipe uses semantic discovery with location/founding-year filters, followed by an explicit classification read. The client still needs to review classifications and matching metadata; a semantic result is not automatically a verified GenAI startup.",
        "sf-funding-april-2026": "Here recent means published from 1 through 30 April 2026, with a 30 April cutoff. A dated timeline places all four fictional announcements within April, then a full-screen funding ledger retains domains, dates, round types and amounts. The USD 50.2M displayed total is the sum of these four fictional round amounts, not a real San Francisco funding total. The API does not have a city parameter on funding-news search: the client resolves company identities, reads geography separately and filters verified San Francisco city matches, excluding unresolved identities and nearby cities. It follows news cursors, deduplicates transaction coverage and distinguishes a round amount from a valuation. A newer HQ snapshot cannot establish a company's HQ as of April; this is not a historical point-in-time reconstruction or a verified list of actual April recipients.",
        "dating-apps-legal": "A horizontal lollipop chart shows all ten fictional apps in descending stored install order within the Google Play Dating category. A second full-screen view traces the selected app to its developer website and illustrative legal record. This is neither an actual top-ten ranking nor an all-platform market census. In real use, discover the source category label, retain observation dates, inspect pagination and then read each app's developer field. Resolve the developer website to a company and request its legal field separately. Missing or ambiguous company joins remain unresolved. A shared website alone does not verify ownership; installs do not mean active users. The registry reference shown is deliberately a DEMO value.",
        "founder-email-excel": "The illustrated worksheet uses fictional identities and reserved example.com emails. A contact-coverage donut counts the three synthetic row types; a separate full-width worksheet then shows all three rows: a person-record email, an explicitly marked company mailbox and a missing email. Real use requires identity resolution, explicit contacts scope and a paid linked Radar plan before contact retrieval. The agent or your application writes the local .xlsx file; there is no Radar export or email-sending tool. The animation illustrates a save and does not claim a real workbook was exported, an address was verified, or any message was sent.",
    }
    article = """# Radar with Claude Code or Codex: seven animated API use cases

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
"""
    for story in data:
        article += f"\n## {story['nav']}\n\n![{story['title']}. {story['badge']}.](demos/media/{story['id']}.gif)\n\n"
        article += f"**Prompt:** {story['prompt']}\n\n**What you would see:** {paragraphs[story['id']]}\n\n"
        article += "**Radar tool recipe:** " + ", ".join(f"`{step['name']}`" for step in story['steps'] if step['type'] == 'radar') + ". Local selection, formatting and file writing are client actions.\n\n"
        article += f"[Download GIF](demos/media/{story['id']}.gif) · [Static image](demos/media/{story['id']}.png) · [API guide]({story['guide'].removeprefix('../')})\n\n"
        if story['sources']:
            article += "Source material: " + ", ".join(f"[{Path(source['file']).name}]({source['file'].removeprefix('../')})" for source in story['sources']) + ".\n"
        else:
            article += "No captured result set is claimed. All displayed company/app identities and numerical rows are illustrative.\n"
    article += "\n## Reproduce and inspect\n\nThe [story data](demos/demo-data.json) records prompts, validated tool requests, source paths/hashes and data labels. The [renderer instructions](demos/README.md) explain deterministic frame capture, GIF encoding, reduced-motion behavior and verification. The API contracts and saved source captures are unchanged.\n"
    (ROOT / "docs/ANIMATED_USE_CASES.md").write_text(article)
    print(f"Built {len(data)} source-qualified stories; all Radar requests validated; no live calls.")


if __name__ == "__main__":
    build()
