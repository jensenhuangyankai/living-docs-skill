# Update Instruction Template

Copy this into the target repository when the environment cannot install the
`living-docs-update` skill directly.

```markdown
---
name: living-docs-update
description: Update source-linked living docs after code changes. Analyze changed files, find affected docs from source_files globs, update the touched docs, and append a changelog entry.
---

# Living Docs Update

## When to Use

- At the end of an implementation session
- After merging or rebasing a branch with meaningful code changes
- When the user asks to update living docs or design docs

## Workflow

1. Gather changed files from git history or the working tree.
2. Match changed files against `source_files` globs in `docs/**/*.md`.
3. Read only the affected docs and the source files that triggered them.
4. Update the smallest set of sections necessary.
5. Propagate major capability or architecture changes to `docs/DESIGN.md`.
6. Append a concise entry to `docs/CHANGELOG.md`.

## Rules

- Do not rewrite unaffected docs.
- Preserve frontmatter keys and update `last_updated`.
- Keep diagrams when the underlying architecture still exists.
- Flag structural uncertainty instead of inventing missing details.
```
