---
name: living-docs-navigator
description: Navigate an existing living-docs system with minimal context. Search docs first, then read only the design, architecture, feature, or service docs relevant to the task. Use when the repo already has living docs and the user needs context without loading everything.
---

# Living Docs Navigator

Use the repository's existing living docs without dragging the whole system into
context.

## When to Use

- The repo already has `docs/`
- The task needs project context before implementation
- The user asks what already exists, why something works a certain way, or
  which docs are relevant

## Workflow

1. Start from [search-patterns.md](references/search-patterns.md).
2. Search for matching docs by keyword, path, or `source_files`.
3. Read `docs/DESIGN.md` only if top-level orientation is needed.
4. Read only the specific architecture, feature, or service docs that match the
   task.
5. If code changed, use the sibling `living-docs-update` matching workflow to
   find impacted docs.

## Rules

- Search first, read second.
- Prefer 2-3 relevant docs over loading the whole tree.
- Check architecture docs before proposing design changes.
