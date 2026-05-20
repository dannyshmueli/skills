# Vault Link and Tag Enrichment

Conservative Obsidian / markdown vault enrichment for AI agents.

Use it to improve wikilinks, backlinks, and tags without turning your graph into keyword soup or stuffing machine telemetry into frontmatter.

## Install

```bash
npx skills add dannyshmueli/skills --skill vault-link-and-tag-enrichment
```

## What it does

- Reads local vault conventions before editing.
- Processes small batches, usually 1-3 notes.
- Judges existing wikilinks for keep/remove/replace.
- Searches for missing high-value links.
- Adds only high-confidence, low-risk links.
- Repairs tags against an existing taxonomy.
- Keeps frontmatter clean with compact scan fields only.
- Writes detailed reasoning to logs or sidecar reports, not Properties.

Core rule: optimize future comprehension, not graph density.

## Included references

```text
references/cron-prompt.md
references/frontmatter-policy.md
references/link-judge-schema.md
```

## License

MIT
