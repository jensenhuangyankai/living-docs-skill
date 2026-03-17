# DESIGN.md Template

```markdown
---
generated_by: codex (living-docs-bootstrap skill)
title: <Project Name> Living Design
status: stable
last_updated: YYYY-MM-DD
---

# <Project Name>

> One-line description of what the project does and who it serves.

## Project Identity

[2-3 paragraphs on purpose, users, scope, and core workflow.]

## Architecture Summary

\`\`\`mermaid
flowchart LR
    UI["UI / Client"] --> API["API / App"]
    API --> Data["Data Store"]
\`\`\`

| Area | Tech | Role |
|------|------|------|
| UI | <tech> | <role> |
| API | <tech> | <role> |
| Data | <tech> | <role> |

## Tech Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Frontend | <tech> | <version> |
| Backend | <tech> | <version> |

## Feature Index

| Feature | Summary | Doc |
|---------|---------|-----|
| <feature> | <summary> | [design.md](features/<feature>/design.md) |

## Document Map

| Document | Purpose |
|----------|---------|
| [architecture/system-overview.md](architecture/system-overview.md) | Cross-cutting system view |
| [features/<feature>/design.md](features/<feature>/design.md) | Feature design |
```
