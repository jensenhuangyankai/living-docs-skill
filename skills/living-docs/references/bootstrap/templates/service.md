# Service Doc Template

```markdown
---
generated_by: codex (living-docs skill)
title: <Service Name> Service
status: stable
source_files:
  service:
    - <glob>
depends_on:
  - architecture/system-overview
last_updated: YYYY-MM-DD
---

# <Service Name> Service

> One-line summary of the service's role.

## Overview

[What the service does and where it fits.]

## Architecture

\`\`\`mermaid
flowchart TD
    Entry["Entry"] --> Logic["Business Logic"] --> Data["Data"]
\`\`\`

## Key Modules

| Module | Path | Responsibility |
|--------|------|----------------|
| <module> | `<path>` | <responsibility> |

## Configuration

| Variable | Required | Purpose |
|----------|----------|---------|
| `<ENV_VAR>` | Yes | <purpose> |
```
