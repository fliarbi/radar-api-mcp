"""The `radar` command-line client and its one-line installer."""
import importlib.util
import subprocess
import sys
from pathlib import Path

from radar_api.service import FEATURES

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("radar_cli", ROOT / "scripts/radar_cli.py")
cli = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cli)


def test_client_knows_every_operation():
    assert cli.FEATURES == {f.name.replace("_", "-"): f.path for f in FEATURES}


def test_options_build_nested_request_bodies():
    pos, body, flags = cli.parse(["--filters.industries", "FinTech", "--filters.locations", "India",
                                  "--limit", "20", "--include-news", "true", "--table"])
    assert body == {"filters": {"industries": ["FinTech"], "locations": ["India"]}, "limit": 20, "include_news": True}
    assert flags == {"table": True} and pos == []


def test_getting_started_documents_every_operation():
    doc = (ROOT / "docs/GETTING_STARTED.md").read_text()
    for name, path in cli.FEATURES.items():
        assert f"`radar {name}`" in doc and f"/v1/{path}" in doc


def test_client_installer_is_valid_and_never_uses_sudo():
    script = ROOT / "scripts/install.sh"
    subprocess.run(["bash", "-n", str(script)], check=True)
    assert "sudo " not in script.read_text().replace("Never uses sudo", "")
    out = subprocess.run(["bash", str(script), "--help"], capture_output=True, text=True, check=True).stdout
    assert "RADAR_NO_PROFILE" in out


def test_client_saves_key_owner_only(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "CONFIG", tmp_path / "radar" / "config.json")
    cli.save_config({"key": "rdr_x"})
    assert oct(cli.CONFIG.stat().st_mode & 0o777) == "0o600"


def test_client_help_runs_without_configuration():
    out = subprocess.run([sys.executable, str(ROOT / "scripts/radar_cli.py"), "--help"], capture_output=True, text=True, check=True).stdout
    assert "radar login" in out
