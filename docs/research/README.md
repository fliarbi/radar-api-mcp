# Radar API research: evidence, findings and capability gaps

Use this directory to trace a documentation or product claim back to its evidence.
Research includes source-code analysis, actual data captures, local contract
fixtures and search-intent research. Those evidence types answer different questions.

| Investigation | Evidence and reader-facing findings | What it establishes |
|---|---|---|
| Empty examples and smaller-company samples, September 24 | [Diagnosis and complete replacements](../EXAMPLE_REPAIRS.md), [every saved response](../EXAMPLE_AUDIT.md) | Populated income, profit screening, jobs, products and activity; blocked balance-sheet/cash-flow reads; preserved original requests and intentional empty cases |
| Contact, founder identity and social-link workflows | [Source findings](CONTACT_WORKFLOW_FINDINGS.md), [evidence manifest](contact-workflow-evidence.json), [contact guide](../CONTACTS.md) | Accepted variables, source fallback behavior, live identity-linkage discrepancies, synthetic output/gate cases and unsupported filters |
| LinkedIn depth correction | [Root cause and source mapping](LINKEDIN_SOCIAL_FINDINGS.md), [live evidence](linkedin-social-evidence.json), [reader guide](../guides/linkedin-social-data-api.md) | Raw profile/post coverage independent of missing derived enrichment; dated followers, headcount, stored posts and explicit partial states |
| Company filters | [All 43 source mappings](../FILTER_AUDIT.md), [structured inventory](../FILTER_AUDIT.json) | Source handler semantics, boundaries, strict/expanded matching and explicit unverified paths |
| Fifty business scenarios | [Feedback audit](../SCENARIO_AUDIT.md), [machine-readable results](../SCENARIO_AUDIT.json), [all requests/outputs](../scenarios/README.md) | Baseline failures, repairs and bounded observed/qualified/unavailable outcomes |
| Company field depth | [Worked examples](../COMPANY_DATA_DEPTH.md), [depth audit](../DATA_DEPTH_AUDIT.md) | Retained business structures, complete saved response arrays and separate selected-field requests |
| Investor, app and opportunity research | [Investor depth](../INVESTOR_DATA_DEPTH.md), [app depth](../APP_DATA_DEPTH.md), [opportunity examples](../POTENTIAL_DATA_EXAMPLES.md) | Snapshot periods, denominators, derived observations and limitations |
| Google/Bing search intent, September 20 | [Original 15-query JSON](2026-09-20-search.json), [readable search research](../SEARCH_RESEARCH.md) | Query outcomes and reader intent; not keyword volumes or ranking predictions |
| Operational and delivery verification | [Verification record](../VERIFICATION.md), [example audit](../EXAMPLE_AUDIT.md) | Distinguishes local checks, live source reads, fixtures and deployment claims |

## Reading evidence correctly

The [all-endpoint output audit](../OUTPUT_DEPTH_AUDIT.md) and
[machine-readable review](endpoint-output-audit.json) cover all 53 data operations
and 16 account/discovery operations, including fresh failures, endpoint ownership,
before/after output shapes and hashes of reviewed adapters. Read this alongside
historical examples when judging current service availability.

- **Source review** describes the implementation inspected at the recorded date;
  it does not verify every source record or every filter combination.
- **Live gateway capture** records a real configured data read, with its timestamp,
  request, status and coverage. A successful request is not independent source-truth
  or identity verification.
- **Local contact/account fixture** exercises real gateway code against explicit
  synthetic upstream values. It demonstrates contract behavior, not production
  entitlement, a real contact address or a completed payment.
- **Schema-validated recipe** demonstrates accepted request syntax. It does not
  claim a live execution, nonempty result or a correct real-world identity join.
- **Search evidence** retains engine, route, query and outcome. News search,
  general web search and CAPTCHA-blocked attempts are distinguished.

The existing search JSON is preserved unchanged. Source configuration, credentials,
raw operator logs and private runtime files remain outside this evidence directory.
The repository remains private until the owner approves public release.
