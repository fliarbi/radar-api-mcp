#!/usr/bin/env python3
"""Capture the API responses behind the demonstration pages.

Walks each segment of docs/use-cases/plan.json in search-demand order, runs every
call of a scenario against a running API and keeps the first `target` scenarios
whose primary call returns populated data. Results go to docs/examples/use-cases/
and the outcome of every attempt to docs/use-cases/capture_log.json (resumable).
Account details (plan, quota, key) are removed before saving.

    PRISM_API_BASE=http://127.0.0.1:8800 PRISM_API_KEY=pna_... \\
        python3 scripts/capture_scenarios.py [--segment ID] [--workers 4] [--redo]

PRISM_CAPTURE_COVERAGE adds a coverage note (e.g. "93% of indexed articles (1 of 14
shards offline)") when the news index is only partly available.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

import scenario_common as sc


def populated(rec: dict, s: dict) -> tuple[bool, str]:
    main = sc.call_of(rec, s["primary"]["call"])
    if not main or main["status"] != 200 or not main["response"].get("ok"):
        err = (main or {}).get("response", {}).get("error") or {}
        return False, f"HTTP {(main or {}).get('status')} {err.get('kind')}"
    data = main["response"].get("data") or {}
    value = data
    for part in s["primary"]["field"].split("."):
        value = value.get(part) if isinstance(value, dict) else None
    value = len(value) if isinstance(value, list) else (value or 0)
    if value < s["primary"]["min"]:
        return False, f"{s['primary']['field']}={value} below {s['primary']['min']}"
    failed = [c["name"] for c in rec["calls"] if c["status"] != 200]
    if len(failed) > len(rec["calls"]) // 2:
        return False, "most supporting calls failed: " + ", ".join(failed)
    return True, f"{s['primary']['field']}={value}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--segment")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--redo", action="store_true", help="recapture scenarios already logged")
    ap.add_argument("--refresh", action="store_true",
                    help="recapture only the kept scenarios with their current plan calls (after a recipe change)")
    args = ap.parse_args()
    base = os.environ.get("PRISM_API_BASE", "http://127.0.0.1:8800").rstrip("/")
    key = os.environ.get("PRISM_API_KEY") or sys.exit("set PRISM_API_KEY")
    plan = json.loads(sc.PLAN.read_text())
    log = json.loads(sc.LOG.read_text()) if sc.LOG.exists() else {}
    lock = threading.Lock()
    sc.CAPS.mkdir(parents=True, exist_ok=True)

    def save_log():
        sc.LOG.write_text(json.dumps(dict(sorted(log.items())), indent=1) + "\n")

    for seg in plan["segments"]:
        if args.segment and seg["id"] != args.segment:
            continue
        if args.redo:
            for s in seg["scenarios"]:
                log.pop(s["slug"], None)
        queue = list(seg["scenarios"])

        def kept() -> int:
            return sum(1 for s in seg["scenarios"] if log.get(s["slug"], {}).get("kept"))

        def refresh(s: dict) -> None:
            if not log.get(s["slug"], {}).get("kept"):
                return
            rec = sc.capture_scenario(base, key, s)
            ok, why = populated(rec, s)
            with lock:
                if ok:
                    (sc.CAPS / f"{s['slug']}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
                    log[s["slug"]].update(why=why, at=rec["captured_at"])
                    save_log()
                print(f"{seg['id']:22} refresh {s['slug']}: {'saved' if ok else 'kept previous capture'} ({why})", flush=True)

        def work(s: dict) -> None:
            if s["slug"] in log or kept() >= seg["target"]:
                return
            rec = sc.capture_scenario(base, key, s)
            ok, why = populated(rec, s)
            with lock:
                if ok and kept() < seg["target"]:
                    (sc.CAPS / f"{s['slug']}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
                    log[s["slug"]] = {"kept": True, "why": why, "at": rec["captured_at"]}
                else:
                    log[s["slug"]] = {"kept": False, "why": why if not ok else "segment target reached",
                                      "at": rec["captured_at"]}
                save_log()
                print(f"{seg['id']:22} {kept():3}/{seg['target']} {s['slug']}: {'kept' if log[s['slug']]['kept'] else 'dropped'} ({why})",
                      flush=True)

        with ThreadPoolExecutor(args.workers) as pool:
            list(pool.map(refresh if args.refresh else work, queue))
        print(f"== {seg['id']}: {kept()} kept", flush=True)


if __name__ == "__main__":
    main()
