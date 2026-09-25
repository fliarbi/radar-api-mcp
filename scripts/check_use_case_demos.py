#!/usr/bin/env python3
"""Check demo contracts/provenance and media hashes; optionally inspect GIF frames."""
import argparse
import hashlib
import json
from pathlib import Path
import struct

from radar_api.service import BY_NAME

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs/demos"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect(stories):
    from PIL import Image

    rows = []
    for story in stories:
        gif = BASE / "media" / (story["id"] + ".gif")
        png = gif.with_suffix(".png")
        with Image.open(gif) as image:
            duration = 0
            result_hashes, prompt_hashes = set(), set()
            loop = image.info.get("loop")
            frames = image.n_frames
            for i in range(frames):
                image.seek(i)
                duration += image.info.get("duration", 0)
                if i in (0, 15, 30, 60, 110, 250, frames - 1):
                    rgb = image.convert("RGB")
                    result_hashes.add(hashlib.sha256(rgb.crop((50, 190, 1230, 690)).tobytes()).hexdigest())
                    prompt_hashes.add(hashlib.sha256(rgb.crop((70, 310, 1210, 620)).tobytes()).hexdigest())
            assert image.size == (1280, 800) and frames >= 100 and loop == 0, gif
            assert abs(duration - story["duration"] * 1000) <= 100, gif
            assert len(result_hashes) >= 3 and len(prompt_hashes) >= 3, "Missing meaningful animation: " + str(gif)
        with Image.open(png) as image:
            assert image.size == (1280, 800), png
        rows.append({"id": story["id"], "gif": "media/" + gif.name, "poster": "media/" + png.name,
                     "width": 1280, "height": 800, "frames": frames, "duration_ms": duration,
                     "loop": loop, "gif_bytes": gif.stat().st_size, "poster_bytes": png.stat().st_size,
                     "gif_sha256": sha(gif), "poster_sha256": sha(png), "data_kind": story["kind"],
                     "result_region_varies": True, "typed_prompt_region_varies": True})
    return {"scope": "Animated client UI concepts; source data and illustrative values are separately labeled",
            "render_sources": [{"file": file, "sha256": sha(BASE / file)}
                               for file in ("stage.html", "stage.js", "stage.css", "demo.css")],
            "story_sha256": sha(BASE / "demo-data.json"), "gifs": len(rows), "clips": rows}


def check():
    stories = json.loads((BASE / "demo-data.json").read_text())
    assert len(stories) == 7 and len({s["id"] for s in stories}) == 7
    javascript = (BASE / "demo-data.js").read_text()
    assert javascript == "window.RADAR_DEMOS = " + json.dumps(stories, ensure_ascii=False, indent=2) + ";\n"
    assert sum(s["kind"] == "captured" for s in stories) == 3
    for story in stories:
        assert story["kind"] in {"captured", "illustrative"}
        assert "not a recording" in story["disclosure"] and story["badge"] and story["footnote"]
        if story["kind"] == "captured":
            assert story["sources"]
        for source in story["sources"]:
            assert sha(BASE / source["file"]) == source["sha256"], source["file"]
        for step in story["steps"]:
            assert step["type"] in {"radar", "client"}
            if step["type"] == "radar":
                BY_NAME[step["name"]].model.model_validate(step["request"])
        assert (BASE / story["guide"]).exists()
    manifest = json.loads((BASE / "media/manifest.json").read_text())
    for source in manifest["render_sources"]:
        assert sha(BASE / source["file"]) == source["sha256"], "Re-render changed animation source: " + source["file"]
    assert manifest["story_sha256"] == sha(BASE / "demo-data.json")
    assert {r["id"] for r in manifest["clips"]} == {s["id"] for s in stories}
    for row in manifest["clips"]:
        gif, png = BASE / row["gif"], BASE / row["poster"]
        assert sha(gif) == row["gif_sha256"] and sha(png) == row["poster_sha256"]
        assert gif.read_bytes()[:6] in (b"GIF87a", b"GIF89a")
        assert struct.unpack("<HH", gif.read_bytes()[6:10]) == (1280, 800)
        assert png.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
        assert struct.unpack(">II", png.read_bytes()[16:24]) == (1280, 800)
        assert row["frames"] >= 100 and row["loop"] == 0
    print(f"Verified {len(stories)} GIF/poster pairs, media hashes, source provenance and typed tool recipes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true", help="Requires Pillow; decode GIF frames and refresh hashes")
    args = parser.parse_args()
    if args.write_manifest:
        records = json.loads((BASE / "demo-data.json").read_text())
        result = inspect(records)
        (BASE / "media/manifest.json").write_text(json.dumps(result, indent=2) + "\n")
    check()
