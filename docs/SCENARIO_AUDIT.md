# Radar API and documentation: 50-scenario feedback audit

The original **50 fixed business questions** ran baseline → repair → re-test, ending
2026-09-23T03:35:37.830082+00:00. Selected documentation samples were subsequently replaced
with smaller companies; each case records its own date and original request.
There are **6 sample replacements**.
See [replacement evidence and blocked sources](EXAMPLE_REPAIRS.md).
This is a semantic/coverage stress test under bounded read
load, **not a production throughput benchmark**. Maximum scenario concurrency was
2; a financial screen separately limits its reads to 3. No production accounts,
source data or source services were mutated.

| Assessment | Original baseline, assessed against its own request | Latest saved sample |
|---|---:|---:|
| observed | 9 | 11 |
| qualified | 27 | 38 |
| failed | 3 | 0 |
| unavailable | 11 | 1 |

HTTP 200 is not the pass criterion: 49 requests returned 200, but coverage,
source staleness, missing periods and access gates remain separately qualified.
Observed elapsed times were p50 0.04s, p95 0.396s and maximum 4.111s;
these include local gateway/source latency and caches and do not establish an SLA.

The baseline unavailable count includes ten missing-operation registry checks and
one actual HTTP 503 News response. Registry checks made no HTTP request; their JSON
records mark the stored 404 as an audit sentinel. The repair round executed all
50 HTTP requests. Baseline outcomes are re-evaluated against their original request
without altering original response payloads. Later sample replacements are not
counted as successful repairs of the original request. The latency distribution
above combines each latest saved sample and is not a new simultaneous load test.

## Feedback that changed the implementation

1. **Wrong industry vocabulary:** AdTech was a valid source dropdown value but the
   gateway queried another industry taxonomy. Suggestions now use the actual Radar
   industry list. The same AdTech request now returns AdTech.
2. **Silent search expansion:** India filters returned US-based sep.com because
   source tier labels were dropped. Structured search now defaults to strict source
   labels, exposes sanitised tier/count metadata, and excludes expanded or unverified
   rows. Explicit expanded mode preserves labels. Stripped filters cannot yield a
   strict shortlist. Tests cover mixed tiers, absent metadata and continued pagination.
3. **No exact revenue workflow:** added the financial filter catalogue and a bounded
   dated-metric screen with inclusive/exclusive bounds, source qualification, consistent
   fiscal periods, unknown/error separation, fan-out limits and settled credit refunds.
4. **No separate team workflow:** added founders, key people and professional groups,
   exact-domain affiliation checks, group-specific filters and separate contact access.
   Incorrect 500-record team retrieval was caught locally and corrected to the existing
   100-record source field limit; professional search pages are independent.
5. **Documentation could not answer concrete questions:** added dedicated financial,
   team and technology/traffic guides plus 50 request/output pages. Guide requests are
   validated against live code models; every scenario is linked from its workflow guide.
   The documentation checker validates request identity, output hashes, full retained
   arrays, source projections and displayed response equality.

## Findings that remain open or qualified

- Under-$10,000 US AdTech startup screening found three unknown annual observations,
  not three qualifying companies. It is not a global exhaustive financial index.
- The positive AdTech screen uses reported annual revenue; its two matches are labelled
  news_report. A filing-only screen may yield different results.
- The replacement electroCore income example has populated annual metrics. Its balance
  sheet and cash-flow examples remain blocked: strict financial-store reads failed
  on an unreachable shard on 2026-09-24. Neither a fiscal label nor HTTP 200 means
  the requested statement metrics are present. Source entitlements remain enforced.
- People records include retired-role and inconsistent-date evidence. Team affiliation
  means the recorded domain, not verified current employment or employee headcount.
- App history has duplicate stored observations. Internship listings include expired
  deadlines and unresolved employer domains. Investor research retains its dated cutoff.
- News was unconnected in the baseline (503). The isolated live-data query integration
  reached an upstream connection failure (502) in this run. Older successful examples
  remain historical evidence; this run does not claim current News availability.

## Reproduce and inspect

[All 50 request/output pages](scenarios/README.md) and the
[machine-readable audit](SCENARIO_AUDIT.json) retain original and replacement requests.
`scripts/scenario_cases.py` defines the current matrix. `scripts/stress_scenarios.py`
executes authenticated, bounded read requests in an operator-configured environment.
`scripts/build_scenario_docs.py` renders the captured baseline and repair evidence;
`scripts/check_docs.py` verifies the checked-in result without requiring live data.
Private runtime configuration and raw capture files are not published with these docs.

The suite checks response envelopes, selected-field identity, country/founded-year
predicates visible in company cards, exact financial constraints, fiscal-period
bounds, exact team affiliation, app rating/install/category/domain predicates and
internship work-mode/stipend assertions. Other classifications remain source predicates;
we do not claim independent validation where returned cards lack supporting fields.
