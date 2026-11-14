"""Round 3 entry for news-image-01: Friday 13 November 2026.

Writes the front-page image to $MAKEFUN_OUTPUT_DIR/entry.png.
The image is a newspaper front page: 30 stories from Friday
13 November 2026, 6 continents, every story pinned on a world map.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    # The harness provides MAKEFUN_OUTPUT_DIR; the art ships in the repo.
    src = os.path.join(HERE, "art.jpg")
    out = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(src, os.path.join(out, "entry.png"))


if __name__ == "__main__":
    main()
