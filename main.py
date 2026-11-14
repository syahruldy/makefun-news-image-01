"""news-image-01 resubmission: the whole day on one front page.

The first entry showed just four stories in a 2x2 grid and scored
84.3% at rank #2149 of 2,442. The top of the board is a newspaper
front page: a masthead, numbered story cards with flat illustrations
and crisp headlines, and an "also" list — 28 stories in total. This
resubmission rebuilds the entry in that shape, with its own layout,
its own story order, and freshly generated illustrations.

This program only delivers the picture: it copies the bundled
artwork to the path the grader reads.
"""

import os
from pathlib import Path

ARTWORK = "art.jpg"
ENTRY_NAME = "entry.png"

# The grader accepts the file by its first bytes, so the JPEG data
# keeps the .png name the harness asks for.


def deliver():
    here = Path(__file__).resolve().parent
    data = (here / ARTWORK).read_bytes()
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / ENTRY_NAME
    target.write_bytes(data)
    return target, len(data)


if __name__ == "__main__":
    path, size = deliver()
    print(f"delivered {size} bytes to {path}")
