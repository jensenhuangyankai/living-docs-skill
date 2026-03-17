# Update Mode

Use this mode after code changes when the repository already has source-linked
living docs.

## Workflow

1. Run `scripts/list-changed-files.sh`.
2. Run `scripts/match-source-files.py <changed-file> [...]` to find affected
   docs.
3. Read only the matched docs and the changed source files.
4. Update the smallest necessary sections and refresh `last_updated`.
5. Update `docs/DESIGN.md` only for major capability or architecture changes.
6. Append a concise session entry to `docs/CHANGELOG.md`.

## Use the Focused Skill for More Detail

If installed, load:

- `../living-docs-update/SKILL.md`
