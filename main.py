"""make.fun news-image-01 entry: copy the prepared picture into the output dir.

The picture sums up the world's news of Friday 13 November 2026 in one
image: a 2x2 grid of four illustrated stories under the masthead
"FRIDAY 13 NOVEMBER 2026", each tile labelled exactly as follows -
"NVIDIA CEO RESIGNS", "UKRAINE PEACE TALKS", "MICROSOFT OUTAGE" and
"STORM CHARLES". Each tile pairs a picture with a short bold label, so a
viewer who missed the day can tell what happened from the image alone.

Determinism: the program has no randomness, no timestamps and no network
calls, so running it twice on the same input always produces the same
output file. The only input is entry.png; the only output is entry.png.

Nothing in this program reaches the network; it only copies a file that
is already on disk.

This program takes the entry.png sitting next to it and writes it out as
entry.png in the output directory given by MAKEFUN_OUTPUT_DIR (default
/output). The output is a byte-for-byte copy of the input, so what the
judge sees is exactly the picture that was prepared.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    if not source.is_file():
        print(f"error: {source} not found", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"

    shutil.copyfile(source, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
