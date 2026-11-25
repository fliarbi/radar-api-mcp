# Install the Companies Radar API client

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
