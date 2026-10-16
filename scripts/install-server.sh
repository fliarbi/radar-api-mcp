#!/usr/bin/env bash
# Install Radar locally. Never enables a service, changes shell profiles or uses sudo.
set -euo pipefail
umask 077

# Define the installer before running it so an incomplete piped download does not
# execute a partially received sequence of installation steps.
main() {
if [[ ${1:-} == --help ]]; then
  cat <<'HELP'
Install the Radar REST API and MCP server for the current user.
Requires Bash, curl and Python 3.11+ with venv/pip support.
Environment:
  GH_TOKEN            GitHub token with Contents: read (only for a private fork)
  RADAR_INSTALL_DIR   New directory (default: ~/.local/share/radar-api-mcp)
  RADAR_REF           Branch, tag or full commit SHA (default: main)
  RADAR_PYTHON        Python executable (default: python3)
  RADAR_UPSTREAM_URL  Operator-supplied Radar URL (default: http://127.0.0.1:5100)
Existing destinations are never overwritten. No server starts automatically.
HELP
  exit 0
fi
[[ $# == 0 ]] || { echo 'Use --help for installer options.' >&2; exit 2; }

python_bin=${RADAR_PYTHON:-python3}
install_dir=${RADAR_INSTALL_DIR:-${HOME:?HOME must be set}/.local/share/radar-api-mcp}
ref=${RADAR_REF:-main}
[[ $ref =~ ^[A-Za-z0-9._/-]+$ && $ref != -* ]] || { echo 'Invalid RADAR_REF.' >&2; exit 2; }
command -v curl >/dev/null || { echo 'Install curl first.' >&2; exit 1; }
command -v "$python_bin" >/dev/null || { echo 'Install Python 3.11+ first.' >&2; exit 1; }
"$python_bin" -c 'import sys, venv; sys.exit(0 if sys.version_info >= (3, 11) else "Python 3.11+ is required")'
install_dir=$("$python_bin" -c 'import os,sys; print(os.path.abspath(os.path.expanduser(sys.argv[1])))' "$install_dir")
if [[ -e $install_dir || -L $install_dir ]]; then
  echo "Destination already exists: $install_dir" >&2
  echo 'Existing files and keys were preserved. Use another RADAR_INSTALL_DIR for a new installation.' >&2
  exit 1
fi

stage=$(mktemp -d "${TMPDIR:-/tmp}/radar-install.XXXXXXXX")
trap 'rm -rf -- "$stage"' EXIT
token=${GH_TOKEN:-${GITHUB_TOKEN:-}}
if [[ -z $token ]] && command -v gh >/dev/null; then
  token=$(gh auth token 2>/dev/null || true)
fi
[[ -z $token || $token =~ ^[A-Za-z0-9_]+$ ]] || { echo 'Invalid GitHub token format.' >&2; exit 2; }
echo "Downloading Radar ($ref)…"
# Config arrives on stdin, so the token is absent from command arguments and files.
if ! {
  if [[ -n $token ]]; then printf 'header = "Authorization: Bearer %s"\n' "$token"; fi
} | curl --config - --proto '=https' --proto-redir '=https' --fail --silent --show-error --location \
    --connect-timeout 15 --max-time 180 --retry 2 \
    "https://api.github.com/repos/fliarbi/radar-api-mcp/tarball/$ref" -o "$stage/source.tar.gz"; then
  echo "Download failed. Check your connection to github.com (a private fork also needs GH_TOKEN)." >&2
  exit 1
fi
unset token GH_TOKEN GITHUB_TOKEN

# GitHub archives have one root directory. Reject traversal and links before extraction.
"$python_bin" - "$stage/source.tar.gz" "$stage/source" <<'PY'
import pathlib
import sys
import tarfile

destination = pathlib.Path(sys.argv[2])
with tarfile.open(sys.argv[1], 'r:gz') as archive:
    members = archive.getmembers()
    roots = {pathlib.PurePosixPath(item.name).parts[0] for item in members if item.name}
    if len(roots) != 1 or not members:
        raise SystemExit('Expected one source directory in the archive')
    for item in members:
        name = pathlib.PurePosixPath(item.name)
        if name.is_absolute() or '..' in name.parts or not (item.isfile() or item.isdir()):
            raise SystemExit('Unsafe source archive member')
    for item in members:
        relative = pathlib.PurePosixPath(item.name).parts[1:]
        target = destination.joinpath(*relative)
        if item.isdir():
            target.mkdir(parents=True, exist_ok=True)
        elif relative:
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(item) as source, target.open('xb') as output:
                import shutil
                shutil.copyfileobj(source, output)
    (destination / 'INSTALL_SOURCE').write_text(next(iter(roots)) + '\n')
if not (destination / 'pyproject.toml').is_file() or not (destination / 'scripts/setup_local.py').is_file():
    raise SystemExit('Incomplete Radar source archive')
PY

mkdir -p -- "$(dirname "$install_dir")"
# mkdir reserves the destination and fails safely if another install created it.
mkdir -- "$install_dir"
cp -R "$stage/source/." "$install_dir/"
echo 'Creating an isolated Python environment and installing dependencies…'
"$python_bin" -m venv "$install_dir/.venv" || {
  echo 'Python venv/pip support is required (python3-venv on Debian/Ubuntu).' >&2; exit 1;
}
"$install_dir/.venv/bin/python" -m pip install --disable-pip-version-check "$install_dir"
# A fresh preview key should not silently copy credentials from another installation.
unset RADAR_ACCOUNT_TOKEN RADAR_ACCOUNT_NEWS_KEY
"$install_dir/.venv/bin/radar-create-key" --name local-preview \
  --file "$install_dir/secrets/keys.json" --key-output "$install_dir/secrets/client-key.txt"
"$install_dir/.venv/bin/python" "$install_dir/scripts/setup_local.py" "$install_dir"
}

main "$@"
