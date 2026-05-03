# Danny's Agent Skills

Reusable skills for AI agents.

Install from this repo:

```bash
npx skills add dannyshmueli/skills --list
npx skills add dannyshmueli/skills --skill negotiate
npx skills add dannyshmueli/skills --skill image-zoom-qa
```

Install all skills from this repo:

```bash
npx skills add dannyshmueli/skills --all
```

## Skills

### negotiate

Personal negotiation advisor with three modes:

- `prep` - prepare before pricing or salary call
- `live` - write response during negotiation
- `analyze` - debrief outcome and bias map after call

Covers pricing, commercial deals, freelance retainers, procurement, and salary negotiation. Uses BATNA, reservation point/red line, target price, ZOPA, anchoring, MESO packages, and cognitive-bias checks.

Example:

```text
/negotiate prep
I am negotiating salary for a Senior Product Manager role.
Offer: 42,000 ILS monthly base + 0.15% options.
Target: 49,000 ILS or equivalent total comp.
Red line: 43,500 ILS if title/level and equity improve.
BATNA: current role at 40,000 ILS plus one active interview.
Variables: base, signing bonus, equity, title, remote days, 6-month review.
```

### image-zoom-qa

Visual QA loop for AI-generated images, screenshots, UI, and video frames. Creates zoomed side-by-side crop boards so agents inspect exact regions instead of saying “close enough.”

Example:

```bash
python3 -m pip install -r skills/.curated/image-zoom-qa/requirements.txt
python3 skills/.curated/image-zoom-qa/scripts/image_zoom_qa.py \
  --reference path/to/reference.png \
  --current path/to/current.png \
  --out image-zoom-qa \
  --canvas-size 1080
```

## License

Each skill carries its own license file.
