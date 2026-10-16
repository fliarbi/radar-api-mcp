#!/usr/bin/env bash
# Install the `radar` command-line client for the Radar API. Never uses sudo and never
# starts a service. Sets RADAR_API_URL through ~/.config/radar/env.sh, loaded by one line
# in your shell startup files (skip with RADAR_NO_PROFILE=1).
# To run your own gateway server instead, use scripts/install-server.sh.
set -euo pipefail
umask 077

# Everything runs inside main so a partly downloaded script cannot execute half the steps.
main() {
if [[ ${1:-} == --help ]]; then
  cat <<'HELP'
Install `radar` (Radar API client: company data, financials, funding, investors and news).
Requires Bash, curl and Python 3.8+.
Environment:
  RADAR_BIN_DIR     Where the command goes (default: ~/.local/bin)
  RADAR_REF         Branch, tag or commit to install from (default: main)
  RADAR_NO_PROFILE  1 = do not add the env.sh line to ~/.bashrc, ~/.zshrc, ~/.profile
  GH_TOKEN          GitHub token with Contents: read (only for a private fork)
Your saved key in ~/.config/radar is kept.
HELP
  exit 0
fi
[[ $# == 0 ]] || { echo 'Use --help for installer options.' >&2; exit 2; }

repo=fliarbi/radar-api-mcp
ref=${RADAR_REF:-main}
bin_dir=${RADAR_BIN_DIR:-${HOME:?HOME must be set}/.local/bin}
[[ $ref =~ ^[A-Za-z0-9._/-]+$ && $ref != -* ]] || { echo 'Invalid RADAR_REF.' >&2; exit 2; }
command -v curl >/dev/null || { echo 'Install curl first.' >&2; exit 1; }
python_bin=$(command -v python3 || true)
[[ -n $python_bin ]] || { echo 'Install Python 3.8 or newer first.' >&2; exit 1; }
"$python_bin" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else "Python 3.8+ is required")'

stage=$(mktemp -d "${TMPDIR:-/tmp}/radar-install.XXXXXXXX")
trap 'rm -rf -- "$stage"' EXIT
token=${GH_TOKEN:-${GITHUB_TOKEN:-}}
[[ -z $token || $token =~ ^[A-Za-z0-9_]+$ ]] || { echo 'Invalid GitHub token format.' >&2; exit 2; }
url="https://raw.githubusercontent.com/$repo/$ref/scripts/radar_cli.py"
[[ -z $token ]] || url="https://api.github.com/repos/$repo/contents/scripts/radar_cli.py?ref=$ref"
echo "Downloading the Radar client ($ref)…"
# The header arrives on stdin, so a token never appears in process arguments or files.
if ! {
  printf 'header = "Accept: application/vnd.github.raw"\n'
  if [[ -n $token ]]; then printf 'header = "Authorization: Bearer %s"\n' "$token"; fi
} | curl --config - --proto '=https' --proto-redir '=https' --fail --silent --show-error --location \
    --connect-timeout 15 --max-time 120 --retry 2 "$url" -o "$stage/radar_cli.py"; then
  echo "Download failed. Check your connection to github.com." >&2
  exit 1
fi
unset token GH_TOKEN GITHUB_TOKEN
grep -q '^VERSION = ' "$stage/radar_cli.py" || { echo 'Unexpected download; nothing was installed.' >&2; exit 1; }
"$python_bin" -m py_compile "$stage/radar_cli.py"

mkdir -p -- "$bin_dir"
share=${XDG_DATA_HOME:-$HOME/.local/share}/radar-cli
mkdir -p -- "$share"
install -m 700 "$stage/radar_cli.py" "$share/radar_cli.py"
printf '#!/bin/sh\nexec "%s" "%s" "$@"\n' "$python_bin" "$share/radar_cli.py" > "$stage/radar"
install -m 700 "$stage/radar" "$bin_dir/radar"
echo "Installed radar in $bin_dir."

# Default API URL (and the command folder on PATH) for curl, Python, MCP clients and the CLI.
conf_dir=${XDG_CONFIG_HOME:-$HOME/.config}/radar
mkdir -p -- "$conf_dir"
cat > "$conf_dir/env.sh" <<ENV
# Radar API: written by the Radar installer. Safe to edit.
export RADAR_API_URL="\${RADAR_API_URL:-https://radar-api.fliarbi.com}"
case ":\$PATH:" in *":$bin_dir:"*) ;; *) export PATH="$bin_dir:\$PATH" ;; esac
ENV
chmod 644 "$conf_dir/env.sh"
line="[ -f \"$conf_dir/env.sh\" ] && . \"$conf_dir/env.sh\"  # radar-api"
if [[ ${RADAR_NO_PROFILE:-0} != 1 ]]; then
  for rc in "$HOME/.bashrc" "$HOME/.zshrc" "$HOME/.profile"; do
    [[ $rc == "$HOME/.profile" || -f $rc ]] || continue
    grep -qs '# radar-api$' "$rc" || printf '\n%s\n' "$line" >> "$rc"
  done
  echo "RADAR_API_URL is set for new shells (from $conf_dir/env.sh)."
else
  echo "Load the API URL with: . $conf_dir/env.sh"
fi
cat <<NEXT

Next (open a new terminal, or run: . $conf_dir/env.sh):
  radar login             # paste your API key once (create one at https://fliarbi.com/radar-api/developer)
  radar features
  radar get-financials --domain zomato.com --period-type annual
NEXT
}

main "$@"
