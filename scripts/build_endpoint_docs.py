#!/usr/bin/env python3
"""Render reviewed live/local captures; never manufacture a successful response.

Run capture scripts first. Raw data stays ignored. Published projections remove
fields/array tails only and preserve every retained value, type and array order.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from endpoint_notes import ACCOUNT_NOTES, NOTES
from guide_expansions import GUIDES
from radar_api.service import BY_NAME, FEATURES

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "docs/examples"
REFERENCE = ROOT / "docs/reference"
OMIT_KEYS = {"headline", "biography", "bio", "snippets", "gender", "input_schema",
             "body", "lede", "full_text", "meta_description", "source_sentence"}


def encoded(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def project(value, path="", omissions=None, preserve_titles=False):
    """Preserve field depth and every array row; omit only identified source prose."""
    omissions = omissions if omissions is not None else []
    if isinstance(value, dict):
        out = {}
        for key, child in value.items():
            at = f"{path}/{key}"
            short_title = key == "headline" and (isinstance(child, (dict, list)) or
                          preserve_titles and isinstance(child, str) and len(child.split()) <= 25)
            if key in OMIT_KEYS and not short_title:
                omissions.append(at)
            else:
                out[key] = project(child, at, omissions, preserve_titles)
        return out
    if isinstance(value, list):
        return [project(child, f"{path}/{i}", omissions, preserve_titles) for i, child in enumerate(value)]
    return value


def select(data, keys, path, omissions):
    for key in list(data):
        if key not in keys:
            omissions.append(f"{path}/{key}")
            del data[key]


def excerpt(name, response):
    omissions = []
    # Envelope metadata is complete, including notes and partial flags.
    out = copy.deepcopy(response)
    if name == "openapi":
        select(out, {"openapi", "info", "paths"}, "", omissions)
        select(out["paths"], {"/healthz"}, "/paths", omissions)
        return out, omissions
    if "data" not in out:
        return out, omissions
    news = name in BY_NAME and (BY_NAME[name].source != "radar" or name == "company_brief")
    data = out["data"] = project(out["data"], "/data", omissions, preserve_titles=news)
    if not isinstance(data, dict):
        return out, omissions
    if name in {"search_jobs", "get_job"}:
        jobs = [(f"/data/jobs/{i}", row) for i, row in enumerate(data.get("jobs", []))]
        if isinstance(data.get("job"), dict):
            jobs.append(("/data/job", data["job"]))
        for path, job in jobs:
            for key in ("description", "description_snippet", "snippet"):
                if key in job:
                    omissions.append(path + "/" + key)
                    del job[key]
    if name == "search_people":
        for i, person in enumerate(data.get("people", [])):
            select(person, {"id", "name", "current_title", "current_company", "current_company_domain",
                            "location", "people_types"}, f"/data/people/{i}", omissions)
    return out, sorted(set(omissions))


def schema_type(prop):
    if "$ref" in prop:
        return prop["$ref"].split("/")[-1]
    if "anyOf" in prop:
        return " or ".join(schema_type(p) for p in prop["anyOf"])
    if prop.get("type") == "array":
        return "array of " + schema_type(prop.get("items", {}))
    return prop.get("type", "object")


def parameter_table(schema):
    rows = ["| Parameter | Required / default | Type and accepted values |", "|---|---|---|"]
    for key, prop in schema.get("properties", {}).items():
        default = "required" if key in schema.get("required", []) else (
            "default `" + json.dumps(prop["default"]) + "`" if "default" in prop else "optional; empty by default")
        constraints = []
        for branch in [prop, *prop.get("anyOf", []), prop.get("items", {})]:
            if "enum" in branch:
                constraints.append("one of " + ", ".join(f"`{x}`" for x in branch["enum"]))
            for field, label in [("minimum", "minimum"), ("maximum", "maximum"), ("minLength", "min characters"),
                                 ("maxLength", "max characters"), ("minItems", "min items"), ("maxItems", "max items"), ("pattern", "pattern")]:
                if field in branch:
                    constraints.append(f"{label}: `{branch[field]}`")
        detail = schema_type(prop) + ("; " + "; ".join(constraints) if constraints else "")
        rows.append(f"| `{key}` | {default} | {detail.replace('|', '&#124;')} |")
    return "\n".join(rows) if len(rows) > 2 else "This operation accepts an empty JSON object: `{}`."


def curl(record, token="RADAR_API_KEY"):
    method, path, body = record["method"], record["path"], record.get("request")
    lines = [f'curl --fail-with-body -X {method} "$RADAR_API_URL{path}"']
    if token:
        lines.append(f'  -H "Authorization: Bearer ${token}"')
    if method in {"POST", "PUT"}:
        lines += ["  -H 'Content-Type: application/json'", "  -d '" + json.dumps(body or {}, separators=(",", ":")) + "'"]
    return " \\\n".join(lines)


def response_block(name, record):
    label = "complete response" if not record["omitted_paths"] else "response excerpt"
    provenance = ("\n\n**Capture method:** " + record["provenance"]) if record["capture_kind"] == "live_data_integration" else ""
    return f"""<!-- response-example: {name} -->
```json
{encoded(record['response']).rstrip()}
```

This is the captured **{label}**, HTTP **{record['http_status']}**, from
**{record['captured_at']}**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/{name}.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.{provenance}
"""


def data_page(feature, record):
    note = NOTES[feature.name]
    scope = feature.path.split("/")[0]
    price = "six credits without News, seven with News; failed sections are refunded" if feature.name == "company_brief" else (
        "three credits per company; failed sections are refunded" if feature.name == "compare_companies" else "one credit for a successful operation")
    schema = feature.model.model_json_schema()
    params = parameter_table(schema)
    if "CompanyFilters" in schema.get("$defs", {}):
        params += "\n\n### Fields inside `filters`\n\n" + parameter_table(schema["$defs"]["CompanyFilters"])
    fields = "\n".join(f"| `{key}` | {meaning} |" for key, meaning in note["fields"].items())
    return f"""# {note['title']}

[All endpoints](README.md) · [Workflow guide](../guides/{note['guide']}.md)

{note['purpose']}

## Route, authentication and credits

**`POST /v1/{feature.path}`** · MCP tool **`{feature.name}`** · key scope **`{scope}`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs {price}. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

{params}

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
{curl(record)}
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: {feature.name} -->
```json
{encoded({'name': feature.name, 'arguments': {'request': record['request']}}).rstrip()}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

{response_block(feature.name, record)}
{note['observed']}

## Read the response

| Field | Meaning and handling |
|---|---|
{fields}

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

{note['workflow']}

{note['pitfall']}

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/{note['guide']}.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
"""


def account_page(name, record, openapi):
    title, purpose, interpretation = ACCOUNT_NOTES[name]
    path = record["path"]
    template = "/account/keys/{key_id}" if name == "account_revoke_key" else (
        "/account/following/{domain}" if name == "account_unfollow" else path)
    operation = openapi["paths"].get(template, {}).get(record["method"].lower(), {})
    schema = operation.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema", {})
    if "$ref" in schema:
        schema = openapi["components"]["schemas"][schema["$ref"].split("/")[-1]]
    params = parameter_table(schema) if record["method"] in {"POST", "PUT"} else "This request has no JSON body."
    for param in operation.get("parameters", []):
        params += f"\n\nPath parameter `{param['name']}`: {schema_type(param['schema'])}; use an identifier returned for your own account."
    token = "RADAR_SESSION_TOKEN" if path.startswith("/account/") else (None if name == "health" else "RADAR_API_KEY")
    auth = "No credential is required; this only reports process liveness." if name == "health" else (
        "Use your existing Radar session in `Authorization: Bearer`. Every request verifies the live identity and current entitlements." if path.startswith("/account/") else
        "Use a data API key in `Authorization: Bearer`. Discovery does not reserve data-operation credits.")
    command = curl(record, token)
    if name == "billing_webhook":
        auth = "Provider-only callback. Verify `X-Razorpay-Signature` against the original raw body with the configured webhook secret. This route does not accept a user API key as payment proof."
        params = "The body is a Razorpay event envelope. Its signature must match the exact bytes; reformatting signed JSON invalidates it. The stored order determines the expected account, credits, amount and currency."
        command = 'curl --fail-with-body "$RADAR_API_URL/billing/webhook" \\\n  -H "X-Razorpay-Signature: $RAZORPAY_SIGNATURE" \\\n  -H \'Content-Type: application/json\' \\\n  --data-binary @captured-event.json'
    return f"""# {title}

[All endpoints](README.md) · [Account guide](../ACCOUNTS.md)

{purpose}

## Method and authentication

**`{record['method']} {template}`**

{auth} Account operations are HTTP-only and are not MCP retrieval tools.
Management requests share account request-rate limits but do not consume a data
operation credit. The billing callback uses provider-event verification instead.

## Request

{params}

```bash
{command}
```

Set the private base URL without a trailing slash. Example IDs identify the
temporary documentation account; use your own returned identifiers when integrating.
Do not paste the redacted credential placeholders into a running application.

## Executed local output

**Provenance: real gateway code and a temporary SQLite account store, with a
synthetic verified Radar identity and synthetic Razorpay provider responses.**
No live user was created, payment collected or production account changed.
The synthetic Business plan and ten-paise credit price exercise the flow;
they do not announce an enabled checkout or an approved pay-per-use tariff.

{response_block(name, record)}
## What this response means

{interpretation}

The capture sequence connected a session, inspected plans, created and listed a
key, linked a placeholder News key, followed one domain, set a spending limit,
created a synthetic order, delivered its signed captured event, inspected usage,
then unfollowed the domain and revoked the key. Responses reflect that order.

Handle `401` by reconnecting an authorized session, `403` by checking plan/access,
and `429` with backoff and the supplied retry interval. Do not automate repeating
checkout requests after an ambiguous network failure: first inspect the provider
order and reconcile its captured status. Key creation reveals a credential once;
key listing is metadata-only. See the [account controls](../ACCOUNTS.md) for
creation caps, shared limits, spending reservations and payment reversal behavior.

Related: [API-key onboarding](../guides/api-keys-authentication.md),
[plans and pay-per-use](../guides/pricing-pay-per-use.md),
[full account schema](../account-openapi.json).
"""


def main():
    EXAMPLES.mkdir(parents=True, exist_ok=True)
    REFERENCE.mkdir(parents=True, exist_ok=True)
    live = json.loads((ROOT / "qa/private/endpoint-live.json").read_text())
    account = json.loads((ROOT / "qa/private/endpoint-accounts.json").read_text())
    openapi = json.loads((ROOT / "docs/account-openapi.json").read_text())
    manifest = []
    for source, kind in ((live, "live_gateway"), (account, "local_account_fixture")):
        for name, raw in source["operations"].items():
            response, omitted = excerpt(name, raw["response"])
            record = {"operation": name, "capture_kind": raw.get("capture_kind", kind), "captured_at": raw.get("captured_at", source["captured_at"]),
                      "provenance": raw["provenance"], "method": raw["method"], "path": raw["path"],
                      "request": raw.get("request"), "http_status": raw["http_status"],
                      "response": response, "omitted_paths": omitted,
                      "credential_redactions": ["/response/data/api_key"] if name == "account_create_key" else [],
                      "hash_basis": "Parsed JSON with sorted keys, after any credential redaction",
                      "original_response_sha256": digest(raw["response"]),
                      "response_excerpt_sha256": digest(response)}
            (EXAMPLES / f"{name}.json").write_text(encoded(record))
            page = data_page(BY_NAME[name], record) if name in BY_NAME else account_page(name, record, openapi)
            (REFERENCE / f"{name}.md").write_text(page)
            manifest.append({k: v for k, v in record.items() if k not in {"response", "omitted_paths"}})
    (EXAMPLES / "index.json").write_text(encoded(manifest))
    data_records = [r for r in manifest if r["operation"] in BY_NAME]
    success_count = sum(r["http_status"] == 200 for r in data_records)
    failed = ", ".join(f"{r['operation']} HTTP {r['http_status']}" for r in data_records if r["http_status"] >= 400) or "none"
    capture_dates = sorted(r["captured_at"][:10] for r in data_records)
    header = f"""# Radar API endpoint reference with captured request and response examples

Every JSON HTTP operation has a request, actual response, field explanation and
integration guidance below. The thirty data operations also show their equivalent
MCP tool call. These examples document observed output, including genuine empty,
partial and failed responses; they are not fabricated success fixtures.

## Capture provenance and limits

The 30 data-operation captures span **{capture_dates[0]} to {capture_dates[-1]}**
through the local authenticated gateway. The original eight News captures returned
503 because their service URLs were unset. They have now been replaced by
successful requests through the actual News applications with live archive data,
using isolated test identity and quota dependencies. These are labeled
`live_data_integration`; they do not verify a deployed News URL or production key.
The current set has **{success_count} HTTP 200 responses**. Remaining failed
primary examples: **{failed}**. A twenty-second timeout bounded the original
HTTP upstream captures. The Stripe brief also combines live Radar sections with
a successful News section under the documented News integration identity.
The preview key had no linked Radar session, so the live source applied anonymous
free-tier access. This is neither a Business-tier coverage audit nor a public
deployment test. Some HTTP 200 responses were partial, empty or source-inconsistent.

The 16 account/discovery examples executed actual local gateway code with synthetic
identity and payment providers. They are explicitly labeled; no live purchase or
production account mutation occurred. `/healthz` reports liveness only. Static
browser routes and the MCP handshake are covered in [transports](transports.md).

Outputs now preserve **all captured array rows and business-data sections**;
the documentation no longer cuts arrays to two items or removes profile fields.
The [company depth walkthrough](../COMPANY_DATA_DEPTH.md) shows populated sectors,
feeds, founders, technology, traffic, apps, hiring, products and innovation.
Each [downloadable example](../examples/index.json) lists any remaining prose
omissions, capture provenance and checksums. News examples retain short headlines,
source URLs, dates, classifications and measured values. Article bodies, ledes,
long source quotations, review snippets and biographies are omitted from
documentation reproduction, with every omitted path recorded. Credentials are
explicitly redacted before a response is stored or hashed; checksums use parsed,
sorted JSON and do not represent HTTP wire bytes.
Read the [measured data-quality notes](../DATA_QUALITY.md) before treating the
sample corporate records as independently verified facts.
The [complete example audit](../EXAMPLE_AUDIT.md) also identifies empty, partial,
restricted and fixture-backed HTTP 200 responses.

## Data operations: REST and MCP

| Endpoint / tool reference | HTTP route | Captured status |
|---|---|---|
"""
    for record in manifest:
        name = record["operation"]
        if name in BY_NAME:
            header += f"| [{name}]({name}.md) | `{record['method']} {record['path']}` | {record['http_status']} |\n"
    header += "\n## Accounts, billing and discovery\n\n| Endpoint reference | HTTP route | Local status |\n|---|---|---|\n"
    for record in manifest:
        name = record["operation"]
        if name not in BY_NAME:
            header += f"| [{ACCOUNT_NOTES[name][0]}]({name}.md) | `{record['method']} {record['path']}` | {record['http_status']} |\n"
    header += "\nReturn to [developer documentation](../README.md) or [workflow guides](../README.md#company-discovery-and-business-data).\n"
    (REFERENCE / "README.md").write_text(header)
    for slug, (name, heading, prose) in GUIDES.items():
        path = ROOT / "docs/guides" / (slug + ".md")
        base = path.read_text().split("<!-- captured-workflow -->")[0].rstrip()
        record = json.loads((EXAMPLES / f"{name}.json").read_text())
        observed = NOTES[name]["observed"] if name in NOTES else ACCOUNT_NOTES[name][2]
        label = ("live data with an isolated News integration identity" if record["capture_kind"] == "live_data_integration" else
                 "live gateway response" if name in NOTES else "executed local account response with synthetic providers")
        section = f"""

<!-- captured-workflow -->
## {heading}

{prose.strip()}

## Worked example: {label}

The request captured for this example was **`{record['method']} {record['path']}`**.
It is separate from any broader filter variants shown earlier in this guide.

<!-- captured-request: {name} -->
```json
{encoded(record['request']).rstrip()}
```

{response_block(name, record)}
{observed}

See the [complete {name} endpoint reference](../reference/{name}.md) for the
parameter table, equivalent command, response fields, access behavior and next steps.
Browse [all 46 JSON endpoint examples](../reference/README.md) for the remaining
company, financial, funding, news, investor, hiring and account operations.
"""
        if record["request"] is None:
            section = section.replace(f"<!-- captured-request: {name} -->\n```json\nnull\n```", "This GET request has no JSON body.")
        path.write_text(base + section)
    build_transports()
    from build_profile_depth_docs import build
    build()
    from audit_examples import build as build_audit
    build_audit()
    assert set(NOTES) == {f.name for f in FEATURES}
    print(f"Rendered {len(manifest)} endpoint references and captured JSON examples")


def build_transports():
    raw = json.loads((ROOT / "qa/private/endpoint-transports.json").read_text())
    envelope, omissions = excerpt("get_company", raw["result"]["structuredContent"])
    published = {k: v for k, v in raw.items() if k != "result"}
    published["result"] = {"structuredContent": envelope, "isError": raw["result"]["isError"]}
    published["omitted_paths"] = ["/result/content", *["/result/structuredContent" + p for p in omissions]]
    published["original_result_sha256"] = digest(raw["result"])
    (EXAMPLES / "transports.json").write_text(encoded(published))
    rows = "\n".join(f"| `GET {r['path']}` | {r['status']} | `{r['content_type']}` | `{r['cache_control']}` |" for r in raw["browser_routes"])
    text = f'''# MCP HTTP transport and browser endpoint examples

[All JSON endpoints](README.md) · [MCP workflow](../guides/company-intelligence-mcp-server.md)

The thirty data tools use the same typed requests and response envelopes as REST.
An MCP client initializes a connection, discovers tools, and calls a tool using
its `name` and an `arguments.request` object. Account mutations remain HTTP-only.

## Captured HTTP MCP initialization

A real MCP SDK client connected to `/mcp` on a temporary loopback gateway on
**{raw['captured_at']}**, using an existing preview key. It listed all thirty
tools and called `get_company` against the configured live Radar service. This
does not claim that a public MCP endpoint has been deployed.

```json
{encoded(raw['initialize']).rstrip()}
```

`protocolVersion` is the negotiated MCP protocol version. `serverInfo.version`
here is the MCP library's reported version, while `/healthz` reports the Radar
package version. Do not conflate those values. Read-only annotations describe
tool intent; account-mode successful calls still consume credits.

## Connect and call with Python

Install this repository's pinned dependencies, set the operator-supplied
`RADAR_API_URL` and load `RADAR_API_KEY` from your secret store. This uses the
tested `mcp` client API rather than manually guessing handshake headers.

```python
import asyncio
import os
import httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

async def main():
    headers = {{"Authorization": "Bearer " + os.environ["RADAR_API_KEY"]}}
    url = os.environ["RADAR_API_URL"].rstrip("/") + "/mcp"
    async with httpx.AsyncClient(headers=headers) as client:
        async with streamable_http_client(url, http_client=client) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                catalog = await session.list_tools()
                print([tool.name for tool in catalog.tools])
                result = await session.call_tool(
                    "get_company", {{"request": {{"domain": "razorpay.com"}}}}
                )
                print(result.isError, result.structuredContent)

asyncio.run(main())
```

Actual returned `CallToolResult` excerpt:

```json
{encoded(published['result']).rstrip()}
```

The duplicated text-content block and review snippets are omitted from this
excerpt; `structuredContent` retains the captured company data and array rows.
The response now includes Razorpay's sectors, feeds, founders, technologies,
traffic, apps and other available sections. Review the
[company field guide](../COMPANY_DATA_DEPTH.md). For a failed tool call, inspect `isError`
and the structured `error` instead of assuming HTTP transport success means data
success. The complete tool-name list, initialization, omission paths and checksum
are in [the downloadable transport capture](../examples/transports.json).

The server uses stateless Streamable HTTP with JSON responses. The SDK owns
initialization and protocol headers; `/mcp` is not another `POST /v1/...` JSON
route. Stdio mode uses `radar-mcp` with the same key and gateway configuration;
its environment belongs to the local operator, not to a remote caller. See the
[user guide](../USER_GUIDE.md) for stdio configuration.

## Browser pages and assets

These routes return HTML, JavaScript or CSS, so a JSON response example would be
misleading. Their actual observed responses are listed below. `/docs` was fetched
from the authenticated preview gateway. The developer console and its assets were
fetched from a temporary local account-mode app, without contacting a live
identity or payment provider.

| Route | HTTP | Content-Type | Cache-Control |
|---|---|---|---|
{rows}

`null` means no Cache-Control header was returned. The console shell and assets
can load before login; account data operations still validate the Radar session.
The console route exists only with account mode enabled. `/docs` is the interactive
OpenAPI UI, while `/v1/openapi.json` returns the contract itself. No generic data
record is returned by these browser assets.

The capture contains the first 120 response characters for each asset, making
the content type reviewable without duplicating bundled application source.
See [account onboarding](../guides/api-keys-authentication.md) and
[OpenAPI discovery](openapi.md) for the next step.
'''
    (REFERENCE / "transports.md").write_text(text)


if __name__ == "__main__":
    main()
