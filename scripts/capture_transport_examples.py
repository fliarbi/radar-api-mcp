#!/usr/bin/env python3
"""Capture real HTTP MCP initialization and one live tool result on loopback."""
import asyncio
import json
import logging
import os
import socket
import threading
import time
import tempfile
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

import httpx
import uvicorn
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from cryptography.fernet import Fernet
from starlette.testclient import TestClient

from radar_api.config import Settings
from radar_api.server import create_app


async def capture(base, key):
    report = {"captured_at": datetime.now(timezone.utc).isoformat(),
              "provenance": "Live HTTP MCP session on a temporary loopback gateway; configured live Radar upstream",
              "browser_routes": []}
    async with httpx.AsyncClient(headers={"Authorization": "Bearer " + key}) as client:
        for route in ["/docs"]:
            result = await client.get(base + route)
            report["browser_routes"].append({"path": route, "status": result.status_code,
                                             "content_type": result.headers.get("content-type"),
                                             "cache_control": result.headers.get("cache-control"),
                                             "body_prefix": result.text[:120]})
        async with streamable_http_client(base + "/mcp", http_client=client) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                report["initialize"] = (await session.initialize()).model_dump(mode="json", exclude_none=True)
                tools = (await session.list_tools()).tools
                report["tools"] = [{"name": tool.name, "annotations": tool.annotations.model_dump(exclude_none=True)} for tool in tools]
                report["tool_call"] = {"name": "get_company", "arguments": {"request": {"domain": "razorpay.com"}}}
                report["result"] = (await session.call_tool(**report["tool_call"])).model_dump(mode="json", exclude_none=True)
    with tempfile.TemporaryDirectory() as directory:
        settings = Settings(accounts_enabled=True, accounts_db=str(Path(directory) / "account.db"),
                            encryption_key=Fernet.generate_key().decode(), allowed_hosts=("testserver",))
        with TestClient(create_app(settings)) as client:
            for route in ["/developer", "/developer/console.js", "/developer/console.css"]:
                result = client.get(route)
                report["browser_routes"].append({"path": route, "status": result.status_code,
                                                 "content_type": result.headers.get("content-type"),
                                                 "cache_control": result.headers.get("cache-control"),
                                                 "body_prefix": result.text[:120]})
    path = Path("qa/private/endpoint-transports.json")
    fd = os.open(path, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "w") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print(f"Captured initialized HTTP MCP session, {len(report['tools'])} tools and one live result")
    for route in report["browser_routes"]:
        print(route["path"], route["status"], route["content_type"])


def main():
    logging.getLogger("httpx").setLevel(logging.WARNING)
    settings = replace(Settings.from_env(), allowed_hosts=("127.0.0.1", "localhost"), timeout_seconds=20)
    key = os.environ.get("RADAR_API_KEY") or Path("secrets/client-key.txt").read_text().strip()
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    base = "http://127.0.0.1:" + str(sock.getsockname()[1])
    server = uvicorn.Server(uvicorn.Config(create_app(settings), log_level="error", access_log=False, ws="none"))
    thread = threading.Thread(target=server.run, kwargs={"sockets": [sock]}, daemon=True)
    thread.start()
    try:
        for _ in range(100):
            if server.started:
                break
            time.sleep(0.02)
        assert server.started
        asyncio.run(capture(base, key))
    finally:
        server.should_exit = True
        thread.join(timeout=5)
        sock.close()
        assert not thread.is_alive()


if __name__ == "__main__":
    main()
