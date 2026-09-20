# Private preview operations

## Release boundary

Keep the GitHub repository private. Public repository visibility, public API
deployment, package publication, billing integration and release announcements
require the owner's separate approval. The included CI only tests and builds.

This package is a standalone gateway to existing Radar and Prism HTTP contracts.
It does not import the production Flask app, connect directly to data stores, copy
existing credentials or alter running production services. Optional account-mode
HTTP routes are documented in [ACCOUNTS.md](ACCOUNTS.md), separately from read-only
MCP retrieval. Upstream searches may update normal quota counters,
telemetry or caches, just as the existing Radar interface does.

## Configure upstream services

Copy settings from `.env.example` into your service manager's environment. Values
are not automatically loaded from `.env`. For shell use, explicitly source a
trusted configuration file with exported variables. Leave unused News URLs blank.

Each base URL is supplied by the operator. Caller-provided URLs, arbitrary paths,
database queries and legacy dispatch keys are never accepted. HTTP redirects are
not followed, to avoid forwarding credentials to another host. Requests use bounded
timeouts and response sizes. Connections use TLS verification for HTTPS.

News requires both a connected service and a linked News API key. Both general
and business News hosts use the linked News key, preserving existing quotas and
entitlements. This preview does not start those services or issue a News account.

## Issue and revoke preview keys

For a caller who already has an authorized Radar session and/or News API key, set
the following variables privately in your shell or secret manager:

```text
RADAR_ACCOUNT_TOKEN=<that caller's Radar session>
RADAR_ACCOUNT_NEWS_KEY=<that caller's News API key>
```

Then run:

```bash
radar-create-key --name analyst-one --key-output secrets/analyst-one.key
```

The command reads these values at runtime, saves the Radar/News links in the
owner-only key store, saves the new client key in an owner-only file, and prints
only file paths. The gateway stores the preview key's SHA-256 hash. Do not use one
operator's privileged upstream session as a default for unrelated customers.

The store has the following shape; this is illustrative, not a working credential:

```json
{
  "keys": [{
    "name": "analyst-one",
    "sha256": "SHA256_OF_ISSUED_PREVIEW_KEY",
    "active": true,
    "expires_at": "2026-12-31T23:59:59Z",
    "rate_per_minute": 60,
    "radar_token": "CALLER_RADAR_SESSION_OR_EMPTY",
    "news_key": "CALLER_NEWS_KEY_OR_EMPTY"
  }]
}
```

Change `active` to false or remove a record to revoke it. Changes are read on the
next request. Expiry requires a timezone. Invalid or expired upstream sessions
remain subject to the upstream service's rules; Radar can fall back to anonymous
coverage, so clients must inspect returned access limits. No local token forge or
session upgrade is performed.

The store must be owned by the process user and have no group/other permissions
(mode `0600`). Keep its directory `0700`. Both `secrets/` and `.env` are ignored by
Git. Upstream links are secrets too; protect backups accordingly.

## Run and connect

`radar-api --host 127.0.0.1 --port 8810` serves REST and `/mcp` in one process.
Stdio uses `radar-mcp` with `RADAR_API_KEY` and the same configuration.
Use absolute paths for the stdio command and key store because client working
directories differ.

In default local-preview mode, all HTTP routes except `/healthz`, including docs,
OpenAPI and MCP, require a key. Account mode additionally serves an unauthenticated
console shell; account routes require a Radar session and the payment webhook requires
its signature. No account data is embedded in the console shell.
An unauthorized request never reaches the data services. Host checks and origin
checks apply to MCP and REST. If using an approved private reverse proxy, list its
exact hostname in `RADAR_ALLOWED_HOSTS` and exact origin in `RADAR_ALLOWED_ORIGINS`.
Do not use wildcard hosts. Terminate HTTPS at the proxy and keep the service
bound to loopback. Access logging is disabled by the CLI; never log request headers,
key-file contents or upstream error bodies.

The default JSON-key limiter is process-local: use **one worker** in that mode.
Account mode uses a persistent ledger and limiter shared by workers on one host;
see [its deployment limits](ACCOUNTS.md). Multiple hosts need a shared transactional
store before rollout. Upstream account
quotas still apply. Body size is capped at 256 KiB; response size defaults to 8 MiB.
Long upstream searches can time out and are surfaced as 504, without silent fallback.

There is no OAuth authorization server. Clients must support stdio or bearer/API-key
authentication for Streamable HTTP. Browser Swagger docs require the authentication
header on the initial page request as well as data calls; an API client or the
downloaded OpenAPI schema is often simpler for a private preview.

## Verification

`pytest` runs isolated synthetic tests; no production credentials or network data
services are required. `python scripts/live_smoke.py` performs bounded live reads
against the configured upstreams, writes counts/status only, and requires a local
preview key. It never saves full financial/news payloads or credentials.

Live checks and mocked contract checks are separate evidence. No success in CI
proves that a particular account has a plan, that the News services are listening,
or that the GitHub repository is public or private. Verify each independently.

After GitHub authentication, use `scripts/publish_private.sh fliarbi/radar-api-mcp`
to create/push the repository. The script refuses to push to an existing public
repository and checks visibility again after the push. It never changes visibility.

## Detailed company profile connection

Set `RADAR_PROFILE_MONGO_URI` in the operator's private environment to connect the
existing Radar company store. Use a credential restricted to read access on
`companies_data.main_data`, `company_pubmap` and `company_enrichment`. The public
request accepts only a validated domain, an optional public company identifier,
named sections and a bounded array limit. It never accepts a database URI, query,
projection, collection or table name.

The reader uses indexed domain/ID equality lookups, takes at most two candidate
records, and rejects ambiguous domains with 409. A public ID is resolved through
the public-ID mapping and matched together with the domain. Driver timeouts are
bounded; raw driver diagnostics and connection details never enter the response.
No collection writes, index changes, refresh jobs or production service restarts
are part of this connection.

Search continues through Radar's existing ClickHouse-backed routes. Detailed profile
fields come from the grouped Mongo company record, while traffic, hiring, patent,
social and reputation observations come from its precomputed enrichment. The
reader intentionally fetches only employee count from the financial block;
financial statement history and estimated-revenue entitlement checks stay on the
existing upstream financial path. Account authentication, company scope, metering
and rate/concurrency limits apply to the new reader like other data operations.

Without this connection, profile responses explicitly say `profile_depth=card`.
If a configured store fails, the result is 503; there is no silent downgrade to a
potentially different entity. Optional enrichment failure preserves the base
profile with partial section coverage. The [field-depth guide](COMPANY_DATA_DEPTH.md)
documents the public sections and their measured examples.

Refresh depth examples by capturing authorized `/v1/companies/profile` requests
for the reviewed domains into ignored `qa/private/profile-<domain>.json` files.
Run `scripts/build_profile_depth_docs.py`, `scripts/export_contract.py`, then
`scripts/build_endpoint_docs.py` and `scripts/check_docs.py`. The first builder also
updates the bundled, sanitized Swagger example. Never copy raw database records
or credentials into the example files.

## News connections and reproducible examples

Ordinary News calls need `RADAR_NEWS_URL`, `RADAR_BUSINESS_NEWS_URL` and a linked
News key. An unset URL produces `503 service_unavailable` before any upstream
query; setting only a key does not establish connectivity. With accounts enabled,
link the key through `/account/news-key`; preview JSON key records use `news_key`.
Keep the service URLs and credentials in the private runtime environment.

To verify available data without deploying the services or charging a customer,
run `.venv/bin/python scripts/capture_news_examples.py`. It loads the sibling
`prism-news-api` and `prism-business-news-api` source trees, overrides only their
identity/quota dependencies in isolated application instances, and executes actual
data queries through the Radar gateway. Coverage and data-plan limits stay active.
Use `--news-source` and `--business-source` for other private checkout locations.
The output is ignored, owner-only `qa/private/endpoint-live.json`; review it, then
run the documentation builder and validator. This capture method is explicitly
labeled `live_data_integration` and must not be relabeled as production-key or
deployed-service verification. The test override is confined to this script;
the installed API and MCP authentication paths are unchanged.
