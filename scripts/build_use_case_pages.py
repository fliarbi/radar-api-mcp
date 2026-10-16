#!/usr/bin/env python3
"""Render the keyword-researched use-case pages from saved Radar API captures.

Writes docs/use-cases/<segment>/<slug>.md for every kept page, one index per segment,
docs/use-cases/README.md, docs/research/KEYWORD_RESEARCH.md and the use-case section at
the top of README.md. Every number comes from a saved response in docs/examples/use-cases/.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scenario_common as sc  # noqa: E402
from scenario_common import bar, day, esc, month, n, pct, table, title_case, trim, usd  # noqa: E402

SEGMENTS = {
    "financial-news": ("Financial news research", "Measure financial news coverage of markets, rates, currencies, commodities, crypto, IPOs and policy: volume, tone, critical share, a twelve-month series and the most consequential headlines, through the Radar API's news operations."),
    "company-financials": ("Company financials research", "Read a company's reported revenue and profit by fiscal period, its recorded funding events and its news coverage: equity research, credit, sales and investor teams screening Indian startups and listed companies."),
    "industry-companies": ("Companies by industry", "List the companies in an industry in India with their headquarters, founding year and size, then map the global competitive set by stage and country: market maps, lead lists and competitor research."),
    "founders-leadership": ("Founders and leadership research", "Find who founded and runs a company, with recorded designations and a company snapshot: sales prospecting, investor diligence, partnerships and journalism."),
}
QUESTION = {
    "financial-news": "How much news did {t} receive between January and April 2026, how negative and critical was it, how did it trend over twelve months, and which headlines mattered most?",
    "company-financials": "What revenue and profit has {t} reported by fiscal year, where does each figure come from, which funding events are recorded, and how much news covered it in January–April 2026?",
    "industry-companies": "Which {t} companies are based in India, how large and how old are they, and who competes in the {t} market worldwide?",
    "founders-leadership": "Who founded {t}, who are its key people, and what does its company profile say?",
}
CLI = {"news_overview": "news-overview", "news_trends": "news-trends", "news_sentiment": "news-sentiment",
       "search_business_news": "search-business-news", "get_financials": "get-financials", "get_company_funding": "get-company-funding",
       "search_companies": "search-companies", "find_competitors": "find-competitors", "get_company_team": "get-company-team",
       "get_company": "get-company"}
METRICS = [("revenue", "Revenue"), ("net_income", "Net income"), ("ebitda", "EBITDA"), ("operating_income", "Operating income")]


def heading(s: dict) -> str:
    h = title_case(s["keyword"]["phrase"])
    return h


def subject(s: dict) -> str:
    return title_case(s["topic"]) if s["segment"] != "financial-news" else s["topic"]


def cli_args(body: dict, prefix: str = "") -> list[str]:
    out = []
    for k, v in body.items():
        name = (prefix + k).replace("_", "-")
        if isinstance(v, dict):
            out += cli_args(v, prefix + k + ".")
        else:
            for x in (v if isinstance(v, list) else [v]):
                x = str(x).lower() if isinstance(x, bool) else x
                out.append(f"--{name} " + (f'"{x}"' if isinstance(x, str) and (" " in x or "&" in x) else str(x)))
    return out


def run_it(s: dict) -> str:
    lines = [f"radar {CLI[c['feature']]} " + " ".join(cli_args(c["body"])) for c in s["calls"]]
    first, second = s["calls"][0], s["calls"][1]
    return f"""## Run it yourself

With the [one-line installer](../../../README.md#install-in-one-line) and your key saved (`radar login`):

```bash
{chr(10).join(lines)}
```

With curl (`RADAR_API_URL` is set by the installer; it defaults to `https://radar-api.fliarbi.com`):

```bash
curl -sS "$RADAR_API_URL{first['path']}" -H "Authorization: Bearer $RADAR_API_KEY" \\
  -H 'Content-Type: application/json' -d '{json.dumps(first['body'])}'
```

```python
import os, requests
base = os.environ.get("RADAR_API_URL", "https://radar-api.fliarbi.com")
r = requests.post(base + "{second['path']}", headers={{"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]}},
                  json={json.dumps(second['body'])}, timeout=120)
print(r.json()["data"])
```

The same operations are MCP tools ({", ".join(sorted({f"`{c['feature']}`" for c in s["calls"]}))}) at `$RADAR_API_URL/mcp`.
"""


def headline_rows(items: list[dict], q: str) -> tuple[list[list], int]:
    words = [w for w in re.findall(r"[a-z0-9]+", q.lower()) if w not in {"and", "the", "of"}] or [q.lower()]
    seen, rows, flagged = set(), [], 0
    for it in items:
        key = it["headline"].lower().strip()
        if key in seen or len(rows) == 12:
            continue
        seen.add(key)
        text = (it["headline"] + " " + (it.get("lede") or "")).lower()
        mark = "" if any(re.search(rf"\b{re.escape(w)}", text) for w in words) else " ⚠"
        flagged += bool(mark)
        rows.append([day(it["published_at"]), f"[{esc(trim(it['headline'], 110))}]({it['url']}){mark}",
                     esc(it["publisher"]), it.get("priority") or "—", (it.get("sentiment") or {}).get("group", "—")])
    return rows, flagged


def news_body(s, rec):
    ov, tr, se, hl = (sc.response(rec, k) for k in ("overview", "trends", "sentiment", "headlines"))
    tone = {g["group"]: g for g in (ov.get("tone") or {}).get("groups") or []}
    crit = ov.get("critical") or {}
    pts = tr.get("points") or []
    peak = max(pts, key=lambda p: p["articles"]) if pts else None
    glance = [["Matching articles, 1 Jan – 30 Apr 2026", n(ov.get("matched"))]]
    if tone:
        glance.append(["Negative · neutral · positive", " · ".join(pct(tone.get(g, {}).get("share_pct")) for g in ("negative", "neutral", "positive"))])
    if crit:
        glance.append(["Critical (priority 7–9)", f"{pct(crit.get('share_pct'))} ({n(crit.get('count'))} articles)"])
    if peak:
        glance.append(["Busiest month, May 2025 – Apr 2026", f"{month(peak['period'])} ({n(peak['articles'])} articles)"])
    if se.get("vs_baseline_ratio") is not None:
        glance.append(["Negative-to-positive vs all news", f"{se['vs_baseline_ratio']}×"])
    body = []
    if pts:
        top = max(p["articles"] for p in pts)
        body += ["## Twelve months of coverage", "", "Monthly matching articles (`news_trends`, `granularity=monthly`).", "",
                 table(["Month", "Articles", "Critical", "Negative", "Positive", ""],
                       [[month(p["period"]) + (" (partial)" if p.get("partial_period") else ""), n(p["articles"]),
                         pct(p.get("critical_pct")), n(p.get("negative")), n(p.get("positive")), bar(p["articles"], top)] for p in pts], "lrrrrl"), ""]
    rows, flagged = headline_rows(hl.get("items") or [], s["q"])
    unresolved = hl.get("unresolved") or 0
    body += ["## Critical headlines", "", "Business and financial news, priority 6 and above, sorted by priority (`search_business_news`, limit 25; up to 12 distinct headlines shown)."
             + (f" {unresolved} matching articles were temporarily unavailable from the article store at capture time." if unresolved else ""), ""]
    if rows:
        body += [table(["Date", "Headline", "Publisher", "Priority", "Tone"], rows, "llllr"), ""]
        if flagged:
            body += ["⚠ The subject phrase does not appear in that headline or its opening text; the article matched on tags or entities.", ""]
    else:
        body += ["No headline could be shown: matching articles were unavailable from the article store at capture time.", ""]
    return glance, body


def financials_body(s, rec):
    fin, fu, nw = (sc.response(rec, k) for k in ("financials", "funding", "news"))
    periods = fin.get("periods") or []
    summ = (fin.get("summary") or {})
    glance = [["Company domain", f"`{s['domain']}`"], ["Fiscal periods with figures", n(fin.get("available_period_count") or len(periods))]]
    if summ.get("narrative"):
        glance.append(["Summary", esc(trim(summ["narrative"], 160))])
    events = fu.get("events") or []
    glance.append(["Recorded funding events", n(len(events))])
    if nw.get("matched") is not None:
        glance.append(["News articles, Jan – Apr 2026", n(nw.get("matched"))])
    body = []
    if periods:
        rows, outliers = [], 0
        typical = {}
        for key, _ in METRICS:   # median of each metric across periods, to flag unit or currency slips
            vals = sorted(abs((p.get("metrics") or {}).get(key, {}).get("value") or 0) for p in periods)
            vals = [v for v in vals if v]
            typical[key] = vals[len(vals) // 2] if len(vals) >= 3 else None
        for p in periods:
            m = p.get("metrics") or {}
            cells = [esc(p.get("period") or "—")]
            for key, _ in METRICS:
                v = m.get(key) or {}
                val = v.get("value")
                mark = ""
                if val and typical.get(key) and abs(val) > 8 * typical[key]:
                    mark, outliers = " ⚠", outliers + 1
                cells.append(usd(val) + mark if val is not None else "—")
            srcs = sorted({(v or {}).get("source_type", "") for v in m.values()} - {""})
            cells.append(", ".join(x.replace("_", " ") for x in srcs) or "—")
            rows.append(cells)
        body += ["## Reported figures by fiscal period", "", "`get_financials` (all statements; USD as returned). A dash means the figure is not recorded, not zero.", "",
                 table(["Period"] + [lbl for _, lbl in METRICS] + ["Source"], rows, "lrrrrl"), "",
                 "“news report” figures are taken from news coverage of results; filing-derived figures say so. Check the source before comparing periods.", ""]
        if outliers:
            body += ["⚠ marks a figure more than eight times this company's typical value for that metric, usually a unit or currency slip in the source report. Verify it before use.", ""]
    if events:
        rows = [[esc(e.get("date") or "—"), esc(e.get("round_type") or "—"), usd(e.get("amount")) if e.get("amount") else "—",
                 esc(trim(e.get("headline"), 140))] for e in events[:12]]
        body += ["## Recorded funding events", "", "`get_company_funding`; amounts are reported figures" + (" (approximate)." if fu.get("amount_approx") else "."), "",
                 table(["Date", "Round", "Amount (USD)", "Evidence"], rows, "llrl"), ""]
    tone = {g["group"]: g for g in (nw.get("tone") or {}).get("groups") or []}
    if tone:
        body += ["## News coverage, Jan – Apr 2026", "", f"`news_overview` for company `{s['domain']}`: {n(nw.get('matched'))} articles; "
                 + " · ".join(f"{g} {pct(tone.get(g, {}).get('share_pct'))}" for g in ("negative", "neutral", "positive"))
                 + (f"; {pct((nw.get('critical') or {}).get('share_pct'))} critical." if nw.get("critical") else "."), ""]
    return glance, body


def industry_body(s, rec):
    co, cp = sc.response(rec, "companies"), sc.response(rec, "competitors")
    comps = co.get("companies") or []
    glance = [["Radar industry", f"“{s['industry']}”"], ["Companies returned (India, first page)", n(len(comps))]]
    summ = cp.get("summary") or {}
    if summ.get("total"):
        glance.append([f"Competitive set for “{s['topic']}” (worldwide)", n(summ["total"])])
    body = []
    if comps:
        rows = [[esc(c.get("name") or "—") + (f" ({esc(c['domain'])})" if c.get("domain") else ""), esc(title_case(c.get("hq") or "—")),
                 esc(c.get("founded") or "—"), esc(c.get("size") or "—"), esc(trim(c.get("tagline") or c.get("description"), 100))] for c in comps]
        body += [f"## {title_case(s['topic'])} companies in India", "",
                 "`search_companies` with the Radar industry filter and location India, first 20 results (`match_tier` strict unless noted).", "",
                 table(["Company", "HQ", "Founded", "Employees", "What they do"], rows, "lllll"), ""]
    stages = cp.get("companies") or {}
    if stages:
        rows = []
        for stage, items in stages.items():
            for c in items[:3]:
                rows.append([esc(stage), esc(c.get("name") or c.get("domain") or "—"), esc(title_case(c.get("location") or "—")),
                             esc(trim(c.get("description"), 100))])
        body += [f"## Competitive set: “{s['topic']}” worldwide", "",
                 "`find_competitors` (`per_stage=3`): companies grouped by stage." +
                 (" Countries: " + ", ".join(f"{title_case(k)} {v}" for k, v in sorted((summ.get("country") or {}).items(), key=lambda x: -x[1])[:6]) + "." if summ.get("country") else ""), "",
                 table(["Stage", "Company", "Location", "Description"], rows, "llll"), ""]
    return glance, body


def leadership_body(s, rec):
    fo, kp, pr = (sc.response(rec, k) for k in ("founders", "key_people", "profile"))
    company = pr.get("company") or {}
    glance = [["Company", esc(company.get("name") or title_case(s["topic"])) + f" (`{s['domain']}`)"],
              ["Founded", esc(company.get("founded") or "—")], ["Employees", esc(company.get("employee_count") or "—")],
              ["Founders recorded", n(len(fo.get("people") or []))], ["Key people recorded", n(len(kp.get("people") or []))]]
    body = []
    if fo.get("people"):
        body += ["## Founders", "", "`get_company_team` with `group=founders` (selected by recorded designation).", "",
                 table(["Name", "Designation"], [[esc(p.get("name")), esc(p.get("designation") or "—")] for p in fo["people"]], "ll"), ""]
    if kp.get("people"):
        body += ["## Key people", "", "`get_company_team` with `group=key_people`.", "",
                 table(["Name", "Designation"], [[esc(p.get("name")), esc(p.get("designation") or "—")] for p in kp["people"][:15]], "ll"), ""]
    if company.get("description"):
        body += ["## Company snapshot", "", esc(trim(company["description"], 400)), "",
                 "`get_company` returns this summary plus `available_fields`; request a field (technology, traffic, apps, legal…) with `get_company_field`.", ""]
    note = (fo.get("coverage") or {}).get("note")
    if note:
        body += [f"Coverage: {esc(note)}", ""]
    return glance, body


BODY = {"financial-news": news_body, "company-financials": financials_body,
        "industry-companies": industry_body, "founders-leadership": leadership_body}


def page(s: dict, rec: dict, related: list[dict]) -> str:
    seg = s["segment"]
    glance, body = BODY[seg](s, rec)
    out = [f"# {heading(s)}: Radar API example with live data", "",
           f"[{SEGMENTS[seg][0]}](README.md) · [All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)", "",
           f"> **Search demand:** {sc.search_line(s)}  ",
           f"> **Data:** {sc.coverage_line(rec)}. Saved API responses: [{s['slug']}.json](../../examples/use-cases/{s['slug']}.json).", "",
           f"**Question.** {QUESTION[seg].format(t=subject(s))}", "",
           "## At a glance", "", table(["Measure", "Value"], glance, "lr"), "", *body, run_it(s), "## Read the result carefully", ""]
    caveats = []
    if seg == "financial-news":
        caveats.append("Window: 1 Jan – 30 Apr 2026 for counts, tone and headlines; May 2025 – Apr 2026 for the monthly series. News intake thins after May 2026.")
    if rec.get("coverage_note"):
        caveats.append(f"Captured while part of the news index was offline ({rec['coverage_note']}): news counts are lower bounds.")
    caveats += [esc(x) for x in sc.notes(rec) if "unavailable" not in x.lower()][:6]
    out += [f"- {c}" for c in dict.fromkeys(caveats)] + [""]
    out += ["## Related use cases", ""] + [f"- [{heading(r)}]({r['slug']}.md)" for r in related] + [""]
    return "\n".join(out)


def index_row(s, rec):
    seg = s["segment"]
    if seg == "financial-news":
        return n(sc.response(rec, "overview").get("matched"))
    if seg == "company-financials":
        return n(len(sc.response(rec, "financials").get("periods") or []))
    if seg == "industry-companies":
        return n(len(sc.response(rec, "companies").get("companies") or []))
    return n(len(sc.response(rec, "founders").get("people") or []))


COLUMN = {"financial-news": "Articles Jan–Apr 2026", "company-financials": "Fiscal periods",
          "industry-companies": "Companies listed", "founders-leadership": "Founders recorded"}


def segment_index(seg, kept, recs):
    title, blurb = SEGMENTS[seg["id"]]
    rows = [[i, f"[{heading(s)}]({s['slug']}.md)", n(s["keyword"]["volume"].get("in") or None), n(s["keyword"]["volume"].get("us") or None),
             index_row(s, recs[s["slug"]])] for i, s in enumerate(kept, 1)]
    return f"""# {title}: {len(kept)} Radar API examples

[All use cases](../README.md) · [Keyword research](../../research/KEYWORD_RESEARCH.md) · [Getting started](../../GETTING_STARTED.md)

{blurb}

Each page answers one researched search query with saved live Radar API responses and the
exact CLI, curl, Python and MCP calls. Pages are ordered by search demand (India + US monthly
searches for the phrase and its variant).

{table(["#", "Use case", "India searches/mo", "US searches/mo", COLUMN[seg["id"]]], rows, "rlrrr")}
"""


def main() -> None:
    plan = json.loads(sc.PLAN.read_text())
    log = json.loads(sc.LOG.read_text())
    summary = []
    for seg in plan["segments"]:
        kept = [s for s in seg["scenarios"] if log.get(s["slug"], {}).get("kept")]
        recs = {s["slug"]: sc.load_capture(s["slug"]) for s in kept}
        d = sc.SCEN / seg["id"]
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.md"):
            old.unlink()
        for i, s in enumerate(kept):
            related = [kept[j] for j in (i - 2, i - 1, i + 1, i + 2) if 0 <= j < len(kept)][:4]
            (d / f"{s['slug']}.md").write_text(page(s, recs[s["slug"]], related))
        (d / "README.md").write_text(segment_index(seg, kept, recs))
        summary.append((seg, kept, recs))
    total = sum(len(k) for _, k, _ in summary)
    when = min(r["captured_at"] for _, _, recs in summary for r in recs.values())
    rows = [[f"[{SEGMENTS[seg['id']][0]}]({seg['id']}/README.md)", len(kept),
             ", ".join(f"[{heading(s)}]({seg['id']}/{s['slug']}.md)" for s in kept[:3])] for seg, kept, _ in summary]
    (sc.SCEN / "README.md").write_text(f"""# Radar API use cases: {total} worked examples

[README](../../README.md) · [Keyword research](../research/KEYWORD_RESEARCH.md) · [Getting started](../GETTING_STARTED.md) · [Tested scenarios](../scenarios/README.md)

Each page answers one real search query with saved responses from the live Radar API and the
exact CLI, curl, Python and MCP calls. Topics were chosen by [keyword research](../research/KEYWORD_RESEARCH.md)
(India and US monthly searches) and kept only when the API returned populated results.

{table(["Segment", "Pages", "Highest-demand pages"], rows, "lrl")}

Captured {day(when)} from https://radar-api.fliarbi.com. News counts are lower bounds while part
of the news index is offline; company, financial and people data are unaffected.

Regenerate: `scripts/plan_use_cases.py` → `scripts/capture_scenarios.py` → `scripts/build_use_case_pages.py`.
""")
    write_research(plan, log)
    rows = [[f"**[{SEGMENTS[seg['id']][0]}](docs/use-cases/{seg['id']}/README.md)**", len(kept),
             " · ".join(f"[{title_case(s['topic'])}](docs/use-cases/{seg['id']}/{s['slug']}.md)" for s in kept[:4])] for seg, kept, _ in summary]
    section = f"""{sc.README_START}
## {total} worked examples with live data

Each page answers one researched search query (“stock market news”, “Zomato revenue”, “fintech
companies in India”, “Razorpay founder”…) with saved live API responses and the exact CLI, curl,
Python and MCP calls. [Browse all {total}](docs/use-cases/README.md) or start with a segment:

{table(["Segment", "Pages", "Start with"], rows, "lrl")}

Topics come from [keyword research](docs/research/KEYWORD_RESEARCH.md) (India and US monthly searches).
Also see the [60 tested business scenarios](docs/scenarios/README.md).
{sc.README_END}"""
    readme = sc.ROOT / "README.md"
    readme.write_text(sc.replace_section(readme.read_text(), section, sc.README_START, sc.README_END, "## See the API in a research UI"))
    print({seg["id"]: len(kept) for seg, kept, _ in summary})


def write_research(plan, log):
    research = json.loads((sc.RESEARCH / plan["research"]).read_text())
    out = ["# Keyword research for the use-case pages", "",
           f"[All use cases](../use-cases/README.md) · [Raw data]({plan['research']})", "",
           f"Research date **{research['date']}**. {research['volume']}", "", research["method"], "",
           "Status: **page** = built; **thin** = captured but below the populated threshold; **excluded** = overlap or ambiguous query; **not reached** = the segment already had its pages.", ""]
    for seg in research["segments"]:
        rows = []
        for t in seg["topics"]:
            slug = sc.slugify(t["target"]["phrase"])
            entry = log.get(slug)
            if t.get("excluded"):
                status = f"excluded: {t['excluded']}"
            elif entry and entry.get("kept"):
                status = f"[page](../use-cases/{seg['id']}/{slug}.md)"
            elif entry and entry["why"] != "segment target reached":
                status = f"thin ({esc(entry['why'])})"
            else:
                status = "not reached"
            rows.append([esc(t["topic"]), *(f"{esc(p['phrase'])}: {n(p['volume']['in'])} / {n(p['volume']['us'])}" for p in t["phrases"]),
                         n(t["score"]), status])
        out += [f"## {SEGMENTS[seg['id']][0]}", "", f"Phrases: {' and '.join('`' + v + '`' for v in seg['variants'])}. Volumes are India / US monthly searches.", "",
                table(["Topic", "Phrase 1", "Phrase 2", "Score", "Status"], rows, "lllrl"), ""]
    (sc.RESEARCH / "KEYWORD_RESEARCH.md").write_text("\n".join(out))


if __name__ == "__main__":
    main()
