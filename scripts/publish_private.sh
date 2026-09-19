#!/usr/bin/env bash
set -euo pipefail
repo=${1:-fliarbi/radar-api-mcp}
if [[ ! "$repo" =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]]; then
  echo 'Use OWNER/REPOSITORY.' >&2
  exit 2
fi
cd "$(dirname "$0")/.."
gh auth status >/dev/null 2>&1 || { echo 'GitHub authentication required: run gh auth login.' >&2; exit 1; }
test -z "$(git status --porcelain)" || { echo 'Commit and review all changes first.' >&2; exit 1; }
if gh repo view "$repo" --json isPrivate --jq '.isPrivate' >/dev/null 2>&1; then
  test "$(gh repo view "$repo" --json isPrivate --jq '.isPrivate')" = true || {
    echo 'Refusing to push: the destination repository is not private.' >&2; exit 1;
  }
else
  gh repo create "$repo" --private --description 'Private Radar company intelligence, financial data and news API + MCP'
fi
test "$(gh repo view "$repo" --json isPrivate --jq '.isPrivate')" = true || {
  echo 'Private visibility could not be verified; no push performed.' >&2; exit 1;
}
expected="git@github.com:${repo}.git"
if git remote get-url origin >/dev/null 2>&1; then
  test "$(git remote get-url origin)" = "$expected" || {
    echo 'Origin differs from the reviewed destination; no push performed.' >&2; exit 1;
  }
else
  git remote add origin "$expected"
fi
git push -u origin main
gh repo view "$repo" --json nameWithOwner,isPrivate,url
test "$(gh repo view "$repo" --json isPrivate --jq '.isPrivate')" = true
