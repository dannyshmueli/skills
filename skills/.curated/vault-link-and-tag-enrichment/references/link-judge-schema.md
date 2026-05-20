# Link Judge Schema

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

Auto-add only score >= 4, low risk, clear placement.

Auto-remove only score <= 1, low risk, and broken/duplicate/archived/obvious keyword garbage.
