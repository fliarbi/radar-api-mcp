# Local Radar animation gallery

Open [index.html](index.html) in a browser, or serve only the documentation folder
from the repository root:

```bash
python3 -m http.server 8820 --directory docs
```

The seven chart formats are a stage-distribution bar, grouped financial columns,
a founder relationship diagram, a founding-year dot plot, a funding timeline, an
app-install lollipop ranking and a contact-coverage donut. Charts describe only
the displayed source-qualified sample. Derived net margins are labelled; unknown
metrics are not plotted as zero.

The GIFs depict a client-built research workspace, not an official Claude Code or
Codex screen. Some use saved source captures; other cohorts and contact rows are
explicitly fictional. The [walkthroughs](../ANIMATED_USE_CASES.md) explain each case.
No live service calls, real contact exports or message sends occur.

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
