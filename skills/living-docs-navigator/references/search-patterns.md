# Search Patterns

Use these patterns to keep context small.

## Start Broad

- `find docs -maxdepth 2 -type f | sort`
- `grep -Ril "<keyword>" docs`

## If the Task Is Architectural

- Read `docs/DESIGN.md`
- Read `docs/architecture/system-overview.md`
- Then read one deeper architecture doc if needed

## If the Task Maps to a Feature

- Search `docs/features/`
- Read only the matching feature doc
- Use its `source_files` frontmatter to jump to code

## If the Task Maps to a Service

- Search `docs/services/`
- Read only the matching service doc

## If Code Already Changed

- Use `living-docs-update/scripts/list-changed-files.sh`
- Then use `living-docs-update/scripts/match-source-files.py` to find affected
  docs
