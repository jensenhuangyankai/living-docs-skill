# Bootstrap Mode

Use this mode when the repository has no structured living-docs system yet.

## Workflow

1. Analyze the repository:
   - project identity
   - services or packages
   - major features
   - data model
   - auth, deployment, and existing docs
2. Create the smallest honest doc tree under `docs/`.
3. Add `docs/DESIGN.md` and `docs/CHANGELOG.md`.
4. Add architecture, service, feature, and UI docs only when they actually
   exist in the repository.
5. Add `source_files` frontmatter to source-linked docs.
6. Leave behind an update path so the docs can be maintained later.

## Use the Focused Skill for More Detail

If you need the deeper bootstrap playbook, load:

- `../living-docs-bootstrap/SKILL.md`

If that focused skill is not installed, use the logic above and keep the docs
set compact.
