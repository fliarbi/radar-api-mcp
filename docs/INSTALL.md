# Install the Radar API client or your own gateway

Most users install the **client**: the `radar` command for the hosted API at
`https://radar-api.fliarbi.com`. Operators who run their own Radar upstream can install
the **gateway server** instead.

## Client: one line

Requires Bash, curl and Python 3.8+ (standard library only).

```bash
curl -fsSL https://raw.githubusercontent.com/fliarbi/radar-api-mcp/main/scripts/install.sh | bash
```

It installs `radar` to `~/.local/bin`, writes `~/.config/radar/env.sh` with
`RADAR_API_URL=https://radar-api.fliarbi.com` and the command folder, and adds one line that
loads it to `~/.bashrc`, `~/.zshrc` and `~/.profile` (skip with `RADAR_NO_PROFILE=1`). It never
uses sudo or starts a service. Then run `radar login` with a key from the
[key page](https://fliarbi.com/radar-api/developer). See [getting started](GETTING_STARTED.md).

To review the script first: `curl -fsSL https://raw.githubusercontent.com/fliarbi/radar-api-mcp/main/scripts/install.sh -o radar-install.sh && less radar-install.sh && bash radar-install.sh`.

## Gateway server: one line

The server installer prepares a local REST API and stdio/HTTP MCP server on Linux or macOS.
It requires Bash, curl, Python 3.11 or newer, `venv`/pip support and internet access to GitHub
and the Python package index. It uses no `sudo` and does not change your shell profile,
install system packages or start a background service.

```bash
curl -fsSL https://raw.githubusercontent.com/fliarbi/radar-api-mcp/main/scripts/install-server.sh | bash
```

## What setup creates

The default installation directory is `~/.local/share/radar-api-mcp`:

| Path | Purpose |
|---|---|
| `.venv/` | Isolated Python environment with the Radar package and dependencies |
| `bin/radar-api` | REST and HTTP MCP launcher; binds to loopback by default |
| `bin/radar-mcp` | Stdio MCP launcher; reads the local API key at startup |
| `env.sh` | Operator upstream URLs; sourced by both launchers |
| `mcp.json` | Client configuration pointing to the absolute stdio launcher path |
| `secrets/client-key.txt` | Newly generated local API key, file mode `0600` |
| `secrets/keys.json` | Key hash, scopes and rate limit, file mode `0600` |
| `INSTALL_SOURCE` | GitHub archive root identifying the downloaded source revision |

The key uses the existing preview policy: 60 requests per minute and normal data
scopes. Contact reveal requires a separately granted `contacts` scope and a paid
linked Radar account. A generated local key does not grant a Radar subscription,
configure data stores or connect an upstream account.

## Start REST and HTTP MCP

Edit `env.sh` to use the Radar URL supplied by your operator. The default is
`http://127.0.0.1:5100`; optional News URLs start empty. Existing environment values
take precedence over the URL defaults in this file. Then start:

```bash
~/.local/share/radar-api-mcp/bin/radar-api --port 8810
```

The server runs in the foreground. Stop it with Ctrl+C. The local HTTP MCP endpoint
is `http://127.0.0.1:8810/mcp`. API/MCP requests need the generated key as a bearer
token or `X-API-Key`. See [authentication](guides/api-keys-authentication.md) and
[operator setup](OPERATIONS.md) for upstream account linking and optional data
connections. Installation success alone does not establish live data coverage.

## Connect a stdio MCP client

Open the generated `mcp.json` and merge its `radar` server entry into your client's
MCP configuration. It contains the actual absolute launcher path for this install.
The launcher reads the API key from its private file, so there is no API key in the
JSON. The client launches the stdio process; an HTTP server is unnecessary for
that transport. See [MCP integration](guides/company-intelligence-mcp-server.md).

## Options, reruns and troubleshooting

Export options before the one-line command or before `bash radar-install.sh`:

| Variable | Default | Use |
|---|---|---|
| `RADAR_INSTALL_DIR` | `~/.local/share/radar-api-mcp` | Choose a new installation directory; spaces are supported |
| `RADAR_REF` | `main` | Install a branch, tag or full commit SHA |
| `RADAR_PYTHON` | `python3` | Choose an installed Python 3.11+ executable |
| `RADAR_UPSTREAM_URL` | `http://127.0.0.1:5100` | Set the operator's Radar URL |
| `RADAR_NEWS_URL` | Empty | Set the separately operated News API URL |
| `RADAR_BUSINESS_NEWS_URL` | Empty | Set the separately operated business-news URL |

`RADAR_REF` selects the downloaded application archive; the one-line bootstrap
URL above follows `main`. To pin both, replace `main` in that URL with a reviewed
full commit SHA and export the same SHA as `RADAR_REF`. Python dependencies follow
the version ranges in `pyproject.toml`; source pinning does not lock dependencies.

If setup finds an existing destination, it exits before downloading or writing
anything there. It does not rotate keys or perform an in-place upgrade. Choose a
new `RADAR_INSTALL_DIR` to test a newer revision. A failed package installation may
leave a partial directory; inspect it before removing it or choose another path.

For a GitHub 404/403, check repository access, token scope and any organization SSO
requirement. A token-free request will not work until public release is approved.
If `venv` creation fails on Debian/Ubuntu, install the matching `python3-venv`
package through your normal system administration process, then retry with a new
directory. No database credentials are included in the installer or templates.
