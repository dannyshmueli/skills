# Frontmatter Policy

Keep Obsidian Properties human-readable.

Use:

```yaml
vault_scan: reviewed | needs-human | skipped
vault_scanned_at: YYYY-MM-DD
```

Do not use noisy scan telemetry fields:

```yaml
backlink_scan_agent: ...
backlink_scan_version: ...
backlink_scan_notes: ...
link_scan_status: ...
tag_scan_status: ...
link_scan_notes: ...
tag_scan_notes: ...
```

Detailed link judgments belong in a log or sidecar report, not every note's frontmatter.
