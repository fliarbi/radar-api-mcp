# Fliar dashboard connection for Radar API keys

This optional integration adds **Radar → Radar API & MCP** and a
**Create or manage API keys** link. It reuses the account console and the signed-in
Radar session on the same browser origin. Prism News keeps its separate key page.

The integration is prepared for private deployment. Installing local files does
not activate a public gateway or alter the GitHub repository's visibility.

## Install into a reviewed local frontend checkout

```bash
python scripts/install_dashboard_panel.py --frontend /path/to/radar
python scripts/install_dashboard_panel.py --frontend /path/to/radar --apply
```

The first command checks the dashboard's integration points. The second creates
a backup outside the served frontend tree, adds the sidebar entry and deep-link
routing, and copies the PHP panel. The backup defaults to the repository's ignored
`qa/private/dashboard-backups` directory with owner-only permissions; use
`--backup-dir` to select another private directory outside the frontend tree.
Review the resulting diff before transferring the two frontend files.
[The reviewed dashboard patch](dashboard.patch) shows the sidebar entry,
section registration and PHP include; the installer checks those anchors before
applying them to a compatible frontend version.
`?tab=radarapi` selects the new panel in the Radar workspace.

With no connection configured, the panel explains that private access is not
enabled. It displays no key-creation link and makes no account/API request.

## Connect the private account gateway

1. Configure account mode using [the account runbook](../../docs/ACCOUNTS.md).
   Keep its persistent encryption key and account database in the secret store.
2. Reserve a same-origin prefix, for example `/radar-api`, and proxy it to the
   account gateway. Strip that prefix when forwarding and start the gateway with
   Uvicorn `--root-path /radar-api`. The console preserves the prefix in assets,
   account requests and the displayed REST/MCP URLs.
3. Add `"radar_developer_path": "/radar-api/developer"` to the existing frontend
   `site_config`. The panel accepts only a same-origin absolute path ending in
   `/developer`, without a query or fragment. External URLs are rejected.
4. Keep the gateway and console behind the chosen private access boundary.
   Configure explicit allowed hosts/origins. Opening the gateway publicly is a
   separate deployment decision; the repository remains private until approved.
5. Sign in to a verified Radar account, open the new panel, connect the session,
   create a scoped key and copy it once. Verify a permitted request, list the key
   metadata and revoke the test key. An expired Radar session must deny issuance.

The mount-prefix regression tests cover direct and nested hosting. They do not
certify a public deployment, a live customer identity or a payment integration.

## Rollback

Remove `radar_developer_path` to disable the launch link. Restore the dashboard
from the owner-only backup printed by the installer after checking for intervening
edits, and remove the copied panel if no other page includes it. Stop routing the
private prefix only after considering active integrations; existing API keys
must be explicitly revoked when access should end.
