# Feature Doc Template

```markdown
---
generated_by: codex (living-docs skill)
title: <Feature Name>
status: stable
source_files:
  app:
    - <glob>
  data:
    - <glob>
depends_on:
  - architecture/system-overview
last_updated: YYYY-MM-DD
---

# <Feature Name>

> One-line summary of the feature and who uses it.

## Overview

[Explain the problem, scope boundaries, and user value.]

## Architecture

\`\`\`mermaid
flowchart LR
    UI["UI"] --> Logic["Logic"] --> Data["Data"]
\`\`\`

## Data Model

[Only include entities that matter to this feature.]

## Key Flows

\`\`\`mermaid
sequenceDiagram
    actor User
    participant App
    participant Data
    User->>App: Action
    App->>Data: Read or write
    Data-->>App: Result
\`\`\`

## Configuration

- feature flags
- roles and permissions
- external dependencies

## Related

- [../../architecture/system-overview.md](../../architecture/system-overview.md)
```
