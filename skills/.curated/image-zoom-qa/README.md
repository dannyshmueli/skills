# Iterative Zoom QA

AI agents are pretty good at comparing a result to a reference image — until the important difference is small.

They may say a design “looks close” while missing the thing you actually care about: a wrong logo, a visible compositing seam, a square shadow, a rotated label, or a miscentered icon.

**Iterative Zoom QA fixes that by making the agent compare the image like a designer would: start broad, crop the suspicious region, zoom in, name the exact difference, change only that thing, and check the same crop again.**

![Before and after: Iterative Zoom QA catches what full-frame review misses](docs/images/before-after-iterative-zoom-qa.jpg)

In this example, the full image felt close. But the zoom crop showed the central logo was wrong — it read like one stylized A instead of the intended double-AA mark. After iterating on that exact crop, the difference was fixed.

## Install

With the skills CLI:

```bash
npx skills add https://github.com/dannyshmueli/image-zoom-qa-skill
```

Or copy this repo into your agent's skills directory.

## What the skill does

1. Compare the full reference and current image.
2. Pick one suspicious region.
3. Generate a zoomed side-by-side crop board.
4. Write a concrete verdict: `PASS`, `PASS WITH NIT`, `FAIL`, or `UNCLEAR`.
5. Iterate the design.
6. Re-run the same crop until the difference is actually fixed.

Good visual QA is not “the vibe is close.” It is:

```text
02-logo-tight: FAIL — reference reads as a double-AA ribbon; current reads as one A.
Next change: replace generated logo with real/ref-crop geometry.
```

## What's included

```text
SKILL.md                         # Agent instructions
scripts/image_zoom_qa.py         # Deterministic crop-board generator
references/example-regions.json  # Example custom crop map
```

## Quick use

```bash
python3 -m pip install Pillow
python3 scripts/image_zoom_qa.py \
  --reference path/to/reference.png \
  --current path/to/current.png \
  --out image-zoom-qa \
  --canvas-size 1080
```

Outputs:

```text
image-zoom-qa/00-image-zoom-qa-index.jpg
image-zoom-qa/01-center-subject.jpg
image-zoom-qa/02-subject-tight.jpg
...
```

## Custom regions

Create `regions.json`:

```json
{
  "01-logo-tight": [390, 285, 695, 575],
  "02-platform-contact": [330, 430, 750, 700],
  "03-right-dock-icons": [850, 215, 1035, 760]
}
```

Run:

```bash
python3 scripts/image_zoom_qa.py \
  --reference ref.png \
  --current current.png \
  --out image-zoom-qa \
  --regions regions.json
```

## When to use it

Use Iterative Zoom QA when:

- your AI agent says the image is close, but your eye says something is off,
- generated images must match a reference,
- a video poster or UI screenshot needs aesthetic QA,
- logos, shadows, icons, text, seams, or subtle layout details matter.

## License

MIT
