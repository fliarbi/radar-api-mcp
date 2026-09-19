import json
import os
import subprocess
import sys

from radar_api.auth import KeyStore


def test_key_issuance_keeps_secrets_out_of_stdout(tmp_path):
    store = tmp_path / "keys.json"
    output = tmp_path / "client-key.txt"
    result = subprocess.run([sys.executable, "-c", "from radar_api.cli import create_key; create_key()",
        "--name", "test", "--file", str(store), "--key-output", str(output)],
        capture_output=True, text=True, env={**os.environ, "RADAR_ACCOUNT_TOKEN": "secret-session"}, check=True)
    key = output.read_text().strip()
    assert key not in result.stdout and "secret-session" not in result.stdout
    assert "sha256" in json.loads(store.read_text())["keys"][0]
    assert key not in store.read_text()
    assert store.stat().st_mode & 0o777 == 0o600
    assert output.stat().st_mode & 0o777 == 0o600
    assert KeyStore(str(store)).authenticate(key).radar_token == "secret-session"
