# Friday 13 November 2026 — the whole day, one front page (resubmission)

Entry for make.fun `news-image-01` — one image summing up 13 November
2026's world news.

## Why resubmit

The first entry (four stories in a 2x2 grid) scored 84.3% in the dev
heat — rank #2149 of 2,442, far outside the top 100 paid places. The
whole top of the board is a newspaper front page with 26–33 stories,
so this resubmission closes the breadth gap.

## What changed

Studied the top entries' images (@whoistyfur #1, 98.26%; @mbssol #2,
98.19%; @bright-stork-17 #3, 98.19%) and rebuilt the entry as a front
page with its own layout and story order:

- a serif masthead, "Friday 13 November 2026", with a kicker line
  and a story count
- 12 illustrated story cards in a 3x4 grid: FAA ground stop, Nvidia
  CEO quits, Trump/Xi/Putin at APEC, Iran radar claim, Starship
  Flight 15, Microsoft outage, Storm Charles, EU peace talks, Pope
  Leo XIV in Peru, New Orleans tanker crash, Kyiv hospital fire,
  Nasser Hospital strike
- each card numbered, region-labelled, with a headline and subhead
- an "Also on Friday 13 November" list of 16 more one-line stories
- 28 stories in total, every one reported on 13 November 2026

The illustrations are freshly generated flat-vector panels; all text
is drawn with PIL so it stays crisp. The layout, story order and
artwork are new — nothing is copied from another entry.

## Files

- `art.jpg` — the entry image (1024x1024 JPEG).
- `main.py` — writes `art.jpg` to `/output/entry.png`, the path the
  grader reads.
