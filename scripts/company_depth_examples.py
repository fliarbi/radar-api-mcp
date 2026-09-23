"""Authored company-depth walkthroughs backed by committed response captures."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXAMPLES = [
    ("financial-statements", "Financial data: income, balance sheet and cash flow", "get_financials.json", """
This Microsoft request returns two fiscal periods with income, balance-sheet and
cash-flow observations together. The captured Q3 FY2026 period reports revenue
of USD 82.886 billion, net income of USD 31.778 billion, total assets of USD 694.228
billion and operating cash flow of USD 46.679 billion. Those are values in the
captured API response, not an independent reconciliation with the company's filings.

Each metric retains its source type, unit, normalized currency and available native
value. EPS is a per-share measure; its null normalized currency must not be filled
in from an unrelated USD metric. Both returned periods and all their metrics appear
below. `available_period_count` is 20 and `access_limited` is true, so two delivered
periods are not the whole archive. `period_end` can be null even when filing or
report dates are available.

For a chosen statement family, use `statement=income`, `balance_sheet` or `cash_flow`;
for time selection, use `period_type`, `year_from` and `year_to`. The
[financial filters guide](guides/financial-filters-data-api.md) explains exact
revenue/profit comparisons, including the executed [US AdTech startup query below
$10,000](scenarios/03-usa-adtech-under-10k.md). Missing revenue remains unknown.
"""),
    ("founders-and-background", "Founders data: names, designations and background flags", "fields/razorpay.com-people.json", """
The company `people` field returns Razorpay's recorded key people and founders,
plus background flags such as colleges and prior companies. This capture includes
Shashank Kumar and Harshil Mathur with their recorded designations. Background flags
are company-level source associations; this response does not assign every listed
college or employer to a particular founder.

The same person can occur in both `key_people` and `founders`; those arrays are
views of the source records, not four distinct people. Founder selection is based
on the recorded designation containing “founder”. Keep `updated_at`, the selection
rule and each array's returned/available counts. These are not verified current
employment records, and no email or phone values are embedded in the response.
"""),
    ("founders-only", "A separate founders-only team request", "scenarios/21-razorpay-founders.json", """
When the application needs only founders, request `group=founders` through the team
endpoint. The response returns the two recorded Razorpay founders without the other
company field groups. Choose `key_people` for leadership or `professionals` for
richer professional cards; those choices have different source coverage and filters.

`matched_observed_rows` describes the bounded observed key-person set, not company
headcount. Professional team retrieval requires the `people` scope in addition to
`companies` and checks the exact recorded company domain. See the
[teams and people guide](guides/teams-people-data-api.md) for paging, designation
filters, career seniority and separate contact retrieval.
"""),
    ("apps-summary", "Apps data: company-level totals", "fields/swiggy.com-apps.json", """
This selected company field reports four apps, 382,800,000 aggregate downloads and
a weighted rating for Swiggy. It is an aggregate observation, not a list of app IDs,
monthly active users, company revenue or verified current store statistics.

Use the next request for individual apps. Aggregate values and individual app
observations can have different dates, source coverage and calculation methods;
do not replace an aggregate with a sum of whatever fits on one roster page.
"""),
    ("apps-roster", "Apps data: individual products matched to the company", "company_apps.json", """
The company-app lookup returns four Google Play records whose normalized developer
website host matches `swiggy.com`: the consumer app, partner app, IM Retails Tasks
and Swiggy Pulse. Every returned app includes its ID, developer, store URL,
observation date and available install/rating metrics.

This is an exact website-host association, not a fuzzy name match or proof of
corporate ownership. An app belonging to the business under another developer
website can be missed. Retain numeric zero separately from null: IM Retails Tasks
has a captured rating/count of zero, while Swiggy Pulse has missing rating data.
Use a returned `app_id` for `get_app` or `get_app_field`, not the company's domain.
"""),
    ("app-growth", "App detail: dated install growth and reliability", "get_app_field.json", """
A separate `growth` request for `in.swiggy.android` exposes the measurements behind
the derived figure: 223,179,065 installs observed on June 11, 2025 and 281,013,619
on June 7, 2026, a 360-day interval. The source reports 25.91% observed change and
26.32% annualized change. Annualizing a measured interval is not a prediction.

Keep the `reliable`, `release_date_suspect` and observation fields. Other explicit
app fields expose listing, developer, ratings, monetization, release and install
history. [All seven app-field examples](APP_DATA_DEPTH.md) preserve their structured
output; install history can include duplicate stored observations.
"""),
    ("linkedin-company", "LinkedIn company data: followers, headcount, snapshots and stored posts", "fields/razorpay.com-social.json", """
The selected `social` field combines recorded platform links with LinkedIn profile
observations and stored posts. The refreshed Razorpay capture includes **1,252,056
followers**, **4,052 observed employees**, company size **1,001–5,000**, one profile
snapshot and **eight distinct posts**. Each post retains its URL, text, publication
and observation times, hashtags, media and stored engagement counters.

The profile was observed on **2026-07-02**. Those figures are historical platform
observations, not current audited headcount. `profile_history` holds the available
snapshots; one snapshot cannot establish follower growth. `recent_posts` means the
newest stored posts, not a live feed. Counts use the latest crawl per post, never a
sum across repeated crawls. Source zero engagement values can include parser defaults.

`updated_at` belongs to the company record; LinkedIn records carry their own
`observed_at`. The source labels this profile's sector HRTech, which disagrees with
Razorpay's business classification; the API preserves it as `recorded_sector`.
The compact company endpoint still returns availability without these rich values.
See [the LinkedIn data guide](guides/linkedin-social-data-api.md).
"""),
    ("linkedin-professional", "LinkedIn-associated professional data: education and experience", "search_people.json", """
The named-person search returns one recorded Satya Nadella profile with a LinkedIn
URL, title, company domain, education entries, experience summaries, professional
ranking fields and investor attributes. The displayed record is the captured Radar
response, not a live verification of his current positions.

`skills` is empty in this particular record; it does not establish that the person
has no skills. Education years are empty strings where no year was returned.
Experience entries containing “present” remain source text and may be stale.
`total_estimate=5` is a search estimate, not five returned people or five confirmed
identities. Review identity and affiliation before joining a person to a company.

People cards have bounded source summaries. Use `get_company_team` with
`group=professionals` when exact recorded company-domain affiliation is required;
plain people search supports company-name/domain prefixes. For contact values,
pass an accepted returned person ID to the separately scoped
[person contact endpoint](CONTACTS.md); `contact_gated` does not contain the contacts.
"""),
    ("business-classification", "Business data: sectors, feeds and revenue models", "fields/razorpay.com-classification.json", """
Razorpay's classification field illustrates business-data depth beyond a company
name: FinTech and Enterprise Applications sectors, Payments/Banking Tech/HRTech
markets, primary and other feeds, business models, revenue models, company types
and source classification flags. All captured arrays are retained below.

These are overlapping source taxonomies, not mutually exclusive segments. A
subscription revenue model is not a revenue amount, and “SaaS” or “Startup” flags
do not independently establish a current business status. Stored profile industry
labels can differ from the company-search dropdown vocabulary; use
`company_filter_options` for the exact search field rather than copying an arbitrary
profile label into `filters.industries`. See the [filter audit](FILTER_AUDIT.md).
"""),
    ("technology-stack", "Technology data: website stack and dated observations", "fields/stripe.com-technology.json", """
Stripe's technology field contains 35 merged website-stack entries and 32 dated
observed technologies in this capture. The separate `technographics` array is empty.
That difference is visible in `coverage.arrays` and must not be erased by combining
every source array into an unexplained technology count.

The response preserves the full returned stack, the observation date and update
date. Detected website technologies do not enumerate every internal business
system or establish purchase intent. The [technology and traffic guide](guides/technology-traffic-data-api.md)
explains discovery filters and the distinction between source observations and a
current technical audit.
"""),
    ("website-traffic", "Traffic data: visits, countries, keywords and engagement", "fields/swiggy.com-traffic.json", """
Swiggy's captured traffic field includes 16,549,799 visits dated May 1, 2026, global
and country ranks, keywords, engagement measures and country-level audience shares.
The India share is `0.9678`, a fraction corresponding to 96.78%; it is not 0.9678%.
The bounce value is also returned as a fraction.

These observations describe website traffic, not verified unique customers or app
usage. The five returned audience countries are not proof that the entire audience
is represented. Retain the date and source values; do not present them as today's
traffic or add overlapping website and app figures into one audience number.
"""),
    ("business-events", "Business events: earnings, products, contracts and people changes", "search_business_events.json", """
This historical Microsoft query covers April 2026. It returned five news-derived
event records from an estimated 68, with a `by_type` breakdown spanning earnings,
key people, contracts, company announcements, lawsuits, layoffs, capital infusion,
M&A, a new product and an asset acquisition. The displayed page includes earnings
and product events; the broader breakdown is not the count of rows on that page.

Preserve event IDs, event type, company domain, the company's recorded role and
publication time. Publication time is not necessarily the date the business event
occurred. Multiple articles can describe one event, so five records do not establish
five distinct corporate actions. `resolved=false` means original article URL,
publisher and title were not joined into the event rows. Company associations
remain source-reported. Pass `next_cursor` unchanged while keeping the
same company, date window and other filters.

This successful September 20 capture used the actual News applications and live
queries with isolated test identity/quota dependencies. It is **historical integration
evidence**, not a fresh service-health check or a verified production News connection.
The later [50-scenario audit](SCENARIO_AUDIT.md) encountered an upstream News connection
failure. Several long headlines were omitted from the saved documentation capture;
the linked JSON lists those prose omissions and retains all event rows and fields
that survived that documented projection.
"""),
    ("company-activity", "Company activity events: effective windows and pulse summaries", "get_company_events.json", """
The company event endpoint is distinct from the dated business-news event search.
This captured 30-day Microsoft request has an empty `events` array and
`truncated=true`, while its `pulse` describes a separate 360-day window. The pulse
contains 345 events over that longer window, a derived momentum measure, leadership
signals and top event drivers.

Do not merge those windows or convert the empty 30-day array into “no company
activity”. Source freshness reports the latest event date separately from insertion
time; recently inserted data need not describe a recent event. Scores, badges and
sentinel-looking recency values are source assessments, not verified events or
financial facts. Preserve them for review with their window and access limits.

For financial announcements, follow through to [financial statements](guides/financial-data-api.md)
and [financial news](guides/financial-news-api.md). For reported transactions, use
[funding rounds](guides/startup-funding-data-api.md) and
[funding-news evidence](guides/funding-news-api.md); an announcement is not by itself
proof of a completed transaction.
"""),
]


def render_examples():
    text = """
<!-- company-depth-examples -->
## Worked examples with actual requests and outputs

The examples below reuse the repository's captured responses. They are not new
live calls made when this page is generated. Each block shows its original capture
time, source mode, exact JSON request and complete saved response. Returned business
arrays are not shortened here; the linked capture lists any earlier documentation
prose omissions and its original-response checksum. Source dates and capture dates
are different, and neither establishes that a record is current today.

Send each body to the stated POST route using your API URL and API key. For MCP,
use the named tool with the same body inside `arguments.request`.
[API-key onboarding](guides/api-keys-authentication.md) explains the credentials.

"""
    text += "\n".join(f"- [{title}](#{key})" for key, title, _, _ in EXAMPLES) + "\n"
    for key, title, source, explanation in EXAMPLES:
        record = json.loads((ROOT / "docs/examples" / source).read_text())
        capture = record.get("current", record)
        assert capture["http_status"] == 200, source
        text += f'''
<a id="{key}"></a>

### {title}

**`{record['method']} {record['path']}`** · MCP **`{record['operation']}`** ·
[Endpoint details](reference/{record['operation']}.md) · [Captured JSON](examples/{source}).

{explanation.strip()}

Exact captured request:

<!-- company-depth-request: {source} -->
```json
{json.dumps(record['request'], ensure_ascii=False, indent=2)}
```

Captured **{capture['captured_at']}**, mode **`{capture['capture_kind']}`**,
HTTP **{capture['http_status']}**. Response:

<!-- company-depth-response: {source} -->
```json
{json.dumps(capture['response'], ensure_ascii=False, indent=2)}
```
'''
    return text
