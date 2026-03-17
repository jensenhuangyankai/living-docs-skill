# Propagation Rules

## Update the Matched Doc When

- its `source_files` globs match a changed file
- a section became stale because interfaces or behavior changed
- configuration, schema, or ownership changed

## Update `docs/DESIGN.md` When

- a new feature area appears
- an existing feature is removed or renamed
- service boundaries change
- architecture or deployment changes affect the top-level summary

## Update `docs/CHANGELOG.md` When

- any documentation file changes
- a major change needs review or follow-up

## Prefer Minimal Edits

- Update affected sections, not whole files.
- Keep diagrams when they are still directionally correct.
- Flag uncertainty instead of inventing architecture.
