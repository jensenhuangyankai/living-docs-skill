---
name: living-docs
description: One-install living-docs skill for bootstrapping, navigating, and updating source-linked design documentation. Use when the user wants a single skill that can create a docs system, load relevant docs with low context overhead, or keep docs synced after code changes.
---

# Living Docs

Single entrypoint for the living-docs workflow. Keep this skill installed when
you want one command surface but still want progressive disclosure.

## Choose the Mode

- **Bootstrap**: No living-docs system exists yet.
  Load [bootstrap.md](references/bootstrap.md).
- **Navigate**: The repo already has docs and you need context.
  Load [navigate.md](references/navigate.md).
- **Update**: Code changed and the docs must be synchronized.
  Load [update.md](references/update.md).

## Rules

- Pick one mode first. Do not load every reference file up front.
- Search first and read only the relevant docs or templates.
- Prefer the smallest accurate docs update over broad rewrites.

## Helpers

- Scaffold docs: `scripts/scaffold-docs.sh`
- List changed files: `scripts/list-changed-files.sh`
- Match changed files to docs: `scripts/match-source-files.py`
