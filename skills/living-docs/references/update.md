# Update Mode

Use this mode after code changes when the repository already has source-linked
living docs.

## Workflow

1. Run `scripts/list-changed-files.sh`.
2. Run `scripts/match-source-files.py <changed-file> [...]` to find affected
   docs.
3. Read only the matched docs and the changed source files.
4. If no doc matches but the change clearly introduces a new feature, service,
   or architecture area, create the smallest missing doc needed.
5. Apply [propagation-rules.md](update/propagation-rules.md).
6. Update the smallest necessary sections and refresh `last_updated`.
7. Update `docs/DESIGN.md` only for major capability or architecture changes.
8. Append a concise session entry to `docs/CHANGELOG.md`.

## Rules

- Change the smallest set of sections possible.
- Create a new doc only when the existing tree no longer covers the changed
  area.
- Preserve frontmatter keys.
- Use [update-instructions-template.md](update/update-instructions-template.md)
  only when a repo-local maintenance file is needed.
