# Propagation Rules

## Create a New Doc When

- a changed area has no matching doc through `source_files`
- a new feature, service, or architecture concern is now important enough to
  deserve its own doc
- adding a section to `docs/DESIGN.md` alone would hide important detail

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

- Prefer extending an existing matched doc before creating a new one.
- Update affected sections, not whole files.
- When a new doc is needed, create the smallest honest doc and add
  `source_files`.
- Keep diagrams when they are still directionally correct.
- Flag uncertainty instead of inventing architecture.
