#!/usr/bin/env python3
"""Prepare the optional Radar dashboard panel in a specified local frontend tree."""
import argparse
import hashlib
import os
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
MARKER = '<!-- radar-api-mcp dashboard integration -->'


def patched(text):
    if MARKER in text:
        return text
    replacements = [
        ('        <div id="nav-radar">', '''        <div id="nav-radar">
            <!-- radar-api-mcp dashboard integration -->
            <button type="button" class="nav-item w-full text-left" data-section="radarapi" onclick="showSection('radarapi')">
                <span class="material-symbols-outlined">key</span>Radar API &amp; MCP
            </button>'''),
        ("    overview:    'Dashboard',", "    radarapi:    'Radar API & MCP',\n    overview:    'Dashboard',"),
        ("const RADAR_SECTIONS = ['overview'", "const RADAR_SECTIONS = ['radarapi','overview'"),
        ('    <section id="section-settings"', "    <?php include __DIR__ . '/../src/php/radar-api-panel.php'; ?>\n\n    <section id=\"section-settings\""),
    ]
    for old, new in replacements:
        if text.count(old) != 1:
            raise ValueError('Dashboard structure changed; review integration anchor: ' + old)
        text = text.replace(old, new, 1)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frontend', type=Path, required=True, help='Local radar/ directory containing public/dashboard.php')
    parser.add_argument('--apply', action='store_true', help='Write local panel and dashboard edits; never deploy remotely')
    parser.add_argument('--backup-dir', type=Path, default=ROOT / 'qa/private/dashboard-backups',
                        help='Owner-only backup directory outside the frontend tree')
    args = parser.parse_args()
    dashboard = args.frontend / 'public/dashboard.php'
    original = dashboard.read_text()
    replacement = patched(original)
    target = args.frontend / 'src/php/radar-api-panel.php'
    if args.apply:
        if replacement != original:
            if args.backup_dir.resolve().is_relative_to(args.frontend.resolve()):
                raise SystemExit('Store backups outside the served frontend tree.')
            args.backup_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
            backup = args.backup_dir / ('dashboard-' + hashlib.sha256(original.encode()).hexdigest()[:16] + '.php')
            fd = os.open(backup, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            with os.fdopen(fd, 'w') as stream:
                stream.write(original)
            dashboard.write_text(replacement)
            print('Owner-only dashboard backup:', backup)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / 'integrations/fliar-dashboard/radar-api-panel.php', target)
        print('Installed local dashboard panel. No server configuration or public deployment changed.')
    else:
        print('Dashboard integration anchors verified. Pass --apply to write local files.')


if __name__ == '__main__':
    main()
