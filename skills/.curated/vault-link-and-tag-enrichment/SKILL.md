---
name: vault-link-and-tag-enrichment
description: Use when an AI agent should conservatively improve an Obsidian or markdown knowledge vault by judging existing wikilinks, adding high-value backlinks, repairing tags against a known taxonomy, and keeping frontmatter clean instead of creating graph-density noise.
version: 1.0.0
author: Danny Shmueli and Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [obsidian, markdown, backlinks, wikilinks, tags, knowledge-management, vault-enrichment]
    related_skills: []
---

# Vault Link and Tag Enrichment

## Overview

Vault Link and Tag Enrichment is a conservative knowledge-management workflow for AI agents working inside Obsidian, LLM Wiki, Foam, or any markdown vault that uses wikilinks and frontmatter.

The goal is not graph density. The goal is future comprehension: fewer stronger links, cleaner tags, and notes that become easier to rediscover without turning Properties/frontmatter into machine sludge.

Use an LLM as a judge, not as a keyword linker. A good enrichment pass reads the note, understands the thesis, searches the vault for real conceptual neighbors, rejects weak matches, applies only safe edits, and records detailed reasoning outside per-note Properties.

## When to Use

Use this skill when:

- The user asks to enrich backlinks, wikilinks, tags, or note relationships in a markdown vault.
- A vault has many orphan or underlinked durable notes.
- A cron job should improve 1-3 notes per run without making noisy changes.
- The user wants to clean old scan frontmatter fields left by agents.
- The agent is reviewing a selected link/tag in Obsidian and deciding keep, add, remove, replace, or needs-human.
- A raw capture, bookmark, transcript, meeting note, or research note has produced a durable concept/query/entity page that now needs links into the graph.

Do not use this skill for:

- Bulk automatic keyword linking.
- Creating new tags without a schema or user approval.
- Rewriting note substance.
- Reclassifying personal or strategic notes aggressively.
- Touching private vaults without explicit user permission and a clear scope.

## Core Principle

Optimize future comprehension, not graph density.

Prefer:

- one strong sibling link over five keyword matches;
- one precise Related entry over scattered inline links;
- human-readable frontmatter over agent telemetry;
- needs-human proposals over risky automatic edits.

Reject links that are only connected because two notes share a trendy word.

## Scope Defaults

Process a small batch per run.

- Manual pilot: 1-3 notes.
- Cron run: max 3 notes.
- User-selected link or note: process only the selected object unless asked to expand.

Skip by default:

- `raw/`
- `assets/`
- `.obsidian/`
- `.git/`
- `node_modules/`
- generated files
- oversized files unless selected by the user

Prefer durable notes such as:

- `concepts/`
- `entities/`
- `queries/`
- `comparisons/`
- `backlogs/`
- `projects/`
- `notes/`

Adapt these paths to the vault's structure. Do not assume the user's vault matches yours.

## Required Orientation

Before broad work, read the vault's local conventions if they exist:

1. `AGENTS.md`, `CLAUDE.md`, or similar agent instructions.
2. `SCHEMA.md`, `TAGS.md`, or any taxonomy note.
3. `index.md`, `README.md`, or map-of-content pages.
4. Recent `log.md` or changelog if edits will be made.

For a selected single link/tag, you may read the target note and candidate note directly after minimal orientation.

## Note Selection for Cron

Select up to 3 notes. Prioritize:

1. Recently created durable notes missing the compact scan field.
2. Recently updated durable notes whose scan date is stale.
3. Notes with fewer than 2 outbound durable links.
4. Orphan-ish notes with low inbound links.
5. Durable pages created from raw/bookmark/transcript material.
6. Notes in active project/backlog areas that benefit from human navigation.

Avoid repeatedly scanning the same note just because it is popular.

## Per-Note Workflow

For each selected note:

1. Read the full note.
2. Extract:
   - thesis;
   - durable entities, concepts, workflows, and decisions;
   - current outbound links;
   - backlinks/inbound links if easy to compute;
   - Related section;
   - frontmatter tags;
   - source refs.
3. Disenrichment pass:
   - judge existing links for keep, remove, replace, or needs-human;
   - detect broken, duplicate, stale, archived, or keyword-only links.
4. Enrichment search pass:
   - create 5-10 targeted searches from the note's thesis and entities;
   - search titles and content;
   - read candidate pages before linking.
5. Candidate judge pass:
   - accept/reject/maybe each proposed link using the schema below.
6. Tag judge pass:
   - compare existing/proposed tags against the vault taxonomy.
7. Apply only safe edits.
8. Update compact scan frontmatter.
9. Put detailed judge results in a log or sidecar report, not note Properties.
10. Verify changed lines and log/report entries.

## Link Judge Schema

Use this schema for existing and proposed links:

```yaml
candidate_link: "[[path-or-title]]"
decision: keep | add | remove | replace | reject | maybe | needs-human
score: 1-5
relationship: parent | child | sibling | example | implementation | source | contrast | duplicate | broken | archived | stale-context | weak-keyword-match
placement: inline | related | frontmatter-source-only | none
reason: "one sentence"
risk: low | medium | high
replacement: null
```

Scoring guide:

- 5: obvious durable relationship; future reader benefits immediately.
- 4: strong relationship with clear placement.
- 3: plausible but not safe to auto-apply.
- 2: weak; usually reject or needs-human.
- 1: broken, duplicate, misleading, or keyword-only.

## Link Auto-Apply Rules

Auto-add only when:

- score >= 4;
- risk is low;
- placement is clear;
- the target note was read or is well-known from the vault index;
- max 3 new links per note unless the user explicitly asks for more.

Good placements:

- inline when the sentence already names the concept/entity;
- Related section when the relationship is useful but not part of the prose;
- source/frontmatter only when the link is provenance, not conceptual relationship.

Auto-remove only when:

- score <= 1;
- risk is low;
- reason is broken, duplicate, archived with known replacement, or clearly unrelated keyword-only link.

Needs-human when:

- score is 2-3;
- risk is medium/high;
- the link affects product thesis, career/interview framing, company strategy, or active plans;
- removal changes interpretation;
- the agent cannot inspect enough context.

Never remove a plausible strategic link just because it is not local to the current paragraph.

## Tag Judge Schema

```yaml
current_tags: []
decision: keep-tags | add-tags | propose-tags | needs-human
accepted_tags: []
maybe_tags: []
rejected_tags: []
reason: "one sentence"
risk: low | medium | high
```

## Tag Auto-Apply Rules

Auto-add tags only when:

- the tag already exists in the vault taxonomy or is clearly already used across the vault;
- confidence is high;
- the tag is central, not merely plausible;
- the note would be hard to find or misleading without it.

Do not auto-create new tags.

Do not auto-remove tags in v1 unless the tag is invalid against taxonomy and clearly accidental. Usually propose removals only.

## Frontmatter Policy

Keep frontmatter minimal. Obsidian Properties become unreadable if every scan writes many machine fields.

Use one compact status field:

```yaml
vault_scan: reviewed | needs-human | skipped
```

Only add a date if it is useful for cron selection:

```yaml
vault_scanned_at: YYYY-MM-DD
```

Do not write fields like:

```yaml
backlink_scan_agent: ...
backlink_scan_version: ...
backlink_scan_notes: ...
link_scan_status: ...
tag_scan_status: ...
link_scan_notes: ...
tag_scan_notes: ...
```

If older notes have noisy scan fields, clean them opportunistically when touching the note. Keep only `vault_scan` and optional `vault_scanned_at`.

Detailed judge results, kept/rejected links, tag reasoning, and proposals belong in:

- `log.md`, if the vault uses one;
- a sidecar report under `queries/`, `reports/`, or `.scratch/`;
- the agent's final report if no durable report is appropriate.

Not in every note's frontmatter.

## Cron Prompt Template

```text
Run conservative vault link/tag enrichment.
Vault: <absolute path>
Process up to 3 markdown notes.
Skip raw/, assets/, .obsidian/, .git/, node_modules/, generated files, and oversized files.
Orient with local agent instructions, schema/taxonomy, index/readme, and recent log if present.
For each note:
- judge existing links for keep/remove/replace;
- search for missing high-value links;
- read candidate targets before linking;
- judge candidate links;
- judge tags against taxonomy;
- auto-add only score >=4 low-risk links/tags;
- auto-remove only broken/duplicate/archived/obvious garbage links;
- never auto-create tags;
- write only compact vault_scan and optional vault_scanned_at in frontmatter;
- put detailed judge notes in log or sidecar report, not Properties/frontmatter;
- append a concise log entry only when files change;
- verify changed notes and log/report tail.
Return concise report: scanned, edited, added, removed, proposed, skipped.
```

## Example Selected-Link Judgment

Selected link:

`[[queries/groundcover/groundcover-ai-era-career-ladder-management-ic]]`

inside:

`concepts/ai-agent-manager-operating-model.md`

Judgment:

```yaml
candidate_link: "[[queries/groundcover/groundcover-ai-era-career-ladder-management-ic]]"
decision: keep
score: 5
relationship: sibling
placement: related
reason: "It connects agent-manager work to the AI-era career ladder idea that senior people manage through the work, not away from it."
risk: low
replacement: null
```

Do not remove this link during disenrichment.

## Common Pitfalls

1. Keyword soup. If two notes share a word but not a durable relationship, reject the link.
2. Frontmatter pollution. Agent telemetry belongs in logs or reports, not Obsidian Properties.
3. Over-removal. A strategic link can be valid even if it is not sentence-local.
4. Tag invention. New taxonomy needs human approval.
5. Batch greed. More than 3 notes per run creates sloppy judgment and noisy diffs.
6. Skipping target reads. Do not add a link to a candidate note you have not inspected unless it is canonical from the index.
7. Treating raw captures as durable notes. Raw material can inform enrichment, but durable concept/query/entity pages are usually the linking surface.

## Verification Checklist

- [ ] Local vault instructions/schema/index were checked when present.
- [ ] Selected notes are in scope and not generated/raw unless explicitly selected.
- [ ] Every added link has score >= 4, low risk, and clear placement.
- [ ] Every removed link is broken, duplicate, archived with known replacement, or obvious garbage.
- [ ] No new tags were invented.
- [ ] Frontmatter uses only compact scan fields.
- [ ] Detailed reasoning is outside per-note Properties.
- [ ] Changed notes were re-read or diffed.
- [ ] Log/report updated only when useful.
