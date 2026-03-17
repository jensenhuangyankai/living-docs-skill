---
name: living-docs-bootstrap
description: Bootstrap a source-linked living documentation system for an existing repository. Create a docs/ tree, design and architecture docs, feature docs with source_files globs, and a repeatable update path. Use when the user wants to set up living docs or design docs in a repo for the first time.
---

# Living Docs Bootstrap

Create the initial living-docs system for a repository, then leave behind a
clear path for future updates.

## When to Use

- The repository has no structured design docs yet
- The user wants self-updating or source-linked docs
- The team wants `docs/` to reflect architecture, features, and code ownership

## Workflow

1. Analyze the repository using [analysis-checklist.md](references/analysis-checklist.md).
2. Plan the document tree using [doc-tree.md](references/doc-tree.md).
3. Create only the docs the project actually needs.
4. Load templates one at a time from `references/templates/`. Do not read every
   template unless the repo truly needs them.
5. Scaffold the folder structure with `scripts/scaffold-docs.sh` when helpful,
   then fill the generated files with project-specific content.
6. Install an update path:
   - Prefer installing the sibling `living-docs-update` skill.
   - Otherwise copy the template from
     `../living-docs-update/references/update-skill-template.md`.
   - Use [install-targets.md](references/install-targets.md) for target paths.
7. Verify that every doc has valid frontmatter and that `source_files` globs
   match real source files.

## Template Map

- Main index: [design-index.md](references/templates/design-index.md)
- Architecture docs: [architecture.md](references/templates/architecture.md)
- Service docs: [service.md](references/templates/service.md)
- Feature docs: [feature.md](references/templates/feature.md)
- UI docs: [ui-pages.md](references/templates/ui-pages.md) and
  [ui-components.md](references/templates/ui-components.md)
- Change log: [changelog.md](references/templates/changelog.md)
- Optional build order: [build-order.md](references/templates/build-order.md)

## Output Rules

- Adapt the docs to the actual repository. Do not fill templates mechanically.
- Keep design intent, architecture, and key flows; avoid huge API catalogs.
- Every source-linked doc must include `source_files`.
- Prefer a smaller accurate docs set over a large generic one.

## Report

End with:

```text
Living Docs Bootstrapped
========================
Documents created: X
Update path installed: <path or skill>
Key source areas covered:
- <glob or path>
- <glob or path>
```
