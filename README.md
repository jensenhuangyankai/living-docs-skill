# Living Docs Skills

Focused skills for bootstrapping, navigating, and maintaining source-linked
living documentation.

## Skills

| Skill | Purpose |
|-------|---------|
| `living-docs` | One-install umbrella skill for bootstrap, navigate, and update workflows |
| `living-docs-bootstrap` | Create the initial `docs/` system for a repository |
| `living-docs-update` | Update affected docs after code changes |
| `living-docs-navigator` | Load only the docs relevant to a task |

## Install

Recommended single install:

```bash
npx skills add https://github.com/jensenhuangyankai/living-docs-skill --skill living-docs
```

Install the whole focused suite:

```bash
npx skills add https://github.com/jensenhuangyankai/living-docs-skill --skill '*'
```

Install individual focused skills:

```bash
npx skills add https://github.com/jensenhuangyankai/living-docs-skill --skill living-docs-bootstrap
npx skills add https://github.com/jensenhuangyankai/living-docs-skill --skill living-docs-update
npx skills add https://github.com/jensenhuangyankai/living-docs-skill --skill living-docs-navigator
```

## Why This Split

The original single skill mixed setup, maintenance, and navigation into one
workflow. This repo now keeps those concerns separate so agents can load only
the instructions they actually need.
