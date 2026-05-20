# Danny Shmueli Skills

Personal public skills for AI agents.

This repo is intentionally small. It contains the skills I want to maintain and invest in, not a mirror of the upstream skills catalog.

## Install

List available skills:

```bash
npx skills add dannyshmueli/skills --list
```

Install one skill:

```bash
npx skills add dannyshmueli/skills --skill vault-link-and-tag-enrichment
npx skills add dannyshmueli/skills --skill image-zoom-qa
```

Install all:

```bash
npx skills add dannyshmueli/skills --all
```

## Skills

### `vault-link-and-tag-enrichment`

Conservative Obsidian / markdown vault enrichment for agents.

Use it to improve wikilinks, backlinks, and tags without turning your graph into keyword soup or stuffing machine telemetry into frontmatter.

Good for:

- Obsidian vaults
- LLM Wiki-style markdown knowledge bases
- cron-based small-batch enrichment
- cleaning noisy scan frontmatter
- deciding whether a proposed wikilink should be kept, added, removed, replaced, or sent to human review

Core rule: optimize future comprehension, not graph density.

### `image-zoom-qa`

Iterative Zoom QA for visual comparison.

Use it when an AI agent says an image “looks close,” but small details matter: logos, shadows, seams, icons, text, alignment, or UI polish.

The skill includes a deterministic crop-board script so agents compare suspicious regions side-by-side instead of handwaving from a full-frame screenshot.

## Repo layout

```text
skills/.curated/
  vault-link-and-tag-enrichment/
    SKILL.md
    README.md
    references/
  image-zoom-qa/
    SKILL.md
    README.md
    scripts/image_zoom_qa.py
    references/example-regions.json
    assets/images/
```

## Development

List local skills:

```bash
npx --yes skills add . --list
```

Install one from local checkout for testing:

```bash
TMP=$(mktemp -d)
cd "$TMP"
npx --yes skills add /Users/danny/dev/skills --skill vault-link-and-tag-enrichment --agent codex -y --copy
```

Before pushing, verify:

```bash
npx --yes skills add . --list
```

## License

MIT
