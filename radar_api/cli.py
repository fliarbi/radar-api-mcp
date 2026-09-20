from __future__ import annotations

import argparse
import hashlib
import json
import os
import secrets
import tempfile
from pathlib import Path

from .auth import KeyStore
from .config import Settings
from .server import build_mcp, create_app
from .service import Service
from .upstream import Upstream
from .accounts import Accounts


def api():
    import uvicorn
    parser = argparse.ArgumentParser(description="Run the private Radar API and MCP endpoint")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8810)
    args = parser.parse_args()
    uvicorn.run(create_app(), host=args.host, port=args.port, access_log=False)


def mcp():
    settings = Settings.from_env()
    accounts = Accounts(settings) if settings.accounts_enabled else None
    build_mcp(Service(Upstream(settings), accounts), stdio_store=KeyStore(settings.keys_file),
              stdio_key=os.getenv("RADAR_API_KEY", "")).run(transport="stdio")


def _private_write(path: Path, content: str):
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=".key-")
    try:
        with os.fdopen(fd, "w") as handle:
            os.fchmod(handle.fileno(), 0o600)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    except BaseException:
        Path(name).unlink(missing_ok=True)
        raise


def create_key():
    parser = argparse.ArgumentParser(description="Create a private preview key without printing secrets")
    parser.add_argument("--name", required=True)
    parser.add_argument("--file", default=Settings.from_env().keys_file)
    parser.add_argument("--key-output", default="secrets/client-key.txt")
    parser.add_argument("--rate", type=int, default=60)
    args = parser.parse_args()
    if not 1 <= args.rate <= 600:
        parser.error("rate must be between 1 and 600")
    path, output = Path(args.file), Path(args.key_output)
    if path.resolve() == output.resolve():
        parser.error("key-output must differ from the key store")
    if output.exists():
        parser.error("key-output exists; choose a new file to preserve the existing key")
    for p in (path, output):
        p.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    key = "rdr_" + secrets.token_hex(32)
    # Lock the separate lockfile because the key store itself is atomically replaced.
    import fcntl
    with open(str(path) + ".lock", "a") as lock:
        os.fchmod(lock.fileno(), 0o600)
        fcntl.flock(lock, fcntl.LOCK_EX)
        if path.exists() and path.stat().st_mode & 0o077:
            parser.error("existing key store must have mode 0600")
        data = json.loads(path.read_text()) if path.exists() else {"keys": []}
        data["keys"].append({"name": args.name, "sha256": hashlib.sha256(key.encode()).hexdigest(),
                             "active": True, "rate_per_minute": args.rate,
                             "radar_token": os.getenv("RADAR_ACCOUNT_TOKEN", ""),
                             "news_key": os.getenv("RADAR_ACCOUNT_NEWS_KEY", "")})
        # Exclusive create keeps simultaneous issuers from replacing another client's key.
        fd = os.open(output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w") as handle:
            handle.write(key + "\n")
        _private_write(path, json.dumps(data, indent=2) + "\n")
    print(f"Created key record for {args.name}. Key saved to {output}; store: {path}.")


if __name__ == "__main__":
    api()
