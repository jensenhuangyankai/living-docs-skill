# Update Instructions Template

Copy this into the target repository when the environment cannot install the
published `living-docs` skill directly.

```markdown
---
name: living-docs
description: Use when the repository already has source-linked living docs and the user mentions docs, design docs, architecture docs, asks to keep docs in sync after code changes, or needs missing docs created for new code areas.
---

# Living Docs

## Infer the Mode

- **Navigate**: The user needs context from existing docs.
- **Update**: Code changed and the docs must be synchronized.

## Navigate Workflow

1. Search `docs/` by keyword or path.
2. Read `docs/DESIGN.md` only if top-level orientation is needed.
3. Read only the matching feature, service, or architecture docs.
4. Use `source_files` frontmatter to jump from docs to code.

## Update Workflow

1. Gather changed files from git history or the working tree.
2. Match changed files against `source_files` globs in `docs/**/*.md`.
3. Read only the affected docs and the source files that triggered them.
4. If no doc matches but the change clearly introduces a new feature, service,
   or architecture area, create the smallest missing doc needed.
5. Update the smallest set of sections necessary.
6. Propagate major capability or architecture changes to `docs/DESIGN.md`.
7. Append a concise entry to `docs/CHANGELOG.md`.

## Rules

- Do not rewrite unaffected docs.
- Create a new doc only when the existing tree no longer covers the changed
  area.
- Preserve frontmatter keys and update `last_updated`.
- Keep diagrams when the underlying architecture still exists.
- Flag structural uncertainty instead of inventing missing details.
```
