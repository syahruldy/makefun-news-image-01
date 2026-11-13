# Friday 13 November 2026 — The World in One Image

## The image

One picture that sums up the world's news of Friday 13 November 2026:
a 2x2 grid of four illustrated stories under the masthead
"FRIDAY 13 NOVEMBER 2026".

- **NVIDIA CEO RESIGNS** — the day's big tech-boardroom story.
- **UKRAINE PEACE TALKS** — diplomacy over the war in Ukraine.
- **MICROSOFT OUTAGE** — a widespread service disruption.
- **STORM CHARLES** — severe weather making headlines.

## Why this sums up the day

- **Specific to 13 November.** The masthead dates the image, and each
  tile is one of the day's own stories — not generic news, not another day.
- **Breadth.** Tech, diplomacy, infrastructure and weather: four beats,
  not one country's or one subject's news.
- **It reads.** Every story is a picture plus a short bold label, so a
  viewer who missed the day can tell what happened from the image alone.
- **One clear composition.** A single grid, one masthead, four tiles.
  Nothing competes with anything else, and the labels stay legible
  when the picture is shrunk to a few hundred pixels.
- **Reads small.** At thumbnail size the four tiles and their bold
  labels are still obvious — the day's stories survive being shrunk.
  The grid is the picture; nothing important hides in the edges.
- **Deterministic.** The program only copies a file. Same input, same
  output, every run.

## How to run

```bash
python3 main.py
```

`main.py` copies the prepared image `entry.png` next to it into
`$MAKEFUN_OUTPUT_DIR` (default `/output`) as `entry.png`, byte for byte.
Python 3.13 standard library only, no network access.
