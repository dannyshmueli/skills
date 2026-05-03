#!/usr/bin/env python3
"""Create side-by-side zoom QA boards for comparing reference vs current images.

This script is intentionally boring: deterministic crops, big side-by-side boards,
and an index sheet. It helps agents stop judging full screenshots too broadly and
instead inspect the specific regions where visual quality usually fails.

Examples:
  python3 scripts/image_zoom_qa.py \
    --reference reference.png \
    --current current.png \
    --out image-zoom-qa

  python3 scripts/image_zoom_qa.py \
    --reference ref.png --current cur.png --out qa \
    --regions regions.json

regions.json:
{
  "hero-logo": [300, 180, 760, 620],
  "right-sidebar": [850, 180, 1040, 820]
}
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, Iterable, Tuple

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageStat

Box = Tuple[int, int, int, int]

DEFAULT_REGIONS: Dict[str, Box] = {
    "01-center-subject": (300, 220, 780, 720),
    "02-subject-tight": (390, 280, 700, 590),
    "03-top-card-shadow": (330, 35, 690, 270),
    "04-left-elements": (60, 250, 420, 720),
    "05-right-elements": (700, 220, 1035, 820),
    "06-bottom-elements": (260, 640, 850, 980),
    "07-flow-lines": (500, 300, 880, 640),
}


def load_font(size: int = 18) -> ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def parse_box(raw: str) -> Box:
    parts = [int(p.strip()) for p in raw.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be x1,y1,x2,y2")
    x1, y1, x2, y2 = parts
    if x2 <= x1 or y2 <= y1:
        raise argparse.ArgumentTypeError("box must satisfy x2>x1 and y2>y1")
    return x1, y1, x2, y2


def load_regions(path: str | None, extra: Iterable[str]) -> Dict[str, Box]:
    regions = dict(DEFAULT_REGIONS)
    if path:
        data = json.loads(Path(path).read_text())
        regions = {str(k): tuple(map(int, v)) for k, v in data.items()}  # type: ignore[assignment]
    for item in extra:
        if "=" not in item:
            raise SystemExit(f"--add-region must be name=x1,y1,x2,y2, got: {item}")
        name, raw_box = item.split("=", 1)
        regions[name] = parse_box(raw_box)
    return regions


def resize_pair(reference: Image.Image, current: Image.Image, canvas_size: int | None) -> tuple[Image.Image, Image.Image]:
    ref = reference.convert("RGB")
    cur = current.convert("RGB")
    if canvas_size:
        ref = ref.resize((canvas_size, canvas_size), Image.Resampling.LANCZOS)
        cur = cur.resize((canvas_size, canvas_size), Image.Resampling.LANCZOS)
    elif ref.size != cur.size:
        cur = cur.resize(ref.size, Image.Resampling.LANCZOS)
    return ref, cur


def crop_metrics(ref_crop: Image.Image, cur_crop: Image.Image) -> tuple[float, float]:
    diff = ImageChops.difference(ref_crop.convert("RGB"), cur_crop.convert("RGB"))
    stat = ImageStat.Stat(diff)
    mae = sum(stat.mean) / 3.0
    # RMSE over RGB channels.
    sq = sum(v for v in stat.rms) / 3.0
    return mae, sq


def make_board(
    ref: Image.Image,
    cur: Image.Image,
    out_dir: Path,
    region_name: str,
    box: Box,
    panel_width: int,
    show_diff: bool,
) -> Path:
    x1, y1, x2, y2 = box
    w, h = ref.size
    x1, x2 = max(0, x1), min(w, x2)
    y1, y2 = max(0, y1), min(h, y2)
    box = (x1, y1, x2, y2)

    rc = ref.crop(box)
    cc = cur.crop(box)
    scale = panel_width / max(rc.width, 1)
    panel_h = max(1, int(rc.height * scale))
    rc_big = rc.resize((panel_width, panel_h), Image.Resampling.LANCZOS)
    cc_big = cc.resize((panel_width, panel_h), Image.Resampling.LANCZOS)

    panels = [rc_big, cc_big]
    labels = ["REFERENCE", "CURRENT"]
    if show_diff:
        diff = ImageChops.difference(rc, cc).convert("L")
        diff = diff.point(lambda p: min(255, p * 4))
        diff_rgb = Image.new("RGB", diff.size, (32, 25, 20))
        heat = Image.new("RGB", diff.size, (255, 113, 60))
        diff_rgb.paste(heat, mask=diff)
        panels.append(diff_rgb.resize((panel_width, panel_h), Image.Resampling.LANCZOS))
        labels.append("DIFF x4")

    gap = 32
    header = 82
    footer = 52
    bg = (246, 240, 228)
    total_w = panel_width * len(panels) + gap * (len(panels) - 1)
    out = Image.new("RGB", (total_w, header + panel_h + footer), bg)
    d = ImageDraw.Draw(out)
    f = load_font(18)
    fb = load_font(24)
    small = load_font(15)

    mae, rmse = crop_metrics(rc, cc)
    d.text((16, 13), region_name, fill=(28, 25, 20), font=fb)
    d.text((16, 48), f"crop {box}  |  MAE {mae:.1f}  RMSE {rmse:.1f}", fill=(108, 88, 58), font=small)

    x = 0
    for label, panel in zip(labels, panels):
        out.paste(panel, (x, header))
        d.text((x + 16, 58), label, fill=(70, 58, 40), font=f)
        x += panel_width + gap
        if x < total_w:
            d.line((x - gap // 2, header, x - gap // 2, header + panel_h), fill=(214, 200, 174), width=2)

    d.text((16, header + panel_h + 16), "Judge geometry, seams, shadows, spacing, legibility — not just full-frame vibe.", fill=(118, 99, 72), font=small)
    out_path = out_dir / f"{region_name}.jpg"
    out.save(out_path, quality=94)
    return out_path


def make_index(paths: list[Path], out_dir: Path) -> Path:
    thumbs = []
    for p in paths:
        im = Image.open(p).convert("RGB")
        im.thumbnail((390, 230), Image.Resampling.LANCZOS)
        thumbs.append((p, im.copy()))

    cols = 2
    cell_w, cell_h = 440, 294
    rows = math.ceil(len(thumbs) / cols)
    out = Image.new("RGB", (cols * cell_w, rows * cell_h + 60), (246, 240, 228))
    d = ImageDraw.Draw(out)
    f = load_font(15)
    fb = load_font(24)
    d.text((16, 16), "Image Zoom QA index", fill=(28, 25, 20), font=fb)

    for i, (p, im) in enumerate(thumbs):
        col = i % cols
        row = i // cols
        x = col * cell_w + 18
        y = 60 + row * cell_h
        d.text((x, y), p.stem, fill=(60, 50, 38), font=f)
        out.paste(im, (x, y + 28))

    idx = out_dir / "00-image-zoom-qa-index.jpg"
    out.save(idx, quality=92)
    return idx


def main() -> None:
    ap = argparse.ArgumentParser(description="Create zoomed side-by-side visual QA boards.")
    ap.add_argument("--reference", required=True, help="Reference image path")
    ap.add_argument("--current", required=True, help="Current image path")
    ap.add_argument("--out", required=True, help="Output directory")
    ap.add_argument("--regions", help="Optional JSON object mapping region names to [x1,y1,x2,y2]")
    ap.add_argument("--add-region", action="append", default=[], help="Add/override one region: name=x1,y1,x2,y2")
    ap.add_argument("--canvas-size", type=int, help="Resize both images to square canvas before cropping, e.g. 1080")
    ap.add_argument("--panel-width", type=int, default=620, help="Width of each zoom panel")
    ap.add_argument("--no-diff", action="store_true", help="Hide amplified diff panel")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    ref_raw = Image.open(args.reference)
    cur_raw = Image.open(args.current)
    ref, cur = resize_pair(ref_raw, cur_raw, args.canvas_size)
    regions = load_regions(args.regions, args.add_region)

    paths = []
    for name, box in regions.items():
        paths.append(make_board(ref, cur, out_dir, name, box, args.panel_width, not args.no_diff))
    idx = make_index(paths, out_dir)

    print(idx)
    for p in paths:
        print(p)


if __name__ == "__main__":
    main()
