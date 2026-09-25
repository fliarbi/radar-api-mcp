#!/usr/bin/env python3
"""Write local launchers after installation, keeping the API key in its private file."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shlex
import sys

from radar_api.config import _base


def configure(root: Path) -> None:
    root = root.resolve()
    settings = {
        "RADAR_UPSTREAM_URL": os.getenv("RADAR_UPSTREAM_URL", "http://127.0.0.1:5100"),
        "RADAR_NEWS_URL": os.getenv("RADAR_NEWS_URL", ""),
        "RADAR_BUSINESS_NEWS_URL": os.getenv("RADAR_BUSINESS_NEWS_URL", ""),
    }
    lines = ["# Local operator settings. This file is sourced by the launchers."]
    for name, value in settings.items():
        value = _base(value)
        lines.append(f'if [ -z "${{{name}:-}}" ]; then export {name}={shlex.quote(value)}; fi')
    files = {root / "env.sh": ("\n".join(lines) + "\n", 0o600)}
    for command in ("radar-api", "radar-mcp"):
        launcher = '''#!/usr/bin/env bash
set -euo pipefail
root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
source "$root/env.sh"
export RADAR_KEYS_FILE="$root/secrets/keys.json"
'''
        if command == "radar-mcp":
            launcher += 'export RADAR_API_KEY="$(<"$root/secrets/client-key.txt")"\n'
        launcher += f'exec "$root/.venv/bin/{command}" "$@"\n'
        files[root / "bin" / command] = (launcher, 0o700)
    mcp_config = {"mcpServers": {"radar": {"command": str(root / "bin/radar-mcp")}}}
    files[root / "mcp.json"] = (json.dumps(mcp_config, indent=2) + "\n", 0o600)
    if any(path.exists() or path.is_symlink() for path in files):
        raise FileExistsError("Existing launchers or configuration will not be replaced")
    for path, (content, mode) in files.items():
        path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        with path.open("x") as handle:
            os.fchmod(handle.fileno(), mode)
            handle.write(content)
    print(f"\nInstalled Radar in {root}")
    print(f"Start REST / HTTP MCP: {shlex.quote(str(root / 'bin/radar-api'))} --port 8810")
    print("Local endpoint after starting: http://127.0.0.1:8810 (MCP: /mcp)")
    print(f"Local stdio MCP configuration: {root / 'mcp.json'}")
    print(f"Edit upstream settings: {root / 'env.sh'}")
    print(f"API key file (not printed): {root / 'secrets/client-key.txt'}")
    print("Setup is complete. Data requires an operator-configured upstream; no server was started.")


if __name__ == "__main__":
    configure(Path(sys.argv[1]))
