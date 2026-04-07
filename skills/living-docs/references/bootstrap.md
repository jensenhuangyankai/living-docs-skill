# Bootstrap Mode

Use this mode when the repository has no structured living-docs system yet.

## Workflow

1. Analyze the repository with [analysis-checklist.md](bootstrap/analysis-checklist.md).
2. Plan the smallest honest doc tree with [doc-tree.md](bootstrap/doc-tree.md).
3. Add `docs/DESIGN.md` and `docs/CHANGELOG.md`.
4. Add architecture, service, feature, and UI docs only when they actually
   exist in the repository.
5. Load templates only as needed from [templates.md](bootstrap/templates.md).
6. Add `source_files` frontmatter to source-linked docs.
7. Leave behind a reusable maintenance path using
   [install-targets.md](bootstrap/install-targets.md).

## Rules

- Prefer a smaller accurate docs set over a large generic one.
- Reuse the bundled `scripts/scaffold-docs.sh` helper when it saves time.
- Do not load every template unless the repository truly needs them.
