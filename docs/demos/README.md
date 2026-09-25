# Local Radar animation gallery

Open [index.html](index.html) in a browser, or serve only the documentation folder
from the repository root:

```bash
python3 -m http.server 8820 --bind 127.0.0.1 --directory docs
```

Then open `http://127.0.0.1:8820/demos/`. This is a local preview, not a deployment.
The gallery uses local assets and no API connection or API key. It supports
play/pause, replay, per-workflow selection, copying prompts and downloading GIFs
or still frames. With reduced motion enabled, it starts on a still image.

The seven chart formats are a stage-distribution bar, grouped financial columns,
a founder relationship diagram, a founding-year dot plot, a funding timeline, an
app-install lollipop ranking and a contact-coverage donut. Charts describe only
the displayed source-qualified sample. Derived net margins are labelled; unknown
metrics are not plotted as zero.

The GIFs depict a client-built research workspace, not an official Claude Code or
Codex screen. Some use saved source captures; other cohorts and contact rows are
explicitly fictional. The [walkthroughs](../ANIMATED_USE_CASES.md) explain each case.
No live service calls, real contact exports or message sends occur.

## Rebuild

Development-only requirements: the repository Python environment, Node 22 or
newer with built-in WebSocket support, a Chrome/Chromium executable, FFmpeg with
GIF palette filters, and Pillow for artifact inspection. These are not API runtime
dependencies. Set `CHROME_BIN` and `FFMPEG_BIN` if they are not in the default paths.

```bash
.venv/bin/python scripts/build_use_case_demos.py
node scripts/render_use_case_demos.mjs --stills
node scripts/render_use_case_demos.mjs --fps 10
.venv/bin/python scripts/check_use_case_demos.py --write-manifest
.venv/bin/python scripts/check_docs.py
```

`--id financial-comparison` renders one story. `--chrome` and `--ffmpeg` accept
executable paths. The renderer launches an isolated temporary headless-browser
profile, opens local files, evaluates explicit animation times and captures PNGs.
Frame files and geometry reports stay in ignored `qa/private/`; the browser profile
is removed. The GIF palette is computed from the complete clip, then applied with
ordered dithering. Every exported loop is 1280 × 800 at 10 frames per second,
lasting 32 seconds. A 42px typed prompt fills the opening search box, slides fully
off-screen, then gives way to a full-screen chart and a separate detailed result view. Equivalent frames may be coalesced by the GIF encoder.

Only the supplied animation pages are opened in this isolated renderer. It does
not attach to a user's browsing session. The gallery has no analytics, remote
fonts, third-party JavaScript, API fetches or credential storage.

## Evidence and limits

[demo-data.json](demo-data.json) is the story and request manifest. The financial
numbers, selected peer cards and professional profile are read directly from
checked-in captures; source file hashes make changes detectable. All Radar tool
requests are validated with the repository's actual input models. Tool execution
and latency are illustrated, not measured.

The checker validates provenance and source hashes, tool request contracts, media
dimensions, frame variation, loop settings, duration, and the presence of all seven
GIF/poster pairs. It writes [media/manifest.json](media/manifest.json) with file hashes
and sizes. Layout measurements and desktop/mobile gallery interaction checks are
separate local QA; visual inspection remains necessary for readability.

The gallery's pause control switches to the final still image. Replay starts the
selected GIF again. This keeps the distributed format a genuine GIF while offering
a way to stop motion. The stills also provide a readable alternative to animation.
