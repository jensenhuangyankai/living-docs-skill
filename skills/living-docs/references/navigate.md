# Navigate Mode

Use this mode when the repo already has living docs and the goal is to load
only the context relevant to the task.

## Workflow

1. Search `docs/` by keyword or path.
2. Read `docs/DESIGN.md` only if top-level orientation is needed.
3. Read the matching feature, service, or architecture docs.
4. Use `source_files` frontmatter to jump from docs to code.

## Search Patterns

- `find docs -maxdepth 2 -type f | sort`
- `grep -Ril "<keyword>" docs`

## Use the Focused Skill for More Detail

If installed, load:

- `../living-docs-navigator/SKILL.md`
