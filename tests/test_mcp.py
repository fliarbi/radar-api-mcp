from __future__ import annotations

import asyncio
import json
import os
import socket
import sys
import threading
import time
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest
import uvicorn
import httpx
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.streamable_http import streamable_http_client

from radar_api.service import FEATURES
from radar_api.server import create_app

from conftest import KEY, SAMPLES, payload_for


@contextmanager
def served(app):
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    server = uvicorn.Server(uvicorn.Config(app, log_level="error", access_log=False, ws="none"))
    thread = threading.Thread(target=server.run, kwargs={"sockets": [sock]}, daemon=True)
    thread.start()
    for _ in range(100):
        if server.started:
            break
        time.sleep(0.02)
    assert server.started
    try:
        yield f"http://127.0.0.1:{port}"
    finally:
        server.should_exit = True
        thread.join(timeout=5)
        sock.close()
        assert not thread.is_alive()


@pytest.mark.asyncio
async def test_real_http_mcp_all_tools_and_rest_parity(harness):
    client, _, app = harness
    upstream = app.state.service.upstream
    from radar_api.profiles import ProfileStore
    from test_profiles import StoreClient, record
    server_app = create_app(upstream.settings, upstream)
    app.state.service.profiles = ProfileStore(upstream.settings, StoreClient([record()]))
    server_app.state.service.profiles = ProfileStore(upstream.settings, StoreClient([record()]))
    server_app.state.service.internships = app.state.service.internships
    with served(server_app) as base:
        async with httpx.AsyncClient(headers={"Authorization": "Bearer " + KEY}) as http_client, \
                streamable_http_client(base + "/mcp", http_client=http_client) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                tools = (await session.list_tools()).tools
                assert {t.name for t in tools} == {f.name for f in FEATURES}
                assert all(t.annotations.readOnlyHint and not t.annotations.destructiveHint for t in tools)
                for feature in FEATURES:
                    result = await session.call_tool(feature.name, {"request": SAMPLES[feature.name]})
                    assert not result.isError, (feature.name, result)
                    rest = client.post("/v1/" + feature.path, json=SAMPLES[feature.name]).json()
                    wire = result.structuredContent
                    def without_retrieval_time(value):
                        if isinstance(value, dict):
                            return {k: without_retrieval_time(v) for k, v in value.items() if k != "retrieved_at"}
                        if isinstance(value, list):
                            return [without_retrieval_time(v) for v in value]
                        return value
                    assert without_retrieval_time(wire["data"]) == without_retrieval_time(rest["data"])
                    assert wire["window"] == rest["window"]
                invalid = await session.call_tool("get_company", {"request": {"domain": "evil.com/path"}})
                assert invalid.isError


@pytest.mark.asyncio
async def test_stdio_protocol_and_missing_key(keyfile, tmp_path):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def do_POST(self):
            self.rfile.read(int(self.headers.get("Content-Length", 0)))
            payload = json.dumps(payload_for(self.path)).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        for key, expected_error in [(KEY, False), ("invalid", True)]:
            params = StdioServerParameters(command=sys.executable,
                args=["-c", "from radar_api.cli import mcp; mcp()"], env={
                    **os.environ, "RADAR_KEYS_FILE": str(keyfile), "RADAR_API_KEY": key,
                    "RADAR_UPSTREAM_URL": f"http://127.0.0.1:{server.server_port}"})
            async with stdio_client(params) as streams:
                async with ClientSession(*streams) as session:
                    await session.initialize()
                    assert len((await session.list_tools()).tools) == 53
                    result = await session.call_tool("get_financials", {"request": {"domain": "example.com"}})
                    assert result.isError is expected_error
                    assert result.structuredContent["ok"] is not expected_error
    finally:
        await asyncio.to_thread(server.shutdown)
        server.server_close()
        thread.join(timeout=5)
