# Document Tree Rules

Use the smallest tree that still captures the system honestly.

## Standard Shape

```text
docs/
  DESIGN.md
  CHANGELOG.md
  BUILD_ORDER.md                # optional
  architecture/
  services/                     # skip for simple monoliths
  features/
  ui/                           # skip for non-UI repos
```

## Include Rules

- Always create `docs/DESIGN.md`.
- Always create `docs/CHANGELOG.md`.
- Create `architecture/system-overview.md` for every repository.
- Add `architecture/data-model.md` only when the project has meaningful data
  persistence.
- Add `architecture/deployment.md` only when deploy/runtime concerns matter.
- Add `architecture/auth-and-security.md` only when auth or permission logic
  exists.
- Create `services/*.md` only when the repo has clearly separable deployable
  services.
- Create `features/<feature>/design.md` only for major feature areas.
- Create `ui/pages.md` and `ui/components.md` only for UI repos.

## Naming Rules

- Use stable nouns based on the codebase, not speculative future names.
- Keep feature directory names short and path-safe.
- Match document names to the repository's language where possible.
