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

Return concise report:
- scanned
- edited
- added links/tags
- removed links
- needs-human proposals
- skipped
