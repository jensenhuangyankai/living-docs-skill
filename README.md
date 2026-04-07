# Living Docs Skill

One skill for bootstrapping, navigating, and maintaining source-linked living
documentation.

## Install

```bash
npx skills add https://github.com/jensenhuangyankai/living-docs-skill --skill living-docs
```

## What It Does

The `living-docs` skill infers the mode from the request and the repository:

- bootstrap living docs in a repo that does not have them yet
- navigate existing docs without loading the whole tree
- update docs after code changes

You do not need separate installs for bootstrap, navigation, or updates. Those
playbooks live inside the single `living-docs` skill as internal references.
