# Install Targets

Use these locations when leaving behind a reusable update path.

## Preferred Option

Install the sibling `living-docs-update` skill in the target environment when
the environment supports installable skills.

## Fallback Paths

| Environment | Install Path |
|-------------|--------------|
| Cursor | `.cursor/skills/living-docs-update/SKILL.md` |
| Claude Code | `AGENTS.md` or `.claude/skills/living-docs-update/SKILL.md` |
| Codex | `.agents/skills/living-docs-update/SKILL.md` |
| Windsurf | `.windsurf/skills/living-docs-update/SKILL.md` |
| Generic | `docs/UPDATE_INSTRUCTIONS.md` |

## Provenance

Every generated markdown file should identify the generating skill.

- Frontmatter files: include `generated_by` as the first field.
- Non-frontmatter files: use an HTML comment at the top.
