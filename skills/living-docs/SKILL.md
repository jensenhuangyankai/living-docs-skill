---
name: living-docs
description: Bootstrap, navigate, update, and align source-linked living docs. Use when the user mentions docs, design docs, architecture docs, keeping docs in sync, asks what docs already exist, needs missing docs created, or wants to grill, stress-test, or clarify a codebase plan before implementation.
---

# Living Docs

Single entrypoint for the living-docs workflow. It can also align a proposed
change against the repo's documented language before implementation begins.

## Infer the Mode

Choose the mode from the request and repository state. Do not ask the user to
pick unless the situation is genuinely ambiguous.

- **Align**: The user has a plan, feature idea, or design direction and wants
  it grilled, stress-tested, clarified, or aligned before building.
  Load [align.md](references/align.md).
- **Bootstrap**: No living-docs system exists yet.
  Load [bootstrap.md](references/bootstrap.md).
- **Navigate**: The repo already has docs and you need context.
  Load [navigate.md](references/navigate.md).
- **Update**: Code changed and the docs must be synchronized.
  Load [update.md](references/update.md).

## Rules

- Pick one mode first. Do not load every reference file up front.
- Treat "docs", "design docs", "architecture docs", and similar wording as a
  likely trigger for this skill.
- Treat "grill", "stress-test", "align before build", "clarify the plan", and
  "interview me" as Align mode triggers when a codebase is involved.
- Search first and read only the relevant docs or templates.
- Prefer the smallest accurate docs update over broad rewrites.

## Helpers

- Scaffold docs: `scripts/scaffold-docs.sh`
- List changed files: `scripts/list-changed-files.sh`
- Match changed files to docs: `scripts/match-source-files.py`
