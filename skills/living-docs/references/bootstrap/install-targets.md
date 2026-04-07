# Install Targets

Use these locations when leaving behind a reusable maintenance path.

## Preferred Option

Install the `living-docs` skill in the target environment when the environment
supports installable skills.

## Fallback Paths

| Environment | Install Path |
|-------------|--------------|
| Cursor | `.cursor/skills/living-docs/SKILL.md` |
| Claude Code | `AGENTS.md` or `.claude/skills/living-docs/SKILL.md` |
| Codex | `.agents/skills/living-docs/SKILL.md` |
| Windsurf | `.windsurf/skills/living-docs/SKILL.md` |
| Generic | `docs/UPDATE_INSTRUCTIONS.md` |

## Provenance

Every generated markdown file should identify the generating skill.

- Frontmatter files: include `generated_by` as the first field.
- Non-frontmatter files: use an HTML comment at the top.
