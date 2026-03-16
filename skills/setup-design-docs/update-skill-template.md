# Update Design Docs Instruction Template

This is the template for the update instruction file that gets installed into the target repository. Copy this verbatim, adjusting only the project-specific examples in the report section if desired.

The install location depends on the AI coding environment — see Step 9 of the setup skill for the mapping table.

---

**Default install path:** `docs/UPDATE_INSTRUCTIONS.md`
**Cursor:** `.cursor/skills/update-design-docs/SKILL.md`
**Claude Code:** Append to `AGENTS.md`

```markdown
---
name: update-design-docs
description: Automated end-of-session instruction that analyzes git changes, identifies affected documentation via source_files globs, updates sub-documents, propagates to DESIGN.md index, and logs to CHANGELOG.md. Use when asked to "update design docs" or "update documentation" at the end of a work session.
---

# Update Design Documentation

## Description

Automated end-of-session skill that analyzes the day's git commits, identifies affected documentation, updates sub-documents, propagates changes to the main index, and logs changes.

## When to Use

Run this skill at the end of a work session when asked to "update design docs" or "update documentation."

## Instructions

Follow these steps in order:

### Step 1: Gather Changes

Run the following command to find today's commits and changed files:

\`\`\`bash
git log --since="midnight" --oneline --name-only
\`\`\`

If no commits today, check if there are any uncommitted changes:

\`\`\`bash
git diff --name-only
git diff --staged --name-only
\`\`\`

Collect all changed file paths into a list.

### Step 2: Build Reverse Index

Parse all `docs/**/*.md` files and read their YAML frontmatter `source_files` fields. Build a reverse index mapping source file globs to affected docs.

For each doc file under `docs/`:
1. Read the file
2. Extract the `source_files` YAML frontmatter block
3. For each glob pattern in source_files, check if any changed files match

Use glob matching logic:
- `src/components/feature/*` matches any file directly in that folder
- `src/server/api/routers/feature.ts` matches that exact file
- `db/migrations/*feature*` matches any migration file with "feature" in the name
- `services/worker/**/*` matches any file recursively in that folder

### Step 3: Identify Affected Documents

For each changed file, find which docs cover it. A doc covers a file if any of its `source_files` globs match the file path.

Group results:
\`\`\`
Changed file → [list of affected docs]
\`\`\`

If no docs are affected (e.g., changes only to specs/ or config files), report "No documentation updates needed" and stop.

### Step 4: Update Sub-Documents

For each affected doc:

1. **Read the current doc** content
2. **Read the changed source files** that triggered the match
3. **Determine what changed**:
   - If API routes/routers changed → update the **API Contracts** table
   - If UI components changed → update the **UI Components** section
   - If database migrations/models changed → update the **Data Model** section
   - If handler/controller files changed → update relevant sections (Architecture, User Flows)
   - If config/env files changed → update **Configuration** section
4. **Update relevant sections** while preserving the overall template structure
5. **Update the `last_updated` date** in the YAML frontmatter

### Step 5: Assess Propagation to DESIGN.md

Check if any sub-document changes are "major" — meaning:
- New sections were added or removed
- New features or capabilities described
- Architecture changes

If major changes detected:
1. Read `docs/DESIGN.md`
2. Find the corresponding feature summary in the Feature Index
3. Update the one-paragraph summary to reflect the change
4. Update `last_updated` in DESIGN.md frontmatter

### Step 6: Log Changes

Append an entry to `docs/CHANGELOG.md` with this format:

\`\`\`markdown
## YYYY-MM-DD

### [Session Summary]

- **[doc-path]**: [Brief description of what changed]
- **[doc-path]**: [Brief description of what changed]

> [Optional: Flag items needing human review]
\`\`\`

### Step 7: Report

Output a summary:

\`\`\`
Documentation Update Summary
=============================
Changed files analyzed: X
Documents updated: Y
  - docs/features/feature-name/design.md (API contracts updated)
  - docs/services/service-name.md (new handler added)
DESIGN.md updated: Yes/No
CHANGELOG.md updated: Yes

Items flagged for review:
  - [Any structural changes that need human verification]
\`\`\`

## Propagation Rules

| Change Type | Sub-Doc Update | DESIGN.md Update | CHANGELOG Entry |
|-------------|---------------|-------------------|-----------------|
| New API endpoint added | Update API Contracts table | No | Yes |
| New component added | Update UI Components tree | No | Yes |
| New feature section | Add section to sub-doc | Update feature summary | Yes (flagged) |
| Feature removed | Archive/remove sub-doc | Remove from feature index | Yes (flagged) |
| Schema change | Update Data Model section | No | Yes |
| New page/route | Update sub-doc + `ui/pages.md` | No | Yes |
| Architecture change | Update relevant arch doc | Update architecture summary | Yes (flagged) |

## Important Notes

- **Preserve template structure**: Never remove standard sections (Overview, Architecture, Data Model, API Contracts, UI Components, User Flows, Configuration, Related)
- **Keep Mermaid diagrams**: Update diagrams if the architecture changed; don't remove them
- **Source links**: When updating API contracts, include source file references
- **Don't touch specs/**: The `specs/` folder (if present) is implementation-focused and separate from this system
- **Frontmatter accuracy**: Ensure `source_files` globs still match after code reorganizations
- **Minimal changes**: Only update sections that are actually affected by the code changes
```
