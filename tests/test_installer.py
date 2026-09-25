"""Installer boundaries: no overwrites, safe archive handling and private launchers."""
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile

import pytest


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts/install.sh"
spec = importlib.util.spec_from_file_location("setup_local", ROOT / "scripts/setup_local.py")
setup_local = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup_local)


def installer_env(tmp_path):
    return {**os.environ, "RADAR_INSTALL_DIR": str(tmp_path / "install"),
            "RADAR_PYTHON": sys.executable, "GH_TOKEN": "test_token", "RADAR_REF": "main"}


def test_existing_install_is_preserved(tmp_path):
    env = installer_env(tmp_path)
    target = Path(env["RADAR_INSTALL_DIR"])
    target.mkdir()
    key = target / "client-key.txt"
    key.write_text("existing-private-key")
    result = subprocess.run(["bash", str(INSTALLER)], env=env, capture_output=True, text=True)
    assert result.returncode != 0
    assert "preserved" in result.stderr
    assert key.read_text() == "existing-private-key"
    assert list(target.iterdir()) == [key]


@pytest.mark.parametrize("member_name,kind", [
    ("repo/../../outside", "file"), ("/outside", "file"), ("repo/link", "symlink"),
])
def test_unsafe_archive_is_rejected_before_install(tmp_path, member_name, kind):
    archive_path = tmp_path / "bad.tar.gz"
    with tarfile.open(archive_path, "w:gz") as archive:
        member = tarfile.TarInfo(member_name)
        if kind == "symlink":
            member.type = tarfile.SYMTYPE
            member.linkname = "/tmp"
            archive.addfile(member)
        else:
            member.size = 3
            archive.addfile(member, io.BytesIO(b"bad"))
    stub_dir = tmp_path / "stubs"
    stub_dir.mkdir()
    curl = stub_dir / "curl"
    curl.write_text('#!/usr/bin/env bash\ncat >/dev/null\n'
                    'while [[ $# -gt 0 ]]; do if [[ $1 == -o ]]; then cp "$TEST_ARCHIVE" "$2"; '
                    'exit; fi; shift; done\nexit 1\n')
    curl.chmod(0o700)
    env = {**installer_env(tmp_path), "PATH": str(stub_dir) + os.pathsep + os.environ["PATH"],
           "TEST_ARCHIVE": str(archive_path)}
    result = subprocess.run(["bash", str(INSTALLER)], env=env, capture_output=True, text=True)
    assert result.returncode != 0
    assert "Unsafe source archive" in result.stderr
    assert not Path(env["RADAR_INSTALL_DIR"]).exists()
    assert not (tmp_path / "outside").exists()
    assert env["GH_TOKEN"] not in result.stdout + result.stderr


def test_mcp_launcher_reads_key_without_embedding_it(tmp_path, monkeypatch, capsys):
    root = tmp_path / "install with spaces"
    (root / ".venv/bin").mkdir(parents=True)
    (root / "secrets").mkdir()
    key = "rdr_" + "a" * 64
    (root / "secrets/client-key.txt").write_text(key + "\n")
    stub = root / ".venv/bin/radar-mcp"
    stub.write_text(f"#!{sys.executable}\nimport hashlib,json,os,sys\n"
                    "print(json.dumps({'key_hash':hashlib.sha256(os.environ['RADAR_API_KEY'].encode()).hexdigest(),"
                    "'store':os.environ['RADAR_KEYS_FILE'],'url':os.environ['RADAR_UPSTREAM_URL'],"
                    "'args':sys.argv[1:]}))\n")
    stub.chmod(0o700)
    monkeypatch.setenv("RADAR_UPSTREAM_URL", "https://radar.example")
    monkeypatch.setenv("RADAR_NEWS_URL", "")
    monkeypatch.setenv("RADAR_BUSINESS_NEWS_URL", "")
    setup_local.configure(root)
    assert key not in capsys.readouterr().out
    config = json.loads((root / "mcp.json").read_text())
    launcher = config["mcpServers"]["radar"]["command"]
    env = {**os.environ, "RADAR_UPSTREAM_URL": "https://override.example", "RADAR_API_KEY": "wrong-key"}
    result = subprocess.run([launcher, "argument with spaces"], env=env, capture_output=True, text=True, check=True)
    actual = json.loads(result.stdout)
    assert actual == {"key_hash": hashlib.sha256(key.encode()).hexdigest(),
                      "store": str(root / "secrets/keys.json"), "url": "https://override.example",
                      "args": ["argument with spaces"]}
    for name in ("env.sh", "mcp.json", "bin/radar-api", "bin/radar-mcp"):
        path = root / name
        assert key not in path.read_text()
        assert path.stat().st_mode & 0o077 == 0
    original = (root / "env.sh").read_bytes()
    with pytest.raises(FileExistsError):
        setup_local.configure(root)
    assert (root / "env.sh").read_bytes() == original


def test_setup_rejects_credentials_in_upstream_url(tmp_path, monkeypatch):
    monkeypatch.setenv("RADAR_UPSTREAM_URL", "https://user:secret@radar.example")
    with pytest.raises(ValueError, match="without credentials"):
        setup_local.configure(tmp_path)
    assert not list(tmp_path.iterdir())
