---
name: image-zoom-qa
description: Use when visually comparing a generated design, screenshot, video poster, or UI iteration against a reference. Creates zoomed side-by-side crop boards so agents inspect exact regions like logos, shadows, alignment, seams, text, and data-flow instead of relying on vague full-frame impressions.
version: 1.0.0
author: Danny Shmueli and Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [iterative-zoom-qa, image-zoom-qa, visual-qa, image-comparison, design-review, screenshot-qa, video-qa]
    related_skills: [dogfood, gpt-image-2-prompting]
---

# Iterative Zoom QA

## Overview

Iterative Zoom QA is a visual-review workflow for comparing a current image against a reference at the places that actually matter.

Full-frame screenshots are deceptive. An AI agent can say a design “looks close” while missing the important difference: the logo is wrong, a platform seam is visible, shadows are square, icons are miscentered, or text has quietly rotated. Iterative Zoom QA forces the agent to crop suspicious regions, zoom them side-by-side, make a region-by-region verdict, change only the proven defect, and re-run the same crop before claiming the design is fixed.

Use it for product videos, generated hero images, landing pages, UI polish, brand asset compositing, and any task where small visual differences determine quality.

## When to Use

Use this skill when:

- Comparing a generated image against a reference image.
- Reviewing a video poster frame or animation still against a target style.
- The user says something like “look closer,” “compare it to this,” “the logo is wrong,” “the shadows are weird,” “it’s not quite there,” or “zoom in.”
- The design includes delicate details: logos, icon fidelity, shadows, rounded cards, 3D platforms, transparent assets, text legibility, seams, or data-flow lines.
- Prior full-frame QA missed an issue.

Do **not** use it as a replacement for human taste. The crop boards reveal details; you still need to judge them honestly.

Naming note: the repository and installable skill use `image-zoom-qa` for compatibility, but the public-facing workflow is **Iterative Zoom QA** because the iteration loop is the point.

## Core Principle

Do not ask “does the whole image look close?” first.

Ask:

1. Which exact regions are likely to fail?
2. What does the reference do in those regions?
3. What does the current image do differently?
4. Is the difference acceptable, intentional, or a defect?
5. What specific change should the next iteration make?

## Workflow

### 1. Start with a full-frame comparison

Create or inspect a side-by-side full-frame comparison first. Use it only to identify suspect regions.

Common suspect regions:

- central logo / brand mark
- object-platform contact point
- card shadows and halos
- text-bearing surfaces
- right/left docks or sidebars
- icon centering
- data-flow lines, arrows, or animated packets
- seams around composited generated assets
- background gradients and edge artifacts

### 2. Define crop regions

Use named crop boxes in image coordinates:

```json
{
  "01-center-logo-platform": [315, 245, 765, 690],
  "02-logo-tight": [390, 285, 695, 575],
  "03-platform-tight": [330, 430, 750, 700],
  "04-right-dock-icons": [850, 215, 1035, 760]
}
```

Use stable, descriptive names. Prefix with numbers so review order is obvious.

### 3. Generate zoom boards

From a repo containing this skill:

```bash
python3 scripts/image_zoom_qa.py \
  --reference path/to/reference.png \
  --current path/to/current.png \
  --out path/to/image-zoom-qa \
  --canvas-size 1080
```

With custom regions:

```bash
python3 scripts/image_zoom_qa.py \
  --reference path/to/reference.png \
  --current path/to/current.png \
  --out path/to/image-zoom-qa \
  --regions regions.json \
  --canvas-size 1080
```

One-off extra region:

```bash
python3 scripts/image_zoom_qa.py \
  --reference ref.png \
  --current current.png \
  --out qa \
  --add-region logo-tight=390,285,695,575
```

The script writes:

- `00-image-zoom-qa-index.jpg` — overview contact sheet.
- one `.jpg` per crop region, with reference/current/diff panels.

### 4. Inspect each zoom board

For each board, write a terse verdict:

```text
02-logo-tight: FAIL
Reference reads as a double-AA ribbon. Current reads as one A. Inner cutout and overlap are wrong.
Next change: replace generated logo with real/ref-crop geometry; do not trust full-frame similarity.
```

Good verdict labels:

- `PASS` — close enough; no action.
- `PASS WITH NIT` — acceptable, but note minor difference.
- `FAIL` — must change.
- `UNCLEAR` — crop is insufficient; create a tighter or wider crop.

### 5. Iterate from the crop verdicts

Only change what the zoom boards prove is wrong. Avoid broad style thrashing.

After changes:

1. render or export a new current image,
2. regenerate the same zoom boards,
3. compare the old failure region again,
4. keep iterating until the exact region passes.

## What to Look For

### Logo and brand marks

Check:

- Does the logo read as the correct glyph on first glance?
- Are there missing strokes, extra strokes, or generated hallucinations?
- Are inner cutouts and overlaps correct?
- Is the mark too flat, too glossy, or incorrectly beveled?
- Is there an unwanted square or rectangular backplate?
- Are transparent edges clean, or is there a halo from stale RGB pixels under alpha?

Common failure: generated image models produce something that “feels like” the logo but changes its actual geometry. Treat that as a fail.

### Platform and object contact

Check:

- Does the object physically sit on the surface?
- Is the contact shadow directly under it and subtle?
- Does the platform have visible thickness if the reference has thickness?
- Is the crop pasted in, or does it blend into the scene?
- Are there hard rectangle edges from a composited asset?

### Shadows

Check:

- Are shadows rounded and aligned with the object shape?
- Are there square grey halos around cards?
- Is the blur warm and natural, not dirty or muddy?
- Are shadows too heavy relative to the reference?

### Text and surfaces

Check:

- Is text upright and readable?
- Did a transform rotate text sideways or 90 degrees?
- Are cards too large, too small, or stealing focus?
- Is tilt subtle and depth-like rather than arbitrary rotation?

### Icons and sidebars

Check:

- Are icons correct, centered, and consistently sized?
- Does the sidebar feel integrated or pasted on?
- Is it visually heavier than the primary subject?

### Flow lines and animation stills

Check:

- Do lines clearly connect source to destination?
- Are animated packets visible in representative frames?
- Do lines look like intentional data flow, not random orbit decoration?
- Are endpoints positioned on meaningful objects?

## Recommended Artifact Set

For a polished visual iteration, save:

```text
reference-vs-current.jpg
image-zoom-qa/00-image-zoom-qa-index.jpg
image-zoom-qa/01-center-logo-platform.jpg
image-zoom-qa/02-logo-tight.jpg
image-zoom-qa/03-platform-tight.jpg
image-zoom-qa/04-card-shadow.jpg
image-zoom-qa/05-right-dock-icons.jpg
image-zoom-qa/06-flow-lines.jpg
```

For video work, also save representative frames:

```text
frame-start.png
frame-middle.png
frame-end.png
motion-contact-sheet.jpg
```

Zoom QA validates spatial quality. Motion contact sheets validate animation quality.

## Script

This repository includes a reusable script:

```text
scripts/image_zoom_qa.py
```

Dependencies:

```bash
python3 -m pip install Pillow
```

Minimal use:

```bash
python3 scripts/image_zoom_qa.py --reference ref.png --current current.png --out image-zoom-qa
```

## Common Pitfalls

1. **Using only full-frame QA.** Full-frame views hide logo and compositing defects. Always crop likely failure points.

2. **Trusting pixel similarity too much.** A high similarity score can be inflated by a shared background. Use it as a hint, not a verdict.

3. **Cropping too loosely.** If a defect is about a logo inner cutout, create a tight logo crop. If it is about seating on a platform, create a wider platform crop too.

4. **Cropping too tightly.** A tight crop may hide whether the element feels integrated. Pair tight crops with context crops.

5. **Changing too many things at once.** Zoom QA should lead to precise edits. Fix the proven failure, then re-run the same crop.

6. **Accepting generated logo approximations.** If brand geometry matters, “close vibe” is not enough. Verify the actual shape.

7. **Ignoring asset transparency.** PNGs can have transparent pixels with stale RGB values that create halos when resized. If you see haze, inspect alpha and RGB under alpha.

8. **Forgetting video motion.** For video, inspect start/mid/end frames and adjacent-frame differences. Image Zoom QA is for image quality, not motion by itself.

## Verification Checklist

- [ ] Reference and current images are the same size, or normalized with `--canvas-size`.
- [ ] Crop regions cover both tight details and wider context.
- [ ] `00-image-zoom-qa-index.jpg` exists.
- [ ] Every suspicious region has a named board.
- [ ] Each board has a PASS / PASS WITH NIT / FAIL / UNCLEAR verdict.
- [ ] Any FAIL has one specific next change.
- [ ] The same failed crop is regenerated after the fix.
- [ ] Final response links to the full-frame comparison and the most important zoom boards.

## Example Review Format

```text
Image Zoom QA verdict:
- 01-center-logo-platform: PASS WITH NIT — good overall; current sits 8px lower than reference.
- 02-logo-tight: PASS — glyph geometry preserved, no obvious seam.
- 04-card-shadow: FAIL — current has a square grey halo; reference has rounded warm shadow.
- 06-flow-lines: FAIL — packets are visible, but endpoints do not clearly hit the analytics card.

Next iteration: fix card shadow renderer and reroute flow endpoints. Do not touch the logo.
```
