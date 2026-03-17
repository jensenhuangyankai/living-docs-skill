---
name: living-docs-update
description: Update source-linked living docs after code changes. Use when the repo already has living docs and the user wants changed files mapped to affected docs, those docs updated, and a changelog entry appended.
---

# Living Docs Update

Keep an existing living-docs system in sync with code changes.

## When to Use

- The repository already has `docs/` with source-linked frontmatter
- The user asks to update living docs or design docs
- A work session ended and meaningful code changed

## Workflow

1. Gather changed files with `scripts/list-changed-files.sh`.
2. Match changed files to docs with `scripts/match-source-files.py`.
3. Read only the affected docs plus the source files that triggered them.
4. Apply the update rules from [propagation-rules.md](references/propagation-rules.md).
5. If the repository needs a portable text version of this workflow, copy
   [update-skill-template.md](references/update-skill-template.md) into the
   target repo.

## Update Rules

- Change the smallest set of sections possible.
- Preserve frontmatter and update `last_updated`.
- Propagate only major capability or architecture shifts to `docs/DESIGN.md`.
- Append a concise session entry to `docs/CHANGELOG.md`.

## Output

Report:

```text
Living Docs Updated
===================
Changed files analyzed: X
Docs updated: Y
DESIGN.md touched: Yes/No
CHANGELOG.md touched: Yes/No
```
